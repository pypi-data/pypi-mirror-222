# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import contextlib

from urllib import request

from django.conf import settings
from oslo_serialization import jsonutils

from heatclient import client as heat_client
from heatclient.common import template_format
from heatclient.common import template_utils
from heatclient.common import utils as heat_utils
from horizon import exceptions
from horizon.utils import functions as utils
from horizon.utils.memoized import memoized
from openstack_dashboard.api import base
from openstack_dashboard.contrib.developer.profiler import api as profiler


def format_parameters(params):
    parameters = {}
    for count, p in enumerate(params, 1):
        parameters['Parameters.member.%d.ParameterKey' % count] = p
        parameters['Parameters.member.%d.ParameterValue' % count] = params[p]
    return parameters


@memoized
def heatclient(request, password=None):
    api_version = "1"
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    cacert = getattr(settings, 'OPENSTACK_SSL_CACERT', None)
    endpoint = base.url_for(request, 'orchestration')
    kwargs = {
        'token': request.user.token.id,
        'insecure': insecure,
        'ca_file': cacert,
        'username': request.user.username,
        'password': password
        # 'timeout': args.timeout,
        # 'ca_file': args.ca_file,
        # 'cert_file': args.cert_file,
        # 'key_file': args.key_file,
    }
    client = heat_client.Client(api_version, endpoint, **kwargs)
    client.format_parameters = format_parameters
    return client


@profiler.trace
def stacks_list(request, marker=None, sort_dir='desc', sort_key='created_at',
                paginate=False, filters=None):
    limit = getattr(settings, 'API_RESULT_LIMIT', 1000)
    page_size = utils.get_page_size(request)

    if paginate:
        request_size = page_size + 1
    else:
        request_size = limit

    kwargs = {'sort_dir': sort_dir, 'sort_key': sort_key}
    if marker:
        kwargs['marker'] = marker

    if filters:
        kwargs.update(filters)
        if 'status' in kwargs:
            kwargs['status'] = kwargs['status'].replace(' ', '_').upper()

    stacks_iter = heatclient(request).stacks.list(limit=request_size,
                                                  **kwargs)

    has_prev_data = False
    has_more_data = False
    stacks = list(stacks_iter)

    if paginate:
        if len(stacks) > page_size:
            stacks.pop()
            has_more_data = True
            if marker is not None:
                has_prev_data = True
        elif sort_dir == 'asc' and marker is not None:
            has_more_data = True
        elif marker is not None:
            has_prev_data = True
    return (stacks, has_more_data, has_prev_data)


def _ignore_if(key, value):
    if key != 'get_file' and key != 'type':
        return True
    if not isinstance(value, str):
        return True
    if (key == 'type' and not value.endswith(('.yaml', '.template'))):
        return True
    return False


@profiler.trace
def get_template_files(template_data=None, template_url=None, files=None):
    if template_data:
        tpl = template_data
    elif template_url:
        with contextlib.closing(request.urlopen(template_url)) as u:
            tpl = u.read()
    else:
        return {}, None
    if not tpl:
        return {}, None
    if isinstance(tpl, bytes):
        tpl = tpl.decode('utf-8')
    template = template_format.parse(tpl)
    if files is None:
        files = {}
    _get_file_contents(template, files)
    return files, template


def _get_file_contents(from_data, files):
    if not isinstance(from_data, (dict, list)):
        return
    if isinstance(from_data, dict):
        recurse_data = from_data.values()
        for key, value in from_data.items():
            if _ignore_if(key, value):
                continue
            if value in files:
                continue
            if not value.startswith(('http://', 'https://')):
                raise exceptions.GetFileError(value, 'get_file')
            if value not in files:
                file_content = heat_utils.read_url_content(value)
                if template_utils.is_template(file_content):
                    template = get_template_files(template_url=value)[1]
                    file_content = jsonutils.dumps(template)
                files[value] = file_content
    else:
        recurse_data = from_data
    for value in recurse_data:
        _get_file_contents(value, files)


@profiler.trace
def stack_delete(request, stack_id):
    return heatclient(request).stacks.delete(stack_id)


@profiler.trace
def stack_get(request, stack_id):
    return heatclient(request).stacks.get(stack_id)


@profiler.trace
def template_get(request, stack_id):
    return heatclient(request).stacks.template(stack_id)


@profiler.trace
def stack_create(request, password=None, **kwargs):
    return heatclient(request, password).stacks.create(**kwargs)


@profiler.trace
def stack_preview(request, password=None, **kwargs):
    return heatclient(request, password).stacks.preview(**kwargs)


@profiler.trace
def stack_update(request, stack_id, password=None, **kwargs):
    return heatclient(request, password).stacks.update(stack_id, **kwargs)


@profiler.trace
def snapshot_create(request, stack_id):
    return heatclient(request).stacks.snapshot(stack_id)


@profiler.trace
def snapshot_list(request, stack_id):
    return heatclient(request).stacks.snapshot_list(stack_id)


@profiler.trace
def snapshot_show(request, stack_id, snapshot_id):
    return heatclient(request).stacks.snapshot_show(stack_id, snapshot_id)


@profiler.trace
def snapshot_delete(request, stack_id, snapshot_id):
    return heatclient(request).stacks.snapshot_delete(stack_id, snapshot_id)


@profiler.trace
def events_list(request, stack_name, marker=None, sort_dir='desc',
                sort_key='event_time', paginate=False, filters=None):
    limit = getattr(settings, 'API_RESULT_LIMIT', 1000)
    page_size = utils.get_page_size(request)

    if paginate:
        request_size = page_size + 1
    else:
        request_size = limit
    kwargs = {'sort_dir': sort_dir, 'sort_key': sort_key}
    if marker:
        kwargs['marker'] = marker

    if filters:
        kwargs.update(filters)

    events_iter = heatclient(request).events.list(stack_name,
                                                  limit=request_size,
                                                  **kwargs)

    has_prev_data = False
    has_more_data = False
    events = list(events_iter)
    if paginate:
        if len(events) > page_size:
            events.pop()
            has_more_data = True
            if marker is not None:
                has_prev_data = True
        elif sort_dir == 'asc' and marker is not None:
            has_more_data = True
        elif marker is not None:
            has_prev_data = True
    return events, has_more_data, has_prev_data


@profiler.trace
def resources_list(request, stack_name):
    return heatclient(request).resources.list(stack_name)


@profiler.trace
def resource_get(request, stack_id, resource_name):
    return heatclient(request).resources.get(stack_id, resource_name)


@profiler.trace
def resource_metadata_get(request, stack_id, resource_name):
    return heatclient(request).resources.metadata(stack_id, resource_name)


@profiler.trace
def template_validate(request, **kwargs):
    return heatclient(request).stacks.validate(**kwargs)


@profiler.trace
def action_check(request, stack_id):
    return heatclient(request).actions.check(stack_id)


@profiler.trace
def action_suspend(request, stack_id):
    return heatclient(request).actions.suspend(stack_id)


@profiler.trace
def action_resume(request, stack_id):
    return heatclient(request).actions.resume(stack_id)


@profiler.trace
def resource_types_list(request, filters=None):
    return heatclient(request).resource_types.list(filters=filters)


@profiler.trace
def resource_type_get(request, resource_type):
    return heatclient(request).resource_types.get(resource_type)


@profiler.trace
def service_list(request):
    return heatclient(request).services.list()


@profiler.trace
def template_version_list(request):
    return heatclient(request).template_versions.list()


@profiler.trace
def template_function_list(request, template_version):
    return heatclient(request).template_versions.get(template_version)
