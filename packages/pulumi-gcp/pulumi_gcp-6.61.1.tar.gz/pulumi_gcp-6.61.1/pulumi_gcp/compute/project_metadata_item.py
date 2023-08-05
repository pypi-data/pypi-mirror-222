# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ProjectMetadataItemArgs', 'ProjectMetadataItem']

@pulumi.input_type
class ProjectMetadataItemArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProjectMetadataItem resource.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
               
               - - -
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The metadata key to set.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value to set for the given metadata key.

        - - -
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ProjectMetadataItemState:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectMetadataItem resources.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
               
               - - -
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The metadata key to set.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value to set for the given metadata key.

        - - -
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class ProjectMetadataItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a single key/value pair on metadata common to all instances for
        a project in GCE. Using `compute.ProjectMetadataItem` lets you
        manage a single key/value setting in the provider rather than the entire
        project metadata map.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ProjectMetadataItem("default",
            key="my_metadata",
            value="my_value")
        ```

        ## Import

        Project metadata items can be imported using the `key`, e.g.

        ```sh
         $ pulumi import gcp:compute/projectMetadataItem:ProjectMetadataItem default my_metadata
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectMetadataItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a single key/value pair on metadata common to all instances for
        a project in GCE. Using `compute.ProjectMetadataItem` lets you
        manage a single key/value setting in the provider rather than the entire
        project metadata map.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.compute.ProjectMetadataItem("default",
            key="my_metadata",
            value="my_value")
        ```

        ## Import

        Project metadata items can be imported using the `key`, e.g.

        ```sh
         $ pulumi import gcp:compute/projectMetadataItem:ProjectMetadataItem default my_metadata
        ```

        :param str resource_name: The name of the resource.
        :param ProjectMetadataItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectMetadataItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectMetadataItemArgs.__new__(ProjectMetadataItemArgs)

            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["project"] = project
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
        super(ProjectMetadataItem, __self__).__init__(
            'gcp:compute/projectMetadataItem:ProjectMetadataItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'ProjectMetadataItem':
        """
        Get an existing ProjectMetadataItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The metadata key to set.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] value: The value to set for the given metadata key.
               
               - - -
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectMetadataItemState.__new__(_ProjectMetadataItemState)

        __props__.__dict__["key"] = key
        __props__.__dict__["project"] = project
        __props__.__dict__["value"] = value
        return ProjectMetadataItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The metadata key to set.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value to set for the given metadata key.

        - - -
        """
        return pulumi.get(self, "value")

