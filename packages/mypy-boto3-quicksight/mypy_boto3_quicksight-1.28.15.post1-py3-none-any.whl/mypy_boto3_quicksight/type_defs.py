"""
Type annotations for quicksight service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/type_defs/)

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AnalysisErrorTypeType,
    AnalysisFilterAttributeType,
    ArcThicknessOptionsType,
    ArcThicknessType,
    AssetBundleExportFormatType,
    AssetBundleExportJobDataSourcePropertyToOverrideType,
    AssetBundleExportJobStatusType,
    AssetBundleExportJobVPCConnectionPropertyToOverrideType,
    AssetBundleImportFailureActionType,
    AssetBundleImportJobStatusType,
    AssignmentStatusType,
    AuthenticationMethodOptionType,
    AuthorSpecifiedAggregationType,
    AxisBindingType,
    BarChartOrientationType,
    BarsArrangementType,
    BaseMapStyleTypeType,
    BoxPlotFillStyleType,
    CategoricalAggregationFunctionType,
    CategoryFilterFunctionType,
    CategoryFilterMatchOperatorType,
    CategoryFilterTypeType,
    ColorFillTypeType,
    ColumnDataRoleType,
    ColumnDataTypeType,
    ColumnOrderingTypeType,
    ColumnRoleType,
    ColumnTagNameType,
    ComparisonMethodType,
    ConditionalFormattingIconSetTypeType,
    ConstantTypeType,
    CrossDatasetTypesType,
    CustomContentImageScalingConfigurationType,
    CustomContentTypeType,
    DashboardBehaviorType,
    DashboardErrorTypeType,
    DashboardFilterAttributeType,
    DashboardUIStateType,
    DataLabelContentType,
    DataLabelOverlapType,
    DataLabelPositionType,
    DataSetFilterAttributeType,
    DataSetImportModeType,
    DatasetParameterValueTypeType,
    DataSourceErrorInfoTypeType,
    DataSourceFilterAttributeType,
    DataSourceTypeType,
    DateAggregationFunctionType,
    DayOfWeekType,
    DefaultAggregationType,
    DisplayFormatType,
    EditionType,
    EmbeddingIdentityTypeType,
    FileFormatType,
    FilterClassType,
    FilterNullOptionType,
    FilterOperatorType,
    FilterVisualScopeType,
    FolderFilterAttributeType,
    FontDecorationType,
    FontStyleType,
    FontWeightNameType,
    ForecastComputationSeasonalityType,
    FunnelChartMeasureDataLabelStyleType,
    GeoSpatialDataRoleType,
    GeospatialSelectedPointStyleType,
    HistogramBinTypeType,
    HorizontalTextAlignmentType,
    IconType,
    IdentityTypeType,
    IngestionErrorTypeType,
    IngestionRequestSourceType,
    IngestionRequestTypeType,
    IngestionStatusType,
    IngestionTypeType,
    InputColumnDataTypeType,
    JoinTypeType,
    LayoutElementTypeType,
    LegendPositionType,
    LineChartLineStyleType,
    LineChartMarkerShapeType,
    LineChartTypeType,
    LineInterpolationType,
    LookbackWindowSizeUnitType,
    MapZoomModeType,
    MaximumMinimumComputationTypeType,
    MemberTypeType,
    MissingDataTreatmentOptionType,
    NamedEntityAggTypeType,
    NamedFilterAggTypeType,
    NamedFilterTypeType,
    NamespaceErrorTypeType,
    NamespaceStatusType,
    NegativeValueDisplayModeType,
    NetworkInterfaceStatusType,
    NumberScaleType,
    NumericEqualityMatchOperatorType,
    NumericSeparatorSymbolType,
    OtherCategoriesType,
    PanelBorderStyleType,
    PaperOrientationType,
    PaperSizeType,
    ParameterValueTypeType,
    PivotTableConditionalFormattingScopeRoleType,
    PivotTableFieldCollapseStateType,
    PivotTableMetricPlacementType,
    PivotTableSubtotalLevelType,
    PrimaryValueDisplayTypeType,
    PropertyRoleType,
    PropertyUsageType,
    RadarChartAxesRangeScaleType,
    RadarChartShapeType,
    ReferenceLineLabelHorizontalPositionType,
    ReferenceLineLabelVerticalPositionType,
    ReferenceLinePatternTypeType,
    ReferenceLineValueLabelRelativePositionType,
    RefreshIntervalType,
    RelativeDateTypeType,
    RelativeFontSizeType,
    ResizeOptionType,
    ResourceStatusType,
    RowLevelPermissionFormatVersionType,
    RowLevelPermissionPolicyType,
    SectionPageBreakStatusType,
    SelectedTooltipTypeType,
    SheetContentTypeType,
    SheetControlDateTimePickerTypeType,
    SheetControlListTypeType,
    SheetControlSliderTypeType,
    SimpleNumericalAggregationFunctionType,
    SmallMultiplesAxisPlacementType,
    SmallMultiplesAxisScaleType,
    SnapshotFileFormatTypeType,
    SnapshotFileSheetSelectionScopeType,
    SnapshotJobStatusType,
    SortDirectionType,
    SpecialValueType,
    StatusType,
    TableBorderStyleType,
    TableCellImageScalingConfigurationType,
    TableOrientationType,
    TableTotalsPlacementType,
    TableTotalsScrollStatusType,
    TemplateErrorTypeType,
    TextQualifierType,
    TextWrapType,
    ThemeTypeType,
    TimeGranularityType,
    TooltipTitleTypeType,
    TopBottomComputationTypeType,
    TopBottomSortOrderType,
    TopicNumericSeparatorSymbolType,
    TopicRefreshStatusType,
    TopicRelativeDateFilterFunctionType,
    TopicScheduleTypeType,
    TopicTimeGranularityType,
    UndefinedSpecifiedValueTypeType,
    URLTargetConfigurationType,
    UserRoleType,
    ValueWhenUnsetOptionType,
    VerticalTextAlignmentType,
    VisibilityType,
    VisualCustomActionTriggerType,
    VPCConnectionAvailabilityStatusType,
    VPCConnectionResourceStatusType,
    WidgetStatusType,
    WordCloudCloudLayoutType,
    WordCloudWordCasingType,
    WordCloudWordOrientationType,
    WordCloudWordPaddingType,
    WordCloudWordScalingType,
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
    "AccountCustomizationTypeDef",
    "AccountInfoTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AttributeAggregationFunctionTypeDef",
    "ColumnIdentifierTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AmazonOpenSearchParametersTypeDef",
    "CalculatedFieldTypeDef",
    "DataSetIdentifierDeclarationTypeDef",
    "EntityTypeDef",
    "AnalysisSearchFilterTypeDef",
    "DataSetReferenceTypeDef",
    "AnalysisSummaryTypeDef",
    "SheetTypeDef",
    "AnchorDateConfigurationTypeDef",
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    "DashboardVisualIdTypeDef",
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    "ArcAxisDisplayRangeTypeDef",
    "ArcConfigurationTypeDef",
    "ArcOptionsTypeDef",
    "AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobResourceIdOverrideConfigurationTypeDef",
    "AssetBundleExportJobThemeOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobAnalysisOverridePropertiesTypeDef",
    "AssetBundleExportJobDashboardOverridePropertiesTypeDef",
    "AssetBundleExportJobDataSetOverridePropertiesTypeDef",
    "AssetBundleExportJobDataSourceOverridePropertiesTypeDef",
    "AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef",
    "AssetBundleExportJobThemeOverridePropertiesTypeDef",
    "AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef",
    "AssetBundleExportJobErrorTypeDef",
    "AssetBundleExportJobSummaryTypeDef",
    "AssetBundleImportJobAnalysisOverrideParametersTypeDef",
    "AssetBundleImportJobDashboardOverrideParametersTypeDef",
    "AssetBundleImportJobDataSetOverrideParametersTypeDef",
    "AssetBundleImportJobDataSourceCredentialPairTypeDef",
    "SslPropertiesTypeDef",
    "VpcConnectionPropertiesTypeDef",
    "AssetBundleImportJobErrorTypeDef",
    "AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef",
    "AssetBundleImportJobResourceIdOverrideConfigurationTypeDef",
    "AssetBundleImportJobThemeOverrideParametersTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef",
    "AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideParametersTypeDef",
    "AssetBundleImportJobSummaryTypeDef",
    "AssetBundleImportSourceDescriptionTypeDef",
    "AssetBundleImportSourceTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "DateAxisOptionsTypeDef",
    "AxisDisplayMinMaxRangeTypeDef",
    "AxisLinearScaleTypeDef",
    "AxisLogarithmicScaleTypeDef",
    "ItemsLimitConfigurationTypeDef",
    "BinCountOptionsTypeDef",
    "BinWidthOptionsTypeDef",
    "BookmarksConfigurationsTypeDef",
    "BorderStyleTypeDef",
    "BoxPlotStyleOptionsTypeDef",
    "PaginationConfigurationTypeDef",
    "CalculatedColumnTypeDef",
    "CalculatedMeasureFieldTypeDef",
    "CancelIngestionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CastColumnTypeOperationTypeDef",
    "CustomFilterConfigurationTypeDef",
    "CustomFilterListConfigurationOutputTypeDef",
    "FilterListConfigurationOutputTypeDef",
    "CustomFilterListConfigurationTypeDef",
    "FilterListConfigurationTypeDef",
    "CellValueSynonymOutputTypeDef",
    "CellValueSynonymTypeDef",
    "SimpleClusterMarkerTypeDef",
    "CollectiveConstantOutputTypeDef",
    "CollectiveConstantTypeDef",
    "DataColorTypeDef",
    "CustomColorTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "GeoSpatialColumnGroupOutputTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "ColumnLevelPermissionRuleOutputTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ComparativeOrderOutputTypeDef",
    "ComparativeOrderTypeDef",
    "ConditionalFormattingSolidColorTypeDef",
    "ConditionalFormattingCustomIconOptionsTypeDef",
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    "ConditionalFormattingIconSetTypeDef",
    "TagTypeDef",
    "CreateAccountSubscriptionRequestRequestTypeDef",
    "SignupResponseTypeDef",
    "ResourcePermissionOutputTypeDef",
    "ResourcePermissionTypeDef",
    "DataSetUsageConfigurationTypeDef",
    "FieldFolderOutputTypeDef",
    "FieldFolderTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "CreateFolderMembershipRequestRequestTypeDef",
    "FolderMemberTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "GroupMemberTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "GroupTypeDef",
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "CreateTemplateAliasRequestRequestTypeDef",
    "TemplateAliasTypeDef",
    "CreateThemeAliasRequestRequestTypeDef",
    "ThemeAliasTypeDef",
    "TopicRefreshScheduleTypeDef",
    "DecimalPlacesConfigurationTypeDef",
    "NegativeValueConfigurationTypeDef",
    "NullValueFormatConfigurationTypeDef",
    "LocalNavigationConfigurationTypeDef",
    "CustomActionURLOperationTypeDef",
    "CustomContentConfigurationTypeDef",
    "CustomNarrativeOptionsTypeDef",
    "CustomParameterValuesOutputTypeDef",
    "CustomParameterValuesTypeDef",
    "InputColumnTypeDef",
    "DataPointDrillUpDownOptionTypeDef",
    "DataPointMenuLabelOptionTypeDef",
    "DataPointTooltipOptionTypeDef",
    "ExportToCSVOptionTypeDef",
    "ExportWithHiddenFieldsOptionTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetLayoutElementMaximizationOptionTypeDef",
    "VisualAxisSortOptionTypeDef",
    "VisualMenuOptionTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardVersionSummaryTypeDef",
    "ExportHiddenFieldsOptionTypeDef",
    "DataAggregationTypeDef",
    "DataBarsOptionsTypeDef",
    "DataColorPaletteOutputTypeDef",
    "DataColorPaletteTypeDef",
    "DataPathLabelTypeTypeDef",
    "FieldLabelTypeTypeDef",
    "MaximumLabelTypeTypeDef",
    "MinimumLabelTypeTypeDef",
    "RangeEndsLabelTypeTypeDef",
    "DataPathValueTypeDef",
    "DataSetSearchFilterTypeDef",
    "OutputColumnTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DatabricksParametersTypeDef",
    "ExasolParametersTypeDef",
    "JiraParametersTypeDef",
    "MariaDbParametersTypeDef",
    "MySqlParametersTypeDef",
    "OracleParametersTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "RdsParametersTypeDef",
    "RedshiftParametersTypeDef",
    "ServiceNowParametersTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "TeradataParametersTypeDef",
    "TwitterParametersTypeDef",
    "DataSourceSearchFilterTypeDef",
    "DataSourceSummaryTypeDef",
    "DateTimeDatasetParameterDefaultValuesOutputTypeDef",
    "DateTimeDatasetParameterDefaultValuesTypeDef",
    "RollingDateConfigurationTypeDef",
    "DateTimeValueWhenUnsetConfigurationOutputTypeDef",
    "MappedDataSetParameterTypeDef",
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    "DateTimeParameterOutputTypeDef",
    "DateTimeParameterTypeDef",
    "SheetControlInfoIconLabelOptionsTypeDef",
    "DecimalDatasetParameterDefaultValuesOutputTypeDef",
    "DecimalDatasetParameterDefaultValuesTypeDef",
    "DecimalValueWhenUnsetConfigurationTypeDef",
    "DecimalParameterOutputTypeDef",
    "DecimalParameterTypeDef",
    "DeleteAccountCustomizationRequestRequestTypeDef",
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    "DeleteAnalysisRequestRequestTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteDataSetRefreshPropertiesRequestRequestTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteFolderMembershipRequestRequestTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteRefreshScheduleRequestRequestTypeDef",
    "DeleteTemplateAliasRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteThemeAliasRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "DeleteTopicRefreshScheduleRequestRequestTypeDef",
    "DeleteTopicRequestRequestTypeDef",
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVPCConnectionRequestRequestTypeDef",
    "DescribeAccountCustomizationRequestRequestTypeDef",
    "DescribeAccountSettingsRequestRequestTypeDef",
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    "DescribeAnalysisRequestRequestTypeDef",
    "DescribeAssetBundleExportJobRequestRequestTypeDef",
    "DescribeAssetBundleImportJobRequestRequestTypeDef",
    "DescribeDashboardDefinitionRequestRequestTypeDef",
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardSnapshotJobRequestRequestTypeDef",
    "DescribeDashboardSnapshotJobResultRequestRequestTypeDef",
    "SnapshotJobErrorInfoTypeDef",
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    "DescribeDataSetRefreshPropertiesRequestRequestTypeDef",
    "DescribeDataSetRequestRequestTypeDef",
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeFolderPermissionsRequestRequestTypeDef",
    "DescribeFolderRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    "FolderTypeDef",
    "DescribeGroupMembershipRequestRequestTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "DescribeIngestionRequestRequestTypeDef",
    "DescribeIpRestrictionRequestRequestTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DescribeRefreshScheduleRequestRequestTypeDef",
    "DescribeTemplateAliasRequestRequestTypeDef",
    "DescribeTemplateDefinitionRequestRequestTypeDef",
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    "DescribeTemplateRequestRequestTypeDef",
    "DescribeThemeAliasRequestRequestTypeDef",
    "DescribeThemePermissionsRequestRequestTypeDef",
    "DescribeThemeRequestRequestTypeDef",
    "DescribeTopicPermissionsRequestRequestTypeDef",
    "DescribeTopicRefreshRequestRequestTypeDef",
    "TopicRefreshDetailsTypeDef",
    "DescribeTopicRefreshScheduleRequestRequestTypeDef",
    "TopicRefreshScheduleOutputTypeDef",
    "DescribeTopicRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "UserTypeDef",
    "DescribeVPCConnectionRequestRequestTypeDef",
    "NegativeFormatTypeDef",
    "DonutCenterOptionsTypeDef",
    "ListControlSelectAllOptionsTypeDef",
    "ErrorInfoTypeDef",
    "ExcludePeriodConfigurationTypeDef",
    "FieldSortTypeDef",
    "FieldTooltipItemTypeDef",
    "GeospatialMapStyleOptionsTypeDef",
    "FilterSelectableValuesOutputTypeDef",
    "FilterSelectableValuesTypeDef",
    "SameSheetTargetVisualConfigurationOutputTypeDef",
    "SameSheetTargetVisualConfigurationTypeDef",
    "FilterOperationTypeDef",
    "FolderSearchFilterTypeDef",
    "FolderSummaryTypeDef",
    "FontSizeTypeDef",
    "FontWeightTypeDef",
    "FontTypeDef",
    "TimeBasedForecastPropertiesTypeDef",
    "WhatIfPointScenarioOutputTypeDef",
    "WhatIfRangeScenarioOutputTypeDef",
    "WhatIfPointScenarioTypeDef",
    "WhatIfRangeScenarioTypeDef",
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    "FreeFormLayoutElementBorderStyleTypeDef",
    "LoadingAnimationTypeDef",
    "SessionTagTypeDef",
    "GeospatialCoordinateBoundsTypeDef",
    "GeospatialHeatmapDataColorTypeDef",
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    "GetSessionEmbedUrlRequestRequestTypeDef",
    "TableBorderOptionsTypeDef",
    "GradientStopTypeDef",
    "GridLayoutScreenCanvasSizeOptionsTypeDef",
    "GridLayoutElementTypeDef",
    "GroupSearchFilterTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "LookbackWindowTypeDef",
    "QueueInfoTypeDef",
    "RowInfoTypeDef",
    "IntegerDatasetParameterDefaultValuesOutputTypeDef",
    "IntegerDatasetParameterDefaultValuesTypeDef",
    "IntegerValueWhenUnsetConfigurationTypeDef",
    "IntegerParameterOutputTypeDef",
    "IntegerParameterTypeDef",
    "JoinKeyPropertiesTypeDef",
    "ProgressBarOptionsTypeDef",
    "SecondaryValueOptionsTypeDef",
    "TrendArrowOptionsTypeDef",
    "LineChartLineStyleSettingsTypeDef",
    "LineChartMarkerStyleSettingsTypeDef",
    "MissingDataConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAnalysesRequestRequestTypeDef",
    "ListAssetBundleExportJobsRequestRequestTypeDef",
    "ListAssetBundleImportJobsRequestRequestTypeDef",
    "ListControlSearchOptionsTypeDef",
    "ListDashboardVersionsRequestRequestTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListFolderMembersRequestRequestTypeDef",
    "MemberIdArnPairTypeDef",
    "ListFoldersRequestRequestTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListRefreshSchedulesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplateAliasesRequestRequestTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "TemplateVersionSummaryTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "ListThemeAliasesRequestRequestTypeDef",
    "ListThemeVersionsRequestRequestTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ThemeSummaryTypeDef",
    "ListTopicRefreshSchedulesRequestRequestTypeDef",
    "ListTopicsRequestRequestTypeDef",
    "TopicSummaryTypeDef",
    "ListUserGroupsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListVPCConnectionsRequestRequestTypeDef",
    "LongFormatTextTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "NamedEntityDefinitionMetricOutputTypeDef",
    "NamedEntityDefinitionMetricTypeDef",
    "NamespaceErrorTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDefaultValuesOutputTypeDef",
    "NewDefaultValuesTypeDef",
    "NumericRangeFilterValueTypeDef",
    "ThousandSeparatorOptionsTypeDef",
    "PercentileAggregationTypeDef",
    "StringParameterOutputTypeDef",
    "StringParameterTypeDef",
    "PercentVisibleRangeTypeDef",
    "PivotTableConditionalFormattingScopeTypeDef",
    "PivotTablePaginatedReportOptionsTypeDef",
    "PivotTableFieldOptionTypeDef",
    "PivotTableFieldSubtotalOptionsTypeDef",
    "RowAlternateColorOptionsOutputTypeDef",
    "RowAlternateColorOptionsTypeDef",
    "ProjectOperationOutputTypeDef",
    "ProjectOperationTypeDef",
    "RadarChartAreaStyleSettingsTypeDef",
    "RangeConstantTypeDef",
    "ReferenceLineCustomLabelConfigurationTypeDef",
    "ReferenceLineStaticDataConfigurationTypeDef",
    "ReferenceLineStyleConfigurationTypeDef",
    "ScheduleRefreshOnEntityTypeDef",
    "RegisterUserRequestRequestTypeDef",
    "StatePersistenceConfigurationsTypeDef",
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    "RenameColumnOperationTypeDef",
    "RestoreAnalysisRequestRequestTypeDef",
    "RowLevelPermissionTagRuleTypeDef",
    "S3BucketConfigurationTypeDef",
    "UploadSettingsTypeDef",
    "SectionAfterPageBreakTypeDef",
    "SpacingTypeDef",
    "SheetVisualScopingConfigurationOutputTypeDef",
    "SheetVisualScopingConfigurationTypeDef",
    "SemanticEntityTypeOutputTypeDef",
    "SemanticEntityTypeTypeDef",
    "SemanticTypeOutputTypeDef",
    "SemanticTypeTypeDef",
    "SheetTextBoxTypeDef",
    "SheetElementConfigurationOverridesTypeDef",
    "ShortFormatTextTypeDef",
    "SmallMultiplesAxisPropertiesTypeDef",
    "SnapshotAnonymousUserRedactedTypeDef",
    "SnapshotFileSheetSelectionOutputTypeDef",
    "SnapshotFileSheetSelectionTypeDef",
    "SnapshotJobResultErrorInfoTypeDef",
    "StringDatasetParameterDefaultValuesOutputTypeDef",
    "StringDatasetParameterDefaultValuesTypeDef",
    "StringValueWhenUnsetConfigurationTypeDef",
    "TableCellImageSizingConfigurationTypeDef",
    "TablePaginatedReportOptionsTypeDef",
    "TableFieldCustomIconContentTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TextControlPlaceholderOptionsTypeDef",
    "UIColorPaletteTypeDef",
    "ThemeErrorTypeDef",
    "TopicSingularFilterConstantTypeDef",
    "UntagColumnOperationOutputTypeDef",
    "UntagColumnOperationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    "UpdateIpRestrictionRequestRequestTypeDef",
    "UpdatePublicSharingSettingsRequestRequestTypeDef",
    "UpdateTemplateAliasRequestRequestTypeDef",
    "UpdateThemeAliasRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateVPCConnectionRequestRequestTypeDef",
    "WaterfallChartOptionsTypeDef",
    "WordCloudOptionsTypeDef",
    "UpdateAccountCustomizationRequestRequestTypeDef",
    "AxisLabelReferenceOptionsTypeDef",
    "CascadingControlSourceTypeDef",
    "CategoryDrillDownFilterOutputTypeDef",
    "CategoryDrillDownFilterTypeDef",
    "ContributionAnalysisDefaultOutputTypeDef",
    "ContributionAnalysisDefaultTypeDef",
    "DynamicDefaultValueTypeDef",
    "FilterOperationSelectedFieldsConfigurationOutputTypeDef",
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    "NumericEqualityDrillDownFilterTypeDef",
    "ParameterSelectableValuesOutputTypeDef",
    "ParameterSelectableValuesTypeDef",
    "TimeEqualityFilterOutputTypeDef",
    "TimeEqualityFilterTypeDef",
    "TimeRangeDrillDownFilterOutputTypeDef",
    "TimeRangeDrillDownFilterTypeDef",
    "AnalysisErrorTypeDef",
    "DashboardErrorTypeDef",
    "TemplateErrorTypeDef",
    "SearchAnalysesRequestRequestTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "DashboardSourceTemplateTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    "ArcAxisConfigurationTypeDef",
    "AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef",
    "AssetBundleCloudFormationOverridePropertyConfigurationTypeDef",
    "AssetBundleImportJobDataSourceCredentialsTypeDef",
    "AxisDisplayRangeOutputTypeDef",
    "AxisDisplayRangeTypeDef",
    "AxisScaleTypeDef",
    "HistogramBinOptionsTypeDef",
    "TileStyleTypeDef",
    "BoxPlotOptionsTypeDef",
    "CreateColumnsOperationOutputTypeDef",
    "CreateColumnsOperationTypeDef",
    "CancelIngestionResponseTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateRefreshScheduleResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeResponseTypeDef",
    "CreateTopicRefreshScheduleResponseTypeDef",
    "CreateTopicResponseTypeDef",
    "CreateVPCConnectionResponseTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAccountSubscriptionResponseTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetRefreshPropertiesResponseTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteFolderMembershipResponseTypeDef",
    "DeleteFolderResponseTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteRefreshScheduleResponseTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteTopicRefreshScheduleResponseTypeDef",
    "DeleteTopicResponseTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserResponseTypeDef",
    "DeleteVPCConnectionResponseTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAccountSubscriptionResponseTypeDef",
    "DescribeIpRestrictionResponseTypeDef",
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListAssetBundleExportJobsResponseTypeDef",
    "ListAssetBundleImportJobsResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "PutDataSetRefreshPropertiesResponseTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "SearchAnalysesResponseTypeDef",
    "StartAssetBundleExportJobResponseTypeDef",
    "StartAssetBundleImportJobResponseTypeDef",
    "StartDashboardSnapshotJobResponseTypeDef",
    "TagResourceResponseTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFolderResponseTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateIpRestrictionResponseTypeDef",
    "UpdatePublicSharingSettingsResponseTypeDef",
    "UpdateRefreshScheduleResponseTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateTopicRefreshScheduleResponseTypeDef",
    "UpdateTopicResponseTypeDef",
    "UpdateVPCConnectionResponseTypeDef",
    "CategoryFilterConfigurationOutputTypeDef",
    "CategoryFilterConfigurationTypeDef",
    "ClusterMarkerTypeDef",
    "TopicCategoryFilterConstantOutputTypeDef",
    "TopicCategoryFilterConstantTypeDef",
    "ColorScaleOutputTypeDef",
    "ColorScaleTypeDef",
    "ColorsConfigurationOutputTypeDef",
    "ColorsConfigurationTypeDef",
    "ColumnTagTypeDef",
    "ColumnGroupSchemaOutputTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupOutputTypeDef",
    "ColumnGroupTypeDef",
    "DataSetSchemaOutputTypeDef",
    "DataSetSchemaTypeDef",
    "ConditionalFormattingCustomIconConditionTypeDef",
    "CreateAccountCustomizationRequestRequestTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateVPCConnectionRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAccountSubscriptionResponseTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeFolderPermissionsResponseTypeDef",
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeTopicPermissionsResponseTypeDef",
    "LinkSharingConfigurationTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateFolderPermissionsResponseTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateTopicPermissionsResponseTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    "UpdateFolderPermissionsRequestRequestTypeDef",
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    "UpdateThemePermissionsRequestRequestTypeDef",
    "UpdateTopicPermissionsRequestRequestTypeDef",
    "DataSetSummaryTypeDef",
    "CreateFolderMembershipResponseTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUserGroupsResponseTypeDef",
    "SearchGroupsResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "CreateTopicRefreshScheduleRequestRequestTypeDef",
    "UpdateTopicRefreshScheduleRequestRequestTypeDef",
    "CustomActionNavigationOperationTypeDef",
    "CustomValuesConfigurationOutputTypeDef",
    "CustomValuesConfigurationTypeDef",
    "CustomSqlOutputTypeDef",
    "CustomSqlTypeDef",
    "RelationalTableOutputTypeDef",
    "RelationalTableTypeDef",
    "SearchDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "SearchDashboardsResponseTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "DashboardVisualPublishOptionsTypeDef",
    "TableInlineVisualizationTypeDef",
    "DataLabelTypeTypeDef",
    "DataPathColorTypeDef",
    "DataPathSortOutputTypeDef",
    "DataPathSortTypeDef",
    "PivotTableDataPathOptionOutputTypeDef",
    "PivotTableDataPathOptionTypeDef",
    "PivotTableFieldCollapseStateTargetOutputTypeDef",
    "PivotTableFieldCollapseStateTargetTypeDef",
    "SearchDataSetsRequestRequestTypeDef",
    "SearchDataSourcesRequestRequestTypeDef",
    "SearchDataSourcesResponseTypeDef",
    "DateTimeDatasetParameterOutputTypeDef",
    "DateTimeDatasetParameterTypeDef",
    "TimeRangeFilterValueOutputTypeDef",
    "TimeRangeFilterValueTypeDef",
    "DecimalDatasetParameterOutputTypeDef",
    "DecimalDatasetParameterTypeDef",
    "DescribeFolderResponseTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeTopicRefreshResponseTypeDef",
    "DescribeTopicRefreshScheduleResponseTypeDef",
    "TopicRefreshScheduleSummaryTypeDef",
    "DescribeUserResponseTypeDef",
    "ListUsersResponseTypeDef",
    "RegisterUserResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "DisplayFormatOptionsTypeDef",
    "DonutOptionsTypeDef",
    "RelativeDatesFilterTypeDef",
    "FilterOperationTargetVisualsConfigurationOutputTypeDef",
    "FilterOperationTargetVisualsConfigurationTypeDef",
    "SearchFoldersRequestRequestTypeDef",
    "ListFoldersResponseTypeDef",
    "SearchFoldersResponseTypeDef",
    "FontConfigurationTypeDef",
    "TypographyOutputTypeDef",
    "TypographyTypeDef",
    "ForecastScenarioOutputTypeDef",
    "ForecastScenarioTypeDef",
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    "SnapshotAnonymousUserTypeDef",
    "GeospatialWindowOptionsTypeDef",
    "GeospatialHeatmapColorScaleOutputTypeDef",
    "GeospatialHeatmapColorScaleTypeDef",
    "TableSideBorderOptionsTypeDef",
    "GradientColorOutputTypeDef",
    "GradientColorTypeDef",
    "GridLayoutCanvasSizeOptionsTypeDef",
    "SearchGroupsRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "IncrementalRefreshTypeDef",
    "IngestionTypeDef",
    "IntegerDatasetParameterOutputTypeDef",
    "IntegerDatasetParameterTypeDef",
    "JoinInstructionTypeDef",
    "LineChartDefaultSeriesSettingsTypeDef",
    "LineChartSeriesSettingsTypeDef",
    "ListAnalysesRequestListAnalysesPaginateTypeDef",
    "ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef",
    "ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef",
    "ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef",
    "ListDashboardsRequestListDashboardsPaginateTypeDef",
    "ListDataSetsRequestListDataSetsPaginateTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef",
    "ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef",
    "ListIngestionsRequestListIngestionsPaginateTypeDef",
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    "ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef",
    "ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef",
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    "ListThemeVersionsRequestListThemeVersionsPaginateTypeDef",
    "ListThemesRequestListThemesPaginateTypeDef",
    "ListUserGroupsRequestListUserGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "SearchAnalysesRequestSearchAnalysesPaginateTypeDef",
    "SearchDashboardsRequestSearchDashboardsPaginateTypeDef",
    "SearchDataSetsRequestSearchDataSetsPaginateTypeDef",
    "SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef",
    "SearchGroupsRequestSearchGroupsPaginateTypeDef",
    "ListFolderMembersResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesResponseTypeDef",
    "ListTopicsResponseTypeDef",
    "VisualSubtitleLabelOptionsTypeDef",
    "S3ParametersTypeDef",
    "TileLayoutStyleTypeDef",
    "NamedEntityDefinitionOutputTypeDef",
    "NamedEntityDefinitionTypeDef",
    "NamespaceInfoV2TypeDef",
    "VPCConnectionSummaryTypeDef",
    "VPCConnectionTypeDef",
    "OverrideDatasetParameterOperationOutputTypeDef",
    "OverrideDatasetParameterOperationTypeDef",
    "NumericSeparatorConfigurationTypeDef",
    "NumericalAggregationFunctionTypeDef",
    "ParametersOutputTypeDef",
    "ParametersTypeDef",
    "VisibleRangeOptionsTypeDef",
    "RadarChartSeriesSettingsTypeDef",
    "TopicRangeFilterConstantTypeDef",
    "RefreshFrequencyTypeDef",
    "RegisteredUserConsoleFeatureConfigurationsTypeDef",
    "RegisteredUserDashboardFeatureConfigurationsTypeDef",
    "RowLevelPermissionTagConfigurationOutputTypeDef",
    "RowLevelPermissionTagConfigurationTypeDef",
    "SnapshotS3DestinationConfigurationTypeDef",
    "S3SourceOutputTypeDef",
    "S3SourceTypeDef",
    "SectionPageBreakConfigurationTypeDef",
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    "SectionStyleTypeDef",
    "SelectedSheetsFilterScopeConfigurationOutputTypeDef",
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    "SheetElementRenderingRuleTypeDef",
    "VisualTitleLabelOptionsTypeDef",
    "SnapshotUserConfigurationRedactedTypeDef",
    "SnapshotFileOutputTypeDef",
    "SnapshotFileTypeDef",
    "StringDatasetParameterOutputTypeDef",
    "StringDatasetParameterTypeDef",
    "TableFieldImageConfigurationTypeDef",
    "TopicNumericEqualityFilterTypeDef",
    "TopicRelativeDateFilterTypeDef",
    "CascadingControlConfigurationOutputTypeDef",
    "CascadingControlConfigurationTypeDef",
    "DateTimeDefaultValuesOutputTypeDef",
    "DateTimeDefaultValuesTypeDef",
    "DecimalDefaultValuesOutputTypeDef",
    "DecimalDefaultValuesTypeDef",
    "IntegerDefaultValuesOutputTypeDef",
    "IntegerDefaultValuesTypeDef",
    "StringDefaultValuesOutputTypeDef",
    "StringDefaultValuesTypeDef",
    "DrillDownFilterOutputTypeDef",
    "DrillDownFilterTypeDef",
    "AnalysisTypeDef",
    "DashboardVersionTypeDef",
    "AnalysisSourceEntityTypeDef",
    "DashboardSourceEntityTypeDef",
    "TemplateSourceEntityTypeDef",
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    "DescribeAssetBundleExportJobResponseTypeDef",
    "StartAssetBundleExportJobRequestRequestTypeDef",
    "NumericAxisOptionsOutputTypeDef",
    "NumericAxisOptionsTypeDef",
    "CategoryFilterOutputTypeDef",
    "CategoryFilterTypeDef",
    "ClusterMarkerConfigurationTypeDef",
    "TopicCategoryFilterOutputTypeDef",
    "TopicCategoryFilterTypeDef",
    "TagColumnOperationOutputTypeDef",
    "TagColumnOperationTypeDef",
    "DataSetConfigurationOutputTypeDef",
    "DataSetConfigurationTypeDef",
    "ConditionalFormattingIconTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "ListDataSetsResponseTypeDef",
    "SearchDataSetsResponseTypeDef",
    "DestinationParameterValueConfigurationOutputTypeDef",
    "DestinationParameterValueConfigurationTypeDef",
    "DashboardPublishOptionsTypeDef",
    "VisualPaletteOutputTypeDef",
    "VisualPaletteTypeDef",
    "PivotTableFieldCollapseStateOptionOutputTypeDef",
    "PivotTableFieldCollapseStateOptionTypeDef",
    "TimeRangeFilterOutputTypeDef",
    "TimeRangeFilterTypeDef",
    "ListTopicRefreshSchedulesResponseTypeDef",
    "DefaultFormattingTypeDef",
    "CustomActionFilterOperationOutputTypeDef",
    "CustomActionFilterOperationTypeDef",
    "AxisLabelOptionsTypeDef",
    "DataLabelOptionsOutputTypeDef",
    "DataLabelOptionsTypeDef",
    "FunnelChartDataLabelOptionsTypeDef",
    "LabelOptionsTypeDef",
    "PanelTitleOptionsTypeDef",
    "TableFieldCustomTextContentTypeDef",
    "ForecastConfigurationOutputTypeDef",
    "ForecastConfigurationTypeDef",
    "DefaultFreeFormLayoutConfigurationTypeDef",
    "SnapshotUserConfigurationTypeDef",
    "GeospatialHeatmapConfigurationOutputTypeDef",
    "GeospatialHeatmapConfigurationTypeDef",
    "GlobalTableBorderOptionsTypeDef",
    "ConditionalFormattingGradientColorOutputTypeDef",
    "ConditionalFormattingGradientColorTypeDef",
    "DefaultGridLayoutConfigurationTypeDef",
    "GridLayoutConfigurationOutputTypeDef",
    "GridLayoutConfigurationTypeDef",
    "RefreshConfigurationTypeDef",
    "DescribeIngestionResponseTypeDef",
    "ListIngestionsResponseTypeDef",
    "LogicalTableSourceTypeDef",
    "DataFieldSeriesItemTypeDef",
    "FieldSeriesItemTypeDef",
    "DataSourceParametersTypeDef",
    "SheetStyleTypeDef",
    "TopicNamedEntityOutputTypeDef",
    "TopicNamedEntityTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListVPCConnectionsResponseTypeDef",
    "DescribeVPCConnectionResponseTypeDef",
    "CurrencyDisplayFormatConfigurationTypeDef",
    "NumberDisplayFormatConfigurationTypeDef",
    "PercentageDisplayFormatConfigurationTypeDef",
    "AggregationFunctionTypeDef",
    "ScrollBarOptionsTypeDef",
    "TopicDateRangeFilterTypeDef",
    "TopicNumericRangeFilterTypeDef",
    "RefreshScheduleOutputTypeDef",
    "RefreshScheduleTypeDef",
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    "SnapshotDestinationConfigurationOutputTypeDef",
    "SnapshotDestinationConfigurationTypeDef",
    "SnapshotJobS3ResultTypeDef",
    "PhysicalTableOutputTypeDef",
    "PhysicalTableTypeDef",
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    "FilterScopeConfigurationOutputTypeDef",
    "FilterScopeConfigurationTypeDef",
    "FreeFormLayoutElementOutputTypeDef",
    "FreeFormLayoutElementTypeDef",
    "SnapshotFileGroupOutputTypeDef",
    "SnapshotFileGroupTypeDef",
    "DatasetParameterOutputTypeDef",
    "DatasetParameterTypeDef",
    "DateTimeParameterDeclarationOutputTypeDef",
    "DateTimeParameterDeclarationTypeDef",
    "DecimalParameterDeclarationOutputTypeDef",
    "DecimalParameterDeclarationTypeDef",
    "IntegerParameterDeclarationOutputTypeDef",
    "IntegerParameterDeclarationTypeDef",
    "StringParameterDeclarationOutputTypeDef",
    "StringParameterDeclarationTypeDef",
    "DateTimeHierarchyOutputTypeDef",
    "ExplicitHierarchyOutputTypeDef",
    "PredefinedHierarchyOutputTypeDef",
    "DateTimeHierarchyTypeDef",
    "ExplicitHierarchyTypeDef",
    "PredefinedHierarchyTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DashboardTypeDef",
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    "AxisDataOptionsOutputTypeDef",
    "AxisDataOptionsTypeDef",
    "TransformOperationOutputTypeDef",
    "TransformOperationTypeDef",
    "TemplateVersionTypeDef",
    "SetParameterValueConfigurationOutputTypeDef",
    "SetParameterValueConfigurationTypeDef",
    "PivotTableFieldOptionsOutputTypeDef",
    "PivotTableFieldOptionsTypeDef",
    "TopicCalculatedFieldOutputTypeDef",
    "TopicCalculatedFieldTypeDef",
    "TopicColumnOutputTypeDef",
    "TopicColumnTypeDef",
    "ChartAxisLabelOptionsOutputTypeDef",
    "ChartAxisLabelOptionsTypeDef",
    "AxisTickLabelOptionsTypeDef",
    "DateTimePickerControlDisplayOptionsTypeDef",
    "DropDownControlDisplayOptionsTypeDef",
    "LegendOptionsTypeDef",
    "ListControlDisplayOptionsTypeDef",
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    "SliderControlDisplayOptionsTypeDef",
    "TextAreaControlDisplayOptionsTypeDef",
    "TextFieldControlDisplayOptionsTypeDef",
    "PanelConfigurationTypeDef",
    "TableFieldLinkContentConfigurationTypeDef",
    "GeospatialPointStyleOptionsOutputTypeDef",
    "GeospatialPointStyleOptionsTypeDef",
    "TableCellStyleTypeDef",
    "ConditionalFormattingColorOutputTypeDef",
    "ConditionalFormattingColorTypeDef",
    "DefaultInteractiveLayoutConfigurationTypeDef",
    "SheetControlLayoutConfigurationOutputTypeDef",
    "SheetControlLayoutConfigurationTypeDef",
    "DataSetRefreshPropertiesTypeDef",
    "SeriesItemTypeDef",
    "AssetBundleImportJobDataSourceOverrideParametersTypeDef",
    "CredentialPairTypeDef",
    "DataSourceTypeDef",
    "ThemeConfigurationOutputTypeDef",
    "ThemeConfigurationTypeDef",
    "ComparisonFormatConfigurationTypeDef",
    "NumericFormatConfigurationTypeDef",
    "AggregationSortConfigurationTypeDef",
    "ColumnSortTypeDef",
    "ColumnTooltipItemTypeDef",
    "NumericEqualityFilterTypeDef",
    "NumericRangeFilterTypeDef",
    "ReferenceLineDynamicDataConfigurationTypeDef",
    "TopicFilterOutputTypeDef",
    "TopicFilterTypeDef",
    "DescribeRefreshScheduleResponseTypeDef",
    "ListRefreshSchedulesResponseTypeDef",
    "CreateRefreshScheduleRequestRequestTypeDef",
    "UpdateRefreshScheduleRequestRequestTypeDef",
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    "SnapshotJobResultFileGroupTypeDef",
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    "FreeFormLayoutConfigurationOutputTypeDef",
    "FreeFormSectionLayoutConfigurationOutputTypeDef",
    "FreeFormLayoutConfigurationTypeDef",
    "FreeFormSectionLayoutConfigurationTypeDef",
    "SnapshotConfigurationOutputTypeDef",
    "SnapshotConfigurationTypeDef",
    "ParameterDeclarationOutputTypeDef",
    "ParameterDeclarationTypeDef",
    "ColumnHierarchyOutputTypeDef",
    "ColumnHierarchyTypeDef",
    "DescribeDashboardResponseTypeDef",
    "LogicalTableOutputTypeDef",
    "LogicalTableTypeDef",
    "TemplateTypeDef",
    "CustomActionSetParametersOperationOutputTypeDef",
    "CustomActionSetParametersOperationTypeDef",
    "AxisDisplayOptionsOutputTypeDef",
    "AxisDisplayOptionsTypeDef",
    "FilterDateTimePickerControlTypeDef",
    "ParameterDateTimePickerControlTypeDef",
    "FilterDropDownControlOutputTypeDef",
    "FilterDropDownControlTypeDef",
    "ParameterDropDownControlOutputTypeDef",
    "ParameterDropDownControlTypeDef",
    "FilterListControlOutputTypeDef",
    "FilterListControlTypeDef",
    "ParameterListControlOutputTypeDef",
    "ParameterListControlTypeDef",
    "FilterRelativeDateTimeControlTypeDef",
    "FilterSliderControlTypeDef",
    "ParameterSliderControlTypeDef",
    "FilterTextAreaControlTypeDef",
    "ParameterTextAreaControlTypeDef",
    "FilterTextFieldControlTypeDef",
    "ParameterTextFieldControlTypeDef",
    "SmallMultiplesOptionsTypeDef",
    "TableFieldLinkConfigurationTypeDef",
    "PivotTableOptionsOutputTypeDef",
    "PivotTableOptionsTypeDef",
    "PivotTotalOptionsTypeDef",
    "SubtotalOptionsOutputTypeDef",
    "SubtotalOptionsTypeDef",
    "TableOptionsOutputTypeDef",
    "TableOptionsTypeDef",
    "TotalOptionsTypeDef",
    "GaugeChartArcConditionalFormattingOutputTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingOutputTypeDef",
    "KPIPrimaryValueConditionalFormattingOutputTypeDef",
    "KPIProgressBarConditionalFormattingOutputTypeDef",
    "ShapeConditionalFormatOutputTypeDef",
    "TableRowConditionalFormattingOutputTypeDef",
    "TextConditionalFormatOutputTypeDef",
    "GaugeChartArcConditionalFormattingTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    "KPIPrimaryValueConditionalFormattingTypeDef",
    "KPIProgressBarConditionalFormattingTypeDef",
    "ShapeConditionalFormatTypeDef",
    "TableRowConditionalFormattingTypeDef",
    "TextConditionalFormatTypeDef",
    "SheetControlLayoutOutputTypeDef",
    "SheetControlLayoutTypeDef",
    "DescribeDataSetRefreshPropertiesResponseTypeDef",
    "PutDataSetRefreshPropertiesRequestRequestTypeDef",
    "AssetBundleImportJobOverrideParametersOutputTypeDef",
    "AssetBundleImportJobOverrideParametersTypeDef",
    "DataSourceCredentialsTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ThemeVersionTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "ComparisonConfigurationTypeDef",
    "DateTimeFormatConfigurationTypeDef",
    "NumberFormatConfigurationTypeDef",
    "ReferenceLineValueLabelConfigurationTypeDef",
    "StringFormatConfigurationTypeDef",
    "TopBottomFilterOutputTypeDef",
    "TopBottomFilterTypeDef",
    "FieldSortOptionsTypeDef",
    "PivotTableSortByOutputTypeDef",
    "PivotTableSortByTypeDef",
    "TooltipItemTypeDef",
    "ReferenceLineDataConfigurationTypeDef",
    "DatasetMetadataOutputTypeDef",
    "DatasetMetadataTypeDef",
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    "AnonymousUserSnapshotJobResultTypeDef",
    "DefaultPaginatedLayoutConfigurationTypeDef",
    "SectionLayoutConfigurationOutputTypeDef",
    "SectionLayoutConfigurationTypeDef",
    "DescribeDashboardSnapshotJobResponseTypeDef",
    "StartDashboardSnapshotJobRequestRequestTypeDef",
    "DataSetTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "DescribeTemplateResponseTypeDef",
    "VisualCustomActionOperationOutputTypeDef",
    "VisualCustomActionOperationTypeDef",
    "LineSeriesAxisDisplayOptionsOutputTypeDef",
    "LineSeriesAxisDisplayOptionsTypeDef",
    "FilterControlOutputTypeDef",
    "FilterControlTypeDef",
    "ParameterControlOutputTypeDef",
    "ParameterControlTypeDef",
    "TableFieldURLConfigurationTypeDef",
    "PivotTableTotalOptionsOutputTypeDef",
    "PivotTableTotalOptionsTypeDef",
    "GaugeChartConditionalFormattingOptionOutputTypeDef",
    "KPIConditionalFormattingOptionOutputTypeDef",
    "FilledMapShapeConditionalFormattingOutputTypeDef",
    "PivotTableCellConditionalFormattingOutputTypeDef",
    "TableCellConditionalFormattingOutputTypeDef",
    "GaugeChartConditionalFormattingOptionTypeDef",
    "KPIConditionalFormattingOptionTypeDef",
    "FilledMapShapeConditionalFormattingTypeDef",
    "PivotTableCellConditionalFormattingTypeDef",
    "TableCellConditionalFormattingTypeDef",
    "DescribeAssetBundleImportJobResponseTypeDef",
    "StartAssetBundleImportJobRequestRequestTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "ThemeTypeDef",
    "GaugeChartOptionsTypeDef",
    "KPIOptionsTypeDef",
    "DateDimensionFieldTypeDef",
    "DateMeasureFieldTypeDef",
    "NumericalDimensionFieldTypeDef",
    "NumericalMeasureFieldTypeDef",
    "ReferenceLineLabelConfigurationTypeDef",
    "CategoricalDimensionFieldTypeDef",
    "CategoricalMeasureFieldTypeDef",
    "FormatConfigurationTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "BarChartSortConfigurationOutputTypeDef",
    "BarChartSortConfigurationTypeDef",
    "BoxPlotSortConfigurationOutputTypeDef",
    "BoxPlotSortConfigurationTypeDef",
    "ComboChartSortConfigurationOutputTypeDef",
    "ComboChartSortConfigurationTypeDef",
    "FilledMapSortConfigurationOutputTypeDef",
    "FilledMapSortConfigurationTypeDef",
    "FunnelChartSortConfigurationOutputTypeDef",
    "FunnelChartSortConfigurationTypeDef",
    "HeatMapSortConfigurationOutputTypeDef",
    "HeatMapSortConfigurationTypeDef",
    "KPISortConfigurationOutputTypeDef",
    "KPISortConfigurationTypeDef",
    "LineChartSortConfigurationOutputTypeDef",
    "LineChartSortConfigurationTypeDef",
    "PieChartSortConfigurationOutputTypeDef",
    "PieChartSortConfigurationTypeDef",
    "RadarChartSortConfigurationOutputTypeDef",
    "RadarChartSortConfigurationTypeDef",
    "SankeyDiagramSortConfigurationOutputTypeDef",
    "SankeyDiagramSortConfigurationTypeDef",
    "TableSortConfigurationOutputTypeDef",
    "TableSortConfigurationTypeDef",
    "TreeMapSortConfigurationOutputTypeDef",
    "TreeMapSortConfigurationTypeDef",
    "WaterfallChartSortConfigurationOutputTypeDef",
    "WaterfallChartSortConfigurationTypeDef",
    "WordCloudSortConfigurationOutputTypeDef",
    "WordCloudSortConfigurationTypeDef",
    "PivotFieldSortOptionsOutputTypeDef",
    "PivotFieldSortOptionsTypeDef",
    "FieldBasedTooltipOutputTypeDef",
    "FieldBasedTooltipTypeDef",
    "TopicDetailsOutputTypeDef",
    "TopicDetailsTypeDef",
    "SnapshotJobResultTypeDef",
    "DefaultNewSheetConfigurationTypeDef",
    "BodySectionContentOutputTypeDef",
    "HeaderFooterSectionConfigurationOutputTypeDef",
    "BodySectionContentTypeDef",
    "HeaderFooterSectionConfigurationTypeDef",
    "DescribeDataSetResponseTypeDef",
    "VisualCustomActionOutputTypeDef",
    "VisualCustomActionTypeDef",
    "TableFieldOptionTypeDef",
    "GaugeChartConditionalFormattingOutputTypeDef",
    "KPIConditionalFormattingOutputTypeDef",
    "FilledMapConditionalFormattingOptionOutputTypeDef",
    "PivotTableConditionalFormattingOptionOutputTypeDef",
    "TableConditionalFormattingOptionOutputTypeDef",
    "GaugeChartConditionalFormattingTypeDef",
    "KPIConditionalFormattingTypeDef",
    "FilledMapConditionalFormattingOptionTypeDef",
    "PivotTableConditionalFormattingOptionTypeDef",
    "TableConditionalFormattingOptionTypeDef",
    "DescribeThemeResponseTypeDef",
    "ReferenceLineTypeDef",
    "DimensionFieldTypeDef",
    "MeasureFieldTypeDef",
    "ColumnConfigurationOutputTypeDef",
    "ColumnConfigurationTypeDef",
    "UnaggregatedFieldTypeDef",
    "FilterGroupOutputTypeDef",
    "FilterGroupTypeDef",
    "PivotTableSortConfigurationOutputTypeDef",
    "PivotTableSortConfigurationTypeDef",
    "TooltipOptionsOutputTypeDef",
    "TooltipOptionsTypeDef",
    "DescribeTopicResponseTypeDef",
    "CreateTopicRequestRequestTypeDef",
    "UpdateTopicRequestRequestTypeDef",
    "DescribeDashboardSnapshotJobResultResponseTypeDef",
    "AnalysisDefaultsTypeDef",
    "BodySectionConfigurationOutputTypeDef",
    "BodySectionConfigurationTypeDef",
    "CustomContentVisualOutputTypeDef",
    "EmptyVisualOutputTypeDef",
    "CustomContentVisualTypeDef",
    "EmptyVisualTypeDef",
    "TableFieldOptionsOutputTypeDef",
    "TableFieldOptionsTypeDef",
    "FilledMapConditionalFormattingOutputTypeDef",
    "PivotTableConditionalFormattingOutputTypeDef",
    "TableConditionalFormattingOutputTypeDef",
    "FilledMapConditionalFormattingTypeDef",
    "PivotTableConditionalFormattingTypeDef",
    "TableConditionalFormattingTypeDef",
    "UniqueValuesComputationTypeDef",
    "BarChartAggregatedFieldWellsOutputTypeDef",
    "BarChartAggregatedFieldWellsTypeDef",
    "BoxPlotAggregatedFieldWellsOutputTypeDef",
    "BoxPlotAggregatedFieldWellsTypeDef",
    "ComboChartAggregatedFieldWellsOutputTypeDef",
    "ComboChartAggregatedFieldWellsTypeDef",
    "FilledMapAggregatedFieldWellsOutputTypeDef",
    "FilledMapAggregatedFieldWellsTypeDef",
    "ForecastComputationTypeDef",
    "FunnelChartAggregatedFieldWellsOutputTypeDef",
    "FunnelChartAggregatedFieldWellsTypeDef",
    "GaugeChartFieldWellsOutputTypeDef",
    "GaugeChartFieldWellsTypeDef",
    "GeospatialMapAggregatedFieldWellsOutputTypeDef",
    "GeospatialMapAggregatedFieldWellsTypeDef",
    "GrowthRateComputationTypeDef",
    "HeatMapAggregatedFieldWellsOutputTypeDef",
    "HeatMapAggregatedFieldWellsTypeDef",
    "HistogramAggregatedFieldWellsOutputTypeDef",
    "HistogramAggregatedFieldWellsTypeDef",
    "KPIFieldWellsOutputTypeDef",
    "KPIFieldWellsTypeDef",
    "LineChartAggregatedFieldWellsOutputTypeDef",
    "LineChartAggregatedFieldWellsTypeDef",
    "MaximumMinimumComputationTypeDef",
    "MetricComparisonComputationTypeDef",
    "PeriodOverPeriodComputationTypeDef",
    "PeriodToDateComputationTypeDef",
    "PieChartAggregatedFieldWellsOutputTypeDef",
    "PieChartAggregatedFieldWellsTypeDef",
    "PivotTableAggregatedFieldWellsOutputTypeDef",
    "PivotTableAggregatedFieldWellsTypeDef",
    "RadarChartAggregatedFieldWellsOutputTypeDef",
    "RadarChartAggregatedFieldWellsTypeDef",
    "SankeyDiagramAggregatedFieldWellsOutputTypeDef",
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    "ScatterPlotUnaggregatedFieldWellsOutputTypeDef",
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    "TableAggregatedFieldWellsOutputTypeDef",
    "TableAggregatedFieldWellsTypeDef",
    "TopBottomMoversComputationTypeDef",
    "TopBottomRankedComputationTypeDef",
    "TotalAggregationComputationTypeDef",
    "TreeMapAggregatedFieldWellsOutputTypeDef",
    "TreeMapAggregatedFieldWellsTypeDef",
    "WaterfallChartAggregatedFieldWellsOutputTypeDef",
    "WaterfallChartAggregatedFieldWellsTypeDef",
    "WordCloudAggregatedFieldWellsOutputTypeDef",
    "WordCloudAggregatedFieldWellsTypeDef",
    "TableUnaggregatedFieldWellsOutputTypeDef",
    "TableUnaggregatedFieldWellsTypeDef",
    "SectionBasedLayoutConfigurationOutputTypeDef",
    "SectionBasedLayoutConfigurationTypeDef",
    "BarChartFieldWellsOutputTypeDef",
    "BarChartFieldWellsTypeDef",
    "BoxPlotFieldWellsOutputTypeDef",
    "BoxPlotFieldWellsTypeDef",
    "ComboChartFieldWellsOutputTypeDef",
    "ComboChartFieldWellsTypeDef",
    "FilledMapFieldWellsOutputTypeDef",
    "FilledMapFieldWellsTypeDef",
    "FunnelChartFieldWellsOutputTypeDef",
    "FunnelChartFieldWellsTypeDef",
    "GaugeChartConfigurationOutputTypeDef",
    "GaugeChartConfigurationTypeDef",
    "GeospatialMapFieldWellsOutputTypeDef",
    "GeospatialMapFieldWellsTypeDef",
    "HeatMapFieldWellsOutputTypeDef",
    "HeatMapFieldWellsTypeDef",
    "HistogramFieldWellsOutputTypeDef",
    "HistogramFieldWellsTypeDef",
    "KPIConfigurationOutputTypeDef",
    "KPIConfigurationTypeDef",
    "LineChartFieldWellsOutputTypeDef",
    "LineChartFieldWellsTypeDef",
    "PieChartFieldWellsOutputTypeDef",
    "PieChartFieldWellsTypeDef",
    "PivotTableFieldWellsOutputTypeDef",
    "PivotTableFieldWellsTypeDef",
    "RadarChartFieldWellsOutputTypeDef",
    "RadarChartFieldWellsTypeDef",
    "SankeyDiagramFieldWellsOutputTypeDef",
    "SankeyDiagramFieldWellsTypeDef",
    "ScatterPlotFieldWellsOutputTypeDef",
    "ScatterPlotFieldWellsTypeDef",
    "ComputationTypeDef",
    "TreeMapFieldWellsOutputTypeDef",
    "TreeMapFieldWellsTypeDef",
    "WaterfallChartFieldWellsOutputTypeDef",
    "WaterfallChartFieldWellsTypeDef",
    "WordCloudFieldWellsOutputTypeDef",
    "WordCloudFieldWellsTypeDef",
    "TableFieldWellsOutputTypeDef",
    "TableFieldWellsTypeDef",
    "LayoutConfigurationOutputTypeDef",
    "LayoutConfigurationTypeDef",
    "BarChartConfigurationOutputTypeDef",
    "BarChartConfigurationTypeDef",
    "BoxPlotChartConfigurationOutputTypeDef",
    "BoxPlotChartConfigurationTypeDef",
    "ComboChartConfigurationOutputTypeDef",
    "ComboChartConfigurationTypeDef",
    "FilledMapConfigurationOutputTypeDef",
    "FilledMapConfigurationTypeDef",
    "FunnelChartConfigurationOutputTypeDef",
    "FunnelChartConfigurationTypeDef",
    "GaugeChartVisualOutputTypeDef",
    "GaugeChartVisualTypeDef",
    "GeospatialMapConfigurationOutputTypeDef",
    "GeospatialMapConfigurationTypeDef",
    "HeatMapConfigurationOutputTypeDef",
    "HeatMapConfigurationTypeDef",
    "HistogramConfigurationOutputTypeDef",
    "HistogramConfigurationTypeDef",
    "KPIVisualOutputTypeDef",
    "KPIVisualTypeDef",
    "LineChartConfigurationOutputTypeDef",
    "LineChartConfigurationTypeDef",
    "PieChartConfigurationOutputTypeDef",
    "PieChartConfigurationTypeDef",
    "PivotTableConfigurationOutputTypeDef",
    "PivotTableConfigurationTypeDef",
    "RadarChartConfigurationOutputTypeDef",
    "RadarChartConfigurationTypeDef",
    "SankeyDiagramChartConfigurationOutputTypeDef",
    "SankeyDiagramChartConfigurationTypeDef",
    "ScatterPlotConfigurationOutputTypeDef",
    "ScatterPlotConfigurationTypeDef",
    "InsightConfigurationOutputTypeDef",
    "InsightConfigurationTypeDef",
    "TreeMapConfigurationOutputTypeDef",
    "TreeMapConfigurationTypeDef",
    "WaterfallChartConfigurationOutputTypeDef",
    "WaterfallChartConfigurationTypeDef",
    "WordCloudChartConfigurationOutputTypeDef",
    "WordCloudChartConfigurationTypeDef",
    "TableConfigurationOutputTypeDef",
    "TableConfigurationTypeDef",
    "LayoutOutputTypeDef",
    "LayoutTypeDef",
    "BarChartVisualOutputTypeDef",
    "BarChartVisualTypeDef",
    "BoxPlotVisualOutputTypeDef",
    "BoxPlotVisualTypeDef",
    "ComboChartVisualOutputTypeDef",
    "ComboChartVisualTypeDef",
    "FilledMapVisualOutputTypeDef",
    "FilledMapVisualTypeDef",
    "FunnelChartVisualOutputTypeDef",
    "FunnelChartVisualTypeDef",
    "GeospatialMapVisualOutputTypeDef",
    "GeospatialMapVisualTypeDef",
    "HeatMapVisualOutputTypeDef",
    "HeatMapVisualTypeDef",
    "HistogramVisualOutputTypeDef",
    "HistogramVisualTypeDef",
    "LineChartVisualOutputTypeDef",
    "LineChartVisualTypeDef",
    "PieChartVisualOutputTypeDef",
    "PieChartVisualTypeDef",
    "PivotTableVisualOutputTypeDef",
    "PivotTableVisualTypeDef",
    "RadarChartVisualOutputTypeDef",
    "RadarChartVisualTypeDef",
    "SankeyDiagramVisualOutputTypeDef",
    "SankeyDiagramVisualTypeDef",
    "ScatterPlotVisualOutputTypeDef",
    "ScatterPlotVisualTypeDef",
    "InsightVisualOutputTypeDef",
    "InsightVisualTypeDef",
    "TreeMapVisualOutputTypeDef",
    "TreeMapVisualTypeDef",
    "WaterfallVisualOutputTypeDef",
    "WaterfallVisualTypeDef",
    "WordCloudVisualOutputTypeDef",
    "WordCloudVisualTypeDef",
    "TableVisualOutputTypeDef",
    "TableVisualTypeDef",
    "VisualOutputTypeDef",
    "VisualTypeDef",
    "SheetDefinitionOutputTypeDef",
    "SheetDefinitionTypeDef",
    "AnalysisDefinitionOutputTypeDef",
    "DashboardVersionDefinitionOutputTypeDef",
    "TemplateVersionDefinitionOutputTypeDef",
    "AnalysisDefinitionTypeDef",
    "DashboardVersionDefinitionTypeDef",
    "TemplateVersionDefinitionTypeDef",
    "DescribeAnalysisDefinitionResponseTypeDef",
    "DescribeDashboardDefinitionResponseTypeDef",
    "DescribeTemplateDefinitionResponseTypeDef",
    "CreateAnalysisRequestRequestTypeDef",
    "UpdateAnalysisRequestRequestTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef",
    {
        "DefaultTheme": str,
        "DefaultEmailCustomizationTemplate": str,
    },
    total=False,
)

AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef",
    {
        "AccountName": str,
        "Edition": EditionType,
        "NotificationEmail": str,
        "AuthenticationType": str,
        "AccountSubscriptionStatus": str,
    },
    total=False,
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": str,
        "Edition": EditionType,
        "DefaultNamespace": str,
        "NotificationEmail": str,
        "PublicSharingEnabled": bool,
        "TerminationProtectionEnabled": bool,
    },
    total=False,
)

ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef",
    {
        "AssignmentName": str,
        "PolicyArn": str,
    },
    total=False,
)

AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

AttributeAggregationFunctionTypeDef = TypedDict(
    "AttributeAggregationFunctionTypeDef",
    {
        "SimpleAttributeAggregation": Literal["UNIQUE_VALUE"],
        "ValueForMultipleValues": str,
    },
    total=False,
)

ColumnIdentifierTypeDef = TypedDict(
    "ColumnIdentifierTypeDef",
    {
        "DataSetIdentifier": str,
        "ColumnName": str,
    },
)

AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef",
    {
        "Domain": str,
    },
)

AmazonOpenSearchParametersTypeDef = TypedDict(
    "AmazonOpenSearchParametersTypeDef",
    {
        "Domain": str,
    },
)

CalculatedFieldTypeDef = TypedDict(
    "CalculatedFieldTypeDef",
    {
        "DataSetIdentifier": str,
        "Name": str,
        "Expression": str,
    },
)

DataSetIdentifierDeclarationTypeDef = TypedDict(
    "DataSetIdentifierDeclarationTypeDef",
    {
        "Identifier": str,
        "DataSetArn": str,
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Path": str,
    },
    total=False,
)

AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": AnalysisFilterAttributeType,
        "Value": str,
    },
    total=False,
)

DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef",
    {
        "DataSetPlaceholder": str,
        "DataSetArn": str,
    },
)

AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "Name": str,
        "Status": ResourceStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

SheetTypeDef = TypedDict(
    "SheetTypeDef",
    {
        "SheetId": str,
        "Name": str,
    },
    total=False,
)

AnchorDateConfigurationTypeDef = TypedDict(
    "AnchorDateConfigurationTypeDef",
    {
        "AnchorOption": Literal["NOW"],
        "ParameterName": str,
    },
    total=False,
)

AnonymousUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)

DashboardVisualIdTypeDef = TypedDict(
    "DashboardVisualIdTypeDef",
    {
        "DashboardId": str,
        "SheetId": str,
        "VisualId": str,
    },
)

AnonymousUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
)

ArcAxisDisplayRangeTypeDef = TypedDict(
    "ArcAxisDisplayRangeTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

ArcConfigurationTypeDef = TypedDict(
    "ArcConfigurationTypeDef",
    {
        "ArcAngle": float,
        "ArcThickness": ArcThicknessOptionsType,
    },
    total=False,
)

ArcOptionsTypeDef = TypedDict(
    "ArcOptionsTypeDef",
    {
        "ArcThickness": ArcThicknessType,
    },
    total=False,
)

_RequiredAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef",
    {
        "Properties": List[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef",
    {
        "Properties": List[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobDashboardOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef",
    {
        "Properties": List[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobDataSetOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef",
    {
        "Properties": List[AssetBundleExportJobDataSourcePropertyToOverrideType],
    },
)
_OptionalAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef",
    {
        "Properties": List[Literal["StartAfterDateTime"]],
    },
)
_OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef,
):
    pass


AssetBundleExportJobResourceIdOverrideConfigurationTypeDef = TypedDict(
    "AssetBundleExportJobResourceIdOverrideConfigurationTypeDef",
    {
        "PrefixForAllResources": bool,
    },
    total=False,
)

_RequiredAssetBundleExportJobThemeOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobThemeOverridePropertiesOutputTypeDef",
    {
        "Properties": List[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobThemeOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobThemeOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobThemeOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobThemeOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobThemeOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef",
    {
        "Properties": List[AssetBundleExportJobVPCConnectionPropertyToOverrideType],
    },
)
_OptionalAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef(
    _RequiredAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef,
    _OptionalAssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef,
):
    pass


_RequiredAssetBundleExportJobAnalysisOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobAnalysisOverridePropertiesTypeDef",
    {
        "Properties": Sequence[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobAnalysisOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobAnalysisOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobAnalysisOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobAnalysisOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobAnalysisOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobDashboardOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDashboardOverridePropertiesTypeDef",
    {
        "Properties": Sequence[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobDashboardOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDashboardOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDashboardOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobDashboardOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobDashboardOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobDataSetOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDataSetOverridePropertiesTypeDef",
    {
        "Properties": Sequence[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobDataSetOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDataSetOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDataSetOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobDataSetOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobDataSetOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobDataSourceOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobDataSourceOverridePropertiesTypeDef",
    {
        "Properties": Sequence[AssetBundleExportJobDataSourcePropertyToOverrideType],
    },
)
_OptionalAssetBundleExportJobDataSourceOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobDataSourceOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobDataSourceOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobDataSourceOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobDataSourceOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef",
    {
        "Properties": Sequence[Literal["StartAfterDateTime"]],
    },
)
_OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobThemeOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobThemeOverridePropertiesTypeDef",
    {
        "Properties": Sequence[Literal["Name"]],
    },
)
_OptionalAssetBundleExportJobThemeOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobThemeOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobThemeOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobThemeOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobThemeOverridePropertiesTypeDef,
):
    pass


_RequiredAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef = TypedDict(
    "_RequiredAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef",
    {
        "Properties": Sequence[AssetBundleExportJobVPCConnectionPropertyToOverrideType],
    },
)
_OptionalAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef = TypedDict(
    "_OptionalAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef",
    {
        "Arn": str,
    },
    total=False,
)


class AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef(
    _RequiredAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef,
    _OptionalAssetBundleExportJobVPCConnectionOverridePropertiesTypeDef,
):
    pass


AssetBundleExportJobErrorTypeDef = TypedDict(
    "AssetBundleExportJobErrorTypeDef",
    {
        "Arn": str,
        "Type": str,
        "Message": str,
    },
    total=False,
)

AssetBundleExportJobSummaryTypeDef = TypedDict(
    "AssetBundleExportJobSummaryTypeDef",
    {
        "JobStatus": AssetBundleExportJobStatusType,
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleExportJobId": str,
        "IncludeAllDependencies": bool,
        "ExportFormat": AssetBundleExportFormatType,
    },
    total=False,
)

_RequiredAssetBundleImportJobAnalysisOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobAnalysisOverrideParametersTypeDef",
    {
        "AnalysisId": str,
    },
)
_OptionalAssetBundleImportJobAnalysisOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobAnalysisOverrideParametersTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AssetBundleImportJobAnalysisOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobAnalysisOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobAnalysisOverrideParametersTypeDef,
):
    pass


_RequiredAssetBundleImportJobDashboardOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobDashboardOverrideParametersTypeDef",
    {
        "DashboardId": str,
    },
)
_OptionalAssetBundleImportJobDashboardOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobDashboardOverrideParametersTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AssetBundleImportJobDashboardOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobDashboardOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobDashboardOverrideParametersTypeDef,
):
    pass


_RequiredAssetBundleImportJobDataSetOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobDataSetOverrideParametersTypeDef",
    {
        "DataSetId": str,
    },
)
_OptionalAssetBundleImportJobDataSetOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobDataSetOverrideParametersTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AssetBundleImportJobDataSetOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobDataSetOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobDataSetOverrideParametersTypeDef,
):
    pass


AssetBundleImportJobDataSourceCredentialPairTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceCredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

SslPropertiesTypeDef = TypedDict(
    "SslPropertiesTypeDef",
    {
        "DisableSsl": bool,
    },
    total=False,
)

VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef",
    {
        "VpcConnectionArn": str,
    },
)

AssetBundleImportJobErrorTypeDef = TypedDict(
    "AssetBundleImportJobErrorTypeDef",
    {
        "Arn": str,
        "Type": str,
        "Message": str,
    },
    total=False,
)

_RequiredAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef",
    {
        "DataSetId": str,
        "ScheduleId": str,
    },
)
_OptionalAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef",
    {
        "StartAfterDateTime": datetime,
    },
    total=False,
)


class AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef(
    _RequiredAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef,
    _OptionalAssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef,
):
    pass


AssetBundleImportJobResourceIdOverrideConfigurationTypeDef = TypedDict(
    "AssetBundleImportJobResourceIdOverrideConfigurationTypeDef",
    {
        "PrefixForAllResources": str,
    },
    total=False,
)

_RequiredAssetBundleImportJobThemeOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobThemeOverrideParametersTypeDef",
    {
        "ThemeId": str,
    },
)
_OptionalAssetBundleImportJobThemeOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobThemeOverrideParametersTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class AssetBundleImportJobThemeOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobThemeOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobThemeOverrideParametersTypeDef,
):
    pass


_RequiredAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef",
    {
        "VPCConnectionId": str,
    },
)
_OptionalAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef",
    {
        "Name": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "DnsResolvers": List[str],
        "RoleArn": str,
    },
    total=False,
)


class AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef(
    _RequiredAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef,
    _OptionalAssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef,
):
    pass


_RequiredAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef",
    {
        "DataSetId": str,
        "ScheduleId": str,
    },
)
_OptionalAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef",
    {
        "StartAfterDateTime": Union[datetime, str],
    },
    total=False,
)


class AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobRefreshScheduleOverrideParametersTypeDef,
):
    pass


_RequiredAssetBundleImportJobVPCConnectionOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobVPCConnectionOverrideParametersTypeDef",
    {
        "VPCConnectionId": str,
    },
)
_OptionalAssetBundleImportJobVPCConnectionOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobVPCConnectionOverrideParametersTypeDef",
    {
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "DnsResolvers": Sequence[str],
        "RoleArn": str,
    },
    total=False,
)


class AssetBundleImportJobVPCConnectionOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobVPCConnectionOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobVPCConnectionOverrideParametersTypeDef,
):
    pass


AssetBundleImportJobSummaryTypeDef = TypedDict(
    "AssetBundleImportJobSummaryTypeDef",
    {
        "JobStatus": AssetBundleImportJobStatusType,
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleImportJobId": str,
        "FailureAction": AssetBundleImportFailureActionType,
    },
    total=False,
)

AssetBundleImportSourceDescriptionTypeDef = TypedDict(
    "AssetBundleImportSourceDescriptionTypeDef",
    {
        "Body": str,
        "S3Uri": str,
    },
    total=False,
)

AssetBundleImportSourceTypeDef = TypedDict(
    "AssetBundleImportSourceTypeDef",
    {
        "Body": Union[str, bytes, IO[Any], StreamingBody],
        "S3Uri": str,
    },
    total=False,
)

AthenaParametersTypeDef = TypedDict(
    "AthenaParametersTypeDef",
    {
        "WorkGroup": str,
        "RoleArn": str,
    },
    total=False,
)

AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef",
    {
        "DataSetName": str,
    },
)

DateAxisOptionsTypeDef = TypedDict(
    "DateAxisOptionsTypeDef",
    {
        "MissingDateVisibility": VisibilityType,
    },
    total=False,
)

AxisDisplayMinMaxRangeTypeDef = TypedDict(
    "AxisDisplayMinMaxRangeTypeDef",
    {
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)

AxisLinearScaleTypeDef = TypedDict(
    "AxisLinearScaleTypeDef",
    {
        "StepCount": int,
        "StepSize": float,
    },
    total=False,
)

AxisLogarithmicScaleTypeDef = TypedDict(
    "AxisLogarithmicScaleTypeDef",
    {
        "Base": float,
    },
    total=False,
)

ItemsLimitConfigurationTypeDef = TypedDict(
    "ItemsLimitConfigurationTypeDef",
    {
        "ItemsLimit": int,
        "OtherCategories": OtherCategoriesType,
    },
    total=False,
)

BinCountOptionsTypeDef = TypedDict(
    "BinCountOptionsTypeDef",
    {
        "Value": int,
    },
    total=False,
)

BinWidthOptionsTypeDef = TypedDict(
    "BinWidthOptionsTypeDef",
    {
        "Value": float,
        "BinCountLimit": int,
    },
    total=False,
)

BookmarksConfigurationsTypeDef = TypedDict(
    "BookmarksConfigurationsTypeDef",
    {
        "Enabled": bool,
    },
)

BorderStyleTypeDef = TypedDict(
    "BorderStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

BoxPlotStyleOptionsTypeDef = TypedDict(
    "BoxPlotStyleOptionsTypeDef",
    {
        "FillStyle": BoxPlotFillStyleType,
    },
    total=False,
)

PaginationConfigurationTypeDef = TypedDict(
    "PaginationConfigurationTypeDef",
    {
        "PageSize": int,
        "PageNumber": int,
    },
)

CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnId": str,
        "Expression": str,
    },
)

CalculatedMeasureFieldTypeDef = TypedDict(
    "CalculatedMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Expression": str,
    },
)

CancelIngestionRequestRequestTypeDef = TypedDict(
    "CancelIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
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

_RequiredCastColumnTypeOperationTypeDef = TypedDict(
    "_RequiredCastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": ColumnDataTypeType,
    },
)
_OptionalCastColumnTypeOperationTypeDef = TypedDict(
    "_OptionalCastColumnTypeOperationTypeDef",
    {
        "Format": str,
    },
    total=False,
)


class CastColumnTypeOperationTypeDef(
    _RequiredCastColumnTypeOperationTypeDef, _OptionalCastColumnTypeOperationTypeDef
):
    pass


_RequiredCustomFilterConfigurationTypeDef = TypedDict(
    "_RequiredCustomFilterConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalCustomFilterConfigurationTypeDef = TypedDict(
    "_OptionalCustomFilterConfigurationTypeDef",
    {
        "CategoryValue": str,
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "ParameterName": str,
    },
    total=False,
)


class CustomFilterConfigurationTypeDef(
    _RequiredCustomFilterConfigurationTypeDef, _OptionalCustomFilterConfigurationTypeDef
):
    pass


_RequiredCustomFilterListConfigurationOutputTypeDef = TypedDict(
    "_RequiredCustomFilterListConfigurationOutputTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalCustomFilterListConfigurationOutputTypeDef = TypedDict(
    "_OptionalCustomFilterListConfigurationOutputTypeDef",
    {
        "CategoryValues": List[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)


class CustomFilterListConfigurationOutputTypeDef(
    _RequiredCustomFilterListConfigurationOutputTypeDef,
    _OptionalCustomFilterListConfigurationOutputTypeDef,
):
    pass


_RequiredFilterListConfigurationOutputTypeDef = TypedDict(
    "_RequiredFilterListConfigurationOutputTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
    },
)
_OptionalFilterListConfigurationOutputTypeDef = TypedDict(
    "_OptionalFilterListConfigurationOutputTypeDef",
    {
        "CategoryValues": List[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)


class FilterListConfigurationOutputTypeDef(
    _RequiredFilterListConfigurationOutputTypeDef, _OptionalFilterListConfigurationOutputTypeDef
):
    pass


_RequiredCustomFilterListConfigurationTypeDef = TypedDict(
    "_RequiredCustomFilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalCustomFilterListConfigurationTypeDef = TypedDict(
    "_OptionalCustomFilterListConfigurationTypeDef",
    {
        "CategoryValues": Sequence[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)


class CustomFilterListConfigurationTypeDef(
    _RequiredCustomFilterListConfigurationTypeDef, _OptionalCustomFilterListConfigurationTypeDef
):
    pass


_RequiredFilterListConfigurationTypeDef = TypedDict(
    "_RequiredFilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
    },
)
_OptionalFilterListConfigurationTypeDef = TypedDict(
    "_OptionalFilterListConfigurationTypeDef",
    {
        "CategoryValues": Sequence[str],
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
    },
    total=False,
)


class FilterListConfigurationTypeDef(
    _RequiredFilterListConfigurationTypeDef, _OptionalFilterListConfigurationTypeDef
):
    pass


CellValueSynonymOutputTypeDef = TypedDict(
    "CellValueSynonymOutputTypeDef",
    {
        "CellValue": str,
        "Synonyms": List[str],
    },
    total=False,
)

CellValueSynonymTypeDef = TypedDict(
    "CellValueSynonymTypeDef",
    {
        "CellValue": str,
        "Synonyms": Sequence[str],
    },
    total=False,
)

SimpleClusterMarkerTypeDef = TypedDict(
    "SimpleClusterMarkerTypeDef",
    {
        "Color": str,
    },
    total=False,
)

CollectiveConstantOutputTypeDef = TypedDict(
    "CollectiveConstantOutputTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

CollectiveConstantTypeDef = TypedDict(
    "CollectiveConstantTypeDef",
    {
        "ValueList": Sequence[str],
    },
    total=False,
)

DataColorTypeDef = TypedDict(
    "DataColorTypeDef",
    {
        "Color": str,
        "DataValue": float,
    },
    total=False,
)

_RequiredCustomColorTypeDef = TypedDict(
    "_RequiredCustomColorTypeDef",
    {
        "Color": str,
    },
)
_OptionalCustomColorTypeDef = TypedDict(
    "_OptionalCustomColorTypeDef",
    {
        "FieldValue": str,
        "SpecialValue": SpecialValueType,
    },
    total=False,
)


class CustomColorTypeDef(_RequiredCustomColorTypeDef, _OptionalCustomColorTypeDef):
    pass


ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "Text": str,
    },
    total=False,
)

ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredGeoSpatialColumnGroupOutputTypeDef = TypedDict(
    "_RequiredGeoSpatialColumnGroupOutputTypeDef",
    {
        "Name": str,
        "Columns": List[str],
    },
)
_OptionalGeoSpatialColumnGroupOutputTypeDef = TypedDict(
    "_OptionalGeoSpatialColumnGroupOutputTypeDef",
    {
        "CountryCode": Literal["US"],
    },
    total=False,
)


class GeoSpatialColumnGroupOutputTypeDef(
    _RequiredGeoSpatialColumnGroupOutputTypeDef, _OptionalGeoSpatialColumnGroupOutputTypeDef
):
    pass


_RequiredGeoSpatialColumnGroupTypeDef = TypedDict(
    "_RequiredGeoSpatialColumnGroupTypeDef",
    {
        "Name": str,
        "Columns": Sequence[str],
    },
)
_OptionalGeoSpatialColumnGroupTypeDef = TypedDict(
    "_OptionalGeoSpatialColumnGroupTypeDef",
    {
        "CountryCode": Literal["US"],
    },
    total=False,
)


class GeoSpatialColumnGroupTypeDef(
    _RequiredGeoSpatialColumnGroupTypeDef, _OptionalGeoSpatialColumnGroupTypeDef
):
    pass


ColumnLevelPermissionRuleOutputTypeDef = TypedDict(
    "ColumnLevelPermissionRuleOutputTypeDef",
    {
        "Principals": List[str],
        "ColumnNames": List[str],
    },
    total=False,
)

ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {
        "Principals": Sequence[str],
        "ColumnNames": Sequence[str],
    },
    total=False,
)

ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "Name": str,
        "DataType": str,
        "GeographicRole": str,
    },
    total=False,
)

ComparativeOrderOutputTypeDef = TypedDict(
    "ComparativeOrderOutputTypeDef",
    {
        "UseOrdering": ColumnOrderingTypeType,
        "SpecifedOrder": List[str],
        "TreatUndefinedSpecifiedValues": UndefinedSpecifiedValueTypeType,
    },
    total=False,
)

ComparativeOrderTypeDef = TypedDict(
    "ComparativeOrderTypeDef",
    {
        "UseOrdering": ColumnOrderingTypeType,
        "SpecifedOrder": Sequence[str],
        "TreatUndefinedSpecifiedValues": UndefinedSpecifiedValueTypeType,
    },
    total=False,
)

_RequiredConditionalFormattingSolidColorTypeDef = TypedDict(
    "_RequiredConditionalFormattingSolidColorTypeDef",
    {
        "Expression": str,
    },
)
_OptionalConditionalFormattingSolidColorTypeDef = TypedDict(
    "_OptionalConditionalFormattingSolidColorTypeDef",
    {
        "Color": str,
    },
    total=False,
)


class ConditionalFormattingSolidColorTypeDef(
    _RequiredConditionalFormattingSolidColorTypeDef, _OptionalConditionalFormattingSolidColorTypeDef
):
    pass


ConditionalFormattingCustomIconOptionsTypeDef = TypedDict(
    "ConditionalFormattingCustomIconOptionsTypeDef",
    {
        "Icon": IconType,
        "UnicodeIcon": str,
    },
    total=False,
)

ConditionalFormattingIconDisplayConfigurationTypeDef = TypedDict(
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    {
        "IconDisplayOption": Literal["ICON_ONLY"],
    },
    total=False,
)

_RequiredConditionalFormattingIconSetTypeDef = TypedDict(
    "_RequiredConditionalFormattingIconSetTypeDef",
    {
        "Expression": str,
    },
)
_OptionalConditionalFormattingIconSetTypeDef = TypedDict(
    "_OptionalConditionalFormattingIconSetTypeDef",
    {
        "IconSetType": ConditionalFormattingIconSetTypeType,
    },
    total=False,
)


class ConditionalFormattingIconSetTypeDef(
    _RequiredConditionalFormattingIconSetTypeDef, _OptionalConditionalFormattingIconSetTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredCreateAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccountSubscriptionRequestRequestTypeDef",
    {
        "Edition": EditionType,
        "AuthenticationMethod": AuthenticationMethodOptionType,
        "AwsAccountId": str,
        "AccountName": str,
        "NotificationEmail": str,
    },
)
_OptionalCreateAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccountSubscriptionRequestRequestTypeDef",
    {
        "ActiveDirectoryName": str,
        "Realm": str,
        "DirectoryId": str,
        "AdminGroup": Sequence[str],
        "AuthorGroup": Sequence[str],
        "ReaderGroup": Sequence[str],
        "FirstName": str,
        "LastName": str,
        "EmailAddress": str,
        "ContactNumber": str,
    },
    total=False,
)


class CreateAccountSubscriptionRequestRequestTypeDef(
    _RequiredCreateAccountSubscriptionRequestRequestTypeDef,
    _OptionalCreateAccountSubscriptionRequestRequestTypeDef,
):
    pass


SignupResponseTypeDef = TypedDict(
    "SignupResponseTypeDef",
    {
        "IAMUser": bool,
        "userLoginName": str,
        "accountName": str,
        "directoryType": str,
    },
    total=False,
)

ResourcePermissionOutputTypeDef = TypedDict(
    "ResourcePermissionOutputTypeDef",
    {
        "Principal": str,
        "Actions": List[str],
    },
)

ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "Principal": str,
        "Actions": Sequence[str],
    },
)

DataSetUsageConfigurationTypeDef = TypedDict(
    "DataSetUsageConfigurationTypeDef",
    {
        "DisableUseAsDirectQuerySource": bool,
        "DisableUseAsImportedSource": bool,
    },
    total=False,
)

FieldFolderOutputTypeDef = TypedDict(
    "FieldFolderOutputTypeDef",
    {
        "description": str,
        "columns": List[str],
    },
    total=False,
)

FieldFolderTypeDef = TypedDict(
    "FieldFolderTypeDef",
    {
        "description": str,
        "columns": Sequence[str],
    },
    total=False,
)

_RequiredRowLevelPermissionDataSetTypeDef = TypedDict(
    "_RequiredRowLevelPermissionDataSetTypeDef",
    {
        "Arn": str,
        "PermissionPolicy": RowLevelPermissionPolicyType,
    },
)
_OptionalRowLevelPermissionDataSetTypeDef = TypedDict(
    "_OptionalRowLevelPermissionDataSetTypeDef",
    {
        "Namespace": str,
        "FormatVersion": RowLevelPermissionFormatVersionType,
        "Status": StatusType,
    },
    total=False,
)


class RowLevelPermissionDataSetTypeDef(
    _RequiredRowLevelPermissionDataSetTypeDef, _OptionalRowLevelPermissionDataSetTypeDef
):
    pass


CreateFolderMembershipRequestRequestTypeDef = TypedDict(
    "CreateFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

FolderMemberTypeDef = TypedDict(
    "FolderMemberTypeDef",
    {
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
    total=False,
)

CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

GroupMemberTypeDef = TypedDict(
    "GroupMemberTypeDef",
    {
        "Arn": str,
        "MemberName": str,
    },
    total=False,
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass


GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Arn": str,
        "GroupName": str,
        "Description": str,
        "PrincipalId": str,
    },
    total=False,
)

_RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
        "Namespace": str,
    },
)
_OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Identities": Mapping[str, Sequence[str]],
    },
    total=False,
)


class CreateIAMPolicyAssignmentRequestRequestTypeDef(
    _RequiredCreateIAMPolicyAssignmentRequestRequestTypeDef,
    _OptionalCreateIAMPolicyAssignmentRequestRequestTypeDef,
):
    pass


_RequiredCreateIngestionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIngestionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "IngestionId": str,
        "AwsAccountId": str,
    },
)
_OptionalCreateIngestionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIngestionRequestRequestTypeDef",
    {
        "IngestionType": IngestionTypeType,
    },
    total=False,
)


class CreateIngestionRequestRequestTypeDef(
    _RequiredCreateIngestionRequestRequestTypeDef, _OptionalCreateIngestionRequestRequestTypeDef
):
    pass


CreateTemplateAliasRequestRequestTypeDef = TypedDict(
    "CreateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "TemplateVersionNumber": int,
    },
    total=False,
)

CreateThemeAliasRequestRequestTypeDef = TypedDict(
    "CreateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef",
    {
        "Arn": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
    total=False,
)

_RequiredTopicRefreshScheduleTypeDef = TypedDict(
    "_RequiredTopicRefreshScheduleTypeDef",
    {
        "IsEnabled": bool,
        "BasedOnSpiceSchedule": bool,
    },
)
_OptionalTopicRefreshScheduleTypeDef = TypedDict(
    "_OptionalTopicRefreshScheduleTypeDef",
    {
        "StartingAt": Union[datetime, str],
        "Timezone": str,
        "RepeatAt": str,
        "TopicScheduleType": TopicScheduleTypeType,
    },
    total=False,
)


class TopicRefreshScheduleTypeDef(
    _RequiredTopicRefreshScheduleTypeDef, _OptionalTopicRefreshScheduleTypeDef
):
    pass


DecimalPlacesConfigurationTypeDef = TypedDict(
    "DecimalPlacesConfigurationTypeDef",
    {
        "DecimalPlaces": int,
    },
)

NegativeValueConfigurationTypeDef = TypedDict(
    "NegativeValueConfigurationTypeDef",
    {
        "DisplayMode": NegativeValueDisplayModeType,
    },
)

NullValueFormatConfigurationTypeDef = TypedDict(
    "NullValueFormatConfigurationTypeDef",
    {
        "NullString": str,
    },
)

LocalNavigationConfigurationTypeDef = TypedDict(
    "LocalNavigationConfigurationTypeDef",
    {
        "TargetSheetId": str,
    },
)

CustomActionURLOperationTypeDef = TypedDict(
    "CustomActionURLOperationTypeDef",
    {
        "URLTemplate": str,
        "URLTarget": URLTargetConfigurationType,
    },
)

CustomContentConfigurationTypeDef = TypedDict(
    "CustomContentConfigurationTypeDef",
    {
        "ContentUrl": str,
        "ContentType": CustomContentTypeType,
        "ImageScaling": CustomContentImageScalingConfigurationType,
    },
    total=False,
)

CustomNarrativeOptionsTypeDef = TypedDict(
    "CustomNarrativeOptionsTypeDef",
    {
        "Narrative": str,
    },
)

CustomParameterValuesOutputTypeDef = TypedDict(
    "CustomParameterValuesOutputTypeDef",
    {
        "StringValues": List[str],
        "IntegerValues": List[int],
        "DecimalValues": List[float],
        "DateTimeValues": List[datetime],
    },
    total=False,
)

CustomParameterValuesTypeDef = TypedDict(
    "CustomParameterValuesTypeDef",
    {
        "StringValues": Sequence[str],
        "IntegerValues": Sequence[int],
        "DecimalValues": Sequence[float],
        "DateTimeValues": Sequence[Union[datetime, str]],
    },
    total=False,
)

InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": InputColumnDataTypeType,
    },
)

DataPointDrillUpDownOptionTypeDef = TypedDict(
    "DataPointDrillUpDownOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

DataPointMenuLabelOptionTypeDef = TypedDict(
    "DataPointMenuLabelOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

DataPointTooltipOptionTypeDef = TypedDict(
    "DataPointTooltipOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

ExportWithHiddenFieldsOptionTypeDef = TypedDict(
    "ExportWithHiddenFieldsOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef",
    {
        "VisibilityState": DashboardUIStateType,
    },
    total=False,
)

SheetLayoutElementMaximizationOptionTypeDef = TypedDict(
    "SheetLayoutElementMaximizationOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

VisualAxisSortOptionTypeDef = TypedDict(
    "VisualAxisSortOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

VisualMenuOptionTypeDef = TypedDict(
    "VisualMenuOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

_RequiredDashboardSearchFilterTypeDef = TypedDict(
    "_RequiredDashboardSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
    },
)
_OptionalDashboardSearchFilterTypeDef = TypedDict(
    "_OptionalDashboardSearchFilterTypeDef",
    {
        "Name": DashboardFilterAttributeType,
        "Value": str,
    },
    total=False,
)


class DashboardSearchFilterTypeDef(
    _RequiredDashboardSearchFilterTypeDef, _OptionalDashboardSearchFilterTypeDef
):
    pass


DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "Arn": str,
        "DashboardId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PublishedVersionNumber": int,
        "LastPublishedTime": datetime,
    },
    total=False,
)

DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "SourceEntityArn": str,
        "Description": str,
    },
    total=False,
)

ExportHiddenFieldsOptionTypeDef = TypedDict(
    "ExportHiddenFieldsOptionTypeDef",
    {
        "AvailabilityStatus": DashboardBehaviorType,
    },
    total=False,
)

DataAggregationTypeDef = TypedDict(
    "DataAggregationTypeDef",
    {
        "DatasetRowDateGranularity": TopicTimeGranularityType,
        "DefaultDateColumnName": str,
    },
    total=False,
)

_RequiredDataBarsOptionsTypeDef = TypedDict(
    "_RequiredDataBarsOptionsTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalDataBarsOptionsTypeDef = TypedDict(
    "_OptionalDataBarsOptionsTypeDef",
    {
        "PositiveColor": str,
        "NegativeColor": str,
    },
    total=False,
)


class DataBarsOptionsTypeDef(_RequiredDataBarsOptionsTypeDef, _OptionalDataBarsOptionsTypeDef):
    pass


DataColorPaletteOutputTypeDef = TypedDict(
    "DataColorPaletteOutputTypeDef",
    {
        "Colors": List[str],
        "MinMaxGradient": List[str],
        "EmptyFillColor": str,
    },
    total=False,
)

DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {
        "Colors": Sequence[str],
        "MinMaxGradient": Sequence[str],
        "EmptyFillColor": str,
    },
    total=False,
)

DataPathLabelTypeTypeDef = TypedDict(
    "DataPathLabelTypeTypeDef",
    {
        "FieldId": str,
        "FieldValue": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

FieldLabelTypeTypeDef = TypedDict(
    "FieldLabelTypeTypeDef",
    {
        "FieldId": str,
        "Visibility": VisibilityType,
    },
    total=False,
)

MaximumLabelTypeTypeDef = TypedDict(
    "MaximumLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

MinimumLabelTypeTypeDef = TypedDict(
    "MinimumLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

RangeEndsLabelTypeTypeDef = TypedDict(
    "RangeEndsLabelTypeTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

DataPathValueTypeDef = TypedDict(
    "DataPathValueTypeDef",
    {
        "FieldId": str,
        "FieldValue": str,
    },
)

DataSetSearchFilterTypeDef = TypedDict(
    "DataSetSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSetFilterAttributeType,
        "Value": str,
    },
)

OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ColumnDataTypeType,
    },
    total=False,
)

DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": DataSourceErrorInfoTypeType,
        "Message": str,
    },
    total=False,
)

DatabricksParametersTypeDef = TypedDict(
    "DatabricksParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "SqlEndpointPath": str,
    },
)

ExasolParametersTypeDef = TypedDict(
    "ExasolParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

JiraParametersTypeDef = TypedDict(
    "JiraParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)

RdsParametersTypeDef = TypedDict(
    "RdsParametersTypeDef",
    {
        "InstanceId": str,
        "Database": str,
    },
)

_RequiredRedshiftParametersTypeDef = TypedDict(
    "_RequiredRedshiftParametersTypeDef",
    {
        "Database": str,
    },
)
_OptionalRedshiftParametersTypeDef = TypedDict(
    "_OptionalRedshiftParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "ClusterId": str,
    },
    total=False,
)


class RedshiftParametersTypeDef(
    _RequiredRedshiftParametersTypeDef, _OptionalRedshiftParametersTypeDef
):
    pass


ServiceNowParametersTypeDef = TypedDict(
    "ServiceNowParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)

SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef",
    {
        "Host": str,
        "Database": str,
        "Warehouse": str,
    },
)

SparkParametersTypeDef = TypedDict(
    "SparkParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)

SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)

TwitterParametersTypeDef = TypedDict(
    "TwitterParametersTypeDef",
    {
        "Query": str,
        "MaxRows": int,
    },
)

DataSourceSearchFilterTypeDef = TypedDict(
    "DataSourceSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSourceFilterAttributeType,
        "Value": str,
    },
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DateTimeDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "DateTimeDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": List[datetime],
    },
    total=False,
)

DateTimeDatasetParameterDefaultValuesTypeDef = TypedDict(
    "DateTimeDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": Sequence[Union[datetime, str]],
    },
    total=False,
)

_RequiredRollingDateConfigurationTypeDef = TypedDict(
    "_RequiredRollingDateConfigurationTypeDef",
    {
        "Expression": str,
    },
)
_OptionalRollingDateConfigurationTypeDef = TypedDict(
    "_OptionalRollingDateConfigurationTypeDef",
    {
        "DataSetIdentifier": str,
    },
    total=False,
)


class RollingDateConfigurationTypeDef(
    _RequiredRollingDateConfigurationTypeDef, _OptionalRollingDateConfigurationTypeDef
):
    pass


DateTimeValueWhenUnsetConfigurationOutputTypeDef = TypedDict(
    "DateTimeValueWhenUnsetConfigurationOutputTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": datetime,
    },
    total=False,
)

MappedDataSetParameterTypeDef = TypedDict(
    "MappedDataSetParameterTypeDef",
    {
        "DataSetIdentifier": str,
        "DataSetParameterName": str,
    },
)

DateTimeValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": Union[datetime, str],
    },
    total=False,
)

DateTimeParameterOutputTypeDef = TypedDict(
    "DateTimeParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[datetime],
    },
)

DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[Union[datetime, str]],
    },
)

SheetControlInfoIconLabelOptionsTypeDef = TypedDict(
    "SheetControlInfoIconLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "InfoIconText": str,
    },
    total=False,
)

DecimalDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "DecimalDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": List[float],
    },
    total=False,
)

DecimalDatasetParameterDefaultValuesTypeDef = TypedDict(
    "DecimalDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": Sequence[float],
    },
    total=False,
)

DecimalValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DecimalValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": float,
    },
    total=False,
)

DecimalParameterOutputTypeDef = TypedDict(
    "DecimalParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[float],
    },
)

DecimalParameterTypeDef = TypedDict(
    "DecimalParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[float],
    },
)

_RequiredDeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class DeleteAccountCustomizationRequestRequestTypeDef(
    _RequiredDeleteAccountCustomizationRequestRequestTypeDef,
    _OptionalDeleteAccountCustomizationRequestRequestTypeDef,
):
    pass


DeleteAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

_RequiredDeleteAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalDeleteAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAnalysisRequestRequestTypeDef",
    {
        "RecoveryWindowInDays": int,
        "ForceDeleteWithoutRecovery": bool,
    },
    total=False,
)


class DeleteAnalysisRequestRequestTypeDef(
    _RequiredDeleteAnalysisRequestRequestTypeDef, _OptionalDeleteAnalysisRequestRequestTypeDef
):
    pass


_RequiredDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDeleteDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDashboardRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteDashboardRequestRequestTypeDef(
    _RequiredDeleteDashboardRequestRequestTypeDef, _OptionalDeleteDashboardRequestRequestTypeDef
):
    pass


DeleteDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DeleteFolderMembershipRequestRequestTypeDef = TypedDict(
    "DeleteFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)

DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DeleteRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "ScheduleId": str,
    },
)

DeleteTemplateAliasRequestRequestTypeDef = TypedDict(
    "DeleteTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

_RequiredDeleteTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDeleteTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTemplateRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteTemplateRequestRequestTypeDef(
    _RequiredDeleteTemplateRequestRequestTypeDef, _OptionalDeleteTemplateRequestRequestTypeDef
):
    pass


DeleteThemeAliasRequestRequestTypeDef = TypedDict(
    "DeleteThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

_RequiredDeleteThemeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDeleteThemeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteThemeRequestRequestTypeDef",
    {
        "VersionNumber": int,
    },
    total=False,
)


class DeleteThemeRequestRequestTypeDef(
    _RequiredDeleteThemeRequestRequestTypeDef, _OptionalDeleteThemeRequestRequestTypeDef
):
    pass


DeleteTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DeleteTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
    },
)

DeleteTopicRequestRequestTypeDef = TypedDict(
    "DeleteTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)

DeleteUserByPrincipalIdRequestRequestTypeDef = TypedDict(
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    {
        "PrincipalId": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DeleteVPCConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
    },
)

_RequiredDescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalDescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
        "Resolved": bool,
    },
    total=False,
)


class DescribeAccountCustomizationRequestRequestTypeDef(
    _RequiredDescribeAccountCustomizationRequestRequestTypeDef,
    _OptionalDescribeAccountCustomizationRequestRequestTypeDef,
):
    pass


DescribeAccountSettingsRequestRequestTypeDef = TypedDict(
    "DescribeAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeAnalysisDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

DescribeAssetBundleExportJobRequestRequestTypeDef = TypedDict(
    "DescribeAssetBundleExportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleExportJobId": str,
    },
)

DescribeAssetBundleImportJobRequestRequestTypeDef = TypedDict(
    "DescribeAssetBundleImportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleImportJobId": str,
    },
)

_RequiredDescribeDashboardDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDashboardDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDescribeDashboardDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDashboardDefinitionRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeDashboardDefinitionRequestRequestTypeDef(
    _RequiredDescribeDashboardDefinitionRequestRequestTypeDef,
    _OptionalDescribeDashboardDefinitionRequestRequestTypeDef,
):
    pass


DescribeDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)

_RequiredDescribeDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalDescribeDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDashboardRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeDashboardRequestRequestTypeDef(
    _RequiredDescribeDashboardRequestRequestTypeDef, _OptionalDescribeDashboardRequestRequestTypeDef
):
    pass


DescribeDashboardSnapshotJobRequestRequestTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
    },
)

DescribeDashboardSnapshotJobResultRequestRequestTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResultRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
    },
)

SnapshotJobErrorInfoTypeDef = TypedDict(
    "SnapshotJobErrorInfoTypeDef",
    {
        "ErrorMessage": str,
        "ErrorType": str,
    },
    total=False,
)

DescribeDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSetRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

DescribeDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)

DescribeFolderPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderRequestRequestTypeDef = TypedDict(
    "DescribeFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

DescribeFolderResolvedPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "FolderId": str,
        "Arn": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "FolderPath": List[str],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DescribeGroupMembershipRequestRequestTypeDef = TypedDict(
    "DescribeGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)

IAMPolicyAssignmentTypeDef = TypedDict(
    "IAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentId": str,
        "AssignmentName": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
    },
    total=False,
)

DescribeIngestionRequestRequestTypeDef = TypedDict(
    "DescribeIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)

DescribeIpRestrictionRequestRequestTypeDef = TypedDict(
    "DescribeIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)

DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)

DescribeRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DescribeRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "ScheduleId": str,
    },
)

DescribeTemplateAliasRequestRequestTypeDef = TypedDict(
    "DescribeTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)

_RequiredDescribeTemplateDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTemplateDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDescribeTemplateDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTemplateDefinitionRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeTemplateDefinitionRequestRequestTypeDef(
    _RequiredDescribeTemplateDefinitionRequestRequestTypeDef,
    _OptionalDescribeTemplateDefinitionRequestRequestTypeDef,
):
    pass


DescribeTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)

_RequiredDescribeTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalDescribeTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeTemplateRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeTemplateRequestRequestTypeDef(
    _RequiredDescribeTemplateRequestRequestTypeDef, _OptionalDescribeTemplateRequestRequestTypeDef
):
    pass


DescribeThemeAliasRequestRequestTypeDef = TypedDict(
    "DescribeThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)

DescribeThemePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)

_RequiredDescribeThemeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalDescribeThemeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeThemeRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "AliasName": str,
    },
    total=False,
)


class DescribeThemeRequestRequestTypeDef(
    _RequiredDescribeThemeRequestRequestTypeDef, _OptionalDescribeThemeRequestRequestTypeDef
):
    pass


DescribeTopicPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTopicPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)

DescribeTopicRefreshRequestRequestTypeDef = TypedDict(
    "DescribeTopicRefreshRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "RefreshId": str,
    },
)

TopicRefreshDetailsTypeDef = TypedDict(
    "TopicRefreshDetailsTypeDef",
    {
        "RefreshArn": str,
        "RefreshId": str,
        "RefreshStatus": TopicRefreshStatusType,
    },
    total=False,
)

DescribeTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DescribeTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
    },
)

_RequiredTopicRefreshScheduleOutputTypeDef = TypedDict(
    "_RequiredTopicRefreshScheduleOutputTypeDef",
    {
        "IsEnabled": bool,
        "BasedOnSpiceSchedule": bool,
    },
)
_OptionalTopicRefreshScheduleOutputTypeDef = TypedDict(
    "_OptionalTopicRefreshScheduleOutputTypeDef",
    {
        "StartingAt": datetime,
        "Timezone": str,
        "RepeatAt": str,
        "TopicScheduleType": TopicScheduleTypeType,
    },
    total=False,
)


class TopicRefreshScheduleOutputTypeDef(
    _RequiredTopicRefreshScheduleOutputTypeDef, _OptionalTopicRefreshScheduleOutputTypeDef
):
    pass


DescribeTopicRequestRequestTypeDef = TypedDict(
    "DescribeTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Email": str,
        "Role": UserRoleType,
        "IdentityType": IdentityTypeType,
        "Active": bool,
        "PrincipalId": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "ExternalLoginFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)

DescribeVPCConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
    },
)

NegativeFormatTypeDef = TypedDict(
    "NegativeFormatTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
    },
    total=False,
)

DonutCenterOptionsTypeDef = TypedDict(
    "DonutCenterOptionsTypeDef",
    {
        "LabelVisibility": VisibilityType,
    },
    total=False,
)

ListControlSelectAllOptionsTypeDef = TypedDict(
    "ListControlSelectAllOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": IngestionErrorTypeType,
        "Message": str,
    },
    total=False,
)

_RequiredExcludePeriodConfigurationTypeDef = TypedDict(
    "_RequiredExcludePeriodConfigurationTypeDef",
    {
        "Amount": int,
        "Granularity": TimeGranularityType,
    },
)
_OptionalExcludePeriodConfigurationTypeDef = TypedDict(
    "_OptionalExcludePeriodConfigurationTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)


class ExcludePeriodConfigurationTypeDef(
    _RequiredExcludePeriodConfigurationTypeDef, _OptionalExcludePeriodConfigurationTypeDef
):
    pass


FieldSortTypeDef = TypedDict(
    "FieldSortTypeDef",
    {
        "FieldId": str,
        "Direction": SortDirectionType,
    },
)

_RequiredFieldTooltipItemTypeDef = TypedDict(
    "_RequiredFieldTooltipItemTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalFieldTooltipItemTypeDef = TypedDict(
    "_OptionalFieldTooltipItemTypeDef",
    {
        "Label": str,
        "Visibility": VisibilityType,
    },
    total=False,
)


class FieldTooltipItemTypeDef(_RequiredFieldTooltipItemTypeDef, _OptionalFieldTooltipItemTypeDef):
    pass


GeospatialMapStyleOptionsTypeDef = TypedDict(
    "GeospatialMapStyleOptionsTypeDef",
    {
        "BaseMapStyle": BaseMapStyleTypeType,
    },
    total=False,
)

FilterSelectableValuesOutputTypeDef = TypedDict(
    "FilterSelectableValuesOutputTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

FilterSelectableValuesTypeDef = TypedDict(
    "FilterSelectableValuesTypeDef",
    {
        "Values": Sequence[str],
    },
    total=False,
)

SameSheetTargetVisualConfigurationOutputTypeDef = TypedDict(
    "SameSheetTargetVisualConfigurationOutputTypeDef",
    {
        "TargetVisuals": List[str],
        "TargetVisualOptions": Literal["ALL_VISUALS"],
    },
    total=False,
)

SameSheetTargetVisualConfigurationTypeDef = TypedDict(
    "SameSheetTargetVisualConfigurationTypeDef",
    {
        "TargetVisuals": Sequence[str],
        "TargetVisualOptions": Literal["ALL_VISUALS"],
    },
    total=False,
)

FilterOperationTypeDef = TypedDict(
    "FilterOperationTypeDef",
    {
        "ConditionExpression": str,
    },
)

FolderSearchFilterTypeDef = TypedDict(
    "FolderSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": FolderFilterAttributeType,
        "Value": str,
    },
    total=False,
)

FolderSummaryTypeDef = TypedDict(
    "FolderSummaryTypeDef",
    {
        "Arn": str,
        "FolderId": str,
        "Name": str,
        "FolderType": Literal["SHARED"],
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

FontSizeTypeDef = TypedDict(
    "FontSizeTypeDef",
    {
        "Relative": RelativeFontSizeType,
    },
    total=False,
)

FontWeightTypeDef = TypedDict(
    "FontWeightTypeDef",
    {
        "Name": FontWeightNameType,
    },
    total=False,
)

FontTypeDef = TypedDict(
    "FontTypeDef",
    {
        "FontFamily": str,
    },
    total=False,
)

TimeBasedForecastPropertiesTypeDef = TypedDict(
    "TimeBasedForecastPropertiesTypeDef",
    {
        "PeriodsForward": int,
        "PeriodsBackward": int,
        "UpperBoundary": float,
        "LowerBoundary": float,
        "PredictionInterval": int,
        "Seasonality": int,
    },
    total=False,
)

WhatIfPointScenarioOutputTypeDef = TypedDict(
    "WhatIfPointScenarioOutputTypeDef",
    {
        "Date": datetime,
        "Value": float,
    },
)

WhatIfRangeScenarioOutputTypeDef = TypedDict(
    "WhatIfRangeScenarioOutputTypeDef",
    {
        "StartDate": datetime,
        "EndDate": datetime,
        "Value": float,
    },
)

WhatIfPointScenarioTypeDef = TypedDict(
    "WhatIfPointScenarioTypeDef",
    {
        "Date": Union[datetime, str],
        "Value": float,
    },
)

WhatIfRangeScenarioTypeDef = TypedDict(
    "WhatIfRangeScenarioTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "Value": float,
    },
)

FreeFormLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "OptimizedViewPortWidth": str,
    },
)

FreeFormLayoutElementBackgroundStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "Color": str,
    },
    total=False,
)

FreeFormLayoutElementBorderStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBorderStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "Color": str,
    },
    total=False,
)

LoadingAnimationTypeDef = TypedDict(
    "LoadingAnimationTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

SessionTagTypeDef = TypedDict(
    "SessionTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

GeospatialCoordinateBoundsTypeDef = TypedDict(
    "GeospatialCoordinateBoundsTypeDef",
    {
        "North": float,
        "South": float,
        "West": float,
        "East": float,
    },
)

GeospatialHeatmapDataColorTypeDef = TypedDict(
    "GeospatialHeatmapDataColorTypeDef",
    {
        "Color": str,
    },
)

_RequiredGetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "_RequiredGetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "IdentityType": EmbeddingIdentityTypeType,
    },
)
_OptionalGetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "_OptionalGetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "UndoRedoDisabled": bool,
        "ResetDisabled": bool,
        "StatePersistenceEnabled": bool,
        "UserArn": str,
        "Namespace": str,
        "AdditionalDashboardIds": Sequence[str],
    },
    total=False,
)


class GetDashboardEmbedUrlRequestRequestTypeDef(
    _RequiredGetDashboardEmbedUrlRequestRequestTypeDef,
    _OptionalGetDashboardEmbedUrlRequestRequestTypeDef,
):
    pass


_RequiredGetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "_RequiredGetSessionEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalGetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "_OptionalGetSessionEmbedUrlRequestRequestTypeDef",
    {
        "EntryPoint": str,
        "SessionLifetimeInMinutes": int,
        "UserArn": str,
    },
    total=False,
)


class GetSessionEmbedUrlRequestRequestTypeDef(
    _RequiredGetSessionEmbedUrlRequestRequestTypeDef,
    _OptionalGetSessionEmbedUrlRequestRequestTypeDef,
):
    pass


TableBorderOptionsTypeDef = TypedDict(
    "TableBorderOptionsTypeDef",
    {
        "Color": str,
        "Thickness": int,
        "Style": TableBorderStyleType,
    },
    total=False,
)

_RequiredGradientStopTypeDef = TypedDict(
    "_RequiredGradientStopTypeDef",
    {
        "GradientOffset": float,
    },
)
_OptionalGradientStopTypeDef = TypedDict(
    "_OptionalGradientStopTypeDef",
    {
        "DataValue": float,
        "Color": str,
    },
    total=False,
)


class GradientStopTypeDef(_RequiredGradientStopTypeDef, _OptionalGradientStopTypeDef):
    pass


_RequiredGridLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "_RequiredGridLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "ResizeOption": ResizeOptionType,
    },
)
_OptionalGridLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "_OptionalGridLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "OptimizedViewPortWidth": str,
    },
    total=False,
)


class GridLayoutScreenCanvasSizeOptionsTypeDef(
    _RequiredGridLayoutScreenCanvasSizeOptionsTypeDef,
    _OptionalGridLayoutScreenCanvasSizeOptionsTypeDef,
):
    pass


_RequiredGridLayoutElementTypeDef = TypedDict(
    "_RequiredGridLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "ColumnSpan": int,
        "RowSpan": int,
    },
)
_OptionalGridLayoutElementTypeDef = TypedDict(
    "_OptionalGridLayoutElementTypeDef",
    {
        "ColumnIndex": int,
        "RowIndex": int,
    },
    total=False,
)


class GridLayoutElementTypeDef(
    _RequiredGridLayoutElementTypeDef, _OptionalGridLayoutElementTypeDef
):
    pass


GroupSearchFilterTypeDef = TypedDict(
    "GroupSearchFilterTypeDef",
    {
        "Operator": Literal["StartsWith"],
        "Name": Literal["GROUP_NAME"],
        "Value": str,
    },
)

GutterStyleTypeDef = TypedDict(
    "GutterStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
    },
    total=False,
)

LookbackWindowTypeDef = TypedDict(
    "LookbackWindowTypeDef",
    {
        "ColumnName": str,
        "Size": int,
        "SizeUnit": LookbackWindowSizeUnitType,
    },
)

QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "WaitingOnIngestion": str,
        "QueuedIngestion": str,
    },
)

RowInfoTypeDef = TypedDict(
    "RowInfoTypeDef",
    {
        "RowsIngested": int,
        "RowsDropped": int,
        "TotalRowsInDataset": int,
    },
    total=False,
)

IntegerDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "IntegerDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": List[int],
    },
    total=False,
)

IntegerDatasetParameterDefaultValuesTypeDef = TypedDict(
    "IntegerDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": Sequence[int],
    },
    total=False,
)

IntegerValueWhenUnsetConfigurationTypeDef = TypedDict(
    "IntegerValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": int,
    },
    total=False,
)

IntegerParameterOutputTypeDef = TypedDict(
    "IntegerParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[int],
    },
)

IntegerParameterTypeDef = TypedDict(
    "IntegerParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[int],
    },
)

JoinKeyPropertiesTypeDef = TypedDict(
    "JoinKeyPropertiesTypeDef",
    {
        "UniqueKey": bool,
    },
    total=False,
)

ProgressBarOptionsTypeDef = TypedDict(
    "ProgressBarOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

SecondaryValueOptionsTypeDef = TypedDict(
    "SecondaryValueOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

TrendArrowOptionsTypeDef = TypedDict(
    "TrendArrowOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

LineChartLineStyleSettingsTypeDef = TypedDict(
    "LineChartLineStyleSettingsTypeDef",
    {
        "LineVisibility": VisibilityType,
        "LineInterpolation": LineInterpolationType,
        "LineStyle": LineChartLineStyleType,
        "LineWidth": str,
    },
    total=False,
)

LineChartMarkerStyleSettingsTypeDef = TypedDict(
    "LineChartMarkerStyleSettingsTypeDef",
    {
        "MarkerVisibility": VisibilityType,
        "MarkerShape": LineChartMarkerShapeType,
        "MarkerSize": str,
        "MarkerColor": str,
    },
    total=False,
)

MissingDataConfigurationTypeDef = TypedDict(
    "MissingDataConfigurationTypeDef",
    {
        "TreatmentOption": MissingDataTreatmentOptionType,
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

_RequiredListAnalysesRequestRequestTypeDef = TypedDict(
    "_RequiredListAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAnalysesRequestRequestTypeDef = TypedDict(
    "_OptionalListAnalysesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAnalysesRequestRequestTypeDef(
    _RequiredListAnalysesRequestRequestTypeDef, _OptionalListAnalysesRequestRequestTypeDef
):
    pass


_RequiredListAssetBundleExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetBundleExportJobsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAssetBundleExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetBundleExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAssetBundleExportJobsRequestRequestTypeDef(
    _RequiredListAssetBundleExportJobsRequestRequestTypeDef,
    _OptionalListAssetBundleExportJobsRequestRequestTypeDef,
):
    pass


_RequiredListAssetBundleImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssetBundleImportJobsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAssetBundleImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssetBundleImportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAssetBundleImportJobsRequestRequestTypeDef(
    _RequiredListAssetBundleImportJobsRequestRequestTypeDef,
    _OptionalListAssetBundleImportJobsRequestRequestTypeDef,
):
    pass


ListControlSearchOptionsTypeDef = TypedDict(
    "ListControlSearchOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

_RequiredListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDashboardVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDashboardVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDashboardVersionsRequestRequestTypeDef(
    _RequiredListDashboardVersionsRequestRequestTypeDef,
    _OptionalListDashboardVersionsRequestRequestTypeDef,
):
    pass


_RequiredListDashboardsRequestRequestTypeDef = TypedDict(
    "_RequiredListDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDashboardsRequestRequestTypeDef = TypedDict(
    "_OptionalListDashboardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDashboardsRequestRequestTypeDef(
    _RequiredListDashboardsRequestRequestTypeDef, _OptionalListDashboardsRequestRequestTypeDef
):
    pass


_RequiredListDataSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDataSetsRequestRequestTypeDef(
    _RequiredListDataSetsRequestRequestTypeDef, _OptionalListDataSetsRequestRequestTypeDef
):
    pass


_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
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


_RequiredListFolderMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListFolderMembersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalListFolderMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListFolderMembersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFolderMembersRequestRequestTypeDef(
    _RequiredListFolderMembersRequestRequestTypeDef, _OptionalListFolderMembersRequestRequestTypeDef
):
    pass


MemberIdArnPairTypeDef = TypedDict(
    "MemberIdArnPairTypeDef",
    {
        "MemberId": str,
        "MemberArn": str,
    },
    total=False,
)

_RequiredListFoldersRequestRequestTypeDef = TypedDict(
    "_RequiredListFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListFoldersRequestRequestTypeDef = TypedDict(
    "_OptionalListFoldersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFoldersRequestRequestTypeDef(
    _RequiredListFoldersRequestRequestTypeDef, _OptionalListFoldersRequestRequestTypeDef
):
    pass


_RequiredListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupMembershipsRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupMembershipsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupMembershipsRequestRequestTypeDef(
    _RequiredListGroupMembershipsRequestRequestTypeDef,
    _OptionalListGroupMembershipsRequestRequestTypeDef,
):
    pass


_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass


_RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIAMPolicyAssignmentsForUserRequestRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsForUserRequestRequestTypeDef,
    _OptionalListIAMPolicyAssignmentsForUserRequestRequestTypeDef,
):
    pass


_RequiredListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIAMPolicyAssignmentsRequestRequestTypeDef(
    _RequiredListIAMPolicyAssignmentsRequestRequestTypeDef,
    _OptionalListIAMPolicyAssignmentsRequestRequestTypeDef,
):
    pass


_RequiredListIngestionsRequestRequestTypeDef = TypedDict(
    "_RequiredListIngestionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
    },
)
_OptionalListIngestionsRequestRequestTypeDef = TypedDict(
    "_OptionalListIngestionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIngestionsRequestRequestTypeDef(
    _RequiredListIngestionsRequestRequestTypeDef, _OptionalListIngestionsRequestRequestTypeDef
):
    pass


_RequiredListNamespacesRequestRequestTypeDef = TypedDict(
    "_RequiredListNamespacesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListNamespacesRequestRequestTypeDef = TypedDict(
    "_OptionalListNamespacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListNamespacesRequestRequestTypeDef(
    _RequiredListNamespacesRequestRequestTypeDef, _OptionalListNamespacesRequestRequestTypeDef
):
    pass


ListRefreshSchedulesRequestRequestTypeDef = TypedDict(
    "ListRefreshSchedulesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

_RequiredListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateAliasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplateAliasesRequestRequestTypeDef(
    _RequiredListTemplateAliasesRequestRequestTypeDef,
    _OptionalListTemplateAliasesRequestRequestTypeDef,
):
    pass


_RequiredListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplateVersionsRequestRequestTypeDef(
    _RequiredListTemplateVersionsRequestRequestTypeDef,
    _OptionalListTemplateVersionsRequestRequestTypeDef,
):
    pass


TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": str,
        "VersionNumber": int,
        "CreatedTime": datetime,
        "Status": ResourceStatusType,
        "Description": str,
    },
    total=False,
)

_RequiredListTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplatesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTemplatesRequestRequestTypeDef(
    _RequiredListTemplatesRequestRequestTypeDef, _OptionalListTemplatesRequestRequestTypeDef
):
    pass


TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": str,
        "TemplateId": str,
        "Name": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredListThemeAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemeAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemeAliasesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThemeAliasesRequestRequestTypeDef(
    _RequiredListThemeAliasesRequestRequestTypeDef, _OptionalListThemeAliasesRequestRequestTypeDef
):
    pass


_RequiredListThemeVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListThemeVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListThemeVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListThemeVersionsRequestRequestTypeDef(
    _RequiredListThemeVersionsRequestRequestTypeDef, _OptionalListThemeVersionsRequestRequestTypeDef
):
    pass


ThemeVersionSummaryTypeDef = TypedDict(
    "ThemeVersionSummaryTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "CreatedTime": datetime,
        "Status": ResourceStatusType,
    },
    total=False,
)

_RequiredListThemesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListThemesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Type": ThemeTypeType,
    },
    total=False,
)


class ListThemesRequestRequestTypeDef(
    _RequiredListThemesRequestRequestTypeDef, _OptionalListThemesRequestRequestTypeDef
):
    pass


ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "LatestVersionNumber": int,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

ListTopicRefreshSchedulesRequestRequestTypeDef = TypedDict(
    "ListTopicRefreshSchedulesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)

_RequiredListTopicsRequestRequestTypeDef = TypedDict(
    "_RequiredListTopicsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListTopicsRequestRequestTypeDef = TypedDict(
    "_OptionalListTopicsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTopicsRequestRequestTypeDef(
    _RequiredListTopicsRequestRequestTypeDef, _OptionalListTopicsRequestRequestTypeDef
):
    pass


TopicSummaryTypeDef = TypedDict(
    "TopicSummaryTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "Name": str,
    },
    total=False,
)

_RequiredListUserGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserGroupsRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUserGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUserGroupsRequestRequestTypeDef(
    _RequiredListUserGroupsRequestRequestTypeDef, _OptionalListUserGroupsRequestRequestTypeDef
):
    pass


_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass


_RequiredListVPCConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredListVPCConnectionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListVPCConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalListVPCConnectionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListVPCConnectionsRequestRequestTypeDef(
    _RequiredListVPCConnectionsRequestRequestTypeDef,
    _OptionalListVPCConnectionsRequestRequestTypeDef,
):
    pass


LongFormatTextTypeDef = TypedDict(
    "LongFormatTextTypeDef",
    {
        "PlainText": str,
        "RichText": str,
    },
    total=False,
)

ManifestFileLocationTypeDef = TypedDict(
    "ManifestFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

MarginStyleTypeDef = TypedDict(
    "MarginStyleTypeDef",
    {
        "Show": bool,
    },
    total=False,
)

NamedEntityDefinitionMetricOutputTypeDef = TypedDict(
    "NamedEntityDefinitionMetricOutputTypeDef",
    {
        "Aggregation": NamedEntityAggTypeType,
        "AggregationFunctionParameters": Dict[str, str],
    },
    total=False,
)

NamedEntityDefinitionMetricTypeDef = TypedDict(
    "NamedEntityDefinitionMetricTypeDef",
    {
        "Aggregation": NamedEntityAggTypeType,
        "AggregationFunctionParameters": Mapping[str, str],
    },
    total=False,
)

NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {
        "Type": NamespaceErrorTypeType,
        "Message": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "SubnetId": str,
        "AvailabilityZone": str,
        "ErrorMessage": str,
        "Status": NetworkInterfaceStatusType,
        "NetworkInterfaceId": str,
    },
    total=False,
)

NewDefaultValuesOutputTypeDef = TypedDict(
    "NewDefaultValuesOutputTypeDef",
    {
        "StringStaticValues": List[str],
        "DecimalStaticValues": List[float],
        "DateTimeStaticValues": List[datetime],
        "IntegerStaticValues": List[int],
    },
    total=False,
)

NewDefaultValuesTypeDef = TypedDict(
    "NewDefaultValuesTypeDef",
    {
        "StringStaticValues": Sequence[str],
        "DecimalStaticValues": Sequence[float],
        "DateTimeStaticValues": Sequence[Union[datetime, str]],
        "IntegerStaticValues": Sequence[int],
    },
    total=False,
)

NumericRangeFilterValueTypeDef = TypedDict(
    "NumericRangeFilterValueTypeDef",
    {
        "StaticValue": float,
        "Parameter": str,
    },
    total=False,
)

ThousandSeparatorOptionsTypeDef = TypedDict(
    "ThousandSeparatorOptionsTypeDef",
    {
        "Symbol": NumericSeparatorSymbolType,
        "Visibility": VisibilityType,
    },
    total=False,
)

PercentileAggregationTypeDef = TypedDict(
    "PercentileAggregationTypeDef",
    {
        "PercentileValue": float,
    },
    total=False,
)

StringParameterOutputTypeDef = TypedDict(
    "StringParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

StringParameterTypeDef = TypedDict(
    "StringParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)

PercentVisibleRangeTypeDef = TypedDict(
    "PercentVisibleRangeTypeDef",
    {
        "From": float,
        "To": float,
    },
    total=False,
)

PivotTableConditionalFormattingScopeTypeDef = TypedDict(
    "PivotTableConditionalFormattingScopeTypeDef",
    {
        "Role": PivotTableConditionalFormattingScopeRoleType,
    },
    total=False,
)

PivotTablePaginatedReportOptionsTypeDef = TypedDict(
    "PivotTablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": VisibilityType,
        "OverflowColumnHeaderVisibility": VisibilityType,
    },
    total=False,
)

_RequiredPivotTableFieldOptionTypeDef = TypedDict(
    "_RequiredPivotTableFieldOptionTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalPivotTableFieldOptionTypeDef = TypedDict(
    "_OptionalPivotTableFieldOptionTypeDef",
    {
        "CustomLabel": str,
        "Visibility": VisibilityType,
    },
    total=False,
)


class PivotTableFieldOptionTypeDef(
    _RequiredPivotTableFieldOptionTypeDef, _OptionalPivotTableFieldOptionTypeDef
):
    pass


PivotTableFieldSubtotalOptionsTypeDef = TypedDict(
    "PivotTableFieldSubtotalOptionsTypeDef",
    {
        "FieldId": str,
    },
    total=False,
)

RowAlternateColorOptionsOutputTypeDef = TypedDict(
    "RowAlternateColorOptionsOutputTypeDef",
    {
        "Status": WidgetStatusType,
        "RowAlternateColors": List[str],
    },
    total=False,
)

RowAlternateColorOptionsTypeDef = TypedDict(
    "RowAlternateColorOptionsTypeDef",
    {
        "Status": WidgetStatusType,
        "RowAlternateColors": Sequence[str],
    },
    total=False,
)

ProjectOperationOutputTypeDef = TypedDict(
    "ProjectOperationOutputTypeDef",
    {
        "ProjectedColumns": List[str],
    },
)

ProjectOperationTypeDef = TypedDict(
    "ProjectOperationTypeDef",
    {
        "ProjectedColumns": Sequence[str],
    },
)

RadarChartAreaStyleSettingsTypeDef = TypedDict(
    "RadarChartAreaStyleSettingsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

RangeConstantTypeDef = TypedDict(
    "RangeConstantTypeDef",
    {
        "Minimum": str,
        "Maximum": str,
    },
    total=False,
)

ReferenceLineCustomLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineCustomLabelConfigurationTypeDef",
    {
        "CustomLabel": str,
    },
)

ReferenceLineStaticDataConfigurationTypeDef = TypedDict(
    "ReferenceLineStaticDataConfigurationTypeDef",
    {
        "Value": float,
    },
)

ReferenceLineStyleConfigurationTypeDef = TypedDict(
    "ReferenceLineStyleConfigurationTypeDef",
    {
        "Pattern": ReferenceLinePatternTypeType,
        "Color": str,
    },
    total=False,
)

ScheduleRefreshOnEntityTypeDef = TypedDict(
    "ScheduleRefreshOnEntityTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "DayOfMonth": str,
    },
    total=False,
)

_RequiredRegisterUserRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterUserRequestRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "Email": str,
        "UserRole": UserRoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalRegisterUserRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterUserRequestRequestTypeDef",
    {
        "IamArn": str,
        "SessionName": str,
        "UserName": str,
        "CustomPermissionsName": str,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)


class RegisterUserRequestRequestTypeDef(
    _RequiredRegisterUserRequestRequestTypeDef, _OptionalRegisterUserRequestRequestTypeDef
):
    pass


StatePersistenceConfigurationsTypeDef = TypedDict(
    "StatePersistenceConfigurationsTypeDef",
    {
        "Enabled": bool,
    },
)

RegisteredUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
    total=False,
)

RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnName": str,
    },
)

RestoreAnalysisRequestRequestTypeDef = TypedDict(
    "RestoreAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)

_RequiredRowLevelPermissionTagRuleTypeDef = TypedDict(
    "_RequiredRowLevelPermissionTagRuleTypeDef",
    {
        "TagKey": str,
        "ColumnName": str,
    },
)
_OptionalRowLevelPermissionTagRuleTypeDef = TypedDict(
    "_OptionalRowLevelPermissionTagRuleTypeDef",
    {
        "TagMultiValueDelimiter": str,
        "MatchAllValue": str,
    },
    total=False,
)


class RowLevelPermissionTagRuleTypeDef(
    _RequiredRowLevelPermissionTagRuleTypeDef, _OptionalRowLevelPermissionTagRuleTypeDef
):
    pass


S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
        "BucketRegion": str,
    },
)

UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": FileFormatType,
        "StartFromRow": int,
        "ContainsHeader": bool,
        "TextQualifier": TextQualifierType,
        "Delimiter": str,
    },
    total=False,
)

SectionAfterPageBreakTypeDef = TypedDict(
    "SectionAfterPageBreakTypeDef",
    {
        "Status": SectionPageBreakStatusType,
    },
    total=False,
)

SpacingTypeDef = TypedDict(
    "SpacingTypeDef",
    {
        "Top": str,
        "Bottom": str,
        "Left": str,
        "Right": str,
    },
    total=False,
)

_RequiredSheetVisualScopingConfigurationOutputTypeDef = TypedDict(
    "_RequiredSheetVisualScopingConfigurationOutputTypeDef",
    {
        "SheetId": str,
        "Scope": FilterVisualScopeType,
    },
)
_OptionalSheetVisualScopingConfigurationOutputTypeDef = TypedDict(
    "_OptionalSheetVisualScopingConfigurationOutputTypeDef",
    {
        "VisualIds": List[str],
    },
    total=False,
)


class SheetVisualScopingConfigurationOutputTypeDef(
    _RequiredSheetVisualScopingConfigurationOutputTypeDef,
    _OptionalSheetVisualScopingConfigurationOutputTypeDef,
):
    pass


_RequiredSheetVisualScopingConfigurationTypeDef = TypedDict(
    "_RequiredSheetVisualScopingConfigurationTypeDef",
    {
        "SheetId": str,
        "Scope": FilterVisualScopeType,
    },
)
_OptionalSheetVisualScopingConfigurationTypeDef = TypedDict(
    "_OptionalSheetVisualScopingConfigurationTypeDef",
    {
        "VisualIds": Sequence[str],
    },
    total=False,
)


class SheetVisualScopingConfigurationTypeDef(
    _RequiredSheetVisualScopingConfigurationTypeDef, _OptionalSheetVisualScopingConfigurationTypeDef
):
    pass


SemanticEntityTypeOutputTypeDef = TypedDict(
    "SemanticEntityTypeOutputTypeDef",
    {
        "TypeName": str,
        "SubTypeName": str,
        "TypeParameters": Dict[str, str],
    },
    total=False,
)

SemanticEntityTypeTypeDef = TypedDict(
    "SemanticEntityTypeTypeDef",
    {
        "TypeName": str,
        "SubTypeName": str,
        "TypeParameters": Mapping[str, str],
    },
    total=False,
)

SemanticTypeOutputTypeDef = TypedDict(
    "SemanticTypeOutputTypeDef",
    {
        "TypeName": str,
        "SubTypeName": str,
        "TypeParameters": Dict[str, str],
        "TruthyCellValue": str,
        "TruthyCellValueSynonyms": List[str],
        "FalseyCellValue": str,
        "FalseyCellValueSynonyms": List[str],
    },
    total=False,
)

SemanticTypeTypeDef = TypedDict(
    "SemanticTypeTypeDef",
    {
        "TypeName": str,
        "SubTypeName": str,
        "TypeParameters": Mapping[str, str],
        "TruthyCellValue": str,
        "TruthyCellValueSynonyms": Sequence[str],
        "FalseyCellValue": str,
        "FalseyCellValueSynonyms": Sequence[str],
    },
    total=False,
)

_RequiredSheetTextBoxTypeDef = TypedDict(
    "_RequiredSheetTextBoxTypeDef",
    {
        "SheetTextBoxId": str,
    },
)
_OptionalSheetTextBoxTypeDef = TypedDict(
    "_OptionalSheetTextBoxTypeDef",
    {
        "Content": str,
    },
    total=False,
)


class SheetTextBoxTypeDef(_RequiredSheetTextBoxTypeDef, _OptionalSheetTextBoxTypeDef):
    pass


SheetElementConfigurationOverridesTypeDef = TypedDict(
    "SheetElementConfigurationOverridesTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

ShortFormatTextTypeDef = TypedDict(
    "ShortFormatTextTypeDef",
    {
        "PlainText": str,
        "RichText": str,
    },
    total=False,
)

SmallMultiplesAxisPropertiesTypeDef = TypedDict(
    "SmallMultiplesAxisPropertiesTypeDef",
    {
        "Scale": SmallMultiplesAxisScaleType,
        "Placement": SmallMultiplesAxisPlacementType,
    },
    total=False,
)

SnapshotAnonymousUserRedactedTypeDef = TypedDict(
    "SnapshotAnonymousUserRedactedTypeDef",
    {
        "RowLevelPermissionTagKeys": List[str],
    },
    total=False,
)

_RequiredSnapshotFileSheetSelectionOutputTypeDef = TypedDict(
    "_RequiredSnapshotFileSheetSelectionOutputTypeDef",
    {
        "SheetId": str,
        "SelectionScope": SnapshotFileSheetSelectionScopeType,
    },
)
_OptionalSnapshotFileSheetSelectionOutputTypeDef = TypedDict(
    "_OptionalSnapshotFileSheetSelectionOutputTypeDef",
    {
        "VisualIds": List[str],
    },
    total=False,
)


class SnapshotFileSheetSelectionOutputTypeDef(
    _RequiredSnapshotFileSheetSelectionOutputTypeDef,
    _OptionalSnapshotFileSheetSelectionOutputTypeDef,
):
    pass


_RequiredSnapshotFileSheetSelectionTypeDef = TypedDict(
    "_RequiredSnapshotFileSheetSelectionTypeDef",
    {
        "SheetId": str,
        "SelectionScope": SnapshotFileSheetSelectionScopeType,
    },
)
_OptionalSnapshotFileSheetSelectionTypeDef = TypedDict(
    "_OptionalSnapshotFileSheetSelectionTypeDef",
    {
        "VisualIds": Sequence[str],
    },
    total=False,
)


class SnapshotFileSheetSelectionTypeDef(
    _RequiredSnapshotFileSheetSelectionTypeDef, _OptionalSnapshotFileSheetSelectionTypeDef
):
    pass


SnapshotJobResultErrorInfoTypeDef = TypedDict(
    "SnapshotJobResultErrorInfoTypeDef",
    {
        "ErrorMessage": str,
        "ErrorType": str,
    },
    total=False,
)

StringDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "StringDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": List[str],
    },
    total=False,
)

StringDatasetParameterDefaultValuesTypeDef = TypedDict(
    "StringDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": Sequence[str],
    },
    total=False,
)

StringValueWhenUnsetConfigurationTypeDef = TypedDict(
    "StringValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": ValueWhenUnsetOptionType,
        "CustomValue": str,
    },
    total=False,
)

TableCellImageSizingConfigurationTypeDef = TypedDict(
    "TableCellImageSizingConfigurationTypeDef",
    {
        "TableCellImageScalingConfiguration": TableCellImageScalingConfigurationType,
    },
    total=False,
)

TablePaginatedReportOptionsTypeDef = TypedDict(
    "TablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": VisibilityType,
        "OverflowColumnHeaderVisibility": VisibilityType,
    },
    total=False,
)

TableFieldCustomIconContentTypeDef = TypedDict(
    "TableFieldCustomIconContentTypeDef",
    {
        "Icon": Literal["LINK"],
    },
    total=False,
)

TemplateSourceTemplateTypeDef = TypedDict(
    "TemplateSourceTemplateTypeDef",
    {
        "Arn": str,
    },
)

TextControlPlaceholderOptionsTypeDef = TypedDict(
    "TextControlPlaceholderOptionsTypeDef",
    {
        "Visibility": VisibilityType,
    },
    total=False,
)

UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": str,
        "PrimaryBackground": str,
        "SecondaryForeground": str,
        "SecondaryBackground": str,
        "Accent": str,
        "AccentForeground": str,
        "Danger": str,
        "DangerForeground": str,
        "Warning": str,
        "WarningForeground": str,
        "Success": str,
        "SuccessForeground": str,
        "Dimension": str,
        "DimensionForeground": str,
        "Measure": str,
        "MeasureForeground": str,
    },
    total=False,
)

ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef",
    {
        "Type": Literal["INTERNAL_FAILURE"],
        "Message": str,
    },
    total=False,
)

TopicSingularFilterConstantTypeDef = TypedDict(
    "TopicSingularFilterConstantTypeDef",
    {
        "ConstantType": ConstantTypeType,
        "SingularConstant": str,
    },
    total=False,
)

UntagColumnOperationOutputTypeDef = TypedDict(
    "UntagColumnOperationOutputTypeDef",
    {
        "ColumnName": str,
        "TagNames": List[ColumnTagNameType],
    },
)

UntagColumnOperationTypeDef = TypedDict(
    "UntagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "TagNames": Sequence[ColumnTagNameType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredUpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultNamespace": str,
    },
)
_OptionalUpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountSettingsRequestRequestTypeDef",
    {
        "NotificationEmail": str,
        "TerminationProtectionEnabled": bool,
    },
    total=False,
)


class UpdateAccountSettingsRequestRequestTypeDef(
    _RequiredUpdateAccountSettingsRequestRequestTypeDef,
    _OptionalUpdateAccountSettingsRequestRequestTypeDef,
):
    pass


UpdateDashboardPublishedVersionRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": int,
    },
)

UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": str,
    },
)

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass


_RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)
_OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Mapping[str, Sequence[str]],
    },
    total=False,
)


class UpdateIAMPolicyAssignmentRequestRequestTypeDef(
    _RequiredUpdateIAMPolicyAssignmentRequestRequestTypeDef,
    _OptionalUpdateIAMPolicyAssignmentRequestRequestTypeDef,
):
    pass


_RequiredUpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalUpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIpRestrictionRequestRequestTypeDef",
    {
        "IpRestrictionRuleMap": Mapping[str, str],
        "Enabled": bool,
    },
    total=False,
)


class UpdateIpRestrictionRequestRequestTypeDef(
    _RequiredUpdateIpRestrictionRequestRequestTypeDef,
    _OptionalUpdateIpRestrictionRequestRequestTypeDef,
):
    pass


_RequiredUpdatePublicSharingSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePublicSharingSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalUpdatePublicSharingSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePublicSharingSettingsRequestRequestTypeDef",
    {
        "PublicSharingEnabled": bool,
    },
    total=False,
)


class UpdatePublicSharingSettingsRequestRequestTypeDef(
    _RequiredUpdatePublicSharingSettingsRequestRequestTypeDef,
    _OptionalUpdatePublicSharingSettingsRequestRequestTypeDef,
):
    pass


UpdateTemplateAliasRequestRequestTypeDef = TypedDict(
    "UpdateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)

UpdateThemeAliasRequestRequestTypeDef = TypedDict(
    "UpdateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Email": str,
        "Role": UserRoleType,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "CustomPermissionsName": str,
        "UnapplyCustomPermissions": bool,
        "ExternalLoginFederationProviderType": str,
        "CustomFederationProviderUrl": str,
        "ExternalLoginId": str,
    },
    total=False,
)


class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass


_RequiredUpdateVPCConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "RoleArn": str,
    },
)
_OptionalUpdateVPCConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVPCConnectionRequestRequestTypeDef",
    {
        "DnsResolvers": Sequence[str],
    },
    total=False,
)


class UpdateVPCConnectionRequestRequestTypeDef(
    _RequiredUpdateVPCConnectionRequestRequestTypeDef,
    _OptionalUpdateVPCConnectionRequestRequestTypeDef,
):
    pass


WaterfallChartOptionsTypeDef = TypedDict(
    "WaterfallChartOptionsTypeDef",
    {
        "TotalBarLabel": str,
    },
    total=False,
)

WordCloudOptionsTypeDef = TypedDict(
    "WordCloudOptionsTypeDef",
    {
        "WordOrientation": WordCloudWordOrientationType,
        "WordScaling": WordCloudWordScalingType,
        "CloudLayout": WordCloudCloudLayoutType,
        "WordCasing": WordCloudWordCasingType,
        "WordPadding": WordCloudWordPaddingType,
        "MaximumStringLength": int,
    },
    total=False,
)

_RequiredUpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": AccountCustomizationTypeDef,
    },
)
_OptionalUpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class UpdateAccountCustomizationRequestRequestTypeDef(
    _RequiredUpdateAccountCustomizationRequestRequestTypeDef,
    _OptionalUpdateAccountCustomizationRequestRequestTypeDef,
):
    pass


AxisLabelReferenceOptionsTypeDef = TypedDict(
    "AxisLabelReferenceOptionsTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)

CascadingControlSourceTypeDef = TypedDict(
    "CascadingControlSourceTypeDef",
    {
        "SourceSheetControlId": str,
        "ColumnToMatch": ColumnIdentifierTypeDef,
    },
    total=False,
)

CategoryDrillDownFilterOutputTypeDef = TypedDict(
    "CategoryDrillDownFilterOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "CategoryValues": List[str],
    },
)

CategoryDrillDownFilterTypeDef = TypedDict(
    "CategoryDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "CategoryValues": Sequence[str],
    },
)

ContributionAnalysisDefaultOutputTypeDef = TypedDict(
    "ContributionAnalysisDefaultOutputTypeDef",
    {
        "MeasureFieldId": str,
        "ContributorDimensions": List[ColumnIdentifierTypeDef],
    },
)

ContributionAnalysisDefaultTypeDef = TypedDict(
    "ContributionAnalysisDefaultTypeDef",
    {
        "MeasureFieldId": str,
        "ContributorDimensions": Sequence[ColumnIdentifierTypeDef],
    },
)

_RequiredDynamicDefaultValueTypeDef = TypedDict(
    "_RequiredDynamicDefaultValueTypeDef",
    {
        "DefaultValueColumn": ColumnIdentifierTypeDef,
    },
)
_OptionalDynamicDefaultValueTypeDef = TypedDict(
    "_OptionalDynamicDefaultValueTypeDef",
    {
        "UserNameColumn": ColumnIdentifierTypeDef,
        "GroupNameColumn": ColumnIdentifierTypeDef,
    },
    total=False,
)


class DynamicDefaultValueTypeDef(
    _RequiredDynamicDefaultValueTypeDef, _OptionalDynamicDefaultValueTypeDef
):
    pass


FilterOperationSelectedFieldsConfigurationOutputTypeDef = TypedDict(
    "FilterOperationSelectedFieldsConfigurationOutputTypeDef",
    {
        "SelectedFields": List[str],
        "SelectedFieldOptions": Literal["ALL_FIELDS"],
        "SelectedColumns": List[ColumnIdentifierTypeDef],
    },
    total=False,
)

FilterOperationSelectedFieldsConfigurationTypeDef = TypedDict(
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    {
        "SelectedFields": Sequence[str],
        "SelectedFieldOptions": Literal["ALL_FIELDS"],
        "SelectedColumns": Sequence[ColumnIdentifierTypeDef],
    },
    total=False,
)

NumericEqualityDrillDownFilterTypeDef = TypedDict(
    "NumericEqualityDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Value": float,
    },
)

ParameterSelectableValuesOutputTypeDef = TypedDict(
    "ParameterSelectableValuesOutputTypeDef",
    {
        "Values": List[str],
        "LinkToDataSetColumn": ColumnIdentifierTypeDef,
    },
    total=False,
)

ParameterSelectableValuesTypeDef = TypedDict(
    "ParameterSelectableValuesTypeDef",
    {
        "Values": Sequence[str],
        "LinkToDataSetColumn": ColumnIdentifierTypeDef,
    },
    total=False,
)

_RequiredTimeEqualityFilterOutputTypeDef = TypedDict(
    "_RequiredTimeEqualityFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalTimeEqualityFilterOutputTypeDef = TypedDict(
    "_OptionalTimeEqualityFilterOutputTypeDef",
    {
        "Value": datetime,
        "ParameterName": str,
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)


class TimeEqualityFilterOutputTypeDef(
    _RequiredTimeEqualityFilterOutputTypeDef, _OptionalTimeEqualityFilterOutputTypeDef
):
    pass


_RequiredTimeEqualityFilterTypeDef = TypedDict(
    "_RequiredTimeEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalTimeEqualityFilterTypeDef = TypedDict(
    "_OptionalTimeEqualityFilterTypeDef",
    {
        "Value": Union[datetime, str],
        "ParameterName": str,
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)


class TimeEqualityFilterTypeDef(
    _RequiredTimeEqualityFilterTypeDef, _OptionalTimeEqualityFilterTypeDef
):
    pass


TimeRangeDrillDownFilterOutputTypeDef = TypedDict(
    "TimeRangeDrillDownFilterOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "RangeMinimum": datetime,
        "RangeMaximum": datetime,
        "TimeGranularity": TimeGranularityType,
    },
)

TimeRangeDrillDownFilterTypeDef = TypedDict(
    "TimeRangeDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "RangeMinimum": Union[datetime, str],
        "RangeMaximum": Union[datetime, str],
        "TimeGranularity": TimeGranularityType,
    },
)

AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": AnalysisErrorTypeType,
        "Message": str,
        "ViolatedEntities": List[EntityTypeDef],
    },
    total=False,
)

DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": DashboardErrorTypeType,
        "Message": str,
        "ViolatedEntities": List[EntityTypeDef],
    },
    total=False,
)

TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": TemplateErrorTypeType,
        "Message": str,
        "ViolatedEntities": List[EntityTypeDef],
    },
    total=False,
)

_RequiredSearchAnalysesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[AnalysisSearchFilterTypeDef],
    },
)
_OptionalSearchAnalysesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchAnalysesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchAnalysesRequestRequestTypeDef(
    _RequiredSearchAnalysesRequestRequestTypeDef, _OptionalSearchAnalysesRequestRequestTypeDef
):
    pass


AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
        "Arn": str,
    },
)

DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
        "Arn": str,
    },
)

TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {
        "Arn": str,
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
    },
)

AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": DashboardVisualIdTypeDef,
    },
)

RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": DashboardVisualIdTypeDef,
    },
)

ArcAxisConfigurationTypeDef = TypedDict(
    "ArcAxisConfigurationTypeDef",
    {
        "Range": ArcAxisDisplayRangeTypeDef,
        "ReserveRange": int,
    },
    total=False,
)

AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef = TypedDict(
    "AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef",
    {
        "ResourceIdOverrideConfiguration": (
            AssetBundleExportJobResourceIdOverrideConfigurationTypeDef
        ),
        "VPCConnections": List[AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef],
        "RefreshSchedules": List[
            AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef
        ],
        "DataSources": List[AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef],
        "DataSets": List[AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef],
        "Themes": List[AssetBundleExportJobThemeOverridePropertiesOutputTypeDef],
        "Analyses": List[AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef],
        "Dashboards": List[AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef],
    },
    total=False,
)

AssetBundleCloudFormationOverridePropertyConfigurationTypeDef = TypedDict(
    "AssetBundleCloudFormationOverridePropertyConfigurationTypeDef",
    {
        "ResourceIdOverrideConfiguration": (
            AssetBundleExportJobResourceIdOverrideConfigurationTypeDef
        ),
        "VPCConnections": Sequence[AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef],
        "RefreshSchedules": Sequence[AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef],
        "DataSources": Sequence[AssetBundleExportJobDataSourceOverridePropertiesTypeDef],
        "DataSets": Sequence[AssetBundleExportJobDataSetOverridePropertiesTypeDef],
        "Themes": Sequence[AssetBundleExportJobThemeOverridePropertiesTypeDef],
        "Analyses": Sequence[AssetBundleExportJobAnalysisOverridePropertiesTypeDef],
        "Dashboards": Sequence[AssetBundleExportJobDashboardOverridePropertiesTypeDef],
    },
    total=False,
)

AssetBundleImportJobDataSourceCredentialsTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceCredentialsTypeDef",
    {
        "CredentialPair": AssetBundleImportJobDataSourceCredentialPairTypeDef,
        "SecretArn": str,
    },
    total=False,
)

AxisDisplayRangeOutputTypeDef = TypedDict(
    "AxisDisplayRangeOutputTypeDef",
    {
        "MinMax": AxisDisplayMinMaxRangeTypeDef,
        "DataDriven": Dict[str, Any],
    },
    total=False,
)

AxisDisplayRangeTypeDef = TypedDict(
    "AxisDisplayRangeTypeDef",
    {
        "MinMax": AxisDisplayMinMaxRangeTypeDef,
        "DataDriven": Mapping[str, Any],
    },
    total=False,
)

AxisScaleTypeDef = TypedDict(
    "AxisScaleTypeDef",
    {
        "Linear": AxisLinearScaleTypeDef,
        "Logarithmic": AxisLogarithmicScaleTypeDef,
    },
    total=False,
)

HistogramBinOptionsTypeDef = TypedDict(
    "HistogramBinOptionsTypeDef",
    {
        "SelectedBinType": HistogramBinTypeType,
        "BinCount": BinCountOptionsTypeDef,
        "BinWidth": BinWidthOptionsTypeDef,
        "StartValue": float,
    },
    total=False,
)

TileStyleTypeDef = TypedDict(
    "TileStyleTypeDef",
    {
        "Border": BorderStyleTypeDef,
    },
    total=False,
)

BoxPlotOptionsTypeDef = TypedDict(
    "BoxPlotOptionsTypeDef",
    {
        "StyleOptions": BoxPlotStyleOptionsTypeDef,
        "OutlierVisibility": VisibilityType,
        "AllDataPointsVisibility": VisibilityType,
    },
    total=False,
)

CreateColumnsOperationOutputTypeDef = TypedDict(
    "CreateColumnsOperationOutputTypeDef",
    {
        "Columns": List[CalculatedColumnTypeDef],
    },
)

CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef",
    {
        "Columns": Sequence[CalculatedColumnTypeDef],
    },
)

CancelIngestionResponseTypeDef = TypedDict(
    "CancelIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAccountCustomizationResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAnalysisResponseTypeDef = TypedDict(
    "CreateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": IngestionStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRefreshScheduleResponseTypeDef = TypedDict(
    "CreateRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTopicRefreshScheduleResponseTypeDef = TypedDict(
    "CreateTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTopicResponseTypeDef = TypedDict(
    "CreateTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "RefreshArn": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateVPCConnectionResponseTypeDef = TypedDict(
    "CreateVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "CreationStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteAccountCustomizationResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteAccountSubscriptionResponseTypeDef = TypedDict(
    "DeleteAccountSubscriptionResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteAnalysisResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "DeletionTime": datetime,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDashboardResponseTypeDef = TypedDict(
    "DeleteDashboardResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "DashboardId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "DeleteDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDataSetResponseTypeDef = TypedDict(
    "DeleteDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteFolderMembershipResponseTypeDef = TypedDict(
    "DeleteFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteFolderResponseTypeDef = TypedDict(
    "DeleteFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteGroupMembershipResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteGroupResponseTypeDef = TypedDict(
    "DeleteGroupResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteRefreshScheduleResponseTypeDef = TypedDict(
    "DeleteRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTemplateAliasResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseTypeDef",
    {
        "Status": int,
        "TemplateId": str,
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTemplateResponseTypeDef = TypedDict(
    "DeleteTemplateResponseTypeDef",
    {
        "RequestId": str,
        "Arn": str,
        "TemplateId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteThemeAliasResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteThemeResponseTypeDef = TypedDict(
    "DeleteThemeResponseTypeDef",
    {
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTopicRefreshScheduleResponseTypeDef = TypedDict(
    "DeleteTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteTopicResponseTypeDef = TypedDict(
    "DeleteTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteVPCConnectionResponseTypeDef = TypedDict(
    "DeleteVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "DeletionStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAccountCustomizationResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {
        "AccountSettings": AccountSettingsTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAccountSubscriptionResponseTypeDef = TypedDict(
    "DescribeAccountSubscriptionResponseTypeDef",
    {
        "AccountInfo": AccountInfoTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeIpRestrictionResponseTypeDef = TypedDict(
    "DescribeIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": Dict[str, str],
        "Enabled": bool,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GenerateEmbedUrlForAnonymousUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "AnonymousUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GenerateEmbedUrlForRegisteredUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetSessionEmbedUrlResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAnalysesResponseTypeDef = TypedDict(
    "ListAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List[AnalysisSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAssetBundleExportJobsResponseTypeDef = TypedDict(
    "ListAssetBundleExportJobsResponseTypeDef",
    {
        "AssetBundleExportJobSummaryList": List[AssetBundleExportJobSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAssetBundleImportJobsResponseTypeDef = TypedDict(
    "ListAssetBundleImportJobsResponseTypeDef",
    {
        "AssetBundleImportJobSummaryList": List[AssetBundleImportJobSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIAMPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List[ActiveIAMPolicyAssignmentTypeDef],
        "RequestId": str,
        "NextToken": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "PutDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RestoreAnalysisResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchAnalysesResponseTypeDef = TypedDict(
    "SearchAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List[AnalysisSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartAssetBundleExportJobResponseTypeDef = TypedDict(
    "StartAssetBundleExportJobResponseTypeDef",
    {
        "Arn": str,
        "AssetBundleExportJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartAssetBundleImportJobResponseTypeDef = TypedDict(
    "StartAssetBundleImportJobResponseTypeDef",
    {
        "Arn": str,
        "AssetBundleImportJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDashboardSnapshotJobResponseTypeDef = TypedDict(
    "StartDashboardSnapshotJobResponseTypeDef",
    {
        "Arn": str,
        "SnapshotJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAccountCustomizationResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateAnalysisResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFolderResponseTypeDef = TypedDict(
    "UpdateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateIpRestrictionResponseTypeDef = TypedDict(
    "UpdateIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdatePublicSharingSettingsResponseTypeDef = TypedDict(
    "UpdatePublicSharingSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateRefreshScheduleResponseTypeDef = TypedDict(
    "UpdateRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTemplateResponseTypeDef = TypedDict(
    "UpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTopicRefreshScheduleResponseTypeDef = TypedDict(
    "UpdateTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTopicResponseTypeDef = TypedDict(
    "UpdateTopicResponseTypeDef",
    {
        "TopicId": str,
        "Arn": str,
        "RefreshArn": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateVPCConnectionResponseTypeDef = TypedDict(
    "UpdateVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "UpdateStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CategoryFilterConfigurationOutputTypeDef = TypedDict(
    "CategoryFilterConfigurationOutputTypeDef",
    {
        "FilterListConfiguration": FilterListConfigurationOutputTypeDef,
        "CustomFilterListConfiguration": CustomFilterListConfigurationOutputTypeDef,
        "CustomFilterConfiguration": CustomFilterConfigurationTypeDef,
    },
    total=False,
)

CategoryFilterConfigurationTypeDef = TypedDict(
    "CategoryFilterConfigurationTypeDef",
    {
        "FilterListConfiguration": FilterListConfigurationTypeDef,
        "CustomFilterListConfiguration": CustomFilterListConfigurationTypeDef,
        "CustomFilterConfiguration": CustomFilterConfigurationTypeDef,
    },
    total=False,
)

ClusterMarkerTypeDef = TypedDict(
    "ClusterMarkerTypeDef",
    {
        "SimpleClusterMarker": SimpleClusterMarkerTypeDef,
    },
    total=False,
)

TopicCategoryFilterConstantOutputTypeDef = TypedDict(
    "TopicCategoryFilterConstantOutputTypeDef",
    {
        "ConstantType": ConstantTypeType,
        "SingularConstant": str,
        "CollectiveConstant": CollectiveConstantOutputTypeDef,
    },
    total=False,
)

TopicCategoryFilterConstantTypeDef = TypedDict(
    "TopicCategoryFilterConstantTypeDef",
    {
        "ConstantType": ConstantTypeType,
        "SingularConstant": str,
        "CollectiveConstant": CollectiveConstantTypeDef,
    },
    total=False,
)

_RequiredColorScaleOutputTypeDef = TypedDict(
    "_RequiredColorScaleOutputTypeDef",
    {
        "Colors": List[DataColorTypeDef],
        "ColorFillType": ColorFillTypeType,
    },
)
_OptionalColorScaleOutputTypeDef = TypedDict(
    "_OptionalColorScaleOutputTypeDef",
    {
        "NullValueColor": DataColorTypeDef,
    },
    total=False,
)


class ColorScaleOutputTypeDef(_RequiredColorScaleOutputTypeDef, _OptionalColorScaleOutputTypeDef):
    pass


_RequiredColorScaleTypeDef = TypedDict(
    "_RequiredColorScaleTypeDef",
    {
        "Colors": Sequence[DataColorTypeDef],
        "ColorFillType": ColorFillTypeType,
    },
)
_OptionalColorScaleTypeDef = TypedDict(
    "_OptionalColorScaleTypeDef",
    {
        "NullValueColor": DataColorTypeDef,
    },
    total=False,
)


class ColorScaleTypeDef(_RequiredColorScaleTypeDef, _OptionalColorScaleTypeDef):
    pass


ColorsConfigurationOutputTypeDef = TypedDict(
    "ColorsConfigurationOutputTypeDef",
    {
        "CustomColors": List[CustomColorTypeDef],
    },
    total=False,
)

ColorsConfigurationTypeDef = TypedDict(
    "ColorsConfigurationTypeDef",
    {
        "CustomColors": Sequence[CustomColorTypeDef],
    },
    total=False,
)

ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": GeoSpatialDataRoleType,
        "ColumnDescription": ColumnDescriptionTypeDef,
    },
    total=False,
)

ColumnGroupSchemaOutputTypeDef = TypedDict(
    "ColumnGroupSchemaOutputTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": List[ColumnGroupColumnSchemaTypeDef],
    },
    total=False,
)

ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {
        "Name": str,
        "ColumnGroupColumnSchemaList": Sequence[ColumnGroupColumnSchemaTypeDef],
    },
    total=False,
)

ColumnGroupOutputTypeDef = TypedDict(
    "ColumnGroupOutputTypeDef",
    {
        "GeoSpatialColumnGroup": GeoSpatialColumnGroupOutputTypeDef,
    },
    total=False,
)

ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef",
    {
        "GeoSpatialColumnGroup": GeoSpatialColumnGroupTypeDef,
    },
    total=False,
)

DataSetSchemaOutputTypeDef = TypedDict(
    "DataSetSchemaOutputTypeDef",
    {
        "ColumnSchemaList": List[ColumnSchemaTypeDef],
    },
    total=False,
)

DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef",
    {
        "ColumnSchemaList": Sequence[ColumnSchemaTypeDef],
    },
    total=False,
)

_RequiredConditionalFormattingCustomIconConditionTypeDef = TypedDict(
    "_RequiredConditionalFormattingCustomIconConditionTypeDef",
    {
        "Expression": str,
        "IconOptions": ConditionalFormattingCustomIconOptionsTypeDef,
    },
)
_OptionalConditionalFormattingCustomIconConditionTypeDef = TypedDict(
    "_OptionalConditionalFormattingCustomIconConditionTypeDef",
    {
        "Color": str,
        "DisplayConfiguration": ConditionalFormattingIconDisplayConfigurationTypeDef,
    },
    total=False,
)


class ConditionalFormattingCustomIconConditionTypeDef(
    _RequiredConditionalFormattingCustomIconConditionTypeDef,
    _OptionalConditionalFormattingCustomIconConditionTypeDef,
):
    pass


_RequiredCreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": AccountCustomizationTypeDef,
    },
)
_OptionalCreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccountCustomizationRequestRequestTypeDef",
    {
        "Namespace": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateAccountCustomizationRequestRequestTypeDef(
    _RequiredCreateAccountCustomizationRequestRequestTypeDef,
    _OptionalCreateAccountCustomizationRequestRequestTypeDef,
):
    pass


_RequiredCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "IdentityStore": Literal["QUICKSIGHT"],
    },
)
_OptionalCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNamespaceRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateNamespaceRequestRequestTypeDef(
    _RequiredCreateNamespaceRequestRequestTypeDef, _OptionalCreateNamespaceRequestRequestTypeDef
):
    pass


_RequiredCreateVPCConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "RoleArn": str,
    },
)
_OptionalCreateVPCConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVPCConnectionRequestRequestTypeDef",
    {
        "DnsResolvers": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateVPCConnectionRequestRequestTypeDef(
    _RequiredCreateVPCConnectionRequestRequestTypeDef,
    _OptionalCreateVPCConnectionRequestRequestTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "RequestId": str,
        "Status": int,
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

CreateAccountSubscriptionResponseTypeDef = TypedDict(
    "CreateAccountSubscriptionResponseTypeDef",
    {
        "SignupResponse": SignupResponseTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeAnalysisPermissionsResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeFolderPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeFolderResolvedPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeThemePermissionsResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTopicPermissionsResponseTypeDef = TypedDict(
    "DescribeTopicPermissionsResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LinkSharingConfigurationTypeDef = TypedDict(
    "LinkSharingConfigurationTypeDef",
    {
        "Permissions": List[ResourcePermissionOutputTypeDef],
    },
    total=False,
)

UpdateAnalysisPermissionsResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateFolderPermissionsResponseTypeDef = TypedDict(
    "UpdateFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateThemePermissionsResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTopicPermissionsResponseTypeDef = TypedDict(
    "UpdateTopicPermissionsResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateFolderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalCreateFolderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFolderRequestRequestTypeDef",
    {
        "Name": str,
        "FolderType": Literal["SHARED"],
        "ParentFolderArn": str,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateFolderRequestRequestTypeDef(
    _RequiredCreateFolderRequestRequestTypeDef, _OptionalCreateFolderRequestRequestTypeDef
):
    pass


_RequiredUpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
_OptionalUpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateAnalysisPermissionsRequestRequestTypeDef(
    _RequiredUpdateAnalysisPermissionsRequestRequestTypeDef,
    _OptionalUpdateAnalysisPermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalUpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "GrantLinkPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokeLinkPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateDashboardPermissionsRequestRequestTypeDef(
    _RequiredUpdateDashboardPermissionsRequestRequestTypeDef,
    _OptionalUpdateDashboardPermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
_OptionalUpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateDataSetPermissionsRequestRequestTypeDef(
    _RequiredUpdateDataSetPermissionsRequestRequestTypeDef,
    _OptionalUpdateDataSetPermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)
_OptionalUpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateDataSourcePermissionsRequestRequestTypeDef(
    _RequiredUpdateDataSourcePermissionsRequestRequestTypeDef,
    _OptionalUpdateDataSourcePermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
_OptionalUpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFolderPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateFolderPermissionsRequestRequestTypeDef(
    _RequiredUpdateFolderPermissionsRequestRequestTypeDef,
    _OptionalUpdateFolderPermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalUpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateTemplatePermissionsRequestRequestTypeDef(
    _RequiredUpdateTemplatePermissionsRequestRequestTypeDef,
    _OptionalUpdateTemplatePermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalUpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemePermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateThemePermissionsRequestRequestTypeDef(
    _RequiredUpdateThemePermissionsRequestRequestTypeDef,
    _OptionalUpdateThemePermissionsRequestRequestTypeDef,
):
    pass


_RequiredUpdateTopicPermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTopicPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
_OptionalUpdateTopicPermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTopicPermissionsRequestRequestTypeDef",
    {
        "GrantPermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
        "RevokePermissions": Sequence[
            Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateTopicPermissionsRequestRequestTypeDef(
    _RequiredUpdateTopicPermissionsRequestRequestTypeDef,
    _OptionalUpdateTopicPermissionsRequestRequestTypeDef,
):
    pass


DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "ImportMode": DataSetImportModeType,
        "RowLevelPermissionDataSet": RowLevelPermissionDataSetTypeDef,
        "RowLevelPermissionTagConfigurationApplied": bool,
        "ColumnLevelPermissionRulesApplied": bool,
    },
    total=False,
)

CreateFolderMembershipResponseTypeDef = TypedDict(
    "CreateFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "FolderMember": FolderMemberTypeDef,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": GroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeGroupMembershipResponseTypeDef = TypedDict(
    "DescribeGroupMembershipResponseTypeDef",
    {
        "GroupMember": GroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List[GroupMemberTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUserGroupsResponseTypeDef = TypedDict(
    "ListUserGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchGroupsResponseTypeDef = TypedDict(
    "SearchGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateTemplateAliasResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTemplateAliasResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTemplateAliasesResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List[TemplateAliasTypeDef],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateTemplateAliasResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateThemeAliasResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeThemeAliasResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListThemeAliasesResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseTypeDef",
    {
        "ThemeAliasList": List[ThemeAliasTypeDef],
        "Status": int,
        "RequestId": str,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateThemeAliasResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetArn": str,
        "RefreshSchedule": TopicRefreshScheduleTypeDef,
    },
)
_OptionalCreateTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTopicRefreshScheduleRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
    total=False,
)


class CreateTopicRefreshScheduleRequestRequestTypeDef(
    _RequiredCreateTopicRefreshScheduleRequestRequestTypeDef,
    _OptionalCreateTopicRefreshScheduleRequestRequestTypeDef,
):
    pass


UpdateTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "UpdateTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
        "RefreshSchedule": TopicRefreshScheduleTypeDef,
    },
)

CustomActionNavigationOperationTypeDef = TypedDict(
    "CustomActionNavigationOperationTypeDef",
    {
        "LocalNavigationConfiguration": LocalNavigationConfigurationTypeDef,
    },
    total=False,
)

_RequiredCustomValuesConfigurationOutputTypeDef = TypedDict(
    "_RequiredCustomValuesConfigurationOutputTypeDef",
    {
        "CustomValues": CustomParameterValuesOutputTypeDef,
    },
)
_OptionalCustomValuesConfigurationOutputTypeDef = TypedDict(
    "_OptionalCustomValuesConfigurationOutputTypeDef",
    {
        "IncludeNullValue": bool,
    },
    total=False,
)


class CustomValuesConfigurationOutputTypeDef(
    _RequiredCustomValuesConfigurationOutputTypeDef, _OptionalCustomValuesConfigurationOutputTypeDef
):
    pass


_RequiredCustomValuesConfigurationTypeDef = TypedDict(
    "_RequiredCustomValuesConfigurationTypeDef",
    {
        "CustomValues": CustomParameterValuesTypeDef,
    },
)
_OptionalCustomValuesConfigurationTypeDef = TypedDict(
    "_OptionalCustomValuesConfigurationTypeDef",
    {
        "IncludeNullValue": bool,
    },
    total=False,
)


class CustomValuesConfigurationTypeDef(
    _RequiredCustomValuesConfigurationTypeDef, _OptionalCustomValuesConfigurationTypeDef
):
    pass


_RequiredCustomSqlOutputTypeDef = TypedDict(
    "_RequiredCustomSqlOutputTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
    },
)
_OptionalCustomSqlOutputTypeDef = TypedDict(
    "_OptionalCustomSqlOutputTypeDef",
    {
        "Columns": List[InputColumnTypeDef],
    },
    total=False,
)


class CustomSqlOutputTypeDef(_RequiredCustomSqlOutputTypeDef, _OptionalCustomSqlOutputTypeDef):
    pass


_RequiredCustomSqlTypeDef = TypedDict(
    "_RequiredCustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
    },
)
_OptionalCustomSqlTypeDef = TypedDict(
    "_OptionalCustomSqlTypeDef",
    {
        "Columns": Sequence[InputColumnTypeDef],
    },
    total=False,
)


class CustomSqlTypeDef(_RequiredCustomSqlTypeDef, _OptionalCustomSqlTypeDef):
    pass


_RequiredRelationalTableOutputTypeDef = TypedDict(
    "_RequiredRelationalTableOutputTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": List[InputColumnTypeDef],
    },
)
_OptionalRelationalTableOutputTypeDef = TypedDict(
    "_OptionalRelationalTableOutputTypeDef",
    {
        "Catalog": str,
        "Schema": str,
    },
    total=False,
)


class RelationalTableOutputTypeDef(
    _RequiredRelationalTableOutputTypeDef, _OptionalRelationalTableOutputTypeDef
):
    pass


_RequiredRelationalTableTypeDef = TypedDict(
    "_RequiredRelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": Sequence[InputColumnTypeDef],
    },
)
_OptionalRelationalTableTypeDef = TypedDict(
    "_OptionalRelationalTableTypeDef",
    {
        "Catalog": str,
        "Schema": str,
    },
    total=False,
)


class RelationalTableTypeDef(_RequiredRelationalTableTypeDef, _OptionalRelationalTableTypeDef):
    pass


_RequiredSearchDashboardsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DashboardSearchFilterTypeDef],
    },
)
_OptionalSearchDashboardsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDashboardsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchDashboardsRequestRequestTypeDef(
    _RequiredSearchDashboardsRequestRequestTypeDef, _OptionalSearchDashboardsRequestRequestTypeDef
):
    pass


ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[DashboardSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchDashboardsResponseTypeDef = TypedDict(
    "SearchDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[DashboardSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDashboardVersionsResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List[DashboardVersionSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DashboardVisualPublishOptionsTypeDef = TypedDict(
    "DashboardVisualPublishOptionsTypeDef",
    {
        "ExportHiddenFieldsOption": ExportHiddenFieldsOptionTypeDef,
    },
    total=False,
)

TableInlineVisualizationTypeDef = TypedDict(
    "TableInlineVisualizationTypeDef",
    {
        "DataBars": DataBarsOptionsTypeDef,
    },
    total=False,
)

DataLabelTypeTypeDef = TypedDict(
    "DataLabelTypeTypeDef",
    {
        "FieldLabelType": FieldLabelTypeTypeDef,
        "DataPathLabelType": DataPathLabelTypeTypeDef,
        "RangeEndsLabelType": RangeEndsLabelTypeTypeDef,
        "MinimumLabelType": MinimumLabelTypeTypeDef,
        "MaximumLabelType": MaximumLabelTypeTypeDef,
    },
    total=False,
)

_RequiredDataPathColorTypeDef = TypedDict(
    "_RequiredDataPathColorTypeDef",
    {
        "Element": DataPathValueTypeDef,
        "Color": str,
    },
)
_OptionalDataPathColorTypeDef = TypedDict(
    "_OptionalDataPathColorTypeDef",
    {
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)


class DataPathColorTypeDef(_RequiredDataPathColorTypeDef, _OptionalDataPathColorTypeDef):
    pass


DataPathSortOutputTypeDef = TypedDict(
    "DataPathSortOutputTypeDef",
    {
        "Direction": SortDirectionType,
        "SortPaths": List[DataPathValueTypeDef],
    },
)

DataPathSortTypeDef = TypedDict(
    "DataPathSortTypeDef",
    {
        "Direction": SortDirectionType,
        "SortPaths": Sequence[DataPathValueTypeDef],
    },
)

_RequiredPivotTableDataPathOptionOutputTypeDef = TypedDict(
    "_RequiredPivotTableDataPathOptionOutputTypeDef",
    {
        "DataPathList": List[DataPathValueTypeDef],
    },
)
_OptionalPivotTableDataPathOptionOutputTypeDef = TypedDict(
    "_OptionalPivotTableDataPathOptionOutputTypeDef",
    {
        "Width": str,
    },
    total=False,
)


class PivotTableDataPathOptionOutputTypeDef(
    _RequiredPivotTableDataPathOptionOutputTypeDef, _OptionalPivotTableDataPathOptionOutputTypeDef
):
    pass


_RequiredPivotTableDataPathOptionTypeDef = TypedDict(
    "_RequiredPivotTableDataPathOptionTypeDef",
    {
        "DataPathList": Sequence[DataPathValueTypeDef],
    },
)
_OptionalPivotTableDataPathOptionTypeDef = TypedDict(
    "_OptionalPivotTableDataPathOptionTypeDef",
    {
        "Width": str,
    },
    total=False,
)


class PivotTableDataPathOptionTypeDef(
    _RequiredPivotTableDataPathOptionTypeDef, _OptionalPivotTableDataPathOptionTypeDef
):
    pass


PivotTableFieldCollapseStateTargetOutputTypeDef = TypedDict(
    "PivotTableFieldCollapseStateTargetOutputTypeDef",
    {
        "FieldId": str,
        "FieldDataPathValues": List[DataPathValueTypeDef],
    },
    total=False,
)

PivotTableFieldCollapseStateTargetTypeDef = TypedDict(
    "PivotTableFieldCollapseStateTargetTypeDef",
    {
        "FieldId": str,
        "FieldDataPathValues": Sequence[DataPathValueTypeDef],
    },
    total=False,
)

_RequiredSearchDataSetsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSetSearchFilterTypeDef],
    },
)
_OptionalSearchDataSetsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDataSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchDataSetsRequestRequestTypeDef(
    _RequiredSearchDataSetsRequestRequestTypeDef, _OptionalSearchDataSetsRequestRequestTypeDef
):
    pass


_RequiredSearchDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSourceSearchFilterTypeDef],
    },
)
_OptionalSearchDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDataSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchDataSourcesRequestRequestTypeDef(
    _RequiredSearchDataSourcesRequestRequestTypeDef, _OptionalSearchDataSourcesRequestRequestTypeDef
):
    pass


SearchDataSourcesResponseTypeDef = TypedDict(
    "SearchDataSourcesResponseTypeDef",
    {
        "DataSourceSummaries": List[DataSourceSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredDateTimeDatasetParameterOutputTypeDef = TypedDict(
    "_RequiredDateTimeDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalDateTimeDatasetParameterOutputTypeDef = TypedDict(
    "_OptionalDateTimeDatasetParameterOutputTypeDef",
    {
        "TimeGranularity": TimeGranularityType,
        "DefaultValues": DateTimeDatasetParameterDefaultValuesOutputTypeDef,
    },
    total=False,
)


class DateTimeDatasetParameterOutputTypeDef(
    _RequiredDateTimeDatasetParameterOutputTypeDef, _OptionalDateTimeDatasetParameterOutputTypeDef
):
    pass


_RequiredDateTimeDatasetParameterTypeDef = TypedDict(
    "_RequiredDateTimeDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalDateTimeDatasetParameterTypeDef = TypedDict(
    "_OptionalDateTimeDatasetParameterTypeDef",
    {
        "TimeGranularity": TimeGranularityType,
        "DefaultValues": DateTimeDatasetParameterDefaultValuesTypeDef,
    },
    total=False,
)


class DateTimeDatasetParameterTypeDef(
    _RequiredDateTimeDatasetParameterTypeDef, _OptionalDateTimeDatasetParameterTypeDef
):
    pass


TimeRangeFilterValueOutputTypeDef = TypedDict(
    "TimeRangeFilterValueOutputTypeDef",
    {
        "StaticValue": datetime,
        "RollingDate": RollingDateConfigurationTypeDef,
        "Parameter": str,
    },
    total=False,
)

TimeRangeFilterValueTypeDef = TypedDict(
    "TimeRangeFilterValueTypeDef",
    {
        "StaticValue": Union[datetime, str],
        "RollingDate": RollingDateConfigurationTypeDef,
        "Parameter": str,
    },
    total=False,
)

_RequiredDecimalDatasetParameterOutputTypeDef = TypedDict(
    "_RequiredDecimalDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalDecimalDatasetParameterOutputTypeDef = TypedDict(
    "_OptionalDecimalDatasetParameterOutputTypeDef",
    {
        "DefaultValues": DecimalDatasetParameterDefaultValuesOutputTypeDef,
    },
    total=False,
)


class DecimalDatasetParameterOutputTypeDef(
    _RequiredDecimalDatasetParameterOutputTypeDef, _OptionalDecimalDatasetParameterOutputTypeDef
):
    pass


_RequiredDecimalDatasetParameterTypeDef = TypedDict(
    "_RequiredDecimalDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalDecimalDatasetParameterTypeDef = TypedDict(
    "_OptionalDecimalDatasetParameterTypeDef",
    {
        "DefaultValues": DecimalDatasetParameterDefaultValuesTypeDef,
    },
    total=False,
)


class DecimalDatasetParameterTypeDef(
    _RequiredDecimalDatasetParameterTypeDef, _OptionalDecimalDatasetParameterTypeDef
):
    pass


DescribeFolderResponseTypeDef = TypedDict(
    "DescribeFolderResponseTypeDef",
    {
        "Status": int,
        "Folder": FolderTypeDef,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": IAMPolicyAssignmentTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTopicRefreshResponseTypeDef = TypedDict(
    "DescribeTopicRefreshResponseTypeDef",
    {
        "RefreshDetails": TopicRefreshDetailsTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTopicRefreshScheduleResponseTypeDef = TypedDict(
    "DescribeTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "RefreshSchedule": TopicRefreshScheduleOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TopicRefreshScheduleSummaryTypeDef = TypedDict(
    "TopicRefreshScheduleSummaryTypeDef",
    {
        "DatasetId": str,
        "DatasetArn": str,
        "DatasetName": str,
        "RefreshSchedule": TopicRefreshScheduleOutputTypeDef,
    },
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserList": List[UserTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RegisterUserResponseTypeDef = TypedDict(
    "RegisterUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DisplayFormatOptionsTypeDef = TypedDict(
    "DisplayFormatOptionsTypeDef",
    {
        "UseBlankCellFormat": bool,
        "BlankCellFormat": str,
        "DateFormat": str,
        "DecimalSeparator": TopicNumericSeparatorSymbolType,
        "GroupingSeparator": str,
        "UseGrouping": bool,
        "FractionDigits": int,
        "Prefix": str,
        "Suffix": str,
        "UnitScaler": NumberScaleType,
        "NegativeFormat": NegativeFormatTypeDef,
        "CurrencySymbol": str,
    },
    total=False,
)

DonutOptionsTypeDef = TypedDict(
    "DonutOptionsTypeDef",
    {
        "ArcOptions": ArcOptionsTypeDef,
        "DonutCenterOptions": DonutCenterOptionsTypeDef,
    },
    total=False,
)

_RequiredRelativeDatesFilterTypeDef = TypedDict(
    "_RequiredRelativeDatesFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AnchorDateConfiguration": AnchorDateConfigurationTypeDef,
        "TimeGranularity": TimeGranularityType,
        "RelativeDateType": RelativeDateTypeType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalRelativeDatesFilterTypeDef = TypedDict(
    "_OptionalRelativeDatesFilterTypeDef",
    {
        "MinimumGranularity": TimeGranularityType,
        "RelativeDateValue": int,
        "ParameterName": str,
        "ExcludePeriodConfiguration": ExcludePeriodConfigurationTypeDef,
    },
    total=False,
)


class RelativeDatesFilterTypeDef(
    _RequiredRelativeDatesFilterTypeDef, _OptionalRelativeDatesFilterTypeDef
):
    pass


FilterOperationTargetVisualsConfigurationOutputTypeDef = TypedDict(
    "FilterOperationTargetVisualsConfigurationOutputTypeDef",
    {
        "SameSheetTargetVisualConfiguration": SameSheetTargetVisualConfigurationOutputTypeDef,
    },
    total=False,
)

FilterOperationTargetVisualsConfigurationTypeDef = TypedDict(
    "FilterOperationTargetVisualsConfigurationTypeDef",
    {
        "SameSheetTargetVisualConfiguration": SameSheetTargetVisualConfigurationTypeDef,
    },
    total=False,
)

_RequiredSearchFoldersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[FolderSearchFilterTypeDef],
    },
)
_OptionalSearchFoldersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchFoldersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchFoldersRequestRequestTypeDef(
    _RequiredSearchFoldersRequestRequestTypeDef, _OptionalSearchFoldersRequestRequestTypeDef
):
    pass


ListFoldersResponseTypeDef = TypedDict(
    "ListFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List[FolderSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchFoldersResponseTypeDef = TypedDict(
    "SearchFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List[FolderSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

FontConfigurationTypeDef = TypedDict(
    "FontConfigurationTypeDef",
    {
        "FontSize": FontSizeTypeDef,
        "FontDecoration": FontDecorationType,
        "FontColor": str,
        "FontWeight": FontWeightTypeDef,
        "FontStyle": FontStyleType,
    },
    total=False,
)

TypographyOutputTypeDef = TypedDict(
    "TypographyOutputTypeDef",
    {
        "FontFamilies": List[FontTypeDef],
    },
    total=False,
)

TypographyTypeDef = TypedDict(
    "TypographyTypeDef",
    {
        "FontFamilies": Sequence[FontTypeDef],
    },
    total=False,
)

ForecastScenarioOutputTypeDef = TypedDict(
    "ForecastScenarioOutputTypeDef",
    {
        "WhatIfPointScenario": WhatIfPointScenarioOutputTypeDef,
        "WhatIfRangeScenario": WhatIfRangeScenarioOutputTypeDef,
    },
    total=False,
)

ForecastScenarioTypeDef = TypedDict(
    "ForecastScenarioTypeDef",
    {
        "WhatIfPointScenario": WhatIfPointScenarioTypeDef,
        "WhatIfRangeScenario": WhatIfRangeScenarioTypeDef,
    },
    total=False,
)

FreeFormLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": FreeFormLayoutScreenCanvasSizeOptionsTypeDef,
    },
    total=False,
)

SnapshotAnonymousUserTypeDef = TypedDict(
    "SnapshotAnonymousUserTypeDef",
    {
        "RowLevelPermissionTags": Sequence[SessionTagTypeDef],
    },
    total=False,
)

GeospatialWindowOptionsTypeDef = TypedDict(
    "GeospatialWindowOptionsTypeDef",
    {
        "Bounds": GeospatialCoordinateBoundsTypeDef,
        "MapZoomMode": MapZoomModeType,
    },
    total=False,
)

GeospatialHeatmapColorScaleOutputTypeDef = TypedDict(
    "GeospatialHeatmapColorScaleOutputTypeDef",
    {
        "Colors": List[GeospatialHeatmapDataColorTypeDef],
    },
    total=False,
)

GeospatialHeatmapColorScaleTypeDef = TypedDict(
    "GeospatialHeatmapColorScaleTypeDef",
    {
        "Colors": Sequence[GeospatialHeatmapDataColorTypeDef],
    },
    total=False,
)

TableSideBorderOptionsTypeDef = TypedDict(
    "TableSideBorderOptionsTypeDef",
    {
        "InnerVertical": TableBorderOptionsTypeDef,
        "InnerHorizontal": TableBorderOptionsTypeDef,
        "Left": TableBorderOptionsTypeDef,
        "Right": TableBorderOptionsTypeDef,
        "Top": TableBorderOptionsTypeDef,
        "Bottom": TableBorderOptionsTypeDef,
    },
    total=False,
)

GradientColorOutputTypeDef = TypedDict(
    "GradientColorOutputTypeDef",
    {
        "Stops": List[GradientStopTypeDef],
    },
    total=False,
)

GradientColorTypeDef = TypedDict(
    "GradientColorTypeDef",
    {
        "Stops": Sequence[GradientStopTypeDef],
    },
    total=False,
)

GridLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "GridLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": GridLayoutScreenCanvasSizeOptionsTypeDef,
    },
    total=False,
)

_RequiredSearchGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "Filters": Sequence[GroupSearchFilterTypeDef],
    },
)
_OptionalSearchGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class SearchGroupsRequestRequestTypeDef(
    _RequiredSearchGroupsRequestRequestTypeDef, _OptionalSearchGroupsRequestRequestTypeDef
):
    pass


ListIAMPolicyAssignmentsResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List[IAMPolicyAssignmentSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IncrementalRefreshTypeDef = TypedDict(
    "IncrementalRefreshTypeDef",
    {
        "LookbackWindow": LookbackWindowTypeDef,
    },
)

_RequiredIngestionTypeDef = TypedDict(
    "_RequiredIngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": IngestionStatusType,
        "CreatedTime": datetime,
    },
)
_OptionalIngestionTypeDef = TypedDict(
    "_OptionalIngestionTypeDef",
    {
        "IngestionId": str,
        "ErrorInfo": ErrorInfoTypeDef,
        "RowInfo": RowInfoTypeDef,
        "QueueInfo": QueueInfoTypeDef,
        "IngestionTimeInSeconds": int,
        "IngestionSizeInBytes": int,
        "RequestSource": IngestionRequestSourceType,
        "RequestType": IngestionRequestTypeType,
    },
    total=False,
)


class IngestionTypeDef(_RequiredIngestionTypeDef, _OptionalIngestionTypeDef):
    pass


_RequiredIntegerDatasetParameterOutputTypeDef = TypedDict(
    "_RequiredIntegerDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalIntegerDatasetParameterOutputTypeDef = TypedDict(
    "_OptionalIntegerDatasetParameterOutputTypeDef",
    {
        "DefaultValues": IntegerDatasetParameterDefaultValuesOutputTypeDef,
    },
    total=False,
)


class IntegerDatasetParameterOutputTypeDef(
    _RequiredIntegerDatasetParameterOutputTypeDef, _OptionalIntegerDatasetParameterOutputTypeDef
):
    pass


_RequiredIntegerDatasetParameterTypeDef = TypedDict(
    "_RequiredIntegerDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalIntegerDatasetParameterTypeDef = TypedDict(
    "_OptionalIntegerDatasetParameterTypeDef",
    {
        "DefaultValues": IntegerDatasetParameterDefaultValuesTypeDef,
    },
    total=False,
)


class IntegerDatasetParameterTypeDef(
    _RequiredIntegerDatasetParameterTypeDef, _OptionalIntegerDatasetParameterTypeDef
):
    pass


_RequiredJoinInstructionTypeDef = TypedDict(
    "_RequiredJoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": JoinTypeType,
        "OnClause": str,
    },
)
_OptionalJoinInstructionTypeDef = TypedDict(
    "_OptionalJoinInstructionTypeDef",
    {
        "LeftJoinKeyProperties": JoinKeyPropertiesTypeDef,
        "RightJoinKeyProperties": JoinKeyPropertiesTypeDef,
    },
    total=False,
)


class JoinInstructionTypeDef(_RequiredJoinInstructionTypeDef, _OptionalJoinInstructionTypeDef):
    pass


LineChartDefaultSeriesSettingsTypeDef = TypedDict(
    "LineChartDefaultSeriesSettingsTypeDef",
    {
        "AxisBinding": AxisBindingType,
        "LineStyleSettings": LineChartLineStyleSettingsTypeDef,
        "MarkerStyleSettings": LineChartMarkerStyleSettingsTypeDef,
    },
    total=False,
)

LineChartSeriesSettingsTypeDef = TypedDict(
    "LineChartSeriesSettingsTypeDef",
    {
        "LineStyleSettings": LineChartLineStyleSettingsTypeDef,
        "MarkerStyleSettings": LineChartMarkerStyleSettingsTypeDef,
    },
    total=False,
)

_RequiredListAnalysesRequestListAnalysesPaginateTypeDef = TypedDict(
    "_RequiredListAnalysesRequestListAnalysesPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAnalysesRequestListAnalysesPaginateTypeDef = TypedDict(
    "_OptionalListAnalysesRequestListAnalysesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAnalysesRequestListAnalysesPaginateTypeDef(
    _RequiredListAnalysesRequestListAnalysesPaginateTypeDef,
    _OptionalListAnalysesRequestListAnalysesPaginateTypeDef,
):
    pass


_RequiredListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef = TypedDict(
    "_RequiredListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef = TypedDict(
    "_OptionalListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef(
    _RequiredListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef,
    _OptionalListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef,
):
    pass


_RequiredListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef = TypedDict(
    "_RequiredListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef = TypedDict(
    "_OptionalListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef(
    _RequiredListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef,
    _OptionalListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef,
):
    pass


_RequiredListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef = TypedDict(
    "_RequiredListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
_OptionalListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef = TypedDict(
    "_OptionalListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef(
    _RequiredListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef,
    _OptionalListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef,
):
    pass


_RequiredListDashboardsRequestListDashboardsPaginateTypeDef = TypedDict(
    "_RequiredListDashboardsRequestListDashboardsPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDashboardsRequestListDashboardsPaginateTypeDef = TypedDict(
    "_OptionalListDashboardsRequestListDashboardsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDashboardsRequestListDashboardsPaginateTypeDef(
    _RequiredListDashboardsRequestListDashboardsPaginateTypeDef,
    _OptionalListDashboardsRequestListDashboardsPaginateTypeDef,
):
    pass


_RequiredListDataSetsRequestListDataSetsPaginateTypeDef = TypedDict(
    "_RequiredListDataSetsRequestListDataSetsPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSetsRequestListDataSetsPaginateTypeDef = TypedDict(
    "_OptionalListDataSetsRequestListDataSetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDataSetsRequestListDataSetsPaginateTypeDef(
    _RequiredListDataSetsRequestListDataSetsPaginateTypeDef,
    _OptionalListDataSetsRequestListDataSetsPaginateTypeDef,
):
    pass


_RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListDataSourcesRequestListDataSourcesPaginateTypeDef(
    _RequiredListDataSourcesRequestListDataSourcesPaginateTypeDef,
    _OptionalListDataSourcesRequestListDataSourcesPaginateTypeDef,
):
    pass


_RequiredListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef = TypedDict(
    "_RequiredListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef = TypedDict(
    "_OptionalListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef(
    _RequiredListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef,
    _OptionalListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef,
):
    pass


_RequiredListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "_RequiredListGroupsRequestListGroupsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "_OptionalListGroupsRequestListGroupsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListGroupsRequestListGroupsPaginateTypeDef(
    _RequiredListGroupsRequestListGroupsPaginateTypeDef,
    _OptionalListGroupsRequestListGroupsPaginateTypeDef,
):
    pass


_RequiredListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef(
    _RequiredListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef,
    _OptionalListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef,
):
    pass


_RequiredListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef = TypedDict(
    "_RequiredListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef = TypedDict(
    "_OptionalListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef",
    {
        "AssignmentStatus": AssignmentStatusType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef(
    _RequiredListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef,
    _OptionalListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef,
):
    pass


_RequiredListIngestionsRequestListIngestionsPaginateTypeDef = TypedDict(
    "_RequiredListIngestionsRequestListIngestionsPaginateTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
    },
)
_OptionalListIngestionsRequestListIngestionsPaginateTypeDef = TypedDict(
    "_OptionalListIngestionsRequestListIngestionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListIngestionsRequestListIngestionsPaginateTypeDef(
    _RequiredListIngestionsRequestListIngestionsPaginateTypeDef,
    _OptionalListIngestionsRequestListIngestionsPaginateTypeDef,
):
    pass


_RequiredListNamespacesRequestListNamespacesPaginateTypeDef = TypedDict(
    "_RequiredListNamespacesRequestListNamespacesPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListNamespacesRequestListNamespacesPaginateTypeDef = TypedDict(
    "_OptionalListNamespacesRequestListNamespacesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListNamespacesRequestListNamespacesPaginateTypeDef(
    _RequiredListNamespacesRequestListNamespacesPaginateTypeDef,
    _OptionalListNamespacesRequestListNamespacesPaginateTypeDef,
):
    pass


_RequiredListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef = TypedDict(
    "_RequiredListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef = TypedDict(
    "_OptionalListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef(
    _RequiredListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef,
    _OptionalListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef,
):
    pass


_RequiredListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef(
    _RequiredListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef,
    _OptionalListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef,
):
    pass


_RequiredListTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "_RequiredListTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "_OptionalListTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListTemplatesRequestListTemplatesPaginateTypeDef(
    _RequiredListTemplatesRequestListTemplatesPaginateTypeDef,
    _OptionalListTemplatesRequestListTemplatesPaginateTypeDef,
):
    pass


_RequiredListThemeVersionsRequestListThemeVersionsPaginateTypeDef = TypedDict(
    "_RequiredListThemeVersionsRequestListThemeVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
_OptionalListThemeVersionsRequestListThemeVersionsPaginateTypeDef = TypedDict(
    "_OptionalListThemeVersionsRequestListThemeVersionsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListThemeVersionsRequestListThemeVersionsPaginateTypeDef(
    _RequiredListThemeVersionsRequestListThemeVersionsPaginateTypeDef,
    _OptionalListThemeVersionsRequestListThemeVersionsPaginateTypeDef,
):
    pass


_RequiredListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "_RequiredListThemesRequestListThemesPaginateTypeDef",
    {
        "AwsAccountId": str,
    },
)
_OptionalListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "_OptionalListThemesRequestListThemesPaginateTypeDef",
    {
        "Type": ThemeTypeType,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListThemesRequestListThemesPaginateTypeDef(
    _RequiredListThemesRequestListThemesPaginateTypeDef,
    _OptionalListThemesRequestListThemesPaginateTypeDef,
):
    pass


_RequiredListUserGroupsRequestListUserGroupsPaginateTypeDef = TypedDict(
    "_RequiredListUserGroupsRequestListUserGroupsPaginateTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUserGroupsRequestListUserGroupsPaginateTypeDef = TypedDict(
    "_OptionalListUserGroupsRequestListUserGroupsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListUserGroupsRequestListUserGroupsPaginateTypeDef(
    _RequiredListUserGroupsRequestListUserGroupsPaginateTypeDef,
    _OptionalListUserGroupsRequestListUserGroupsPaginateTypeDef,
):
    pass


_RequiredListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_RequiredListUsersRequestListUsersPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
_OptionalListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "_OptionalListUsersRequestListUsersPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListUsersRequestListUsersPaginateTypeDef(
    _RequiredListUsersRequestListUsersPaginateTypeDef,
    _OptionalListUsersRequestListUsersPaginateTypeDef,
):
    pass


_RequiredSearchAnalysesRequestSearchAnalysesPaginateTypeDef = TypedDict(
    "_RequiredSearchAnalysesRequestSearchAnalysesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[AnalysisSearchFilterTypeDef],
    },
)
_OptionalSearchAnalysesRequestSearchAnalysesPaginateTypeDef = TypedDict(
    "_OptionalSearchAnalysesRequestSearchAnalysesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchAnalysesRequestSearchAnalysesPaginateTypeDef(
    _RequiredSearchAnalysesRequestSearchAnalysesPaginateTypeDef,
    _OptionalSearchAnalysesRequestSearchAnalysesPaginateTypeDef,
):
    pass


_RequiredSearchDashboardsRequestSearchDashboardsPaginateTypeDef = TypedDict(
    "_RequiredSearchDashboardsRequestSearchDashboardsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DashboardSearchFilterTypeDef],
    },
)
_OptionalSearchDashboardsRequestSearchDashboardsPaginateTypeDef = TypedDict(
    "_OptionalSearchDashboardsRequestSearchDashboardsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchDashboardsRequestSearchDashboardsPaginateTypeDef(
    _RequiredSearchDashboardsRequestSearchDashboardsPaginateTypeDef,
    _OptionalSearchDashboardsRequestSearchDashboardsPaginateTypeDef,
):
    pass


_RequiredSearchDataSetsRequestSearchDataSetsPaginateTypeDef = TypedDict(
    "_RequiredSearchDataSetsRequestSearchDataSetsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSetSearchFilterTypeDef],
    },
)
_OptionalSearchDataSetsRequestSearchDataSetsPaginateTypeDef = TypedDict(
    "_OptionalSearchDataSetsRequestSearchDataSetsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchDataSetsRequestSearchDataSetsPaginateTypeDef(
    _RequiredSearchDataSetsRequestSearchDataSetsPaginateTypeDef,
    _OptionalSearchDataSetsRequestSearchDataSetsPaginateTypeDef,
):
    pass


_RequiredSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef = TypedDict(
    "_RequiredSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSourceSearchFilterTypeDef],
    },
)
_OptionalSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef = TypedDict(
    "_OptionalSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef(
    _RequiredSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef,
    _OptionalSearchDataSourcesRequestSearchDataSourcesPaginateTypeDef,
):
    pass


_RequiredSearchGroupsRequestSearchGroupsPaginateTypeDef = TypedDict(
    "_RequiredSearchGroupsRequestSearchGroupsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "Filters": Sequence[GroupSearchFilterTypeDef],
    },
)
_OptionalSearchGroupsRequestSearchGroupsPaginateTypeDef = TypedDict(
    "_OptionalSearchGroupsRequestSearchGroupsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class SearchGroupsRequestSearchGroupsPaginateTypeDef(
    _RequiredSearchGroupsRequestSearchGroupsPaginateTypeDef,
    _OptionalSearchGroupsRequestSearchGroupsPaginateTypeDef,
):
    pass


ListFolderMembersResponseTypeDef = TypedDict(
    "ListFolderMembersResponseTypeDef",
    {
        "Status": int,
        "FolderMemberList": List[MemberIdArnPairTypeDef],
        "NextToken": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List[TemplateVersionSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List[TemplateSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListThemeVersionsResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseTypeDef",
    {
        "ThemeVersionSummaryList": List[ThemeVersionSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "ThemeSummaryList": List[ThemeSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef",
    {
        "TopicsSummaries": List[TopicSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VisualSubtitleLabelOptionsTypeDef = TypedDict(
    "VisualSubtitleLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FormatText": LongFormatTextTypeDef,
    },
    total=False,
)

_RequiredS3ParametersTypeDef = TypedDict(
    "_RequiredS3ParametersTypeDef",
    {
        "ManifestFileLocation": ManifestFileLocationTypeDef,
    },
)
_OptionalS3ParametersTypeDef = TypedDict(
    "_OptionalS3ParametersTypeDef",
    {
        "RoleArn": str,
    },
    total=False,
)


class S3ParametersTypeDef(_RequiredS3ParametersTypeDef, _OptionalS3ParametersTypeDef):
    pass


TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {
        "Gutter": GutterStyleTypeDef,
        "Margin": MarginStyleTypeDef,
    },
    total=False,
)

NamedEntityDefinitionOutputTypeDef = TypedDict(
    "NamedEntityDefinitionOutputTypeDef",
    {
        "FieldName": str,
        "PropertyName": str,
        "PropertyRole": PropertyRoleType,
        "PropertyUsage": PropertyUsageType,
        "Metric": NamedEntityDefinitionMetricOutputTypeDef,
    },
    total=False,
)

NamedEntityDefinitionTypeDef = TypedDict(
    "NamedEntityDefinitionTypeDef",
    {
        "FieldName": str,
        "PropertyName": str,
        "PropertyRole": PropertyRoleType,
        "PropertyUsage": PropertyUsageType,
        "Metric": NamedEntityDefinitionMetricTypeDef,
    },
    total=False,
)

NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": str,
        "Arn": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "NamespaceError": NamespaceErrorTypeDef,
    },
    total=False,
)

VPCConnectionSummaryTypeDef = TypedDict(
    "VPCConnectionSummaryTypeDef",
    {
        "VPCConnectionId": str,
        "Arn": str,
        "Name": str,
        "VPCId": str,
        "SecurityGroupIds": List[str],
        "DnsResolvers": List[str],
        "Status": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "NetworkInterfaces": List[NetworkInterfaceTypeDef],
        "RoleArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

VPCConnectionTypeDef = TypedDict(
    "VPCConnectionTypeDef",
    {
        "VPCConnectionId": str,
        "Arn": str,
        "Name": str,
        "VPCId": str,
        "SecurityGroupIds": List[str],
        "DnsResolvers": List[str],
        "Status": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "NetworkInterfaces": List[NetworkInterfaceTypeDef],
        "RoleArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredOverrideDatasetParameterOperationOutputTypeDef = TypedDict(
    "_RequiredOverrideDatasetParameterOperationOutputTypeDef",
    {
        "ParameterName": str,
    },
)
_OptionalOverrideDatasetParameterOperationOutputTypeDef = TypedDict(
    "_OptionalOverrideDatasetParameterOperationOutputTypeDef",
    {
        "NewParameterName": str,
        "NewDefaultValues": NewDefaultValuesOutputTypeDef,
    },
    total=False,
)


class OverrideDatasetParameterOperationOutputTypeDef(
    _RequiredOverrideDatasetParameterOperationOutputTypeDef,
    _OptionalOverrideDatasetParameterOperationOutputTypeDef,
):
    pass


_RequiredOverrideDatasetParameterOperationTypeDef = TypedDict(
    "_RequiredOverrideDatasetParameterOperationTypeDef",
    {
        "ParameterName": str,
    },
)
_OptionalOverrideDatasetParameterOperationTypeDef = TypedDict(
    "_OptionalOverrideDatasetParameterOperationTypeDef",
    {
        "NewParameterName": str,
        "NewDefaultValues": NewDefaultValuesTypeDef,
    },
    total=False,
)


class OverrideDatasetParameterOperationTypeDef(
    _RequiredOverrideDatasetParameterOperationTypeDef,
    _OptionalOverrideDatasetParameterOperationTypeDef,
):
    pass


NumericSeparatorConfigurationTypeDef = TypedDict(
    "NumericSeparatorConfigurationTypeDef",
    {
        "DecimalSeparator": NumericSeparatorSymbolType,
        "ThousandsSeparator": ThousandSeparatorOptionsTypeDef,
    },
    total=False,
)

NumericalAggregationFunctionTypeDef = TypedDict(
    "NumericalAggregationFunctionTypeDef",
    {
        "SimpleNumericalAggregation": SimpleNumericalAggregationFunctionType,
        "PercentileAggregation": PercentileAggregationTypeDef,
    },
    total=False,
)

ParametersOutputTypeDef = TypedDict(
    "ParametersOutputTypeDef",
    {
        "StringParameters": List[StringParameterOutputTypeDef],
        "IntegerParameters": List[IntegerParameterOutputTypeDef],
        "DecimalParameters": List[DecimalParameterOutputTypeDef],
        "DateTimeParameters": List[DateTimeParameterOutputTypeDef],
    },
    total=False,
)

ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "StringParameters": Sequence[StringParameterTypeDef],
        "IntegerParameters": Sequence[IntegerParameterTypeDef],
        "DecimalParameters": Sequence[DecimalParameterTypeDef],
        "DateTimeParameters": Sequence[DateTimeParameterTypeDef],
    },
    total=False,
)

VisibleRangeOptionsTypeDef = TypedDict(
    "VisibleRangeOptionsTypeDef",
    {
        "PercentRange": PercentVisibleRangeTypeDef,
    },
    total=False,
)

RadarChartSeriesSettingsTypeDef = TypedDict(
    "RadarChartSeriesSettingsTypeDef",
    {
        "AreaStyleSettings": RadarChartAreaStyleSettingsTypeDef,
    },
    total=False,
)

TopicRangeFilterConstantTypeDef = TypedDict(
    "TopicRangeFilterConstantTypeDef",
    {
        "ConstantType": ConstantTypeType,
        "RangeConstant": RangeConstantTypeDef,
    },
    total=False,
)

_RequiredRefreshFrequencyTypeDef = TypedDict(
    "_RequiredRefreshFrequencyTypeDef",
    {
        "Interval": RefreshIntervalType,
    },
)
_OptionalRefreshFrequencyTypeDef = TypedDict(
    "_OptionalRefreshFrequencyTypeDef",
    {
        "RefreshOnDay": ScheduleRefreshOnEntityTypeDef,
        "Timezone": str,
        "TimeOfTheDay": str,
    },
    total=False,
)


class RefreshFrequencyTypeDef(_RequiredRefreshFrequencyTypeDef, _OptionalRefreshFrequencyTypeDef):
    pass


RegisteredUserConsoleFeatureConfigurationsTypeDef = TypedDict(
    "RegisteredUserConsoleFeatureConfigurationsTypeDef",
    {
        "StatePersistence": StatePersistenceConfigurationsTypeDef,
    },
    total=False,
)

RegisteredUserDashboardFeatureConfigurationsTypeDef = TypedDict(
    "RegisteredUserDashboardFeatureConfigurationsTypeDef",
    {
        "StatePersistence": StatePersistenceConfigurationsTypeDef,
        "Bookmarks": BookmarksConfigurationsTypeDef,
    },
    total=False,
)

_RequiredRowLevelPermissionTagConfigurationOutputTypeDef = TypedDict(
    "_RequiredRowLevelPermissionTagConfigurationOutputTypeDef",
    {
        "TagRules": List[RowLevelPermissionTagRuleTypeDef],
    },
)
_OptionalRowLevelPermissionTagConfigurationOutputTypeDef = TypedDict(
    "_OptionalRowLevelPermissionTagConfigurationOutputTypeDef",
    {
        "Status": StatusType,
        "TagRuleConfigurations": List[List[str]],
    },
    total=False,
)


class RowLevelPermissionTagConfigurationOutputTypeDef(
    _RequiredRowLevelPermissionTagConfigurationOutputTypeDef,
    _OptionalRowLevelPermissionTagConfigurationOutputTypeDef,
):
    pass


_RequiredRowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "_RequiredRowLevelPermissionTagConfigurationTypeDef",
    {
        "TagRules": Sequence[RowLevelPermissionTagRuleTypeDef],
    },
)
_OptionalRowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "_OptionalRowLevelPermissionTagConfigurationTypeDef",
    {
        "Status": StatusType,
        "TagRuleConfigurations": Sequence[Sequence[str]],
    },
    total=False,
)


class RowLevelPermissionTagConfigurationTypeDef(
    _RequiredRowLevelPermissionTagConfigurationTypeDef,
    _OptionalRowLevelPermissionTagConfigurationTypeDef,
):
    pass


SnapshotS3DestinationConfigurationTypeDef = TypedDict(
    "SnapshotS3DestinationConfigurationTypeDef",
    {
        "BucketConfiguration": S3BucketConfigurationTypeDef,
    },
    total=False,
)

_RequiredS3SourceOutputTypeDef = TypedDict(
    "_RequiredS3SourceOutputTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": List[InputColumnTypeDef],
    },
)
_OptionalS3SourceOutputTypeDef = TypedDict(
    "_OptionalS3SourceOutputTypeDef",
    {
        "UploadSettings": UploadSettingsTypeDef,
    },
    total=False,
)


class S3SourceOutputTypeDef(_RequiredS3SourceOutputTypeDef, _OptionalS3SourceOutputTypeDef):
    pass


_RequiredS3SourceTypeDef = TypedDict(
    "_RequiredS3SourceTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": Sequence[InputColumnTypeDef],
    },
)
_OptionalS3SourceTypeDef = TypedDict(
    "_OptionalS3SourceTypeDef",
    {
        "UploadSettings": UploadSettingsTypeDef,
    },
    total=False,
)


class S3SourceTypeDef(_RequiredS3SourceTypeDef, _OptionalS3SourceTypeDef):
    pass


SectionPageBreakConfigurationTypeDef = TypedDict(
    "SectionPageBreakConfigurationTypeDef",
    {
        "After": SectionAfterPageBreakTypeDef,
    },
    total=False,
)

SectionBasedLayoutPaperCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    {
        "PaperSize": PaperSizeType,
        "PaperOrientation": PaperOrientationType,
        "PaperMargin": SpacingTypeDef,
    },
    total=False,
)

SectionStyleTypeDef = TypedDict(
    "SectionStyleTypeDef",
    {
        "Height": str,
        "Padding": SpacingTypeDef,
    },
    total=False,
)

SelectedSheetsFilterScopeConfigurationOutputTypeDef = TypedDict(
    "SelectedSheetsFilterScopeConfigurationOutputTypeDef",
    {
        "SheetVisualScopingConfigurations": List[SheetVisualScopingConfigurationOutputTypeDef],
    },
    total=False,
)

SelectedSheetsFilterScopeConfigurationTypeDef = TypedDict(
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    {
        "SheetVisualScopingConfigurations": Sequence[SheetVisualScopingConfigurationTypeDef],
    },
    total=False,
)

SheetElementRenderingRuleTypeDef = TypedDict(
    "SheetElementRenderingRuleTypeDef",
    {
        "Expression": str,
        "ConfigurationOverrides": SheetElementConfigurationOverridesTypeDef,
    },
)

VisualTitleLabelOptionsTypeDef = TypedDict(
    "VisualTitleLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FormatText": ShortFormatTextTypeDef,
    },
    total=False,
)

SnapshotUserConfigurationRedactedTypeDef = TypedDict(
    "SnapshotUserConfigurationRedactedTypeDef",
    {
        "AnonymousUsers": List[SnapshotAnonymousUserRedactedTypeDef],
    },
    total=False,
)

SnapshotFileOutputTypeDef = TypedDict(
    "SnapshotFileOutputTypeDef",
    {
        "SheetSelections": List[SnapshotFileSheetSelectionOutputTypeDef],
        "FormatType": SnapshotFileFormatTypeType,
    },
)

SnapshotFileTypeDef = TypedDict(
    "SnapshotFileTypeDef",
    {
        "SheetSelections": Sequence[SnapshotFileSheetSelectionTypeDef],
        "FormatType": SnapshotFileFormatTypeType,
    },
)

_RequiredStringDatasetParameterOutputTypeDef = TypedDict(
    "_RequiredStringDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalStringDatasetParameterOutputTypeDef = TypedDict(
    "_OptionalStringDatasetParameterOutputTypeDef",
    {
        "DefaultValues": StringDatasetParameterDefaultValuesOutputTypeDef,
    },
    total=False,
)


class StringDatasetParameterOutputTypeDef(
    _RequiredStringDatasetParameterOutputTypeDef, _OptionalStringDatasetParameterOutputTypeDef
):
    pass


_RequiredStringDatasetParameterTypeDef = TypedDict(
    "_RequiredStringDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
    },
)
_OptionalStringDatasetParameterTypeDef = TypedDict(
    "_OptionalStringDatasetParameterTypeDef",
    {
        "DefaultValues": StringDatasetParameterDefaultValuesTypeDef,
    },
    total=False,
)


class StringDatasetParameterTypeDef(
    _RequiredStringDatasetParameterTypeDef, _OptionalStringDatasetParameterTypeDef
):
    pass


TableFieldImageConfigurationTypeDef = TypedDict(
    "TableFieldImageConfigurationTypeDef",
    {
        "SizingOptions": TableCellImageSizingConfigurationTypeDef,
    },
    total=False,
)

TopicNumericEqualityFilterTypeDef = TypedDict(
    "TopicNumericEqualityFilterTypeDef",
    {
        "Constant": TopicSingularFilterConstantTypeDef,
        "Aggregation": NamedFilterAggTypeType,
    },
    total=False,
)

TopicRelativeDateFilterTypeDef = TypedDict(
    "TopicRelativeDateFilterTypeDef",
    {
        "TimeGranularity": TopicTimeGranularityType,
        "RelativeDateFilterFunction": TopicRelativeDateFilterFunctionType,
        "Constant": TopicSingularFilterConstantTypeDef,
    },
    total=False,
)

CascadingControlConfigurationOutputTypeDef = TypedDict(
    "CascadingControlConfigurationOutputTypeDef",
    {
        "SourceControls": List[CascadingControlSourceTypeDef],
    },
    total=False,
)

CascadingControlConfigurationTypeDef = TypedDict(
    "CascadingControlConfigurationTypeDef",
    {
        "SourceControls": Sequence[CascadingControlSourceTypeDef],
    },
    total=False,
)

DateTimeDefaultValuesOutputTypeDef = TypedDict(
    "DateTimeDefaultValuesOutputTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": List[datetime],
        "RollingDate": RollingDateConfigurationTypeDef,
    },
    total=False,
)

DateTimeDefaultValuesTypeDef = TypedDict(
    "DateTimeDefaultValuesTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": Sequence[Union[datetime, str]],
        "RollingDate": RollingDateConfigurationTypeDef,
    },
    total=False,
)

DecimalDefaultValuesOutputTypeDef = TypedDict(
    "DecimalDefaultValuesOutputTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": List[float],
    },
    total=False,
)

DecimalDefaultValuesTypeDef = TypedDict(
    "DecimalDefaultValuesTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": Sequence[float],
    },
    total=False,
)

IntegerDefaultValuesOutputTypeDef = TypedDict(
    "IntegerDefaultValuesOutputTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": List[int],
    },
    total=False,
)

IntegerDefaultValuesTypeDef = TypedDict(
    "IntegerDefaultValuesTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": Sequence[int],
    },
    total=False,
)

StringDefaultValuesOutputTypeDef = TypedDict(
    "StringDefaultValuesOutputTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": List[str],
    },
    total=False,
)

StringDefaultValuesTypeDef = TypedDict(
    "StringDefaultValuesTypeDef",
    {
        "DynamicValue": DynamicDefaultValueTypeDef,
        "StaticValues": Sequence[str],
    },
    total=False,
)

DrillDownFilterOutputTypeDef = TypedDict(
    "DrillDownFilterOutputTypeDef",
    {
        "NumericEqualityFilter": NumericEqualityDrillDownFilterTypeDef,
        "CategoryFilter": CategoryDrillDownFilterOutputTypeDef,
        "TimeRangeFilter": TimeRangeDrillDownFilterOutputTypeDef,
    },
    total=False,
)

DrillDownFilterTypeDef = TypedDict(
    "DrillDownFilterTypeDef",
    {
        "NumericEqualityFilter": NumericEqualityDrillDownFilterTypeDef,
        "CategoryFilter": CategoryDrillDownFilterTypeDef,
        "TimeRangeFilter": TimeRangeDrillDownFilterTypeDef,
    },
    total=False,
)

AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "AnalysisId": str,
        "Arn": str,
        "Name": str,
        "Status": ResourceStatusType,
        "Errors": List[AnalysisErrorTypeDef],
        "DataSetArns": List[str],
        "ThemeArn": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Sheets": List[SheetTypeDef],
    },
    total=False,
)

DashboardVersionTypeDef = TypedDict(
    "DashboardVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[DashboardErrorTypeDef],
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "Arn": str,
        "SourceEntityArn": str,
        "DataSetArns": List[str],
        "Description": str,
        "ThemeArn": str,
        "Sheets": List[SheetTypeDef],
    },
    total=False,
)

AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef",
    {
        "SourceTemplate": AnalysisSourceTemplateTypeDef,
    },
    total=False,
)

DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {
        "SourceTemplate": DashboardSourceTemplateTypeDef,
    },
    total=False,
)

TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": TemplateSourceAnalysisTypeDef,
        "SourceTemplate": TemplateSourceTemplateTypeDef,
    },
    total=False,
)

AnonymousUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": AnonymousUserDashboardEmbeddingConfigurationTypeDef,
        "DashboardVisual": AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef,
        "QSearchBar": AnonymousUserQSearchBarEmbeddingConfigurationTypeDef,
    },
    total=False,
)

DescribeAssetBundleExportJobResponseTypeDef = TypedDict(
    "DescribeAssetBundleExportJobResponseTypeDef",
    {
        "JobStatus": AssetBundleExportJobStatusType,
        "DownloadUrl": str,
        "Errors": List[AssetBundleExportJobErrorTypeDef],
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleExportJobId": str,
        "AwsAccountId": str,
        "ResourceArns": List[str],
        "IncludeAllDependencies": bool,
        "ExportFormat": AssetBundleExportFormatType,
        "CloudFormationOverridePropertyConfiguration": (
            AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef
        ),
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartAssetBundleExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartAssetBundleExportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleExportJobId": str,
        "ResourceArns": Sequence[str],
        "ExportFormat": AssetBundleExportFormatType,
    },
)
_OptionalStartAssetBundleExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartAssetBundleExportJobRequestRequestTypeDef",
    {
        "IncludeAllDependencies": bool,
        "CloudFormationOverridePropertyConfiguration": (
            AssetBundleCloudFormationOverridePropertyConfigurationTypeDef
        ),
    },
    total=False,
)


class StartAssetBundleExportJobRequestRequestTypeDef(
    _RequiredStartAssetBundleExportJobRequestRequestTypeDef,
    _OptionalStartAssetBundleExportJobRequestRequestTypeDef,
):
    pass


NumericAxisOptionsOutputTypeDef = TypedDict(
    "NumericAxisOptionsOutputTypeDef",
    {
        "Scale": AxisScaleTypeDef,
        "Range": AxisDisplayRangeOutputTypeDef,
    },
    total=False,
)

NumericAxisOptionsTypeDef = TypedDict(
    "NumericAxisOptionsTypeDef",
    {
        "Scale": AxisScaleTypeDef,
        "Range": AxisDisplayRangeTypeDef,
    },
    total=False,
)

CategoryFilterOutputTypeDef = TypedDict(
    "CategoryFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationOutputTypeDef,
    },
)

CategoryFilterTypeDef = TypedDict(
    "CategoryFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationTypeDef,
    },
)

ClusterMarkerConfigurationTypeDef = TypedDict(
    "ClusterMarkerConfigurationTypeDef",
    {
        "ClusterMarker": ClusterMarkerTypeDef,
    },
    total=False,
)

TopicCategoryFilterOutputTypeDef = TypedDict(
    "TopicCategoryFilterOutputTypeDef",
    {
        "CategoryFilterFunction": CategoryFilterFunctionType,
        "CategoryFilterType": CategoryFilterTypeType,
        "Constant": TopicCategoryFilterConstantOutputTypeDef,
        "Inverse": bool,
    },
    total=False,
)

TopicCategoryFilterTypeDef = TypedDict(
    "TopicCategoryFilterTypeDef",
    {
        "CategoryFilterFunction": CategoryFilterFunctionType,
        "CategoryFilterType": CategoryFilterTypeType,
        "Constant": TopicCategoryFilterConstantTypeDef,
        "Inverse": bool,
    },
    total=False,
)

TagColumnOperationOutputTypeDef = TypedDict(
    "TagColumnOperationOutputTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ColumnTagTypeDef],
    },
)

TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": Sequence[ColumnTagTypeDef],
    },
)

DataSetConfigurationOutputTypeDef = TypedDict(
    "DataSetConfigurationOutputTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": DataSetSchemaOutputTypeDef,
        "ColumnGroupSchemaList": List[ColumnGroupSchemaOutputTypeDef],
    },
    total=False,
)

DataSetConfigurationTypeDef = TypedDict(
    "DataSetConfigurationTypeDef",
    {
        "Placeholder": str,
        "DataSetSchema": DataSetSchemaTypeDef,
        "ColumnGroupSchemaList": Sequence[ColumnGroupSchemaTypeDef],
    },
    total=False,
)

ConditionalFormattingIconTypeDef = TypedDict(
    "ConditionalFormattingIconTypeDef",
    {
        "IconSet": ConditionalFormattingIconSetTypeDef,
        "CustomCondition": ConditionalFormattingCustomIconConditionTypeDef,
    },
    total=False,
)

DescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "LinkSharingConfiguration": LinkSharingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "LinkSharingConfiguration": LinkSharingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[DataSetSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SearchDataSetsResponseTypeDef = TypedDict(
    "SearchDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[DataSetSummaryTypeDef],
        "NextToken": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DestinationParameterValueConfigurationOutputTypeDef = TypedDict(
    "DestinationParameterValueConfigurationOutputTypeDef",
    {
        "CustomValuesConfiguration": CustomValuesConfigurationOutputTypeDef,
        "SelectAllValueOptions": Literal["ALL_VALUES"],
        "SourceParameterName": str,
        "SourceField": str,
        "SourceColumn": ColumnIdentifierTypeDef,
    },
    total=False,
)

DestinationParameterValueConfigurationTypeDef = TypedDict(
    "DestinationParameterValueConfigurationTypeDef",
    {
        "CustomValuesConfiguration": CustomValuesConfigurationTypeDef,
        "SelectAllValueOptions": Literal["ALL_VALUES"],
        "SourceParameterName": str,
        "SourceField": str,
        "SourceColumn": ColumnIdentifierTypeDef,
    },
    total=False,
)

DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": AdHocFilteringOptionTypeDef,
        "ExportToCSVOption": ExportToCSVOptionTypeDef,
        "SheetControlsOption": SheetControlsOptionTypeDef,
        "VisualPublishOptions": DashboardVisualPublishOptionsTypeDef,
        "SheetLayoutElementMaximizationOption": SheetLayoutElementMaximizationOptionTypeDef,
        "VisualMenuOption": VisualMenuOptionTypeDef,
        "VisualAxisSortOption": VisualAxisSortOptionTypeDef,
        "ExportWithHiddenFieldsOption": ExportWithHiddenFieldsOptionTypeDef,
        "DataPointDrillUpDownOption": DataPointDrillUpDownOptionTypeDef,
        "DataPointMenuLabelOption": DataPointMenuLabelOptionTypeDef,
        "DataPointTooltipOption": DataPointTooltipOptionTypeDef,
    },
    total=False,
)

VisualPaletteOutputTypeDef = TypedDict(
    "VisualPaletteOutputTypeDef",
    {
        "ChartColor": str,
        "ColorMap": List[DataPathColorTypeDef],
    },
    total=False,
)

VisualPaletteTypeDef = TypedDict(
    "VisualPaletteTypeDef",
    {
        "ChartColor": str,
        "ColorMap": Sequence[DataPathColorTypeDef],
    },
    total=False,
)

_RequiredPivotTableFieldCollapseStateOptionOutputTypeDef = TypedDict(
    "_RequiredPivotTableFieldCollapseStateOptionOutputTypeDef",
    {
        "Target": PivotTableFieldCollapseStateTargetOutputTypeDef,
    },
)
_OptionalPivotTableFieldCollapseStateOptionOutputTypeDef = TypedDict(
    "_OptionalPivotTableFieldCollapseStateOptionOutputTypeDef",
    {
        "State": PivotTableFieldCollapseStateType,
    },
    total=False,
)


class PivotTableFieldCollapseStateOptionOutputTypeDef(
    _RequiredPivotTableFieldCollapseStateOptionOutputTypeDef,
    _OptionalPivotTableFieldCollapseStateOptionOutputTypeDef,
):
    pass


_RequiredPivotTableFieldCollapseStateOptionTypeDef = TypedDict(
    "_RequiredPivotTableFieldCollapseStateOptionTypeDef",
    {
        "Target": PivotTableFieldCollapseStateTargetTypeDef,
    },
)
_OptionalPivotTableFieldCollapseStateOptionTypeDef = TypedDict(
    "_OptionalPivotTableFieldCollapseStateOptionTypeDef",
    {
        "State": PivotTableFieldCollapseStateType,
    },
    total=False,
)


class PivotTableFieldCollapseStateOptionTypeDef(
    _RequiredPivotTableFieldCollapseStateOptionTypeDef,
    _OptionalPivotTableFieldCollapseStateOptionTypeDef,
):
    pass


_RequiredTimeRangeFilterOutputTypeDef = TypedDict(
    "_RequiredTimeRangeFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalTimeRangeFilterOutputTypeDef = TypedDict(
    "_OptionalTimeRangeFilterOutputTypeDef",
    {
        "IncludeMinimum": bool,
        "IncludeMaximum": bool,
        "RangeMinimumValue": TimeRangeFilterValueOutputTypeDef,
        "RangeMaximumValue": TimeRangeFilterValueOutputTypeDef,
        "ExcludePeriodConfiguration": ExcludePeriodConfigurationTypeDef,
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)


class TimeRangeFilterOutputTypeDef(
    _RequiredTimeRangeFilterOutputTypeDef, _OptionalTimeRangeFilterOutputTypeDef
):
    pass


_RequiredTimeRangeFilterTypeDef = TypedDict(
    "_RequiredTimeRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalTimeRangeFilterTypeDef = TypedDict(
    "_OptionalTimeRangeFilterTypeDef",
    {
        "IncludeMinimum": bool,
        "IncludeMaximum": bool,
        "RangeMinimumValue": TimeRangeFilterValueTypeDef,
        "RangeMaximumValue": TimeRangeFilterValueTypeDef,
        "ExcludePeriodConfiguration": ExcludePeriodConfigurationTypeDef,
        "TimeGranularity": TimeGranularityType,
    },
    total=False,
)


class TimeRangeFilterTypeDef(_RequiredTimeRangeFilterTypeDef, _OptionalTimeRangeFilterTypeDef):
    pass


ListTopicRefreshSchedulesResponseTypeDef = TypedDict(
    "ListTopicRefreshSchedulesResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "RefreshSchedules": List[TopicRefreshScheduleSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DefaultFormattingTypeDef = TypedDict(
    "DefaultFormattingTypeDef",
    {
        "DisplayFormat": DisplayFormatType,
        "DisplayFormatOptions": DisplayFormatOptionsTypeDef,
    },
    total=False,
)

CustomActionFilterOperationOutputTypeDef = TypedDict(
    "CustomActionFilterOperationOutputTypeDef",
    {
        "SelectedFieldsConfiguration": FilterOperationSelectedFieldsConfigurationOutputTypeDef,
        "TargetVisualsConfiguration": FilterOperationTargetVisualsConfigurationOutputTypeDef,
    },
)

CustomActionFilterOperationTypeDef = TypedDict(
    "CustomActionFilterOperationTypeDef",
    {
        "SelectedFieldsConfiguration": FilterOperationSelectedFieldsConfigurationTypeDef,
        "TargetVisualsConfiguration": FilterOperationTargetVisualsConfigurationTypeDef,
    },
)

AxisLabelOptionsTypeDef = TypedDict(
    "AxisLabelOptionsTypeDef",
    {
        "FontConfiguration": FontConfigurationTypeDef,
        "CustomLabel": str,
        "ApplyTo": AxisLabelReferenceOptionsTypeDef,
    },
    total=False,
)

DataLabelOptionsOutputTypeDef = TypedDict(
    "DataLabelOptionsOutputTypeDef",
    {
        "Visibility": VisibilityType,
        "CategoryLabelVisibility": VisibilityType,
        "MeasureLabelVisibility": VisibilityType,
        "DataLabelTypes": List[DataLabelTypeTypeDef],
        "Position": DataLabelPositionType,
        "LabelContent": DataLabelContentType,
        "LabelFontConfiguration": FontConfigurationTypeDef,
        "LabelColor": str,
        "Overlap": DataLabelOverlapType,
        "TotalsVisibility": VisibilityType,
    },
    total=False,
)

DataLabelOptionsTypeDef = TypedDict(
    "DataLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "CategoryLabelVisibility": VisibilityType,
        "MeasureLabelVisibility": VisibilityType,
        "DataLabelTypes": Sequence[DataLabelTypeTypeDef],
        "Position": DataLabelPositionType,
        "LabelContent": DataLabelContentType,
        "LabelFontConfiguration": FontConfigurationTypeDef,
        "LabelColor": str,
        "Overlap": DataLabelOverlapType,
        "TotalsVisibility": VisibilityType,
    },
    total=False,
)

FunnelChartDataLabelOptionsTypeDef = TypedDict(
    "FunnelChartDataLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "CategoryLabelVisibility": VisibilityType,
        "MeasureLabelVisibility": VisibilityType,
        "Position": DataLabelPositionType,
        "LabelFontConfiguration": FontConfigurationTypeDef,
        "LabelColor": str,
        "MeasureDataLabelStyle": FunnelChartMeasureDataLabelStyleType,
    },
    total=False,
)

LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": FontConfigurationTypeDef,
        "CustomLabel": str,
    },
    total=False,
)

PanelTitleOptionsTypeDef = TypedDict(
    "PanelTitleOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": FontConfigurationTypeDef,
        "HorizontalTextAlignment": HorizontalTextAlignmentType,
    },
    total=False,
)

_RequiredTableFieldCustomTextContentTypeDef = TypedDict(
    "_RequiredTableFieldCustomTextContentTypeDef",
    {
        "FontConfiguration": FontConfigurationTypeDef,
    },
)
_OptionalTableFieldCustomTextContentTypeDef = TypedDict(
    "_OptionalTableFieldCustomTextContentTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TableFieldCustomTextContentTypeDef(
    _RequiredTableFieldCustomTextContentTypeDef, _OptionalTableFieldCustomTextContentTypeDef
):
    pass


ForecastConfigurationOutputTypeDef = TypedDict(
    "ForecastConfigurationOutputTypeDef",
    {
        "ForecastProperties": TimeBasedForecastPropertiesTypeDef,
        "Scenario": ForecastScenarioOutputTypeDef,
    },
    total=False,
)

ForecastConfigurationTypeDef = TypedDict(
    "ForecastConfigurationTypeDef",
    {
        "ForecastProperties": TimeBasedForecastPropertiesTypeDef,
        "Scenario": ForecastScenarioTypeDef,
    },
    total=False,
)

DefaultFreeFormLayoutConfigurationTypeDef = TypedDict(
    "DefaultFreeFormLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": FreeFormLayoutCanvasSizeOptionsTypeDef,
    },
)

SnapshotUserConfigurationTypeDef = TypedDict(
    "SnapshotUserConfigurationTypeDef",
    {
        "AnonymousUsers": Sequence[SnapshotAnonymousUserTypeDef],
    },
    total=False,
)

GeospatialHeatmapConfigurationOutputTypeDef = TypedDict(
    "GeospatialHeatmapConfigurationOutputTypeDef",
    {
        "HeatmapColor": GeospatialHeatmapColorScaleOutputTypeDef,
    },
    total=False,
)

GeospatialHeatmapConfigurationTypeDef = TypedDict(
    "GeospatialHeatmapConfigurationTypeDef",
    {
        "HeatmapColor": GeospatialHeatmapColorScaleTypeDef,
    },
    total=False,
)

GlobalTableBorderOptionsTypeDef = TypedDict(
    "GlobalTableBorderOptionsTypeDef",
    {
        "UniformBorder": TableBorderOptionsTypeDef,
        "SideSpecificBorder": TableSideBorderOptionsTypeDef,
    },
    total=False,
)

ConditionalFormattingGradientColorOutputTypeDef = TypedDict(
    "ConditionalFormattingGradientColorOutputTypeDef",
    {
        "Expression": str,
        "Color": GradientColorOutputTypeDef,
    },
)

ConditionalFormattingGradientColorTypeDef = TypedDict(
    "ConditionalFormattingGradientColorTypeDef",
    {
        "Expression": str,
        "Color": GradientColorTypeDef,
    },
)

DefaultGridLayoutConfigurationTypeDef = TypedDict(
    "DefaultGridLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": GridLayoutCanvasSizeOptionsTypeDef,
    },
)

_RequiredGridLayoutConfigurationOutputTypeDef = TypedDict(
    "_RequiredGridLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[GridLayoutElementTypeDef],
    },
)
_OptionalGridLayoutConfigurationOutputTypeDef = TypedDict(
    "_OptionalGridLayoutConfigurationOutputTypeDef",
    {
        "CanvasSizeOptions": GridLayoutCanvasSizeOptionsTypeDef,
    },
    total=False,
)


class GridLayoutConfigurationOutputTypeDef(
    _RequiredGridLayoutConfigurationOutputTypeDef, _OptionalGridLayoutConfigurationOutputTypeDef
):
    pass


_RequiredGridLayoutConfigurationTypeDef = TypedDict(
    "_RequiredGridLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[GridLayoutElementTypeDef],
    },
)
_OptionalGridLayoutConfigurationTypeDef = TypedDict(
    "_OptionalGridLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": GridLayoutCanvasSizeOptionsTypeDef,
    },
    total=False,
)


class GridLayoutConfigurationTypeDef(
    _RequiredGridLayoutConfigurationTypeDef, _OptionalGridLayoutConfigurationTypeDef
):
    pass


RefreshConfigurationTypeDef = TypedDict(
    "RefreshConfigurationTypeDef",
    {
        "IncrementalRefresh": IncrementalRefreshTypeDef,
    },
)

DescribeIngestionResponseTypeDef = TypedDict(
    "DescribeIngestionResponseTypeDef",
    {
        "Ingestion": IngestionTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "Ingestions": List[IngestionTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {
        "JoinInstruction": JoinInstructionTypeDef,
        "PhysicalTableId": str,
        "DataSetArn": str,
    },
    total=False,
)

_RequiredDataFieldSeriesItemTypeDef = TypedDict(
    "_RequiredDataFieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
    },
)
_OptionalDataFieldSeriesItemTypeDef = TypedDict(
    "_OptionalDataFieldSeriesItemTypeDef",
    {
        "FieldValue": str,
        "Settings": LineChartSeriesSettingsTypeDef,
    },
    total=False,
)


class DataFieldSeriesItemTypeDef(
    _RequiredDataFieldSeriesItemTypeDef, _OptionalDataFieldSeriesItemTypeDef
):
    pass


_RequiredFieldSeriesItemTypeDef = TypedDict(
    "_RequiredFieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
    },
)
_OptionalFieldSeriesItemTypeDef = TypedDict(
    "_OptionalFieldSeriesItemTypeDef",
    {
        "Settings": LineChartSeriesSettingsTypeDef,
    },
    total=False,
)


class FieldSeriesItemTypeDef(_RequiredFieldSeriesItemTypeDef, _OptionalFieldSeriesItemTypeDef):
    pass


DataSourceParametersTypeDef = TypedDict(
    "DataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": AmazonElasticsearchParametersTypeDef,
        "AthenaParameters": AthenaParametersTypeDef,
        "AuroraParameters": AuroraParametersTypeDef,
        "AuroraPostgreSqlParameters": AuroraPostgreSqlParametersTypeDef,
        "AwsIotAnalyticsParameters": AwsIotAnalyticsParametersTypeDef,
        "JiraParameters": JiraParametersTypeDef,
        "MariaDbParameters": MariaDbParametersTypeDef,
        "MySqlParameters": MySqlParametersTypeDef,
        "OracleParameters": OracleParametersTypeDef,
        "PostgreSqlParameters": PostgreSqlParametersTypeDef,
        "PrestoParameters": PrestoParametersTypeDef,
        "RdsParameters": RdsParametersTypeDef,
        "RedshiftParameters": RedshiftParametersTypeDef,
        "S3Parameters": S3ParametersTypeDef,
        "ServiceNowParameters": ServiceNowParametersTypeDef,
        "SnowflakeParameters": SnowflakeParametersTypeDef,
        "SparkParameters": SparkParametersTypeDef,
        "SqlServerParameters": SqlServerParametersTypeDef,
        "TeradataParameters": TeradataParametersTypeDef,
        "TwitterParameters": TwitterParametersTypeDef,
        "AmazonOpenSearchParameters": AmazonOpenSearchParametersTypeDef,
        "ExasolParameters": ExasolParametersTypeDef,
        "DatabricksParameters": DatabricksParametersTypeDef,
    },
    total=False,
)

SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {
        "Tile": TileStyleTypeDef,
        "TileLayout": TileLayoutStyleTypeDef,
    },
    total=False,
)

_RequiredTopicNamedEntityOutputTypeDef = TypedDict(
    "_RequiredTopicNamedEntityOutputTypeDef",
    {
        "EntityName": str,
    },
)
_OptionalTopicNamedEntityOutputTypeDef = TypedDict(
    "_OptionalTopicNamedEntityOutputTypeDef",
    {
        "EntityDescription": str,
        "EntitySynonyms": List[str],
        "SemanticEntityType": SemanticEntityTypeOutputTypeDef,
        "Definition": List[NamedEntityDefinitionOutputTypeDef],
    },
    total=False,
)


class TopicNamedEntityOutputTypeDef(
    _RequiredTopicNamedEntityOutputTypeDef, _OptionalTopicNamedEntityOutputTypeDef
):
    pass


_RequiredTopicNamedEntityTypeDef = TypedDict(
    "_RequiredTopicNamedEntityTypeDef",
    {
        "EntityName": str,
    },
)
_OptionalTopicNamedEntityTypeDef = TypedDict(
    "_OptionalTopicNamedEntityTypeDef",
    {
        "EntityDescription": str,
        "EntitySynonyms": Sequence[str],
        "SemanticEntityType": SemanticEntityTypeTypeDef,
        "Definition": Sequence[NamedEntityDefinitionTypeDef],
    },
    total=False,
)


class TopicNamedEntityTypeDef(_RequiredTopicNamedEntityTypeDef, _OptionalTopicNamedEntityTypeDef):
    pass


DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "Namespace": NamespaceInfoV2TypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List[NamespaceInfoV2TypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListVPCConnectionsResponseTypeDef = TypedDict(
    "ListVPCConnectionsResponseTypeDef",
    {
        "VPCConnectionSummaries": List[VPCConnectionSummaryTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeVPCConnectionResponseTypeDef = TypedDict(
    "DescribeVPCConnectionResponseTypeDef",
    {
        "VPCConnection": VPCConnectionTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CurrencyDisplayFormatConfigurationTypeDef = TypedDict(
    "CurrencyDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": NumericSeparatorConfigurationTypeDef,
        "Symbol": str,
        "DecimalPlacesConfiguration": DecimalPlacesConfigurationTypeDef,
        "NumberScale": NumberScaleType,
        "NegativeValueConfiguration": NegativeValueConfigurationTypeDef,
        "NullValueFormatConfiguration": NullValueFormatConfigurationTypeDef,
    },
    total=False,
)

NumberDisplayFormatConfigurationTypeDef = TypedDict(
    "NumberDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": NumericSeparatorConfigurationTypeDef,
        "DecimalPlacesConfiguration": DecimalPlacesConfigurationTypeDef,
        "NumberScale": NumberScaleType,
        "NegativeValueConfiguration": NegativeValueConfigurationTypeDef,
        "NullValueFormatConfiguration": NullValueFormatConfigurationTypeDef,
    },
    total=False,
)

PercentageDisplayFormatConfigurationTypeDef = TypedDict(
    "PercentageDisplayFormatConfigurationTypeDef",
    {
        "Prefix": str,
        "Suffix": str,
        "SeparatorConfiguration": NumericSeparatorConfigurationTypeDef,
        "DecimalPlacesConfiguration": DecimalPlacesConfigurationTypeDef,
        "NegativeValueConfiguration": NegativeValueConfigurationTypeDef,
        "NullValueFormatConfiguration": NullValueFormatConfigurationTypeDef,
    },
    total=False,
)

AggregationFunctionTypeDef = TypedDict(
    "AggregationFunctionTypeDef",
    {
        "NumericalAggregationFunction": NumericalAggregationFunctionTypeDef,
        "CategoricalAggregationFunction": CategoricalAggregationFunctionType,
        "DateAggregationFunction": DateAggregationFunctionType,
        "AttributeAggregationFunction": AttributeAggregationFunctionTypeDef,
    },
    total=False,
)

ScrollBarOptionsTypeDef = TypedDict(
    "ScrollBarOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "VisibleRange": VisibleRangeOptionsTypeDef,
    },
    total=False,
)

TopicDateRangeFilterTypeDef = TypedDict(
    "TopicDateRangeFilterTypeDef",
    {
        "Inclusive": bool,
        "Constant": TopicRangeFilterConstantTypeDef,
    },
    total=False,
)

TopicNumericRangeFilterTypeDef = TypedDict(
    "TopicNumericRangeFilterTypeDef",
    {
        "Inclusive": bool,
        "Constant": TopicRangeFilterConstantTypeDef,
        "Aggregation": NamedFilterAggTypeType,
    },
    total=False,
)

_RequiredRefreshScheduleOutputTypeDef = TypedDict(
    "_RequiredRefreshScheduleOutputTypeDef",
    {
        "ScheduleId": str,
        "ScheduleFrequency": RefreshFrequencyTypeDef,
        "RefreshType": IngestionTypeType,
    },
)
_OptionalRefreshScheduleOutputTypeDef = TypedDict(
    "_OptionalRefreshScheduleOutputTypeDef",
    {
        "StartAfterDateTime": datetime,
        "Arn": str,
    },
    total=False,
)


class RefreshScheduleOutputTypeDef(
    _RequiredRefreshScheduleOutputTypeDef, _OptionalRefreshScheduleOutputTypeDef
):
    pass


_RequiredRefreshScheduleTypeDef = TypedDict(
    "_RequiredRefreshScheduleTypeDef",
    {
        "ScheduleId": str,
        "ScheduleFrequency": RefreshFrequencyTypeDef,
        "RefreshType": IngestionTypeType,
    },
)
_OptionalRefreshScheduleTypeDef = TypedDict(
    "_OptionalRefreshScheduleTypeDef",
    {
        "StartAfterDateTime": Union[datetime, str],
        "Arn": str,
    },
    total=False,
)


class RefreshScheduleTypeDef(_RequiredRefreshScheduleTypeDef, _OptionalRefreshScheduleTypeDef):
    pass


RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    {
        "InitialPath": str,
        "FeatureConfigurations": RegisteredUserConsoleFeatureConfigurationsTypeDef,
    },
    total=False,
)

_RequiredRegisteredUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "_RequiredRegisteredUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
    },
)
_OptionalRegisteredUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "_OptionalRegisteredUserDashboardEmbeddingConfigurationTypeDef",
    {
        "FeatureConfigurations": RegisteredUserDashboardFeatureConfigurationsTypeDef,
    },
    total=False,
)


class RegisteredUserDashboardEmbeddingConfigurationTypeDef(
    _RequiredRegisteredUserDashboardEmbeddingConfigurationTypeDef,
    _OptionalRegisteredUserDashboardEmbeddingConfigurationTypeDef,
):
    pass


SnapshotDestinationConfigurationOutputTypeDef = TypedDict(
    "SnapshotDestinationConfigurationOutputTypeDef",
    {
        "S3Destinations": List[SnapshotS3DestinationConfigurationTypeDef],
    },
    total=False,
)

SnapshotDestinationConfigurationTypeDef = TypedDict(
    "SnapshotDestinationConfigurationTypeDef",
    {
        "S3Destinations": Sequence[SnapshotS3DestinationConfigurationTypeDef],
    },
    total=False,
)

SnapshotJobS3ResultTypeDef = TypedDict(
    "SnapshotJobS3ResultTypeDef",
    {
        "S3DestinationConfiguration": SnapshotS3DestinationConfigurationTypeDef,
        "S3Uri": str,
        "ErrorInfo": List[SnapshotJobResultErrorInfoTypeDef],
    },
    total=False,
)

PhysicalTableOutputTypeDef = TypedDict(
    "PhysicalTableOutputTypeDef",
    {
        "RelationalTable": RelationalTableOutputTypeDef,
        "CustomSql": CustomSqlOutputTypeDef,
        "S3Source": S3SourceOutputTypeDef,
    },
    total=False,
)

PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": RelationalTableTypeDef,
        "CustomSql": CustomSqlTypeDef,
        "S3Source": S3SourceTypeDef,
    },
    total=False,
)

SectionBasedLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    {
        "PaperCanvasSizeOptions": SectionBasedLayoutPaperCanvasSizeOptionsTypeDef,
    },
    total=False,
)

FilterScopeConfigurationOutputTypeDef = TypedDict(
    "FilterScopeConfigurationOutputTypeDef",
    {
        "SelectedSheets": SelectedSheetsFilterScopeConfigurationOutputTypeDef,
    },
    total=False,
)

FilterScopeConfigurationTypeDef = TypedDict(
    "FilterScopeConfigurationTypeDef",
    {
        "SelectedSheets": SelectedSheetsFilterScopeConfigurationTypeDef,
    },
    total=False,
)

_RequiredFreeFormLayoutElementOutputTypeDef = TypedDict(
    "_RequiredFreeFormLayoutElementOutputTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "XAxisLocation": str,
        "YAxisLocation": str,
        "Width": str,
        "Height": str,
    },
)
_OptionalFreeFormLayoutElementOutputTypeDef = TypedDict(
    "_OptionalFreeFormLayoutElementOutputTypeDef",
    {
        "Visibility": VisibilityType,
        "RenderingRules": List[SheetElementRenderingRuleTypeDef],
        "BorderStyle": FreeFormLayoutElementBorderStyleTypeDef,
        "SelectedBorderStyle": FreeFormLayoutElementBorderStyleTypeDef,
        "BackgroundStyle": FreeFormLayoutElementBackgroundStyleTypeDef,
        "LoadingAnimation": LoadingAnimationTypeDef,
    },
    total=False,
)


class FreeFormLayoutElementOutputTypeDef(
    _RequiredFreeFormLayoutElementOutputTypeDef, _OptionalFreeFormLayoutElementOutputTypeDef
):
    pass


_RequiredFreeFormLayoutElementTypeDef = TypedDict(
    "_RequiredFreeFormLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "XAxisLocation": str,
        "YAxisLocation": str,
        "Width": str,
        "Height": str,
    },
)
_OptionalFreeFormLayoutElementTypeDef = TypedDict(
    "_OptionalFreeFormLayoutElementTypeDef",
    {
        "Visibility": VisibilityType,
        "RenderingRules": Sequence[SheetElementRenderingRuleTypeDef],
        "BorderStyle": FreeFormLayoutElementBorderStyleTypeDef,
        "SelectedBorderStyle": FreeFormLayoutElementBorderStyleTypeDef,
        "BackgroundStyle": FreeFormLayoutElementBackgroundStyleTypeDef,
        "LoadingAnimation": LoadingAnimationTypeDef,
    },
    total=False,
)


class FreeFormLayoutElementTypeDef(
    _RequiredFreeFormLayoutElementTypeDef, _OptionalFreeFormLayoutElementTypeDef
):
    pass


SnapshotFileGroupOutputTypeDef = TypedDict(
    "SnapshotFileGroupOutputTypeDef",
    {
        "Files": List[SnapshotFileOutputTypeDef],
    },
    total=False,
)

SnapshotFileGroupTypeDef = TypedDict(
    "SnapshotFileGroupTypeDef",
    {
        "Files": Sequence[SnapshotFileTypeDef],
    },
    total=False,
)

DatasetParameterOutputTypeDef = TypedDict(
    "DatasetParameterOutputTypeDef",
    {
        "StringDatasetParameter": StringDatasetParameterOutputTypeDef,
        "DecimalDatasetParameter": DecimalDatasetParameterOutputTypeDef,
        "IntegerDatasetParameter": IntegerDatasetParameterOutputTypeDef,
        "DateTimeDatasetParameter": DateTimeDatasetParameterOutputTypeDef,
    },
    total=False,
)

DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "StringDatasetParameter": StringDatasetParameterTypeDef,
        "DecimalDatasetParameter": DecimalDatasetParameterTypeDef,
        "IntegerDatasetParameter": IntegerDatasetParameterTypeDef,
        "DateTimeDatasetParameter": DateTimeDatasetParameterTypeDef,
    },
    total=False,
)

_RequiredDateTimeParameterDeclarationOutputTypeDef = TypedDict(
    "_RequiredDateTimeParameterDeclarationOutputTypeDef",
    {
        "Name": str,
    },
)
_OptionalDateTimeParameterDeclarationOutputTypeDef = TypedDict(
    "_OptionalDateTimeParameterDeclarationOutputTypeDef",
    {
        "DefaultValues": DateTimeDefaultValuesOutputTypeDef,
        "TimeGranularity": TimeGranularityType,
        "ValueWhenUnset": DateTimeValueWhenUnsetConfigurationOutputTypeDef,
        "MappedDataSetParameters": List[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class DateTimeParameterDeclarationOutputTypeDef(
    _RequiredDateTimeParameterDeclarationOutputTypeDef,
    _OptionalDateTimeParameterDeclarationOutputTypeDef,
):
    pass


_RequiredDateTimeParameterDeclarationTypeDef = TypedDict(
    "_RequiredDateTimeParameterDeclarationTypeDef",
    {
        "Name": str,
    },
)
_OptionalDateTimeParameterDeclarationTypeDef = TypedDict(
    "_OptionalDateTimeParameterDeclarationTypeDef",
    {
        "DefaultValues": DateTimeDefaultValuesTypeDef,
        "TimeGranularity": TimeGranularityType,
        "ValueWhenUnset": DateTimeValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": Sequence[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class DateTimeParameterDeclarationTypeDef(
    _RequiredDateTimeParameterDeclarationTypeDef, _OptionalDateTimeParameterDeclarationTypeDef
):
    pass


_RequiredDecimalParameterDeclarationOutputTypeDef = TypedDict(
    "_RequiredDecimalParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalDecimalParameterDeclarationOutputTypeDef = TypedDict(
    "_OptionalDecimalParameterDeclarationOutputTypeDef",
    {
        "DefaultValues": DecimalDefaultValuesOutputTypeDef,
        "ValueWhenUnset": DecimalValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": List[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class DecimalParameterDeclarationOutputTypeDef(
    _RequiredDecimalParameterDeclarationOutputTypeDef,
    _OptionalDecimalParameterDeclarationOutputTypeDef,
):
    pass


_RequiredDecimalParameterDeclarationTypeDef = TypedDict(
    "_RequiredDecimalParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalDecimalParameterDeclarationTypeDef = TypedDict(
    "_OptionalDecimalParameterDeclarationTypeDef",
    {
        "DefaultValues": DecimalDefaultValuesTypeDef,
        "ValueWhenUnset": DecimalValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": Sequence[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class DecimalParameterDeclarationTypeDef(
    _RequiredDecimalParameterDeclarationTypeDef, _OptionalDecimalParameterDeclarationTypeDef
):
    pass


_RequiredIntegerParameterDeclarationOutputTypeDef = TypedDict(
    "_RequiredIntegerParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalIntegerParameterDeclarationOutputTypeDef = TypedDict(
    "_OptionalIntegerParameterDeclarationOutputTypeDef",
    {
        "DefaultValues": IntegerDefaultValuesOutputTypeDef,
        "ValueWhenUnset": IntegerValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": List[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class IntegerParameterDeclarationOutputTypeDef(
    _RequiredIntegerParameterDeclarationOutputTypeDef,
    _OptionalIntegerParameterDeclarationOutputTypeDef,
):
    pass


_RequiredIntegerParameterDeclarationTypeDef = TypedDict(
    "_RequiredIntegerParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalIntegerParameterDeclarationTypeDef = TypedDict(
    "_OptionalIntegerParameterDeclarationTypeDef",
    {
        "DefaultValues": IntegerDefaultValuesTypeDef,
        "ValueWhenUnset": IntegerValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": Sequence[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class IntegerParameterDeclarationTypeDef(
    _RequiredIntegerParameterDeclarationTypeDef, _OptionalIntegerParameterDeclarationTypeDef
):
    pass


_RequiredStringParameterDeclarationOutputTypeDef = TypedDict(
    "_RequiredStringParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalStringParameterDeclarationOutputTypeDef = TypedDict(
    "_OptionalStringParameterDeclarationOutputTypeDef",
    {
        "DefaultValues": StringDefaultValuesOutputTypeDef,
        "ValueWhenUnset": StringValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": List[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class StringParameterDeclarationOutputTypeDef(
    _RequiredStringParameterDeclarationOutputTypeDef,
    _OptionalStringParameterDeclarationOutputTypeDef,
):
    pass


_RequiredStringParameterDeclarationTypeDef = TypedDict(
    "_RequiredStringParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
    },
)
_OptionalStringParameterDeclarationTypeDef = TypedDict(
    "_OptionalStringParameterDeclarationTypeDef",
    {
        "DefaultValues": StringDefaultValuesTypeDef,
        "ValueWhenUnset": StringValueWhenUnsetConfigurationTypeDef,
        "MappedDataSetParameters": Sequence[MappedDataSetParameterTypeDef],
    },
    total=False,
)


class StringParameterDeclarationTypeDef(
    _RequiredStringParameterDeclarationTypeDef, _OptionalStringParameterDeclarationTypeDef
):
    pass


_RequiredDateTimeHierarchyOutputTypeDef = TypedDict(
    "_RequiredDateTimeHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
    },
)
_OptionalDateTimeHierarchyOutputTypeDef = TypedDict(
    "_OptionalDateTimeHierarchyOutputTypeDef",
    {
        "DrillDownFilters": List[DrillDownFilterOutputTypeDef],
    },
    total=False,
)


class DateTimeHierarchyOutputTypeDef(
    _RequiredDateTimeHierarchyOutputTypeDef, _OptionalDateTimeHierarchyOutputTypeDef
):
    pass


_RequiredExplicitHierarchyOutputTypeDef = TypedDict(
    "_RequiredExplicitHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
        "Columns": List[ColumnIdentifierTypeDef],
    },
)
_OptionalExplicitHierarchyOutputTypeDef = TypedDict(
    "_OptionalExplicitHierarchyOutputTypeDef",
    {
        "DrillDownFilters": List[DrillDownFilterOutputTypeDef],
    },
    total=False,
)


class ExplicitHierarchyOutputTypeDef(
    _RequiredExplicitHierarchyOutputTypeDef, _OptionalExplicitHierarchyOutputTypeDef
):
    pass


_RequiredPredefinedHierarchyOutputTypeDef = TypedDict(
    "_RequiredPredefinedHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
        "Columns": List[ColumnIdentifierTypeDef],
    },
)
_OptionalPredefinedHierarchyOutputTypeDef = TypedDict(
    "_OptionalPredefinedHierarchyOutputTypeDef",
    {
        "DrillDownFilters": List[DrillDownFilterOutputTypeDef],
    },
    total=False,
)


class PredefinedHierarchyOutputTypeDef(
    _RequiredPredefinedHierarchyOutputTypeDef, _OptionalPredefinedHierarchyOutputTypeDef
):
    pass


_RequiredDateTimeHierarchyTypeDef = TypedDict(
    "_RequiredDateTimeHierarchyTypeDef",
    {
        "HierarchyId": str,
    },
)
_OptionalDateTimeHierarchyTypeDef = TypedDict(
    "_OptionalDateTimeHierarchyTypeDef",
    {
        "DrillDownFilters": Sequence[DrillDownFilterTypeDef],
    },
    total=False,
)


class DateTimeHierarchyTypeDef(
    _RequiredDateTimeHierarchyTypeDef, _OptionalDateTimeHierarchyTypeDef
):
    pass


_RequiredExplicitHierarchyTypeDef = TypedDict(
    "_RequiredExplicitHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": Sequence[ColumnIdentifierTypeDef],
    },
)
_OptionalExplicitHierarchyTypeDef = TypedDict(
    "_OptionalExplicitHierarchyTypeDef",
    {
        "DrillDownFilters": Sequence[DrillDownFilterTypeDef],
    },
    total=False,
)


class ExplicitHierarchyTypeDef(
    _RequiredExplicitHierarchyTypeDef, _OptionalExplicitHierarchyTypeDef
):
    pass


_RequiredPredefinedHierarchyTypeDef = TypedDict(
    "_RequiredPredefinedHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": Sequence[ColumnIdentifierTypeDef],
    },
)
_OptionalPredefinedHierarchyTypeDef = TypedDict(
    "_OptionalPredefinedHierarchyTypeDef",
    {
        "DrillDownFilters": Sequence[DrillDownFilterTypeDef],
    },
    total=False,
)


class PredefinedHierarchyTypeDef(
    _RequiredPredefinedHierarchyTypeDef, _OptionalPredefinedHierarchyTypeDef
):
    pass


DescribeAnalysisResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseTypeDef",
    {
        "Analysis": AnalysisTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DashboardTypeDef = TypedDict(
    "DashboardTypeDef",
    {
        "DashboardId": str,
        "Arn": str,
        "Name": str,
        "Version": DashboardVersionTypeDef,
        "CreatedTime": datetime,
        "LastPublishedTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AuthorizedResourceArns": Sequence[str],
        "ExperienceConfiguration": AnonymousUserEmbeddingExperienceConfigurationTypeDef,
    },
)
_OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "SessionTags": Sequence[SessionTagTypeDef],
        "AllowedDomains": Sequence[str],
    },
    total=False,
)


class GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef(
    _RequiredGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef,
    _OptionalGenerateEmbedUrlForAnonymousUserRequestRequestTypeDef,
):
    pass


AxisDataOptionsOutputTypeDef = TypedDict(
    "AxisDataOptionsOutputTypeDef",
    {
        "NumericAxisOptions": NumericAxisOptionsOutputTypeDef,
        "DateAxisOptions": DateAxisOptionsTypeDef,
    },
    total=False,
)

AxisDataOptionsTypeDef = TypedDict(
    "AxisDataOptionsTypeDef",
    {
        "NumericAxisOptions": NumericAxisOptionsTypeDef,
        "DateAxisOptions": DateAxisOptionsTypeDef,
    },
    total=False,
)

TransformOperationOutputTypeDef = TypedDict(
    "TransformOperationOutputTypeDef",
    {
        "ProjectOperation": ProjectOperationOutputTypeDef,
        "FilterOperation": FilterOperationTypeDef,
        "CreateColumnsOperation": CreateColumnsOperationOutputTypeDef,
        "RenameColumnOperation": RenameColumnOperationTypeDef,
        "CastColumnTypeOperation": CastColumnTypeOperationTypeDef,
        "TagColumnOperation": TagColumnOperationOutputTypeDef,
        "UntagColumnOperation": UntagColumnOperationOutputTypeDef,
        "OverrideDatasetParameterOperation": OverrideDatasetParameterOperationOutputTypeDef,
    },
    total=False,
)

TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": ProjectOperationTypeDef,
        "FilterOperation": FilterOperationTypeDef,
        "CreateColumnsOperation": CreateColumnsOperationTypeDef,
        "RenameColumnOperation": RenameColumnOperationTypeDef,
        "CastColumnTypeOperation": CastColumnTypeOperationTypeDef,
        "TagColumnOperation": TagColumnOperationTypeDef,
        "UntagColumnOperation": UntagColumnOperationTypeDef,
        "OverrideDatasetParameterOperation": OverrideDatasetParameterOperationTypeDef,
    },
    total=False,
)

TemplateVersionTypeDef = TypedDict(
    "TemplateVersionTypeDef",
    {
        "CreatedTime": datetime,
        "Errors": List[TemplateErrorTypeDef],
        "VersionNumber": int,
        "Status": ResourceStatusType,
        "DataSetConfigurations": List[DataSetConfigurationOutputTypeDef],
        "Description": str,
        "SourceEntityArn": str,
        "ThemeArn": str,
        "Sheets": List[SheetTypeDef],
    },
    total=False,
)

SetParameterValueConfigurationOutputTypeDef = TypedDict(
    "SetParameterValueConfigurationOutputTypeDef",
    {
        "DestinationParameterName": str,
        "Value": DestinationParameterValueConfigurationOutputTypeDef,
    },
)

SetParameterValueConfigurationTypeDef = TypedDict(
    "SetParameterValueConfigurationTypeDef",
    {
        "DestinationParameterName": str,
        "Value": DestinationParameterValueConfigurationTypeDef,
    },
)

PivotTableFieldOptionsOutputTypeDef = TypedDict(
    "PivotTableFieldOptionsOutputTypeDef",
    {
        "SelectedFieldOptions": List[PivotTableFieldOptionTypeDef],
        "DataPathOptions": List[PivotTableDataPathOptionOutputTypeDef],
        "CollapseStateOptions": List[PivotTableFieldCollapseStateOptionOutputTypeDef],
    },
    total=False,
)

PivotTableFieldOptionsTypeDef = TypedDict(
    "PivotTableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": Sequence[PivotTableFieldOptionTypeDef],
        "DataPathOptions": Sequence[PivotTableDataPathOptionTypeDef],
        "CollapseStateOptions": Sequence[PivotTableFieldCollapseStateOptionTypeDef],
    },
    total=False,
)

_RequiredTopicCalculatedFieldOutputTypeDef = TypedDict(
    "_RequiredTopicCalculatedFieldOutputTypeDef",
    {
        "CalculatedFieldName": str,
        "Expression": str,
    },
)
_OptionalTopicCalculatedFieldOutputTypeDef = TypedDict(
    "_OptionalTopicCalculatedFieldOutputTypeDef",
    {
        "CalculatedFieldDescription": str,
        "CalculatedFieldSynonyms": List[str],
        "IsIncludedInTopic": bool,
        "DisableIndexing": bool,
        "ColumnDataRole": ColumnDataRoleType,
        "TimeGranularity": TopicTimeGranularityType,
        "DefaultFormatting": DefaultFormattingTypeDef,
        "Aggregation": DefaultAggregationType,
        "ComparativeOrder": ComparativeOrderOutputTypeDef,
        "SemanticType": SemanticTypeOutputTypeDef,
        "AllowedAggregations": List[AuthorSpecifiedAggregationType],
        "NotAllowedAggregations": List[AuthorSpecifiedAggregationType],
        "NeverAggregateInFilter": bool,
        "CellValueSynonyms": List[CellValueSynonymOutputTypeDef],
    },
    total=False,
)


class TopicCalculatedFieldOutputTypeDef(
    _RequiredTopicCalculatedFieldOutputTypeDef, _OptionalTopicCalculatedFieldOutputTypeDef
):
    pass


_RequiredTopicCalculatedFieldTypeDef = TypedDict(
    "_RequiredTopicCalculatedFieldTypeDef",
    {
        "CalculatedFieldName": str,
        "Expression": str,
    },
)
_OptionalTopicCalculatedFieldTypeDef = TypedDict(
    "_OptionalTopicCalculatedFieldTypeDef",
    {
        "CalculatedFieldDescription": str,
        "CalculatedFieldSynonyms": Sequence[str],
        "IsIncludedInTopic": bool,
        "DisableIndexing": bool,
        "ColumnDataRole": ColumnDataRoleType,
        "TimeGranularity": TopicTimeGranularityType,
        "DefaultFormatting": DefaultFormattingTypeDef,
        "Aggregation": DefaultAggregationType,
        "ComparativeOrder": ComparativeOrderTypeDef,
        "SemanticType": SemanticTypeTypeDef,
        "AllowedAggregations": Sequence[AuthorSpecifiedAggregationType],
        "NotAllowedAggregations": Sequence[AuthorSpecifiedAggregationType],
        "NeverAggregateInFilter": bool,
        "CellValueSynonyms": Sequence[CellValueSynonymTypeDef],
    },
    total=False,
)


class TopicCalculatedFieldTypeDef(
    _RequiredTopicCalculatedFieldTypeDef, _OptionalTopicCalculatedFieldTypeDef
):
    pass


_RequiredTopicColumnOutputTypeDef = TypedDict(
    "_RequiredTopicColumnOutputTypeDef",
    {
        "ColumnName": str,
    },
)
_OptionalTopicColumnOutputTypeDef = TypedDict(
    "_OptionalTopicColumnOutputTypeDef",
    {
        "ColumnFriendlyName": str,
        "ColumnDescription": str,
        "ColumnSynonyms": List[str],
        "ColumnDataRole": ColumnDataRoleType,
        "Aggregation": DefaultAggregationType,
        "IsIncludedInTopic": bool,
        "DisableIndexing": bool,
        "ComparativeOrder": ComparativeOrderOutputTypeDef,
        "SemanticType": SemanticTypeOutputTypeDef,
        "TimeGranularity": TopicTimeGranularityType,
        "AllowedAggregations": List[AuthorSpecifiedAggregationType],
        "NotAllowedAggregations": List[AuthorSpecifiedAggregationType],
        "DefaultFormatting": DefaultFormattingTypeDef,
        "NeverAggregateInFilter": bool,
        "CellValueSynonyms": List[CellValueSynonymOutputTypeDef],
    },
    total=False,
)


class TopicColumnOutputTypeDef(
    _RequiredTopicColumnOutputTypeDef, _OptionalTopicColumnOutputTypeDef
):
    pass


_RequiredTopicColumnTypeDef = TypedDict(
    "_RequiredTopicColumnTypeDef",
    {
        "ColumnName": str,
    },
)
_OptionalTopicColumnTypeDef = TypedDict(
    "_OptionalTopicColumnTypeDef",
    {
        "ColumnFriendlyName": str,
        "ColumnDescription": str,
        "ColumnSynonyms": Sequence[str],
        "ColumnDataRole": ColumnDataRoleType,
        "Aggregation": DefaultAggregationType,
        "IsIncludedInTopic": bool,
        "DisableIndexing": bool,
        "ComparativeOrder": ComparativeOrderTypeDef,
        "SemanticType": SemanticTypeTypeDef,
        "TimeGranularity": TopicTimeGranularityType,
        "AllowedAggregations": Sequence[AuthorSpecifiedAggregationType],
        "NotAllowedAggregations": Sequence[AuthorSpecifiedAggregationType],
        "DefaultFormatting": DefaultFormattingTypeDef,
        "NeverAggregateInFilter": bool,
        "CellValueSynonyms": Sequence[CellValueSynonymTypeDef],
    },
    total=False,
)


class TopicColumnTypeDef(_RequiredTopicColumnTypeDef, _OptionalTopicColumnTypeDef):
    pass


ChartAxisLabelOptionsOutputTypeDef = TypedDict(
    "ChartAxisLabelOptionsOutputTypeDef",
    {
        "Visibility": VisibilityType,
        "SortIconVisibility": VisibilityType,
        "AxisLabelOptions": List[AxisLabelOptionsTypeDef],
    },
    total=False,
)

ChartAxisLabelOptionsTypeDef = TypedDict(
    "ChartAxisLabelOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "SortIconVisibility": VisibilityType,
        "AxisLabelOptions": Sequence[AxisLabelOptionsTypeDef],
    },
    total=False,
)

AxisTickLabelOptionsTypeDef = TypedDict(
    "AxisTickLabelOptionsTypeDef",
    {
        "LabelOptions": LabelOptionsTypeDef,
        "RotationAngle": float,
    },
    total=False,
)

DateTimePickerControlDisplayOptionsTypeDef = TypedDict(
    "DateTimePickerControlDisplayOptionsTypeDef",
    {
        "TitleOptions": LabelOptionsTypeDef,
        "DateTimeFormat": str,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

DropDownControlDisplayOptionsTypeDef = TypedDict(
    "DropDownControlDisplayOptionsTypeDef",
    {
        "SelectAllOptions": ListControlSelectAllOptionsTypeDef,
        "TitleOptions": LabelOptionsTypeDef,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

LegendOptionsTypeDef = TypedDict(
    "LegendOptionsTypeDef",
    {
        "Visibility": VisibilityType,
        "Title": LabelOptionsTypeDef,
        "Position": LegendPositionType,
        "Width": str,
        "Height": str,
    },
    total=False,
)

ListControlDisplayOptionsTypeDef = TypedDict(
    "ListControlDisplayOptionsTypeDef",
    {
        "SearchOptions": ListControlSearchOptionsTypeDef,
        "SelectAllOptions": ListControlSelectAllOptionsTypeDef,
        "TitleOptions": LabelOptionsTypeDef,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

RelativeDateTimeControlDisplayOptionsTypeDef = TypedDict(
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    {
        "TitleOptions": LabelOptionsTypeDef,
        "DateTimeFormat": str,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

SliderControlDisplayOptionsTypeDef = TypedDict(
    "SliderControlDisplayOptionsTypeDef",
    {
        "TitleOptions": LabelOptionsTypeDef,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

TextAreaControlDisplayOptionsTypeDef = TypedDict(
    "TextAreaControlDisplayOptionsTypeDef",
    {
        "TitleOptions": LabelOptionsTypeDef,
        "PlaceholderOptions": TextControlPlaceholderOptionsTypeDef,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

TextFieldControlDisplayOptionsTypeDef = TypedDict(
    "TextFieldControlDisplayOptionsTypeDef",
    {
        "TitleOptions": LabelOptionsTypeDef,
        "PlaceholderOptions": TextControlPlaceholderOptionsTypeDef,
        "InfoIconLabelOptions": SheetControlInfoIconLabelOptionsTypeDef,
    },
    total=False,
)

PanelConfigurationTypeDef = TypedDict(
    "PanelConfigurationTypeDef",
    {
        "Title": PanelTitleOptionsTypeDef,
        "BorderVisibility": VisibilityType,
        "BorderThickness": str,
        "BorderStyle": PanelBorderStyleType,
        "BorderColor": str,
        "GutterVisibility": VisibilityType,
        "GutterSpacing": str,
        "BackgroundVisibility": VisibilityType,
        "BackgroundColor": str,
    },
    total=False,
)

TableFieldLinkContentConfigurationTypeDef = TypedDict(
    "TableFieldLinkContentConfigurationTypeDef",
    {
        "CustomTextContent": TableFieldCustomTextContentTypeDef,
        "CustomIconContent": TableFieldCustomIconContentTypeDef,
    },
    total=False,
)

GeospatialPointStyleOptionsOutputTypeDef = TypedDict(
    "GeospatialPointStyleOptionsOutputTypeDef",
    {
        "SelectedPointStyle": GeospatialSelectedPointStyleType,
        "ClusterMarkerConfiguration": ClusterMarkerConfigurationTypeDef,
        "HeatmapConfiguration": GeospatialHeatmapConfigurationOutputTypeDef,
    },
    total=False,
)

GeospatialPointStyleOptionsTypeDef = TypedDict(
    "GeospatialPointStyleOptionsTypeDef",
    {
        "SelectedPointStyle": GeospatialSelectedPointStyleType,
        "ClusterMarkerConfiguration": ClusterMarkerConfigurationTypeDef,
        "HeatmapConfiguration": GeospatialHeatmapConfigurationTypeDef,
    },
    total=False,
)

TableCellStyleTypeDef = TypedDict(
    "TableCellStyleTypeDef",
    {
        "Visibility": VisibilityType,
        "FontConfiguration": FontConfigurationTypeDef,
        "TextWrap": TextWrapType,
        "HorizontalTextAlignment": HorizontalTextAlignmentType,
        "VerticalTextAlignment": VerticalTextAlignmentType,
        "BackgroundColor": str,
        "Height": int,
        "Border": GlobalTableBorderOptionsTypeDef,
    },
    total=False,
)

ConditionalFormattingColorOutputTypeDef = TypedDict(
    "ConditionalFormattingColorOutputTypeDef",
    {
        "Solid": ConditionalFormattingSolidColorTypeDef,
        "Gradient": ConditionalFormattingGradientColorOutputTypeDef,
    },
    total=False,
)

ConditionalFormattingColorTypeDef = TypedDict(
    "ConditionalFormattingColorTypeDef",
    {
        "Solid": ConditionalFormattingSolidColorTypeDef,
        "Gradient": ConditionalFormattingGradientColorTypeDef,
    },
    total=False,
)

DefaultInteractiveLayoutConfigurationTypeDef = TypedDict(
    "DefaultInteractiveLayoutConfigurationTypeDef",
    {
        "Grid": DefaultGridLayoutConfigurationTypeDef,
        "FreeForm": DefaultFreeFormLayoutConfigurationTypeDef,
    },
    total=False,
)

SheetControlLayoutConfigurationOutputTypeDef = TypedDict(
    "SheetControlLayoutConfigurationOutputTypeDef",
    {
        "GridLayout": GridLayoutConfigurationOutputTypeDef,
    },
    total=False,
)

SheetControlLayoutConfigurationTypeDef = TypedDict(
    "SheetControlLayoutConfigurationTypeDef",
    {
        "GridLayout": GridLayoutConfigurationTypeDef,
    },
    total=False,
)

DataSetRefreshPropertiesTypeDef = TypedDict(
    "DataSetRefreshPropertiesTypeDef",
    {
        "RefreshConfiguration": RefreshConfigurationTypeDef,
    },
)

SeriesItemTypeDef = TypedDict(
    "SeriesItemTypeDef",
    {
        "FieldSeriesItem": FieldSeriesItemTypeDef,
        "DataFieldSeriesItem": DataFieldSeriesItemTypeDef,
    },
    total=False,
)

_RequiredAssetBundleImportJobDataSourceOverrideParametersTypeDef = TypedDict(
    "_RequiredAssetBundleImportJobDataSourceOverrideParametersTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalAssetBundleImportJobDataSourceOverrideParametersTypeDef = TypedDict(
    "_OptionalAssetBundleImportJobDataSourceOverrideParametersTypeDef",
    {
        "Name": str,
        "DataSourceParameters": DataSourceParametersTypeDef,
        "VpcConnectionProperties": VpcConnectionPropertiesTypeDef,
        "SslProperties": SslPropertiesTypeDef,
        "Credentials": AssetBundleImportJobDataSourceCredentialsTypeDef,
    },
    total=False,
)


class AssetBundleImportJobDataSourceOverrideParametersTypeDef(
    _RequiredAssetBundleImportJobDataSourceOverrideParametersTypeDef,
    _OptionalAssetBundleImportJobDataSourceOverrideParametersTypeDef,
):
    pass


_RequiredCredentialPairTypeDef = TypedDict(
    "_RequiredCredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
_OptionalCredentialPairTypeDef = TypedDict(
    "_OptionalCredentialPairTypeDef",
    {
        "AlternateDataSourceParameters": Sequence[DataSourceParametersTypeDef],
    },
    total=False,
)


class CredentialPairTypeDef(_RequiredCredentialPairTypeDef, _OptionalCredentialPairTypeDef):
    pass


DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Status": ResourceStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "DataSourceParameters": DataSourceParametersTypeDef,
        "AlternateDataSourceParameters": List[DataSourceParametersTypeDef],
        "VpcConnectionProperties": VpcConnectionPropertiesTypeDef,
        "SslProperties": SslPropertiesTypeDef,
        "ErrorInfo": DataSourceErrorInfoTypeDef,
        "SecretArn": str,
    },
    total=False,
)

ThemeConfigurationOutputTypeDef = TypedDict(
    "ThemeConfigurationOutputTypeDef",
    {
        "DataColorPalette": DataColorPaletteOutputTypeDef,
        "UIColorPalette": UIColorPaletteTypeDef,
        "Sheet": SheetStyleTypeDef,
        "Typography": TypographyOutputTypeDef,
    },
    total=False,
)

ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": DataColorPaletteTypeDef,
        "UIColorPalette": UIColorPaletteTypeDef,
        "Sheet": SheetStyleTypeDef,
        "Typography": TypographyTypeDef,
    },
    total=False,
)

ComparisonFormatConfigurationTypeDef = TypedDict(
    "ComparisonFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": NumberDisplayFormatConfigurationTypeDef,
        "PercentageDisplayFormatConfiguration": PercentageDisplayFormatConfigurationTypeDef,
    },
    total=False,
)

NumericFormatConfigurationTypeDef = TypedDict(
    "NumericFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": NumberDisplayFormatConfigurationTypeDef,
        "CurrencyDisplayFormatConfiguration": CurrencyDisplayFormatConfigurationTypeDef,
        "PercentageDisplayFormatConfiguration": PercentageDisplayFormatConfigurationTypeDef,
    },
    total=False,
)

_RequiredAggregationSortConfigurationTypeDef = TypedDict(
    "_RequiredAggregationSortConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "SortDirection": SortDirectionType,
    },
)
_OptionalAggregationSortConfigurationTypeDef = TypedDict(
    "_OptionalAggregationSortConfigurationTypeDef",
    {
        "AggregationFunction": AggregationFunctionTypeDef,
    },
    total=False,
)


class AggregationSortConfigurationTypeDef(
    _RequiredAggregationSortConfigurationTypeDef, _OptionalAggregationSortConfigurationTypeDef
):
    pass


_RequiredColumnSortTypeDef = TypedDict(
    "_RequiredColumnSortTypeDef",
    {
        "SortBy": ColumnIdentifierTypeDef,
        "Direction": SortDirectionType,
    },
)
_OptionalColumnSortTypeDef = TypedDict(
    "_OptionalColumnSortTypeDef",
    {
        "AggregationFunction": AggregationFunctionTypeDef,
    },
    total=False,
)


class ColumnSortTypeDef(_RequiredColumnSortTypeDef, _OptionalColumnSortTypeDef):
    pass


_RequiredColumnTooltipItemTypeDef = TypedDict(
    "_RequiredColumnTooltipItemTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalColumnTooltipItemTypeDef = TypedDict(
    "_OptionalColumnTooltipItemTypeDef",
    {
        "Label": str,
        "Visibility": VisibilityType,
        "Aggregation": AggregationFunctionTypeDef,
    },
    total=False,
)


class ColumnTooltipItemTypeDef(
    _RequiredColumnTooltipItemTypeDef, _OptionalColumnTooltipItemTypeDef
):
    pass


_RequiredNumericEqualityFilterTypeDef = TypedDict(
    "_RequiredNumericEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "MatchOperator": NumericEqualityMatchOperatorType,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalNumericEqualityFilterTypeDef = TypedDict(
    "_OptionalNumericEqualityFilterTypeDef",
    {
        "Value": float,
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "AggregationFunction": AggregationFunctionTypeDef,
        "ParameterName": str,
    },
    total=False,
)


class NumericEqualityFilterTypeDef(
    _RequiredNumericEqualityFilterTypeDef, _OptionalNumericEqualityFilterTypeDef
):
    pass


_RequiredNumericRangeFilterTypeDef = TypedDict(
    "_RequiredNumericRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
    },
)
_OptionalNumericRangeFilterTypeDef = TypedDict(
    "_OptionalNumericRangeFilterTypeDef",
    {
        "IncludeMinimum": bool,
        "IncludeMaximum": bool,
        "RangeMinimum": NumericRangeFilterValueTypeDef,
        "RangeMaximum": NumericRangeFilterValueTypeDef,
        "SelectAllOptions": Literal["FILTER_ALL_VALUES"],
        "AggregationFunction": AggregationFunctionTypeDef,
    },
    total=False,
)


class NumericRangeFilterTypeDef(
    _RequiredNumericRangeFilterTypeDef, _OptionalNumericRangeFilterTypeDef
):
    pass


_RequiredReferenceLineDynamicDataConfigurationTypeDef = TypedDict(
    "_RequiredReferenceLineDynamicDataConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Calculation": NumericalAggregationFunctionTypeDef,
    },
)
_OptionalReferenceLineDynamicDataConfigurationTypeDef = TypedDict(
    "_OptionalReferenceLineDynamicDataConfigurationTypeDef",
    {
        "MeasureAggregationFunction": AggregationFunctionTypeDef,
    },
    total=False,
)


class ReferenceLineDynamicDataConfigurationTypeDef(
    _RequiredReferenceLineDynamicDataConfigurationTypeDef,
    _OptionalReferenceLineDynamicDataConfigurationTypeDef,
):
    pass


_RequiredTopicFilterOutputTypeDef = TypedDict(
    "_RequiredTopicFilterOutputTypeDef",
    {
        "FilterName": str,
        "OperandFieldName": str,
    },
)
_OptionalTopicFilterOutputTypeDef = TypedDict(
    "_OptionalTopicFilterOutputTypeDef",
    {
        "FilterDescription": str,
        "FilterClass": FilterClassType,
        "FilterSynonyms": List[str],
        "FilterType": NamedFilterTypeType,
        "CategoryFilter": TopicCategoryFilterOutputTypeDef,
        "NumericEqualityFilter": TopicNumericEqualityFilterTypeDef,
        "NumericRangeFilter": TopicNumericRangeFilterTypeDef,
        "DateRangeFilter": TopicDateRangeFilterTypeDef,
        "RelativeDateFilter": TopicRelativeDateFilterTypeDef,
    },
    total=False,
)


class TopicFilterOutputTypeDef(
    _RequiredTopicFilterOutputTypeDef, _OptionalTopicFilterOutputTypeDef
):
    pass


_RequiredTopicFilterTypeDef = TypedDict(
    "_RequiredTopicFilterTypeDef",
    {
        "FilterName": str,
        "OperandFieldName": str,
    },
)
_OptionalTopicFilterTypeDef = TypedDict(
    "_OptionalTopicFilterTypeDef",
    {
        "FilterDescription": str,
        "FilterClass": FilterClassType,
        "FilterSynonyms": Sequence[str],
        "FilterType": NamedFilterTypeType,
        "CategoryFilter": TopicCategoryFilterTypeDef,
        "NumericEqualityFilter": TopicNumericEqualityFilterTypeDef,
        "NumericRangeFilter": TopicNumericRangeFilterTypeDef,
        "DateRangeFilter": TopicDateRangeFilterTypeDef,
        "RelativeDateFilter": TopicRelativeDateFilterTypeDef,
    },
    total=False,
)


class TopicFilterTypeDef(_RequiredTopicFilterTypeDef, _OptionalTopicFilterTypeDef):
    pass


DescribeRefreshScheduleResponseTypeDef = TypedDict(
    "DescribeRefreshScheduleResponseTypeDef",
    {
        "RefreshSchedule": RefreshScheduleOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListRefreshSchedulesResponseTypeDef = TypedDict(
    "ListRefreshSchedulesResponseTypeDef",
    {
        "RefreshSchedules": List[RefreshScheduleOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRefreshScheduleRequestRequestTypeDef = TypedDict(
    "CreateRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "Schedule": RefreshScheduleTypeDef,
    },
)

UpdateRefreshScheduleRequestRequestTypeDef = TypedDict(
    "UpdateRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "Schedule": RefreshScheduleTypeDef,
    },
)

RegisteredUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": RegisteredUserDashboardEmbeddingConfigurationTypeDef,
        "QuickSightConsole": RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef,
        "QSearchBar": RegisteredUserQSearchBarEmbeddingConfigurationTypeDef,
        "DashboardVisual": RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef,
    },
    total=False,
)

SnapshotJobResultFileGroupTypeDef = TypedDict(
    "SnapshotJobResultFileGroupTypeDef",
    {
        "Files": List[SnapshotFileOutputTypeDef],
        "S3Results": List[SnapshotJobS3ResultTypeDef],
    },
    total=False,
)

DefaultSectionBasedLayoutConfigurationTypeDef = TypedDict(
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)

_RequiredFreeFormLayoutConfigurationOutputTypeDef = TypedDict(
    "_RequiredFreeFormLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[FreeFormLayoutElementOutputTypeDef],
    },
)
_OptionalFreeFormLayoutConfigurationOutputTypeDef = TypedDict(
    "_OptionalFreeFormLayoutConfigurationOutputTypeDef",
    {
        "CanvasSizeOptions": FreeFormLayoutCanvasSizeOptionsTypeDef,
    },
    total=False,
)


class FreeFormLayoutConfigurationOutputTypeDef(
    _RequiredFreeFormLayoutConfigurationOutputTypeDef,
    _OptionalFreeFormLayoutConfigurationOutputTypeDef,
):
    pass


FreeFormSectionLayoutConfigurationOutputTypeDef = TypedDict(
    "FreeFormSectionLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[FreeFormLayoutElementOutputTypeDef],
    },
)

_RequiredFreeFormLayoutConfigurationTypeDef = TypedDict(
    "_RequiredFreeFormLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[FreeFormLayoutElementTypeDef],
    },
)
_OptionalFreeFormLayoutConfigurationTypeDef = TypedDict(
    "_OptionalFreeFormLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": FreeFormLayoutCanvasSizeOptionsTypeDef,
    },
    total=False,
)


class FreeFormLayoutConfigurationTypeDef(
    _RequiredFreeFormLayoutConfigurationTypeDef, _OptionalFreeFormLayoutConfigurationTypeDef
):
    pass


FreeFormSectionLayoutConfigurationTypeDef = TypedDict(
    "FreeFormSectionLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[FreeFormLayoutElementTypeDef],
    },
)

_RequiredSnapshotConfigurationOutputTypeDef = TypedDict(
    "_RequiredSnapshotConfigurationOutputTypeDef",
    {
        "FileGroups": List[SnapshotFileGroupOutputTypeDef],
    },
)
_OptionalSnapshotConfigurationOutputTypeDef = TypedDict(
    "_OptionalSnapshotConfigurationOutputTypeDef",
    {
        "DestinationConfiguration": SnapshotDestinationConfigurationOutputTypeDef,
        "Parameters": ParametersOutputTypeDef,
    },
    total=False,
)


class SnapshotConfigurationOutputTypeDef(
    _RequiredSnapshotConfigurationOutputTypeDef, _OptionalSnapshotConfigurationOutputTypeDef
):
    pass


_RequiredSnapshotConfigurationTypeDef = TypedDict(
    "_RequiredSnapshotConfigurationTypeDef",
    {
        "FileGroups": Sequence[SnapshotFileGroupTypeDef],
    },
)
_OptionalSnapshotConfigurationTypeDef = TypedDict(
    "_OptionalSnapshotConfigurationTypeDef",
    {
        "DestinationConfiguration": SnapshotDestinationConfigurationTypeDef,
        "Parameters": ParametersTypeDef,
    },
    total=False,
)


class SnapshotConfigurationTypeDef(
    _RequiredSnapshotConfigurationTypeDef, _OptionalSnapshotConfigurationTypeDef
):
    pass


ParameterDeclarationOutputTypeDef = TypedDict(
    "ParameterDeclarationOutputTypeDef",
    {
        "StringParameterDeclaration": StringParameterDeclarationOutputTypeDef,
        "DecimalParameterDeclaration": DecimalParameterDeclarationOutputTypeDef,
        "IntegerParameterDeclaration": IntegerParameterDeclarationOutputTypeDef,
        "DateTimeParameterDeclaration": DateTimeParameterDeclarationOutputTypeDef,
    },
    total=False,
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "StringParameterDeclaration": StringParameterDeclarationTypeDef,
        "DecimalParameterDeclaration": DecimalParameterDeclarationTypeDef,
        "IntegerParameterDeclaration": IntegerParameterDeclarationTypeDef,
        "DateTimeParameterDeclaration": DateTimeParameterDeclarationTypeDef,
    },
    total=False,
)

ColumnHierarchyOutputTypeDef = TypedDict(
    "ColumnHierarchyOutputTypeDef",
    {
        "ExplicitHierarchy": ExplicitHierarchyOutputTypeDef,
        "DateTimeHierarchy": DateTimeHierarchyOutputTypeDef,
        "PredefinedHierarchy": PredefinedHierarchyOutputTypeDef,
    },
    total=False,
)

ColumnHierarchyTypeDef = TypedDict(
    "ColumnHierarchyTypeDef",
    {
        "ExplicitHierarchy": ExplicitHierarchyTypeDef,
        "DateTimeHierarchy": DateTimeHierarchyTypeDef,
        "PredefinedHierarchy": PredefinedHierarchyTypeDef,
    },
    total=False,
)

DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "Dashboard": DashboardTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredLogicalTableOutputTypeDef = TypedDict(
    "_RequiredLogicalTableOutputTypeDef",
    {
        "Alias": str,
        "Source": LogicalTableSourceTypeDef,
    },
)
_OptionalLogicalTableOutputTypeDef = TypedDict(
    "_OptionalLogicalTableOutputTypeDef",
    {
        "DataTransforms": List[TransformOperationOutputTypeDef],
    },
    total=False,
)


class LogicalTableOutputTypeDef(
    _RequiredLogicalTableOutputTypeDef, _OptionalLogicalTableOutputTypeDef
):
    pass


_RequiredLogicalTableTypeDef = TypedDict(
    "_RequiredLogicalTableTypeDef",
    {
        "Alias": str,
        "Source": LogicalTableSourceTypeDef,
    },
)
_OptionalLogicalTableTypeDef = TypedDict(
    "_OptionalLogicalTableTypeDef",
    {
        "DataTransforms": Sequence[TransformOperationTypeDef],
    },
    total=False,
)


class LogicalTableTypeDef(_RequiredLogicalTableTypeDef, _OptionalLogicalTableTypeDef):
    pass


TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Version": TemplateVersionTypeDef,
        "TemplateId": str,
        "LastUpdatedTime": datetime,
        "CreatedTime": datetime,
    },
    total=False,
)

CustomActionSetParametersOperationOutputTypeDef = TypedDict(
    "CustomActionSetParametersOperationOutputTypeDef",
    {
        "ParameterValueConfigurations": List[SetParameterValueConfigurationOutputTypeDef],
    },
)

CustomActionSetParametersOperationTypeDef = TypedDict(
    "CustomActionSetParametersOperationTypeDef",
    {
        "ParameterValueConfigurations": Sequence[SetParameterValueConfigurationTypeDef],
    },
)

AxisDisplayOptionsOutputTypeDef = TypedDict(
    "AxisDisplayOptionsOutputTypeDef",
    {
        "TickLabelOptions": AxisTickLabelOptionsTypeDef,
        "AxisLineVisibility": VisibilityType,
        "GridLineVisibility": VisibilityType,
        "DataOptions": AxisDataOptionsOutputTypeDef,
        "ScrollbarOptions": ScrollBarOptionsTypeDef,
        "AxisOffset": str,
    },
    total=False,
)

AxisDisplayOptionsTypeDef = TypedDict(
    "AxisDisplayOptionsTypeDef",
    {
        "TickLabelOptions": AxisTickLabelOptionsTypeDef,
        "AxisLineVisibility": VisibilityType,
        "GridLineVisibility": VisibilityType,
        "DataOptions": AxisDataOptionsTypeDef,
        "ScrollbarOptions": ScrollBarOptionsTypeDef,
        "AxisOffset": str,
    },
    total=False,
)

_RequiredFilterDateTimePickerControlTypeDef = TypedDict(
    "_RequiredFilterDateTimePickerControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterDateTimePickerControlTypeDef = TypedDict(
    "_OptionalFilterDateTimePickerControlTypeDef",
    {
        "DisplayOptions": DateTimePickerControlDisplayOptionsTypeDef,
        "Type": SheetControlDateTimePickerTypeType,
    },
    total=False,
)


class FilterDateTimePickerControlTypeDef(
    _RequiredFilterDateTimePickerControlTypeDef, _OptionalFilterDateTimePickerControlTypeDef
):
    pass


_RequiredParameterDateTimePickerControlTypeDef = TypedDict(
    "_RequiredParameterDateTimePickerControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterDateTimePickerControlTypeDef = TypedDict(
    "_OptionalParameterDateTimePickerControlTypeDef",
    {
        "DisplayOptions": DateTimePickerControlDisplayOptionsTypeDef,
    },
    total=False,
)


class ParameterDateTimePickerControlTypeDef(
    _RequiredParameterDateTimePickerControlTypeDef, _OptionalParameterDateTimePickerControlTypeDef
):
    pass


_RequiredFilterDropDownControlOutputTypeDef = TypedDict(
    "_RequiredFilterDropDownControlOutputTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterDropDownControlOutputTypeDef = TypedDict(
    "_OptionalFilterDropDownControlOutputTypeDef",
    {
        "DisplayOptions": DropDownControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": FilterSelectableValuesOutputTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationOutputTypeDef,
    },
    total=False,
)


class FilterDropDownControlOutputTypeDef(
    _RequiredFilterDropDownControlOutputTypeDef, _OptionalFilterDropDownControlOutputTypeDef
):
    pass


_RequiredFilterDropDownControlTypeDef = TypedDict(
    "_RequiredFilterDropDownControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterDropDownControlTypeDef = TypedDict(
    "_OptionalFilterDropDownControlTypeDef",
    {
        "DisplayOptions": DropDownControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": FilterSelectableValuesTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationTypeDef,
    },
    total=False,
)


class FilterDropDownControlTypeDef(
    _RequiredFilterDropDownControlTypeDef, _OptionalFilterDropDownControlTypeDef
):
    pass


_RequiredParameterDropDownControlOutputTypeDef = TypedDict(
    "_RequiredParameterDropDownControlOutputTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterDropDownControlOutputTypeDef = TypedDict(
    "_OptionalParameterDropDownControlOutputTypeDef",
    {
        "DisplayOptions": DropDownControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": ParameterSelectableValuesOutputTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationOutputTypeDef,
    },
    total=False,
)


class ParameterDropDownControlOutputTypeDef(
    _RequiredParameterDropDownControlOutputTypeDef, _OptionalParameterDropDownControlOutputTypeDef
):
    pass


_RequiredParameterDropDownControlTypeDef = TypedDict(
    "_RequiredParameterDropDownControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterDropDownControlTypeDef = TypedDict(
    "_OptionalParameterDropDownControlTypeDef",
    {
        "DisplayOptions": DropDownControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": ParameterSelectableValuesTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationTypeDef,
    },
    total=False,
)


class ParameterDropDownControlTypeDef(
    _RequiredParameterDropDownControlTypeDef, _OptionalParameterDropDownControlTypeDef
):
    pass


_RequiredFilterListControlOutputTypeDef = TypedDict(
    "_RequiredFilterListControlOutputTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterListControlOutputTypeDef = TypedDict(
    "_OptionalFilterListControlOutputTypeDef",
    {
        "DisplayOptions": ListControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": FilterSelectableValuesOutputTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationOutputTypeDef,
    },
    total=False,
)


class FilterListControlOutputTypeDef(
    _RequiredFilterListControlOutputTypeDef, _OptionalFilterListControlOutputTypeDef
):
    pass


_RequiredFilterListControlTypeDef = TypedDict(
    "_RequiredFilterListControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterListControlTypeDef = TypedDict(
    "_OptionalFilterListControlTypeDef",
    {
        "DisplayOptions": ListControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": FilterSelectableValuesTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationTypeDef,
    },
    total=False,
)


class FilterListControlTypeDef(
    _RequiredFilterListControlTypeDef, _OptionalFilterListControlTypeDef
):
    pass


_RequiredParameterListControlOutputTypeDef = TypedDict(
    "_RequiredParameterListControlOutputTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterListControlOutputTypeDef = TypedDict(
    "_OptionalParameterListControlOutputTypeDef",
    {
        "DisplayOptions": ListControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": ParameterSelectableValuesOutputTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationOutputTypeDef,
    },
    total=False,
)


class ParameterListControlOutputTypeDef(
    _RequiredParameterListControlOutputTypeDef, _OptionalParameterListControlOutputTypeDef
):
    pass


_RequiredParameterListControlTypeDef = TypedDict(
    "_RequiredParameterListControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterListControlTypeDef = TypedDict(
    "_OptionalParameterListControlTypeDef",
    {
        "DisplayOptions": ListControlDisplayOptionsTypeDef,
        "Type": SheetControlListTypeType,
        "SelectableValues": ParameterSelectableValuesTypeDef,
        "CascadingControlConfiguration": CascadingControlConfigurationTypeDef,
    },
    total=False,
)


class ParameterListControlTypeDef(
    _RequiredParameterListControlTypeDef, _OptionalParameterListControlTypeDef
):
    pass


_RequiredFilterRelativeDateTimeControlTypeDef = TypedDict(
    "_RequiredFilterRelativeDateTimeControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterRelativeDateTimeControlTypeDef = TypedDict(
    "_OptionalFilterRelativeDateTimeControlTypeDef",
    {
        "DisplayOptions": RelativeDateTimeControlDisplayOptionsTypeDef,
    },
    total=False,
)


class FilterRelativeDateTimeControlTypeDef(
    _RequiredFilterRelativeDateTimeControlTypeDef, _OptionalFilterRelativeDateTimeControlTypeDef
):
    pass


_RequiredFilterSliderControlTypeDef = TypedDict(
    "_RequiredFilterSliderControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
    },
)
_OptionalFilterSliderControlTypeDef = TypedDict(
    "_OptionalFilterSliderControlTypeDef",
    {
        "DisplayOptions": SliderControlDisplayOptionsTypeDef,
        "Type": SheetControlSliderTypeType,
    },
    total=False,
)


class FilterSliderControlTypeDef(
    _RequiredFilterSliderControlTypeDef, _OptionalFilterSliderControlTypeDef
):
    pass


_RequiredParameterSliderControlTypeDef = TypedDict(
    "_RequiredParameterSliderControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
    },
)
_OptionalParameterSliderControlTypeDef = TypedDict(
    "_OptionalParameterSliderControlTypeDef",
    {
        "DisplayOptions": SliderControlDisplayOptionsTypeDef,
    },
    total=False,
)


class ParameterSliderControlTypeDef(
    _RequiredParameterSliderControlTypeDef, _OptionalParameterSliderControlTypeDef
):
    pass


_RequiredFilterTextAreaControlTypeDef = TypedDict(
    "_RequiredFilterTextAreaControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterTextAreaControlTypeDef = TypedDict(
    "_OptionalFilterTextAreaControlTypeDef",
    {
        "Delimiter": str,
        "DisplayOptions": TextAreaControlDisplayOptionsTypeDef,
    },
    total=False,
)


class FilterTextAreaControlTypeDef(
    _RequiredFilterTextAreaControlTypeDef, _OptionalFilterTextAreaControlTypeDef
):
    pass


_RequiredParameterTextAreaControlTypeDef = TypedDict(
    "_RequiredParameterTextAreaControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterTextAreaControlTypeDef = TypedDict(
    "_OptionalParameterTextAreaControlTypeDef",
    {
        "Delimiter": str,
        "DisplayOptions": TextAreaControlDisplayOptionsTypeDef,
    },
    total=False,
)


class ParameterTextAreaControlTypeDef(
    _RequiredParameterTextAreaControlTypeDef, _OptionalParameterTextAreaControlTypeDef
):
    pass


_RequiredFilterTextFieldControlTypeDef = TypedDict(
    "_RequiredFilterTextFieldControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
    },
)
_OptionalFilterTextFieldControlTypeDef = TypedDict(
    "_OptionalFilterTextFieldControlTypeDef",
    {
        "DisplayOptions": TextFieldControlDisplayOptionsTypeDef,
    },
    total=False,
)


class FilterTextFieldControlTypeDef(
    _RequiredFilterTextFieldControlTypeDef, _OptionalFilterTextFieldControlTypeDef
):
    pass


_RequiredParameterTextFieldControlTypeDef = TypedDict(
    "_RequiredParameterTextFieldControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
    },
)
_OptionalParameterTextFieldControlTypeDef = TypedDict(
    "_OptionalParameterTextFieldControlTypeDef",
    {
        "DisplayOptions": TextFieldControlDisplayOptionsTypeDef,
    },
    total=False,
)


class ParameterTextFieldControlTypeDef(
    _RequiredParameterTextFieldControlTypeDef, _OptionalParameterTextFieldControlTypeDef
):
    pass


SmallMultiplesOptionsTypeDef = TypedDict(
    "SmallMultiplesOptionsTypeDef",
    {
        "MaxVisibleRows": int,
        "MaxVisibleColumns": int,
        "PanelConfiguration": PanelConfigurationTypeDef,
        "XAxis": SmallMultiplesAxisPropertiesTypeDef,
        "YAxis": SmallMultiplesAxisPropertiesTypeDef,
    },
    total=False,
)

TableFieldLinkConfigurationTypeDef = TypedDict(
    "TableFieldLinkConfigurationTypeDef",
    {
        "Target": URLTargetConfigurationType,
        "Content": TableFieldLinkContentConfigurationTypeDef,
    },
)

PivotTableOptionsOutputTypeDef = TypedDict(
    "PivotTableOptionsOutputTypeDef",
    {
        "MetricPlacement": PivotTableMetricPlacementType,
        "SingleMetricVisibility": VisibilityType,
        "ColumnNamesVisibility": VisibilityType,
        "ToggleButtonsVisibility": VisibilityType,
        "ColumnHeaderStyle": TableCellStyleTypeDef,
        "RowHeaderStyle": TableCellStyleTypeDef,
        "CellStyle": TableCellStyleTypeDef,
        "RowFieldNamesStyle": TableCellStyleTypeDef,
        "RowAlternateColorOptions": RowAlternateColorOptionsOutputTypeDef,
        "CollapsedRowDimensionsVisibility": VisibilityType,
    },
    total=False,
)

PivotTableOptionsTypeDef = TypedDict(
    "PivotTableOptionsTypeDef",
    {
        "MetricPlacement": PivotTableMetricPlacementType,
        "SingleMetricVisibility": VisibilityType,
        "ColumnNamesVisibility": VisibilityType,
        "ToggleButtonsVisibility": VisibilityType,
        "ColumnHeaderStyle": TableCellStyleTypeDef,
        "RowHeaderStyle": TableCellStyleTypeDef,
        "CellStyle": TableCellStyleTypeDef,
        "RowFieldNamesStyle": TableCellStyleTypeDef,
        "RowAlternateColorOptions": RowAlternateColorOptionsTypeDef,
        "CollapsedRowDimensionsVisibility": VisibilityType,
    },
    total=False,
)

PivotTotalOptionsTypeDef = TypedDict(
    "PivotTotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "Placement": TableTotalsPlacementType,
        "ScrollStatus": TableTotalsScrollStatusType,
        "CustomLabel": str,
        "TotalCellStyle": TableCellStyleTypeDef,
        "ValueCellStyle": TableCellStyleTypeDef,
        "MetricHeaderCellStyle": TableCellStyleTypeDef,
    },
    total=False,
)

SubtotalOptionsOutputTypeDef = TypedDict(
    "SubtotalOptionsOutputTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "CustomLabel": str,
        "FieldLevel": PivotTableSubtotalLevelType,
        "FieldLevelOptions": List[PivotTableFieldSubtotalOptionsTypeDef],
        "TotalCellStyle": TableCellStyleTypeDef,
        "ValueCellStyle": TableCellStyleTypeDef,
        "MetricHeaderCellStyle": TableCellStyleTypeDef,
    },
    total=False,
)

SubtotalOptionsTypeDef = TypedDict(
    "SubtotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "CustomLabel": str,
        "FieldLevel": PivotTableSubtotalLevelType,
        "FieldLevelOptions": Sequence[PivotTableFieldSubtotalOptionsTypeDef],
        "TotalCellStyle": TableCellStyleTypeDef,
        "ValueCellStyle": TableCellStyleTypeDef,
        "MetricHeaderCellStyle": TableCellStyleTypeDef,
    },
    total=False,
)

TableOptionsOutputTypeDef = TypedDict(
    "TableOptionsOutputTypeDef",
    {
        "Orientation": TableOrientationType,
        "HeaderStyle": TableCellStyleTypeDef,
        "CellStyle": TableCellStyleTypeDef,
        "RowAlternateColorOptions": RowAlternateColorOptionsOutputTypeDef,
    },
    total=False,
)

TableOptionsTypeDef = TypedDict(
    "TableOptionsTypeDef",
    {
        "Orientation": TableOrientationType,
        "HeaderStyle": TableCellStyleTypeDef,
        "CellStyle": TableCellStyleTypeDef,
        "RowAlternateColorOptions": RowAlternateColorOptionsTypeDef,
    },
    total=False,
)

TotalOptionsTypeDef = TypedDict(
    "TotalOptionsTypeDef",
    {
        "TotalsVisibility": VisibilityType,
        "Placement": TableTotalsPlacementType,
        "ScrollStatus": TableTotalsScrollStatusType,
        "CustomLabel": str,
        "TotalCellStyle": TableCellStyleTypeDef,
    },
    total=False,
)

GaugeChartArcConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartArcConditionalFormattingOutputTypeDef",
    {
        "ForegroundColor": ConditionalFormattingColorOutputTypeDef,
    },
    total=False,
)

GaugeChartPrimaryValueConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartPrimaryValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": ConditionalFormattingColorOutputTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

KPIPrimaryValueConditionalFormattingOutputTypeDef = TypedDict(
    "KPIPrimaryValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": ConditionalFormattingColorOutputTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

KPIProgressBarConditionalFormattingOutputTypeDef = TypedDict(
    "KPIProgressBarConditionalFormattingOutputTypeDef",
    {
        "ForegroundColor": ConditionalFormattingColorOutputTypeDef,
    },
    total=False,
)

ShapeConditionalFormatOutputTypeDef = TypedDict(
    "ShapeConditionalFormatOutputTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorOutputTypeDef,
    },
)

TableRowConditionalFormattingOutputTypeDef = TypedDict(
    "TableRowConditionalFormattingOutputTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorOutputTypeDef,
        "TextColor": ConditionalFormattingColorOutputTypeDef,
    },
    total=False,
)

TextConditionalFormatOutputTypeDef = TypedDict(
    "TextConditionalFormatOutputTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorOutputTypeDef,
        "TextColor": ConditionalFormattingColorOutputTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

GaugeChartArcConditionalFormattingTypeDef = TypedDict(
    "GaugeChartArcConditionalFormattingTypeDef",
    {
        "ForegroundColor": ConditionalFormattingColorTypeDef,
    },
    total=False,
)

GaugeChartPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": ConditionalFormattingColorTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

KPIPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "KPIPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": ConditionalFormattingColorTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

KPIProgressBarConditionalFormattingTypeDef = TypedDict(
    "KPIProgressBarConditionalFormattingTypeDef",
    {
        "ForegroundColor": ConditionalFormattingColorTypeDef,
    },
    total=False,
)

ShapeConditionalFormatTypeDef = TypedDict(
    "ShapeConditionalFormatTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorTypeDef,
    },
)

TableRowConditionalFormattingTypeDef = TypedDict(
    "TableRowConditionalFormattingTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorTypeDef,
        "TextColor": ConditionalFormattingColorTypeDef,
    },
    total=False,
)

TextConditionalFormatTypeDef = TypedDict(
    "TextConditionalFormatTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorTypeDef,
        "TextColor": ConditionalFormattingColorTypeDef,
        "Icon": ConditionalFormattingIconTypeDef,
    },
    total=False,
)

SheetControlLayoutOutputTypeDef = TypedDict(
    "SheetControlLayoutOutputTypeDef",
    {
        "Configuration": SheetControlLayoutConfigurationOutputTypeDef,
    },
)

SheetControlLayoutTypeDef = TypedDict(
    "SheetControlLayoutTypeDef",
    {
        "Configuration": SheetControlLayoutConfigurationTypeDef,
    },
)

DescribeDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "DescribeDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "DataSetRefreshProperties": DataSetRefreshPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

PutDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "PutDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "DataSetRefreshProperties": DataSetRefreshPropertiesTypeDef,
    },
)

AssetBundleImportJobOverrideParametersOutputTypeDef = TypedDict(
    "AssetBundleImportJobOverrideParametersOutputTypeDef",
    {
        "ResourceIdOverrideConfiguration": (
            AssetBundleImportJobResourceIdOverrideConfigurationTypeDef
        ),
        "VPCConnections": List[AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef],
        "RefreshSchedules": List[
            AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef
        ],
        "DataSources": List[AssetBundleImportJobDataSourceOverrideParametersTypeDef],
        "DataSets": List[AssetBundleImportJobDataSetOverrideParametersTypeDef],
        "Themes": List[AssetBundleImportJobThemeOverrideParametersTypeDef],
        "Analyses": List[AssetBundleImportJobAnalysisOverrideParametersTypeDef],
        "Dashboards": List[AssetBundleImportJobDashboardOverrideParametersTypeDef],
    },
    total=False,
)

AssetBundleImportJobOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobOverrideParametersTypeDef",
    {
        "ResourceIdOverrideConfiguration": (
            AssetBundleImportJobResourceIdOverrideConfigurationTypeDef
        ),
        "VPCConnections": Sequence[AssetBundleImportJobVPCConnectionOverrideParametersTypeDef],
        "RefreshSchedules": Sequence[AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef],
        "DataSources": Sequence[AssetBundleImportJobDataSourceOverrideParametersTypeDef],
        "DataSets": Sequence[AssetBundleImportJobDataSetOverrideParametersTypeDef],
        "Themes": Sequence[AssetBundleImportJobThemeOverrideParametersTypeDef],
        "Analyses": Sequence[AssetBundleImportJobAnalysisOverrideParametersTypeDef],
        "Dashboards": Sequence[AssetBundleImportJobDashboardOverrideParametersTypeDef],
    },
    total=False,
)

DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {
        "CredentialPair": CredentialPairTypeDef,
        "CopySourceArn": str,
        "SecretArn": str,
    },
    total=False,
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "DataSource": DataSourceTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "DataSources": List[DataSourceTypeDef],
        "NextToken": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ThemeVersionTypeDef = TypedDict(
    "ThemeVersionTypeDef",
    {
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "BaseThemeId": str,
        "CreatedTime": datetime,
        "Configuration": ThemeConfigurationOutputTypeDef,
        "Errors": List[ThemeErrorTypeDef],
        "Status": ResourceStatusType,
    },
    total=False,
)

_RequiredCreateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "Name": str,
        "BaseThemeId": str,
        "Configuration": ThemeConfigurationTypeDef,
    },
)
_OptionalCreateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestRequestTypeDef",
    {
        "VersionDescription": str,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateThemeRequestRequestTypeDef(
    _RequiredCreateThemeRequestRequestTypeDef, _OptionalCreateThemeRequestRequestTypeDef
):
    pass


_RequiredUpdateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "BaseThemeId": str,
    },
)
_OptionalUpdateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestRequestTypeDef",
    {
        "Name": str,
        "VersionDescription": str,
        "Configuration": ThemeConfigurationTypeDef,
    },
    total=False,
)


class UpdateThemeRequestRequestTypeDef(
    _RequiredUpdateThemeRequestRequestTypeDef, _OptionalUpdateThemeRequestRequestTypeDef
):
    pass


ComparisonConfigurationTypeDef = TypedDict(
    "ComparisonConfigurationTypeDef",
    {
        "ComparisonMethod": ComparisonMethodType,
        "ComparisonFormat": ComparisonFormatConfigurationTypeDef,
    },
    total=False,
)

DateTimeFormatConfigurationTypeDef = TypedDict(
    "DateTimeFormatConfigurationTypeDef",
    {
        "DateTimeFormat": str,
        "NullValueFormatConfiguration": NullValueFormatConfigurationTypeDef,
        "NumericFormatConfiguration": NumericFormatConfigurationTypeDef,
    },
    total=False,
)

NumberFormatConfigurationTypeDef = TypedDict(
    "NumberFormatConfigurationTypeDef",
    {
        "FormatConfiguration": NumericFormatConfigurationTypeDef,
    },
    total=False,
)

ReferenceLineValueLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineValueLabelConfigurationTypeDef",
    {
        "RelativePosition": ReferenceLineValueLabelRelativePositionType,
        "FormatConfiguration": NumericFormatConfigurationTypeDef,
    },
    total=False,
)

StringFormatConfigurationTypeDef = TypedDict(
    "StringFormatConfigurationTypeDef",
    {
        "NullValueFormatConfiguration": NullValueFormatConfigurationTypeDef,
        "NumericFormatConfiguration": NumericFormatConfigurationTypeDef,
    },
    total=False,
)

_RequiredTopBottomFilterOutputTypeDef = TypedDict(
    "_RequiredTopBottomFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationSortConfigurations": List[AggregationSortConfigurationTypeDef],
    },
)
_OptionalTopBottomFilterOutputTypeDef = TypedDict(
    "_OptionalTopBottomFilterOutputTypeDef",
    {
        "Limit": int,
        "TimeGranularity": TimeGranularityType,
        "ParameterName": str,
    },
    total=False,
)


class TopBottomFilterOutputTypeDef(
    _RequiredTopBottomFilterOutputTypeDef, _OptionalTopBottomFilterOutputTypeDef
):
    pass


_RequiredTopBottomFilterTypeDef = TypedDict(
    "_RequiredTopBottomFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationSortConfigurations": Sequence[AggregationSortConfigurationTypeDef],
    },
)
_OptionalTopBottomFilterTypeDef = TypedDict(
    "_OptionalTopBottomFilterTypeDef",
    {
        "Limit": int,
        "TimeGranularity": TimeGranularityType,
        "ParameterName": str,
    },
    total=False,
)


class TopBottomFilterTypeDef(_RequiredTopBottomFilterTypeDef, _OptionalTopBottomFilterTypeDef):
    pass


FieldSortOptionsTypeDef = TypedDict(
    "FieldSortOptionsTypeDef",
    {
        "FieldSort": FieldSortTypeDef,
        "ColumnSort": ColumnSortTypeDef,
    },
    total=False,
)

PivotTableSortByOutputTypeDef = TypedDict(
    "PivotTableSortByOutputTypeDef",
    {
        "Field": FieldSortTypeDef,
        "Column": ColumnSortTypeDef,
        "DataPath": DataPathSortOutputTypeDef,
    },
    total=False,
)

PivotTableSortByTypeDef = TypedDict(
    "PivotTableSortByTypeDef",
    {
        "Field": FieldSortTypeDef,
        "Column": ColumnSortTypeDef,
        "DataPath": DataPathSortTypeDef,
    },
    total=False,
)

TooltipItemTypeDef = TypedDict(
    "TooltipItemTypeDef",
    {
        "FieldTooltipItem": FieldTooltipItemTypeDef,
        "ColumnTooltipItem": ColumnTooltipItemTypeDef,
    },
    total=False,
)

ReferenceLineDataConfigurationTypeDef = TypedDict(
    "ReferenceLineDataConfigurationTypeDef",
    {
        "StaticConfiguration": ReferenceLineStaticDataConfigurationTypeDef,
        "DynamicConfiguration": ReferenceLineDynamicDataConfigurationTypeDef,
        "AxisBinding": AxisBindingType,
    },
    total=False,
)

_RequiredDatasetMetadataOutputTypeDef = TypedDict(
    "_RequiredDatasetMetadataOutputTypeDef",
    {
        "DatasetArn": str,
    },
)
_OptionalDatasetMetadataOutputTypeDef = TypedDict(
    "_OptionalDatasetMetadataOutputTypeDef",
    {
        "DatasetName": str,
        "DatasetDescription": str,
        "DataAggregation": DataAggregationTypeDef,
        "Filters": List[TopicFilterOutputTypeDef],
        "Columns": List[TopicColumnOutputTypeDef],
        "CalculatedFields": List[TopicCalculatedFieldOutputTypeDef],
        "NamedEntities": List[TopicNamedEntityOutputTypeDef],
    },
    total=False,
)


class DatasetMetadataOutputTypeDef(
    _RequiredDatasetMetadataOutputTypeDef, _OptionalDatasetMetadataOutputTypeDef
):
    pass


_RequiredDatasetMetadataTypeDef = TypedDict(
    "_RequiredDatasetMetadataTypeDef",
    {
        "DatasetArn": str,
    },
)
_OptionalDatasetMetadataTypeDef = TypedDict(
    "_OptionalDatasetMetadataTypeDef",
    {
        "DatasetName": str,
        "DatasetDescription": str,
        "DataAggregation": DataAggregationTypeDef,
        "Filters": Sequence[TopicFilterTypeDef],
        "Columns": Sequence[TopicColumnTypeDef],
        "CalculatedFields": Sequence[TopicCalculatedFieldTypeDef],
        "NamedEntities": Sequence[TopicNamedEntityTypeDef],
    },
    total=False,
)


class DatasetMetadataTypeDef(_RequiredDatasetMetadataTypeDef, _OptionalDatasetMetadataTypeDef):
    pass


_RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserArn": str,
        "ExperienceConfiguration": RegisteredUserEmbeddingExperienceConfigurationTypeDef,
    },
)
_OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "SessionLifetimeInMinutes": int,
        "AllowedDomains": Sequence[str],
    },
    total=False,
)


class GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef(
    _RequiredGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef,
    _OptionalGenerateEmbedUrlForRegisteredUserRequestRequestTypeDef,
):
    pass


AnonymousUserSnapshotJobResultTypeDef = TypedDict(
    "AnonymousUserSnapshotJobResultTypeDef",
    {
        "FileGroups": List[SnapshotJobResultFileGroupTypeDef],
    },
    total=False,
)

DefaultPaginatedLayoutConfigurationTypeDef = TypedDict(
    "DefaultPaginatedLayoutConfigurationTypeDef",
    {
        "SectionBased": DefaultSectionBasedLayoutConfigurationTypeDef,
    },
    total=False,
)

SectionLayoutConfigurationOutputTypeDef = TypedDict(
    "SectionLayoutConfigurationOutputTypeDef",
    {
        "FreeFormLayout": FreeFormSectionLayoutConfigurationOutputTypeDef,
    },
)

SectionLayoutConfigurationTypeDef = TypedDict(
    "SectionLayoutConfigurationTypeDef",
    {
        "FreeFormLayout": FreeFormSectionLayoutConfigurationTypeDef,
    },
)

DescribeDashboardSnapshotJobResponseTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResponseTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
        "UserConfiguration": SnapshotUserConfigurationRedactedTypeDef,
        "SnapshotConfiguration": SnapshotConfigurationOutputTypeDef,
        "Arn": str,
        "JobStatus": SnapshotJobStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDashboardSnapshotJobRequestRequestTypeDef = TypedDict(
    "StartDashboardSnapshotJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
        "UserConfiguration": SnapshotUserConfigurationTypeDef,
        "SnapshotConfiguration": SnapshotConfigurationTypeDef,
    },
)

DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "PhysicalTableMap": Dict[str, PhysicalTableOutputTypeDef],
        "LogicalTableMap": Dict[str, LogicalTableOutputTypeDef],
        "OutputColumns": List[OutputColumnTypeDef],
        "ImportMode": DataSetImportModeType,
        "ConsumedSpiceCapacityInBytes": int,
        "ColumnGroups": List[ColumnGroupOutputTypeDef],
        "FieldFolders": Dict[str, FieldFolderOutputTypeDef],
        "RowLevelPermissionDataSet": RowLevelPermissionDataSetTypeDef,
        "RowLevelPermissionTagConfiguration": RowLevelPermissionTagConfigurationOutputTypeDef,
        "ColumnLevelPermissionRules": List[ColumnLevelPermissionRuleOutputTypeDef],
        "DataSetUsageConfiguration": DataSetUsageConfigurationTypeDef,
        "DatasetParameters": List[DatasetParameterOutputTypeDef],
    },
    total=False,
)

_RequiredCreateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, Union[PhysicalTableTypeDef, PhysicalTableOutputTypeDef]],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalCreateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSetRequestRequestTypeDef",
    {
        "LogicalTableMap": Mapping[str, Union[LogicalTableTypeDef, LogicalTableOutputTypeDef]],
        "ColumnGroups": Sequence[Union[ColumnGroupTypeDef, ColumnGroupOutputTypeDef]],
        "FieldFolders": Mapping[str, Union[FieldFolderTypeDef, FieldFolderOutputTypeDef]],
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "RowLevelPermissionDataSet": RowLevelPermissionDataSetTypeDef,
        "RowLevelPermissionTagConfiguration": RowLevelPermissionTagConfigurationTypeDef,
        "ColumnLevelPermissionRules": Sequence[
            Union[ColumnLevelPermissionRuleTypeDef, ColumnLevelPermissionRuleOutputTypeDef]
        ],
        "Tags": Sequence[TagTypeDef],
        "DataSetUsageConfiguration": DataSetUsageConfigurationTypeDef,
        "DatasetParameters": Sequence[
            Union[DatasetParameterTypeDef, DatasetParameterOutputTypeDef]
        ],
    },
    total=False,
)


class CreateDataSetRequestRequestTypeDef(
    _RequiredCreateDataSetRequestRequestTypeDef, _OptionalCreateDataSetRequestRequestTypeDef
):
    pass


_RequiredUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, Union[PhysicalTableTypeDef, PhysicalTableOutputTypeDef]],
        "ImportMode": DataSetImportModeType,
    },
)
_OptionalUpdateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSetRequestRequestTypeDef",
    {
        "LogicalTableMap": Mapping[str, Union[LogicalTableTypeDef, LogicalTableOutputTypeDef]],
        "ColumnGroups": Sequence[Union[ColumnGroupTypeDef, ColumnGroupOutputTypeDef]],
        "FieldFolders": Mapping[str, Union[FieldFolderTypeDef, FieldFolderOutputTypeDef]],
        "RowLevelPermissionDataSet": RowLevelPermissionDataSetTypeDef,
        "RowLevelPermissionTagConfiguration": RowLevelPermissionTagConfigurationTypeDef,
        "ColumnLevelPermissionRules": Sequence[
            Union[ColumnLevelPermissionRuleTypeDef, ColumnLevelPermissionRuleOutputTypeDef]
        ],
        "DataSetUsageConfiguration": DataSetUsageConfigurationTypeDef,
        "DatasetParameters": Sequence[
            Union[DatasetParameterTypeDef, DatasetParameterOutputTypeDef]
        ],
    },
    total=False,
)


class UpdateDataSetRequestRequestTypeDef(
    _RequiredUpdateDataSetRequestRequestTypeDef, _OptionalUpdateDataSetRequestRequestTypeDef
):
    pass


DescribeTemplateResponseTypeDef = TypedDict(
    "DescribeTemplateResponseTypeDef",
    {
        "Template": TemplateTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

VisualCustomActionOperationOutputTypeDef = TypedDict(
    "VisualCustomActionOperationOutputTypeDef",
    {
        "FilterOperation": CustomActionFilterOperationOutputTypeDef,
        "NavigationOperation": CustomActionNavigationOperationTypeDef,
        "URLOperation": CustomActionURLOperationTypeDef,
        "SetParametersOperation": CustomActionSetParametersOperationOutputTypeDef,
    },
    total=False,
)

VisualCustomActionOperationTypeDef = TypedDict(
    "VisualCustomActionOperationTypeDef",
    {
        "FilterOperation": CustomActionFilterOperationTypeDef,
        "NavigationOperation": CustomActionNavigationOperationTypeDef,
        "URLOperation": CustomActionURLOperationTypeDef,
        "SetParametersOperation": CustomActionSetParametersOperationTypeDef,
    },
    total=False,
)

LineSeriesAxisDisplayOptionsOutputTypeDef = TypedDict(
    "LineSeriesAxisDisplayOptionsOutputTypeDef",
    {
        "AxisOptions": AxisDisplayOptionsOutputTypeDef,
        "MissingDataConfigurations": List[MissingDataConfigurationTypeDef],
    },
    total=False,
)

LineSeriesAxisDisplayOptionsTypeDef = TypedDict(
    "LineSeriesAxisDisplayOptionsTypeDef",
    {
        "AxisOptions": AxisDisplayOptionsTypeDef,
        "MissingDataConfigurations": Sequence[MissingDataConfigurationTypeDef],
    },
    total=False,
)

FilterControlOutputTypeDef = TypedDict(
    "FilterControlOutputTypeDef",
    {
        "DateTimePicker": FilterDateTimePickerControlTypeDef,
        "List": FilterListControlOutputTypeDef,
        "Dropdown": FilterDropDownControlOutputTypeDef,
        "TextField": FilterTextFieldControlTypeDef,
        "TextArea": FilterTextAreaControlTypeDef,
        "Slider": FilterSliderControlTypeDef,
        "RelativeDateTime": FilterRelativeDateTimeControlTypeDef,
    },
    total=False,
)

FilterControlTypeDef = TypedDict(
    "FilterControlTypeDef",
    {
        "DateTimePicker": FilterDateTimePickerControlTypeDef,
        "List": FilterListControlTypeDef,
        "Dropdown": FilterDropDownControlTypeDef,
        "TextField": FilterTextFieldControlTypeDef,
        "TextArea": FilterTextAreaControlTypeDef,
        "Slider": FilterSliderControlTypeDef,
        "RelativeDateTime": FilterRelativeDateTimeControlTypeDef,
    },
    total=False,
)

ParameterControlOutputTypeDef = TypedDict(
    "ParameterControlOutputTypeDef",
    {
        "DateTimePicker": ParameterDateTimePickerControlTypeDef,
        "List": ParameterListControlOutputTypeDef,
        "Dropdown": ParameterDropDownControlOutputTypeDef,
        "TextField": ParameterTextFieldControlTypeDef,
        "TextArea": ParameterTextAreaControlTypeDef,
        "Slider": ParameterSliderControlTypeDef,
    },
    total=False,
)

ParameterControlTypeDef = TypedDict(
    "ParameterControlTypeDef",
    {
        "DateTimePicker": ParameterDateTimePickerControlTypeDef,
        "List": ParameterListControlTypeDef,
        "Dropdown": ParameterDropDownControlTypeDef,
        "TextField": ParameterTextFieldControlTypeDef,
        "TextArea": ParameterTextAreaControlTypeDef,
        "Slider": ParameterSliderControlTypeDef,
    },
    total=False,
)

TableFieldURLConfigurationTypeDef = TypedDict(
    "TableFieldURLConfigurationTypeDef",
    {
        "LinkConfiguration": TableFieldLinkConfigurationTypeDef,
        "ImageConfiguration": TableFieldImageConfigurationTypeDef,
    },
    total=False,
)

PivotTableTotalOptionsOutputTypeDef = TypedDict(
    "PivotTableTotalOptionsOutputTypeDef",
    {
        "RowSubtotalOptions": SubtotalOptionsOutputTypeDef,
        "ColumnSubtotalOptions": SubtotalOptionsOutputTypeDef,
        "RowTotalOptions": PivotTotalOptionsTypeDef,
        "ColumnTotalOptions": PivotTotalOptionsTypeDef,
    },
    total=False,
)

PivotTableTotalOptionsTypeDef = TypedDict(
    "PivotTableTotalOptionsTypeDef",
    {
        "RowSubtotalOptions": SubtotalOptionsTypeDef,
        "ColumnSubtotalOptions": SubtotalOptionsTypeDef,
        "RowTotalOptions": PivotTotalOptionsTypeDef,
        "ColumnTotalOptions": PivotTotalOptionsTypeDef,
    },
    total=False,
)

GaugeChartConditionalFormattingOptionOutputTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOptionOutputTypeDef",
    {
        "PrimaryValue": GaugeChartPrimaryValueConditionalFormattingOutputTypeDef,
        "Arc": GaugeChartArcConditionalFormattingOutputTypeDef,
    },
    total=False,
)

KPIConditionalFormattingOptionOutputTypeDef = TypedDict(
    "KPIConditionalFormattingOptionOutputTypeDef",
    {
        "PrimaryValue": KPIPrimaryValueConditionalFormattingOutputTypeDef,
        "ProgressBar": KPIProgressBarConditionalFormattingOutputTypeDef,
    },
    total=False,
)

_RequiredFilledMapShapeConditionalFormattingOutputTypeDef = TypedDict(
    "_RequiredFilledMapShapeConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalFilledMapShapeConditionalFormattingOutputTypeDef = TypedDict(
    "_OptionalFilledMapShapeConditionalFormattingOutputTypeDef",
    {
        "Format": ShapeConditionalFormatOutputTypeDef,
    },
    total=False,
)


class FilledMapShapeConditionalFormattingOutputTypeDef(
    _RequiredFilledMapShapeConditionalFormattingOutputTypeDef,
    _OptionalFilledMapShapeConditionalFormattingOutputTypeDef,
):
    pass


_RequiredPivotTableCellConditionalFormattingOutputTypeDef = TypedDict(
    "_RequiredPivotTableCellConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalPivotTableCellConditionalFormattingOutputTypeDef = TypedDict(
    "_OptionalPivotTableCellConditionalFormattingOutputTypeDef",
    {
        "TextFormat": TextConditionalFormatOutputTypeDef,
        "Scope": PivotTableConditionalFormattingScopeTypeDef,
        "Scopes": List[PivotTableConditionalFormattingScopeTypeDef],
    },
    total=False,
)


class PivotTableCellConditionalFormattingOutputTypeDef(
    _RequiredPivotTableCellConditionalFormattingOutputTypeDef,
    _OptionalPivotTableCellConditionalFormattingOutputTypeDef,
):
    pass


_RequiredTableCellConditionalFormattingOutputTypeDef = TypedDict(
    "_RequiredTableCellConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalTableCellConditionalFormattingOutputTypeDef = TypedDict(
    "_OptionalTableCellConditionalFormattingOutputTypeDef",
    {
        "TextFormat": TextConditionalFormatOutputTypeDef,
    },
    total=False,
)


class TableCellConditionalFormattingOutputTypeDef(
    _RequiredTableCellConditionalFormattingOutputTypeDef,
    _OptionalTableCellConditionalFormattingOutputTypeDef,
):
    pass


GaugeChartConditionalFormattingOptionTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": GaugeChartPrimaryValueConditionalFormattingTypeDef,
        "Arc": GaugeChartArcConditionalFormattingTypeDef,
    },
    total=False,
)

KPIConditionalFormattingOptionTypeDef = TypedDict(
    "KPIConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": KPIPrimaryValueConditionalFormattingTypeDef,
        "ProgressBar": KPIProgressBarConditionalFormattingTypeDef,
    },
    total=False,
)

_RequiredFilledMapShapeConditionalFormattingTypeDef = TypedDict(
    "_RequiredFilledMapShapeConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalFilledMapShapeConditionalFormattingTypeDef = TypedDict(
    "_OptionalFilledMapShapeConditionalFormattingTypeDef",
    {
        "Format": ShapeConditionalFormatTypeDef,
    },
    total=False,
)


class FilledMapShapeConditionalFormattingTypeDef(
    _RequiredFilledMapShapeConditionalFormattingTypeDef,
    _OptionalFilledMapShapeConditionalFormattingTypeDef,
):
    pass


_RequiredPivotTableCellConditionalFormattingTypeDef = TypedDict(
    "_RequiredPivotTableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalPivotTableCellConditionalFormattingTypeDef = TypedDict(
    "_OptionalPivotTableCellConditionalFormattingTypeDef",
    {
        "TextFormat": TextConditionalFormatTypeDef,
        "Scope": PivotTableConditionalFormattingScopeTypeDef,
        "Scopes": Sequence[PivotTableConditionalFormattingScopeTypeDef],
    },
    total=False,
)


class PivotTableCellConditionalFormattingTypeDef(
    _RequiredPivotTableCellConditionalFormattingTypeDef,
    _OptionalPivotTableCellConditionalFormattingTypeDef,
):
    pass


_RequiredTableCellConditionalFormattingTypeDef = TypedDict(
    "_RequiredTableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalTableCellConditionalFormattingTypeDef = TypedDict(
    "_OptionalTableCellConditionalFormattingTypeDef",
    {
        "TextFormat": TextConditionalFormatTypeDef,
    },
    total=False,
)


class TableCellConditionalFormattingTypeDef(
    _RequiredTableCellConditionalFormattingTypeDef, _OptionalTableCellConditionalFormattingTypeDef
):
    pass


DescribeAssetBundleImportJobResponseTypeDef = TypedDict(
    "DescribeAssetBundleImportJobResponseTypeDef",
    {
        "JobStatus": AssetBundleImportJobStatusType,
        "Errors": List[AssetBundleImportJobErrorTypeDef],
        "RollbackErrors": List[AssetBundleImportJobErrorTypeDef],
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleImportJobId": str,
        "AwsAccountId": str,
        "AssetBundleImportSource": AssetBundleImportSourceDescriptionTypeDef,
        "OverrideParameters": AssetBundleImportJobOverrideParametersOutputTypeDef,
        "FailureAction": AssetBundleImportFailureActionType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredStartAssetBundleImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartAssetBundleImportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleImportJobId": str,
        "AssetBundleImportSource": AssetBundleImportSourceTypeDef,
    },
)
_OptionalStartAssetBundleImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartAssetBundleImportJobRequestRequestTypeDef",
    {
        "OverrideParameters": AssetBundleImportJobOverrideParametersTypeDef,
        "FailureAction": AssetBundleImportFailureActionType,
    },
    total=False,
)


class StartAssetBundleImportJobRequestRequestTypeDef(
    _RequiredStartAssetBundleImportJobRequestRequestTypeDef,
    _OptionalStartAssetBundleImportJobRequestRequestTypeDef,
):
    pass


_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "DataSourceParameters": DataSourceParametersTypeDef,
        "Credentials": DataSourceCredentialsTypeDef,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "VpcConnectionProperties": VpcConnectionPropertiesTypeDef,
        "SslProperties": SslPropertiesTypeDef,
        "Tags": Sequence[TagTypeDef],
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
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "DataSourceParameters": DataSourceParametersTypeDef,
        "Credentials": DataSourceCredentialsTypeDef,
        "VpcConnectionProperties": VpcConnectionPropertiesTypeDef,
        "SslProperties": SslPropertiesTypeDef,
    },
    total=False,
)


class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass


ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ThemeId": str,
        "Version": ThemeVersionTypeDef,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Type": ThemeTypeType,
    },
    total=False,
)

GaugeChartOptionsTypeDef = TypedDict(
    "GaugeChartOptionsTypeDef",
    {
        "PrimaryValueDisplayType": PrimaryValueDisplayTypeType,
        "Comparison": ComparisonConfigurationTypeDef,
        "ArcAxis": ArcAxisConfigurationTypeDef,
        "Arc": ArcConfigurationTypeDef,
        "PrimaryValueFontConfiguration": FontConfigurationTypeDef,
    },
    total=False,
)

KPIOptionsTypeDef = TypedDict(
    "KPIOptionsTypeDef",
    {
        "ProgressBar": ProgressBarOptionsTypeDef,
        "TrendArrows": TrendArrowOptionsTypeDef,
        "SecondaryValue": SecondaryValueOptionsTypeDef,
        "Comparison": ComparisonConfigurationTypeDef,
        "PrimaryValueDisplayType": PrimaryValueDisplayTypeType,
        "PrimaryValueFontConfiguration": FontConfigurationTypeDef,
        "SecondaryValueFontConfiguration": FontConfigurationTypeDef,
    },
    total=False,
)

_RequiredDateDimensionFieldTypeDef = TypedDict(
    "_RequiredDateDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalDateDimensionFieldTypeDef = TypedDict(
    "_OptionalDateDimensionFieldTypeDef",
    {
        "DateGranularity": TimeGranularityType,
        "HierarchyId": str,
        "FormatConfiguration": DateTimeFormatConfigurationTypeDef,
    },
    total=False,
)


class DateDimensionFieldTypeDef(
    _RequiredDateDimensionFieldTypeDef, _OptionalDateDimensionFieldTypeDef
):
    pass


_RequiredDateMeasureFieldTypeDef = TypedDict(
    "_RequiredDateMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalDateMeasureFieldTypeDef = TypedDict(
    "_OptionalDateMeasureFieldTypeDef",
    {
        "AggregationFunction": DateAggregationFunctionType,
        "FormatConfiguration": DateTimeFormatConfigurationTypeDef,
    },
    total=False,
)


class DateMeasureFieldTypeDef(_RequiredDateMeasureFieldTypeDef, _OptionalDateMeasureFieldTypeDef):
    pass


_RequiredNumericalDimensionFieldTypeDef = TypedDict(
    "_RequiredNumericalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalNumericalDimensionFieldTypeDef = TypedDict(
    "_OptionalNumericalDimensionFieldTypeDef",
    {
        "HierarchyId": str,
        "FormatConfiguration": NumberFormatConfigurationTypeDef,
    },
    total=False,
)


class NumericalDimensionFieldTypeDef(
    _RequiredNumericalDimensionFieldTypeDef, _OptionalNumericalDimensionFieldTypeDef
):
    pass


_RequiredNumericalMeasureFieldTypeDef = TypedDict(
    "_RequiredNumericalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalNumericalMeasureFieldTypeDef = TypedDict(
    "_OptionalNumericalMeasureFieldTypeDef",
    {
        "AggregationFunction": NumericalAggregationFunctionTypeDef,
        "FormatConfiguration": NumberFormatConfigurationTypeDef,
    },
    total=False,
)


class NumericalMeasureFieldTypeDef(
    _RequiredNumericalMeasureFieldTypeDef, _OptionalNumericalMeasureFieldTypeDef
):
    pass


ReferenceLineLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineLabelConfigurationTypeDef",
    {
        "ValueLabelConfiguration": ReferenceLineValueLabelConfigurationTypeDef,
        "CustomLabelConfiguration": ReferenceLineCustomLabelConfigurationTypeDef,
        "FontConfiguration": FontConfigurationTypeDef,
        "FontColor": str,
        "HorizontalPosition": ReferenceLineLabelHorizontalPositionType,
        "VerticalPosition": ReferenceLineLabelVerticalPositionType,
    },
    total=False,
)

_RequiredCategoricalDimensionFieldTypeDef = TypedDict(
    "_RequiredCategoricalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalCategoricalDimensionFieldTypeDef = TypedDict(
    "_OptionalCategoricalDimensionFieldTypeDef",
    {
        "HierarchyId": str,
        "FormatConfiguration": StringFormatConfigurationTypeDef,
    },
    total=False,
)


class CategoricalDimensionFieldTypeDef(
    _RequiredCategoricalDimensionFieldTypeDef, _OptionalCategoricalDimensionFieldTypeDef
):
    pass


_RequiredCategoricalMeasureFieldTypeDef = TypedDict(
    "_RequiredCategoricalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalCategoricalMeasureFieldTypeDef = TypedDict(
    "_OptionalCategoricalMeasureFieldTypeDef",
    {
        "AggregationFunction": CategoricalAggregationFunctionType,
        "FormatConfiguration": StringFormatConfigurationTypeDef,
    },
    total=False,
)


class CategoricalMeasureFieldTypeDef(
    _RequiredCategoricalMeasureFieldTypeDef, _OptionalCategoricalMeasureFieldTypeDef
):
    pass


FormatConfigurationTypeDef = TypedDict(
    "FormatConfigurationTypeDef",
    {
        "StringFormatConfiguration": StringFormatConfigurationTypeDef,
        "NumberFormatConfiguration": NumberFormatConfigurationTypeDef,
        "DateTimeFormatConfiguration": DateTimeFormatConfigurationTypeDef,
    },
    total=False,
)

FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "CategoryFilter": CategoryFilterOutputTypeDef,
        "NumericRangeFilter": NumericRangeFilterTypeDef,
        "NumericEqualityFilter": NumericEqualityFilterTypeDef,
        "TimeEqualityFilter": TimeEqualityFilterOutputTypeDef,
        "TimeRangeFilter": TimeRangeFilterOutputTypeDef,
        "RelativeDatesFilter": RelativeDatesFilterTypeDef,
        "TopBottomFilter": TopBottomFilterOutputTypeDef,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "CategoryFilter": CategoryFilterTypeDef,
        "NumericRangeFilter": NumericRangeFilterTypeDef,
        "NumericEqualityFilter": NumericEqualityFilterTypeDef,
        "TimeEqualityFilter": TimeEqualityFilterTypeDef,
        "TimeRangeFilter": TimeRangeFilterTypeDef,
        "RelativeDatesFilter": RelativeDatesFilterTypeDef,
        "TopBottomFilter": TopBottomFilterTypeDef,
    },
    total=False,
)

BarChartSortConfigurationOutputTypeDef = TypedDict(
    "BarChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": List[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": List[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

BarChartSortConfigurationTypeDef = TypedDict(
    "BarChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": Sequence[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": Sequence[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

BoxPlotSortConfigurationOutputTypeDef = TypedDict(
    "BoxPlotSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "PaginationConfiguration": PaginationConfigurationTypeDef,
    },
    total=False,
)

BoxPlotSortConfigurationTypeDef = TypedDict(
    "BoxPlotSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "PaginationConfiguration": PaginationConfigurationTypeDef,
    },
    total=False,
)

ComboChartSortConfigurationOutputTypeDef = TypedDict(
    "ComboChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": List[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

ComboChartSortConfigurationTypeDef = TypedDict(
    "ComboChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": Sequence[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

FilledMapSortConfigurationOutputTypeDef = TypedDict(
    "FilledMapSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
    },
    total=False,
)

FilledMapSortConfigurationTypeDef = TypedDict(
    "FilledMapSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
    },
    total=False,
)

FunnelChartSortConfigurationOutputTypeDef = TypedDict(
    "FunnelChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

FunnelChartSortConfigurationTypeDef = TypedDict(
    "FunnelChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

HeatMapSortConfigurationOutputTypeDef = TypedDict(
    "HeatMapSortConfigurationOutputTypeDef",
    {
        "HeatMapRowSort": List[FieldSortOptionsTypeDef],
        "HeatMapColumnSort": List[FieldSortOptionsTypeDef],
        "HeatMapRowItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "HeatMapColumnItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

HeatMapSortConfigurationTypeDef = TypedDict(
    "HeatMapSortConfigurationTypeDef",
    {
        "HeatMapRowSort": Sequence[FieldSortOptionsTypeDef],
        "HeatMapColumnSort": Sequence[FieldSortOptionsTypeDef],
        "HeatMapRowItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "HeatMapColumnItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

KPISortConfigurationOutputTypeDef = TypedDict(
    "KPISortConfigurationOutputTypeDef",
    {
        "TrendGroupSort": List[FieldSortOptionsTypeDef],
    },
    total=False,
)

KPISortConfigurationTypeDef = TypedDict(
    "KPISortConfigurationTypeDef",
    {
        "TrendGroupSort": Sequence[FieldSortOptionsTypeDef],
    },
    total=False,
)

LineChartSortConfigurationOutputTypeDef = TypedDict(
    "LineChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "ColorItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": List[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

LineChartSortConfigurationTypeDef = TypedDict(
    "LineChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "ColorItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": Sequence[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

PieChartSortConfigurationOutputTypeDef = TypedDict(
    "PieChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": List[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

PieChartSortConfigurationTypeDef = TypedDict(
    "PieChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "SmallMultiplesSort": Sequence[FieldSortOptionsTypeDef],
        "SmallMultiplesLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

RadarChartSortConfigurationOutputTypeDef = TypedDict(
    "RadarChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": List[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

RadarChartSortConfigurationTypeDef = TypedDict(
    "RadarChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "ColorSort": Sequence[FieldSortOptionsTypeDef],
        "ColorItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

SankeyDiagramSortConfigurationOutputTypeDef = TypedDict(
    "SankeyDiagramSortConfigurationOutputTypeDef",
    {
        "WeightSort": List[FieldSortOptionsTypeDef],
        "SourceItemsLimit": ItemsLimitConfigurationTypeDef,
        "DestinationItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

SankeyDiagramSortConfigurationTypeDef = TypedDict(
    "SankeyDiagramSortConfigurationTypeDef",
    {
        "WeightSort": Sequence[FieldSortOptionsTypeDef],
        "SourceItemsLimit": ItemsLimitConfigurationTypeDef,
        "DestinationItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

TableSortConfigurationOutputTypeDef = TypedDict(
    "TableSortConfigurationOutputTypeDef",
    {
        "RowSort": List[FieldSortOptionsTypeDef],
        "PaginationConfiguration": PaginationConfigurationTypeDef,
    },
    total=False,
)

TableSortConfigurationTypeDef = TypedDict(
    "TableSortConfigurationTypeDef",
    {
        "RowSort": Sequence[FieldSortOptionsTypeDef],
        "PaginationConfiguration": PaginationConfigurationTypeDef,
    },
    total=False,
)

TreeMapSortConfigurationOutputTypeDef = TypedDict(
    "TreeMapSortConfigurationOutputTypeDef",
    {
        "TreeMapSort": List[FieldSortOptionsTypeDef],
        "TreeMapGroupItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

TreeMapSortConfigurationTypeDef = TypedDict(
    "TreeMapSortConfigurationTypeDef",
    {
        "TreeMapSort": Sequence[FieldSortOptionsTypeDef],
        "TreeMapGroupItemsLimitConfiguration": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

WaterfallChartSortConfigurationOutputTypeDef = TypedDict(
    "WaterfallChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": List[FieldSortOptionsTypeDef],
        "BreakdownItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

WaterfallChartSortConfigurationTypeDef = TypedDict(
    "WaterfallChartSortConfigurationTypeDef",
    {
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
        "BreakdownItemsLimit": ItemsLimitConfigurationTypeDef,
    },
    total=False,
)

WordCloudSortConfigurationOutputTypeDef = TypedDict(
    "WordCloudSortConfigurationOutputTypeDef",
    {
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "CategorySort": List[FieldSortOptionsTypeDef],
    },
    total=False,
)

WordCloudSortConfigurationTypeDef = TypedDict(
    "WordCloudSortConfigurationTypeDef",
    {
        "CategoryItemsLimit": ItemsLimitConfigurationTypeDef,
        "CategorySort": Sequence[FieldSortOptionsTypeDef],
    },
    total=False,
)

PivotFieldSortOptionsOutputTypeDef = TypedDict(
    "PivotFieldSortOptionsOutputTypeDef",
    {
        "FieldId": str,
        "SortBy": PivotTableSortByOutputTypeDef,
    },
)

PivotFieldSortOptionsTypeDef = TypedDict(
    "PivotFieldSortOptionsTypeDef",
    {
        "FieldId": str,
        "SortBy": PivotTableSortByTypeDef,
    },
)

FieldBasedTooltipOutputTypeDef = TypedDict(
    "FieldBasedTooltipOutputTypeDef",
    {
        "AggregationVisibility": VisibilityType,
        "TooltipTitleType": TooltipTitleTypeType,
        "TooltipFields": List[TooltipItemTypeDef],
    },
    total=False,
)

FieldBasedTooltipTypeDef = TypedDict(
    "FieldBasedTooltipTypeDef",
    {
        "AggregationVisibility": VisibilityType,
        "TooltipTitleType": TooltipTitleTypeType,
        "TooltipFields": Sequence[TooltipItemTypeDef],
    },
    total=False,
)

TopicDetailsOutputTypeDef = TypedDict(
    "TopicDetailsOutputTypeDef",
    {
        "Name": str,
        "Description": str,
        "DataSets": List[DatasetMetadataOutputTypeDef],
    },
    total=False,
)

TopicDetailsTypeDef = TypedDict(
    "TopicDetailsTypeDef",
    {
        "Name": str,
        "Description": str,
        "DataSets": Sequence[DatasetMetadataTypeDef],
    },
    total=False,
)

SnapshotJobResultTypeDef = TypedDict(
    "SnapshotJobResultTypeDef",
    {
        "AnonymousUsers": List[AnonymousUserSnapshotJobResultTypeDef],
    },
    total=False,
)

DefaultNewSheetConfigurationTypeDef = TypedDict(
    "DefaultNewSheetConfigurationTypeDef",
    {
        "InteractiveLayoutConfiguration": DefaultInteractiveLayoutConfigurationTypeDef,
        "PaginatedLayoutConfiguration": DefaultPaginatedLayoutConfigurationTypeDef,
        "SheetContentType": SheetContentTypeType,
    },
    total=False,
)

BodySectionContentOutputTypeDef = TypedDict(
    "BodySectionContentOutputTypeDef",
    {
        "Layout": SectionLayoutConfigurationOutputTypeDef,
    },
    total=False,
)

_RequiredHeaderFooterSectionConfigurationOutputTypeDef = TypedDict(
    "_RequiredHeaderFooterSectionConfigurationOutputTypeDef",
    {
        "SectionId": str,
        "Layout": SectionLayoutConfigurationOutputTypeDef,
    },
)
_OptionalHeaderFooterSectionConfigurationOutputTypeDef = TypedDict(
    "_OptionalHeaderFooterSectionConfigurationOutputTypeDef",
    {
        "Style": SectionStyleTypeDef,
    },
    total=False,
)


class HeaderFooterSectionConfigurationOutputTypeDef(
    _RequiredHeaderFooterSectionConfigurationOutputTypeDef,
    _OptionalHeaderFooterSectionConfigurationOutputTypeDef,
):
    pass


BodySectionContentTypeDef = TypedDict(
    "BodySectionContentTypeDef",
    {
        "Layout": SectionLayoutConfigurationTypeDef,
    },
    total=False,
)

_RequiredHeaderFooterSectionConfigurationTypeDef = TypedDict(
    "_RequiredHeaderFooterSectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Layout": SectionLayoutConfigurationTypeDef,
    },
)
_OptionalHeaderFooterSectionConfigurationTypeDef = TypedDict(
    "_OptionalHeaderFooterSectionConfigurationTypeDef",
    {
        "Style": SectionStyleTypeDef,
    },
    total=False,
)


class HeaderFooterSectionConfigurationTypeDef(
    _RequiredHeaderFooterSectionConfigurationTypeDef,
    _OptionalHeaderFooterSectionConfigurationTypeDef,
):
    pass


DescribeDataSetResponseTypeDef = TypedDict(
    "DescribeDataSetResponseTypeDef",
    {
        "DataSet": DataSetTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredVisualCustomActionOutputTypeDef = TypedDict(
    "_RequiredVisualCustomActionOutputTypeDef",
    {
        "CustomActionId": str,
        "Name": str,
        "Trigger": VisualCustomActionTriggerType,
        "ActionOperations": List[VisualCustomActionOperationOutputTypeDef],
    },
)
_OptionalVisualCustomActionOutputTypeDef = TypedDict(
    "_OptionalVisualCustomActionOutputTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)


class VisualCustomActionOutputTypeDef(
    _RequiredVisualCustomActionOutputTypeDef, _OptionalVisualCustomActionOutputTypeDef
):
    pass


_RequiredVisualCustomActionTypeDef = TypedDict(
    "_RequiredVisualCustomActionTypeDef",
    {
        "CustomActionId": str,
        "Name": str,
        "Trigger": VisualCustomActionTriggerType,
        "ActionOperations": Sequence[VisualCustomActionOperationTypeDef],
    },
)
_OptionalVisualCustomActionTypeDef = TypedDict(
    "_OptionalVisualCustomActionTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)


class VisualCustomActionTypeDef(
    _RequiredVisualCustomActionTypeDef, _OptionalVisualCustomActionTypeDef
):
    pass


_RequiredTableFieldOptionTypeDef = TypedDict(
    "_RequiredTableFieldOptionTypeDef",
    {
        "FieldId": str,
    },
)
_OptionalTableFieldOptionTypeDef = TypedDict(
    "_OptionalTableFieldOptionTypeDef",
    {
        "Width": str,
        "CustomLabel": str,
        "Visibility": VisibilityType,
        "URLStyling": TableFieldURLConfigurationTypeDef,
    },
    total=False,
)


class TableFieldOptionTypeDef(_RequiredTableFieldOptionTypeDef, _OptionalTableFieldOptionTypeDef):
    pass


GaugeChartConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[GaugeChartConditionalFormattingOptionOutputTypeDef],
    },
    total=False,
)

KPIConditionalFormattingOutputTypeDef = TypedDict(
    "KPIConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[KPIConditionalFormattingOptionOutputTypeDef],
    },
    total=False,
)

FilledMapConditionalFormattingOptionOutputTypeDef = TypedDict(
    "FilledMapConditionalFormattingOptionOutputTypeDef",
    {
        "Shape": FilledMapShapeConditionalFormattingOutputTypeDef,
    },
)

PivotTableConditionalFormattingOptionOutputTypeDef = TypedDict(
    "PivotTableConditionalFormattingOptionOutputTypeDef",
    {
        "Cell": PivotTableCellConditionalFormattingOutputTypeDef,
    },
    total=False,
)

TableConditionalFormattingOptionOutputTypeDef = TypedDict(
    "TableConditionalFormattingOptionOutputTypeDef",
    {
        "Cell": TableCellConditionalFormattingOutputTypeDef,
        "Row": TableRowConditionalFormattingOutputTypeDef,
    },
    total=False,
)

GaugeChartConditionalFormattingTypeDef = TypedDict(
    "GaugeChartConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[GaugeChartConditionalFormattingOptionTypeDef],
    },
    total=False,
)

KPIConditionalFormattingTypeDef = TypedDict(
    "KPIConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[KPIConditionalFormattingOptionTypeDef],
    },
    total=False,
)

FilledMapConditionalFormattingOptionTypeDef = TypedDict(
    "FilledMapConditionalFormattingOptionTypeDef",
    {
        "Shape": FilledMapShapeConditionalFormattingTypeDef,
    },
)

PivotTableConditionalFormattingOptionTypeDef = TypedDict(
    "PivotTableConditionalFormattingOptionTypeDef",
    {
        "Cell": PivotTableCellConditionalFormattingTypeDef,
    },
    total=False,
)

TableConditionalFormattingOptionTypeDef = TypedDict(
    "TableConditionalFormattingOptionTypeDef",
    {
        "Cell": TableCellConditionalFormattingTypeDef,
        "Row": TableRowConditionalFormattingTypeDef,
    },
    total=False,
)

DescribeThemeResponseTypeDef = TypedDict(
    "DescribeThemeResponseTypeDef",
    {
        "Theme": ThemeTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredReferenceLineTypeDef = TypedDict(
    "_RequiredReferenceLineTypeDef",
    {
        "DataConfiguration": ReferenceLineDataConfigurationTypeDef,
    },
)
_OptionalReferenceLineTypeDef = TypedDict(
    "_OptionalReferenceLineTypeDef",
    {
        "Status": WidgetStatusType,
        "StyleConfiguration": ReferenceLineStyleConfigurationTypeDef,
        "LabelConfiguration": ReferenceLineLabelConfigurationTypeDef,
    },
    total=False,
)


class ReferenceLineTypeDef(_RequiredReferenceLineTypeDef, _OptionalReferenceLineTypeDef):
    pass


DimensionFieldTypeDef = TypedDict(
    "DimensionFieldTypeDef",
    {
        "NumericalDimensionField": NumericalDimensionFieldTypeDef,
        "CategoricalDimensionField": CategoricalDimensionFieldTypeDef,
        "DateDimensionField": DateDimensionFieldTypeDef,
    },
    total=False,
)

MeasureFieldTypeDef = TypedDict(
    "MeasureFieldTypeDef",
    {
        "NumericalMeasureField": NumericalMeasureFieldTypeDef,
        "CategoricalMeasureField": CategoricalMeasureFieldTypeDef,
        "DateMeasureField": DateMeasureFieldTypeDef,
        "CalculatedMeasureField": CalculatedMeasureFieldTypeDef,
    },
    total=False,
)

_RequiredColumnConfigurationOutputTypeDef = TypedDict(
    "_RequiredColumnConfigurationOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalColumnConfigurationOutputTypeDef = TypedDict(
    "_OptionalColumnConfigurationOutputTypeDef",
    {
        "FormatConfiguration": FormatConfigurationTypeDef,
        "Role": ColumnRoleType,
        "ColorsConfiguration": ColorsConfigurationOutputTypeDef,
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
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalColumnConfigurationTypeDef = TypedDict(
    "_OptionalColumnConfigurationTypeDef",
    {
        "FormatConfiguration": FormatConfigurationTypeDef,
        "Role": ColumnRoleType,
        "ColorsConfiguration": ColorsConfigurationTypeDef,
    },
    total=False,
)


class ColumnConfigurationTypeDef(
    _RequiredColumnConfigurationTypeDef, _OptionalColumnConfigurationTypeDef
):
    pass


_RequiredUnaggregatedFieldTypeDef = TypedDict(
    "_RequiredUnaggregatedFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
_OptionalUnaggregatedFieldTypeDef = TypedDict(
    "_OptionalUnaggregatedFieldTypeDef",
    {
        "FormatConfiguration": FormatConfigurationTypeDef,
    },
    total=False,
)


class UnaggregatedFieldTypeDef(
    _RequiredUnaggregatedFieldTypeDef, _OptionalUnaggregatedFieldTypeDef
):
    pass


_RequiredFilterGroupOutputTypeDef = TypedDict(
    "_RequiredFilterGroupOutputTypeDef",
    {
        "FilterGroupId": str,
        "Filters": List[FilterOutputTypeDef],
        "ScopeConfiguration": FilterScopeConfigurationOutputTypeDef,
        "CrossDataset": CrossDatasetTypesType,
    },
)
_OptionalFilterGroupOutputTypeDef = TypedDict(
    "_OptionalFilterGroupOutputTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)


class FilterGroupOutputTypeDef(
    _RequiredFilterGroupOutputTypeDef, _OptionalFilterGroupOutputTypeDef
):
    pass


_RequiredFilterGroupTypeDef = TypedDict(
    "_RequiredFilterGroupTypeDef",
    {
        "FilterGroupId": str,
        "Filters": Sequence[FilterTypeDef],
        "ScopeConfiguration": FilterScopeConfigurationTypeDef,
        "CrossDataset": CrossDatasetTypesType,
    },
)
_OptionalFilterGroupTypeDef = TypedDict(
    "_OptionalFilterGroupTypeDef",
    {
        "Status": WidgetStatusType,
    },
    total=False,
)


class FilterGroupTypeDef(_RequiredFilterGroupTypeDef, _OptionalFilterGroupTypeDef):
    pass


PivotTableSortConfigurationOutputTypeDef = TypedDict(
    "PivotTableSortConfigurationOutputTypeDef",
    {
        "FieldSortOptions": List[PivotFieldSortOptionsOutputTypeDef],
    },
    total=False,
)

PivotTableSortConfigurationTypeDef = TypedDict(
    "PivotTableSortConfigurationTypeDef",
    {
        "FieldSortOptions": Sequence[PivotFieldSortOptionsTypeDef],
    },
    total=False,
)

TooltipOptionsOutputTypeDef = TypedDict(
    "TooltipOptionsOutputTypeDef",
    {
        "TooltipVisibility": VisibilityType,
        "SelectedTooltipType": SelectedTooltipTypeType,
        "FieldBasedTooltip": FieldBasedTooltipOutputTypeDef,
    },
    total=False,
)

TooltipOptionsTypeDef = TypedDict(
    "TooltipOptionsTypeDef",
    {
        "TooltipVisibility": VisibilityType,
        "SelectedTooltipType": SelectedTooltipTypeType,
        "FieldBasedTooltip": FieldBasedTooltipTypeDef,
    },
    total=False,
)

DescribeTopicResponseTypeDef = TypedDict(
    "DescribeTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "Topic": TopicDetailsOutputTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateTopicRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "Topic": TopicDetailsTypeDef,
    },
)
_OptionalCreateTopicRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTopicRequestRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)


class CreateTopicRequestRequestTypeDef(
    _RequiredCreateTopicRequestRequestTypeDef, _OptionalCreateTopicRequestRequestTypeDef
):
    pass


UpdateTopicRequestRequestTypeDef = TypedDict(
    "UpdateTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "Topic": TopicDetailsTypeDef,
    },
)

DescribeDashboardSnapshotJobResultResponseTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResultResponseTypeDef",
    {
        "Arn": str,
        "JobStatus": SnapshotJobStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Result": SnapshotJobResultTypeDef,
        "ErrorInfo": SnapshotJobErrorInfoTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AnalysisDefaultsTypeDef = TypedDict(
    "AnalysisDefaultsTypeDef",
    {
        "DefaultNewSheetConfiguration": DefaultNewSheetConfigurationTypeDef,
    },
)

_RequiredBodySectionConfigurationOutputTypeDef = TypedDict(
    "_RequiredBodySectionConfigurationOutputTypeDef",
    {
        "SectionId": str,
        "Content": BodySectionContentOutputTypeDef,
    },
)
_OptionalBodySectionConfigurationOutputTypeDef = TypedDict(
    "_OptionalBodySectionConfigurationOutputTypeDef",
    {
        "Style": SectionStyleTypeDef,
        "PageBreakConfiguration": SectionPageBreakConfigurationTypeDef,
    },
    total=False,
)


class BodySectionConfigurationOutputTypeDef(
    _RequiredBodySectionConfigurationOutputTypeDef, _OptionalBodySectionConfigurationOutputTypeDef
):
    pass


_RequiredBodySectionConfigurationTypeDef = TypedDict(
    "_RequiredBodySectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Content": BodySectionContentTypeDef,
    },
)
_OptionalBodySectionConfigurationTypeDef = TypedDict(
    "_OptionalBodySectionConfigurationTypeDef",
    {
        "Style": SectionStyleTypeDef,
        "PageBreakConfiguration": SectionPageBreakConfigurationTypeDef,
    },
    total=False,
)


class BodySectionConfigurationTypeDef(
    _RequiredBodySectionConfigurationTypeDef, _OptionalBodySectionConfigurationTypeDef
):
    pass


_RequiredCustomContentVisualOutputTypeDef = TypedDict(
    "_RequiredCustomContentVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalCustomContentVisualOutputTypeDef = TypedDict(
    "_OptionalCustomContentVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": CustomContentConfigurationTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class CustomContentVisualOutputTypeDef(
    _RequiredCustomContentVisualOutputTypeDef, _OptionalCustomContentVisualOutputTypeDef
):
    pass


_RequiredEmptyVisualOutputTypeDef = TypedDict(
    "_RequiredEmptyVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalEmptyVisualOutputTypeDef = TypedDict(
    "_OptionalEmptyVisualOutputTypeDef",
    {
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class EmptyVisualOutputTypeDef(
    _RequiredEmptyVisualOutputTypeDef, _OptionalEmptyVisualOutputTypeDef
):
    pass


_RequiredCustomContentVisualTypeDef = TypedDict(
    "_RequiredCustomContentVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalCustomContentVisualTypeDef = TypedDict(
    "_OptionalCustomContentVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": CustomContentConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class CustomContentVisualTypeDef(
    _RequiredCustomContentVisualTypeDef, _OptionalCustomContentVisualTypeDef
):
    pass


_RequiredEmptyVisualTypeDef = TypedDict(
    "_RequiredEmptyVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalEmptyVisualTypeDef = TypedDict(
    "_OptionalEmptyVisualTypeDef",
    {
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class EmptyVisualTypeDef(_RequiredEmptyVisualTypeDef, _OptionalEmptyVisualTypeDef):
    pass


TableFieldOptionsOutputTypeDef = TypedDict(
    "TableFieldOptionsOutputTypeDef",
    {
        "SelectedFieldOptions": List[TableFieldOptionTypeDef],
        "Order": List[str],
    },
    total=False,
)

TableFieldOptionsTypeDef = TypedDict(
    "TableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": Sequence[TableFieldOptionTypeDef],
        "Order": Sequence[str],
    },
    total=False,
)

FilledMapConditionalFormattingOutputTypeDef = TypedDict(
    "FilledMapConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[FilledMapConditionalFormattingOptionOutputTypeDef],
    },
)

PivotTableConditionalFormattingOutputTypeDef = TypedDict(
    "PivotTableConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[PivotTableConditionalFormattingOptionOutputTypeDef],
    },
    total=False,
)

TableConditionalFormattingOutputTypeDef = TypedDict(
    "TableConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[TableConditionalFormattingOptionOutputTypeDef],
    },
    total=False,
)

FilledMapConditionalFormattingTypeDef = TypedDict(
    "FilledMapConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[FilledMapConditionalFormattingOptionTypeDef],
    },
)

PivotTableConditionalFormattingTypeDef = TypedDict(
    "PivotTableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[PivotTableConditionalFormattingOptionTypeDef],
    },
    total=False,
)

TableConditionalFormattingTypeDef = TypedDict(
    "TableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[TableConditionalFormattingOptionTypeDef],
    },
    total=False,
)

_RequiredUniqueValuesComputationTypeDef = TypedDict(
    "_RequiredUniqueValuesComputationTypeDef",
    {
        "ComputationId": str,
        "Category": DimensionFieldTypeDef,
    },
)
_OptionalUniqueValuesComputationTypeDef = TypedDict(
    "_OptionalUniqueValuesComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UniqueValuesComputationTypeDef(
    _RequiredUniqueValuesComputationTypeDef, _OptionalUniqueValuesComputationTypeDef
):
    pass


BarChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "BarChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
        "Colors": List[DimensionFieldTypeDef],
        "SmallMultiples": List[DimensionFieldTypeDef],
    },
    total=False,
)

BarChartAggregatedFieldWellsTypeDef = TypedDict(
    "BarChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
        "Colors": Sequence[DimensionFieldTypeDef],
        "SmallMultiples": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

BoxPlotAggregatedFieldWellsOutputTypeDef = TypedDict(
    "BoxPlotAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

BoxPlotAggregatedFieldWellsTypeDef = TypedDict(
    "BoxPlotAggregatedFieldWellsTypeDef",
    {
        "GroupBy": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

ComboChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "ComboChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "BarValues": List[MeasureFieldTypeDef],
        "Colors": List[DimensionFieldTypeDef],
        "LineValues": List[MeasureFieldTypeDef],
    },
    total=False,
)

ComboChartAggregatedFieldWellsTypeDef = TypedDict(
    "ComboChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "BarValues": Sequence[MeasureFieldTypeDef],
        "Colors": Sequence[DimensionFieldTypeDef],
        "LineValues": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

FilledMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "FilledMapAggregatedFieldWellsOutputTypeDef",
    {
        "Geospatial": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

FilledMapAggregatedFieldWellsTypeDef = TypedDict(
    "FilledMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

_RequiredForecastComputationTypeDef = TypedDict(
    "_RequiredForecastComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
    },
)
_OptionalForecastComputationTypeDef = TypedDict(
    "_OptionalForecastComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
        "PeriodsForward": int,
        "PeriodsBackward": int,
        "UpperBoundary": float,
        "LowerBoundary": float,
        "PredictionInterval": int,
        "Seasonality": ForecastComputationSeasonalityType,
        "CustomSeasonalityValue": int,
    },
    total=False,
)


class ForecastComputationTypeDef(
    _RequiredForecastComputationTypeDef, _OptionalForecastComputationTypeDef
):
    pass


FunnelChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "FunnelChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

FunnelChartAggregatedFieldWellsTypeDef = TypedDict(
    "FunnelChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

GaugeChartFieldWellsOutputTypeDef = TypedDict(
    "GaugeChartFieldWellsOutputTypeDef",
    {
        "Values": List[MeasureFieldTypeDef],
        "TargetValues": List[MeasureFieldTypeDef],
    },
    total=False,
)

GaugeChartFieldWellsTypeDef = TypedDict(
    "GaugeChartFieldWellsTypeDef",
    {
        "Values": Sequence[MeasureFieldTypeDef],
        "TargetValues": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

GeospatialMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "GeospatialMapAggregatedFieldWellsOutputTypeDef",
    {
        "Geospatial": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
        "Colors": List[DimensionFieldTypeDef],
    },
    total=False,
)

GeospatialMapAggregatedFieldWellsTypeDef = TypedDict(
    "GeospatialMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
        "Colors": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

_RequiredGrowthRateComputationTypeDef = TypedDict(
    "_RequiredGrowthRateComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
    },
)
_OptionalGrowthRateComputationTypeDef = TypedDict(
    "_OptionalGrowthRateComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
        "PeriodSize": int,
    },
    total=False,
)


class GrowthRateComputationTypeDef(
    _RequiredGrowthRateComputationTypeDef, _OptionalGrowthRateComputationTypeDef
):
    pass


HeatMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "HeatMapAggregatedFieldWellsOutputTypeDef",
    {
        "Rows": List[DimensionFieldTypeDef],
        "Columns": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

HeatMapAggregatedFieldWellsTypeDef = TypedDict(
    "HeatMapAggregatedFieldWellsTypeDef",
    {
        "Rows": Sequence[DimensionFieldTypeDef],
        "Columns": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

HistogramAggregatedFieldWellsOutputTypeDef = TypedDict(
    "HistogramAggregatedFieldWellsOutputTypeDef",
    {
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

HistogramAggregatedFieldWellsTypeDef = TypedDict(
    "HistogramAggregatedFieldWellsTypeDef",
    {
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

KPIFieldWellsOutputTypeDef = TypedDict(
    "KPIFieldWellsOutputTypeDef",
    {
        "Values": List[MeasureFieldTypeDef],
        "TargetValues": List[MeasureFieldTypeDef],
        "TrendGroups": List[DimensionFieldTypeDef],
    },
    total=False,
)

KPIFieldWellsTypeDef = TypedDict(
    "KPIFieldWellsTypeDef",
    {
        "Values": Sequence[MeasureFieldTypeDef],
        "TargetValues": Sequence[MeasureFieldTypeDef],
        "TrendGroups": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

LineChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "LineChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
        "Colors": List[DimensionFieldTypeDef],
        "SmallMultiples": List[DimensionFieldTypeDef],
    },
    total=False,
)

LineChartAggregatedFieldWellsTypeDef = TypedDict(
    "LineChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
        "Colors": Sequence[DimensionFieldTypeDef],
        "SmallMultiples": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

_RequiredMaximumMinimumComputationTypeDef = TypedDict(
    "_RequiredMaximumMinimumComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
        "Type": MaximumMinimumComputationTypeType,
    },
)
_OptionalMaximumMinimumComputationTypeDef = TypedDict(
    "_OptionalMaximumMinimumComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
    },
    total=False,
)


class MaximumMinimumComputationTypeDef(
    _RequiredMaximumMinimumComputationTypeDef, _OptionalMaximumMinimumComputationTypeDef
):
    pass


_RequiredMetricComparisonComputationTypeDef = TypedDict(
    "_RequiredMetricComparisonComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
        "FromValue": MeasureFieldTypeDef,
        "TargetValue": MeasureFieldTypeDef,
    },
)
_OptionalMetricComparisonComputationTypeDef = TypedDict(
    "_OptionalMetricComparisonComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class MetricComparisonComputationTypeDef(
    _RequiredMetricComparisonComputationTypeDef, _OptionalMetricComparisonComputationTypeDef
):
    pass


_RequiredPeriodOverPeriodComputationTypeDef = TypedDict(
    "_RequiredPeriodOverPeriodComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
    },
)
_OptionalPeriodOverPeriodComputationTypeDef = TypedDict(
    "_OptionalPeriodOverPeriodComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
    },
    total=False,
)


class PeriodOverPeriodComputationTypeDef(
    _RequiredPeriodOverPeriodComputationTypeDef, _OptionalPeriodOverPeriodComputationTypeDef
):
    pass


_RequiredPeriodToDateComputationTypeDef = TypedDict(
    "_RequiredPeriodToDateComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
    },
)
_OptionalPeriodToDateComputationTypeDef = TypedDict(
    "_OptionalPeriodToDateComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
        "PeriodTimeGranularity": TimeGranularityType,
    },
    total=False,
)


class PeriodToDateComputationTypeDef(
    _RequiredPeriodToDateComputationTypeDef, _OptionalPeriodToDateComputationTypeDef
):
    pass


PieChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "PieChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
        "SmallMultiples": List[DimensionFieldTypeDef],
    },
    total=False,
)

PieChartAggregatedFieldWellsTypeDef = TypedDict(
    "PieChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
        "SmallMultiples": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

PivotTableAggregatedFieldWellsOutputTypeDef = TypedDict(
    "PivotTableAggregatedFieldWellsOutputTypeDef",
    {
        "Rows": List[DimensionFieldTypeDef],
        "Columns": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

PivotTableAggregatedFieldWellsTypeDef = TypedDict(
    "PivotTableAggregatedFieldWellsTypeDef",
    {
        "Rows": Sequence[DimensionFieldTypeDef],
        "Columns": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

RadarChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "RadarChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": List[DimensionFieldTypeDef],
        "Color": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

RadarChartAggregatedFieldWellsTypeDef = TypedDict(
    "RadarChartAggregatedFieldWellsTypeDef",
    {
        "Category": Sequence[DimensionFieldTypeDef],
        "Color": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

SankeyDiagramAggregatedFieldWellsOutputTypeDef = TypedDict(
    "SankeyDiagramAggregatedFieldWellsOutputTypeDef",
    {
        "Source": List[DimensionFieldTypeDef],
        "Destination": List[DimensionFieldTypeDef],
        "Weight": List[MeasureFieldTypeDef],
    },
    total=False,
)

SankeyDiagramAggregatedFieldWellsTypeDef = TypedDict(
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    {
        "Source": Sequence[DimensionFieldTypeDef],
        "Destination": Sequence[DimensionFieldTypeDef],
        "Weight": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef",
    {
        "XAxis": List[MeasureFieldTypeDef],
        "YAxis": List[MeasureFieldTypeDef],
        "Category": List[DimensionFieldTypeDef],
        "Size": List[MeasureFieldTypeDef],
        "Label": List[DimensionFieldTypeDef],
    },
    total=False,
)

ScatterPlotCategoricallyAggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    {
        "XAxis": Sequence[MeasureFieldTypeDef],
        "YAxis": Sequence[MeasureFieldTypeDef],
        "Category": Sequence[DimensionFieldTypeDef],
        "Size": Sequence[MeasureFieldTypeDef],
        "Label": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

ScatterPlotUnaggregatedFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotUnaggregatedFieldWellsOutputTypeDef",
    {
        "XAxis": List[DimensionFieldTypeDef],
        "YAxis": List[DimensionFieldTypeDef],
        "Size": List[MeasureFieldTypeDef],
        "Category": List[DimensionFieldTypeDef],
        "Label": List[DimensionFieldTypeDef],
    },
    total=False,
)

ScatterPlotUnaggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    {
        "XAxis": Sequence[DimensionFieldTypeDef],
        "YAxis": Sequence[DimensionFieldTypeDef],
        "Size": Sequence[MeasureFieldTypeDef],
        "Category": Sequence[DimensionFieldTypeDef],
        "Label": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

TableAggregatedFieldWellsOutputTypeDef = TypedDict(
    "TableAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
    },
    total=False,
)

TableAggregatedFieldWellsTypeDef = TypedDict(
    "TableAggregatedFieldWellsTypeDef",
    {
        "GroupBy": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

_RequiredTopBottomMoversComputationTypeDef = TypedDict(
    "_RequiredTopBottomMoversComputationTypeDef",
    {
        "ComputationId": str,
        "Time": DimensionFieldTypeDef,
        "Category": DimensionFieldTypeDef,
        "Type": TopBottomComputationTypeType,
    },
)
_OptionalTopBottomMoversComputationTypeDef = TypedDict(
    "_OptionalTopBottomMoversComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
        "MoverSize": int,
        "SortOrder": TopBottomSortOrderType,
    },
    total=False,
)


class TopBottomMoversComputationTypeDef(
    _RequiredTopBottomMoversComputationTypeDef, _OptionalTopBottomMoversComputationTypeDef
):
    pass


_RequiredTopBottomRankedComputationTypeDef = TypedDict(
    "_RequiredTopBottomRankedComputationTypeDef",
    {
        "ComputationId": str,
        "Category": DimensionFieldTypeDef,
        "Type": TopBottomComputationTypeType,
    },
)
_OptionalTopBottomRankedComputationTypeDef = TypedDict(
    "_OptionalTopBottomRankedComputationTypeDef",
    {
        "Name": str,
        "Value": MeasureFieldTypeDef,
        "ResultSize": int,
    },
    total=False,
)


class TopBottomRankedComputationTypeDef(
    _RequiredTopBottomRankedComputationTypeDef, _OptionalTopBottomRankedComputationTypeDef
):
    pass


_RequiredTotalAggregationComputationTypeDef = TypedDict(
    "_RequiredTotalAggregationComputationTypeDef",
    {
        "ComputationId": str,
        "Value": MeasureFieldTypeDef,
    },
)
_OptionalTotalAggregationComputationTypeDef = TypedDict(
    "_OptionalTotalAggregationComputationTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class TotalAggregationComputationTypeDef(
    _RequiredTotalAggregationComputationTypeDef, _OptionalTotalAggregationComputationTypeDef
):
    pass


TreeMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "TreeMapAggregatedFieldWellsOutputTypeDef",
    {
        "Groups": List[DimensionFieldTypeDef],
        "Sizes": List[MeasureFieldTypeDef],
        "Colors": List[MeasureFieldTypeDef],
    },
    total=False,
)

TreeMapAggregatedFieldWellsTypeDef = TypedDict(
    "TreeMapAggregatedFieldWellsTypeDef",
    {
        "Groups": Sequence[DimensionFieldTypeDef],
        "Sizes": Sequence[MeasureFieldTypeDef],
        "Colors": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

WaterfallChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "WaterfallChartAggregatedFieldWellsOutputTypeDef",
    {
        "Categories": List[DimensionFieldTypeDef],
        "Values": List[MeasureFieldTypeDef],
        "Breakdowns": List[DimensionFieldTypeDef],
    },
    total=False,
)

WaterfallChartAggregatedFieldWellsTypeDef = TypedDict(
    "WaterfallChartAggregatedFieldWellsTypeDef",
    {
        "Categories": Sequence[DimensionFieldTypeDef],
        "Values": Sequence[MeasureFieldTypeDef],
        "Breakdowns": Sequence[DimensionFieldTypeDef],
    },
    total=False,
)

WordCloudAggregatedFieldWellsOutputTypeDef = TypedDict(
    "WordCloudAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": List[DimensionFieldTypeDef],
        "Size": List[MeasureFieldTypeDef],
    },
    total=False,
)

WordCloudAggregatedFieldWellsTypeDef = TypedDict(
    "WordCloudAggregatedFieldWellsTypeDef",
    {
        "GroupBy": Sequence[DimensionFieldTypeDef],
        "Size": Sequence[MeasureFieldTypeDef],
    },
    total=False,
)

TableUnaggregatedFieldWellsOutputTypeDef = TypedDict(
    "TableUnaggregatedFieldWellsOutputTypeDef",
    {
        "Values": List[UnaggregatedFieldTypeDef],
    },
    total=False,
)

TableUnaggregatedFieldWellsTypeDef = TypedDict(
    "TableUnaggregatedFieldWellsTypeDef",
    {
        "Values": Sequence[UnaggregatedFieldTypeDef],
    },
    total=False,
)

SectionBasedLayoutConfigurationOutputTypeDef = TypedDict(
    "SectionBasedLayoutConfigurationOutputTypeDef",
    {
        "HeaderSections": List[HeaderFooterSectionConfigurationOutputTypeDef],
        "BodySections": List[BodySectionConfigurationOutputTypeDef],
        "FooterSections": List[HeaderFooterSectionConfigurationOutputTypeDef],
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)

SectionBasedLayoutConfigurationTypeDef = TypedDict(
    "SectionBasedLayoutConfigurationTypeDef",
    {
        "HeaderSections": Sequence[HeaderFooterSectionConfigurationTypeDef],
        "BodySections": Sequence[BodySectionConfigurationTypeDef],
        "FooterSections": Sequence[HeaderFooterSectionConfigurationTypeDef],
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)

BarChartFieldWellsOutputTypeDef = TypedDict(
    "BarChartFieldWellsOutputTypeDef",
    {
        "BarChartAggregatedFieldWells": BarChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

BarChartFieldWellsTypeDef = TypedDict(
    "BarChartFieldWellsTypeDef",
    {
        "BarChartAggregatedFieldWells": BarChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

BoxPlotFieldWellsOutputTypeDef = TypedDict(
    "BoxPlotFieldWellsOutputTypeDef",
    {
        "BoxPlotAggregatedFieldWells": BoxPlotAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

BoxPlotFieldWellsTypeDef = TypedDict(
    "BoxPlotFieldWellsTypeDef",
    {
        "BoxPlotAggregatedFieldWells": BoxPlotAggregatedFieldWellsTypeDef,
    },
    total=False,
)

ComboChartFieldWellsOutputTypeDef = TypedDict(
    "ComboChartFieldWellsOutputTypeDef",
    {
        "ComboChartAggregatedFieldWells": ComboChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

ComboChartFieldWellsTypeDef = TypedDict(
    "ComboChartFieldWellsTypeDef",
    {
        "ComboChartAggregatedFieldWells": ComboChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

FilledMapFieldWellsOutputTypeDef = TypedDict(
    "FilledMapFieldWellsOutputTypeDef",
    {
        "FilledMapAggregatedFieldWells": FilledMapAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

FilledMapFieldWellsTypeDef = TypedDict(
    "FilledMapFieldWellsTypeDef",
    {
        "FilledMapAggregatedFieldWells": FilledMapAggregatedFieldWellsTypeDef,
    },
    total=False,
)

FunnelChartFieldWellsOutputTypeDef = TypedDict(
    "FunnelChartFieldWellsOutputTypeDef",
    {
        "FunnelChartAggregatedFieldWells": FunnelChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

FunnelChartFieldWellsTypeDef = TypedDict(
    "FunnelChartFieldWellsTypeDef",
    {
        "FunnelChartAggregatedFieldWells": FunnelChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

GaugeChartConfigurationOutputTypeDef = TypedDict(
    "GaugeChartConfigurationOutputTypeDef",
    {
        "FieldWells": GaugeChartFieldWellsOutputTypeDef,
        "GaugeChartOptions": GaugeChartOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "TooltipOptions": TooltipOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

GaugeChartConfigurationTypeDef = TypedDict(
    "GaugeChartConfigurationTypeDef",
    {
        "FieldWells": GaugeChartFieldWellsTypeDef,
        "GaugeChartOptions": GaugeChartOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "TooltipOptions": TooltipOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

GeospatialMapFieldWellsOutputTypeDef = TypedDict(
    "GeospatialMapFieldWellsOutputTypeDef",
    {
        "GeospatialMapAggregatedFieldWells": GeospatialMapAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

GeospatialMapFieldWellsTypeDef = TypedDict(
    "GeospatialMapFieldWellsTypeDef",
    {
        "GeospatialMapAggregatedFieldWells": GeospatialMapAggregatedFieldWellsTypeDef,
    },
    total=False,
)

HeatMapFieldWellsOutputTypeDef = TypedDict(
    "HeatMapFieldWellsOutputTypeDef",
    {
        "HeatMapAggregatedFieldWells": HeatMapAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

HeatMapFieldWellsTypeDef = TypedDict(
    "HeatMapFieldWellsTypeDef",
    {
        "HeatMapAggregatedFieldWells": HeatMapAggregatedFieldWellsTypeDef,
    },
    total=False,
)

HistogramFieldWellsOutputTypeDef = TypedDict(
    "HistogramFieldWellsOutputTypeDef",
    {
        "HistogramAggregatedFieldWells": HistogramAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

HistogramFieldWellsTypeDef = TypedDict(
    "HistogramFieldWellsTypeDef",
    {
        "HistogramAggregatedFieldWells": HistogramAggregatedFieldWellsTypeDef,
    },
    total=False,
)

KPIConfigurationOutputTypeDef = TypedDict(
    "KPIConfigurationOutputTypeDef",
    {
        "FieldWells": KPIFieldWellsOutputTypeDef,
        "SortConfiguration": KPISortConfigurationOutputTypeDef,
        "KPIOptions": KPIOptionsTypeDef,
    },
    total=False,
)

KPIConfigurationTypeDef = TypedDict(
    "KPIConfigurationTypeDef",
    {
        "FieldWells": KPIFieldWellsTypeDef,
        "SortConfiguration": KPISortConfigurationTypeDef,
        "KPIOptions": KPIOptionsTypeDef,
    },
    total=False,
)

LineChartFieldWellsOutputTypeDef = TypedDict(
    "LineChartFieldWellsOutputTypeDef",
    {
        "LineChartAggregatedFieldWells": LineChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

LineChartFieldWellsTypeDef = TypedDict(
    "LineChartFieldWellsTypeDef",
    {
        "LineChartAggregatedFieldWells": LineChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

PieChartFieldWellsOutputTypeDef = TypedDict(
    "PieChartFieldWellsOutputTypeDef",
    {
        "PieChartAggregatedFieldWells": PieChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

PieChartFieldWellsTypeDef = TypedDict(
    "PieChartFieldWellsTypeDef",
    {
        "PieChartAggregatedFieldWells": PieChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

PivotTableFieldWellsOutputTypeDef = TypedDict(
    "PivotTableFieldWellsOutputTypeDef",
    {
        "PivotTableAggregatedFieldWells": PivotTableAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

PivotTableFieldWellsTypeDef = TypedDict(
    "PivotTableFieldWellsTypeDef",
    {
        "PivotTableAggregatedFieldWells": PivotTableAggregatedFieldWellsTypeDef,
    },
    total=False,
)

RadarChartFieldWellsOutputTypeDef = TypedDict(
    "RadarChartFieldWellsOutputTypeDef",
    {
        "RadarChartAggregatedFieldWells": RadarChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

RadarChartFieldWellsTypeDef = TypedDict(
    "RadarChartFieldWellsTypeDef",
    {
        "RadarChartAggregatedFieldWells": RadarChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

SankeyDiagramFieldWellsOutputTypeDef = TypedDict(
    "SankeyDiagramFieldWellsOutputTypeDef",
    {
        "SankeyDiagramAggregatedFieldWells": SankeyDiagramAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

SankeyDiagramFieldWellsTypeDef = TypedDict(
    "SankeyDiagramFieldWellsTypeDef",
    {
        "SankeyDiagramAggregatedFieldWells": SankeyDiagramAggregatedFieldWellsTypeDef,
    },
    total=False,
)

ScatterPlotFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotFieldWellsOutputTypeDef",
    {
        "ScatterPlotCategoricallyAggregatedFieldWells": (
            ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef
        ),
        "ScatterPlotUnaggregatedFieldWells": ScatterPlotUnaggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

ScatterPlotFieldWellsTypeDef = TypedDict(
    "ScatterPlotFieldWellsTypeDef",
    {
        "ScatterPlotCategoricallyAggregatedFieldWells": (
            ScatterPlotCategoricallyAggregatedFieldWellsTypeDef
        ),
        "ScatterPlotUnaggregatedFieldWells": ScatterPlotUnaggregatedFieldWellsTypeDef,
    },
    total=False,
)

ComputationTypeDef = TypedDict(
    "ComputationTypeDef",
    {
        "TopBottomRanked": TopBottomRankedComputationTypeDef,
        "TopBottomMovers": TopBottomMoversComputationTypeDef,
        "TotalAggregation": TotalAggregationComputationTypeDef,
        "MaximumMinimum": MaximumMinimumComputationTypeDef,
        "MetricComparison": MetricComparisonComputationTypeDef,
        "PeriodOverPeriod": PeriodOverPeriodComputationTypeDef,
        "PeriodToDate": PeriodToDateComputationTypeDef,
        "GrowthRate": GrowthRateComputationTypeDef,
        "UniqueValues": UniqueValuesComputationTypeDef,
        "Forecast": ForecastComputationTypeDef,
    },
    total=False,
)

TreeMapFieldWellsOutputTypeDef = TypedDict(
    "TreeMapFieldWellsOutputTypeDef",
    {
        "TreeMapAggregatedFieldWells": TreeMapAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

TreeMapFieldWellsTypeDef = TypedDict(
    "TreeMapFieldWellsTypeDef",
    {
        "TreeMapAggregatedFieldWells": TreeMapAggregatedFieldWellsTypeDef,
    },
    total=False,
)

WaterfallChartFieldWellsOutputTypeDef = TypedDict(
    "WaterfallChartFieldWellsOutputTypeDef",
    {
        "WaterfallChartAggregatedFieldWells": WaterfallChartAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

WaterfallChartFieldWellsTypeDef = TypedDict(
    "WaterfallChartFieldWellsTypeDef",
    {
        "WaterfallChartAggregatedFieldWells": WaterfallChartAggregatedFieldWellsTypeDef,
    },
    total=False,
)

WordCloudFieldWellsOutputTypeDef = TypedDict(
    "WordCloudFieldWellsOutputTypeDef",
    {
        "WordCloudAggregatedFieldWells": WordCloudAggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

WordCloudFieldWellsTypeDef = TypedDict(
    "WordCloudFieldWellsTypeDef",
    {
        "WordCloudAggregatedFieldWells": WordCloudAggregatedFieldWellsTypeDef,
    },
    total=False,
)

TableFieldWellsOutputTypeDef = TypedDict(
    "TableFieldWellsOutputTypeDef",
    {
        "TableAggregatedFieldWells": TableAggregatedFieldWellsOutputTypeDef,
        "TableUnaggregatedFieldWells": TableUnaggregatedFieldWellsOutputTypeDef,
    },
    total=False,
)

TableFieldWellsTypeDef = TypedDict(
    "TableFieldWellsTypeDef",
    {
        "TableAggregatedFieldWells": TableAggregatedFieldWellsTypeDef,
        "TableUnaggregatedFieldWells": TableUnaggregatedFieldWellsTypeDef,
    },
    total=False,
)

LayoutConfigurationOutputTypeDef = TypedDict(
    "LayoutConfigurationOutputTypeDef",
    {
        "GridLayout": GridLayoutConfigurationOutputTypeDef,
        "FreeFormLayout": FreeFormLayoutConfigurationOutputTypeDef,
        "SectionBasedLayout": SectionBasedLayoutConfigurationOutputTypeDef,
    },
    total=False,
)

LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "GridLayout": GridLayoutConfigurationTypeDef,
        "FreeFormLayout": FreeFormLayoutConfigurationTypeDef,
        "SectionBasedLayout": SectionBasedLayoutConfigurationTypeDef,
    },
    total=False,
)

BarChartConfigurationOutputTypeDef = TypedDict(
    "BarChartConfigurationOutputTypeDef",
    {
        "FieldWells": BarChartFieldWellsOutputTypeDef,
        "SortConfiguration": BarChartSortConfigurationOutputTypeDef,
        "Orientation": BarChartOrientationType,
        "BarsArrangement": BarsArrangementType,
        "VisualPalette": VisualPaletteOutputTypeDef,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "CategoryAxis": AxisDisplayOptionsOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ValueAxis": AxisDisplayOptionsOutputTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "ReferenceLines": List[ReferenceLineTypeDef],
        "ContributionAnalysisDefaults": List[ContributionAnalysisDefaultOutputTypeDef],
    },
    total=False,
)

BarChartConfigurationTypeDef = TypedDict(
    "BarChartConfigurationTypeDef",
    {
        "FieldWells": BarChartFieldWellsTypeDef,
        "SortConfiguration": BarChartSortConfigurationTypeDef,
        "Orientation": BarChartOrientationType,
        "BarsArrangement": BarsArrangementType,
        "VisualPalette": VisualPaletteTypeDef,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "CategoryAxis": AxisDisplayOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ValueAxis": AxisDisplayOptionsTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "ReferenceLines": Sequence[ReferenceLineTypeDef],
        "ContributionAnalysisDefaults": Sequence[ContributionAnalysisDefaultTypeDef],
    },
    total=False,
)

BoxPlotChartConfigurationOutputTypeDef = TypedDict(
    "BoxPlotChartConfigurationOutputTypeDef",
    {
        "FieldWells": BoxPlotFieldWellsOutputTypeDef,
        "SortConfiguration": BoxPlotSortConfigurationOutputTypeDef,
        "BoxPlotOptions": BoxPlotOptionsTypeDef,
        "CategoryAxis": AxisDisplayOptionsOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "ReferenceLines": List[ReferenceLineTypeDef],
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

BoxPlotChartConfigurationTypeDef = TypedDict(
    "BoxPlotChartConfigurationTypeDef",
    {
        "FieldWells": BoxPlotFieldWellsTypeDef,
        "SortConfiguration": BoxPlotSortConfigurationTypeDef,
        "BoxPlotOptions": BoxPlotOptionsTypeDef,
        "CategoryAxis": AxisDisplayOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "ReferenceLines": Sequence[ReferenceLineTypeDef],
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

ComboChartConfigurationOutputTypeDef = TypedDict(
    "ComboChartConfigurationOutputTypeDef",
    {
        "FieldWells": ComboChartFieldWellsOutputTypeDef,
        "SortConfiguration": ComboChartSortConfigurationOutputTypeDef,
        "BarsArrangement": BarsArrangementType,
        "CategoryAxis": AxisDisplayOptionsOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "SecondaryYAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "SecondaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "BarDataLabels": DataLabelOptionsOutputTypeDef,
        "LineDataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "ReferenceLines": List[ReferenceLineTypeDef],
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

ComboChartConfigurationTypeDef = TypedDict(
    "ComboChartConfigurationTypeDef",
    {
        "FieldWells": ComboChartFieldWellsTypeDef,
        "SortConfiguration": ComboChartSortConfigurationTypeDef,
        "BarsArrangement": BarsArrangementType,
        "CategoryAxis": AxisDisplayOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "SecondaryYAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "SecondaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "BarDataLabels": DataLabelOptionsTypeDef,
        "LineDataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "ReferenceLines": Sequence[ReferenceLineTypeDef],
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

FilledMapConfigurationOutputTypeDef = TypedDict(
    "FilledMapConfigurationOutputTypeDef",
    {
        "FieldWells": FilledMapFieldWellsOutputTypeDef,
        "SortConfiguration": FilledMapSortConfigurationOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "WindowOptions": GeospatialWindowOptionsTypeDef,
        "MapStyleOptions": GeospatialMapStyleOptionsTypeDef,
    },
    total=False,
)

FilledMapConfigurationTypeDef = TypedDict(
    "FilledMapConfigurationTypeDef",
    {
        "FieldWells": FilledMapFieldWellsTypeDef,
        "SortConfiguration": FilledMapSortConfigurationTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "WindowOptions": GeospatialWindowOptionsTypeDef,
        "MapStyleOptions": GeospatialMapStyleOptionsTypeDef,
    },
    total=False,
)

FunnelChartConfigurationOutputTypeDef = TypedDict(
    "FunnelChartConfigurationOutputTypeDef",
    {
        "FieldWells": FunnelChartFieldWellsOutputTypeDef,
        "SortConfiguration": FunnelChartSortConfigurationOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "DataLabelOptions": FunnelChartDataLabelOptionsTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

FunnelChartConfigurationTypeDef = TypedDict(
    "FunnelChartConfigurationTypeDef",
    {
        "FieldWells": FunnelChartFieldWellsTypeDef,
        "SortConfiguration": FunnelChartSortConfigurationTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "DataLabelOptions": FunnelChartDataLabelOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

_RequiredGaugeChartVisualOutputTypeDef = TypedDict(
    "_RequiredGaugeChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGaugeChartVisualOutputTypeDef = TypedDict(
    "_OptionalGaugeChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": GaugeChartConfigurationOutputTypeDef,
        "ConditionalFormatting": GaugeChartConditionalFormattingOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class GaugeChartVisualOutputTypeDef(
    _RequiredGaugeChartVisualOutputTypeDef, _OptionalGaugeChartVisualOutputTypeDef
):
    pass


_RequiredGaugeChartVisualTypeDef = TypedDict(
    "_RequiredGaugeChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGaugeChartVisualTypeDef = TypedDict(
    "_OptionalGaugeChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": GaugeChartConfigurationTypeDef,
        "ConditionalFormatting": GaugeChartConditionalFormattingTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class GaugeChartVisualTypeDef(_RequiredGaugeChartVisualTypeDef, _OptionalGaugeChartVisualTypeDef):
    pass


GeospatialMapConfigurationOutputTypeDef = TypedDict(
    "GeospatialMapConfigurationOutputTypeDef",
    {
        "FieldWells": GeospatialMapFieldWellsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "WindowOptions": GeospatialWindowOptionsTypeDef,
        "MapStyleOptions": GeospatialMapStyleOptionsTypeDef,
        "PointStyleOptions": GeospatialPointStyleOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

GeospatialMapConfigurationTypeDef = TypedDict(
    "GeospatialMapConfigurationTypeDef",
    {
        "FieldWells": GeospatialMapFieldWellsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "WindowOptions": GeospatialWindowOptionsTypeDef,
        "MapStyleOptions": GeospatialMapStyleOptionsTypeDef,
        "PointStyleOptions": GeospatialPointStyleOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

HeatMapConfigurationOutputTypeDef = TypedDict(
    "HeatMapConfigurationOutputTypeDef",
    {
        "FieldWells": HeatMapFieldWellsOutputTypeDef,
        "SortConfiguration": HeatMapSortConfigurationOutputTypeDef,
        "RowLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColumnLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorScale": ColorScaleOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
    },
    total=False,
)

HeatMapConfigurationTypeDef = TypedDict(
    "HeatMapConfigurationTypeDef",
    {
        "FieldWells": HeatMapFieldWellsTypeDef,
        "SortConfiguration": HeatMapSortConfigurationTypeDef,
        "RowLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColumnLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorScale": ColorScaleTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
    },
    total=False,
)

HistogramConfigurationOutputTypeDef = TypedDict(
    "HistogramConfigurationOutputTypeDef",
    {
        "FieldWells": HistogramFieldWellsOutputTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "YAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "BinOptions": HistogramBinOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

HistogramConfigurationTypeDef = TypedDict(
    "HistogramConfigurationTypeDef",
    {
        "FieldWells": HistogramFieldWellsTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "YAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "BinOptions": HistogramBinOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

_RequiredKPIVisualOutputTypeDef = TypedDict(
    "_RequiredKPIVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalKPIVisualOutputTypeDef = TypedDict(
    "_OptionalKPIVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": KPIConfigurationOutputTypeDef,
        "ConditionalFormatting": KPIConditionalFormattingOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class KPIVisualOutputTypeDef(_RequiredKPIVisualOutputTypeDef, _OptionalKPIVisualOutputTypeDef):
    pass


_RequiredKPIVisualTypeDef = TypedDict(
    "_RequiredKPIVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalKPIVisualTypeDef = TypedDict(
    "_OptionalKPIVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": KPIConfigurationTypeDef,
        "ConditionalFormatting": KPIConditionalFormattingTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class KPIVisualTypeDef(_RequiredKPIVisualTypeDef, _OptionalKPIVisualTypeDef):
    pass


LineChartConfigurationOutputTypeDef = TypedDict(
    "LineChartConfigurationOutputTypeDef",
    {
        "FieldWells": LineChartFieldWellsOutputTypeDef,
        "SortConfiguration": LineChartSortConfigurationOutputTypeDef,
        "ForecastConfigurations": List[ForecastConfigurationOutputTypeDef],
        "Type": LineChartTypeType,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "PrimaryYAxisDisplayOptions": LineSeriesAxisDisplayOptionsOutputTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "SecondaryYAxisDisplayOptions": LineSeriesAxisDisplayOptionsOutputTypeDef,
        "SecondaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "DefaultSeriesSettings": LineChartDefaultSeriesSettingsTypeDef,
        "Series": List[SeriesItemTypeDef],
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "ReferenceLines": List[ReferenceLineTypeDef],
        "Tooltip": TooltipOptionsOutputTypeDef,
        "ContributionAnalysisDefaults": List[ContributionAnalysisDefaultOutputTypeDef],
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

LineChartConfigurationTypeDef = TypedDict(
    "LineChartConfigurationTypeDef",
    {
        "FieldWells": LineChartFieldWellsTypeDef,
        "SortConfiguration": LineChartSortConfigurationTypeDef,
        "ForecastConfigurations": Sequence[ForecastConfigurationTypeDef],
        "Type": LineChartTypeType,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "PrimaryYAxisDisplayOptions": LineSeriesAxisDisplayOptionsTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "SecondaryYAxisDisplayOptions": LineSeriesAxisDisplayOptionsTypeDef,
        "SecondaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "DefaultSeriesSettings": LineChartDefaultSeriesSettingsTypeDef,
        "Series": Sequence[SeriesItemTypeDef],
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "ReferenceLines": Sequence[ReferenceLineTypeDef],
        "Tooltip": TooltipOptionsTypeDef,
        "ContributionAnalysisDefaults": Sequence[ContributionAnalysisDefaultTypeDef],
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

PieChartConfigurationOutputTypeDef = TypedDict(
    "PieChartConfigurationOutputTypeDef",
    {
        "FieldWells": PieChartFieldWellsOutputTypeDef,
        "SortConfiguration": PieChartSortConfigurationOutputTypeDef,
        "DonutOptions": DonutOptionsTypeDef,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
        "ContributionAnalysisDefaults": List[ContributionAnalysisDefaultOutputTypeDef],
    },
    total=False,
)

PieChartConfigurationTypeDef = TypedDict(
    "PieChartConfigurationTypeDef",
    {
        "FieldWells": PieChartFieldWellsTypeDef,
        "SortConfiguration": PieChartSortConfigurationTypeDef,
        "DonutOptions": DonutOptionsTypeDef,
        "SmallMultiplesOptions": SmallMultiplesOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ValueLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
        "ContributionAnalysisDefaults": Sequence[ContributionAnalysisDefaultTypeDef],
    },
    total=False,
)

PivotTableConfigurationOutputTypeDef = TypedDict(
    "PivotTableConfigurationOutputTypeDef",
    {
        "FieldWells": PivotTableFieldWellsOutputTypeDef,
        "SortConfiguration": PivotTableSortConfigurationOutputTypeDef,
        "TableOptions": PivotTableOptionsOutputTypeDef,
        "TotalOptions": PivotTableTotalOptionsOutputTypeDef,
        "FieldOptions": PivotTableFieldOptionsOutputTypeDef,
        "PaginatedReportOptions": PivotTablePaginatedReportOptionsTypeDef,
    },
    total=False,
)

PivotTableConfigurationTypeDef = TypedDict(
    "PivotTableConfigurationTypeDef",
    {
        "FieldWells": PivotTableFieldWellsTypeDef,
        "SortConfiguration": PivotTableSortConfigurationTypeDef,
        "TableOptions": PivotTableOptionsTypeDef,
        "TotalOptions": PivotTableTotalOptionsTypeDef,
        "FieldOptions": PivotTableFieldOptionsTypeDef,
        "PaginatedReportOptions": PivotTablePaginatedReportOptionsTypeDef,
    },
    total=False,
)

RadarChartConfigurationOutputTypeDef = TypedDict(
    "RadarChartConfigurationOutputTypeDef",
    {
        "FieldWells": RadarChartFieldWellsOutputTypeDef,
        "SortConfiguration": RadarChartSortConfigurationOutputTypeDef,
        "Shape": RadarChartShapeType,
        "BaseSeriesSettings": RadarChartSeriesSettingsTypeDef,
        "StartAngle": float,
        "VisualPalette": VisualPaletteOutputTypeDef,
        "AlternateBandColorsVisibility": VisibilityType,
        "AlternateBandEvenColor": str,
        "AlternateBandOddColor": str,
        "CategoryAxis": AxisDisplayOptionsOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorAxis": AxisDisplayOptionsOutputTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "AxesRangeScale": RadarChartAxesRangeScaleType,
    },
    total=False,
)

RadarChartConfigurationTypeDef = TypedDict(
    "RadarChartConfigurationTypeDef",
    {
        "FieldWells": RadarChartFieldWellsTypeDef,
        "SortConfiguration": RadarChartSortConfigurationTypeDef,
        "Shape": RadarChartShapeType,
        "BaseSeriesSettings": RadarChartSeriesSettingsTypeDef,
        "StartAngle": float,
        "VisualPalette": VisualPaletteTypeDef,
        "AlternateBandColorsVisibility": VisibilityType,
        "AlternateBandEvenColor": str,
        "AlternateBandOddColor": str,
        "CategoryAxis": AxisDisplayOptionsTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorAxis": AxisDisplayOptionsTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "AxesRangeScale": RadarChartAxesRangeScaleType,
    },
    total=False,
)

SankeyDiagramChartConfigurationOutputTypeDef = TypedDict(
    "SankeyDiagramChartConfigurationOutputTypeDef",
    {
        "FieldWells": SankeyDiagramFieldWellsOutputTypeDef,
        "SortConfiguration": SankeyDiagramSortConfigurationOutputTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
    },
    total=False,
)

SankeyDiagramChartConfigurationTypeDef = TypedDict(
    "SankeyDiagramChartConfigurationTypeDef",
    {
        "FieldWells": SankeyDiagramFieldWellsTypeDef,
        "SortConfiguration": SankeyDiagramSortConfigurationTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
    },
    total=False,
)

ScatterPlotConfigurationOutputTypeDef = TypedDict(
    "ScatterPlotConfigurationOutputTypeDef",
    {
        "FieldWells": ScatterPlotFieldWellsOutputTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "YAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "YAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

ScatterPlotConfigurationTypeDef = TypedDict(
    "ScatterPlotConfigurationTypeDef",
    {
        "FieldWells": ScatterPlotFieldWellsTypeDef,
        "XAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "XAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "YAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "YAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

InsightConfigurationOutputTypeDef = TypedDict(
    "InsightConfigurationOutputTypeDef",
    {
        "Computations": List[ComputationTypeDef],
        "CustomNarrative": CustomNarrativeOptionsTypeDef,
    },
    total=False,
)

InsightConfigurationTypeDef = TypedDict(
    "InsightConfigurationTypeDef",
    {
        "Computations": Sequence[ComputationTypeDef],
        "CustomNarrative": CustomNarrativeOptionsTypeDef,
    },
    total=False,
)

TreeMapConfigurationOutputTypeDef = TypedDict(
    "TreeMapConfigurationOutputTypeDef",
    {
        "FieldWells": TreeMapFieldWellsOutputTypeDef,
        "SortConfiguration": TreeMapSortConfigurationOutputTypeDef,
        "GroupLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "SizeLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "ColorScale": ColorScaleOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "Tooltip": TooltipOptionsOutputTypeDef,
    },
    total=False,
)

TreeMapConfigurationTypeDef = TypedDict(
    "TreeMapConfigurationTypeDef",
    {
        "FieldWells": TreeMapFieldWellsTypeDef,
        "SortConfiguration": TreeMapSortConfigurationTypeDef,
        "GroupLabelOptions": ChartAxisLabelOptionsTypeDef,
        "SizeLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorLabelOptions": ChartAxisLabelOptionsTypeDef,
        "ColorScale": ColorScaleTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "Tooltip": TooltipOptionsTypeDef,
    },
    total=False,
)

WaterfallChartConfigurationOutputTypeDef = TypedDict(
    "WaterfallChartConfigurationOutputTypeDef",
    {
        "FieldWells": WaterfallChartFieldWellsOutputTypeDef,
        "SortConfiguration": WaterfallChartSortConfigurationOutputTypeDef,
        "WaterfallChartOptions": WaterfallChartOptionsTypeDef,
        "CategoryAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "CategoryAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsOutputTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsOutputTypeDef,
        "VisualPalette": VisualPaletteOutputTypeDef,
    },
    total=False,
)

WaterfallChartConfigurationTypeDef = TypedDict(
    "WaterfallChartConfigurationTypeDef",
    {
        "FieldWells": WaterfallChartFieldWellsTypeDef,
        "SortConfiguration": WaterfallChartSortConfigurationTypeDef,
        "WaterfallChartOptions": WaterfallChartOptionsTypeDef,
        "CategoryAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "CategoryAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "PrimaryYAxisLabelOptions": ChartAxisLabelOptionsTypeDef,
        "PrimaryYAxisDisplayOptions": AxisDisplayOptionsTypeDef,
        "Legend": LegendOptionsTypeDef,
        "DataLabels": DataLabelOptionsTypeDef,
        "VisualPalette": VisualPaletteTypeDef,
    },
    total=False,
)

WordCloudChartConfigurationOutputTypeDef = TypedDict(
    "WordCloudChartConfigurationOutputTypeDef",
    {
        "FieldWells": WordCloudFieldWellsOutputTypeDef,
        "SortConfiguration": WordCloudSortConfigurationOutputTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsOutputTypeDef,
        "WordCloudOptions": WordCloudOptionsTypeDef,
    },
    total=False,
)

WordCloudChartConfigurationTypeDef = TypedDict(
    "WordCloudChartConfigurationTypeDef",
    {
        "FieldWells": WordCloudFieldWellsTypeDef,
        "SortConfiguration": WordCloudSortConfigurationTypeDef,
        "CategoryLabelOptions": ChartAxisLabelOptionsTypeDef,
        "WordCloudOptions": WordCloudOptionsTypeDef,
    },
    total=False,
)

TableConfigurationOutputTypeDef = TypedDict(
    "TableConfigurationOutputTypeDef",
    {
        "FieldWells": TableFieldWellsOutputTypeDef,
        "SortConfiguration": TableSortConfigurationOutputTypeDef,
        "TableOptions": TableOptionsOutputTypeDef,
        "TotalOptions": TotalOptionsTypeDef,
        "FieldOptions": TableFieldOptionsOutputTypeDef,
        "PaginatedReportOptions": TablePaginatedReportOptionsTypeDef,
        "TableInlineVisualizations": List[TableInlineVisualizationTypeDef],
    },
    total=False,
)

TableConfigurationTypeDef = TypedDict(
    "TableConfigurationTypeDef",
    {
        "FieldWells": TableFieldWellsTypeDef,
        "SortConfiguration": TableSortConfigurationTypeDef,
        "TableOptions": TableOptionsTypeDef,
        "TotalOptions": TotalOptionsTypeDef,
        "FieldOptions": TableFieldOptionsTypeDef,
        "PaginatedReportOptions": TablePaginatedReportOptionsTypeDef,
        "TableInlineVisualizations": Sequence[TableInlineVisualizationTypeDef],
    },
    total=False,
)

LayoutOutputTypeDef = TypedDict(
    "LayoutOutputTypeDef",
    {
        "Configuration": LayoutConfigurationOutputTypeDef,
    },
)

LayoutTypeDef = TypedDict(
    "LayoutTypeDef",
    {
        "Configuration": LayoutConfigurationTypeDef,
    },
)

_RequiredBarChartVisualOutputTypeDef = TypedDict(
    "_RequiredBarChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBarChartVisualOutputTypeDef = TypedDict(
    "_OptionalBarChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": BarChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class BarChartVisualOutputTypeDef(
    _RequiredBarChartVisualOutputTypeDef, _OptionalBarChartVisualOutputTypeDef
):
    pass


_RequiredBarChartVisualTypeDef = TypedDict(
    "_RequiredBarChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBarChartVisualTypeDef = TypedDict(
    "_OptionalBarChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": BarChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class BarChartVisualTypeDef(_RequiredBarChartVisualTypeDef, _OptionalBarChartVisualTypeDef):
    pass


_RequiredBoxPlotVisualOutputTypeDef = TypedDict(
    "_RequiredBoxPlotVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBoxPlotVisualOutputTypeDef = TypedDict(
    "_OptionalBoxPlotVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": BoxPlotChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class BoxPlotVisualOutputTypeDef(
    _RequiredBoxPlotVisualOutputTypeDef, _OptionalBoxPlotVisualOutputTypeDef
):
    pass


_RequiredBoxPlotVisualTypeDef = TypedDict(
    "_RequiredBoxPlotVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalBoxPlotVisualTypeDef = TypedDict(
    "_OptionalBoxPlotVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": BoxPlotChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class BoxPlotVisualTypeDef(_RequiredBoxPlotVisualTypeDef, _OptionalBoxPlotVisualTypeDef):
    pass


_RequiredComboChartVisualOutputTypeDef = TypedDict(
    "_RequiredComboChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalComboChartVisualOutputTypeDef = TypedDict(
    "_OptionalComboChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": ComboChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class ComboChartVisualOutputTypeDef(
    _RequiredComboChartVisualOutputTypeDef, _OptionalComboChartVisualOutputTypeDef
):
    pass


_RequiredComboChartVisualTypeDef = TypedDict(
    "_RequiredComboChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalComboChartVisualTypeDef = TypedDict(
    "_OptionalComboChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": ComboChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class ComboChartVisualTypeDef(_RequiredComboChartVisualTypeDef, _OptionalComboChartVisualTypeDef):
    pass


_RequiredFilledMapVisualOutputTypeDef = TypedDict(
    "_RequiredFilledMapVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFilledMapVisualOutputTypeDef = TypedDict(
    "_OptionalFilledMapVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": FilledMapConfigurationOutputTypeDef,
        "ConditionalFormatting": FilledMapConditionalFormattingOutputTypeDef,
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class FilledMapVisualOutputTypeDef(
    _RequiredFilledMapVisualOutputTypeDef, _OptionalFilledMapVisualOutputTypeDef
):
    pass


_RequiredFilledMapVisualTypeDef = TypedDict(
    "_RequiredFilledMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFilledMapVisualTypeDef = TypedDict(
    "_OptionalFilledMapVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": FilledMapConfigurationTypeDef,
        "ConditionalFormatting": FilledMapConditionalFormattingTypeDef,
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class FilledMapVisualTypeDef(_RequiredFilledMapVisualTypeDef, _OptionalFilledMapVisualTypeDef):
    pass


_RequiredFunnelChartVisualOutputTypeDef = TypedDict(
    "_RequiredFunnelChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFunnelChartVisualOutputTypeDef = TypedDict(
    "_OptionalFunnelChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": FunnelChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class FunnelChartVisualOutputTypeDef(
    _RequiredFunnelChartVisualOutputTypeDef, _OptionalFunnelChartVisualOutputTypeDef
):
    pass


_RequiredFunnelChartVisualTypeDef = TypedDict(
    "_RequiredFunnelChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalFunnelChartVisualTypeDef = TypedDict(
    "_OptionalFunnelChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": FunnelChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class FunnelChartVisualTypeDef(
    _RequiredFunnelChartVisualTypeDef, _OptionalFunnelChartVisualTypeDef
):
    pass


_RequiredGeospatialMapVisualOutputTypeDef = TypedDict(
    "_RequiredGeospatialMapVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGeospatialMapVisualOutputTypeDef = TypedDict(
    "_OptionalGeospatialMapVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": GeospatialMapConfigurationOutputTypeDef,
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class GeospatialMapVisualOutputTypeDef(
    _RequiredGeospatialMapVisualOutputTypeDef, _OptionalGeospatialMapVisualOutputTypeDef
):
    pass


_RequiredGeospatialMapVisualTypeDef = TypedDict(
    "_RequiredGeospatialMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalGeospatialMapVisualTypeDef = TypedDict(
    "_OptionalGeospatialMapVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": GeospatialMapConfigurationTypeDef,
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class GeospatialMapVisualTypeDef(
    _RequiredGeospatialMapVisualTypeDef, _OptionalGeospatialMapVisualTypeDef
):
    pass


_RequiredHeatMapVisualOutputTypeDef = TypedDict(
    "_RequiredHeatMapVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHeatMapVisualOutputTypeDef = TypedDict(
    "_OptionalHeatMapVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": HeatMapConfigurationOutputTypeDef,
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class HeatMapVisualOutputTypeDef(
    _RequiredHeatMapVisualOutputTypeDef, _OptionalHeatMapVisualOutputTypeDef
):
    pass


_RequiredHeatMapVisualTypeDef = TypedDict(
    "_RequiredHeatMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHeatMapVisualTypeDef = TypedDict(
    "_OptionalHeatMapVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": HeatMapConfigurationTypeDef,
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class HeatMapVisualTypeDef(_RequiredHeatMapVisualTypeDef, _OptionalHeatMapVisualTypeDef):
    pass


_RequiredHistogramVisualOutputTypeDef = TypedDict(
    "_RequiredHistogramVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHistogramVisualOutputTypeDef = TypedDict(
    "_OptionalHistogramVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": HistogramConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class HistogramVisualOutputTypeDef(
    _RequiredHistogramVisualOutputTypeDef, _OptionalHistogramVisualOutputTypeDef
):
    pass


_RequiredHistogramVisualTypeDef = TypedDict(
    "_RequiredHistogramVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalHistogramVisualTypeDef = TypedDict(
    "_OptionalHistogramVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": HistogramConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class HistogramVisualTypeDef(_RequiredHistogramVisualTypeDef, _OptionalHistogramVisualTypeDef):
    pass


_RequiredLineChartVisualOutputTypeDef = TypedDict(
    "_RequiredLineChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalLineChartVisualOutputTypeDef = TypedDict(
    "_OptionalLineChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": LineChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class LineChartVisualOutputTypeDef(
    _RequiredLineChartVisualOutputTypeDef, _OptionalLineChartVisualOutputTypeDef
):
    pass


_RequiredLineChartVisualTypeDef = TypedDict(
    "_RequiredLineChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalLineChartVisualTypeDef = TypedDict(
    "_OptionalLineChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": LineChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class LineChartVisualTypeDef(_RequiredLineChartVisualTypeDef, _OptionalLineChartVisualTypeDef):
    pass


_RequiredPieChartVisualOutputTypeDef = TypedDict(
    "_RequiredPieChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPieChartVisualOutputTypeDef = TypedDict(
    "_OptionalPieChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": PieChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class PieChartVisualOutputTypeDef(
    _RequiredPieChartVisualOutputTypeDef, _OptionalPieChartVisualOutputTypeDef
):
    pass


_RequiredPieChartVisualTypeDef = TypedDict(
    "_RequiredPieChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPieChartVisualTypeDef = TypedDict(
    "_OptionalPieChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": PieChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class PieChartVisualTypeDef(_RequiredPieChartVisualTypeDef, _OptionalPieChartVisualTypeDef):
    pass


_RequiredPivotTableVisualOutputTypeDef = TypedDict(
    "_RequiredPivotTableVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPivotTableVisualOutputTypeDef = TypedDict(
    "_OptionalPivotTableVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": PivotTableConfigurationOutputTypeDef,
        "ConditionalFormatting": PivotTableConditionalFormattingOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class PivotTableVisualOutputTypeDef(
    _RequiredPivotTableVisualOutputTypeDef, _OptionalPivotTableVisualOutputTypeDef
):
    pass


_RequiredPivotTableVisualTypeDef = TypedDict(
    "_RequiredPivotTableVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalPivotTableVisualTypeDef = TypedDict(
    "_OptionalPivotTableVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": PivotTableConfigurationTypeDef,
        "ConditionalFormatting": PivotTableConditionalFormattingTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class PivotTableVisualTypeDef(_RequiredPivotTableVisualTypeDef, _OptionalPivotTableVisualTypeDef):
    pass


_RequiredRadarChartVisualOutputTypeDef = TypedDict(
    "_RequiredRadarChartVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalRadarChartVisualOutputTypeDef = TypedDict(
    "_OptionalRadarChartVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": RadarChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class RadarChartVisualOutputTypeDef(
    _RequiredRadarChartVisualOutputTypeDef, _OptionalRadarChartVisualOutputTypeDef
):
    pass


_RequiredRadarChartVisualTypeDef = TypedDict(
    "_RequiredRadarChartVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalRadarChartVisualTypeDef = TypedDict(
    "_OptionalRadarChartVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": RadarChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class RadarChartVisualTypeDef(_RequiredRadarChartVisualTypeDef, _OptionalRadarChartVisualTypeDef):
    pass


_RequiredSankeyDiagramVisualOutputTypeDef = TypedDict(
    "_RequiredSankeyDiagramVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalSankeyDiagramVisualOutputTypeDef = TypedDict(
    "_OptionalSankeyDiagramVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": SankeyDiagramChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class SankeyDiagramVisualOutputTypeDef(
    _RequiredSankeyDiagramVisualOutputTypeDef, _OptionalSankeyDiagramVisualOutputTypeDef
):
    pass


_RequiredSankeyDiagramVisualTypeDef = TypedDict(
    "_RequiredSankeyDiagramVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalSankeyDiagramVisualTypeDef = TypedDict(
    "_OptionalSankeyDiagramVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": SankeyDiagramChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class SankeyDiagramVisualTypeDef(
    _RequiredSankeyDiagramVisualTypeDef, _OptionalSankeyDiagramVisualTypeDef
):
    pass


_RequiredScatterPlotVisualOutputTypeDef = TypedDict(
    "_RequiredScatterPlotVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalScatterPlotVisualOutputTypeDef = TypedDict(
    "_OptionalScatterPlotVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": ScatterPlotConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class ScatterPlotVisualOutputTypeDef(
    _RequiredScatterPlotVisualOutputTypeDef, _OptionalScatterPlotVisualOutputTypeDef
):
    pass


_RequiredScatterPlotVisualTypeDef = TypedDict(
    "_RequiredScatterPlotVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalScatterPlotVisualTypeDef = TypedDict(
    "_OptionalScatterPlotVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": ScatterPlotConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class ScatterPlotVisualTypeDef(
    _RequiredScatterPlotVisualTypeDef, _OptionalScatterPlotVisualTypeDef
):
    pass


_RequiredInsightVisualOutputTypeDef = TypedDict(
    "_RequiredInsightVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalInsightVisualOutputTypeDef = TypedDict(
    "_OptionalInsightVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "InsightConfiguration": InsightConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class InsightVisualOutputTypeDef(
    _RequiredInsightVisualOutputTypeDef, _OptionalInsightVisualOutputTypeDef
):
    pass


_RequiredInsightVisualTypeDef = TypedDict(
    "_RequiredInsightVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
    },
)
_OptionalInsightVisualTypeDef = TypedDict(
    "_OptionalInsightVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "InsightConfiguration": InsightConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class InsightVisualTypeDef(_RequiredInsightVisualTypeDef, _OptionalInsightVisualTypeDef):
    pass


_RequiredTreeMapVisualOutputTypeDef = TypedDict(
    "_RequiredTreeMapVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTreeMapVisualOutputTypeDef = TypedDict(
    "_OptionalTreeMapVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": TreeMapConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class TreeMapVisualOutputTypeDef(
    _RequiredTreeMapVisualOutputTypeDef, _OptionalTreeMapVisualOutputTypeDef
):
    pass


_RequiredTreeMapVisualTypeDef = TypedDict(
    "_RequiredTreeMapVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTreeMapVisualTypeDef = TypedDict(
    "_OptionalTreeMapVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": TreeMapConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class TreeMapVisualTypeDef(_RequiredTreeMapVisualTypeDef, _OptionalTreeMapVisualTypeDef):
    pass


_RequiredWaterfallVisualOutputTypeDef = TypedDict(
    "_RequiredWaterfallVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWaterfallVisualOutputTypeDef = TypedDict(
    "_OptionalWaterfallVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": WaterfallChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class WaterfallVisualOutputTypeDef(
    _RequiredWaterfallVisualOutputTypeDef, _OptionalWaterfallVisualOutputTypeDef
):
    pass


_RequiredWaterfallVisualTypeDef = TypedDict(
    "_RequiredWaterfallVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWaterfallVisualTypeDef = TypedDict(
    "_OptionalWaterfallVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": WaterfallChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class WaterfallVisualTypeDef(_RequiredWaterfallVisualTypeDef, _OptionalWaterfallVisualTypeDef):
    pass


_RequiredWordCloudVisualOutputTypeDef = TypedDict(
    "_RequiredWordCloudVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWordCloudVisualOutputTypeDef = TypedDict(
    "_OptionalWordCloudVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": WordCloudChartConfigurationOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
        "ColumnHierarchies": List[ColumnHierarchyOutputTypeDef],
    },
    total=False,
)


class WordCloudVisualOutputTypeDef(
    _RequiredWordCloudVisualOutputTypeDef, _OptionalWordCloudVisualOutputTypeDef
):
    pass


_RequiredWordCloudVisualTypeDef = TypedDict(
    "_RequiredWordCloudVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalWordCloudVisualTypeDef = TypedDict(
    "_OptionalWordCloudVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": WordCloudChartConfigurationTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
        "ColumnHierarchies": Sequence[ColumnHierarchyTypeDef],
    },
    total=False,
)


class WordCloudVisualTypeDef(_RequiredWordCloudVisualTypeDef, _OptionalWordCloudVisualTypeDef):
    pass


_RequiredTableVisualOutputTypeDef = TypedDict(
    "_RequiredTableVisualOutputTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTableVisualOutputTypeDef = TypedDict(
    "_OptionalTableVisualOutputTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": TableConfigurationOutputTypeDef,
        "ConditionalFormatting": TableConditionalFormattingOutputTypeDef,
        "Actions": List[VisualCustomActionOutputTypeDef],
    },
    total=False,
)


class TableVisualOutputTypeDef(
    _RequiredTableVisualOutputTypeDef, _OptionalTableVisualOutputTypeDef
):
    pass


_RequiredTableVisualTypeDef = TypedDict(
    "_RequiredTableVisualTypeDef",
    {
        "VisualId": str,
    },
)
_OptionalTableVisualTypeDef = TypedDict(
    "_OptionalTableVisualTypeDef",
    {
        "Title": VisualTitleLabelOptionsTypeDef,
        "Subtitle": VisualSubtitleLabelOptionsTypeDef,
        "ChartConfiguration": TableConfigurationTypeDef,
        "ConditionalFormatting": TableConditionalFormattingTypeDef,
        "Actions": Sequence[VisualCustomActionTypeDef],
    },
    total=False,
)


class TableVisualTypeDef(_RequiredTableVisualTypeDef, _OptionalTableVisualTypeDef):
    pass


VisualOutputTypeDef = TypedDict(
    "VisualOutputTypeDef",
    {
        "TableVisual": TableVisualOutputTypeDef,
        "PivotTableVisual": PivotTableVisualOutputTypeDef,
        "BarChartVisual": BarChartVisualOutputTypeDef,
        "KPIVisual": KPIVisualOutputTypeDef,
        "PieChartVisual": PieChartVisualOutputTypeDef,
        "GaugeChartVisual": GaugeChartVisualOutputTypeDef,
        "LineChartVisual": LineChartVisualOutputTypeDef,
        "HeatMapVisual": HeatMapVisualOutputTypeDef,
        "TreeMapVisual": TreeMapVisualOutputTypeDef,
        "GeospatialMapVisual": GeospatialMapVisualOutputTypeDef,
        "FilledMapVisual": FilledMapVisualOutputTypeDef,
        "FunnelChartVisual": FunnelChartVisualOutputTypeDef,
        "ScatterPlotVisual": ScatterPlotVisualOutputTypeDef,
        "ComboChartVisual": ComboChartVisualOutputTypeDef,
        "BoxPlotVisual": BoxPlotVisualOutputTypeDef,
        "WaterfallVisual": WaterfallVisualOutputTypeDef,
        "HistogramVisual": HistogramVisualOutputTypeDef,
        "WordCloudVisual": WordCloudVisualOutputTypeDef,
        "InsightVisual": InsightVisualOutputTypeDef,
        "SankeyDiagramVisual": SankeyDiagramVisualOutputTypeDef,
        "CustomContentVisual": CustomContentVisualOutputTypeDef,
        "EmptyVisual": EmptyVisualOutputTypeDef,
        "RadarChartVisual": RadarChartVisualOutputTypeDef,
    },
    total=False,
)

VisualTypeDef = TypedDict(
    "VisualTypeDef",
    {
        "TableVisual": TableVisualTypeDef,
        "PivotTableVisual": PivotTableVisualTypeDef,
        "BarChartVisual": BarChartVisualTypeDef,
        "KPIVisual": KPIVisualTypeDef,
        "PieChartVisual": PieChartVisualTypeDef,
        "GaugeChartVisual": GaugeChartVisualTypeDef,
        "LineChartVisual": LineChartVisualTypeDef,
        "HeatMapVisual": HeatMapVisualTypeDef,
        "TreeMapVisual": TreeMapVisualTypeDef,
        "GeospatialMapVisual": GeospatialMapVisualTypeDef,
        "FilledMapVisual": FilledMapVisualTypeDef,
        "FunnelChartVisual": FunnelChartVisualTypeDef,
        "ScatterPlotVisual": ScatterPlotVisualTypeDef,
        "ComboChartVisual": ComboChartVisualTypeDef,
        "BoxPlotVisual": BoxPlotVisualTypeDef,
        "WaterfallVisual": WaterfallVisualTypeDef,
        "HistogramVisual": HistogramVisualTypeDef,
        "WordCloudVisual": WordCloudVisualTypeDef,
        "InsightVisual": InsightVisualTypeDef,
        "SankeyDiagramVisual": SankeyDiagramVisualTypeDef,
        "CustomContentVisual": CustomContentVisualTypeDef,
        "EmptyVisual": EmptyVisualTypeDef,
        "RadarChartVisual": RadarChartVisualTypeDef,
    },
    total=False,
)

_RequiredSheetDefinitionOutputTypeDef = TypedDict(
    "_RequiredSheetDefinitionOutputTypeDef",
    {
        "SheetId": str,
    },
)
_OptionalSheetDefinitionOutputTypeDef = TypedDict(
    "_OptionalSheetDefinitionOutputTypeDef",
    {
        "Title": str,
        "Description": str,
        "Name": str,
        "ParameterControls": List[ParameterControlOutputTypeDef],
        "FilterControls": List[FilterControlOutputTypeDef],
        "Visuals": List[VisualOutputTypeDef],
        "TextBoxes": List[SheetTextBoxTypeDef],
        "Layouts": List[LayoutOutputTypeDef],
        "SheetControlLayouts": List[SheetControlLayoutOutputTypeDef],
        "ContentType": SheetContentTypeType,
    },
    total=False,
)


class SheetDefinitionOutputTypeDef(
    _RequiredSheetDefinitionOutputTypeDef, _OptionalSheetDefinitionOutputTypeDef
):
    pass


_RequiredSheetDefinitionTypeDef = TypedDict(
    "_RequiredSheetDefinitionTypeDef",
    {
        "SheetId": str,
    },
)
_OptionalSheetDefinitionTypeDef = TypedDict(
    "_OptionalSheetDefinitionTypeDef",
    {
        "Title": str,
        "Description": str,
        "Name": str,
        "ParameterControls": Sequence[ParameterControlTypeDef],
        "FilterControls": Sequence[FilterControlTypeDef],
        "Visuals": Sequence[VisualTypeDef],
        "TextBoxes": Sequence[SheetTextBoxTypeDef],
        "Layouts": Sequence[LayoutTypeDef],
        "SheetControlLayouts": Sequence[SheetControlLayoutTypeDef],
        "ContentType": SheetContentTypeType,
    },
    total=False,
)


class SheetDefinitionTypeDef(_RequiredSheetDefinitionTypeDef, _OptionalSheetDefinitionTypeDef):
    pass


_RequiredAnalysisDefinitionOutputTypeDef = TypedDict(
    "_RequiredAnalysisDefinitionOutputTypeDef",
    {
        "DataSetIdentifierDeclarations": List[DataSetIdentifierDeclarationTypeDef],
    },
)
_OptionalAnalysisDefinitionOutputTypeDef = TypedDict(
    "_OptionalAnalysisDefinitionOutputTypeDef",
    {
        "Sheets": List[SheetDefinitionOutputTypeDef],
        "CalculatedFields": List[CalculatedFieldTypeDef],
        "ParameterDeclarations": List[ParameterDeclarationOutputTypeDef],
        "FilterGroups": List[FilterGroupOutputTypeDef],
        "ColumnConfigurations": List[ColumnConfigurationOutputTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class AnalysisDefinitionOutputTypeDef(
    _RequiredAnalysisDefinitionOutputTypeDef, _OptionalAnalysisDefinitionOutputTypeDef
):
    pass


_RequiredDashboardVersionDefinitionOutputTypeDef = TypedDict(
    "_RequiredDashboardVersionDefinitionOutputTypeDef",
    {
        "DataSetIdentifierDeclarations": List[DataSetIdentifierDeclarationTypeDef],
    },
)
_OptionalDashboardVersionDefinitionOutputTypeDef = TypedDict(
    "_OptionalDashboardVersionDefinitionOutputTypeDef",
    {
        "Sheets": List[SheetDefinitionOutputTypeDef],
        "CalculatedFields": List[CalculatedFieldTypeDef],
        "ParameterDeclarations": List[ParameterDeclarationOutputTypeDef],
        "FilterGroups": List[FilterGroupOutputTypeDef],
        "ColumnConfigurations": List[ColumnConfigurationOutputTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class DashboardVersionDefinitionOutputTypeDef(
    _RequiredDashboardVersionDefinitionOutputTypeDef,
    _OptionalDashboardVersionDefinitionOutputTypeDef,
):
    pass


_RequiredTemplateVersionDefinitionOutputTypeDef = TypedDict(
    "_RequiredTemplateVersionDefinitionOutputTypeDef",
    {
        "DataSetConfigurations": List[DataSetConfigurationOutputTypeDef],
    },
)
_OptionalTemplateVersionDefinitionOutputTypeDef = TypedDict(
    "_OptionalTemplateVersionDefinitionOutputTypeDef",
    {
        "Sheets": List[SheetDefinitionOutputTypeDef],
        "CalculatedFields": List[CalculatedFieldTypeDef],
        "ParameterDeclarations": List[ParameterDeclarationOutputTypeDef],
        "FilterGroups": List[FilterGroupOutputTypeDef],
        "ColumnConfigurations": List[ColumnConfigurationOutputTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class TemplateVersionDefinitionOutputTypeDef(
    _RequiredTemplateVersionDefinitionOutputTypeDef, _OptionalTemplateVersionDefinitionOutputTypeDef
):
    pass


_RequiredAnalysisDefinitionTypeDef = TypedDict(
    "_RequiredAnalysisDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": Sequence[DataSetIdentifierDeclarationTypeDef],
    },
)
_OptionalAnalysisDefinitionTypeDef = TypedDict(
    "_OptionalAnalysisDefinitionTypeDef",
    {
        "Sheets": Sequence[SheetDefinitionTypeDef],
        "CalculatedFields": Sequence[CalculatedFieldTypeDef],
        "ParameterDeclarations": Sequence[ParameterDeclarationTypeDef],
        "FilterGroups": Sequence[FilterGroupTypeDef],
        "ColumnConfigurations": Sequence[ColumnConfigurationTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class AnalysisDefinitionTypeDef(
    _RequiredAnalysisDefinitionTypeDef, _OptionalAnalysisDefinitionTypeDef
):
    pass


_RequiredDashboardVersionDefinitionTypeDef = TypedDict(
    "_RequiredDashboardVersionDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": Sequence[DataSetIdentifierDeclarationTypeDef],
    },
)
_OptionalDashboardVersionDefinitionTypeDef = TypedDict(
    "_OptionalDashboardVersionDefinitionTypeDef",
    {
        "Sheets": Sequence[SheetDefinitionTypeDef],
        "CalculatedFields": Sequence[CalculatedFieldTypeDef],
        "ParameterDeclarations": Sequence[ParameterDeclarationTypeDef],
        "FilterGroups": Sequence[FilterGroupTypeDef],
        "ColumnConfigurations": Sequence[ColumnConfigurationTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class DashboardVersionDefinitionTypeDef(
    _RequiredDashboardVersionDefinitionTypeDef, _OptionalDashboardVersionDefinitionTypeDef
):
    pass


_RequiredTemplateVersionDefinitionTypeDef = TypedDict(
    "_RequiredTemplateVersionDefinitionTypeDef",
    {
        "DataSetConfigurations": Sequence[DataSetConfigurationTypeDef],
    },
)
_OptionalTemplateVersionDefinitionTypeDef = TypedDict(
    "_OptionalTemplateVersionDefinitionTypeDef",
    {
        "Sheets": Sequence[SheetDefinitionTypeDef],
        "CalculatedFields": Sequence[CalculatedFieldTypeDef],
        "ParameterDeclarations": Sequence[ParameterDeclarationTypeDef],
        "FilterGroups": Sequence[FilterGroupTypeDef],
        "ColumnConfigurations": Sequence[ColumnConfigurationTypeDef],
        "AnalysisDefaults": AnalysisDefaultsTypeDef,
    },
    total=False,
)


class TemplateVersionDefinitionTypeDef(
    _RequiredTemplateVersionDefinitionTypeDef, _OptionalTemplateVersionDefinitionTypeDef
):
    pass


DescribeAnalysisDefinitionResponseTypeDef = TypedDict(
    "DescribeAnalysisDefinitionResponseTypeDef",
    {
        "AnalysisId": str,
        "Name": str,
        "Errors": List[AnalysisErrorTypeDef],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": AnalysisDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDashboardDefinitionResponseTypeDef = TypedDict(
    "DescribeDashboardDefinitionResponseTypeDef",
    {
        "DashboardId": str,
        "Errors": List[DashboardErrorTypeDef],
        "Name": str,
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": DashboardVersionDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "DashboardPublishOptions": DashboardPublishOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeTemplateDefinitionResponseTypeDef = TypedDict(
    "DescribeTemplateDefinitionResponseTypeDef",
    {
        "Name": str,
        "TemplateId": str,
        "Errors": List[TemplateErrorTypeDef],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": TemplateVersionDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
    },
)
_OptionalCreateAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAnalysisRequestRequestTypeDef",
    {
        "Parameters": ParametersTypeDef,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "SourceEntity": AnalysisSourceEntityTypeDef,
        "ThemeArn": str,
        "Tags": Sequence[TagTypeDef],
        "Definition": AnalysisDefinitionTypeDef,
    },
    total=False,
)


class CreateAnalysisRequestRequestTypeDef(
    _RequiredCreateAnalysisRequestRequestTypeDef, _OptionalCreateAnalysisRequestRequestTypeDef
):
    pass


_RequiredUpdateAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
    },
)
_OptionalUpdateAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnalysisRequestRequestTypeDef",
    {
        "Parameters": ParametersTypeDef,
        "SourceEntity": AnalysisSourceEntityTypeDef,
        "ThemeArn": str,
        "Definition": AnalysisDefinitionTypeDef,
    },
    total=False,
)


class UpdateAnalysisRequestRequestTypeDef(
    _RequiredUpdateAnalysisRequestRequestTypeDef, _OptionalUpdateAnalysisRequestRequestTypeDef
):
    pass


_RequiredCreateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
    },
)
_OptionalCreateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDashboardRequestRequestTypeDef",
    {
        "Parameters": ParametersTypeDef,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "SourceEntity": DashboardSourceEntityTypeDef,
        "Tags": Sequence[TagTypeDef],
        "VersionDescription": str,
        "DashboardPublishOptions": DashboardPublishOptionsTypeDef,
        "ThemeArn": str,
        "Definition": DashboardVersionDefinitionTypeDef,
    },
    total=False,
)


class CreateDashboardRequestRequestTypeDef(
    _RequiredCreateDashboardRequestRequestTypeDef, _OptionalCreateDashboardRequestRequestTypeDef
):
    pass


_RequiredUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
    },
)
_OptionalUpdateDashboardRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDashboardRequestRequestTypeDef",
    {
        "SourceEntity": DashboardSourceEntityTypeDef,
        "Parameters": ParametersTypeDef,
        "VersionDescription": str,
        "DashboardPublishOptions": DashboardPublishOptionsTypeDef,
        "ThemeArn": str,
        "Definition": DashboardVersionDefinitionTypeDef,
    },
    total=False,
)


class UpdateDashboardRequestRequestTypeDef(
    _RequiredUpdateDashboardRequestRequestTypeDef, _OptionalUpdateDashboardRequestRequestTypeDef
):
    pass


_RequiredCreateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalCreateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateRequestRequestTypeDef",
    {
        "Name": str,
        "Permissions": Sequence[Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]],
        "SourceEntity": TemplateSourceEntityTypeDef,
        "Tags": Sequence[TagTypeDef],
        "VersionDescription": str,
        "Definition": TemplateVersionDefinitionTypeDef,
    },
    total=False,
)


class CreateTemplateRequestRequestTypeDef(
    _RequiredCreateTemplateRequestRequestTypeDef, _OptionalCreateTemplateRequestRequestTypeDef
):
    pass


_RequiredUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
_OptionalUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateRequestRequestTypeDef",
    {
        "SourceEntity": TemplateSourceEntityTypeDef,
        "VersionDescription": str,
        "Name": str,
        "Definition": TemplateVersionDefinitionTypeDef,
    },
    total=False,
)


class UpdateTemplateRequestRequestTypeDef(
    _RequiredUpdateTemplateRequestRequestTypeDef, _OptionalUpdateTemplateRequestRequestTypeDef
):
    pass
