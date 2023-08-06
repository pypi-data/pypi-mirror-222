"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import AssociateUserToPermissionGroupRequestRequestTypeDef

    data: AssociateUserToPermissionGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ApiAccessType,
    ApplicationPermissionType,
    ChangeTypeType,
    ColumnDataTypeType,
    DatasetKindType,
    DatasetStatusType,
    DataViewStatusType,
    ErrorCategoryType,
    ExportFileFormatType,
    IngestionStatusType,
    PermissionGroupMembershipStatusType,
    UserStatusType,
    UserTypeType,
    locationTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateUserToPermissionGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsCredentialsTypeDef",
    "ChangesetErrorInfoTypeDef",
    "ColumnDefinitionTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "DataViewDestinationTypeParamsTypeDef",
    "DatasetOwnerInfoTypeDef",
    "CreatePermissionGroupRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CredentialsTypeDef",
    "DataViewDestinationTypeParamsOutputTypeDef",
    "DataViewErrorInfoTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeletePermissionGroupRequestRequestTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisassociateUserFromPermissionGroupRequestRequestTypeDef",
    "EnableUserRequestRequestTypeDef",
    "GetChangesetRequestRequestTypeDef",
    "GetDataViewRequestRequestTypeDef",
    "GetDatasetRequestRequestTypeDef",
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    "S3LocationTypeDef",
    "GetPermissionGroupRequestRequestTypeDef",
    "PermissionGroupTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListChangesetsRequestRequestTypeDef",
    "ListDataViewsRequestRequestTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListPermissionGroupsByUserRequestRequestTypeDef",
    "PermissionGroupByUserTypeDef",
    "ListPermissionGroupsRequestRequestTypeDef",
    "ListUsersByPermissionGroupRequestRequestTypeDef",
    "UserByPermissionGroupTypeDef",
    "ListUsersRequestRequestTypeDef",
    "UserTypeDef",
    "ResourcePermissionTypeDef",
    "ResetUserPasswordRequestRequestTypeDef",
    "UpdateChangesetRequestRequestTypeDef",
    "UpdatePermissionGroupRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "AssociateUserToPermissionGroupResponseTypeDef",
    "CreateChangesetResponseTypeDef",
    "CreateDataViewResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreatePermissionGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeletePermissionGroupResponseTypeDef",
    "DisableUserResponseTypeDef",
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    "EnableUserResponseTypeDef",
    "GetUserResponseTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ResetUserPasswordResponseTypeDef",
    "UpdateChangesetResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdatePermissionGroupResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "ChangesetSummaryTypeDef",
    "GetChangesetResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "CreateDataViewRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "DataViewSummaryTypeDef",
    "GetDataViewResponseTypeDef",
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    "GetPermissionGroupResponseTypeDef",
    "ListPermissionGroupsResponseTypeDef",
    "ListChangesetsRequestListChangesetsPaginateTypeDef",
    "ListDataViewsRequestListDataViewsPaginateTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListPermissionGroupsByUserResponseTypeDef",
    "ListUsersByPermissionGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PermissionGroupParamsTypeDef",
    "ListChangesetsResponseTypeDef",
    "SchemaUnionOutputTypeDef",
    "SchemaUnionTypeDef",
    "ListDataViewsResponseTypeDef",
    "DatasetTypeDef",
    "GetDatasetResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
)

_RequiredAssociateUserToPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateUserToPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
    },
)
_OptionalAssociateUserToPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateUserToPermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class AssociateUserToPermissionGroupRequestRequestTypeDef(
    _RequiredAssociateUserToPermissionGroupRequestRequestTypeDef,
    _OptionalAssociateUserToPermissionGroupRequestRequestTypeDef,
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

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
        "expiration": int,
    },
    total=False,
)

ChangesetErrorInfoTypeDef = TypedDict(
    "ChangesetErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "dataType": ColumnDataTypeType,
        "columnName": str,
        "columnDescription": str,
    },
    total=False,
)

_RequiredCreateChangesetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
    },
)
_OptionalCreateChangesetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChangesetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateChangesetRequestRequestTypeDef(
    _RequiredCreateChangesetRequestRequestTypeDef, _OptionalCreateChangesetRequestRequestTypeDef
):
    pass

_RequiredDataViewDestinationTypeParamsTypeDef = TypedDict(
    "_RequiredDataViewDestinationTypeParamsTypeDef",
    {
        "destinationType": str,
    },
)
_OptionalDataViewDestinationTypeParamsTypeDef = TypedDict(
    "_OptionalDataViewDestinationTypeParamsTypeDef",
    {
        "s3DestinationExportFileFormat": ExportFileFormatType,
        "s3DestinationExportFileFormatOptions": Mapping[str, str],
    },
    total=False,
)

class DataViewDestinationTypeParamsTypeDef(
    _RequiredDataViewDestinationTypeParamsTypeDef, _OptionalDataViewDestinationTypeParamsTypeDef
):
    pass

DatasetOwnerInfoTypeDef = TypedDict(
    "DatasetOwnerInfoTypeDef",
    {
        "name": str,
        "phoneNumber": str,
        "email": str,
    },
    total=False,
)

_RequiredCreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "applicationPermissions": Sequence[ApplicationPermissionType],
    },
)
_OptionalCreatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionGroupRequestRequestTypeDef",
    {
        "description": str,
        "clientToken": str,
    },
    total=False,
)

class CreatePermissionGroupRequestRequestTypeDef(
    _RequiredCreatePermissionGroupRequestRequestTypeDef,
    _OptionalCreatePermissionGroupRequestRequestTypeDef,
):
    pass

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "emailAddress": str,
        "type": UserTypeType,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "firstName": str,
        "lastName": str,
        "ApiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "clientToken": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
    total=False,
)

_RequiredDataViewDestinationTypeParamsOutputTypeDef = TypedDict(
    "_RequiredDataViewDestinationTypeParamsOutputTypeDef",
    {
        "destinationType": str,
    },
)
_OptionalDataViewDestinationTypeParamsOutputTypeDef = TypedDict(
    "_OptionalDataViewDestinationTypeParamsOutputTypeDef",
    {
        "s3DestinationExportFileFormat": ExportFileFormatType,
        "s3DestinationExportFileFormatOptions": Dict[str, str],
    },
    total=False,
)

class DataViewDestinationTypeParamsOutputTypeDef(
    _RequiredDataViewDestinationTypeParamsOutputTypeDef,
    _OptionalDataViewDestinationTypeParamsOutputTypeDef,
):
    pass

DataViewErrorInfoTypeDef = TypedDict(
    "DataViewErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

_RequiredDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteDatasetRequestRequestTypeDef(
    _RequiredDeleteDatasetRequestRequestTypeDef, _OptionalDeleteDatasetRequestRequestTypeDef
):
    pass

_RequiredDeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)
_OptionalDeletePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeletePermissionGroupRequestRequestTypeDef(
    _RequiredDeletePermissionGroupRequestRequestTypeDef,
    _OptionalDeletePermissionGroupRequestRequestTypeDef,
):
    pass

_RequiredDisableUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisableUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalDisableUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisableUserRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisableUserRequestRequestTypeDef(
    _RequiredDisableUserRequestRequestTypeDef, _OptionalDisableUserRequestRequestTypeDef
):
    pass

_RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "userId": str,
    },
)
_OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DisassociateUserFromPermissionGroupRequestRequestTypeDef(
    _RequiredDisassociateUserFromPermissionGroupRequestRequestTypeDef,
    _OptionalDisassociateUserFromPermissionGroupRequestRequestTypeDef,
):
    pass

_RequiredEnableUserRequestRequestTypeDef = TypedDict(
    "_RequiredEnableUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalEnableUserRequestRequestTypeDef = TypedDict(
    "_OptionalEnableUserRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class EnableUserRequestRequestTypeDef(
    _RequiredEnableUserRequestRequestTypeDef, _OptionalEnableUserRequestRequestTypeDef
):
    pass

GetChangesetRequestRequestTypeDef = TypedDict(
    "GetChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
    },
)

GetDataViewRequestRequestTypeDef = TypedDict(
    "GetDataViewRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)

GetDatasetRequestRequestTypeDef = TypedDict(
    "GetDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)

GetExternalDataViewAccessDetailsRequestRequestTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsRequestRequestTypeDef",
    {
        "dataViewId": str,
        "datasetId": str,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

GetPermissionGroupRequestRequestTypeDef = TypedDict(
    "GetPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)

PermissionGroupTypeDef = TypedDict(
    "PermissionGroupTypeDef",
    {
        "permissionGroupId": str,
        "name": str,
        "description": str,
        "applicationPermissions": List[ApplicationPermissionType],
        "createTime": int,
        "lastModifiedTime": int,
        "membershipStatus": PermissionGroupMembershipStatusType,
    },
    total=False,
)

_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "durationInMinutes": int,
    },
    total=False,
)

class GetProgrammaticAccessCredentialsRequestRequestTypeDef(
    _RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef,
    _OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef,
):
    pass

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)

GetWorkingLocationRequestRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestRequestTypeDef",
    {
        "locationType": locationTypeType,
    },
    total=False,
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

_RequiredListChangesetsRequestRequestTypeDef = TypedDict(
    "_RequiredListChangesetsRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListChangesetsRequestRequestTypeDef = TypedDict(
    "_OptionalListChangesetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListChangesetsRequestRequestTypeDef(
    _RequiredListChangesetsRequestRequestTypeDef, _OptionalListChangesetsRequestRequestTypeDef
):
    pass

_RequiredListDataViewsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataViewsRequestRequestTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListDataViewsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataViewsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDataViewsRequestRequestTypeDef(
    _RequiredListDataViewsRequestRequestTypeDef, _OptionalListDataViewsRequestRequestTypeDef
):
    pass

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

_RequiredListPermissionGroupsByUserRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionGroupsByUserRequestRequestTypeDef",
    {
        "userId": str,
        "maxResults": int,
    },
)
_OptionalListPermissionGroupsByUserRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionGroupsByUserRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListPermissionGroupsByUserRequestRequestTypeDef(
    _RequiredListPermissionGroupsByUserRequestRequestTypeDef,
    _OptionalListPermissionGroupsByUserRequestRequestTypeDef,
):
    pass

PermissionGroupByUserTypeDef = TypedDict(
    "PermissionGroupByUserTypeDef",
    {
        "permissionGroupId": str,
        "name": str,
        "membershipStatus": PermissionGroupMembershipStatusType,
    },
    total=False,
)

_RequiredListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
    },
)
_OptionalListPermissionGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListPermissionGroupsRequestRequestTypeDef(
    _RequiredListPermissionGroupsRequestRequestTypeDef,
    _OptionalListPermissionGroupsRequestRequestTypeDef,
):
    pass

_RequiredListUsersByPermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersByPermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
        "maxResults": int,
    },
)
_OptionalListUsersByPermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersByPermissionGroupRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListUsersByPermissionGroupRequestRequestTypeDef(
    _RequiredListUsersByPermissionGroupRequestRequestTypeDef,
    _OptionalListUsersByPermissionGroupRequestRequestTypeDef,
):
    pass

UserByPermissionGroupTypeDef = TypedDict(
    "UserByPermissionGroupTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "membershipStatus": PermissionGroupMembershipStatusType,
    },
    total=False,
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "maxResults": int,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
    },
    total=False,
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "permission": str,
    },
    total=False,
)

_RequiredResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredResetUserPasswordRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalResetUserPasswordRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ResetUserPasswordRequestRequestTypeDef(
    _RequiredResetUserPasswordRequestRequestTypeDef, _OptionalResetUserPasswordRequestRequestTypeDef
):
    pass

_RequiredUpdateChangesetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "sourceParams": Mapping[str, str],
        "formatParams": Mapping[str, str],
    },
)
_OptionalUpdateChangesetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChangesetRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateChangesetRequestRequestTypeDef(
    _RequiredUpdateChangesetRequestRequestTypeDef, _OptionalUpdateChangesetRequestRequestTypeDef
):
    pass

_RequiredUpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePermissionGroupRequestRequestTypeDef",
    {
        "permissionGroupId": str,
    },
)
_OptionalUpdatePermissionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePermissionGroupRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "applicationPermissions": Sequence[ApplicationPermissionType],
        "clientToken": str,
    },
    total=False,
)

class UpdatePermissionGroupRequestRequestTypeDef(
    _RequiredUpdatePermissionGroupRequestRequestTypeDef,
    _OptionalUpdatePermissionGroupRequestRequestTypeDef,
):
    pass

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "userId": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "type": UserTypeType,
        "firstName": str,
        "lastName": str,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

AssociateUserToPermissionGroupResponseTypeDef = TypedDict(
    "AssociateUserToPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "datasetId": str,
        "changesetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDataViewResponseTypeDef = TypedDict(
    "CreateDataViewResponseTypeDef",
    {
        "datasetId": str,
        "dataViewId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreatePermissionGroupResponseTypeDef = TypedDict(
    "CreatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeletePermissionGroupResponseTypeDef = TypedDict(
    "DeletePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisableUserResponseTypeDef = TypedDict(
    "DisableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateUserFromPermissionGroupResponseTypeDef = TypedDict(
    "DisassociateUserFromPermissionGroupResponseTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EnableUserResponseTypeDef = TypedDict(
    "EnableUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userId": str,
        "status": UserStatusType,
        "firstName": str,
        "lastName": str,
        "emailAddress": str,
        "type": UserTypeType,
        "apiAccess": ApiAccessType,
        "apiAccessPrincipalArn": str,
        "createTime": int,
        "lastEnabledTime": int,
        "lastDisabledTime": int,
        "lastModifiedTime": int,
        "lastLoginTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ResetUserPasswordResponseTypeDef = TypedDict(
    "ResetUserPasswordResponseTypeDef",
    {
        "userId": str,
        "temporaryPassword": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateChangesetResponseTypeDef = TypedDict(
    "UpdateChangesetResponseTypeDef",
    {
        "changesetId": str,
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "datasetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePermissionGroupResponseTypeDef = TypedDict(
    "UpdatePermissionGroupResponseTypeDef",
    {
        "permissionGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ChangesetSummaryTypeDef = TypedDict(
    "ChangesetSummaryTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": ChangesetErrorInfoTypeDef,
        "activeUntilTimestamp": int,
        "activeFromTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
    },
    total=False,
)

GetChangesetResponseTypeDef = TypedDict(
    "GetChangesetResponseTypeDef",
    {
        "changesetId": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceParams": Dict[str, str],
        "formatParams": Dict[str, str],
        "createTime": int,
        "status": IngestionStatusType,
        "errorInfo": ChangesetErrorInfoTypeDef,
        "activeUntilTimestamp": int,
        "activeFromTimestamp": int,
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "columns": List[ColumnDefinitionTypeDef],
        "primaryKeyColumns": List[str],
    },
    total=False,
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": Sequence[ColumnDefinitionTypeDef],
        "primaryKeyColumns": Sequence[str],
    },
    total=False,
)

_RequiredCreateDataViewRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataViewRequestRequestTypeDef",
    {
        "datasetId": str,
        "destinationTypeParams": DataViewDestinationTypeParamsTypeDef,
    },
)
_OptionalCreateDataViewRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataViewRequestRequestTypeDef",
    {
        "clientToken": str,
        "autoUpdate": bool,
        "sortColumns": Sequence[str],
        "partitionColumns": Sequence[str],
        "asOfTimestamp": int,
    },
    total=False,
)

class CreateDataViewRequestRequestTypeDef(
    _RequiredCreateDataViewRequestRequestTypeDef, _OptionalCreateDataViewRequestRequestTypeDef
):
    pass

GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": CredentialsTypeDef,
        "durationInMinutes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DataViewSummaryTypeDef = TypedDict(
    "DataViewSummaryTypeDef",
    {
        "dataViewId": str,
        "dataViewArn": str,
        "datasetId": str,
        "asOfTimestamp": int,
        "partitionColumns": List[str],
        "sortColumns": List[str],
        "status": DataViewStatusType,
        "errorInfo": DataViewErrorInfoTypeDef,
        "destinationTypeProperties": DataViewDestinationTypeParamsOutputTypeDef,
        "autoUpdate": bool,
        "createTime": int,
        "lastModifiedTime": int,
    },
    total=False,
)

GetDataViewResponseTypeDef = TypedDict(
    "GetDataViewResponseTypeDef",
    {
        "autoUpdate": bool,
        "partitionColumns": List[str],
        "datasetId": str,
        "asOfTimestamp": int,
        "errorInfo": DataViewErrorInfoTypeDef,
        "lastModifiedTime": int,
        "createTime": int,
        "sortColumns": List[str],
        "dataViewId": str,
        "dataViewArn": str,
        "destinationTypeParams": DataViewDestinationTypeParamsOutputTypeDef,
        "status": DataViewStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetExternalDataViewAccessDetailsResponseTypeDef = TypedDict(
    "GetExternalDataViewAccessDetailsResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "s3Location": S3LocationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetPermissionGroupResponseTypeDef = TypedDict(
    "GetPermissionGroupResponseTypeDef",
    {
        "permissionGroup": PermissionGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListPermissionGroupsResponseTypeDef = TypedDict(
    "ListPermissionGroupsResponseTypeDef",
    {
        "permissionGroups": List[PermissionGroupTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredListChangesetsRequestListChangesetsPaginateTypeDef = TypedDict(
    "_RequiredListChangesetsRequestListChangesetsPaginateTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListChangesetsRequestListChangesetsPaginateTypeDef = TypedDict(
    "_OptionalListChangesetsRequestListChangesetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListChangesetsRequestListChangesetsPaginateTypeDef(
    _RequiredListChangesetsRequestListChangesetsPaginateTypeDef,
    _OptionalListChangesetsRequestListChangesetsPaginateTypeDef,
):
    pass

_RequiredListDataViewsRequestListDataViewsPaginateTypeDef = TypedDict(
    "_RequiredListDataViewsRequestListDataViewsPaginateTypeDef",
    {
        "datasetId": str,
    },
)
_OptionalListDataViewsRequestListDataViewsPaginateTypeDef = TypedDict(
    "_OptionalListDataViewsRequestListDataViewsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

class ListDataViewsRequestListDataViewsPaginateTypeDef(
    _RequiredListDataViewsRequestListDataViewsPaginateTypeDef,
    _OptionalListDataViewsRequestListDataViewsPaginateTypeDef,
):
    pass

ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef = TypedDict(
    "ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListPermissionGroupsByUserResponseTypeDef = TypedDict(
    "ListPermissionGroupsByUserResponseTypeDef",
    {
        "permissionGroups": List[PermissionGroupByUserTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUsersByPermissionGroupResponseTypeDef = TypedDict(
    "ListUsersByPermissionGroupResponseTypeDef",
    {
        "users": List[UserByPermissionGroupTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "users": List[UserTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PermissionGroupParamsTypeDef = TypedDict(
    "PermissionGroupParamsTypeDef",
    {
        "permissionGroupId": str,
        "datasetPermissions": Sequence[ResourcePermissionTypeDef],
    },
    total=False,
)

ListChangesetsResponseTypeDef = TypedDict(
    "ListChangesetsResponseTypeDef",
    {
        "changesets": List[ChangesetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SchemaUnionOutputTypeDef = TypedDict(
    "SchemaUnionOutputTypeDef",
    {
        "tabularSchemaConfig": SchemaDefinitionOutputTypeDef,
    },
    total=False,
)

SchemaUnionTypeDef = TypedDict(
    "SchemaUnionTypeDef",
    {
        "tabularSchemaConfig": SchemaDefinitionTypeDef,
    },
    total=False,
)

ListDataViewsResponseTypeDef = TypedDict(
    "ListDataViewsResponseTypeDef",
    {
        "nextToken": str,
        "dataViews": List[DataViewSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "ownerInfo": DatasetOwnerInfoTypeDef,
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": SchemaUnionOutputTypeDef,
        "alias": str,
    },
    total=False,
)

GetDatasetResponseTypeDef = TypedDict(
    "GetDatasetResponseTypeDef",
    {
        "datasetId": str,
        "datasetArn": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
        "datasetDescription": str,
        "createTime": int,
        "lastModifiedTime": int,
        "schemaDefinition": SchemaUnionOutputTypeDef,
        "alias": str,
        "status": DatasetStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "datasetTitle": str,
        "kind": DatasetKindType,
        "permissionGroupParams": PermissionGroupParamsTypeDef,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "datasetDescription": str,
        "ownerInfo": DatasetOwnerInfoTypeDef,
        "alias": str,
        "schemaDefinition": SchemaUnionTypeDef,
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

_RequiredUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetRequestRequestTypeDef",
    {
        "datasetId": str,
        "datasetTitle": str,
        "kind": DatasetKindType,
    },
)
_OptionalUpdateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetRequestRequestTypeDef",
    {
        "clientToken": str,
        "datasetDescription": str,
        "alias": str,
        "schemaDefinition": SchemaUnionTypeDef,
    },
    total=False,
)

class UpdateDatasetRequestRequestTypeDef(
    _RequiredUpdateDatasetRequestRequestTypeDef, _OptionalUpdateDatasetRequestRequestTypeDef
):
    pass

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasets": List[DatasetTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
