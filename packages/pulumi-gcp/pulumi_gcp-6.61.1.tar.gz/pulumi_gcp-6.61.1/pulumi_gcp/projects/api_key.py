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

__all__ = ['ApiKeyArgs', 'ApiKey']

@pulumi.input_type
class ApiKeyArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 restrictions: Optional[pulumi.Input['ApiKeyRestrictionsArgs']] = None):
        """
        The set of arguments for constructing a ApiKey resource.
        :param pulumi.Input[str] display_name: Human-readable display name of this API key. Modifiable by user.
        :param pulumi.Input[str] name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input['ApiKeyRestrictionsArgs'] restrictions: Key restrictions.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if restrictions is not None:
            pulumi.set(__self__, "restrictions", restrictions)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable display name of this API key. Modifiable by user.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def restrictions(self) -> Optional[pulumi.Input['ApiKeyRestrictionsArgs']]:
        """
        Key restrictions.
        """
        return pulumi.get(self, "restrictions")

    @restrictions.setter
    def restrictions(self, value: Optional[pulumi.Input['ApiKeyRestrictionsArgs']]):
        pulumi.set(self, "restrictions", value)


@pulumi.input_type
class _ApiKeyState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 key_string: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 restrictions: Optional[pulumi.Input['ApiKeyRestrictionsArgs']] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiKey resources.
        :param pulumi.Input[str] display_name: Human-readable display name of this API key. Modifiable by user.
        :param pulumi.Input[str] key_string: Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.
        :param pulumi.Input[str] name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input['ApiKeyRestrictionsArgs'] restrictions: Key restrictions.
        :param pulumi.Input[str] uid: Output only. Unique id in UUID4 format.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if key_string is not None:
            pulumi.set(__self__, "key_string", key_string)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if restrictions is not None:
            pulumi.set(__self__, "restrictions", restrictions)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human-readable display name of this API key. Modifiable by user.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="keyString")
    def key_string(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.
        """
        return pulumi.get(self, "key_string")

    @key_string.setter
    def key_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_string", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def restrictions(self) -> Optional[pulumi.Input['ApiKeyRestrictionsArgs']]:
        """
        Key restrictions.
        """
        return pulumi.get(self, "restrictions")

    @restrictions.setter
    def restrictions(self, value: Optional[pulumi.Input['ApiKeyRestrictionsArgs']]):
        pulumi.set(self, "restrictions", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Unique id in UUID4 format.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


class ApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 restrictions: Optional[pulumi.Input[pulumi.InputType['ApiKeyRestrictionsArgs']]] = None,
                 __props__=None):
        """
        The Apikeys Key resource

        ## Example Usage
        ### Android_key
        A basic example of a android api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                android_key_restrictions=gcp.projects.ApiKeyRestrictionsAndroidKeyRestrictionsArgs(
                    allowed_applications=[gcp.projects.ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs(
                        package_name="com.example.app123",
                        sha1_fingerprint="1699466a142d4682a5f91b50fdf400f2358e2b0b",
                    )],
                ),
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
            ))
        ```
        ### Basic_key
        A basic example of a api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                browser_key_restrictions=gcp.projects.ApiKeyRestrictionsBrowserKeyRestrictionsArgs(
                    allowed_referrers=[".*"],
                ),
            ))
        ```
        ### Ios_key
        A basic example of a ios api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                ios_key_restrictions=gcp.projects.ApiKeyRestrictionsIosKeyRestrictionsArgs(
                    allowed_bundle_ids=["com.google.app.macos"],
                ),
            ))
        ```
        ### Minimal_key
        A minimal example of a api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name)
        ```
        ### Server_key
        A basic example of a server api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                server_key_restrictions=gcp.projects.ApiKeyRestrictionsServerKeyRestrictionsArgs(
                    allowed_ips=["127.0.0.1"],
                ),
            ))
        ```

        ## Import

        Key can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default projects/{{project}}/locations/global/keys/{{name}}
        ```

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human-readable display name of this API key. Modifiable by user.
        :param pulumi.Input[str] name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[pulumi.InputType['ApiKeyRestrictionsArgs']] restrictions: Key restrictions.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApiKeyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Apikeys Key resource

        ## Example Usage
        ### Android_key
        A basic example of a android api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                android_key_restrictions=gcp.projects.ApiKeyRestrictionsAndroidKeyRestrictionsArgs(
                    allowed_applications=[gcp.projects.ApiKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationArgs(
                        package_name="com.example.app123",
                        sha1_fingerprint="1699466a142d4682a5f91b50fdf400f2358e2b0b",
                    )],
                ),
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
            ))
        ```
        ### Basic_key
        A basic example of a api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                browser_key_restrictions=gcp.projects.ApiKeyRestrictionsBrowserKeyRestrictionsArgs(
                    allowed_referrers=[".*"],
                ),
            ))
        ```
        ### Ios_key
        A basic example of a ios api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                ios_key_restrictions=gcp.projects.ApiKeyRestrictionsIosKeyRestrictionsArgs(
                    allowed_bundle_ids=["com.google.app.macos"],
                ),
            ))
        ```
        ### Minimal_key
        A minimal example of a api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name)
        ```
        ### Server_key
        A basic example of a server api keys key
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.organizations.Project("basic",
            project_id="app",
            org_id="123456789")
        primary = gcp.projects.ApiKey("primary",
            display_name="sample-key",
            project=basic.name,
            restrictions=gcp.projects.ApiKeyRestrictionsArgs(
                api_targets=[gcp.projects.ApiKeyRestrictionsApiTargetArgs(
                    service="translate.googleapis.com",
                    methods=["GET*"],
                )],
                server_key_restrictions=gcp.projects.ApiKeyRestrictionsServerKeyRestrictionsArgs(
                    allowed_ips=["127.0.0.1"],
                ),
            ))
        ```

        ## Import

        Key can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default projects/{{project}}/locations/global/keys/{{name}}
        ```

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:projects/apiKey:ApiKey default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param ApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 restrictions: Optional[pulumi.Input[pulumi.InputType['ApiKeyRestrictionsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiKeyArgs.__new__(ApiKeyArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["restrictions"] = restrictions
            __props__.__dict__["key_string"] = None
            __props__.__dict__["uid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["keyString"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ApiKey, __self__).__init__(
            'gcp:projects/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            key_string: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            restrictions: Optional[pulumi.Input[pulumi.InputType['ApiKeyRestrictionsArgs']]] = None,
            uid: Optional[pulumi.Input[str]] = None) -> 'ApiKey':
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Human-readable display name of this API key. Modifiable by user.
        :param pulumi.Input[str] key_string: Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.
        :param pulumi.Input[str] name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[pulumi.InputType['ApiKeyRestrictionsArgs']] restrictions: Key restrictions.
        :param pulumi.Input[str] uid: Output only. Unique id in UUID4 format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiKeyState.__new__(_ApiKeyState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["key_string"] = key_string
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["restrictions"] = restrictions
        __props__.__dict__["uid"] = uid
        return ApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable display name of this API key. Modifiable by user.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="keyString")
    def key_string(self) -> pulumi.Output[str]:
        """
        Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.
        """
        return pulumi.get(self, "key_string")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: `a-z?`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def restrictions(self) -> pulumi.Output[Optional['outputs.ApiKeyRestrictions']]:
        """
        Key restrictions.
        """
        return pulumi.get(self, "restrictions")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Output only. Unique id in UUID4 format.
        """
        return pulumi.get(self, "uid")

