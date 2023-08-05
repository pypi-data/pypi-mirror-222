# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BillingAccountSinkArgs', 'BillingAccountSink']

@pulumi.input_type
class BillingAccountSinkArgs:
    def __init__(__self__, *,
                 billing_account: pulumi.Input[str],
                 destination: pulumi.Input[str],
                 bigquery_options: Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BillingAccountSink resource.
        :param pulumi.Input[str] billing_account: The billing account exported to the sink.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:
               
               - `storage.googleapis.com/[GCS_BUCKET]`
               - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
               - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
               - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`
               
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input['BillingAccountSinkBigqueryOptionsArgs'] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] description: A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[bool] disabled: If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]] exclusions: Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] name: The name of the logging sink.
        """
        pulumi.set(__self__, "billing_account", billing_account)
        pulumi.set(__self__, "destination", destination)
        if bigquery_options is not None:
            pulumi.set(__self__, "bigquery_options", bigquery_options)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Input[str]:
        """
        The billing account exported to the sink.
        """
        return pulumi.get(self, "billing_account")

    @billing_account.setter
    def billing_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account", value)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Input[str]:
        """
        The destination of the sink (or, in other words, where logs are written to). Can be a
        Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:

        - `storage.googleapis.com/[GCS_BUCKET]`
        - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
        - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
        - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`

        The writer associated with the sink must have access to write to the above resource.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']]:
        """
        Options that affect sinks exporting data to BigQuery. Structure documented below.
        """
        return pulumi.get(self, "bigquery_options")

    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']]):
        pulumi.set(self, "bigquery_options", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of this sink. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to True, then this sink is disabled and it does not export any log entries.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]]:
        """
        Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]]):
        pulumi.set(self, "exclusions", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        The filter to apply when exporting logs. Only log entries that match the filter are exported.
        See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
        write a filter.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the logging sink.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BillingAccountSinkState:
    def __init__(__self__, *,
                 bigquery_options: Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 writer_identity: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BillingAccountSink resources.
        :param pulumi.Input['BillingAccountSinkBigqueryOptionsArgs'] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] billing_account: The billing account exported to the sink.
        :param pulumi.Input[str] description: A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:
               
               - `storage.googleapis.com/[GCS_BUCKET]`
               - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
               - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
               - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`
               
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input[bool] disabled: If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]] exclusions: Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] name: The name of the logging sink.
        :param pulumi.Input[str] writer_identity: The identity associated with this sink. This identity must be granted write access to the
               configured `destination`.
        """
        if bigquery_options is not None:
            pulumi.set(__self__, "bigquery_options", bigquery_options)
        if billing_account is not None:
            pulumi.set(__self__, "billing_account", billing_account)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if writer_identity is not None:
            pulumi.set(__self__, "writer_identity", writer_identity)

    @property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']]:
        """
        Options that affect sinks exporting data to BigQuery. Structure documented below.
        """
        return pulumi.get(self, "bigquery_options")

    @bigquery_options.setter
    def bigquery_options(self, value: Optional[pulumi.Input['BillingAccountSinkBigqueryOptionsArgs']]):
        pulumi.set(self, "bigquery_options", value)

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[str]]:
        """
        The billing account exported to the sink.
        """
        return pulumi.get(self, "billing_account")

    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_account", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of this sink. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        The destination of the sink (or, in other words, where logs are written to). Can be a
        Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:

        - `storage.googleapis.com/[GCS_BUCKET]`
        - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
        - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
        - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`

        The writer associated with the sink must have access to write to the above resource.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to True, then this sink is disabled and it does not export any log entries.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]]:
        """
        Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BillingAccountSinkExclusionArgs']]]]):
        pulumi.set(self, "exclusions", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        The filter to apply when exporting logs. Only log entries that match the filter are exported.
        See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
        write a filter.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the logging sink.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> Optional[pulumi.Input[str]]:
        """
        The identity associated with this sink. This identity must be granted write access to the
        configured `destination`.
        """
        return pulumi.get(self, "writer_identity")

    @writer_identity.setter
    def writer_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "writer_identity", value)


class BillingAccountSink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_options: Optional[pulumi.Input[pulumi.InputType['BillingAccountSinkBigqueryOptionsArgs']]] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingAccountSinkExclusionArgs']]]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.sinks)
        * How-to Guides
            * [Exporting Logs](https://cloud.google.com/logging/docs/export)

        > **Note** You must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
        [granted on the billing account](https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy) to
        the credentials used with this provider. [IAM roles granted on a billing account](https://cloud.google.com/billing/docs/how-to/billing-access) are separate from the
        typical IAM roles granted on a project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        log_bucket = gcp.storage.Bucket("log-bucket", location="US")
        my_sink = gcp.logging.BillingAccountSink("my-sink",
            description="some explanation on what this is",
            billing_account="ABCDEF-012345-GHIJKL",
            destination=log_bucket.name.apply(lambda name: f"storage.googleapis.com/{name}"))
        log_writer = gcp.projects.IAMBinding("log-writer",
            project="your-project-id",
            role="roles/storage.objectCreator",
            members=[my_sink.writer_identity])
        ```

        ## Import

        Billing account logging sinks can be imported using this format

        ```sh
         $ pulumi import gcp:logging/billingAccountSink:BillingAccountSink my_sink billingAccounts/{{billing_account_id}}/sinks/{{sink_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BillingAccountSinkBigqueryOptionsArgs']] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] billing_account: The billing account exported to the sink.
        :param pulumi.Input[str] description: A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:
               
               - `storage.googleapis.com/[GCS_BUCKET]`
               - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
               - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
               - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`
               
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input[bool] disabled: If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingAccountSinkExclusionArgs']]]] exclusions: Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] name: The name of the logging sink.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BillingAccountSinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.sinks)
        * How-to Guides
            * [Exporting Logs](https://cloud.google.com/logging/docs/export)

        > **Note** You must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
        [granted on the billing account](https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy) to
        the credentials used with this provider. [IAM roles granted on a billing account](https://cloud.google.com/billing/docs/how-to/billing-access) are separate from the
        typical IAM roles granted on a project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        log_bucket = gcp.storage.Bucket("log-bucket", location="US")
        my_sink = gcp.logging.BillingAccountSink("my-sink",
            description="some explanation on what this is",
            billing_account="ABCDEF-012345-GHIJKL",
            destination=log_bucket.name.apply(lambda name: f"storage.googleapis.com/{name}"))
        log_writer = gcp.projects.IAMBinding("log-writer",
            project="your-project-id",
            role="roles/storage.objectCreator",
            members=[my_sink.writer_identity])
        ```

        ## Import

        Billing account logging sinks can be imported using this format

        ```sh
         $ pulumi import gcp:logging/billingAccountSink:BillingAccountSink my_sink billingAccounts/{{billing_account_id}}/sinks/{{sink_id}}
        ```

        :param str resource_name: The name of the resource.
        :param BillingAccountSinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BillingAccountSinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_options: Optional[pulumi.Input[pulumi.InputType['BillingAccountSinkBigqueryOptionsArgs']]] = None,
                 billing_account: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingAccountSinkExclusionArgs']]]]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BillingAccountSinkArgs.__new__(BillingAccountSinkArgs)

            __props__.__dict__["bigquery_options"] = bigquery_options
            if billing_account is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account'")
            __props__.__dict__["billing_account"] = billing_account
            __props__.__dict__["description"] = description
            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__.__dict__["destination"] = destination
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["exclusions"] = exclusions
            __props__.__dict__["filter"] = filter
            __props__.__dict__["name"] = name
            __props__.__dict__["writer_identity"] = None
        super(BillingAccountSink, __self__).__init__(
            'gcp:logging/billingAccountSink:BillingAccountSink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bigquery_options: Optional[pulumi.Input[pulumi.InputType['BillingAccountSinkBigqueryOptionsArgs']]] = None,
            billing_account: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            destination: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingAccountSinkExclusionArgs']]]]] = None,
            filter: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            writer_identity: Optional[pulumi.Input[str]] = None) -> 'BillingAccountSink':
        """
        Get an existing BillingAccountSink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BillingAccountSinkBigqueryOptionsArgs']] bigquery_options: Options that affect sinks exporting data to BigQuery. Structure documented below.
        :param pulumi.Input[str] billing_account: The billing account exported to the sink.
        :param pulumi.Input[str] description: A description of this sink. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] destination: The destination of the sink (or, in other words, where logs are written to). Can be a
               Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:
               
               - `storage.googleapis.com/[GCS_BUCKET]`
               - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
               - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
               - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`
               
               The writer associated with the sink must have access to write to the above resource.
        :param pulumi.Input[bool] disabled: If set to True, then this sink is disabled and it does not export any log entries.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BillingAccountSinkExclusionArgs']]]] exclusions: Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        :param pulumi.Input[str] filter: The filter to apply when exporting logs. Only log entries that match the filter are exported.
               See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
               write a filter.
        :param pulumi.Input[str] name: The name of the logging sink.
        :param pulumi.Input[str] writer_identity: The identity associated with this sink. This identity must be granted write access to the
               configured `destination`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BillingAccountSinkState.__new__(_BillingAccountSinkState)

        __props__.__dict__["bigquery_options"] = bigquery_options
        __props__.__dict__["billing_account"] = billing_account
        __props__.__dict__["description"] = description
        __props__.__dict__["destination"] = destination
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["exclusions"] = exclusions
        __props__.__dict__["filter"] = filter
        __props__.__dict__["name"] = name
        __props__.__dict__["writer_identity"] = writer_identity
        return BillingAccountSink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> pulumi.Output['outputs.BillingAccountSinkBigqueryOptions']:
        """
        Options that affect sinks exporting data to BigQuery. Structure documented below.
        """
        return pulumi.get(self, "bigquery_options")

    @property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[str]:
        """
        The billing account exported to the sink.
        """
        return pulumi.get(self, "billing_account")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of this sink. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[str]:
        """
        The destination of the sink (or, in other words, where logs are written to). Can be a
        Cloud Storage bucket, a PubSub topic, a BigQuery dataset or a Cloud Logging bucket. Examples:

        - `storage.googleapis.com/[GCS_BUCKET]`
        - `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]`
        - `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`
        - `logging.googleapis.com/projects/[PROJECT_ID]]/locations/global/buckets/[BUCKET_ID]`

        The writer associated with the sink must have access to write to the above resource.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to True, then this sink is disabled and it does not export any log entries.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def exclusions(self) -> pulumi.Output[Optional[Sequence['outputs.BillingAccountSinkExclusion']]]:
        """
        Log entries that match any of the exclusion filters will not be exported. If a log entry is matched by both `filter` and one of `exclusions.filter`, it will not be exported.  Can be repeated multiple times for multiple exclusions. Structure is documented below.
        """
        return pulumi.get(self, "exclusions")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[str]]:
        """
        The filter to apply when exporting logs. Only log entries that match the filter are exported.
        See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
        write a filter.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the logging sink.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[str]:
        """
        The identity associated with this sink. This identity must be granted write access to the
        configured `destination`.
        """
        return pulumi.get(self, "writer_identity")

