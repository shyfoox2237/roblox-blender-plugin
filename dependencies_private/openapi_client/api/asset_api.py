# coding: utf-8

"""
    assets-upload-api

    An autogenerated client for the assets-upload-api.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AssetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def asset_create(self, file_content, **kwargs):  # noqa: E501
        """asset_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.asset_create(file_content, async_req=True)
        >>> result = thread.get()

        :param file_content: (required)
        :type file_content: file
        :param request:
        :type request: AssetCreateRequestRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RobloxLongrunningOperation
        """
        kwargs['_return_http_data_only'] = True
        return self.asset_create_with_http_info(file_content, **kwargs)  # noqa: E501

    def asset_create_with_http_info(self, file_content, **kwargs):  # noqa: E501
        """asset_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.asset_create_with_http_info(file_content, async_req=True)
        >>> result = thread.get()

        :param file_content: (required)
        :type file_content: file
        :param request:
        :type request: AssetCreateRequestRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(RobloxLongrunningOperation, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'file_content',
            'request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'file_content' is set
        if self.api_client.client_side_validation and local_var_params.get('file_content') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_content` when calling `asset_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}
        if 'request' in local_var_params:
            form_params.append(('request', local_var_params['request']))  # noqa: E501
        if 'file_content' in local_var_params:
            local_var_files['fileContent'] = local_var_params['file_content']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "RobloxLongrunningOperation",
            400: "MicrosoftAspNetCoreMvcProblemDetails",
            401: "MicrosoftAspNetCoreMvcProblemDetails",
            403: "MicrosoftAspNetCoreMvcProblemDetails",
        }

        return self.api_client.call_api(
            '/v1/assets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def asset_update(self, asset_id, file_content, **kwargs):  # noqa: E501
        """asset_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.asset_update(asset_id, file_content, async_req=True)
        >>> result = thread.get()

        :param asset_id: (required)
        :type asset_id: int
        :param file_content: (required)
        :type file_content: file
        :param request:
        :type request: AssetCreateRequestRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RobloxLongrunningOperation
        """
        kwargs['_return_http_data_only'] = True
        return self.asset_update_with_http_info(asset_id, file_content, **kwargs)  # noqa: E501

    def asset_update_with_http_info(self, asset_id, file_content, **kwargs):  # noqa: E501
        """asset_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.asset_update_with_http_info(asset_id, file_content, async_req=True)
        >>> result = thread.get()

        :param asset_id: (required)
        :type asset_id: int
        :param file_content: (required)
        :type file_content: file
        :param request:
        :type request: AssetCreateRequestRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(RobloxLongrunningOperation, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'asset_id',
            'file_content',
            'request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method asset_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'asset_id' is set
        if self.api_client.client_side_validation and local_var_params.get('asset_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `asset_id` when calling `asset_update`")  # noqa: E501
        # verify the required parameter 'file_content' is set
        if self.api_client.client_side_validation and local_var_params.get('file_content') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_content` when calling `asset_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['assetId'] = local_var_params['asset_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}
        if 'request' in local_var_params:
            form_params.append(('request', local_var_params['request']))  # noqa: E501
        if 'file_content' in local_var_params:
            local_var_files['fileContent'] = local_var_params['file_content']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data'],
                'PATCH', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "RobloxLongrunningOperation",
            400: "MicrosoftAspNetCoreMvcProblemDetails",
            401: "MicrosoftAspNetCoreMvcProblemDetails",
            403: "MicrosoftAspNetCoreMvcProblemDetails",
        }

        return self.api_client.call_api(
            '/v1/assets/{assetId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
