"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs/)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import FileConfigurationTypeDef

    data: FileConfigurationTypeDef = ...
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence, Union

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "FileConfigurationTypeDef",
    "ScheduleConfigurationTypeDef",
    "FileConfigurationOutputTypeDef",
    "ResponseMetadataTypeDef",
    "EventFilterTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteDataIntegrationRequestRequestTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventIntegrationAssociationTypeDef",
    "GetDataIntegrationRequestRequestTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    "ListDataIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataIntegrationRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
    "CreateDataIntegrationRequestRequestTypeDef",
    "FileConfigurationUnionTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateEventIntegrationRequestRequestTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsResponseTypeDef",
)

_RequiredFileConfigurationTypeDef = TypedDict(
    "_RequiredFileConfigurationTypeDef",
    {
        "Folders": Sequence[str],
    },
)
_OptionalFileConfigurationTypeDef = TypedDict(
    "_OptionalFileConfigurationTypeDef",
    {
        "Filters": Mapping[str, Sequence[str]],
    },
    total=False,
)

class FileConfigurationTypeDef(
    _RequiredFileConfigurationTypeDef, _OptionalFileConfigurationTypeDef
):
    pass

_RequiredScheduleConfigurationTypeDef = TypedDict(
    "_RequiredScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalScheduleConfigurationTypeDef = TypedDict(
    "_OptionalScheduleConfigurationTypeDef",
    {
        "FirstExecutionFrom": str,
        "Object": str,
    },
    total=False,
)

class ScheduleConfigurationTypeDef(
    _RequiredScheduleConfigurationTypeDef, _OptionalScheduleConfigurationTypeDef
):
    pass

_RequiredFileConfigurationOutputTypeDef = TypedDict(
    "_RequiredFileConfigurationOutputTypeDef",
    {
        "Folders": List[str],
    },
)
_OptionalFileConfigurationOutputTypeDef = TypedDict(
    "_OptionalFileConfigurationOutputTypeDef",
    {
        "Filters": Dict[str, List[str]],
    },
    total=False,
)

class FileConfigurationOutputTypeDef(
    _RequiredFileConfigurationOutputTypeDef, _OptionalFileConfigurationOutputTypeDef
):
    pass

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

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

DataIntegrationAssociationSummaryTypeDef = TypedDict(
    "DataIntegrationAssociationSummaryTypeDef",
    {
        "DataIntegrationAssociationArn": str,
        "DataIntegrationArn": str,
        "ClientId": str,
    },
    total=False,
)

DataIntegrationSummaryTypeDef = TypedDict(
    "DataIntegrationSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "SourceURI": str,
    },
    total=False,
)

DeleteDataIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteDataIntegrationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)

DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": str,
        "EventIntegrationAssociationId": str,
        "EventIntegrationName": str,
        "ClientId": str,
        "EventBridgeRuleName": str,
        "ClientAssociationMetadata": Dict[str, str],
    },
    total=False,
)

GetDataIntegrationRequestRequestTypeDef = TypedDict(
    "GetDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)
_OptionalListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDataIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListDataIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListDataIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListDataIntegrationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
    },
)
_OptionalListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEventIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListEventIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListEventIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateDataIntegrationRequestRequestTypeDef(
    _RequiredUpdateDataIntegrationRequestRequestTypeDef,
    _OptionalUpdateDataIntegrationRequestRequestTypeDef,
):
    pass

_RequiredUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateEventIntegrationRequestRequestTypeDef(
    _RequiredUpdateEventIntegrationRequestRequestTypeDef,
    _OptionalUpdateEventIntegrationRequestRequestTypeDef,
):
    pass

_RequiredCreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfig": ScheduleConfigurationTypeDef,
    },
)
_OptionalCreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataIntegrationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Mapping[str, str],
        "ClientToken": str,
        "FileConfiguration": FileConfigurationTypeDef,
        "ObjectConfiguration": Mapping[str, Mapping[str, Sequence[str]]],
    },
    total=False,
)

class CreateDataIntegrationRequestRequestTypeDef(
    _RequiredCreateDataIntegrationRequestRequestTypeDef,
    _OptionalCreateDataIntegrationRequestRequestTypeDef,
):
    pass

FileConfigurationUnionTypeDef = Union[FileConfigurationTypeDef, FileConfigurationOutputTypeDef]
CreateDataIntegrationResponseTypeDef = TypedDict(
    "CreateDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "ClientToken": str,
        "FileConfiguration": FileConfigurationOutputTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDataIntegrationResponseTypeDef = TypedDict(
    "GetDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "Tags": Dict[str, str],
        "FileConfiguration": FileConfigurationOutputTypeDef,
        "ObjectConfiguration": Dict[str, Dict[str, List[str]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": EventFilterTypeDef,
        "EventBridgeBus": str,
    },
)
_OptionalCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateEventIntegrationRequestRequestTypeDef(
    _RequiredCreateEventIntegrationRequestRequestTypeDef,
    _OptionalCreateEventIntegrationRequestRequestTypeDef,
):
    pass

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": str,
        "Name": str,
        "Description": str,
        "EventFilter": EventFilterTypeDef,
        "EventBridgeBus": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": EventFilterTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDataIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListDataIntegrationAssociationsResponseTypeDef",
    {
        "DataIntegrationAssociations": List[DataIntegrationAssociationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDataIntegrationsResponseTypeDef = TypedDict(
    "ListDataIntegrationsResponseTypeDef",
    {
        "DataIntegrations": List[DataIntegrationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List[EventIntegrationAssociationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List[EventIntegrationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
