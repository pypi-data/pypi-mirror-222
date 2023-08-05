# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ConsentStoreIamBindingConditionArgs',
    'ConsentStoreIamMemberConditionArgs',
    'DatasetIamBindingConditionArgs',
    'DatasetIamMemberConditionArgs',
    'DicomStoreIamBindingConditionArgs',
    'DicomStoreIamMemberConditionArgs',
    'DicomStoreNotificationConfigArgs',
    'DicomStoreStreamConfigArgs',
    'DicomStoreStreamConfigBigqueryDestinationArgs',
    'FhirStoreIamBindingConditionArgs',
    'FhirStoreIamMemberConditionArgs',
    'FhirStoreNotificationConfigArgs',
    'FhirStoreStreamConfigArgs',
    'FhirStoreStreamConfigBigqueryDestinationArgs',
    'FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs',
    'Hl7StoreIamBindingConditionArgs',
    'Hl7StoreIamMemberConditionArgs',
    'Hl7StoreNotificationConfigArgs',
    'Hl7StoreNotificationConfigsArgs',
    'Hl7StoreParserConfigArgs',
]

@pulumi.input_type
class ConsentStoreIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class ConsentStoreIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class DatasetIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class DatasetIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class DicomStoreIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class DicomStoreIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class DicomStoreNotificationConfigArgs:
    def __init__(__self__, *,
                 pubsub_topic: pulumi.Input[str]):
        """
        :param pulumi.Input[str] pubsub_topic: The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
               PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
               It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
               was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
               project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
               Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        """
        pulumi.set(__self__, "pubsub_topic", pubsub_topic)

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[str]:
        """
        The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
        PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
        It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
        was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
        project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
        Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        """
        return pulumi.get(self, "pubsub_topic")

    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "pubsub_topic", value)


@pulumi.input_type
class DicomStoreStreamConfigArgs:
    def __init__(__self__, *,
                 bigquery_destination: pulumi.Input['DicomStoreStreamConfigBigqueryDestinationArgs']):
        """
        :param pulumi.Input['DicomStoreStreamConfigBigqueryDestinationArgs'] bigquery_destination: BigQueryDestination to include a fully qualified BigQuery table URI where DICOM instance metadata will be streamed.
               Structure is documented below.
        """
        pulumi.set(__self__, "bigquery_destination", bigquery_destination)

    @property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(self) -> pulumi.Input['DicomStoreStreamConfigBigqueryDestinationArgs']:
        """
        BigQueryDestination to include a fully qualified BigQuery table URI where DICOM instance metadata will be streamed.
        Structure is documented below.
        """
        return pulumi.get(self, "bigquery_destination")

    @bigquery_destination.setter
    def bigquery_destination(self, value: pulumi.Input['DicomStoreStreamConfigBigqueryDestinationArgs']):
        pulumi.set(self, "bigquery_destination", value)


@pulumi.input_type
class DicomStoreStreamConfigBigqueryDestinationArgs:
    def __init__(__self__, *,
                 table_uri: pulumi.Input[str]):
        """
        :param pulumi.Input[str] table_uri: a fully qualified BigQuery table URI where DICOM instance metadata will be streamed.
        """
        pulumi.set(__self__, "table_uri", table_uri)

    @property
    @pulumi.getter(name="tableUri")
    def table_uri(self) -> pulumi.Input[str]:
        """
        a fully qualified BigQuery table URI where DICOM instance metadata will be streamed.
        """
        return pulumi.get(self, "table_uri")

    @table_uri.setter
    def table_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_uri", value)


@pulumi.input_type
class FhirStoreIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FhirStoreIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FhirStoreNotificationConfigArgs:
    def __init__(__self__, *,
                 pubsub_topic: pulumi.Input[str],
                 send_full_resource: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] pubsub_topic: The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
               PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
               It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
               was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
               project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
               Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        :param pulumi.Input[bool] send_full_resource: Whether to send full FHIR resource to this Pub/Sub topic for Create and Update operation.
               Note that setting this to true does not guarantee that all resources will be sent in the format of
               full FHIR resource. When a resource change is too large or during heavy traffic, only the resource name will be
               sent. Clients should always check the "payloadType" label from a Pub/Sub message to determine whether
               it needs to fetch the full resource as a separate operation.
        """
        pulumi.set(__self__, "pubsub_topic", pubsub_topic)
        if send_full_resource is not None:
            pulumi.set(__self__, "send_full_resource", send_full_resource)

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[str]:
        """
        The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
        PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
        It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
        was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
        project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
        Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        """
        return pulumi.get(self, "pubsub_topic")

    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "pubsub_topic", value)

    @property
    @pulumi.getter(name="sendFullResource")
    def send_full_resource(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to send full FHIR resource to this Pub/Sub topic for Create and Update operation.
        Note that setting this to true does not guarantee that all resources will be sent in the format of
        full FHIR resource. When a resource change is too large or during heavy traffic, only the resource name will be
        sent. Clients should always check the "payloadType" label from a Pub/Sub message to determine whether
        it needs to fetch the full resource as a separate operation.
        """
        return pulumi.get(self, "send_full_resource")

    @send_full_resource.setter
    def send_full_resource(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_full_resource", value)


@pulumi.input_type
class FhirStoreStreamConfigArgs:
    def __init__(__self__, *,
                 bigquery_destination: pulumi.Input['FhirStoreStreamConfigBigqueryDestinationArgs'],
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input['FhirStoreStreamConfigBigqueryDestinationArgs'] bigquery_destination: The destination BigQuery structure that contains both the dataset location and corresponding schema config.
               The output is organized in one table per resource type. The server reuses the existing tables (if any) that
               are named after the resource types, e.g. "Patient", "Observation". When there is no existing table for a given
               resource type, the server attempts to create one.
               See the [streaming config reference](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#streamconfig) for more details.
               Structure is documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_types: Supply a FHIR resource type (such as "Patient" or "Observation"). See
               https://www.hl7.org/fhir/valueset-resource-types.html for a list of all FHIR resource types. The server treats
               an empty list as an intent to stream all the supported resource types in this FHIR store.
        """
        pulumi.set(__self__, "bigquery_destination", bigquery_destination)
        if resource_types is not None:
            pulumi.set(__self__, "resource_types", resource_types)

    @property
    @pulumi.getter(name="bigqueryDestination")
    def bigquery_destination(self) -> pulumi.Input['FhirStoreStreamConfigBigqueryDestinationArgs']:
        """
        The destination BigQuery structure that contains both the dataset location and corresponding schema config.
        The output is organized in one table per resource type. The server reuses the existing tables (if any) that
        are named after the resource types, e.g. "Patient", "Observation". When there is no existing table for a given
        resource type, the server attempts to create one.
        See the [streaming config reference](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#streamconfig) for more details.
        Structure is documented below.
        """
        return pulumi.get(self, "bigquery_destination")

    @bigquery_destination.setter
    def bigquery_destination(self, value: pulumi.Input['FhirStoreStreamConfigBigqueryDestinationArgs']):
        pulumi.set(self, "bigquery_destination", value)

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Supply a FHIR resource type (such as "Patient" or "Observation"). See
        https://www.hl7.org/fhir/valueset-resource-types.html for a list of all FHIR resource types. The server treats
        an empty list as an intent to stream all the supported resource types in this FHIR store.
        """
        return pulumi.get(self, "resource_types")

    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_types", value)


@pulumi.input_type
class FhirStoreStreamConfigBigqueryDestinationArgs:
    def __init__(__self__, *,
                 dataset_uri: pulumi.Input[str],
                 schema_config: pulumi.Input['FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs']):
        """
        :param pulumi.Input[str] dataset_uri: BigQuery URI to a dataset, up to 2000 characters long, in the format bq://projectId.bqDatasetId
        :param pulumi.Input['FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs'] schema_config: The configuration for the exported BigQuery schema.
               Structure is documented below.
        """
        pulumi.set(__self__, "dataset_uri", dataset_uri)
        pulumi.set(__self__, "schema_config", schema_config)

    @property
    @pulumi.getter(name="datasetUri")
    def dataset_uri(self) -> pulumi.Input[str]:
        """
        BigQuery URI to a dataset, up to 2000 characters long, in the format bq://projectId.bqDatasetId
        """
        return pulumi.get(self, "dataset_uri")

    @dataset_uri.setter
    def dataset_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_uri", value)

    @property
    @pulumi.getter(name="schemaConfig")
    def schema_config(self) -> pulumi.Input['FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs']:
        """
        The configuration for the exported BigQuery schema.
        Structure is documented below.
        """
        return pulumi.get(self, "schema_config")

    @schema_config.setter
    def schema_config(self, value: pulumi.Input['FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs']):
        pulumi.set(self, "schema_config", value)


@pulumi.input_type
class FhirStoreStreamConfigBigqueryDestinationSchemaConfigArgs:
    def __init__(__self__, *,
                 recursive_structure_depth: pulumi.Input[int],
                 schema_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] recursive_structure_depth: The depth for all recursive structures in the output analytics schema. For example, concept in the CodeSystem
               resource is a recursive structure; when the depth is 2, the CodeSystem table will have a column called
               concept.concept but not concept.concept.concept. If not specified or set to 0, the server will use the default
               value 2. The maximum depth allowed is 5.
        :param pulumi.Input[str] schema_type: Specifies the output schema type.
               * ANALYTICS: Analytics schema defined by the FHIR community.
               See https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md.
               * ANALYTICS_V2: Analytics V2, similar to schema defined by the FHIR community, with added support for extensions with one or more occurrences and contained resources in stringified JSON.
               * LOSSLESS: A data-driven schema generated from the fields present in the FHIR data being exported, with no additional simplification.
               Default value is `ANALYTICS`.
               Possible values are: `ANALYTICS`, `ANALYTICS_V2`, `LOSSLESS`.
        """
        pulumi.set(__self__, "recursive_structure_depth", recursive_structure_depth)
        if schema_type is not None:
            pulumi.set(__self__, "schema_type", schema_type)

    @property
    @pulumi.getter(name="recursiveStructureDepth")
    def recursive_structure_depth(self) -> pulumi.Input[int]:
        """
        The depth for all recursive structures in the output analytics schema. For example, concept in the CodeSystem
        resource is a recursive structure; when the depth is 2, the CodeSystem table will have a column called
        concept.concept but not concept.concept.concept. If not specified or set to 0, the server will use the default
        value 2. The maximum depth allowed is 5.
        """
        return pulumi.get(self, "recursive_structure_depth")

    @recursive_structure_depth.setter
    def recursive_structure_depth(self, value: pulumi.Input[int]):
        pulumi.set(self, "recursive_structure_depth", value)

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the output schema type.
        * ANALYTICS: Analytics schema defined by the FHIR community.
        See https://github.com/FHIR/sql-on-fhir/blob/master/sql-on-fhir.md.
        * ANALYTICS_V2: Analytics V2, similar to schema defined by the FHIR community, with added support for extensions with one or more occurrences and contained resources in stringified JSON.
        * LOSSLESS: A data-driven schema generated from the fields present in the FHIR data being exported, with no additional simplification.
        Default value is `ANALYTICS`.
        Possible values are: `ANALYTICS`, `ANALYTICS_V2`, `LOSSLESS`.
        """
        return pulumi.get(self, "schema_type")

    @schema_type.setter
    def schema_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_type", value)


@pulumi.input_type
class Hl7StoreIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class Hl7StoreIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class Hl7StoreNotificationConfigArgs:
    def __init__(__self__, *,
                 pubsub_topic: pulumi.Input[str]):
        """
        :param pulumi.Input[str] pubsub_topic: The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
               PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
               It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
               was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
               project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
               Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        """
        pulumi.set(__self__, "pubsub_topic", pubsub_topic)

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[str]:
        """
        The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
        PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
        It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
        was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
        project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
        Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        """
        return pulumi.get(self, "pubsub_topic")

    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "pubsub_topic", value)


@pulumi.input_type
class Hl7StoreNotificationConfigsArgs:
    def __init__(__self__, *,
                 pubsub_topic: pulumi.Input[str],
                 filter: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] pubsub_topic: The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
               PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
               It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
               was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
               project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
               Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
               If a notification cannot be published to Cloud Pub/Sub, errors will be logged to Stackdriver
        :param pulumi.Input[str] filter: Restricts notifications sent for messages matching a filter. If this is empty, all messages
               are matched. Syntax: https://cloud.google.com/appengine/docs/standard/python/search/query_strings
               Fields/functions available for filtering are:
               * messageType, from the MSH-9.1 field. For example, NOT messageType = "ADT".
               * send_date or sendDate, the YYYY-MM-DD date the message was sent in the dataset's timeZone, from the MSH-7 segment. For example, send_date < "2017-01-02".
               * sendTime, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, sendTime < "2017-01-02T00:00:00-05:00".
               * sendFacility, the care center that the message came from, from the MSH-4 segment. For example, sendFacility = "ABC".
               * PatientId(value, type), which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, PatientId("123456", "MRN").
               * labels.x, a string value of the label with key x as set using the Message.labels map. For example, labels."priority"="high". The operator :* can be used to assert the existence of a label. For example, labels."priority":*.
        """
        pulumi.set(__self__, "pubsub_topic", pubsub_topic)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[str]:
        """
        The Cloud Pub/Sub topic that notifications of changes are published on. Supplied by the client.
        PubsubMessage.Data will contain the resource name. PubsubMessage.MessageId is the ID of this message.
        It is guaranteed to be unique within the topic. PubsubMessage.PublishTime is the time at which the message
        was published. Notifications are only sent if the topic is non-empty. Topic names must be scoped to a
        project. service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com must have publisher permissions on the given
        Cloud Pub/Sub topic. Not having adequate permissions will cause the calls that send notifications to fail.
        If a notification cannot be published to Cloud Pub/Sub, errors will be logged to Stackdriver
        """
        return pulumi.get(self, "pubsub_topic")

    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "pubsub_topic", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        Restricts notifications sent for messages matching a filter. If this is empty, all messages
        are matched. Syntax: https://cloud.google.com/appengine/docs/standard/python/search/query_strings
        Fields/functions available for filtering are:
        * messageType, from the MSH-9.1 field. For example, NOT messageType = "ADT".
        * send_date or sendDate, the YYYY-MM-DD date the message was sent in the dataset's timeZone, from the MSH-7 segment. For example, send_date < "2017-01-02".
        * sendTime, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, sendTime < "2017-01-02T00:00:00-05:00".
        * sendFacility, the care center that the message came from, from the MSH-4 segment. For example, sendFacility = "ABC".
        * PatientId(value, type), which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, PatientId("123456", "MRN").
        * labels.x, a string value of the label with key x as set using the Message.labels map. For example, labels."priority"="high". The operator :* can be used to assert the existence of a label. For example, labels."priority":*.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)


@pulumi.input_type
class Hl7StoreParserConfigArgs:
    def __init__(__self__, *,
                 allow_null_header: Optional[pulumi.Input[bool]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 segment_terminator: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] allow_null_header: Determines whether messages with no header are allowed.
        :param pulumi.Input[str] schema: JSON encoded string for schemas used to parse messages in this
               store if schematized parsing is desired.
        :param pulumi.Input[str] segment_terminator: Byte(s) to be used as the segment terminator. If this is unset, '\\r' will be used as segment terminator.
               A base64-encoded string.
        :param pulumi.Input[str] version: The version of the unschematized parser to be used when a custom `schema` is not set.
               Default value is `V1`.
               Possible values are: `V1`, `V2`, `V3`.
        """
        if allow_null_header is not None:
            pulumi.set(__self__, "allow_null_header", allow_null_header)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if segment_terminator is not None:
            pulumi.set(__self__, "segment_terminator", segment_terminator)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="allowNullHeader")
    def allow_null_header(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether messages with no header are allowed.
        """
        return pulumi.get(self, "allow_null_header")

    @allow_null_header.setter
    def allow_null_header(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_null_header", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        JSON encoded string for schemas used to parse messages in this
        store if schematized parsing is desired.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> Optional[pulumi.Input[str]]:
        """
        Byte(s) to be used as the segment terminator. If this is unset, '\\r' will be used as segment terminator.
        A base64-encoded string.
        """
        return pulumi.get(self, "segment_terminator")

    @segment_terminator.setter
    def segment_terminator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "segment_terminator", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the unschematized parser to be used when a custom `schema` is not set.
        Default value is `V1`.
        Possible values are: `V1`, `V2`, `V3`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


