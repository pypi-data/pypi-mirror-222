"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""
import sys
from datetime import datetime
from typing import Dict, Mapping, Union

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "GenerateDataSetRequestRequestTypeDef",
    "StartSupportDataExportRequestRequestTypeDef",
    "GenerateDataSetResultTypeDef",
    "StartSupportDataExportResultTypeDef",
)

TimestampTypeDef = Union[datetime, str]
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

_RequiredGenerateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataSetRequestRequestTypeDef",
    {
        "dataSetType": DataSetTypeType,
        "dataSetPublicationDate": TimestampTypeDef,
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalGenerateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataSetRequestRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Mapping[str, str],
    },
    total=False,
)


class GenerateDataSetRequestRequestTypeDef(
    _RequiredGenerateDataSetRequestRequestTypeDef, _OptionalGenerateDataSetRequestRequestTypeDef
):
    pass


_RequiredStartSupportDataExportRequestRequestTypeDef = TypedDict(
    "_RequiredStartSupportDataExportRequestRequestTypeDef",
    {
        "dataSetType": SupportDataSetTypeType,
        "fromDate": TimestampTypeDef,
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalStartSupportDataExportRequestRequestTypeDef = TypedDict(
    "_OptionalStartSupportDataExportRequestRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Mapping[str, str],
    },
    total=False,
)


class StartSupportDataExportRequestRequestTypeDef(
    _RequiredStartSupportDataExportRequestRequestTypeDef,
    _OptionalStartSupportDataExportRequestRequestTypeDef,
):
    pass


GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
