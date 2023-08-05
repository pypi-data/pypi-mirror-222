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

__all__ = ['DenyPolicyArgs', 'DenyPolicy']

@pulumi.input_type
class DenyPolicyArgs:
    def __init__(__self__, *,
                 parent: pulumi.Input[str],
                 rules: pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]],
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DenyPolicy resource.
        :param pulumi.Input[str] parent: The attachment point is identified by its URL-encoded full resource name.
        :param pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]] rules: Rules to be applied.
               Structure is documented below.
        :param pulumi.Input[str] display_name: The display name of the rule.
        :param pulumi.Input[str] name: The name of the policy.
        """
        pulumi.set(__self__, "parent", parent)
        pulumi.set(__self__, "rules", rules)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Input[str]:
        """
        The attachment point is identified by its URL-encoded full resource name.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]]:
        """
        Rules to be applied.
        Structure is documented below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the rule.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DenyPolicyState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering DenyPolicy resources.
        :param pulumi.Input[str] display_name: The display name of the rule.
        :param pulumi.Input[str] etag: The hash of the resource. Used internally during updates.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] parent: The attachment point is identified by its URL-encoded full resource name.
        :param pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]] rules: Rules to be applied.
               Structure is documented below.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the rule.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        The hash of the resource. Used internally during updates.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The attachment point is identified by its URL-encoded full resource name.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]]]:
        """
        Rules to be applied.
        Structure is documented below.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DenyPolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class DenyPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DenyPolicyRuleArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        DenyPolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:iam/denyPolicy:DenyPolicy default {{parent}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The display name of the rule.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] parent: The attachment point is identified by its URL-encoded full resource name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DenyPolicyRuleArgs']]]] rules: Rules to be applied.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DenyPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        DenyPolicy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:iam/denyPolicy:DenyPolicy default {{parent}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param DenyPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DenyPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DenyPolicyRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DenyPolicyArgs.__new__(DenyPolicyArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            if parent is None and not opts.urn:
                raise TypeError("Missing required property 'parent'")
            __props__.__dict__["parent"] = parent
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["etag"] = None
        super(DenyPolicy, __self__).__init__(
            'gcp:iam/denyPolicy:DenyPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DenyPolicyRuleArgs']]]]] = None) -> 'DenyPolicy':
        """
        Get an existing DenyPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The display name of the rule.
        :param pulumi.Input[str] etag: The hash of the resource. Used internally during updates.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] parent: The attachment point is identified by its URL-encoded full resource name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DenyPolicyRuleArgs']]]] rules: Rules to be applied.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DenyPolicyState.__new__(_DenyPolicyState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["etag"] = etag
        __props__.__dict__["name"] = name
        __props__.__dict__["parent"] = parent
        __props__.__dict__["rules"] = rules
        return DenyPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the rule.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The hash of the resource. Used internally during updates.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        The attachment point is identified by its URL-encoded full resource name.
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.DenyPolicyRule']]:
        """
        Rules to be applied.
        Structure is documented below.
        """
        return pulumi.get(self, "rules")

