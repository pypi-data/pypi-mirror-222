# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsearch.cps.apis.public.api_client import ApiClient
from deepsearch.cps.apis.public.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TasksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def abort_project_task(self, proj_key, task_id, **kwargs):  # noqa: E501
        """abort_project_task  # noqa: E501

        Abort a task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_project_task(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.abort_project_task_with_http_info(proj_key, task_id, **kwargs)  # noqa: E501

    def abort_project_task_with_http_info(self, proj_key, task_id, **kwargs):  # noqa: E501
        """abort_project_task  # noqa: E501

        Abort a task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_project_task_with_http_info(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'task_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method abort_project_task" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `abort_project_task`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `abort_project_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/tasks/{task_id}/actions/abort', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_celery_task(self, proj_key, task_id, **kwargs):  # noqa: E501
        """get_project_celery_task  # noqa: E501

        Get a celery task for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_celery_task(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CeleryTaskPromise
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_project_celery_task_with_http_info(proj_key, task_id, **kwargs)  # noqa: E501

    def get_project_celery_task_with_http_info(self, proj_key, task_id, **kwargs):  # noqa: E501
        """get_project_celery_task  # noqa: E501

        Get a celery task for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_celery_task_with_http_info(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CeleryTaskPromise, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'task_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_celery_task" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `get_project_celery_task`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `get_project_celery_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/celery_tasks/{task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CeleryTaskPromise',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_task(self, proj_key, task_id, **kwargs):  # noqa: E501
        """get_project_task  # noqa: E501

        Get a task for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_task(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ProjectTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_project_task_with_http_info(proj_key, task_id, **kwargs)  # noqa: E501

    def get_project_task_with_http_info(self, proj_key, task_id, **kwargs):  # noqa: E501
        """get_project_task  # noqa: E501

        Get a task for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_task_with_http_info(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ProjectTask, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'task_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_task" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `get_project_task`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `get_project_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer', 'KGAuth']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/tasks/{task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_failure_celery_tasks(self, proj_key, task_id, **kwargs):  # noqa: E501
        """list_failure_celery_tasks  # noqa: E501

        Get celery tasks that failed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_failure_celery_tasks(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CeleryTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_failure_celery_tasks_with_http_info(proj_key, task_id, **kwargs)  # noqa: E501

    def list_failure_celery_tasks_with_http_info(self, proj_key, task_id, **kwargs):  # noqa: E501
        """list_failure_celery_tasks  # noqa: E501

        Get celery tasks that failed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_failure_celery_tasks_with_http_info(proj_key, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CeleryTask], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'task_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_failure_celery_tasks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `list_failure_celery_tasks`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `list_failure_celery_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'proj_key' in local_var_params and local_var_params['proj_key'] is not None:  # noqa: E501
            query_params.append(('proj_key', local_var_params['proj_key']))  # noqa: E501
        if 'task_id' in local_var_params and local_var_params['task_id'] is not None:  # noqa: E501
            query_params.append(('task_id', local_var_params['task_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/system/celery_tasks/failure', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CeleryTask]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_project_tasks(self, proj_key, **kwargs):  # noqa: E501
        """list_project_tasks  # noqa: E501

        List tasks for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_tasks(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_type:
        :param int limit:
        :param int skip:
        :param str sort_by:
        :param str sort_order:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ProjectTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_project_tasks_with_http_info(proj_key, **kwargs)  # noqa: E501

    def list_project_tasks_with_http_info(self, proj_key, **kwargs):  # noqa: E501
        """list_project_tasks  # noqa: E501

        List tasks for a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_tasks_with_http_info(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str task_type:
        :param int limit:
        :param int skip:
        :param str sort_by:
        :param str sort_order:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ProjectTask], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'task_type',
            'limit',
            'skip',
            'sort_by',
            'sort_order'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_project_tasks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `list_project_tasks`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_project_tasks`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'skip' in local_var_params and local_var_params['skip'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip` when calling `list_project_tasks`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []
        if 'task_type' in local_var_params and local_var_params['task_type'] is not None:  # noqa: E501
            query_params.append(('task_type', local_var_params['task_type']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'skip' in local_var_params and local_var_params['skip'] is not None:  # noqa: E501
            query_params.append(('skip', local_var_params['skip']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sort_by', local_var_params['sort_by']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sort_order', local_var_params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProjectTask]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_system_celery_tasks(self, **kwargs):  # noqa: E501
        """list_system_celery_tasks  # noqa: E501

        Get the status of Celery tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_system_celery_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key:
        :param str project_task_id:
        :param float started_since: If set, return the tasks created at or after this timestamp. Otherwise, return the tasks created up to 60 minutes of the system's date, if `project_task_id` is not set.
        :param float task_status:
        :param int limit:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CeleryTask1]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_system_celery_tasks_with_http_info(**kwargs)  # noqa: E501

    def list_system_celery_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """list_system_celery_tasks  # noqa: E501

        Get the status of Celery tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_system_celery_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key:
        :param str project_task_id:
        :param float started_since: If set, return the tasks created at or after this timestamp. Otherwise, return the tasks created up to 60 minutes of the system's date, if `project_task_id` is not set.
        :param float task_status:
        :param int limit:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CeleryTask1], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'project_task_id',
            'started_since',
            'task_status',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_system_celery_tasks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'proj_key' in local_var_params and local_var_params['proj_key'] is not None:  # noqa: E501
            query_params.append(('proj_key', local_var_params['proj_key']))  # noqa: E501
        if 'project_task_id' in local_var_params and local_var_params['project_task_id'] is not None:  # noqa: E501
            query_params.append(('project_task_id', local_var_params['project_task_id']))  # noqa: E501
        if 'started_since' in local_var_params and local_var_params['started_since'] is not None:  # noqa: E501
            query_params.append(('started_since', local_var_params['started_since']))  # noqa: E501
        if 'task_status' in local_var_params and local_var_params['task_status'] is not None:  # noqa: E501
            query_params.append(('task_status', local_var_params['task_status']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/system/celery_tasks/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CeleryTask1]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
