"""
Type annotations for kendra service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/type_defs/)

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlConfigurationSummaryTypeDef

    data: AccessControlConfigurationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AlfrescoEntityType,
    AttributeSuggestionsModeType,
    ConditionOperatorType,
    ConfluenceAttachmentFieldNameType,
    ConfluenceAuthenticationTypeType,
    ConfluenceBlogFieldNameType,
    ConfluencePageFieldNameType,
    ConfluenceSpaceFieldNameType,
    ConfluenceVersionType,
    ContentTypeType,
    DatabaseEngineTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    DocumentAttributeValueTypeType,
    DocumentStatusType,
    EntityTypeType,
    ErrorCodeType,
    ExperienceStatusType,
    FaqFileFormatType,
    FaqStatusType,
    FeaturedResultsSetStatusType,
    HighlightTypeType,
    IndexEditionType,
    IndexStatusType,
    IntervalType,
    IssueSubEntityType,
    KeyLocationType,
    MetricTypeType,
    ModeType,
    OrderType,
    PersonaType,
    PrincipalMappingStatusType,
    PrincipalTypeType,
    QueryIdentifiersEnclosingOptionType,
    QueryResultFormatType,
    QueryResultTypeType,
    QuerySuggestionsBlockListStatusType,
    QuerySuggestionsStatusType,
    ReadAccessTypeType,
    RelevanceTypeType,
    SalesforceChatterFeedIncludeFilterTypeType,
    SalesforceKnowledgeArticleStateType,
    SalesforceStandardObjectNameType,
    ScoreConfidenceType,
    ServiceNowAuthenticationTypeType,
    ServiceNowBuildVersionTypeType,
    SharePointOnlineAuthenticationTypeType,
    SharePointVersionType,
    SlackEntityType,
    SortOrderType,
    SuggestionTypeType,
    ThesaurusStatusType,
    TypeType,
    UserContextPolicyType,
    UserGroupResolutionModeType,
    WebCrawlerModeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlConfigurationSummaryTypeDef",
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationOutputTypeDef",
    "S3PathTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "EntityConfigurationTypeDef",
    "FailedEntityTypeDef",
    "ResponseMetadataTypeDef",
    "EntityPersonaConfigurationTypeDef",
    "SuggestableConfigTypeDef",
    "BasicAuthenticationConfigurationTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteFeaturedResultsSetErrorTypeDef",
    "BatchDeleteFeaturedResultsSetRequestRequestTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "StatusTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClearQuerySuggestionsRequestRequestTypeDef",
    "ClickFeedbackTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "ContentSourceConfigurationOutputTypeDef",
    "ContentSourceConfigurationTypeDef",
    "CorrectionTypeDef",
    "PrincipalTypeDef",
    "TagTypeDef",
    "FeaturedDocumentTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "UserGroupResolutionConfigurationTypeDef",
    "TemplateConfigurationOutputTypeDef",
    "TemplateConfigurationTypeDef",
    "DataSourceGroupTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "SqlConfigurationTypeDef",
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteExperienceRequestRequestTypeDef",
    "DeleteFaqRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePrincipalMappingRequestRequestTypeDef",
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    "DeleteThesaurusRequestRequestTypeDef",
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeExperienceRequestRequestTypeDef",
    "ExperienceEndpointTypeDef",
    "DescribeFaqRequestRequestTypeDef",
    "DescribeFeaturedResultsSetRequestRequestTypeDef",
    "FeaturedDocumentMissingTypeDef",
    "FeaturedDocumentWithMetadataTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribePrincipalMappingRequestRequestTypeDef",
    "GroupOrderingIdSummaryTypeDef",
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    "DescribeThesaurusRequestRequestTypeDef",
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    "DocumentAttributeValueOutputTypeDef",
    "DocumentAttributeValueTypeDef",
    "RelevanceOutputTypeDef",
    "SearchTypeDef",
    "RelevanceTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "EntityDisplayDataTypeDef",
    "UserIdentityConfigurationTypeDef",
    "FacetResultTypeDef",
    "FacetTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "FeaturedResultsSetSummaryTypeDef",
    "GetSnapshotsRequestRequestTypeDef",
    "TimeRangeOutputTypeDef",
    "GitHubDocumentCrawlPropertiesTypeDef",
    "SaaSConfigurationTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "GroupSummaryTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "TextDocumentStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListAccessControlConfigurationsRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListEntityPersonasRequestRequestTypeDef",
    "PersonasSummaryTypeDef",
    "ListExperienceEntitiesRequestRequestTypeDef",
    "ListExperiencesRequestRequestTypeDef",
    "ListFaqsRequestRequestTypeDef",
    "ListFeaturedResultsSetsRequestRequestTypeDef",
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListThesauriRequestRequestTypeDef",
    "ThesaurusSummaryTypeDef",
    "SortingConfigurationTypeDef",
    "SpellCorrectionConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "WarningTypeDef",
    "RelevanceFeedbackTypeDef",
    "SeedUrlConfigurationOutputTypeDef",
    "SeedUrlConfigurationTypeDef",
    "SiteMapsConfigurationOutputTypeDef",
    "SiteMapsConfigurationTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "SuggestionHighlightTypeDef",
    "TableCellTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ColumnConfigurationOutputTypeDef",
    "ColumnConfigurationTypeDef",
    "GoogleDriveConfigurationOutputTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "SalesforceChatterFeedConfigurationOutputTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationOutputTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationOutputTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationOutputTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationOutputTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "WorkDocsConfigurationOutputTypeDef",
    "WorkDocsConfigurationTypeDef",
    "BoxConfigurationOutputTypeDef",
    "FsxConfigurationOutputTypeDef",
    "JiraConfigurationOutputTypeDef",
    "QuipConfigurationOutputTypeDef",
    "SlackConfigurationOutputTypeDef",
    "AlfrescoConfigurationOutputTypeDef",
    "OnPremiseConfigurationTypeDef",
    "OneDriveUsersOutputTypeDef",
    "OneDriveUsersTypeDef",
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    "UpdateThesaurusRequestRequestTypeDef",
    "AlfrescoConfigurationTypeDef",
    "BoxConfigurationTypeDef",
    "FsxConfigurationTypeDef",
    "JiraConfigurationTypeDef",
    "QuipConfigurationTypeDef",
    "SlackConfigurationTypeDef",
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    "AssociateEntitiesToExperienceResponseTypeDef",
    "AssociatePersonasToEntitiesResponseTypeDef",
    "CreateAccessControlConfigurationResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateExperienceResponseTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    "CreateThesaurusResponseTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    "DescribeThesaurusResponseTypeDef",
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAccessControlConfigurationsResponseTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    "AttributeSuggestionsDescribeConfigTypeDef",
    "AttributeSuggestionsUpdateConfigTypeDef",
    "AuthenticationConfigurationOutputTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchDeleteFeaturedResultsSetResponseTypeDef",
    "BatchGetDocumentStatusResponseTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "ConfluenceAttachmentConfigurationOutputTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceBlogConfigurationOutputTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "SharePointConfigurationOutputTypeDef",
    "SharePointConfigurationTypeDef",
    "ConfluencePageConfigurationOutputTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluenceSpaceConfigurationOutputTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "SpellCorrectedQueryTypeDef",
    "HierarchicalPrincipalOutputTypeDef",
    "HierarchicalPrincipalTypeDef",
    "CreateFaqRequestRequestTypeDef",
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    "CreateThesaurusRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateFeaturedResultsSetRequestRequestTypeDef",
    "FeaturedResultsSetTypeDef",
    "UpdateFeaturedResultsSetRequestRequestTypeDef",
    "UserContextTypeDef",
    "ListDataSourcesResponseTypeDef",
    "DataSourceSyncJobTypeDef",
    "ExperiencesSummaryTypeDef",
    "DescribeFeaturedResultsSetResponseTypeDef",
    "DescribePrincipalMappingResponseTypeDef",
    "DocumentAttributeConditionOutputTypeDef",
    "DocumentAttributeOutputTypeDef",
    "DocumentAttributeTargetOutputTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentMetadataConfigurationOutputTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "S3DataSourceConfigurationOutputTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "ExperienceEntitiesSummaryTypeDef",
    "ExperienceConfigurationOutputTypeDef",
    "ExperienceConfigurationTypeDef",
    "ListFaqsResponseTypeDef",
    "ListFeaturedResultsSetsResponseTypeDef",
    "GetSnapshotsResponseTypeDef",
    "GroupMembersTypeDef",
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    "TextWithHighlightsTypeDef",
    "ListIndicesResponseTypeDef",
    "IndexStatisticsTypeDef",
    "UserTokenConfigurationTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListEntityPersonasResponseTypeDef",
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    "ListThesauriResponseTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "UrlsOutputTypeDef",
    "UrlsTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "TableRowTypeDef",
    "DatabaseConfigurationOutputTypeDef",
    "DatabaseConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationOutputTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "ServiceNowConfigurationOutputTypeDef",
    "ServiceNowConfigurationTypeDef",
    "GitHubConfigurationOutputTypeDef",
    "GitHubConfigurationTypeDef",
    "OneDriveConfigurationOutputTypeDef",
    "OneDriveConfigurationTypeDef",
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    "ConfluenceConfigurationOutputTypeDef",
    "ConfluenceConfigurationTypeDef",
    "DescribeAccessControlConfigurationResponseTypeDef",
    "CreateAccessControlConfigurationRequestRequestTypeDef",
    "UpdateAccessControlConfigurationRequestRequestTypeDef",
    "CreateFeaturedResultsSetResponseTypeDef",
    "UpdateFeaturedResultsSetResponseTypeDef",
    "AttributeSuggestionsGetConfigTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListExperiencesResponseTypeDef",
    "HookConfigurationOutputTypeDef",
    "RetrieveResultItemTypeDef",
    "SourceDocumentTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationOutputTypeDef",
    "HookConfigurationTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    "AttributeFilterTypeDef",
    "DocumentInfoTypeDef",
    "DocumentTypeDef",
    "QueryRequestRequestTypeDef",
    "RetrieveRequestRequestTypeDef",
    "ListExperienceEntitiesResponseTypeDef",
    "DescribeExperienceResponseTypeDef",
    "CreateExperienceRequestRequestTypeDef",
    "UpdateExperienceRequestRequestTypeDef",
    "PutPrincipalMappingRequestRequestTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "WebCrawlerConfigurationOutputTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "SuggestionValueTypeDef",
    "TableExcerptTypeDef",
    "SalesforceConfigurationOutputTypeDef",
    "SalesforceConfigurationTypeDef",
    "GetQuerySuggestionsRequestRequestTypeDef",
    "RetrieveResultTypeDef",
    "CustomDocumentEnrichmentConfigurationOutputTypeDef",
    "CustomDocumentEnrichmentConfigurationTypeDef",
    "BatchGetDocumentStatusRequestRequestTypeDef",
    "AdditionalResultAttributeTypeDef",
    "SuggestionTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "DataSourceConfigurationTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
    "FeaturedResultsItemTypeDef",
    "QueryResultItemTypeDef",
    "GetQuerySuggestionsResponseTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "QueryResultTypeDef",
)

AccessControlConfigurationSummaryTypeDef = TypedDict(
    "AccessControlConfigurationSummaryTypeDef",
    {
        "Id": str,
    },
)

AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef",
    {
        "KeyPath": str,
    },
    total=False,
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "AllowedGroupsColumnName": str,
    },
)

_RequiredDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_RequiredDataSourceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": str,
        "IndexFieldName": str,
    },
)
_OptionalDataSourceToIndexFieldMappingTypeDef = TypedDict(
    "_OptionalDataSourceToIndexFieldMappingTypeDef",
    {
        "DateFieldFormat": str,
    },
    total=False,
)


class DataSourceToIndexFieldMappingTypeDef(
    _RequiredDataSourceToIndexFieldMappingTypeDef, _OptionalDataSourceToIndexFieldMappingTypeDef
):
    pass


DataSourceVpcConfigurationOutputTypeDef = TypedDict(
    "DataSourceVpcConfigurationOutputTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

S3PathTypeDef = TypedDict(
    "S3PathTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)

EntityConfigurationTypeDef = TypedDict(
    "EntityConfigurationTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
    },
)

FailedEntityTypeDef = TypedDict(
    "FailedEntityTypeDef",
    {
        "EntityId": str,
        "ErrorMessage": str,
    },
    total=False,
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

EntityPersonaConfigurationTypeDef = TypedDict(
    "EntityPersonaConfigurationTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
    },
)

SuggestableConfigTypeDef = TypedDict(
    "SuggestableConfigTypeDef",
    {
        "AttributeName": str,
        "Suggestable": bool,
    },
    total=False,
)

BasicAuthenticationConfigurationTypeDef = TypedDict(
    "BasicAuthenticationConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": str,
    },
)

_RequiredDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_RequiredDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalDataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "_OptionalDataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceSyncJobId": str,
    },
    total=False,
)


class DataSourceSyncJobMetricTargetTypeDef(
    _RequiredDataSourceSyncJobMetricTargetTypeDef, _OptionalDataSourceSyncJobMetricTargetTypeDef
):
    pass


BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

BatchDeleteFeaturedResultsSetErrorTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
)

BatchDeleteFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetIds": Sequence[str],
    },
)

BatchGetDocumentStatusResponseErrorTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseErrorTypeDef",
    {
        "DocumentId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "DocumentId": str,
        "DocumentStatus": DocumentStatusType,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)

ClearQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "ClearQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": Union[datetime, str],
    },
)

ConfluenceAttachmentToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceAttachmentFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceBlogFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "Credentials": str,
    },
    total=False,
)


class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass


ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluencePageFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConfluenceSpaceToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": ConfluenceSpaceFieldNameType,
        "DateFieldFormat": str,
        "IndexFieldName": str,
    },
    total=False,
)

ConnectionConfigurationTypeDef = TypedDict(
    "ConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
)

ContentSourceConfigurationOutputTypeDef = TypedDict(
    "ContentSourceConfigurationOutputTypeDef",
    {
        "DataSourceIds": List[str],
        "FaqIds": List[str],
        "DirectPutContent": bool,
    },
    total=False,
)

ContentSourceConfigurationTypeDef = TypedDict(
    "ContentSourceConfigurationTypeDef",
    {
        "DataSourceIds": Sequence[str],
        "FaqIds": Sequence[str],
        "DirectPutContent": bool,
    },
    total=False,
)

CorrectionTypeDef = TypedDict(
    "CorrectionTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
        "Term": str,
        "CorrectedTerm": str,
    },
    total=False,
)

_RequiredPrincipalTypeDef = TypedDict(
    "_RequiredPrincipalTypeDef",
    {
        "Name": str,
        "Type": PrincipalTypeType,
        "Access": ReadAccessTypeType,
    },
)
_OptionalPrincipalTypeDef = TypedDict(
    "_OptionalPrincipalTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)


class PrincipalTypeDef(_RequiredPrincipalTypeDef, _OptionalPrincipalTypeDef):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

FeaturedDocumentTypeDef = TypedDict(
    "FeaturedDocumentTypeDef",
    {
        "Id": str,
    },
    total=False,
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

UserGroupResolutionConfigurationTypeDef = TypedDict(
    "UserGroupResolutionConfigurationTypeDef",
    {
        "UserGroupResolutionMode": UserGroupResolutionModeType,
    },
)

TemplateConfigurationOutputTypeDef = TypedDict(
    "TemplateConfigurationOutputTypeDef",
    {
        "Template": Dict[str, Any],
    },
    total=False,
)

TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "Template": Mapping[str, Any],
    },
    total=False,
)

DataSourceGroupTypeDef = TypedDict(
    "DataSourceGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": str,
    },
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": DataSourceTypeType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": DataSourceStatusType,
        "LanguageCode": str,
    },
    total=False,
)

DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "DocumentsAdded": str,
        "DocumentsModified": str,
        "DocumentsDeleted": str,
        "DocumentsFailed": str,
        "DocumentsScanned": str,
    },
    total=False,
)

SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {
        "QueryIdentifiersEnclosingOption": QueryIdentifiersEnclosingOptionType,
    },
    total=False,
)

DeleteAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteExperienceRequestRequestTypeDef = TypedDict(
    "DeleteExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteFaqRequestRequestTypeDef = TypedDict(
    "DeleteFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredDeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
    },
)
_OptionalDeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "OrderingId": int,
    },
    total=False,
)


class DeletePrincipalMappingRequestRequestTypeDef(
    _RequiredDeletePrincipalMappingRequestRequestTypeDef,
    _OptionalDeletePrincipalMappingRequestRequestTypeDef,
):
    pass


DeleteQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteThesaurusRequestRequestTypeDef = TypedDict(
    "DeleteThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeExperienceRequestRequestTypeDef = TypedDict(
    "DescribeExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

ExperienceEndpointTypeDef = TypedDict(
    "ExperienceEndpointTypeDef",
    {
        "EndpointType": Literal["HOME"],
        "Endpoint": str,
    },
    total=False,
)

DescribeFaqRequestRequestTypeDef = TypedDict(
    "DescribeFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "DescribeFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetId": str,
    },
)

FeaturedDocumentMissingTypeDef = TypedDict(
    "FeaturedDocumentMissingTypeDef",
    {
        "Id": str,
    },
    total=False,
)

FeaturedDocumentWithMetadataTypeDef = TypedDict(
    "FeaturedDocumentWithMetadataTypeDef",
    {
        "Id": str,
        "Title": str,
        "URI": str,
    },
    total=False,
)

DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

_RequiredDescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
    },
)
_OptionalDescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)


class DescribePrincipalMappingRequestRequestTypeDef(
    _RequiredDescribePrincipalMappingRequestRequestTypeDef,
    _OptionalDescribePrincipalMappingRequestRequestTypeDef,
):
    pass


GroupOrderingIdSummaryTypeDef = TypedDict(
    "GroupOrderingIdSummaryTypeDef",
    {
        "Status": PrincipalMappingStatusType,
        "LastUpdatedAt": datetime,
        "ReceivedAt": datetime,
        "OrderingId": int,
        "FailureReason": str,
    },
    total=False,
)

DescribeQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

DescribeThesaurusRequestRequestTypeDef = TypedDict(
    "DescribeThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DisassociatePersonasFromEntitiesRequestRequestTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityIds": Sequence[str],
    },
)

DocumentAttributeValueOutputTypeDef = TypedDict(
    "DocumentAttributeValueOutputTypeDef",
    {
        "StringValue": str,
        "StringListValue": List[str],
        "LongValue": int,
        "DateValue": datetime,
    },
    total=False,
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "StringValue": str,
        "StringListValue": Sequence[str],
        "LongValue": int,
        "DateValue": Union[datetime, str],
    },
    total=False,
)

RelevanceOutputTypeDef = TypedDict(
    "RelevanceOutputTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": OrderType,
        "ValueImportanceMap": Dict[str, int],
    },
    total=False,
)

SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {
        "Facetable": bool,
        "Searchable": bool,
        "Displayable": bool,
        "Sortable": bool,
    },
    total=False,
)

RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": bool,
        "Importance": int,
        "Duration": str,
        "RankOrder": OrderType,
        "ValueImportanceMap": Mapping[str, int],
    },
    total=False,
)

DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)

EntityDisplayDataTypeDef = TypedDict(
    "EntityDisplayDataTypeDef",
    {
        "UserName": str,
        "GroupName": str,
        "IdentifiedUserName": str,
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)

UserIdentityConfigurationTypeDef = TypedDict(
    "UserIdentityConfigurationTypeDef",
    {
        "IdentityAttributeName": str,
    },
    total=False,
)

FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": str,
        "DocumentAttributeValueType": DocumentAttributeValueTypeType,
        "DocumentAttributeValueCountPairs": List[Dict[str, Any]],
    },
    total=False,
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "DocumentAttributeKey": str,
        "Facets": Sequence[Dict[str, Any]],
        "MaxResults": int,
    },
    total=False,
)

FaqStatisticsTypeDef = TypedDict(
    "FaqStatisticsTypeDef",
    {
        "IndexedQuestionAnswersCount": int,
    },
)

FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": FaqStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
    },
    total=False,
)

FeaturedResultsSetSummaryTypeDef = TypedDict(
    "FeaturedResultsSetSummaryTypeDef",
    {
        "FeaturedResultsSetId": str,
        "FeaturedResultsSetName": str,
        "Status": FeaturedResultsSetStatusType,
        "LastUpdatedTimestamp": int,
        "CreationTimestamp": int,
    },
    total=False,
)

_RequiredGetSnapshotsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSnapshotsRequestRequestTypeDef",
    {
        "IndexId": str,
        "Interval": IntervalType,
        "MetricType": MetricTypeType,
    },
)
_OptionalGetSnapshotsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSnapshotsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetSnapshotsRequestRequestTypeDef(
    _RequiredGetSnapshotsRequestRequestTypeDef, _OptionalGetSnapshotsRequestRequestTypeDef
):
    pass


TimeRangeOutputTypeDef = TypedDict(
    "TimeRangeOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

GitHubDocumentCrawlPropertiesTypeDef = TypedDict(
    "GitHubDocumentCrawlPropertiesTypeDef",
    {
        "CrawlRepositoryDocuments": bool,
        "CrawlIssue": bool,
        "CrawlIssueComment": bool,
        "CrawlIssueCommentAttachment": bool,
        "CrawlPullRequest": bool,
        "CrawlPullRequestComment": bool,
        "CrawlPullRequestCommentAttachment": bool,
    },
    total=False,
)

SaaSConfigurationTypeDef = TypedDict(
    "SaaSConfigurationTypeDef",
    {
        "OrganizationName": str,
        "HostUrl": str,
    },
)

_RequiredMemberGroupTypeDef = TypedDict(
    "_RequiredMemberGroupTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalMemberGroupTypeDef = TypedDict(
    "_OptionalMemberGroupTypeDef",
    {
        "DataSourceId": str,
    },
    total=False,
)


class MemberGroupTypeDef(_RequiredMemberGroupTypeDef, _OptionalMemberGroupTypeDef):
    pass


MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "UserId": str,
    },
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupId": str,
        "OrderingId": int,
    },
    total=False,
)

_RequiredHighlightTypeDef = TypedDict(
    "_RequiredHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
)
_OptionalHighlightTypeDef = TypedDict(
    "_OptionalHighlightTypeDef",
    {
        "TopAnswer": bool,
        "Type": HighlightTypeType,
    },
    total=False,
)


class HighlightTypeDef(_RequiredHighlightTypeDef, _OptionalHighlightTypeDef):
    pass


_RequiredIndexConfigurationSummaryTypeDef = TypedDict(
    "_RequiredIndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": IndexStatusType,
    },
)
_OptionalIndexConfigurationSummaryTypeDef = TypedDict(
    "_OptionalIndexConfigurationSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
    },
    total=False,
)


class IndexConfigurationSummaryTypeDef(
    _RequiredIndexConfigurationSummaryTypeDef, _OptionalIndexConfigurationSummaryTypeDef
):
    pass


TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "IndexedTextDocumentsCount": int,
        "IndexedTextBytes": int,
    },
)

JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef",
    {
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
    },
)

_RequiredJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_RequiredJwtTokenTypeConfigurationTypeDef",
    {
        "KeyLocation": KeyLocationType,
    },
)
_OptionalJwtTokenTypeConfigurationTypeDef = TypedDict(
    "_OptionalJwtTokenTypeConfigurationTypeDef",
    {
        "URL": str,
        "SecretManagerArn": str,
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
        "Issuer": str,
        "ClaimRegex": str,
    },
    total=False,
)


class JwtTokenTypeConfigurationTypeDef(
    _RequiredJwtTokenTypeConfigurationTypeDef, _OptionalJwtTokenTypeConfigurationTypeDef
):
    pass


_RequiredListAccessControlConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessControlConfigurationsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListAccessControlConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessControlConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccessControlConfigurationsRequestRequestTypeDef(
    _RequiredListAccessControlConfigurationsRequestRequestTypeDef,
    _OptionalListAccessControlConfigurationsRequestRequestTypeDef,
):
    pass


TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass


_RequiredListEntityPersonasRequestRequestTypeDef = TypedDict(
    "_RequiredListEntityPersonasRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListEntityPersonasRequestRequestTypeDef = TypedDict(
    "_OptionalListEntityPersonasRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListEntityPersonasRequestRequestTypeDef(
    _RequiredListEntityPersonasRequestRequestTypeDef,
    _OptionalListEntityPersonasRequestRequestTypeDef,
):
    pass


PersonasSummaryTypeDef = TypedDict(
    "PersonasSummaryTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

_RequiredListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListExperienceEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListExperienceEntitiesRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListExperienceEntitiesRequestRequestTypeDef(
    _RequiredListExperienceEntitiesRequestRequestTypeDef,
    _OptionalListExperienceEntitiesRequestRequestTypeDef,
):
    pass


_RequiredListExperiencesRequestRequestTypeDef = TypedDict(
    "_RequiredListExperiencesRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListExperiencesRequestRequestTypeDef = TypedDict(
    "_OptionalListExperiencesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListExperiencesRequestRequestTypeDef(
    _RequiredListExperiencesRequestRequestTypeDef, _OptionalListExperiencesRequestRequestTypeDef
):
    pass


_RequiredListFaqsRequestRequestTypeDef = TypedDict(
    "_RequiredListFaqsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListFaqsRequestRequestTypeDef = TypedDict(
    "_OptionalListFaqsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFaqsRequestRequestTypeDef(
    _RequiredListFaqsRequestRequestTypeDef, _OptionalListFaqsRequestRequestTypeDef
):
    pass


_RequiredListFeaturedResultsSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListFeaturedResultsSetsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListFeaturedResultsSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListFeaturedResultsSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFeaturedResultsSetsRequestRequestTypeDef(
    _RequiredListFeaturedResultsSetsRequestRequestTypeDef,
    _OptionalListFeaturedResultsSetsRequestRequestTypeDef,
):
    pass


_RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "IndexId": str,
        "OrderingId": int,
    },
)
_OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupsOlderThanOrderingIdRequestRequestTypeDef(
    _RequiredListGroupsOlderThanOrderingIdRequestRequestTypeDef,
    _OptionalListGroupsOlderThanOrderingIdRequestRequestTypeDef,
):
    pass


ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

_RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "_RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "_OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQuerySuggestionsBlockListsRequestRequestTypeDef(
    _RequiredListQuerySuggestionsBlockListsRequestRequestTypeDef,
    _OptionalListQuerySuggestionsBlockListsRequestRequestTypeDef,
):
    pass


QuerySuggestionsBlockListSummaryTypeDef = TypedDict(
    "QuerySuggestionsBlockListSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "ItemCount": int,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

_RequiredListThesauriRequestRequestTypeDef = TypedDict(
    "_RequiredListThesauriRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalListThesauriRequestRequestTypeDef = TypedDict(
    "_OptionalListThesauriRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThesauriRequestRequestTypeDef(
    _RequiredListThesauriRequestRequestTypeDef, _OptionalListThesauriRequestRequestTypeDef
):
    pass


ThesaurusSummaryTypeDef = TypedDict(
    "ThesaurusSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": ThesaurusStatusType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortOrder": SortOrderType,
    },
)

SpellCorrectionConfigurationTypeDef = TypedDict(
    "SpellCorrectionConfigurationTypeDef",
    {
        "IncludeQuerySpellCheckSuggestions": bool,
    },
)

ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {
        "ScoreConfidence": ScoreConfidenceType,
    },
    total=False,
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Message": str,
        "Code": Literal["QUERY_LANGUAGE_INVALID_SYNTAX"],
    },
    total=False,
)

RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {
        "ResultId": str,
        "RelevanceValue": RelevanceTypeType,
    },
)

_RequiredSeedUrlConfigurationOutputTypeDef = TypedDict(
    "_RequiredSeedUrlConfigurationOutputTypeDef",
    {
        "SeedUrls": List[str],
    },
)
_OptionalSeedUrlConfigurationOutputTypeDef = TypedDict(
    "_OptionalSeedUrlConfigurationOutputTypeDef",
    {
        "WebCrawlerMode": WebCrawlerModeType,
    },
    total=False,
)


class SeedUrlConfigurationOutputTypeDef(
    _RequiredSeedUrlConfigurationOutputTypeDef, _OptionalSeedUrlConfigurationOutputTypeDef
):
    pass


_RequiredSeedUrlConfigurationTypeDef = TypedDict(
    "_RequiredSeedUrlConfigurationTypeDef",
    {
        "SeedUrls": Sequence[str],
    },
)
_OptionalSeedUrlConfigurationTypeDef = TypedDict(
    "_OptionalSeedUrlConfigurationTypeDef",
    {
        "WebCrawlerMode": WebCrawlerModeType,
    },
    total=False,
)


class SeedUrlConfigurationTypeDef(
    _RequiredSeedUrlConfigurationTypeDef, _OptionalSeedUrlConfigurationTypeDef
):
    pass


SiteMapsConfigurationOutputTypeDef = TypedDict(
    "SiteMapsConfigurationOutputTypeDef",
    {
        "SiteMaps": List[str],
    },
)

SiteMapsConfigurationTypeDef = TypedDict(
    "SiteMapsConfigurationTypeDef",
    {
        "SiteMaps": Sequence[str],
    },
)

StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

SuggestionHighlightTypeDef = TypedDict(
    "SuggestionHighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

TableCellTypeDef = TypedDict(
    "TableCellTypeDef",
    {
        "Value": str,
        "TopAnswer": bool,
        "Highlighted": bool,
        "Header": bool,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredColumnConfigurationOutputTypeDef = TypedDict(
    "_RequiredColumnConfigurationOutputTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": List[str],
    },
)
_OptionalColumnConfigurationOutputTypeDef = TypedDict(
    "_OptionalColumnConfigurationOutputTypeDef",
    {
        "DocumentTitleColumnName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class ColumnConfigurationOutputTypeDef(
    _RequiredColumnConfigurationOutputTypeDef, _OptionalColumnConfigurationOutputTypeDef
):
    pass


_RequiredColumnConfigurationTypeDef = TypedDict(
    "_RequiredColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": Sequence[str],
    },
)
_OptionalColumnConfigurationTypeDef = TypedDict(
    "_OptionalColumnConfigurationTypeDef",
    {
        "DocumentTitleColumnName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class ColumnConfigurationTypeDef(
    _RequiredColumnConfigurationTypeDef, _OptionalColumnConfigurationTypeDef
):
    pass


_RequiredGoogleDriveConfigurationOutputTypeDef = TypedDict(
    "_RequiredGoogleDriveConfigurationOutputTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGoogleDriveConfigurationOutputTypeDef = TypedDict(
    "_OptionalGoogleDriveConfigurationOutputTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "ExcludeMimeTypes": List[str],
        "ExcludeUserAccounts": List[str],
        "ExcludeSharedDrives": List[str],
    },
    total=False,
)


class GoogleDriveConfigurationOutputTypeDef(
    _RequiredGoogleDriveConfigurationOutputTypeDef, _OptionalGoogleDriveConfigurationOutputTypeDef
):
    pass


_RequiredGoogleDriveConfigurationTypeDef = TypedDict(
    "_RequiredGoogleDriveConfigurationTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGoogleDriveConfigurationTypeDef = TypedDict(
    "_OptionalGoogleDriveConfigurationTypeDef",
    {
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "ExcludeMimeTypes": Sequence[str],
        "ExcludeUserAccounts": Sequence[str],
        "ExcludeSharedDrives": Sequence[str],
    },
    total=False,
)


class GoogleDriveConfigurationTypeDef(
    _RequiredGoogleDriveConfigurationTypeDef, _OptionalGoogleDriveConfigurationTypeDef
):
    pass


_RequiredSalesforceChatterFeedConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceChatterFeedConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceChatterFeedConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceChatterFeedConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "IncludeFilterTypes": List[SalesforceChatterFeedIncludeFilterTypeType],
    },
    total=False,
)


class SalesforceChatterFeedConfigurationOutputTypeDef(
    _RequiredSalesforceChatterFeedConfigurationOutputTypeDef,
    _OptionalSalesforceChatterFeedConfigurationOutputTypeDef,
):
    pass


_RequiredSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "IncludeFilterTypes": Sequence[SalesforceChatterFeedIncludeFilterTypeType],
    },
    total=False,
)


class SalesforceChatterFeedConfigurationTypeDef(
    _RequiredSalesforceChatterFeedConfigurationTypeDef,
    _OptionalSalesforceChatterFeedConfigurationTypeDef,
):
    pass


_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef,
    _OptionalSalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef,
):
    pass


_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef,
    _OptionalSalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef,
):
    pass


_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef(
    _RequiredSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
    _OptionalSalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
):
    pass


SalesforceStandardObjectAttachmentConfigurationOutputTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)

SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)

_RequiredSalesforceStandardObjectConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceStandardObjectConfigurationOutputTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardObjectConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceStandardObjectConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceStandardObjectConfigurationOutputTypeDef(
    _RequiredSalesforceStandardObjectConfigurationOutputTypeDef,
    _OptionalSalesforceStandardObjectConfigurationOutputTypeDef,
):
    pass


_RequiredSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
    },
)
_OptionalSalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceStandardObjectConfigurationTypeDef",
    {
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SalesforceStandardObjectConfigurationTypeDef(
    _RequiredSalesforceStandardObjectConfigurationTypeDef,
    _OptionalSalesforceStandardObjectConfigurationTypeDef,
):
    pass


_RequiredServiceNowKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "_RequiredServiceNowKnowledgeArticleConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "_OptionalServiceNowKnowledgeArticleConfigurationOutputTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "FilterQuery": str,
    },
    total=False,
)


class ServiceNowKnowledgeArticleConfigurationOutputTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationOutputTypeDef,
    _OptionalServiceNowKnowledgeArticleConfigurationOutputTypeDef,
):
    pass


_RequiredServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": Sequence[str],
        "ExcludeAttachmentFilePatterns": Sequence[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "FilterQuery": str,
    },
    total=False,
)


class ServiceNowKnowledgeArticleConfigurationTypeDef(
    _RequiredServiceNowKnowledgeArticleConfigurationTypeDef,
    _OptionalServiceNowKnowledgeArticleConfigurationTypeDef,
):
    pass


_RequiredServiceNowServiceCatalogConfigurationOutputTypeDef = TypedDict(
    "_RequiredServiceNowServiceCatalogConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowServiceCatalogConfigurationOutputTypeDef = TypedDict(
    "_OptionalServiceNowServiceCatalogConfigurationOutputTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class ServiceNowServiceCatalogConfigurationOutputTypeDef(
    _RequiredServiceNowServiceCatalogConfigurationOutputTypeDef,
    _OptionalServiceNowServiceCatalogConfigurationOutputTypeDef,
):
    pass


_RequiredServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowServiceCatalogConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
    },
)
_OptionalServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowServiceCatalogConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "IncludeAttachmentFilePatterns": Sequence[str],
        "ExcludeAttachmentFilePatterns": Sequence[str],
        "DocumentTitleFieldName": str,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class ServiceNowServiceCatalogConfigurationTypeDef(
    _RequiredServiceNowServiceCatalogConfigurationTypeDef,
    _OptionalServiceNowServiceCatalogConfigurationTypeDef,
):
    pass


_RequiredWorkDocsConfigurationOutputTypeDef = TypedDict(
    "_RequiredWorkDocsConfigurationOutputTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalWorkDocsConfigurationOutputTypeDef = TypedDict(
    "_OptionalWorkDocsConfigurationOutputTypeDef",
    {
        "CrawlComments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class WorkDocsConfigurationOutputTypeDef(
    _RequiredWorkDocsConfigurationOutputTypeDef, _OptionalWorkDocsConfigurationOutputTypeDef
):
    pass


_RequiredWorkDocsConfigurationTypeDef = TypedDict(
    "_RequiredWorkDocsConfigurationTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalWorkDocsConfigurationTypeDef = TypedDict(
    "_OptionalWorkDocsConfigurationTypeDef",
    {
        "CrawlComments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class WorkDocsConfigurationTypeDef(
    _RequiredWorkDocsConfigurationTypeDef, _OptionalWorkDocsConfigurationTypeDef
):
    pass


_RequiredBoxConfigurationOutputTypeDef = TypedDict(
    "_RequiredBoxConfigurationOutputTypeDef",
    {
        "EnterpriseId": str,
        "SecretArn": str,
    },
)
_OptionalBoxConfigurationOutputTypeDef = TypedDict(
    "_OptionalBoxConfigurationOutputTypeDef",
    {
        "UseChangeLog": bool,
        "CrawlComments": bool,
        "CrawlTasks": bool,
        "CrawlWebLinks": bool,
        "FileFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "TaskFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "CommentFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "WebLinkFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
    },
    total=False,
)


class BoxConfigurationOutputTypeDef(
    _RequiredBoxConfigurationOutputTypeDef, _OptionalBoxConfigurationOutputTypeDef
):
    pass


_RequiredFsxConfigurationOutputTypeDef = TypedDict(
    "_RequiredFsxConfigurationOutputTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
    },
)
_OptionalFsxConfigurationOutputTypeDef = TypedDict(
    "_OptionalFsxConfigurationOutputTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class FsxConfigurationOutputTypeDef(
    _RequiredFsxConfigurationOutputTypeDef, _OptionalFsxConfigurationOutputTypeDef
):
    pass


_RequiredJiraConfigurationOutputTypeDef = TypedDict(
    "_RequiredJiraConfigurationOutputTypeDef",
    {
        "JiraAccountUrl": str,
        "SecretArn": str,
    },
)
_OptionalJiraConfigurationOutputTypeDef = TypedDict(
    "_OptionalJiraConfigurationOutputTypeDef",
    {
        "UseChangeLog": bool,
        "Project": List[str],
        "IssueType": List[str],
        "Status": List[str],
        "IssueSubEntityFilter": List[IssueSubEntityType],
        "AttachmentFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "CommentFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "IssueFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "ProjectFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "WorkLogFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
    },
    total=False,
)


class JiraConfigurationOutputTypeDef(
    _RequiredJiraConfigurationOutputTypeDef, _OptionalJiraConfigurationOutputTypeDef
):
    pass


_RequiredQuipConfigurationOutputTypeDef = TypedDict(
    "_RequiredQuipConfigurationOutputTypeDef",
    {
        "Domain": str,
        "SecretArn": str,
    },
)
_OptionalQuipConfigurationOutputTypeDef = TypedDict(
    "_OptionalQuipConfigurationOutputTypeDef",
    {
        "CrawlFileComments": bool,
        "CrawlChatRooms": bool,
        "CrawlAttachments": bool,
        "FolderIds": List[str],
        "ThreadFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "MessageFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "AttachmentFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
    },
    total=False,
)


class QuipConfigurationOutputTypeDef(
    _RequiredQuipConfigurationOutputTypeDef, _OptionalQuipConfigurationOutputTypeDef
):
    pass


_RequiredSlackConfigurationOutputTypeDef = TypedDict(
    "_RequiredSlackConfigurationOutputTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": List[SlackEntityType],
        "SinceCrawlDate": str,
    },
)
_OptionalSlackConfigurationOutputTypeDef = TypedDict(
    "_OptionalSlackConfigurationOutputTypeDef",
    {
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "UseChangeLog": bool,
        "CrawlBotMessage": bool,
        "ExcludeArchived": bool,
        "LookBackPeriod": int,
        "PrivateChannelFilter": List[str],
        "PublicChannelFilter": List[str],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SlackConfigurationOutputTypeDef(
    _RequiredSlackConfigurationOutputTypeDef, _OptionalSlackConfigurationOutputTypeDef
):
    pass


_RequiredAlfrescoConfigurationOutputTypeDef = TypedDict(
    "_RequiredAlfrescoConfigurationOutputTypeDef",
    {
        "SiteUrl": str,
        "SiteId": str,
        "SecretArn": str,
        "SslCertificateS3Path": S3PathTypeDef,
    },
)
_OptionalAlfrescoConfigurationOutputTypeDef = TypedDict(
    "_OptionalAlfrescoConfigurationOutputTypeDef",
    {
        "CrawlSystemFolders": bool,
        "CrawlComments": bool,
        "EntityFilter": List[AlfrescoEntityType],
        "DocumentLibraryFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "BlogFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "WikiFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
    },
    total=False,
)


class AlfrescoConfigurationOutputTypeDef(
    _RequiredAlfrescoConfigurationOutputTypeDef, _OptionalAlfrescoConfigurationOutputTypeDef
):
    pass


OnPremiseConfigurationTypeDef = TypedDict(
    "OnPremiseConfigurationTypeDef",
    {
        "HostUrl": str,
        "OrganizationName": str,
        "SslCertificateS3Path": S3PathTypeDef,
    },
)

OneDriveUsersOutputTypeDef = TypedDict(
    "OneDriveUsersOutputTypeDef",
    {
        "OneDriveUserList": List[str],
        "OneDriveUserS3Path": S3PathTypeDef,
    },
    total=False,
)

OneDriveUsersTypeDef = TypedDict(
    "OneDriveUsersTypeDef",
    {
        "OneDriveUserList": Sequence[str],
        "OneDriveUserS3Path": S3PathTypeDef,
    },
    total=False,
)

_RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
_OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceS3Path": S3PathTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class UpdateQuerySuggestionsBlockListRequestRequestTypeDef(
    _RequiredUpdateQuerySuggestionsBlockListRequestRequestTypeDef,
    _OptionalUpdateQuerySuggestionsBlockListRequestRequestTypeDef,
):
    pass


_RequiredUpdateThesaurusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateThesaurusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThesaurusRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RoleArn": str,
        "SourceS3Path": S3PathTypeDef,
    },
    total=False,
)


class UpdateThesaurusRequestRequestTypeDef(
    _RequiredUpdateThesaurusRequestRequestTypeDef, _OptionalUpdateThesaurusRequestRequestTypeDef
):
    pass


_RequiredAlfrescoConfigurationTypeDef = TypedDict(
    "_RequiredAlfrescoConfigurationTypeDef",
    {
        "SiteUrl": str,
        "SiteId": str,
        "SecretArn": str,
        "SslCertificateS3Path": S3PathTypeDef,
    },
)
_OptionalAlfrescoConfigurationTypeDef = TypedDict(
    "_OptionalAlfrescoConfigurationTypeDef",
    {
        "CrawlSystemFolders": bool,
        "CrawlComments": bool,
        "EntityFilter": Sequence[AlfrescoEntityType],
        "DocumentLibraryFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "BlogFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "WikiFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
    },
    total=False,
)


class AlfrescoConfigurationTypeDef(
    _RequiredAlfrescoConfigurationTypeDef, _OptionalAlfrescoConfigurationTypeDef
):
    pass


_RequiredBoxConfigurationTypeDef = TypedDict(
    "_RequiredBoxConfigurationTypeDef",
    {
        "EnterpriseId": str,
        "SecretArn": str,
    },
)
_OptionalBoxConfigurationTypeDef = TypedDict(
    "_OptionalBoxConfigurationTypeDef",
    {
        "UseChangeLog": bool,
        "CrawlComments": bool,
        "CrawlTasks": bool,
        "CrawlWebLinks": bool,
        "FileFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "TaskFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "CommentFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "WebLinkFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
    },
    total=False,
)


class BoxConfigurationTypeDef(_RequiredBoxConfigurationTypeDef, _OptionalBoxConfigurationTypeDef):
    pass


_RequiredFsxConfigurationTypeDef = TypedDict(
    "_RequiredFsxConfigurationTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
    },
)
_OptionalFsxConfigurationTypeDef = TypedDict(
    "_OptionalFsxConfigurationTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class FsxConfigurationTypeDef(_RequiredFsxConfigurationTypeDef, _OptionalFsxConfigurationTypeDef):
    pass


_RequiredJiraConfigurationTypeDef = TypedDict(
    "_RequiredJiraConfigurationTypeDef",
    {
        "JiraAccountUrl": str,
        "SecretArn": str,
    },
)
_OptionalJiraConfigurationTypeDef = TypedDict(
    "_OptionalJiraConfigurationTypeDef",
    {
        "UseChangeLog": bool,
        "Project": Sequence[str],
        "IssueType": Sequence[str],
        "Status": Sequence[str],
        "IssueSubEntityFilter": Sequence[IssueSubEntityType],
        "AttachmentFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "CommentFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "IssueFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "ProjectFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "WorkLogFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
    },
    total=False,
)


class JiraConfigurationTypeDef(
    _RequiredJiraConfigurationTypeDef, _OptionalJiraConfigurationTypeDef
):
    pass


_RequiredQuipConfigurationTypeDef = TypedDict(
    "_RequiredQuipConfigurationTypeDef",
    {
        "Domain": str,
        "SecretArn": str,
    },
)
_OptionalQuipConfigurationTypeDef = TypedDict(
    "_OptionalQuipConfigurationTypeDef",
    {
        "CrawlFileComments": bool,
        "CrawlChatRooms": bool,
        "CrawlAttachments": bool,
        "FolderIds": Sequence[str],
        "ThreadFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "MessageFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "AttachmentFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
    },
    total=False,
)


class QuipConfigurationTypeDef(
    _RequiredQuipConfigurationTypeDef, _OptionalQuipConfigurationTypeDef
):
    pass


_RequiredSlackConfigurationTypeDef = TypedDict(
    "_RequiredSlackConfigurationTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": Sequence[SlackEntityType],
        "SinceCrawlDate": str,
    },
)
_OptionalSlackConfigurationTypeDef = TypedDict(
    "_OptionalSlackConfigurationTypeDef",
    {
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "UseChangeLog": bool,
        "CrawlBotMessage": bool,
        "ExcludeArchived": bool,
        "LookBackPeriod": int,
        "PrivateChannelFilter": Sequence[str],
        "PublicChannelFilter": Sequence[str],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
    },
    total=False,
)


class SlackConfigurationTypeDef(
    _RequiredSlackConfigurationTypeDef, _OptionalSlackConfigurationTypeDef
):
    pass


AssociateEntitiesToExperienceRequestRequestTypeDef = TypedDict(
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence[EntityConfigurationTypeDef],
    },
)

DisassociateEntitiesFromExperienceRequestRequestTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence[EntityConfigurationTypeDef],
    },
)

AssociateEntitiesToExperienceResponseTypeDef = TypedDict(
    "AssociateEntitiesToExperienceResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociatePersonasToEntitiesResponseTypeDef = TypedDict(
    "AssociatePersonasToEntitiesResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAccessControlConfigurationResponseTypeDef = TypedDict(
    "CreateAccessControlConfigurationResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateExperienceResponseTypeDef = TypedDict(
    "CreateExperienceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFaqResponseTypeDef = TypedDict(
    "CreateFaqResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateThesaurusResponseTypeDef = TypedDict(
    "CreateThesaurusResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeFaqResponseTypeDef = TypedDict(
    "DescribeFaqResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": S3PathTypeDef,
        "Status": FaqStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "SourceS3Path": S3PathTypeDef,
        "ItemCount": int,
        "FileSizeBytes": int,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeThesaurusResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "Status": ThesaurusStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "RoleArn": str,
        "SourceS3Path": S3PathTypeDef,
        "FileSizeBytes": int,
        "TermCount": int,
        "SynonymRuleCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociateEntitiesFromExperienceResponseTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisassociatePersonasFromEntitiesResponseTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAccessControlConfigurationsResponseTypeDef = TypedDict(
    "ListAccessControlConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "AccessControlConfigurations": List[AccessControlConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "ExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AssociatePersonasToEntitiesRequestRequestTypeDef = TypedDict(
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Personas": Sequence[EntityPersonaConfigurationTypeDef],
    },
)

AttributeSuggestionsDescribeConfigTypeDef = TypedDict(
    "AttributeSuggestionsDescribeConfigTypeDef",
    {
        "SuggestableConfigList": List[SuggestableConfigTypeDef],
        "AttributeSuggestionsMode": AttributeSuggestionsModeType,
    },
    total=False,
)

AttributeSuggestionsUpdateConfigTypeDef = TypedDict(
    "AttributeSuggestionsUpdateConfigTypeDef",
    {
        "SuggestableConfigList": Sequence[SuggestableConfigTypeDef],
        "AttributeSuggestionsMode": AttributeSuggestionsModeType,
    },
    total=False,
)

AuthenticationConfigurationOutputTypeDef = TypedDict(
    "AuthenticationConfigurationOutputTypeDef",
    {
        "BasicAuthentication": List[BasicAuthenticationConfigurationTypeDef],
    },
    total=False,
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "BasicAuthentication": Sequence[BasicAuthenticationConfigurationTypeDef],
    },
    total=False,
)

_RequiredBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentIdList": Sequence[str],
    },
)
_OptionalBatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteDocumentRequestRequestTypeDef",
    {
        "DataSourceSyncJobMetricTarget": DataSourceSyncJobMetricTargetTypeDef,
    },
    total=False,
)


class BatchDeleteDocumentRequestRequestTypeDef(
    _RequiredBatchDeleteDocumentRequestRequestTypeDef,
    _OptionalBatchDeleteDocumentRequestRequestTypeDef,
):
    pass


BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "FailedDocuments": List[BatchDeleteDocumentResponseFailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchDeleteFeaturedResultsSetResponseTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetResponseTypeDef",
    {
        "Errors": List[BatchDeleteFeaturedResultsSetErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchGetDocumentStatusResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseTypeDef",
    {
        "Errors": List[BatchGetDocumentStatusResponseErrorTypeDef],
        "DocumentStatusList": List[StatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "FailedDocuments": List[BatchPutDocumentResponseFailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConfluenceAttachmentConfigurationOutputTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationOutputTypeDef",
    {
        "CrawlAttachments": bool,
        "AttachmentFieldMappings": List[ConfluenceAttachmentToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluenceAttachmentConfigurationTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "AttachmentFieldMappings": Sequence[ConfluenceAttachmentToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluenceBlogConfigurationOutputTypeDef = TypedDict(
    "ConfluenceBlogConfigurationOutputTypeDef",
    {
        "BlogFieldMappings": List[ConfluenceBlogToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {
        "BlogFieldMappings": Sequence[ConfluenceBlogToIndexFieldMappingTypeDef],
    },
    total=False,
)

_RequiredSharePointConfigurationOutputTypeDef = TypedDict(
    "_RequiredSharePointConfigurationOutputTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": List[str],
        "SecretArn": str,
    },
)
_OptionalSharePointConfigurationOutputTypeDef = TypedDict(
    "_OptionalSharePointConfigurationOutputTypeDef",
    {
        "CrawlAttachments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "DocumentTitleFieldName": str,
        "DisableLocalGroups": bool,
        "SslCertificateS3Path": S3PathTypeDef,
        "AuthenticationType": SharePointOnlineAuthenticationTypeType,
        "ProxyConfiguration": ProxyConfigurationTypeDef,
    },
    total=False,
)


class SharePointConfigurationOutputTypeDef(
    _RequiredSharePointConfigurationOutputTypeDef, _OptionalSharePointConfigurationOutputTypeDef
):
    pass


_RequiredSharePointConfigurationTypeDef = TypedDict(
    "_RequiredSharePointConfigurationTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": Sequence[str],
        "SecretArn": str,
    },
)
_OptionalSharePointConfigurationTypeDef = TypedDict(
    "_OptionalSharePointConfigurationTypeDef",
    {
        "CrawlAttachments": bool,
        "UseChangeLog": bool,
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "DocumentTitleFieldName": str,
        "DisableLocalGroups": bool,
        "SslCertificateS3Path": S3PathTypeDef,
        "AuthenticationType": SharePointOnlineAuthenticationTypeType,
        "ProxyConfiguration": ProxyConfigurationTypeDef,
    },
    total=False,
)


class SharePointConfigurationTypeDef(
    _RequiredSharePointConfigurationTypeDef, _OptionalSharePointConfigurationTypeDef
):
    pass


ConfluencePageConfigurationOutputTypeDef = TypedDict(
    "ConfluencePageConfigurationOutputTypeDef",
    {
        "PageFieldMappings": List[ConfluencePageToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {
        "PageFieldMappings": Sequence[ConfluencePageToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluenceSpaceConfigurationOutputTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationOutputTypeDef",
    {
        "CrawlPersonalSpaces": bool,
        "CrawlArchivedSpaces": bool,
        "IncludeSpaces": List[str],
        "ExcludeSpaces": List[str],
        "SpaceFieldMappings": List[ConfluenceSpaceToIndexFieldMappingTypeDef],
    },
    total=False,
)

ConfluenceSpaceConfigurationTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationTypeDef",
    {
        "CrawlPersonalSpaces": bool,
        "CrawlArchivedSpaces": bool,
        "IncludeSpaces": Sequence[str],
        "ExcludeSpaces": Sequence[str],
        "SpaceFieldMappings": Sequence[ConfluenceSpaceToIndexFieldMappingTypeDef],
    },
    total=False,
)

SpellCorrectedQueryTypeDef = TypedDict(
    "SpellCorrectedQueryTypeDef",
    {
        "SuggestedQueryText": str,
        "Corrections": List[CorrectionTypeDef],
    },
    total=False,
)

HierarchicalPrincipalOutputTypeDef = TypedDict(
    "HierarchicalPrincipalOutputTypeDef",
    {
        "PrincipalList": List[PrincipalTypeDef],
    },
)

HierarchicalPrincipalTypeDef = TypedDict(
    "HierarchicalPrincipalTypeDef",
    {
        "PrincipalList": Sequence[PrincipalTypeDef],
    },
)

_RequiredCreateFaqRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFaqRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "S3Path": S3PathTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateFaqRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFaqRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "FileFormat": FaqFileFormatType,
        "ClientToken": str,
        "LanguageCode": str,
    },
    total=False,
)


class CreateFaqRequestRequestTypeDef(
    _RequiredCreateFaqRequestRequestTypeDef, _OptionalCreateFaqRequestRequestTypeDef
):
    pass


_RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "SourceS3Path": S3PathTypeDef,
        "RoleArn": str,
    },
)
_OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateQuerySuggestionsBlockListRequestRequestTypeDef(
    _RequiredCreateQuerySuggestionsBlockListRequestRequestTypeDef,
    _OptionalCreateQuerySuggestionsBlockListRequestRequestTypeDef,
):
    pass


_RequiredCreateThesaurusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThesaurusRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "RoleArn": str,
        "SourceS3Path": S3PathTypeDef,
    },
)
_OptionalCreateThesaurusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThesaurusRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Sequence[TagTypeDef],
        "ClientToken": str,
    },
    total=False,
)


class CreateThesaurusRequestRequestTypeDef(
    _RequiredCreateThesaurusRequestRequestTypeDef, _OptionalCreateThesaurusRequestRequestTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

_RequiredCreateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetName": str,
    },
)
_OptionalCreateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFeaturedResultsSetRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Status": FeaturedResultsSetStatusType,
        "QueryTexts": Sequence[str],
        "FeaturedDocuments": Sequence[FeaturedDocumentTypeDef],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFeaturedResultsSetRequestRequestTypeDef(
    _RequiredCreateFeaturedResultsSetRequestRequestTypeDef,
    _OptionalCreateFeaturedResultsSetRequestRequestTypeDef,
):
    pass


FeaturedResultsSetTypeDef = TypedDict(
    "FeaturedResultsSetTypeDef",
    {
        "FeaturedResultsSetId": str,
        "FeaturedResultsSetName": str,
        "Description": str,
        "Status": FeaturedResultsSetStatusType,
        "QueryTexts": List[str],
        "FeaturedDocuments": List[FeaturedDocumentTypeDef],
        "LastUpdatedTimestamp": int,
        "CreationTimestamp": int,
    },
    total=False,
)

_RequiredUpdateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetId": str,
    },
)
_OptionalUpdateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeaturedResultsSetRequestRequestTypeDef",
    {
        "FeaturedResultsSetName": str,
        "Description": str,
        "Status": FeaturedResultsSetStatusType,
        "QueryTexts": Sequence[str],
        "FeaturedDocuments": Sequence[FeaturedDocumentTypeDef],
    },
    total=False,
)


class UpdateFeaturedResultsSetRequestRequestTypeDef(
    _RequiredUpdateFeaturedResultsSetRequestRequestTypeDef,
    _OptionalUpdateFeaturedResultsSetRequestRequestTypeDef,
):
    pass


UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "Token": str,
        "UserId": str,
        "Groups": Sequence[str],
        "DataSourceGroups": Sequence[DataSourceGroupTypeDef],
    },
    total=False,
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "SummaryItems": List[DataSourceSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "ExecutionId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Status": DataSourceSyncJobStatusType,
        "ErrorMessage": str,
        "ErrorCode": ErrorCodeType,
        "DataSourceErrorCode": str,
        "Metrics": DataSourceSyncJobMetricsTypeDef,
    },
    total=False,
)

ExperiencesSummaryTypeDef = TypedDict(
    "ExperiencesSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "CreatedAt": datetime,
        "Status": ExperienceStatusType,
        "Endpoints": List[ExperienceEndpointTypeDef],
    },
    total=False,
)

DescribeFeaturedResultsSetResponseTypeDef = TypedDict(
    "DescribeFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSetId": str,
        "FeaturedResultsSetName": str,
        "Description": str,
        "Status": FeaturedResultsSetStatusType,
        "QueryTexts": List[str],
        "FeaturedDocumentsWithMetadata": List[FeaturedDocumentWithMetadataTypeDef],
        "FeaturedDocumentsMissing": List[FeaturedDocumentMissingTypeDef],
        "LastUpdatedTimestamp": int,
        "CreationTimestamp": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribePrincipalMappingResponseTypeDef = TypedDict(
    "DescribePrincipalMappingResponseTypeDef",
    {
        "IndexId": str,
        "DataSourceId": str,
        "GroupId": str,
        "GroupOrderingIdSummaries": List[GroupOrderingIdSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDocumentAttributeConditionOutputTypeDef = TypedDict(
    "_RequiredDocumentAttributeConditionOutputTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
    },
)
_OptionalDocumentAttributeConditionOutputTypeDef = TypedDict(
    "_OptionalDocumentAttributeConditionOutputTypeDef",
    {
        "ConditionOnValue": DocumentAttributeValueOutputTypeDef,
    },
    total=False,
)


class DocumentAttributeConditionOutputTypeDef(
    _RequiredDocumentAttributeConditionOutputTypeDef,
    _OptionalDocumentAttributeConditionOutputTypeDef,
):
    pass


DocumentAttributeOutputTypeDef = TypedDict(
    "DocumentAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": DocumentAttributeValueOutputTypeDef,
    },
)

DocumentAttributeTargetOutputTypeDef = TypedDict(
    "DocumentAttributeTargetOutputTypeDef",
    {
        "TargetDocumentAttributeKey": str,
        "TargetDocumentAttributeValueDeletion": bool,
        "TargetDocumentAttributeValue": DocumentAttributeValueOutputTypeDef,
    },
    total=False,
)

DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {
        "DocumentAttributeValue": DocumentAttributeValueOutputTypeDef,
        "Count": int,
        "FacetResults": List[Dict[str, Any]],
    },
    total=False,
)

_RequiredDocumentAttributeConditionTypeDef = TypedDict(
    "_RequiredDocumentAttributeConditionTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
    },
)
_OptionalDocumentAttributeConditionTypeDef = TypedDict(
    "_OptionalDocumentAttributeConditionTypeDef",
    {
        "ConditionOnValue": DocumentAttributeValueTypeDef,
    },
    total=False,
)


class DocumentAttributeConditionTypeDef(
    _RequiredDocumentAttributeConditionTypeDef, _OptionalDocumentAttributeConditionTypeDef
):
    pass


DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "TargetDocumentAttributeKey": str,
        "TargetDocumentAttributeValueDeletion": bool,
        "TargetDocumentAttributeValue": DocumentAttributeValueTypeDef,
    },
    total=False,
)

DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "Key": str,
        "Value": DocumentAttributeValueTypeDef,
    },
)

_RequiredDocumentMetadataConfigurationOutputTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationOutputTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
    },
)
_OptionalDocumentMetadataConfigurationOutputTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationOutputTypeDef",
    {
        "Relevance": RelevanceOutputTypeDef,
        "Search": SearchTypeDef,
    },
    total=False,
)


class DocumentMetadataConfigurationOutputTypeDef(
    _RequiredDocumentMetadataConfigurationOutputTypeDef,
    _OptionalDocumentMetadataConfigurationOutputTypeDef,
):
    pass


_RequiredDocumentMetadataConfigurationTypeDef = TypedDict(
    "_RequiredDocumentMetadataConfigurationTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
    },
)
_OptionalDocumentMetadataConfigurationTypeDef = TypedDict(
    "_OptionalDocumentMetadataConfigurationTypeDef",
    {
        "Relevance": RelevanceTypeDef,
        "Search": SearchTypeDef,
    },
    total=False,
)


class DocumentMetadataConfigurationTypeDef(
    _RequiredDocumentMetadataConfigurationTypeDef, _OptionalDocumentMetadataConfigurationTypeDef
):
    pass


DocumentRelevanceConfigurationTypeDef = TypedDict(
    "DocumentRelevanceConfigurationTypeDef",
    {
        "Name": str,
        "Relevance": RelevanceTypeDef,
    },
)

_RequiredS3DataSourceConfigurationOutputTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationOutputTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3DataSourceConfigurationOutputTypeDef = TypedDict(
    "_OptionalS3DataSourceConfigurationOutputTypeDef",
    {
        "InclusionPrefixes": List[str],
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "DocumentsMetadataConfiguration": DocumentsMetadataConfigurationTypeDef,
        "AccessControlListConfiguration": AccessControlListConfigurationTypeDef,
    },
    total=False,
)


class S3DataSourceConfigurationOutputTypeDef(
    _RequiredS3DataSourceConfigurationOutputTypeDef, _OptionalS3DataSourceConfigurationOutputTypeDef
):
    pass


_RequiredS3DataSourceConfigurationTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3DataSourceConfigurationTypeDef = TypedDict(
    "_OptionalS3DataSourceConfigurationTypeDef",
    {
        "InclusionPrefixes": Sequence[str],
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "DocumentsMetadataConfiguration": DocumentsMetadataConfigurationTypeDef,
        "AccessControlListConfiguration": AccessControlListConfigurationTypeDef,
    },
    total=False,
)


class S3DataSourceConfigurationTypeDef(
    _RequiredS3DataSourceConfigurationTypeDef, _OptionalS3DataSourceConfigurationTypeDef
):
    pass


ExperienceEntitiesSummaryTypeDef = TypedDict(
    "ExperienceEntitiesSummaryTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
        "DisplayData": EntityDisplayDataTypeDef,
    },
    total=False,
)

ExperienceConfigurationOutputTypeDef = TypedDict(
    "ExperienceConfigurationOutputTypeDef",
    {
        "ContentSourceConfiguration": ContentSourceConfigurationOutputTypeDef,
        "UserIdentityConfiguration": UserIdentityConfigurationTypeDef,
    },
    total=False,
)

ExperienceConfigurationTypeDef = TypedDict(
    "ExperienceConfigurationTypeDef",
    {
        "ContentSourceConfiguration": ContentSourceConfigurationTypeDef,
        "UserIdentityConfiguration": UserIdentityConfigurationTypeDef,
    },
    total=False,
)

ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {
        "NextToken": str,
        "FaqSummaryItems": List[FaqSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListFeaturedResultsSetsResponseTypeDef = TypedDict(
    "ListFeaturedResultsSetsResponseTypeDef",
    {
        "FeaturedResultsSetSummaryItems": List[FeaturedResultsSetSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSnapshotsResponseTypeDef = TypedDict(
    "GetSnapshotsResponseTypeDef",
    {
        "SnapShotTimeFilter": TimeRangeOutputTypeDef,
        "SnapshotsDataHeader": List[str],
        "SnapshotsData": List[List[str]],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "MemberGroups": Sequence[MemberGroupTypeDef],
        "MemberUsers": Sequence[MemberUserTypeDef],
        "S3PathforGroupMembers": S3PathTypeDef,
    },
    total=False,
)

ListGroupsOlderThanOrderingIdResponseTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    {
        "GroupsSummaries": List[GroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List[HighlightTypeDef],
    },
    total=False,
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List[IndexConfigurationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "FaqStatistics": FaqStatisticsTypeDef,
        "TextDocumentStatistics": TextDocumentStatisticsTypeDef,
    },
)

UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": JwtTokenTypeConfigurationTypeDef,
        "JsonTokenTypeConfiguration": JsonTokenTypeConfigurationTypeDef,
    },
    total=False,
)

_RequiredListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartTimeFilter": TimeRangeTypeDef,
        "StatusFilter": DataSourceSyncJobStatusType,
    },
    total=False,
)


class ListDataSourceSyncJobsRequestRequestTypeDef(
    _RequiredListDataSourceSyncJobsRequestRequestTypeDef,
    _OptionalListDataSourceSyncJobsRequestRequestTypeDef,
):
    pass


ListEntityPersonasResponseTypeDef = TypedDict(
    "ListEntityPersonasResponseTypeDef",
    {
        "SummaryItems": List[PersonasSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListQuerySuggestionsBlockListsResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    {
        "BlockListSummaryItems": List[QuerySuggestionsBlockListSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListThesauriResponseTypeDef = TypedDict(
    "ListThesauriResponseTypeDef",
    {
        "NextToken": str,
        "ThesaurusSummaryItems": List[ThesaurusSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_RequiredSubmitFeedbackRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryId": str,
    },
)
_OptionalSubmitFeedbackRequestRequestTypeDef = TypedDict(
    "_OptionalSubmitFeedbackRequestRequestTypeDef",
    {
        "ClickFeedbackItems": Sequence[ClickFeedbackTypeDef],
        "RelevanceFeedbackItems": Sequence[RelevanceFeedbackTypeDef],
    },
    total=False,
)


class SubmitFeedbackRequestRequestTypeDef(
    _RequiredSubmitFeedbackRequestRequestTypeDef, _OptionalSubmitFeedbackRequestRequestTypeDef
):
    pass


UrlsOutputTypeDef = TypedDict(
    "UrlsOutputTypeDef",
    {
        "SeedUrlConfiguration": SeedUrlConfigurationOutputTypeDef,
        "SiteMapsConfiguration": SiteMapsConfigurationOutputTypeDef,
    },
    total=False,
)

UrlsTypeDef = TypedDict(
    "UrlsTypeDef",
    {
        "SeedUrlConfiguration": SeedUrlConfigurationTypeDef,
        "SiteMapsConfiguration": SiteMapsConfigurationTypeDef,
    },
    total=False,
)

SuggestionTextWithHighlightsTypeDef = TypedDict(
    "SuggestionTextWithHighlightsTypeDef",
    {
        "Text": str,
        "Highlights": List[SuggestionHighlightTypeDef],
    },
    total=False,
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "Cells": List[TableCellTypeDef],
    },
    total=False,
)

_RequiredDatabaseConfigurationOutputTypeDef = TypedDict(
    "_RequiredDatabaseConfigurationOutputTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": ConnectionConfigurationTypeDef,
        "ColumnConfiguration": ColumnConfigurationOutputTypeDef,
    },
)
_OptionalDatabaseConfigurationOutputTypeDef = TypedDict(
    "_OptionalDatabaseConfigurationOutputTypeDef",
    {
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "AclConfiguration": AclConfigurationTypeDef,
        "SqlConfiguration": SqlConfigurationTypeDef,
    },
    total=False,
)


class DatabaseConfigurationOutputTypeDef(
    _RequiredDatabaseConfigurationOutputTypeDef, _OptionalDatabaseConfigurationOutputTypeDef
):
    pass


_RequiredDatabaseConfigurationTypeDef = TypedDict(
    "_RequiredDatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": ConnectionConfigurationTypeDef,
        "ColumnConfiguration": ColumnConfigurationTypeDef,
    },
)
_OptionalDatabaseConfigurationTypeDef = TypedDict(
    "_OptionalDatabaseConfigurationTypeDef",
    {
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "AclConfiguration": AclConfigurationTypeDef,
        "SqlConfiguration": SqlConfigurationTypeDef,
    },
    total=False,
)


class DatabaseConfigurationTypeDef(
    _RequiredDatabaseConfigurationTypeDef, _OptionalDatabaseConfigurationTypeDef
):
    pass


_RequiredSalesforceKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceKnowledgeArticleConfigurationOutputTypeDef",
    {
        "IncludedStates": List[SalesforceKnowledgeArticleStateType],
    },
)
_OptionalSalesforceKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceKnowledgeArticleConfigurationOutputTypeDef",
    {
        "StandardKnowledgeArticleTypeConfiguration": (
            SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef
        ),
        "CustomKnowledgeArticleTypeConfigurations": List[
            SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef
        ],
    },
    total=False,
)


class SalesforceKnowledgeArticleConfigurationOutputTypeDef(
    _RequiredSalesforceKnowledgeArticleConfigurationOutputTypeDef,
    _OptionalSalesforceKnowledgeArticleConfigurationOutputTypeDef,
):
    pass


_RequiredSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "IncludedStates": Sequence[SalesforceKnowledgeArticleStateType],
    },
)
_OptionalSalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "StandardKnowledgeArticleTypeConfiguration": (
            SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef
        ),
        "CustomKnowledgeArticleTypeConfigurations": Sequence[
            SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef
        ],
    },
    total=False,
)


class SalesforceKnowledgeArticleConfigurationTypeDef(
    _RequiredSalesforceKnowledgeArticleConfigurationTypeDef,
    _OptionalSalesforceKnowledgeArticleConfigurationTypeDef,
):
    pass


_RequiredServiceNowConfigurationOutputTypeDef = TypedDict(
    "_RequiredServiceNowConfigurationOutputTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
    },
)
_OptionalServiceNowConfigurationOutputTypeDef = TypedDict(
    "_OptionalServiceNowConfigurationOutputTypeDef",
    {
        "KnowledgeArticleConfiguration": ServiceNowKnowledgeArticleConfigurationOutputTypeDef,
        "ServiceCatalogConfiguration": ServiceNowServiceCatalogConfigurationOutputTypeDef,
        "AuthenticationType": ServiceNowAuthenticationTypeType,
    },
    total=False,
)


class ServiceNowConfigurationOutputTypeDef(
    _RequiredServiceNowConfigurationOutputTypeDef, _OptionalServiceNowConfigurationOutputTypeDef
):
    pass


_RequiredServiceNowConfigurationTypeDef = TypedDict(
    "_RequiredServiceNowConfigurationTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
    },
)
_OptionalServiceNowConfigurationTypeDef = TypedDict(
    "_OptionalServiceNowConfigurationTypeDef",
    {
        "KnowledgeArticleConfiguration": ServiceNowKnowledgeArticleConfigurationTypeDef,
        "ServiceCatalogConfiguration": ServiceNowServiceCatalogConfigurationTypeDef,
        "AuthenticationType": ServiceNowAuthenticationTypeType,
    },
    total=False,
)


class ServiceNowConfigurationTypeDef(
    _RequiredServiceNowConfigurationTypeDef, _OptionalServiceNowConfigurationTypeDef
):
    pass


_RequiredGitHubConfigurationOutputTypeDef = TypedDict(
    "_RequiredGitHubConfigurationOutputTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGitHubConfigurationOutputTypeDef = TypedDict(
    "_OptionalGitHubConfigurationOutputTypeDef",
    {
        "SaaSConfiguration": SaaSConfigurationTypeDef,
        "OnPremiseConfiguration": OnPremiseConfigurationTypeDef,
        "Type": TypeType,
        "UseChangeLog": bool,
        "GitHubDocumentCrawlProperties": GitHubDocumentCrawlPropertiesTypeDef,
        "RepositoryFilter": List[str],
        "InclusionFolderNamePatterns": List[str],
        "InclusionFileTypePatterns": List[str],
        "InclusionFileNamePatterns": List[str],
        "ExclusionFolderNamePatterns": List[str],
        "ExclusionFileTypePatterns": List[str],
        "ExclusionFileNamePatterns": List[str],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "GitHubRepositoryConfigurationFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "GitHubCommitConfigurationFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "GitHubIssueDocumentConfigurationFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "GitHubIssueCommentConfigurationFieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "GitHubIssueAttachmentConfigurationFieldMappings": List[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestCommentConfigurationFieldMappings": List[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestDocumentConfigurationFieldMappings": List[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": List[
            DataSourceToIndexFieldMappingTypeDef
        ],
    },
    total=False,
)


class GitHubConfigurationOutputTypeDef(
    _RequiredGitHubConfigurationOutputTypeDef, _OptionalGitHubConfigurationOutputTypeDef
):
    pass


_RequiredGitHubConfigurationTypeDef = TypedDict(
    "_RequiredGitHubConfigurationTypeDef",
    {
        "SecretArn": str,
    },
)
_OptionalGitHubConfigurationTypeDef = TypedDict(
    "_OptionalGitHubConfigurationTypeDef",
    {
        "SaaSConfiguration": SaaSConfigurationTypeDef,
        "OnPremiseConfiguration": OnPremiseConfigurationTypeDef,
        "Type": TypeType,
        "UseChangeLog": bool,
        "GitHubDocumentCrawlProperties": GitHubDocumentCrawlPropertiesTypeDef,
        "RepositoryFilter": Sequence[str],
        "InclusionFolderNamePatterns": Sequence[str],
        "InclusionFileTypePatterns": Sequence[str],
        "InclusionFileNamePatterns": Sequence[str],
        "ExclusionFolderNamePatterns": Sequence[str],
        "ExclusionFileTypePatterns": Sequence[str],
        "ExclusionFileNamePatterns": Sequence[str],
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "GitHubRepositoryConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubCommitConfigurationFieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "GitHubIssueDocumentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubIssueCommentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubIssueAttachmentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestCommentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestDocumentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
        "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": Sequence[
            DataSourceToIndexFieldMappingTypeDef
        ],
    },
    total=False,
)


class GitHubConfigurationTypeDef(
    _RequiredGitHubConfigurationTypeDef, _OptionalGitHubConfigurationTypeDef
):
    pass


_RequiredOneDriveConfigurationOutputTypeDef = TypedDict(
    "_RequiredOneDriveConfigurationOutputTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": OneDriveUsersOutputTypeDef,
    },
)
_OptionalOneDriveConfigurationOutputTypeDef = TypedDict(
    "_OptionalOneDriveConfigurationOutputTypeDef",
    {
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "FieldMappings": List[DataSourceToIndexFieldMappingTypeDef],
        "DisableLocalGroups": bool,
    },
    total=False,
)


class OneDriveConfigurationOutputTypeDef(
    _RequiredOneDriveConfigurationOutputTypeDef, _OptionalOneDriveConfigurationOutputTypeDef
):
    pass


_RequiredOneDriveConfigurationTypeDef = TypedDict(
    "_RequiredOneDriveConfigurationTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": OneDriveUsersTypeDef,
    },
)
_OptionalOneDriveConfigurationTypeDef = TypedDict(
    "_OptionalOneDriveConfigurationTypeDef",
    {
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "FieldMappings": Sequence[DataSourceToIndexFieldMappingTypeDef],
        "DisableLocalGroups": bool,
    },
    total=False,
)


class OneDriveConfigurationTypeDef(
    _RequiredOneDriveConfigurationTypeDef, _OptionalOneDriveConfigurationTypeDef
):
    pass


DescribeQuerySuggestionsConfigResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    {
        "Mode": ModeType,
        "Status": QuerySuggestionsStatusType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "LastSuggestionsBuildTime": datetime,
        "LastClearTime": datetime,
        "TotalSuggestionsCount": int,
        "AttributeSuggestionsConfig": AttributeSuggestionsDescribeConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "Mode": ModeType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "AttributeSuggestionsConfig": AttributeSuggestionsUpdateConfigTypeDef,
    },
    total=False,
)


class UpdateQuerySuggestionsConfigRequestRequestTypeDef(
    _RequiredUpdateQuerySuggestionsConfigRequestRequestTypeDef,
    _OptionalUpdateQuerySuggestionsConfigRequestRequestTypeDef,
):
    pass


_RequiredConfluenceConfigurationOutputTypeDef = TypedDict(
    "_RequiredConfluenceConfigurationOutputTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
    },
)
_OptionalConfluenceConfigurationOutputTypeDef = TypedDict(
    "_OptionalConfluenceConfigurationOutputTypeDef",
    {
        "SpaceConfiguration": ConfluenceSpaceConfigurationOutputTypeDef,
        "PageConfiguration": ConfluencePageConfigurationOutputTypeDef,
        "BlogConfiguration": ConfluenceBlogConfigurationOutputTypeDef,
        "AttachmentConfiguration": ConfluenceAttachmentConfigurationOutputTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "InclusionPatterns": List[str],
        "ExclusionPatterns": List[str],
        "ProxyConfiguration": ProxyConfigurationTypeDef,
        "AuthenticationType": ConfluenceAuthenticationTypeType,
    },
    total=False,
)


class ConfluenceConfigurationOutputTypeDef(
    _RequiredConfluenceConfigurationOutputTypeDef, _OptionalConfluenceConfigurationOutputTypeDef
):
    pass


_RequiredConfluenceConfigurationTypeDef = TypedDict(
    "_RequiredConfluenceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
    },
)
_OptionalConfluenceConfigurationTypeDef = TypedDict(
    "_OptionalConfluenceConfigurationTypeDef",
    {
        "SpaceConfiguration": ConfluenceSpaceConfigurationTypeDef,
        "PageConfiguration": ConfluencePageConfigurationTypeDef,
        "BlogConfiguration": ConfluenceBlogConfigurationTypeDef,
        "AttachmentConfiguration": ConfluenceAttachmentConfigurationTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "InclusionPatterns": Sequence[str],
        "ExclusionPatterns": Sequence[str],
        "ProxyConfiguration": ProxyConfigurationTypeDef,
        "AuthenticationType": ConfluenceAuthenticationTypeType,
    },
    total=False,
)


class ConfluenceConfigurationTypeDef(
    _RequiredConfluenceConfigurationTypeDef, _OptionalConfluenceConfigurationTypeDef
):
    pass


DescribeAccessControlConfigurationResponseTypeDef = TypedDict(
    "DescribeAccessControlConfigurationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "ErrorMessage": str,
        "AccessControlList": List[PrincipalTypeDef],
        "HierarchicalAccessControlList": List[HierarchicalPrincipalOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
    },
)
_OptionalCreateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessControlConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "AccessControlList": Sequence[PrincipalTypeDef],
        "HierarchicalAccessControlList": Sequence[HierarchicalPrincipalTypeDef],
        "ClientToken": str,
    },
    total=False,
)


class CreateAccessControlConfigurationRequestRequestTypeDef(
    _RequiredCreateAccessControlConfigurationRequestRequestTypeDef,
    _OptionalCreateAccessControlConfigurationRequestRequestTypeDef,
):
    pass


_RequiredUpdateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
_OptionalUpdateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessControlConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "AccessControlList": Sequence[PrincipalTypeDef],
        "HierarchicalAccessControlList": Sequence[HierarchicalPrincipalTypeDef],
    },
    total=False,
)


class UpdateAccessControlConfigurationRequestRequestTypeDef(
    _RequiredUpdateAccessControlConfigurationRequestRequestTypeDef,
    _OptionalUpdateAccessControlConfigurationRequestRequestTypeDef,
):
    pass


CreateFeaturedResultsSetResponseTypeDef = TypedDict(
    "CreateFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSet": FeaturedResultsSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFeaturedResultsSetResponseTypeDef = TypedDict(
    "UpdateFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSet": FeaturedResultsSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AttributeSuggestionsGetConfigTypeDef = TypedDict(
    "AttributeSuggestionsGetConfigTypeDef",
    {
        "SuggestionAttributes": Sequence[str],
        "AdditionalResponseAttributes": Sequence[str],
        "AttributeFilter": "AttributeFilterTypeDef",
        "UserContext": UserContextTypeDef,
    },
    total=False,
)

ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "History": List[DataSourceSyncJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListExperiencesResponseTypeDef = TypedDict(
    "ListExperiencesResponseTypeDef",
    {
        "SummaryItems": List[ExperiencesSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredHookConfigurationOutputTypeDef = TypedDict(
    "_RequiredHookConfigurationOutputTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
    },
)
_OptionalHookConfigurationOutputTypeDef = TypedDict(
    "_OptionalHookConfigurationOutputTypeDef",
    {
        "InvocationCondition": DocumentAttributeConditionOutputTypeDef,
    },
    total=False,
)


class HookConfigurationOutputTypeDef(
    _RequiredHookConfigurationOutputTypeDef, _OptionalHookConfigurationOutputTypeDef
):
    pass


RetrieveResultItemTypeDef = TypedDict(
    "RetrieveResultItemTypeDef",
    {
        "Id": str,
        "DocumentId": str,
        "DocumentTitle": str,
        "Content": str,
        "DocumentURI": str,
        "DocumentAttributes": List[DocumentAttributeOutputTypeDef],
    },
    total=False,
)

SourceDocumentTypeDef = TypedDict(
    "SourceDocumentTypeDef",
    {
        "DocumentId": str,
        "SuggestionAttributes": List[str],
        "AdditionalAttributes": List[DocumentAttributeOutputTypeDef],
    },
    total=False,
)

InlineCustomDocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationOutputTypeDef",
    {
        "Condition": DocumentAttributeConditionOutputTypeDef,
        "Target": DocumentAttributeTargetOutputTypeDef,
        "DocumentContentDeletion": bool,
    },
    total=False,
)

_RequiredHookConfigurationTypeDef = TypedDict(
    "_RequiredHookConfigurationTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
    },
)
_OptionalHookConfigurationTypeDef = TypedDict(
    "_OptionalHookConfigurationTypeDef",
    {
        "InvocationCondition": DocumentAttributeConditionTypeDef,
    },
    total=False,
)


class HookConfigurationTypeDef(
    _RequiredHookConfigurationTypeDef, _OptionalHookConfigurationTypeDef
):
    pass


InlineCustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    {
        "Condition": DocumentAttributeConditionTypeDef,
        "Target": DocumentAttributeTargetTypeDef,
        "DocumentContentDeletion": bool,
    },
    total=False,
)

AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "AndAllFilters": Sequence[Dict[str, Any]],
        "OrAllFilters": Sequence[Dict[str, Any]],
        "NotFilter": Dict[str, Any],
        "EqualsTo": DocumentAttributeTypeDef,
        "ContainsAll": DocumentAttributeTypeDef,
        "ContainsAny": DocumentAttributeTypeDef,
        "GreaterThan": DocumentAttributeTypeDef,
        "GreaterThanOrEquals": DocumentAttributeTypeDef,
        "LessThan": DocumentAttributeTypeDef,
        "LessThanOrEquals": DocumentAttributeTypeDef,
    },
    total=False,
)

_RequiredDocumentInfoTypeDef = TypedDict(
    "_RequiredDocumentInfoTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalDocumentInfoTypeDef = TypedDict(
    "_OptionalDocumentInfoTypeDef",
    {
        "Attributes": Sequence[DocumentAttributeTypeDef],
    },
    total=False,
)


class DocumentInfoTypeDef(_RequiredDocumentInfoTypeDef, _OptionalDocumentInfoTypeDef):
    pass


_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "Id": str,
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "Title": str,
        "Blob": Union[str, bytes, IO[Any], StreamingBody],
        "S3Path": S3PathTypeDef,
        "Attributes": Sequence[DocumentAttributeTypeDef],
        "AccessControlList": Sequence[PrincipalTypeDef],
        "HierarchicalAccessControlList": Sequence[HierarchicalPrincipalTypeDef],
        "ContentType": ContentTypeType,
        "AccessControlConfigurationId": str,
    },
    total=False,
)


class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass


_RequiredQueryRequestRequestTypeDef = TypedDict(
    "_RequiredQueryRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
_OptionalQueryRequestRequestTypeDef = TypedDict(
    "_OptionalQueryRequestRequestTypeDef",
    {
        "QueryText": str,
        "AttributeFilter": "AttributeFilterTypeDef",
        "Facets": Sequence["FacetTypeDef"],
        "RequestedDocumentAttributes": Sequence[str],
        "QueryResultTypeFilter": QueryResultTypeType,
        "DocumentRelevanceOverrideConfigurations": Sequence[DocumentRelevanceConfigurationTypeDef],
        "PageNumber": int,
        "PageSize": int,
        "SortingConfiguration": SortingConfigurationTypeDef,
        "UserContext": UserContextTypeDef,
        "VisitorId": str,
        "SpellCorrectionConfiguration": SpellCorrectionConfigurationTypeDef,
    },
    total=False,
)


class QueryRequestRequestTypeDef(
    _RequiredQueryRequestRequestTypeDef, _OptionalQueryRequestRequestTypeDef
):
    pass


_RequiredRetrieveRequestRequestTypeDef = TypedDict(
    "_RequiredRetrieveRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
    },
)
_OptionalRetrieveRequestRequestTypeDef = TypedDict(
    "_OptionalRetrieveRequestRequestTypeDef",
    {
        "AttributeFilter": "AttributeFilterTypeDef",
        "RequestedDocumentAttributes": Sequence[str],
        "DocumentRelevanceOverrideConfigurations": Sequence[DocumentRelevanceConfigurationTypeDef],
        "PageNumber": int,
        "PageSize": int,
        "UserContext": UserContextTypeDef,
    },
    total=False,
)


class RetrieveRequestRequestTypeDef(
    _RequiredRetrieveRequestRequestTypeDef, _OptionalRetrieveRequestRequestTypeDef
):
    pass


ListExperienceEntitiesResponseTypeDef = TypedDict(
    "ListExperienceEntitiesResponseTypeDef",
    {
        "SummaryItems": List[ExperienceEntitiesSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeExperienceResponseTypeDef = TypedDict(
    "DescribeExperienceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Endpoints": List[ExperienceEndpointTypeDef],
        "Configuration": ExperienceConfigurationOutputTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": ExperienceStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
    },
)
_OptionalCreateExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperienceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Configuration": ExperienceConfigurationTypeDef,
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)


class CreateExperienceRequestRequestTypeDef(
    _RequiredCreateExperienceRequestRequestTypeDef, _OptionalCreateExperienceRequestRequestTypeDef
):
    pass


_RequiredUpdateExperienceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateExperienceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Configuration": ExperienceConfigurationTypeDef,
        "Description": str,
    },
    total=False,
)


class UpdateExperienceRequestRequestTypeDef(
    _RequiredUpdateExperienceRequestRequestTypeDef, _OptionalUpdateExperienceRequestRequestTypeDef
):
    pass


_RequiredPutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "_RequiredPutPrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "GroupMembers": GroupMembersTypeDef,
    },
)
_OptionalPutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "_OptionalPutPrincipalMappingRequestRequestTypeDef",
    {
        "DataSourceId": str,
        "OrderingId": int,
        "RoleArn": str,
    },
    total=False,
)


class PutPrincipalMappingRequestRequestTypeDef(
    _RequiredPutPrincipalMappingRequestRequestTypeDef,
    _OptionalPutPrincipalMappingRequestRequestTypeDef,
):
    pass


AdditionalResultAttributeValueTypeDef = TypedDict(
    "AdditionalResultAttributeValueTypeDef",
    {
        "TextWithHighlightsValue": TextWithHighlightsTypeDef,
    },
    total=False,
)

_RequiredCreateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
    },
)
_OptionalCreateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIndexRequestRequestTypeDef",
    {
        "Edition": IndexEditionType,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "Description": str,
        "ClientToken": str,
        "Tags": Sequence[TagTypeDef],
        "UserTokenConfigurations": Sequence[UserTokenConfigurationTypeDef],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": UserGroupResolutionConfigurationTypeDef,
    },
    total=False,
)


class CreateIndexRequestRequestTypeDef(
    _RequiredCreateIndexRequestRequestTypeDef, _OptionalCreateIndexRequestRequestTypeDef
):
    pass


DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "Status": IndexStatusType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List[DocumentMetadataConfigurationOutputTypeDef],
        "IndexStatistics": IndexStatisticsTypeDef,
        "ErrorMessage": str,
        "CapacityUnits": CapacityUnitsConfigurationTypeDef,
        "UserTokenConfigurations": List[UserTokenConfigurationTypeDef],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": UserGroupResolutionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredUpdateIndexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateIndexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Description": str,
        "DocumentMetadataConfigurationUpdates": Sequence[DocumentMetadataConfigurationTypeDef],
        "CapacityUnits": CapacityUnitsConfigurationTypeDef,
        "UserTokenConfigurations": Sequence[UserTokenConfigurationTypeDef],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": UserGroupResolutionConfigurationTypeDef,
    },
    total=False,
)


class UpdateIndexRequestRequestTypeDef(
    _RequiredUpdateIndexRequestRequestTypeDef, _OptionalUpdateIndexRequestRequestTypeDef
):
    pass


_RequiredWebCrawlerConfigurationOutputTypeDef = TypedDict(
    "_RequiredWebCrawlerConfigurationOutputTypeDef",
    {
        "Urls": UrlsOutputTypeDef,
    },
)
_OptionalWebCrawlerConfigurationOutputTypeDef = TypedDict(
    "_OptionalWebCrawlerConfigurationOutputTypeDef",
    {
        "CrawlDepth": int,
        "MaxLinksPerPage": int,
        "MaxContentSizePerPageInMegaBytes": float,
        "MaxUrlsPerMinuteCrawlRate": int,
        "UrlInclusionPatterns": List[str],
        "UrlExclusionPatterns": List[str],
        "ProxyConfiguration": ProxyConfigurationTypeDef,
        "AuthenticationConfiguration": AuthenticationConfigurationOutputTypeDef,
    },
    total=False,
)


class WebCrawlerConfigurationOutputTypeDef(
    _RequiredWebCrawlerConfigurationOutputTypeDef, _OptionalWebCrawlerConfigurationOutputTypeDef
):
    pass


_RequiredWebCrawlerConfigurationTypeDef = TypedDict(
    "_RequiredWebCrawlerConfigurationTypeDef",
    {
        "Urls": UrlsTypeDef,
    },
)
_OptionalWebCrawlerConfigurationTypeDef = TypedDict(
    "_OptionalWebCrawlerConfigurationTypeDef",
    {
        "CrawlDepth": int,
        "MaxLinksPerPage": int,
        "MaxContentSizePerPageInMegaBytes": float,
        "MaxUrlsPerMinuteCrawlRate": int,
        "UrlInclusionPatterns": Sequence[str],
        "UrlExclusionPatterns": Sequence[str],
        "ProxyConfiguration": ProxyConfigurationTypeDef,
        "AuthenticationConfiguration": AuthenticationConfigurationTypeDef,
    },
    total=False,
)


class WebCrawlerConfigurationTypeDef(
    _RequiredWebCrawlerConfigurationTypeDef, _OptionalWebCrawlerConfigurationTypeDef
):
    pass


SuggestionValueTypeDef = TypedDict(
    "SuggestionValueTypeDef",
    {
        "Text": SuggestionTextWithHighlightsTypeDef,
    },
    total=False,
)

TableExcerptTypeDef = TypedDict(
    "TableExcerptTypeDef",
    {
        "Rows": List[TableRowTypeDef],
        "TotalNumberOfRows": int,
    },
    total=False,
)

_RequiredSalesforceConfigurationOutputTypeDef = TypedDict(
    "_RequiredSalesforceConfigurationOutputTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
    },
)
_OptionalSalesforceConfigurationOutputTypeDef = TypedDict(
    "_OptionalSalesforceConfigurationOutputTypeDef",
    {
        "StandardObjectConfigurations": List[SalesforceStandardObjectConfigurationOutputTypeDef],
        "KnowledgeArticleConfiguration": SalesforceKnowledgeArticleConfigurationOutputTypeDef,
        "ChatterFeedConfiguration": SalesforceChatterFeedConfigurationOutputTypeDef,
        "CrawlAttachments": bool,
        "StandardObjectAttachmentConfiguration": (
            SalesforceStandardObjectAttachmentConfigurationOutputTypeDef
        ),
        "IncludeAttachmentFilePatterns": List[str],
        "ExcludeAttachmentFilePatterns": List[str],
    },
    total=False,
)


class SalesforceConfigurationOutputTypeDef(
    _RequiredSalesforceConfigurationOutputTypeDef, _OptionalSalesforceConfigurationOutputTypeDef
):
    pass


_RequiredSalesforceConfigurationTypeDef = TypedDict(
    "_RequiredSalesforceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
    },
)
_OptionalSalesforceConfigurationTypeDef = TypedDict(
    "_OptionalSalesforceConfigurationTypeDef",
    {
        "StandardObjectConfigurations": Sequence[SalesforceStandardObjectConfigurationTypeDef],
        "KnowledgeArticleConfiguration": SalesforceKnowledgeArticleConfigurationTypeDef,
        "ChatterFeedConfiguration": SalesforceChatterFeedConfigurationTypeDef,
        "CrawlAttachments": bool,
        "StandardObjectAttachmentConfiguration": (
            SalesforceStandardObjectAttachmentConfigurationTypeDef
        ),
        "IncludeAttachmentFilePatterns": Sequence[str],
        "ExcludeAttachmentFilePatterns": Sequence[str],
    },
    total=False,
)


class SalesforceConfigurationTypeDef(
    _RequiredSalesforceConfigurationTypeDef, _OptionalSalesforceConfigurationTypeDef
):
    pass


_RequiredGetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
    },
)
_OptionalGetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetQuerySuggestionsRequestRequestTypeDef",
    {
        "MaxSuggestionsCount": int,
        "SuggestionTypes": Sequence[SuggestionTypeType],
        "AttributeSuggestionsConfig": AttributeSuggestionsGetConfigTypeDef,
    },
    total=False,
)


class GetQuerySuggestionsRequestRequestTypeDef(
    _RequiredGetQuerySuggestionsRequestRequestTypeDef,
    _OptionalGetQuerySuggestionsRequestRequestTypeDef,
):
    pass


RetrieveResultTypeDef = TypedDict(
    "RetrieveResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List[RetrieveResultItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CustomDocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationOutputTypeDef",
    {
        "InlineConfigurations": List[InlineCustomDocumentEnrichmentConfigurationOutputTypeDef],
        "PreExtractionHookConfiguration": HookConfigurationOutputTypeDef,
        "PostExtractionHookConfiguration": HookConfigurationOutputTypeDef,
        "RoleArn": str,
    },
    total=False,
)

CustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationTypeDef",
    {
        "InlineConfigurations": Sequence[InlineCustomDocumentEnrichmentConfigurationTypeDef],
        "PreExtractionHookConfiguration": HookConfigurationTypeDef,
        "PostExtractionHookConfiguration": HookConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)

BatchGetDocumentStatusRequestRequestTypeDef = TypedDict(
    "BatchGetDocumentStatusRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentInfoList": Sequence[DocumentInfoTypeDef],
    },
)

AdditionalResultAttributeTypeDef = TypedDict(
    "AdditionalResultAttributeTypeDef",
    {
        "Key": str,
        "ValueType": Literal["TEXT_WITH_HIGHLIGHTS_VALUE"],
        "Value": AdditionalResultAttributeValueTypeDef,
    },
)

SuggestionTypeDef = TypedDict(
    "SuggestionTypeDef",
    {
        "Id": str,
        "Value": SuggestionValueTypeDef,
        "SourceDocuments": List[SourceDocumentTypeDef],
    },
    total=False,
)

DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "S3Configuration": S3DataSourceConfigurationOutputTypeDef,
        "SharePointConfiguration": SharePointConfigurationOutputTypeDef,
        "DatabaseConfiguration": DatabaseConfigurationOutputTypeDef,
        "SalesforceConfiguration": SalesforceConfigurationOutputTypeDef,
        "OneDriveConfiguration": OneDriveConfigurationOutputTypeDef,
        "ServiceNowConfiguration": ServiceNowConfigurationOutputTypeDef,
        "ConfluenceConfiguration": ConfluenceConfigurationOutputTypeDef,
        "GoogleDriveConfiguration": GoogleDriveConfigurationOutputTypeDef,
        "WebCrawlerConfiguration": WebCrawlerConfigurationOutputTypeDef,
        "WorkDocsConfiguration": WorkDocsConfigurationOutputTypeDef,
        "FsxConfiguration": FsxConfigurationOutputTypeDef,
        "SlackConfiguration": SlackConfigurationOutputTypeDef,
        "BoxConfiguration": BoxConfigurationOutputTypeDef,
        "QuipConfiguration": QuipConfigurationOutputTypeDef,
        "JiraConfiguration": JiraConfigurationOutputTypeDef,
        "GitHubConfiguration": GitHubConfigurationOutputTypeDef,
        "AlfrescoConfiguration": AlfrescoConfigurationOutputTypeDef,
        "TemplateConfiguration": TemplateConfigurationOutputTypeDef,
    },
    total=False,
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "S3Configuration": S3DataSourceConfigurationTypeDef,
        "SharePointConfiguration": SharePointConfigurationTypeDef,
        "DatabaseConfiguration": DatabaseConfigurationTypeDef,
        "SalesforceConfiguration": SalesforceConfigurationTypeDef,
        "OneDriveConfiguration": OneDriveConfigurationTypeDef,
        "ServiceNowConfiguration": ServiceNowConfigurationTypeDef,
        "ConfluenceConfiguration": ConfluenceConfigurationTypeDef,
        "GoogleDriveConfiguration": GoogleDriveConfigurationTypeDef,
        "WebCrawlerConfiguration": WebCrawlerConfigurationTypeDef,
        "WorkDocsConfiguration": WorkDocsConfigurationTypeDef,
        "FsxConfiguration": FsxConfigurationTypeDef,
        "SlackConfiguration": SlackConfigurationTypeDef,
        "BoxConfiguration": BoxConfigurationTypeDef,
        "QuipConfiguration": QuipConfigurationTypeDef,
        "JiraConfiguration": JiraConfigurationTypeDef,
        "GitHubConfiguration": GitHubConfigurationTypeDef,
        "AlfrescoConfiguration": AlfrescoConfigurationTypeDef,
        "TemplateConfiguration": TemplateConfigurationTypeDef,
    },
    total=False,
)

_RequiredBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredBatchPutDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "Documents": Sequence[DocumentTypeDef],
    },
)
_OptionalBatchPutDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalBatchPutDocumentRequestRequestTypeDef",
    {
        "RoleArn": str,
        "CustomDocumentEnrichmentConfiguration": CustomDocumentEnrichmentConfigurationTypeDef,
    },
    total=False,
)


class BatchPutDocumentRequestRequestTypeDef(
    _RequiredBatchPutDocumentRequestRequestTypeDef, _OptionalBatchPutDocumentRequestRequestTypeDef
):
    pass


FeaturedResultsItemTypeDef = TypedDict(
    "FeaturedResultsItemTypeDef",
    {
        "Id": str,
        "Type": QueryResultTypeType,
        "AdditionalAttributes": List[AdditionalResultAttributeTypeDef],
        "DocumentId": str,
        "DocumentTitle": TextWithHighlightsTypeDef,
        "DocumentExcerpt": TextWithHighlightsTypeDef,
        "DocumentURI": str,
        "DocumentAttributes": List[DocumentAttributeOutputTypeDef],
        "FeedbackToken": str,
    },
    total=False,
)

QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": str,
        "Type": QueryResultTypeType,
        "Format": QueryResultFormatType,
        "AdditionalAttributes": List[AdditionalResultAttributeTypeDef],
        "DocumentId": str,
        "DocumentTitle": TextWithHighlightsTypeDef,
        "DocumentExcerpt": TextWithHighlightsTypeDef,
        "DocumentURI": str,
        "DocumentAttributes": List[DocumentAttributeOutputTypeDef],
        "ScoreAttributes": ScoreAttributesTypeDef,
        "FeedbackToken": str,
        "TableExcerpt": TableExcerptTypeDef,
    },
    total=False,
)

GetQuerySuggestionsResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List[SuggestionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Configuration": DataSourceConfigurationOutputTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatusType,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": CustomDocumentEnrichmentConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "Configuration": DataSourceConfigurationTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
        "Tags": Sequence[TagTypeDef],
        "ClientToken": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": CustomDocumentEnrichmentConfigurationTypeDef,
    },
    total=False,
)


class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass


_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Configuration": DataSourceConfigurationTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationTypeDef,
        "Description": str,
        "Schedule": str,
        "RoleArn": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": CustomDocumentEnrichmentConfigurationTypeDef,
    },
    total=False,
)


class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass


QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List[QueryResultItemTypeDef],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
        "Warnings": List[WarningTypeDef],
        "SpellCorrectedQueries": List[SpellCorrectedQueryTypeDef],
        "FeaturedResultsItems": List[FeaturedResultsItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
