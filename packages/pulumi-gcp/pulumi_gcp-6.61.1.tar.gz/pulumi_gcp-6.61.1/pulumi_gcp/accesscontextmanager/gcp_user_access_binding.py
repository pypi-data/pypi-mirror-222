# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GcpUserAccessBindingArgs', 'GcpUserAccessBinding']

@pulumi.input_type
class GcpUserAccessBindingArgs:
    def __init__(__self__, *,
                 access_levels: pulumi.Input[str],
                 group_key: pulumi.Input[str],
                 organization_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GcpUserAccessBinding resource.
        :param pulumi.Input[str] access_levels: Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        :param pulumi.Input[str] group_key: Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        :param pulumi.Input[str] organization_id: Required. ID of the parent organization.
               
               
               - - -
        """
        pulumi.set(__self__, "access_levels", access_levels)
        pulumi.set(__self__, "group_key", group_key)
        pulumi.set(__self__, "organization_id", organization_id)

    @property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> pulumi.Input[str]:
        """
        Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        """
        return pulumi.get(self, "access_levels")

    @access_levels.setter
    def access_levels(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_levels", value)

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Input[str]:
        """
        Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        """
        return pulumi.get(self, "group_key")

    @group_key.setter
    def group_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_key", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        """
        Required. ID of the parent organization.


        - - -
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)


@pulumi.input_type
class _GcpUserAccessBindingState:
    def __init__(__self__, *,
                 access_levels: Optional[pulumi.Input[str]] = None,
                 group_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GcpUserAccessBinding resources.
        :param pulumi.Input[str] access_levels: Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        :param pulumi.Input[str] group_key: Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        :param pulumi.Input[str] name: Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by RFC 3986 Section 2.3). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
        :param pulumi.Input[str] organization_id: Required. ID of the parent organization.
               
               
               - - -
        """
        if access_levels is not None:
            pulumi.set(__self__, "access_levels", access_levels)
        if group_key is not None:
            pulumi.set(__self__, "group_key", group_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)

    @property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        """
        return pulumi.get(self, "access_levels")

    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_levels", value)

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        """
        return pulumi.get(self, "group_key")

    @group_key.setter
    def group_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by RFC 3986 Section 2.3). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. ID of the parent organization.


        - - -
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)


class GcpUserAccessBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_levels: Optional[pulumi.Input[str]] = None,
                 group_key: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Restricts access to Cloud Console and Google Cloud APIs for a set of users using Context-Aware Access.

        To get more information about GcpUserAccessBinding, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings)

        ## Example Usage

        ## Import

        GcpUserAccessBinding can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:accesscontextmanager/gcpUserAccessBinding:GcpUserAccessBinding default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_levels: Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        :param pulumi.Input[str] group_key: Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        :param pulumi.Input[str] organization_id: Required. ID of the parent organization.
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GcpUserAccessBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Restricts access to Cloud Console and Google Cloud APIs for a set of users using Context-Aware Access.

        To get more information about GcpUserAccessBinding, see:

        * [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings)

        ## Example Usage

        ## Import

        GcpUserAccessBinding can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:accesscontextmanager/gcpUserAccessBinding:GcpUserAccessBinding default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param GcpUserAccessBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GcpUserAccessBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_levels: Optional[pulumi.Input[str]] = None,
                 group_key: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GcpUserAccessBindingArgs.__new__(GcpUserAccessBindingArgs)

            if access_levels is None and not opts.urn:
                raise TypeError("Missing required property 'access_levels'")
            __props__.__dict__["access_levels"] = access_levels
            if group_key is None and not opts.urn:
                raise TypeError("Missing required property 'group_key'")
            __props__.__dict__["group_key"] = group_key
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["name"] = None
        super(GcpUserAccessBinding, __self__).__init__(
            'gcp:accesscontextmanager/gcpUserAccessBinding:GcpUserAccessBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_levels: Optional[pulumi.Input[str]] = None,
            group_key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None) -> 'GcpUserAccessBinding':
        """
        Get an existing GcpUserAccessBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_levels: Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        :param pulumi.Input[str] group_key: Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        :param pulumi.Input[str] name: Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by RFC 3986 Section 2.3). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
        :param pulumi.Input[str] organization_id: Required. ID of the parent organization.
               
               
               - - -
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GcpUserAccessBindingState.__new__(_GcpUserAccessBindingState)

        __props__.__dict__["access_levels"] = access_levels
        __props__.__dict__["group_key"] = group_key
        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        return GcpUserAccessBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> pulumi.Output[str]:
        """
        Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        """
        return pulumi.get(self, "access_levels")

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Output[str]:
        """
        Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the G Suite Directory API's Groups resource. If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        """
        return pulumi.get(self, "group_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by RFC 3986 Section 2.3). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        Required. ID of the parent organization.


        - - -
        """
        return pulumi.get(self, "organization_id")

