# coding: utf-8

"""
    assets-upload-api

    An autogenerated client for the assets-upload-api.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'asset_info': 'RobloxOperationscoreOperationserviceV1Beta1AssetInfo',
        'metadata': 'GoogleProtobufWellKnownTypesAny'
    }

    attribute_map = {
        'asset_info': 'assetInfo',
        'metadata': 'metadata'
    }

    def __init__(self, asset_info=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._asset_info = None
        self._metadata = None
        self.discriminator = None

        if asset_info is not None:
            self.asset_info = asset_info
        if metadata is not None:
            self.metadata = metadata

    @property
    def asset_info(self):
        """Gets the asset_info of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501


        :return: The asset_info of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501
        :rtype: RobloxOperationscoreOperationserviceV1Beta1AssetInfo
        """
        return self._asset_info

    @asset_info.setter
    def asset_info(self, asset_info):
        """Sets the asset_info of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.


        :param asset_info: The asset_info of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501
        :type asset_info: RobloxOperationscoreOperationserviceV1Beta1AssetInfo
        """

        self._asset_info = asset_info

    @property
    def metadata(self):
        """Gets the metadata of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501


        :return: The metadata of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501
        :rtype: GoogleProtobufWellKnownTypesAny
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.


        :param metadata: The metadata of this RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult.  # noqa: E501
        :type metadata: GoogleProtobufWellKnownTypesAny
        """

        self._metadata = metadata

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RobloxOperationscoreOperationserviceV1Beta1PublicAssetCreationResult):
            return True

        return self.to_dict() != other.to_dict()