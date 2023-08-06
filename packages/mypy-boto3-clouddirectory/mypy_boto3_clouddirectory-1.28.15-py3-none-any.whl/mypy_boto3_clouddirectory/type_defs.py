"""
Type annotations for clouddirectory service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_clouddirectory/type_defs/)

Usage::

    ```python
    from mypy_boto3_clouddirectory.type_defs import ObjectReferenceTypeDef

    data: ObjectReferenceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BatchReadExceptionTypeType,
    ConsistencyLevelType,
    DirectoryStateType,
    FacetAttributeTypeType,
    FacetStyleType,
    ObjectTypeType,
    RangeModeType,
    RequiredAttributeBehaviorType,
    RuleTypeType,
    UpdateActionTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ObjectReferenceTypeDef",
    "SchemaFacetTypeDef",
    "ApplySchemaRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TypedLinkSchemaAndFacetNameTypeDef",
    "AttributeKeyTypeDef",
    "TypedAttributeValueOutputTypeDef",
    "TypedAttributeValueTypeDef",
    "BatchAttachObjectResponseTypeDef",
    "BatchAttachToIndexResponseTypeDef",
    "BatchCreateIndexResponseTypeDef",
    "BatchCreateObjectResponseTypeDef",
    "BatchDetachFromIndexResponseTypeDef",
    "BatchDetachObjectResponseTypeDef",
    "BatchListObjectChildrenResponseTypeDef",
    "PathToObjectIdentifiersTypeDef",
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    "BatchListObjectPoliciesResponseTypeDef",
    "BatchListPolicyAttachmentsResponseTypeDef",
    "BatchReadExceptionTypeDef",
    "BatchUpdateObjectAttributesResponseTypeDef",
    "CreateDirectoryRequestRequestTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "DeleteDirectoryRequestRequestTypeDef",
    "DeleteFacetRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    "DirectoryTypeDef",
    "DisableDirectoryRequestRequestTypeDef",
    "EnableDirectoryRequestRequestTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "FacetAttributeReferenceTypeDef",
    "FacetTypeDef",
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    "GetDirectoryRequestRequestTypeDef",
    "GetFacetRequestRequestTypeDef",
    "GetSchemaAsJsonRequestRequestTypeDef",
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAppliedSchemaArnsRequestRequestTypeDef",
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    "ListDirectoriesRequestRequestTypeDef",
    "ListFacetAttributesRequestRequestTypeDef",
    "ListFacetNamesRequestRequestTypeDef",
    "ListManagedSchemaArnsRequestRequestTypeDef",
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTypedLinkFacetAttributesRequestRequestTypeDef",
    "ListTypedLinkFacetNamesRequestRequestTypeDef",
    "PolicyAttachmentTypeDef",
    "PublishSchemaRequestRequestTypeDef",
    "PutSchemaFromJsonRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpgradeAppliedSchemaRequestRequestTypeDef",
    "UpgradePublishedSchemaRequestRequestTypeDef",
    "AttachObjectRequestRequestTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "AttachToIndexRequestRequestTypeDef",
    "BatchAttachObjectTypeDef",
    "BatchAttachPolicyTypeDef",
    "BatchAttachToIndexTypeDef",
    "BatchDeleteObjectTypeDef",
    "BatchDetachFromIndexTypeDef",
    "BatchDetachObjectTypeDef",
    "BatchDetachPolicyTypeDef",
    "BatchGetObjectInformationTypeDef",
    "BatchListAttachedIndicesTypeDef",
    "BatchListObjectChildrenTypeDef",
    "BatchListObjectParentPathsTypeDef",
    "BatchListObjectParentsTypeDef",
    "BatchListObjectPoliciesTypeDef",
    "BatchListPolicyAttachmentsTypeDef",
    "BatchLookupPolicyTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DetachFromIndexRequestRequestTypeDef",
    "DetachObjectRequestRequestTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "GetObjectInformationRequestRequestTypeDef",
    "ListAttachedIndicesRequestRequestTypeDef",
    "ListObjectChildrenRequestRequestTypeDef",
    "ListObjectParentPathsRequestRequestTypeDef",
    "ListObjectParentsRequestRequestTypeDef",
    "ListObjectPoliciesRequestRequestTypeDef",
    "ListPolicyAttachmentsRequestRequestTypeDef",
    "LookupPolicyRequestRequestTypeDef",
    "BatchGetObjectAttributesTypeDef",
    "BatchGetObjectInformationResponseTypeDef",
    "BatchListObjectAttributesTypeDef",
    "BatchRemoveFacetFromObjectTypeDef",
    "GetObjectAttributesRequestRequestTypeDef",
    "ListObjectAttributesRequestRequestTypeDef",
    "RemoveFacetFromObjectRequestRequestTypeDef",
    "ApplySchemaResponseTypeDef",
    "AttachObjectResponseTypeDef",
    "AttachToIndexResponseTypeDef",
    "CreateDirectoryResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateObjectResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDirectoryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DetachFromIndexResponseTypeDef",
    "DetachObjectResponseTypeDef",
    "DisableDirectoryResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDirectoryResponseTypeDef",
    "GetAppliedSchemaVersionResponseTypeDef",
    "GetObjectInformationResponseTypeDef",
    "GetSchemaAsJsonResponseTypeDef",
    "GetTypedLinkFacetInformationResponseTypeDef",
    "ListAppliedSchemaArnsResponseTypeDef",
    "ListDevelopmentSchemaArnsResponseTypeDef",
    "ListFacetNamesResponseTypeDef",
    "ListManagedSchemaArnsResponseTypeDef",
    "ListObjectChildrenResponseTypeDef",
    "ListObjectPoliciesResponseTypeDef",
    "ListPolicyAttachmentsResponseTypeDef",
    "ListPublishedSchemaArnsResponseTypeDef",
    "ListTypedLinkFacetNamesResponseTypeDef",
    "PublishSchemaResponseTypeDef",
    "PutSchemaFromJsonResponseTypeDef",
    "UpdateObjectAttributesResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpgradeAppliedSchemaResponseTypeDef",
    "UpgradePublishedSchemaResponseTypeDef",
    "BatchCreateIndexTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "AttributeKeyAndValueOutputTypeDef",
    "AttributeNameAndValueOutputTypeDef",
    "AttributeKeyAndValueTypeDef",
    "AttributeNameAndValueTypeDef",
    "LinkAttributeActionTypeDef",
    "ObjectAttributeActionTypeDef",
    "TypedAttributeValueRangeTypeDef",
    "BatchListObjectParentPathsResponseTypeDef",
    "ListObjectParentPathsResponseTypeDef",
    "BatchListObjectParentsResponseTypeDef",
    "ListObjectParentsResponseTypeDef",
    "GetDirectoryResponseTypeDef",
    "ListDirectoriesResponseTypeDef",
    "FacetAttributeDefinitionOutputTypeDef",
    "TypedLinkAttributeDefinitionOutputTypeDef",
    "FacetAttributeDefinitionTypeDef",
    "TypedLinkAttributeDefinitionTypeDef",
    "GetFacetResponseTypeDef",
    "ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    "ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    "ListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    "ListFacetNamesRequestListFacetNamesPaginateTypeDef",
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    "ListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    "ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    "ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    "ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    "ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    "LookupPolicyRequestLookupPolicyPaginateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "PolicyToPathTypeDef",
    "BatchGetLinkAttributesResponseTypeDef",
    "BatchGetObjectAttributesResponseTypeDef",
    "BatchListObjectAttributesResponseTypeDef",
    "GetLinkAttributesResponseTypeDef",
    "GetObjectAttributesResponseTypeDef",
    "IndexAttachmentTypeDef",
    "ListObjectAttributesResponseTypeDef",
    "TypedLinkSpecifierOutputTypeDef",
    "AddFacetToObjectRequestRequestTypeDef",
    "BatchAddFacetToObjectTypeDef",
    "BatchCreateObjectTypeDef",
    "CreateObjectRequestRequestTypeDef",
    "AttachTypedLinkRequestRequestTypeDef",
    "BatchAttachTypedLinkTypeDef",
    "TypedLinkSpecifierTypeDef",
    "LinkAttributeUpdateTypeDef",
    "ObjectAttributeUpdateTypeDef",
    "ObjectAttributeRangeTypeDef",
    "TypedLinkAttributeRangeTypeDef",
    "FacetAttributeOutputTypeDef",
    "ListTypedLinkFacetAttributesResponseTypeDef",
    "FacetAttributeTypeDef",
    "TypedLinkFacetAttributeUpdateTypeDef",
    "TypedLinkFacetTypeDef",
    "BatchLookupPolicyResponseTypeDef",
    "LookupPolicyResponseTypeDef",
    "BatchListAttachedIndicesResponseTypeDef",
    "BatchListIndexResponseTypeDef",
    "ListAttachedIndicesResponseTypeDef",
    "ListIndexResponseTypeDef",
    "AttachTypedLinkResponseTypeDef",
    "BatchAttachTypedLinkResponseTypeDef",
    "BatchListIncomingTypedLinksResponseTypeDef",
    "BatchListOutgoingTypedLinksResponseTypeDef",
    "ListIncomingTypedLinksResponseTypeDef",
    "ListOutgoingTypedLinksResponseTypeDef",
    "BatchDetachTypedLinkTypeDef",
    "BatchGetLinkAttributesTypeDef",
    "DetachTypedLinkRequestRequestTypeDef",
    "GetLinkAttributesRequestRequestTypeDef",
    "BatchUpdateLinkAttributesTypeDef",
    "UpdateLinkAttributesRequestRequestTypeDef",
    "BatchUpdateObjectAttributesTypeDef",
    "UpdateObjectAttributesRequestRequestTypeDef",
    "BatchListIndexTypeDef",
    "ListIndexRequestListIndexPaginateTypeDef",
    "ListIndexRequestRequestTypeDef",
    "BatchListIncomingTypedLinksTypeDef",
    "BatchListOutgoingTypedLinksTypeDef",
    "ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    "ListIncomingTypedLinksRequestRequestTypeDef",
    "ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    "ListOutgoingTypedLinksRequestRequestTypeDef",
    "ListFacetAttributesResponseTypeDef",
    "CreateFacetRequestRequestTypeDef",
    "FacetAttributeUpdateTypeDef",
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    "CreateTypedLinkFacetRequestRequestTypeDef",
    "BatchWriteOperationResponseTypeDef",
    "BatchReadSuccessfulResponseTypeDef",
    "BatchWriteOperationTypeDef",
    "BatchReadOperationTypeDef",
    "UpdateFacetRequestRequestTypeDef",
    "BatchWriteResponseTypeDef",
    "BatchReadOperationResponseTypeDef",
    "BatchWriteRequestRequestTypeDef",
    "BatchReadRequestRequestTypeDef",
    "BatchReadResponseTypeDef",
)

ObjectReferenceTypeDef = TypedDict(
    "ObjectReferenceTypeDef",
    {
        "Selector": str,
    },
    total=False,
)

SchemaFacetTypeDef = TypedDict(
    "SchemaFacetTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
    },
    total=False,
)

ApplySchemaRequestRequestTypeDef = TypedDict(
    "ApplySchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)

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

TypedLinkSchemaAndFacetNameTypeDef = TypedDict(
    "TypedLinkSchemaAndFacetNameTypeDef",
    {
        "SchemaArn": str,
        "TypedLinkName": str,
    },
)

AttributeKeyTypeDef = TypedDict(
    "AttributeKeyTypeDef",
    {
        "SchemaArn": str,
        "FacetName": str,
        "Name": str,
    },
)

TypedAttributeValueOutputTypeDef = TypedDict(
    "TypedAttributeValueOutputTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)

TypedAttributeValueTypeDef = TypedDict(
    "TypedAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[str, bytes, IO[Any], StreamingBody],
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": Union[datetime, str],
    },
    total=False,
)

BatchAttachObjectResponseTypeDef = TypedDict(
    "BatchAttachObjectResponseTypeDef",
    {
        "attachedObjectIdentifier": str,
    },
    total=False,
)

BatchAttachToIndexResponseTypeDef = TypedDict(
    "BatchAttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
    },
    total=False,
)

BatchCreateIndexResponseTypeDef = TypedDict(
    "BatchCreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchCreateObjectResponseTypeDef = TypedDict(
    "BatchCreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

BatchDetachFromIndexResponseTypeDef = TypedDict(
    "BatchDetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
    },
    total=False,
)

BatchDetachObjectResponseTypeDef = TypedDict(
    "BatchDetachObjectResponseTypeDef",
    {
        "detachedObjectIdentifier": str,
    },
    total=False,
)

BatchListObjectChildrenResponseTypeDef = TypedDict(
    "BatchListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
    },
    total=False,
)

PathToObjectIdentifiersTypeDef = TypedDict(
    "PathToObjectIdentifiersTypeDef",
    {
        "Path": str,
        "ObjectIdentifiers": List[str],
    },
    total=False,
)

ObjectIdentifierAndLinkNameTupleTypeDef = TypedDict(
    "ObjectIdentifierAndLinkNameTupleTypeDef",
    {
        "ObjectIdentifier": str,
        "LinkName": str,
    },
    total=False,
)

BatchListObjectPoliciesResponseTypeDef = TypedDict(
    "BatchListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
    },
    total=False,
)

BatchListPolicyAttachmentsResponseTypeDef = TypedDict(
    "BatchListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
    },
    total=False,
)

BatchReadExceptionTypeDef = TypedDict(
    "BatchReadExceptionTypeDef",
    {
        "Type": BatchReadExceptionTypeType,
        "Message": str,
    },
    total=False,
)

BatchUpdateObjectAttributesResponseTypeDef = TypedDict(
    "BatchUpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
    },
    total=False,
)

CreateDirectoryRequestRequestTypeDef = TypedDict(
    "CreateDirectoryRequestRequestTypeDef",
    {
        "Name": str,
        "SchemaArn": str,
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDirectoryRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

DeleteFacetRequestRequestTypeDef = TypedDict(
    "DeleteFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

DeleteTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "DeleteTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

DirectoryTypeDef = TypedDict(
    "DirectoryTypeDef",
    {
        "Name": str,
        "DirectoryArn": str,
        "State": DirectoryStateType,
        "CreationDateTime": datetime,
    },
    total=False,
)

DisableDirectoryRequestRequestTypeDef = TypedDict(
    "DisableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

EnableDirectoryRequestRequestTypeDef = TypedDict(
    "EnableDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Type": RuleTypeType,
        "Parameters": Dict[str, str],
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Type": RuleTypeType,
        "Parameters": Mapping[str, str],
    },
    total=False,
)

FacetAttributeReferenceTypeDef = TypedDict(
    "FacetAttributeReferenceTypeDef",
    {
        "TargetFacetName": str,
        "TargetAttributeName": str,
    },
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "Name": str,
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)

GetAppliedSchemaVersionRequestRequestTypeDef = TypedDict(
    "GetAppliedSchemaVersionRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetDirectoryRequestRequestTypeDef = TypedDict(
    "GetDirectoryRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)

GetFacetRequestRequestTypeDef = TypedDict(
    "GetFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

GetSchemaAsJsonRequestRequestTypeDef = TypedDict(
    "GetSchemaAsJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)

GetTypedLinkFacetInformationRequestRequestTypeDef = TypedDict(
    "GetTypedLinkFacetInformationRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
    },
)
_OptionalListAppliedSchemaArnsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppliedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAppliedSchemaArnsRequestRequestTypeDef(
    _RequiredListAppliedSchemaArnsRequestRequestTypeDef,
    _OptionalListAppliedSchemaArnsRequestRequestTypeDef,
):
    pass


ListDevelopmentSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDirectoriesRequestRequestTypeDef = TypedDict(
    "ListDirectoriesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "state": DirectoryStateType,
    },
    total=False,
)

_RequiredListFacetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListFacetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListFacetAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFacetAttributesRequestRequestTypeDef(
    _RequiredListFacetAttributesRequestRequestTypeDef,
    _OptionalListFacetAttributesRequestRequestTypeDef,
):
    pass


_RequiredListFacetNamesRequestRequestTypeDef = TypedDict(
    "_RequiredListFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListFacetNamesRequestRequestTypeDef = TypedDict(
    "_OptionalListFacetNamesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFacetNamesRequestRequestTypeDef(
    _RequiredListFacetNamesRequestRequestTypeDef, _OptionalListFacetNamesRequestRequestTypeDef
):
    pass


ListManagedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPublishedSchemaArnsRequestRequestTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListTypedLinkFacetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTypedLinkFacetAttributesRequestRequestTypeDef(
    _RequiredListTypedLinkFacetAttributesRequestRequestTypeDef,
    _OptionalListTypedLinkFacetAttributesRequestRequestTypeDef,
):
    pass


_RequiredListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListTypedLinkFacetNamesRequestRequestTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetNamesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTypedLinkFacetNamesRequestRequestTypeDef(
    _RequiredListTypedLinkFacetNamesRequestRequestTypeDef,
    _OptionalListTypedLinkFacetNamesRequestRequestTypeDef,
):
    pass


PolicyAttachmentTypeDef = TypedDict(
    "PolicyAttachmentTypeDef",
    {
        "PolicyId": str,
        "ObjectIdentifier": str,
        "PolicyType": str,
    },
    total=False,
)

_RequiredPublishSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredPublishSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "Version": str,
    },
)
_OptionalPublishSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalPublishSchemaRequestRequestTypeDef",
    {
        "MinorVersion": str,
        "Name": str,
    },
    total=False,
)


class PublishSchemaRequestRequestTypeDef(
    _RequiredPublishSchemaRequestRequestTypeDef, _OptionalPublishSchemaRequestRequestTypeDef
):
    pass


PutSchemaFromJsonRequestRequestTypeDef = TypedDict(
    "PutSchemaFromJsonRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Document": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)

_RequiredUpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "PublishedSchemaArn": str,
        "DirectoryArn": str,
    },
)
_OptionalUpgradeAppliedSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradeAppliedSchemaRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class UpgradeAppliedSchemaRequestRequestTypeDef(
    _RequiredUpgradeAppliedSchemaRequestRequestTypeDef,
    _OptionalUpgradeAppliedSchemaRequestRequestTypeDef,
):
    pass


_RequiredUpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredUpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DevelopmentSchemaArn": str,
        "PublishedSchemaArn": str,
        "MinorVersion": str,
    },
)
_OptionalUpgradePublishedSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalUpgradePublishedSchemaRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)


class UpgradePublishedSchemaRequestRequestTypeDef(
    _RequiredUpgradePublishedSchemaRequestRequestTypeDef,
    _OptionalUpgradePublishedSchemaRequestRequestTypeDef,
):
    pass


AttachObjectRequestRequestTypeDef = TypedDict(
    "AttachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

AttachToIndexRequestRequestTypeDef = TypedDict(
    "AttachToIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)

BatchAttachObjectTypeDef = TypedDict(
    "BatchAttachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "ChildReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)

BatchAttachPolicyTypeDef = TypedDict(
    "BatchAttachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

BatchAttachToIndexTypeDef = TypedDict(
    "BatchAttachToIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)

BatchDeleteObjectTypeDef = TypedDict(
    "BatchDeleteObjectTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

BatchDetachFromIndexTypeDef = TypedDict(
    "BatchDetachFromIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)

_RequiredBatchDetachObjectTypeDef = TypedDict(
    "_RequiredBatchDetachObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)
_OptionalBatchDetachObjectTypeDef = TypedDict(
    "_OptionalBatchDetachObjectTypeDef",
    {
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchDetachObjectTypeDef(
    _RequiredBatchDetachObjectTypeDef, _OptionalBatchDetachObjectTypeDef
):
    pass


BatchDetachPolicyTypeDef = TypedDict(
    "BatchDetachPolicyTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

BatchGetObjectInformationTypeDef = TypedDict(
    "BatchGetObjectInformationTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

_RequiredBatchListAttachedIndicesTypeDef = TypedDict(
    "_RequiredBatchListAttachedIndicesTypeDef",
    {
        "TargetReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListAttachedIndicesTypeDef = TypedDict(
    "_OptionalBatchListAttachedIndicesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListAttachedIndicesTypeDef(
    _RequiredBatchListAttachedIndicesTypeDef, _OptionalBatchListAttachedIndicesTypeDef
):
    pass


_RequiredBatchListObjectChildrenTypeDef = TypedDict(
    "_RequiredBatchListObjectChildrenTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListObjectChildrenTypeDef = TypedDict(
    "_OptionalBatchListObjectChildrenTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectChildrenTypeDef(
    _RequiredBatchListObjectChildrenTypeDef, _OptionalBatchListObjectChildrenTypeDef
):
    pass


_RequiredBatchListObjectParentPathsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentPathsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListObjectParentPathsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentPathsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectParentPathsTypeDef(
    _RequiredBatchListObjectParentPathsTypeDef, _OptionalBatchListObjectParentPathsTypeDef
):
    pass


_RequiredBatchListObjectParentsTypeDef = TypedDict(
    "_RequiredBatchListObjectParentsTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListObjectParentsTypeDef = TypedDict(
    "_OptionalBatchListObjectParentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectParentsTypeDef(
    _RequiredBatchListObjectParentsTypeDef, _OptionalBatchListObjectParentsTypeDef
):
    pass


_RequiredBatchListObjectPoliciesTypeDef = TypedDict(
    "_RequiredBatchListObjectPoliciesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListObjectPoliciesTypeDef = TypedDict(
    "_OptionalBatchListObjectPoliciesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListObjectPoliciesTypeDef(
    _RequiredBatchListObjectPoliciesTypeDef, _OptionalBatchListObjectPoliciesTypeDef
):
    pass


_RequiredBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_RequiredBatchListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListPolicyAttachmentsTypeDef = TypedDict(
    "_OptionalBatchListPolicyAttachmentsTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListPolicyAttachmentsTypeDef(
    _RequiredBatchListPolicyAttachmentsTypeDef, _OptionalBatchListPolicyAttachmentsTypeDef
):
    pass


_RequiredBatchLookupPolicyTypeDef = TypedDict(
    "_RequiredBatchLookupPolicyTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchLookupPolicyTypeDef = TypedDict(
    "_OptionalBatchLookupPolicyTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchLookupPolicyTypeDef(
    _RequiredBatchLookupPolicyTypeDef, _OptionalBatchLookupPolicyTypeDef
):
    pass


DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

DetachFromIndexRequestRequestTypeDef = TypedDict(
    "DetachFromIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
        "TargetReference": ObjectReferenceTypeDef,
    },
)

DetachObjectRequestRequestTypeDef = TypedDict(
    "DetachObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

_RequiredGetObjectInformationRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectInformationRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalGetObjectInformationRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectInformationRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetObjectInformationRequestRequestTypeDef(
    _RequiredGetObjectInformationRequestRequestTypeDef,
    _OptionalGetObjectInformationRequestRequestTypeDef,
):
    pass


_RequiredListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttachedIndicesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
_OptionalListAttachedIndicesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttachedIndicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListAttachedIndicesRequestRequestTypeDef(
    _RequiredListAttachedIndicesRequestRequestTypeDef,
    _OptionalListAttachedIndicesRequestRequestTypeDef,
):
    pass


_RequiredListObjectChildrenRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectChildrenRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectChildrenRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectChildrenRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListObjectChildrenRequestRequestTypeDef(
    _RequiredListObjectChildrenRequestRequestTypeDef,
    _OptionalListObjectChildrenRequestRequestTypeDef,
):
    pass


_RequiredListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectParentPathsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectParentPathsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectParentPathsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListObjectParentPathsRequestRequestTypeDef(
    _RequiredListObjectParentPathsRequestRequestTypeDef,
    _OptionalListObjectParentPathsRequestRequestTypeDef,
):
    pass


_RequiredListObjectParentsRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectParentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectParentsRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectParentsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "IncludeAllLinksToEachParent": bool,
    },
    total=False,
)


class ListObjectParentsRequestRequestTypeDef(
    _RequiredListObjectParentsRequestRequestTypeDef, _OptionalListObjectParentsRequestRequestTypeDef
):
    pass


_RequiredListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectPoliciesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListObjectPoliciesRequestRequestTypeDef(
    _RequiredListObjectPoliciesRequestRequestTypeDef,
    _OptionalListObjectPoliciesRequestRequestTypeDef,
):
    pass


_RequiredListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListPolicyAttachmentsRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
    },
)
_OptionalListPolicyAttachmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListPolicyAttachmentsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListPolicyAttachmentsRequestRequestTypeDef(
    _RequiredListPolicyAttachmentsRequestRequestTypeDef,
    _OptionalListPolicyAttachmentsRequestRequestTypeDef,
):
    pass


_RequiredLookupPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredLookupPolicyRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalLookupPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalLookupPolicyRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class LookupPolicyRequestRequestTypeDef(
    _RequiredLookupPolicyRequestRequestTypeDef, _OptionalLookupPolicyRequestRequestTypeDef
):
    pass


BatchGetObjectAttributesTypeDef = TypedDict(
    "BatchGetObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
    },
)

BatchGetObjectInformationResponseTypeDef = TypedDict(
    "BatchGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[SchemaFacetTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)

_RequiredBatchListObjectAttributesTypeDef = TypedDict(
    "_RequiredBatchListObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListObjectAttributesTypeDef = TypedDict(
    "_OptionalBatchListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": SchemaFacetTypeDef,
    },
    total=False,
)


class BatchListObjectAttributesTypeDef(
    _RequiredBatchListObjectAttributesTypeDef, _OptionalBatchListObjectAttributesTypeDef
):
    pass


BatchRemoveFacetFromObjectTypeDef = TypedDict(
    "BatchRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

_RequiredGetObjectAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "SchemaFacet": SchemaFacetTypeDef,
        "AttributeNames": Sequence[str],
    },
)
_OptionalGetObjectAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetObjectAttributesRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetObjectAttributesRequestRequestTypeDef(
    _RequiredGetObjectAttributesRequestRequestTypeDef,
    _OptionalGetObjectAttributesRequestRequestTypeDef,
):
    pass


_RequiredListObjectAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredListObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalListObjectAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
        "FacetFilter": SchemaFacetTypeDef,
    },
    total=False,
)


class ListObjectAttributesRequestRequestTypeDef(
    _RequiredListObjectAttributesRequestRequestTypeDef,
    _OptionalListObjectAttributesRequestRequestTypeDef,
):
    pass


RemoveFacetFromObjectRequestRequestTypeDef = TypedDict(
    "RemoveFacetFromObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

ApplySchemaResponseTypeDef = TypedDict(
    "ApplySchemaResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AttachObjectResponseTypeDef = TypedDict(
    "AttachObjectResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AttachToIndexResponseTypeDef = TypedDict(
    "AttachToIndexResponseTypeDef",
    {
        "AttachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDirectoryResponseTypeDef = TypedDict(
    "CreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateObjectResponseTypeDef = TypedDict(
    "CreateObjectResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDirectoryResponseTypeDef = TypedDict(
    "DeleteDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DetachFromIndexResponseTypeDef = TypedDict(
    "DetachFromIndexResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DetachObjectResponseTypeDef = TypedDict(
    "DetachObjectResponseTypeDef",
    {
        "DetachedObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisableDirectoryResponseTypeDef = TypedDict(
    "DisableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EnableDirectoryResponseTypeDef = TypedDict(
    "EnableDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "GetAppliedSchemaVersionResponseTypeDef",
    {
        "AppliedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetObjectInformationResponseTypeDef = TypedDict(
    "GetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[SchemaFacetTypeDef],
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSchemaAsJsonResponseTypeDef = TypedDict(
    "GetSchemaAsJsonResponseTypeDef",
    {
        "Name": str,
        "Document": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "GetTypedLinkFacetInformationResponseTypeDef",
    {
        "IdentityAttributeOrder": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "ListAppliedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFacetNamesResponseTypeDef = TypedDict(
    "ListFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListManagedSchemaArnsResponseTypeDef = TypedDict(
    "ListManagedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListObjectChildrenResponseTypeDef = TypedDict(
    "ListObjectChildrenResponseTypeDef",
    {
        "Children": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListObjectPoliciesResponseTypeDef = TypedDict(
    "ListObjectPoliciesResponseTypeDef",
    {
        "AttachedPolicyIds": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPolicyAttachmentsResponseTypeDef = TypedDict(
    "ListPolicyAttachmentsResponseTypeDef",
    {
        "ObjectIdentifiers": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "ListPublishedSchemaArnsResponseTypeDef",
    {
        "SchemaArns": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetNamesResponseTypeDef",
    {
        "FacetNames": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PublishSchemaResponseTypeDef = TypedDict(
    "PublishSchemaResponseTypeDef",
    {
        "PublishedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutSchemaFromJsonResponseTypeDef = TypedDict(
    "PutSchemaFromJsonResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateObjectAttributesResponseTypeDef = TypedDict(
    "UpdateObjectAttributesResponseTypeDef",
    {
        "ObjectIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "UpgradeAppliedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "DirectoryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpgradePublishedSchemaResponseTypeDef = TypedDict(
    "UpgradePublishedSchemaResponseTypeDef",
    {
        "UpgradedSchemaArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredBatchCreateIndexTypeDef = TypedDict(
    "_RequiredBatchCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
    },
)
_OptionalBatchCreateIndexTypeDef = TypedDict(
    "_OptionalBatchCreateIndexTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchCreateIndexTypeDef(_RequiredBatchCreateIndexTypeDef, _OptionalBatchCreateIndexTypeDef):
    pass


_RequiredCreateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "OrderedIndexedAttributeList": Sequence[AttributeKeyTypeDef],
        "IsUnique": bool,
    },
)
_OptionalCreateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestRequestTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
    total=False,
)


class CreateIndexRequestRequestTypeDef(
    _RequiredCreateIndexRequestRequestTypeDef, _OptionalCreateIndexRequestRequestTypeDef
):
    pass


AttributeKeyAndValueOutputTypeDef = TypedDict(
    "AttributeKeyAndValueOutputTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValueOutputTypeDef,
    },
)

AttributeNameAndValueOutputTypeDef = TypedDict(
    "AttributeNameAndValueOutputTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValueOutputTypeDef,
    },
)

AttributeKeyAndValueTypeDef = TypedDict(
    "AttributeKeyAndValueTypeDef",
    {
        "Key": AttributeKeyTypeDef,
        "Value": TypedAttributeValueTypeDef,
    },
)

AttributeNameAndValueTypeDef = TypedDict(
    "AttributeNameAndValueTypeDef",
    {
        "AttributeName": str,
        "Value": TypedAttributeValueTypeDef,
    },
)

LinkAttributeActionTypeDef = TypedDict(
    "LinkAttributeActionTypeDef",
    {
        "AttributeActionType": UpdateActionTypeType,
        "AttributeUpdateValue": TypedAttributeValueTypeDef,
    },
    total=False,
)

ObjectAttributeActionTypeDef = TypedDict(
    "ObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": UpdateActionTypeType,
        "ObjectAttributeUpdateValue": TypedAttributeValueTypeDef,
    },
    total=False,
)

_RequiredTypedAttributeValueRangeTypeDef = TypedDict(
    "_RequiredTypedAttributeValueRangeTypeDef",
    {
        "StartMode": RangeModeType,
        "EndMode": RangeModeType,
    },
)
_OptionalTypedAttributeValueRangeTypeDef = TypedDict(
    "_OptionalTypedAttributeValueRangeTypeDef",
    {
        "StartValue": TypedAttributeValueTypeDef,
        "EndValue": TypedAttributeValueTypeDef,
    },
    total=False,
)


class TypedAttributeValueRangeTypeDef(
    _RequiredTypedAttributeValueRangeTypeDef, _OptionalTypedAttributeValueRangeTypeDef
):
    pass


BatchListObjectParentPathsResponseTypeDef = TypedDict(
    "BatchListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[PathToObjectIdentifiersTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListObjectParentPathsResponseTypeDef = TypedDict(
    "ListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[PathToObjectIdentifiersTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchListObjectParentsResponseTypeDef = TypedDict(
    "BatchListObjectParentsResponseTypeDef",
    {
        "ParentLinks": List[ObjectIdentifierAndLinkNameTupleTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListObjectParentsResponseTypeDef = TypedDict(
    "ListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List[ObjectIdentifierAndLinkNameTupleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDirectoryResponseTypeDef = TypedDict(
    "GetDirectoryResponseTypeDef",
    {
        "Directory": DirectoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDirectoriesResponseTypeDef = TypedDict(
    "ListDirectoriesResponseTypeDef",
    {
        "Directories": List[DirectoryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredFacetAttributeDefinitionOutputTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionOutputTypeDef",
    {
        "Type": FacetAttributeTypeType,
    },
)
_OptionalFacetAttributeDefinitionOutputTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionOutputTypeDef",
    {
        "DefaultValue": TypedAttributeValueOutputTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, RuleOutputTypeDef],
    },
    total=False,
)


class FacetAttributeDefinitionOutputTypeDef(
    _RequiredFacetAttributeDefinitionOutputTypeDef, _OptionalFacetAttributeDefinitionOutputTypeDef
):
    pass


_RequiredTypedLinkAttributeDefinitionOutputTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionOutputTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
)
_OptionalTypedLinkAttributeDefinitionOutputTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionOutputTypeDef",
    {
        "DefaultValue": TypedAttributeValueOutputTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, RuleOutputTypeDef],
    },
    total=False,
)


class TypedLinkAttributeDefinitionOutputTypeDef(
    _RequiredTypedLinkAttributeDefinitionOutputTypeDef,
    _OptionalTypedLinkAttributeDefinitionOutputTypeDef,
):
    pass


_RequiredFacetAttributeDefinitionTypeDef = TypedDict(
    "_RequiredFacetAttributeDefinitionTypeDef",
    {
        "Type": FacetAttributeTypeType,
    },
)
_OptionalFacetAttributeDefinitionTypeDef = TypedDict(
    "_OptionalFacetAttributeDefinitionTypeDef",
    {
        "DefaultValue": TypedAttributeValueTypeDef,
        "IsImmutable": bool,
        "Rules": Mapping[str, RuleTypeDef],
    },
    total=False,
)


class FacetAttributeDefinitionTypeDef(
    _RequiredFacetAttributeDefinitionTypeDef, _OptionalFacetAttributeDefinitionTypeDef
):
    pass


_RequiredTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeDefinitionTypeDef",
    {
        "Name": str,
        "Type": FacetAttributeTypeType,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
)
_OptionalTypedLinkAttributeDefinitionTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeDefinitionTypeDef",
    {
        "DefaultValue": TypedAttributeValueTypeDef,
        "IsImmutable": bool,
        "Rules": Mapping[str, RuleTypeDef],
    },
    total=False,
)


class TypedLinkAttributeDefinitionTypeDef(
    _RequiredTypedLinkAttributeDefinitionTypeDef, _OptionalTypedLinkAttributeDefinitionTypeDef
):
    pass


GetFacetResponseTypeDef = TypedDict(
    "GetFacetResponseTypeDef",
    {
        "Facet": FacetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef = TypedDict(
    "_RequiredListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    {
        "DirectoryArn": str,
    },
)
_OptionalListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef = TypedDict(
    "_OptionalListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef(
    _RequiredListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef,
    _OptionalListAppliedSchemaArnsRequestListAppliedSchemaArnsPaginateTypeDef,
):
    pass


_RequiredListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef = TypedDict(
    "_RequiredListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "TargetReference": ObjectReferenceTypeDef,
    },
)
_OptionalListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef = TypedDict(
    "_OptionalListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef(
    _RequiredListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef,
    _OptionalListAttachedIndicesRequestListAttachedIndicesPaginateTypeDef,
):
    pass


ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef = TypedDict(
    "ListDevelopmentSchemaArnsRequestListDevelopmentSchemaArnsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListDirectoriesRequestListDirectoriesPaginateTypeDef = TypedDict(
    "ListDirectoriesRequestListDirectoriesPaginateTypeDef",
    {
        "state": DirectoryStateType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListFacetAttributesRequestListFacetAttributesPaginateTypeDef = TypedDict(
    "_RequiredListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListFacetAttributesRequestListFacetAttributesPaginateTypeDef = TypedDict(
    "_OptionalListFacetAttributesRequestListFacetAttributesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListFacetAttributesRequestListFacetAttributesPaginateTypeDef(
    _RequiredListFacetAttributesRequestListFacetAttributesPaginateTypeDef,
    _OptionalListFacetAttributesRequestListFacetAttributesPaginateTypeDef,
):
    pass


_RequiredListFacetNamesRequestListFacetNamesPaginateTypeDef = TypedDict(
    "_RequiredListFacetNamesRequestListFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListFacetNamesRequestListFacetNamesPaginateTypeDef = TypedDict(
    "_OptionalListFacetNamesRequestListFacetNamesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListFacetNamesRequestListFacetNamesPaginateTypeDef(
    _RequiredListFacetNamesRequestListFacetNamesPaginateTypeDef,
    _OptionalListFacetNamesRequestListFacetNamesPaginateTypeDef,
):
    pass


ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef = TypedDict(
    "ListManagedSchemaArnsRequestListManagedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListObjectAttributesRequestListObjectAttributesPaginateTypeDef = TypedDict(
    "_RequiredListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectAttributesRequestListObjectAttributesPaginateTypeDef = TypedDict(
    "_OptionalListObjectAttributesRequestListObjectAttributesPaginateTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
        "FacetFilter": SchemaFacetTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListObjectAttributesRequestListObjectAttributesPaginateTypeDef(
    _RequiredListObjectAttributesRequestListObjectAttributesPaginateTypeDef,
    _OptionalListObjectAttributesRequestListObjectAttributesPaginateTypeDef,
):
    pass


_RequiredListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef = TypedDict(
    "_RequiredListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef = TypedDict(
    "_OptionalListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef(
    _RequiredListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef,
    _OptionalListObjectParentPathsRequestListObjectParentPathsPaginateTypeDef,
):
    pass


_RequiredListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef = TypedDict(
    "_RequiredListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef = TypedDict(
    "_OptionalListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef(
    _RequiredListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef,
    _OptionalListObjectPoliciesRequestListObjectPoliciesPaginateTypeDef,
):
    pass


_RequiredListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef = TypedDict(
    "_RequiredListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    {
        "DirectoryArn": str,
        "PolicyReference": ObjectReferenceTypeDef,
    },
)
_OptionalListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef = TypedDict(
    "_OptionalListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef(
    _RequiredListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef,
    _OptionalListPolicyAttachmentsRequestListPolicyAttachmentsPaginateTypeDef,
):
    pass


ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef = TypedDict(
    "ListPublishedSchemaArnsRequestListPublishedSchemaArnsPaginateTypeDef",
    {
        "SchemaArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(
    _RequiredListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
    _OptionalListTagsForResourceRequestListTagsForResourcePaginateTypeDef,
):
    pass


_RequiredListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef(
    _RequiredListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef,
    _OptionalListTypedLinkFacetAttributesRequestListTypedLinkFacetAttributesPaginateTypeDef,
):
    pass


_RequiredListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef = TypedDict(
    "_RequiredListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    {
        "SchemaArn": str,
    },
)
_OptionalListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef = TypedDict(
    "_OptionalListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef(
    _RequiredListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef,
    _OptionalListTypedLinkFacetNamesRequestListTypedLinkFacetNamesPaginateTypeDef,
):
    pass


_RequiredLookupPolicyRequestLookupPolicyPaginateTypeDef = TypedDict(
    "_RequiredLookupPolicyRequestLookupPolicyPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalLookupPolicyRequestLookupPolicyPaginateTypeDef = TypedDict(
    "_OptionalLookupPolicyRequestLookupPolicyPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class LookupPolicyRequestLookupPolicyPaginateTypeDef(
    _RequiredLookupPolicyRequestLookupPolicyPaginateTypeDef,
    _OptionalLookupPolicyRequestLookupPolicyPaginateTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

PolicyToPathTypeDef = TypedDict(
    "PolicyToPathTypeDef",
    {
        "Path": str,
        "Policies": List[PolicyAttachmentTypeDef],
    },
    total=False,
)

BatchGetLinkAttributesResponseTypeDef = TypedDict(
    "BatchGetLinkAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
    },
    total=False,
)

BatchGetObjectAttributesResponseTypeDef = TypedDict(
    "BatchGetObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
    },
    total=False,
)

BatchListObjectAttributesResponseTypeDef = TypedDict(
    "BatchListObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "NextToken": str,
    },
    total=False,
)

GetLinkAttributesResponseTypeDef = TypedDict(
    "GetLinkAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetObjectAttributesResponseTypeDef = TypedDict(
    "GetObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IndexAttachmentTypeDef = TypedDict(
    "IndexAttachmentTypeDef",
    {
        "IndexedAttributes": List[AttributeKeyAndValueOutputTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)

ListObjectAttributesResponseTypeDef = TypedDict(
    "ListObjectAttributesResponseTypeDef",
    {
        "Attributes": List[AttributeKeyAndValueOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TypedLinkSpecifierOutputTypeDef = TypedDict(
    "TypedLinkSpecifierOutputTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": List[AttributeNameAndValueOutputTypeDef],
    },
)

_RequiredAddFacetToObjectRequestRequestTypeDef = TypedDict(
    "_RequiredAddFacetToObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalAddFacetToObjectRequestRequestTypeDef = TypedDict(
    "_OptionalAddFacetToObjectRequestRequestTypeDef",
    {
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
    },
    total=False,
)


class AddFacetToObjectRequestRequestTypeDef(
    _RequiredAddFacetToObjectRequestRequestTypeDef, _OptionalAddFacetToObjectRequestRequestTypeDef
):
    pass


BatchAddFacetToObjectTypeDef = TypedDict(
    "BatchAddFacetToObjectTypeDef",
    {
        "SchemaFacet": SchemaFacetTypeDef,
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
        "ObjectReference": ObjectReferenceTypeDef,
    },
)

_RequiredBatchCreateObjectTypeDef = TypedDict(
    "_RequiredBatchCreateObjectTypeDef",
    {
        "SchemaFacet": Sequence[SchemaFacetTypeDef],
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
    },
)
_OptionalBatchCreateObjectTypeDef = TypedDict(
    "_OptionalBatchCreateObjectTypeDef",
    {
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class BatchCreateObjectTypeDef(
    _RequiredBatchCreateObjectTypeDef, _OptionalBatchCreateObjectTypeDef
):
    pass


_RequiredCreateObjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateObjectRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SchemaFacets": Sequence[SchemaFacetTypeDef],
    },
)
_OptionalCreateObjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateObjectRequestRequestTypeDef",
    {
        "ObjectAttributeList": Sequence[AttributeKeyAndValueTypeDef],
        "ParentReference": ObjectReferenceTypeDef,
        "LinkName": str,
    },
    total=False,
)


class CreateObjectRequestRequestTypeDef(
    _RequiredCreateObjectRequestRequestTypeDef, _OptionalCreateObjectRequestRequestTypeDef
):
    pass


AttachTypedLinkRequestRequestTypeDef = TypedDict(
    "AttachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueTypeDef],
    },
)

BatchAttachTypedLinkTypeDef = TypedDict(
    "BatchAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "Attributes": Sequence[AttributeNameAndValueTypeDef],
    },
)

TypedLinkSpecifierTypeDef = TypedDict(
    "TypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": TypedLinkSchemaAndFacetNameTypeDef,
        "SourceObjectReference": ObjectReferenceTypeDef,
        "TargetObjectReference": ObjectReferenceTypeDef,
        "IdentityAttributeValues": Sequence[AttributeNameAndValueTypeDef],
    },
)

LinkAttributeUpdateTypeDef = TypedDict(
    "LinkAttributeUpdateTypeDef",
    {
        "AttributeKey": AttributeKeyTypeDef,
        "AttributeAction": LinkAttributeActionTypeDef,
    },
    total=False,
)

ObjectAttributeUpdateTypeDef = TypedDict(
    "ObjectAttributeUpdateTypeDef",
    {
        "ObjectAttributeKey": AttributeKeyTypeDef,
        "ObjectAttributeAction": ObjectAttributeActionTypeDef,
    },
    total=False,
)

ObjectAttributeRangeTypeDef = TypedDict(
    "ObjectAttributeRangeTypeDef",
    {
        "AttributeKey": AttributeKeyTypeDef,
        "Range": TypedAttributeValueRangeTypeDef,
    },
    total=False,
)

_RequiredTypedLinkAttributeRangeTypeDef = TypedDict(
    "_RequiredTypedLinkAttributeRangeTypeDef",
    {
        "Range": TypedAttributeValueRangeTypeDef,
    },
)
_OptionalTypedLinkAttributeRangeTypeDef = TypedDict(
    "_OptionalTypedLinkAttributeRangeTypeDef",
    {
        "AttributeName": str,
    },
    total=False,
)


class TypedLinkAttributeRangeTypeDef(
    _RequiredTypedLinkAttributeRangeTypeDef, _OptionalTypedLinkAttributeRangeTypeDef
):
    pass


_RequiredFacetAttributeOutputTypeDef = TypedDict(
    "_RequiredFacetAttributeOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalFacetAttributeOutputTypeDef = TypedDict(
    "_OptionalFacetAttributeOutputTypeDef",
    {
        "AttributeDefinition": FacetAttributeDefinitionOutputTypeDef,
        "AttributeReference": FacetAttributeReferenceTypeDef,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
    total=False,
)


class FacetAttributeOutputTypeDef(
    _RequiredFacetAttributeOutputTypeDef, _OptionalFacetAttributeOutputTypeDef
):
    pass


ListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "ListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[TypedLinkAttributeDefinitionOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredFacetAttributeTypeDef = TypedDict(
    "_RequiredFacetAttributeTypeDef",
    {
        "Name": str,
    },
)
_OptionalFacetAttributeTypeDef = TypedDict(
    "_OptionalFacetAttributeTypeDef",
    {
        "AttributeDefinition": FacetAttributeDefinitionTypeDef,
        "AttributeReference": FacetAttributeReferenceTypeDef,
        "RequiredBehavior": RequiredAttributeBehaviorType,
    },
    total=False,
)


class FacetAttributeTypeDef(_RequiredFacetAttributeTypeDef, _OptionalFacetAttributeTypeDef):
    pass


TypedLinkFacetAttributeUpdateTypeDef = TypedDict(
    "TypedLinkFacetAttributeUpdateTypeDef",
    {
        "Attribute": TypedLinkAttributeDefinitionTypeDef,
        "Action": UpdateActionTypeType,
    },
)

TypedLinkFacetTypeDef = TypedDict(
    "TypedLinkFacetTypeDef",
    {
        "Name": str,
        "Attributes": Sequence[TypedLinkAttributeDefinitionTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)

BatchLookupPolicyResponseTypeDef = TypedDict(
    "BatchLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List[PolicyToPathTypeDef],
        "NextToken": str,
    },
    total=False,
)

LookupPolicyResponseTypeDef = TypedDict(
    "LookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List[PolicyToPathTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchListAttachedIndicesResponseTypeDef = TypedDict(
    "BatchListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
    },
    total=False,
)

BatchListIndexResponseTypeDef = TypedDict(
    "BatchListIndexResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListAttachedIndicesResponseTypeDef = TypedDict(
    "ListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIndexResponseTypeDef = TypedDict(
    "ListIndexResponseTypeDef",
    {
        "IndexAttachments": List[IndexAttachmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AttachTypedLinkResponseTypeDef = TypedDict(
    "AttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchAttachTypedLinkResponseTypeDef = TypedDict(
    "BatchAttachTypedLinkResponseTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierOutputTypeDef,
    },
    total=False,
)

BatchListIncomingTypedLinksResponseTypeDef = TypedDict(
    "BatchListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "NextToken": str,
    },
    total=False,
)

BatchListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "BatchListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListIncomingTypedLinksResponseTypeDef = TypedDict(
    "ListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "ListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[TypedLinkSpecifierOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDetachTypedLinkTypeDef = TypedDict(
    "BatchDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
    },
)

BatchGetLinkAttributesTypeDef = TypedDict(
    "BatchGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeNames": Sequence[str],
    },
)

DetachTypedLinkRequestRequestTypeDef = TypedDict(
    "DetachTypedLinkRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
    },
)

_RequiredGetLinkAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeNames": Sequence[str],
    },
)
_OptionalGetLinkAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetLinkAttributesRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class GetLinkAttributesRequestRequestTypeDef(
    _RequiredGetLinkAttributesRequestRequestTypeDef, _OptionalGetLinkAttributesRequestRequestTypeDef
):
    pass


BatchUpdateLinkAttributesTypeDef = TypedDict(
    "BatchUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)

UpdateLinkAttributesRequestRequestTypeDef = TypedDict(
    "UpdateLinkAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "TypedLinkSpecifier": TypedLinkSpecifierTypeDef,
        "AttributeUpdates": Sequence[LinkAttributeUpdateTypeDef],
    },
)

BatchUpdateObjectAttributesTypeDef = TypedDict(
    "BatchUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)

UpdateObjectAttributesRequestRequestTypeDef = TypedDict(
    "UpdateObjectAttributesRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
        "AttributeUpdates": Sequence[ObjectAttributeUpdateTypeDef],
    },
)

_RequiredBatchListIndexTypeDef = TypedDict(
    "_RequiredBatchListIndexTypeDef",
    {
        "IndexReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListIndexTypeDef = TypedDict(
    "_OptionalBatchListIndexTypeDef",
    {
        "RangesOnIndexedValues": Sequence[ObjectAttributeRangeTypeDef],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class BatchListIndexTypeDef(_RequiredBatchListIndexTypeDef, _OptionalBatchListIndexTypeDef):
    pass


_RequiredListIndexRequestListIndexPaginateTypeDef = TypedDict(
    "_RequiredListIndexRequestListIndexPaginateTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
    },
)
_OptionalListIndexRequestListIndexPaginateTypeDef = TypedDict(
    "_OptionalListIndexRequestListIndexPaginateTypeDef",
    {
        "RangesOnIndexedValues": Sequence[ObjectAttributeRangeTypeDef],
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListIndexRequestListIndexPaginateTypeDef(
    _RequiredListIndexRequestListIndexPaginateTypeDef,
    _OptionalListIndexRequestListIndexPaginateTypeDef,
):
    pass


_RequiredListIndexRequestRequestTypeDef = TypedDict(
    "_RequiredListIndexRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "IndexReference": ObjectReferenceTypeDef,
    },
)
_OptionalListIndexRequestRequestTypeDef = TypedDict(
    "_OptionalListIndexRequestRequestTypeDef",
    {
        "RangesOnIndexedValues": Sequence[ObjectAttributeRangeTypeDef],
        "MaxResults": int,
        "NextToken": str,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListIndexRequestRequestTypeDef(
    _RequiredListIndexRequestRequestTypeDef, _OptionalListIndexRequestRequestTypeDef
):
    pass


_RequiredBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListIncomingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListIncomingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListIncomingTypedLinksTypeDef(
    _RequiredBatchListIncomingTypedLinksTypeDef, _OptionalBatchListIncomingTypedLinksTypeDef
):
    pass


_RequiredBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_RequiredBatchListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalBatchListOutgoingTypedLinksTypeDef = TypedDict(
    "_OptionalBatchListOutgoingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class BatchListOutgoingTypedLinksTypeDef(
    _RequiredBatchListOutgoingTypedLinksTypeDef, _OptionalBatchListOutgoingTypedLinksTypeDef
):
    pass


_RequiredListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef(
    _RequiredListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef,
    _OptionalListIncomingTypedLinksRequestListIncomingTypedLinksPaginateTypeDef,
):
    pass


_RequiredListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListIncomingTypedLinksRequestRequestTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksRequestRequestTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListIncomingTypedLinksRequestRequestTypeDef(
    _RequiredListIncomingTypedLinksRequestRequestTypeDef,
    _OptionalListIncomingTypedLinksRequestRequestTypeDef,
):
    pass


_RequiredListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "ConsistencyLevel": ConsistencyLevelType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef(
    _RequiredListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef,
    _OptionalListOutgoingTypedLinksRequestListOutgoingTypedLinksPaginateTypeDef,
):
    pass


_RequiredListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "ObjectReference": ObjectReferenceTypeDef,
    },
)
_OptionalListOutgoingTypedLinksRequestRequestTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksRequestRequestTypeDef",
    {
        "FilterAttributeRanges": Sequence[TypedLinkAttributeRangeTypeDef],
        "FilterTypedLink": TypedLinkSchemaAndFacetNameTypeDef,
        "NextToken": str,
        "MaxResults": int,
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class ListOutgoingTypedLinksRequestRequestTypeDef(
    _RequiredListOutgoingTypedLinksRequestRequestTypeDef,
    _OptionalListOutgoingTypedLinksRequestRequestTypeDef,
):
    pass


ListFacetAttributesResponseTypeDef = TypedDict(
    "ListFacetAttributesResponseTypeDef",
    {
        "Attributes": List[FacetAttributeOutputTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateFacetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalCreateFacetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFacetRequestRequestTypeDef",
    {
        "Attributes": Sequence[FacetAttributeTypeDef],
        "ObjectType": ObjectTypeType,
        "FacetStyle": FacetStyleType,
    },
    total=False,
)


class CreateFacetRequestRequestTypeDef(
    _RequiredCreateFacetRequestRequestTypeDef, _OptionalCreateFacetRequestRequestTypeDef
):
    pass


FacetAttributeUpdateTypeDef = TypedDict(
    "FacetAttributeUpdateTypeDef",
    {
        "Attribute": FacetAttributeTypeDef,
        "Action": UpdateActionTypeType,
    },
    total=False,
)

UpdateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "UpdateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
        "AttributeUpdates": Sequence[TypedLinkFacetAttributeUpdateTypeDef],
        "IdentityAttributeOrder": Sequence[str],
    },
)

CreateTypedLinkFacetRequestRequestTypeDef = TypedDict(
    "CreateTypedLinkFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Facet": TypedLinkFacetTypeDef,
    },
)

BatchWriteOperationResponseTypeDef = TypedDict(
    "BatchWriteOperationResponseTypeDef",
    {
        "CreateObject": BatchCreateObjectResponseTypeDef,
        "AttachObject": BatchAttachObjectResponseTypeDef,
        "DetachObject": BatchDetachObjectResponseTypeDef,
        "UpdateObjectAttributes": BatchUpdateObjectAttributesResponseTypeDef,
        "DeleteObject": Dict[str, Any],
        "AddFacetToObject": Dict[str, Any],
        "RemoveFacetFromObject": Dict[str, Any],
        "AttachPolicy": Dict[str, Any],
        "DetachPolicy": Dict[str, Any],
        "CreateIndex": BatchCreateIndexResponseTypeDef,
        "AttachToIndex": BatchAttachToIndexResponseTypeDef,
        "DetachFromIndex": BatchDetachFromIndexResponseTypeDef,
        "AttachTypedLink": BatchAttachTypedLinkResponseTypeDef,
        "DetachTypedLink": Dict[str, Any],
        "UpdateLinkAttributes": Dict[str, Any],
    },
    total=False,
)

BatchReadSuccessfulResponseTypeDef = TypedDict(
    "BatchReadSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": BatchListObjectAttributesResponseTypeDef,
        "ListObjectChildren": BatchListObjectChildrenResponseTypeDef,
        "GetObjectInformation": BatchGetObjectInformationResponseTypeDef,
        "GetObjectAttributes": BatchGetObjectAttributesResponseTypeDef,
        "ListAttachedIndices": BatchListAttachedIndicesResponseTypeDef,
        "ListObjectParentPaths": BatchListObjectParentPathsResponseTypeDef,
        "ListObjectPolicies": BatchListObjectPoliciesResponseTypeDef,
        "ListPolicyAttachments": BatchListPolicyAttachmentsResponseTypeDef,
        "LookupPolicy": BatchLookupPolicyResponseTypeDef,
        "ListIndex": BatchListIndexResponseTypeDef,
        "ListOutgoingTypedLinks": BatchListOutgoingTypedLinksResponseTypeDef,
        "ListIncomingTypedLinks": BatchListIncomingTypedLinksResponseTypeDef,
        "GetLinkAttributes": BatchGetLinkAttributesResponseTypeDef,
        "ListObjectParents": BatchListObjectParentsResponseTypeDef,
    },
    total=False,
)

BatchWriteOperationTypeDef = TypedDict(
    "BatchWriteOperationTypeDef",
    {
        "CreateObject": BatchCreateObjectTypeDef,
        "AttachObject": BatchAttachObjectTypeDef,
        "DetachObject": BatchDetachObjectTypeDef,
        "UpdateObjectAttributes": BatchUpdateObjectAttributesTypeDef,
        "DeleteObject": BatchDeleteObjectTypeDef,
        "AddFacetToObject": BatchAddFacetToObjectTypeDef,
        "RemoveFacetFromObject": BatchRemoveFacetFromObjectTypeDef,
        "AttachPolicy": BatchAttachPolicyTypeDef,
        "DetachPolicy": BatchDetachPolicyTypeDef,
        "CreateIndex": BatchCreateIndexTypeDef,
        "AttachToIndex": BatchAttachToIndexTypeDef,
        "DetachFromIndex": BatchDetachFromIndexTypeDef,
        "AttachTypedLink": BatchAttachTypedLinkTypeDef,
        "DetachTypedLink": BatchDetachTypedLinkTypeDef,
        "UpdateLinkAttributes": BatchUpdateLinkAttributesTypeDef,
    },
    total=False,
)

BatchReadOperationTypeDef = TypedDict(
    "BatchReadOperationTypeDef",
    {
        "ListObjectAttributes": BatchListObjectAttributesTypeDef,
        "ListObjectChildren": BatchListObjectChildrenTypeDef,
        "ListAttachedIndices": BatchListAttachedIndicesTypeDef,
        "ListObjectParentPaths": BatchListObjectParentPathsTypeDef,
        "GetObjectInformation": BatchGetObjectInformationTypeDef,
        "GetObjectAttributes": BatchGetObjectAttributesTypeDef,
        "ListObjectParents": BatchListObjectParentsTypeDef,
        "ListObjectPolicies": BatchListObjectPoliciesTypeDef,
        "ListPolicyAttachments": BatchListPolicyAttachmentsTypeDef,
        "LookupPolicy": BatchLookupPolicyTypeDef,
        "ListIndex": BatchListIndexTypeDef,
        "ListOutgoingTypedLinks": BatchListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": BatchListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": BatchGetLinkAttributesTypeDef,
    },
    total=False,
)

_RequiredUpdateFacetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFacetRequestRequestTypeDef",
    {
        "SchemaArn": str,
        "Name": str,
    },
)
_OptionalUpdateFacetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFacetRequestRequestTypeDef",
    {
        "AttributeUpdates": Sequence[FacetAttributeUpdateTypeDef],
        "ObjectType": ObjectTypeType,
    },
    total=False,
)


class UpdateFacetRequestRequestTypeDef(
    _RequiredUpdateFacetRequestRequestTypeDef, _OptionalUpdateFacetRequestRequestTypeDef
):
    pass


BatchWriteResponseTypeDef = TypedDict(
    "BatchWriteResponseTypeDef",
    {
        "Responses": List[BatchWriteOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchReadOperationResponseTypeDef = TypedDict(
    "BatchReadOperationResponseTypeDef",
    {
        "SuccessfulResponse": BatchReadSuccessfulResponseTypeDef,
        "ExceptionResponse": BatchReadExceptionTypeDef,
    },
    total=False,
)

BatchWriteRequestRequestTypeDef = TypedDict(
    "BatchWriteRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchWriteOperationTypeDef],
    },
)

_RequiredBatchReadRequestRequestTypeDef = TypedDict(
    "_RequiredBatchReadRequestRequestTypeDef",
    {
        "DirectoryArn": str,
        "Operations": Sequence[BatchReadOperationTypeDef],
    },
)
_OptionalBatchReadRequestRequestTypeDef = TypedDict(
    "_OptionalBatchReadRequestRequestTypeDef",
    {
        "ConsistencyLevel": ConsistencyLevelType,
    },
    total=False,
)


class BatchReadRequestRequestTypeDef(
    _RequiredBatchReadRequestRequestTypeDef, _OptionalBatchReadRequestRequestTypeDef
):
    pass


BatchReadResponseTypeDef = TypedDict(
    "BatchReadResponseTypeDef",
    {
        "Responses": List[BatchReadOperationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
