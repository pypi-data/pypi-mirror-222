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

__all__ = ['LinkedDatasetArgs', 'LinkedDataset']

@pulumi.input_type
class LinkedDatasetArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 link_id: pulumi.Input[str],
                 bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LinkedDataset resource.
        :param pulumi.Input[str] bucket: The bucket to which the linked dataset is attached.
               
               
               - - -
        :param pulumi.Input[str] link_id: The id of the linked dataset.
        :param pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]] bigquery_datasets: The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
               with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
               Views corresponding to the LogViews in the bucket.
               Structure is documented below.
        :param pulumi.Input[str] description: Describes this link. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] location: The location of the linked dataset.
        :param pulumi.Input[str] parent: The parent of the linked dataset.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "link_id", link_id)
        if bigquery_datasets is not None:
            pulumi.set(__self__, "bigquery_datasets", bigquery_datasets)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The bucket to which the linked dataset is attached.


        - - -
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Input[str]:
        """
        The id of the linked dataset.
        """
        return pulumi.get(self, "link_id")

    @link_id.setter
    def link_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "link_id", value)

    @property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]]:
        """
        The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
        with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
        Views corresponding to the LogViews in the bucket.
        Structure is documented below.
        """
        return pulumi.get(self, "bigquery_datasets")

    @bigquery_datasets.setter
    def bigquery_datasets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]]):
        pulumi.set(self, "bigquery_datasets", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Describes this link. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the linked dataset.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The parent of the linked dataset.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)


@pulumi.input_type
class _LinkedDatasetState:
    def __init__(__self__, *,
                 bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lifecycle_state: Optional[pulumi.Input[str]] = None,
                 link_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LinkedDataset resources.
        :param pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]] bigquery_datasets: The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
               with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
               Views corresponding to the LogViews in the bucket.
               Structure is documented below.
        :param pulumi.Input[str] bucket: The bucket to which the linked dataset is attached.
               
               
               - - -
        :param pulumi.Input[str] create_time: Output only. The creation timestamp of the link. A timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
               and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: Describes this link. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] lifecycle_state: Output only. The linked dataset lifecycle state.
        :param pulumi.Input[str] link_id: The id of the linked dataset.
        :param pulumi.Input[str] location: The location of the linked dataset.
        :param pulumi.Input[str] name: The resource name of the linked dataset. The name can have up to 100 characters. A valid link id
               (at the end of the link name) must only have alphanumeric characters and underscores within it.
        :param pulumi.Input[str] parent: The parent of the linked dataset.
        """
        if bigquery_datasets is not None:
            pulumi.set(__self__, "bigquery_datasets", bigquery_datasets)
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lifecycle_state is not None:
            pulumi.set(__self__, "lifecycle_state", lifecycle_state)
        if link_id is not None:
            pulumi.set(__self__, "link_id", link_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)

    @property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]]:
        """
        The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
        with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
        Views corresponding to the LogViews in the bucket.
        Structure is documented below.
        """
        return pulumi.get(self, "bigquery_datasets")

    @bigquery_datasets.setter
    def bigquery_datasets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatasetBigqueryDatasetArgs']]]]):
        pulumi.set(self, "bigquery_datasets", value)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The bucket to which the linked dataset is attached.


        - - -
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The creation timestamp of the link. A timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
        and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Describes this link. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The linked dataset lifecycle state.
        """
        return pulumi.get(self, "lifecycle_state")

    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_state", value)

    @property
    @pulumi.getter(name="linkId")
    def link_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the linked dataset.
        """
        return pulumi.get(self, "link_id")

    @link_id.setter
    def link_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "link_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the linked dataset.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the linked dataset. The name can have up to 100 characters. A valid link id
        (at the end of the link name) must only have alphanumeric characters and underscores within it.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The parent of the linked dataset.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)


class LinkedDataset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LinkedDatasetBigqueryDatasetArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 link_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes a BigQuery linked dataset

        To get more information about LinkedDataset, see:

        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets.links)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/logging/docs/apis)

        ## Example Usage
        ### Logging Linked Dataset Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        logging_linked_dataset_project_bucket_config = gcp.logging.ProjectBucketConfig("loggingLinkedDatasetProjectBucketConfig",
            location="global",
            project="my-project-name",
            enable_analytics=True,
            bucket_id="my-bucket")
        logging_linked_dataset_linked_dataset = gcp.logging.LinkedDataset("loggingLinkedDatasetLinkedDataset",
            link_id="mylink",
            bucket=logging_linked_dataset_project_bucket_config.id,
            description="Linked dataset test")
        ```
        ### Logging Linked Dataset All Params

        ```python
        import pulumi
        import pulumi_gcp as gcp

        logging_linked_dataset_project_bucket_config = gcp.logging.ProjectBucketConfig("loggingLinkedDatasetProjectBucketConfig",
            bucket_id="my-bucket",
            enable_analytics=True,
            location="global",
            project="my-project-name")
        logging_linked_dataset_linked_dataset = gcp.logging.LinkedDataset("loggingLinkedDatasetLinkedDataset",
            bucket="my-bucket",
            description="Linked dataset test",
            link_id="mylink",
            location="global",
            parent="projects/my-project-name",
            opts=pulumi.ResourceOptions(depends_on=["google_logging_project_bucket_config.logging_linked_dataset"]))
        ```

        ## Import

        LinkedDataset can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:logging/linkedDataset:LinkedDataset default {{parent}}/locations/{{location}}/buckets/{{bucket}}/links/{{link_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LinkedDatasetBigqueryDatasetArgs']]]] bigquery_datasets: The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
               with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
               Views corresponding to the LogViews in the bucket.
               Structure is documented below.
        :param pulumi.Input[str] bucket: The bucket to which the linked dataset is attached.
               
               
               - - -
        :param pulumi.Input[str] description: Describes this link. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] link_id: The id of the linked dataset.
        :param pulumi.Input[str] location: The location of the linked dataset.
        :param pulumi.Input[str] parent: The parent of the linked dataset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkedDatasetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a BigQuery linked dataset

        To get more information about LinkedDataset, see:

        * [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets.links)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/logging/docs/apis)

        ## Example Usage
        ### Logging Linked Dataset Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        logging_linked_dataset_project_bucket_config = gcp.logging.ProjectBucketConfig("loggingLinkedDatasetProjectBucketConfig",
            location="global",
            project="my-project-name",
            enable_analytics=True,
            bucket_id="my-bucket")
        logging_linked_dataset_linked_dataset = gcp.logging.LinkedDataset("loggingLinkedDatasetLinkedDataset",
            link_id="mylink",
            bucket=logging_linked_dataset_project_bucket_config.id,
            description="Linked dataset test")
        ```
        ### Logging Linked Dataset All Params

        ```python
        import pulumi
        import pulumi_gcp as gcp

        logging_linked_dataset_project_bucket_config = gcp.logging.ProjectBucketConfig("loggingLinkedDatasetProjectBucketConfig",
            bucket_id="my-bucket",
            enable_analytics=True,
            location="global",
            project="my-project-name")
        logging_linked_dataset_linked_dataset = gcp.logging.LinkedDataset("loggingLinkedDatasetLinkedDataset",
            bucket="my-bucket",
            description="Linked dataset test",
            link_id="mylink",
            location="global",
            parent="projects/my-project-name",
            opts=pulumi.ResourceOptions(depends_on=["google_logging_project_bucket_config.logging_linked_dataset"]))
        ```

        ## Import

        LinkedDataset can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:logging/linkedDataset:LinkedDataset default {{parent}}/locations/{{location}}/buckets/{{bucket}}/links/{{link_id}}
        ```

        :param str resource_name: The name of the resource.
        :param LinkedDatasetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkedDatasetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LinkedDatasetBigqueryDatasetArgs']]]]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 link_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkedDatasetArgs.__new__(LinkedDatasetArgs)

            __props__.__dict__["bigquery_datasets"] = bigquery_datasets
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["description"] = description
            if link_id is None and not opts.urn:
                raise TypeError("Missing required property 'link_id'")
            __props__.__dict__["link_id"] = link_id
            __props__.__dict__["location"] = location
            __props__.__dict__["parent"] = parent
            __props__.__dict__["create_time"] = None
            __props__.__dict__["lifecycle_state"] = None
            __props__.__dict__["name"] = None
        super(LinkedDataset, __self__).__init__(
            'gcp:logging/linkedDataset:LinkedDataset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bigquery_datasets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LinkedDatasetBigqueryDatasetArgs']]]]] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            lifecycle_state: Optional[pulumi.Input[str]] = None,
            link_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None) -> 'LinkedDataset':
        """
        Get an existing LinkedDataset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LinkedDatasetBigqueryDatasetArgs']]]] bigquery_datasets: The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
               with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
               Views corresponding to the LogViews in the bucket.
               Structure is documented below.
        :param pulumi.Input[str] bucket: The bucket to which the linked dataset is attached.
               
               
               - - -
        :param pulumi.Input[str] create_time: Output only. The creation timestamp of the link. A timestamp in RFC3339 UTC "Zulu" format,
               with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
               and "2014-10-02T15:01:23.045123456Z".
        :param pulumi.Input[str] description: Describes this link. The maximum length of the description is 8000 characters.
        :param pulumi.Input[str] lifecycle_state: Output only. The linked dataset lifecycle state.
        :param pulumi.Input[str] link_id: The id of the linked dataset.
        :param pulumi.Input[str] location: The location of the linked dataset.
        :param pulumi.Input[str] name: The resource name of the linked dataset. The name can have up to 100 characters. A valid link id
               (at the end of the link name) must only have alphanumeric characters and underscores within it.
        :param pulumi.Input[str] parent: The parent of the linked dataset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LinkedDatasetState.__new__(_LinkedDatasetState)

        __props__.__dict__["bigquery_datasets"] = bigquery_datasets
        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["lifecycle_state"] = lifecycle_state
        __props__.__dict__["link_id"] = link_id
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["parent"] = parent
        return LinkedDataset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bigqueryDatasets")
    def bigquery_datasets(self) -> pulumi.Output[Sequence['outputs.LinkedDatasetBigqueryDataset']]:
        """
        The information of a BigQuery Dataset. When a link is created, a BigQuery dataset is created along
        with it, in the same project as the LogBucket it's linked to. This dataset will also have BigQuery
        Views corresponding to the LogViews in the bucket.
        Structure is documented below.
        """
        return pulumi.get(self, "bigquery_datasets")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The bucket to which the linked dataset is attached.


        - - -
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. The creation timestamp of the link. A timestamp in RFC3339 UTC "Zulu" format,
        with nanosecond resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
        and "2014-10-02T15:01:23.045123456Z".
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Describes this link. The maximum length of the description is 8000 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Output[str]:
        """
        Output only. The linked dataset lifecycle state.
        """
        return pulumi.get(self, "lifecycle_state")

    @property
    @pulumi.getter(name="linkId")
    def link_id(self) -> pulumi.Output[str]:
        """
        The id of the linked dataset.
        """
        return pulumi.get(self, "link_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the linked dataset.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the linked dataset. The name can have up to 100 characters. A valid link id
        (at the end of the link name) must only have alphanumeric characters and underscores within it.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        The parent of the linked dataset.
        """
        return pulumi.get(self, "parent")

