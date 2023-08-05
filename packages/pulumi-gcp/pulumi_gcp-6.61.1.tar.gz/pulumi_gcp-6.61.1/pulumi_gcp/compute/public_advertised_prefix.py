# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PublicAdvertisedPrefixArgs', 'PublicAdvertisedPrefix']

@pulumi.input_type
class PublicAdvertisedPrefixArgs:
    def __init__(__self__, *,
                 dns_verification_ip: pulumi.Input[str],
                 ip_cidr_range: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PublicAdvertisedPrefix resource.
        :param pulumi.Input[str] dns_verification_ip: The IPv4 address to be used for reverse DNS verification.
        :param pulumi.Input[str] ip_cidr_range: The IPv4 address range, in CIDR format, represented by this public advertised prefix.
               
               
               - - -
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. The name must be 1-63 characters long, and
               comply with RFC1035. Specifically, the name must be 1-63 characters
               long and match the regular expression `a-z?`
               which means the first character must be a lowercase letter, and all
               following characters must be a dash, lowercase letter, or digit,
               except the last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "dns_verification_ip", dns_verification_ip)
        pulumi.set(__self__, "ip_cidr_range", ip_cidr_range)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> pulumi.Input[str]:
        """
        The IPv4 address to be used for reverse DNS verification.
        """
        return pulumi.get(self, "dns_verification_ip")

    @dns_verification_ip.setter
    def dns_verification_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "dns_verification_ip", value)

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Input[str]:
        """
        The IPv4 address range, in CIDR format, represented by this public advertised prefix.


        - - -
        """
        return pulumi.get(self, "ip_cidr_range")

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_cidr_range", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. The name must be 1-63 characters long, and
        comply with RFC1035. Specifically, the name must be 1-63 characters
        long and match the regular expression `a-z?`
        which means the first character must be a lowercase letter, and all
        following characters must be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _PublicAdvertisedPrefixState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_verification_ip: Optional[pulumi.Input[str]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PublicAdvertisedPrefix resources.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] dns_verification_ip: The IPv4 address to be used for reverse DNS verification.
        :param pulumi.Input[str] ip_cidr_range: The IPv4 address range, in CIDR format, represented by this public advertised prefix.
               
               
               - - -
        :param pulumi.Input[str] name: Name of the resource. The name must be 1-63 characters long, and
               comply with RFC1035. Specifically, the name must be 1-63 characters
               long and match the regular expression `a-z?`
               which means the first character must be a lowercase letter, and all
               following characters must be a dash, lowercase letter, or digit,
               except the last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_verification_ip is not None:
            pulumi.set(__self__, "dns_verification_ip", dns_verification_ip)
        if ip_cidr_range is not None:
            pulumi.set(__self__, "ip_cidr_range", ip_cidr_range)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address to be used for reverse DNS verification.
        """
        return pulumi.get(self, "dns_verification_ip")

    @dns_verification_ip.setter
    def dns_verification_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_verification_ip", value)

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 address range, in CIDR format, represented by this public advertised prefix.


        - - -
        """
        return pulumi.get(self, "ip_cidr_range")

    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_cidr_range", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. The name must be 1-63 characters long, and
        comply with RFC1035. Specifically, the name must be 1-63 characters
        long and match the regular expression `a-z?`
        which means the first character must be a lowercase letter, and all
        following characters must be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)


class PublicAdvertisedPrefix(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_verification_ip: Optional[pulumi.Input[str]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a PublicAdvertisedPrefix for use with bring your own IP addresses (BYOIP).

        To get more information about PublicAdvertisedPrefix, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes)
        * How-to Guides
            * [Using bring your own IP](https://cloud.google.com/vpc/docs/using-bring-your-own-ip)

        ## Example Usage
        ### Public Advertised Prefixes Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        prefixes = gcp.compute.PublicAdvertisedPrefix("prefixes",
            description="description",
            dns_verification_ip="127.127.0.0",
            ip_cidr_range="127.127.0.0/16")
        ```

        ## Import

        PublicAdvertisedPrefix can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default projects/{{project}}/global/publicAdvertisedPrefixes/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] dns_verification_ip: The IPv4 address to be used for reverse DNS verification.
        :param pulumi.Input[str] ip_cidr_range: The IPv4 address range, in CIDR format, represented by this public advertised prefix.
               
               
               - - -
        :param pulumi.Input[str] name: Name of the resource. The name must be 1-63 characters long, and
               comply with RFC1035. Specifically, the name must be 1-63 characters
               long and match the regular expression `a-z?`
               which means the first character must be a lowercase letter, and all
               following characters must be a dash, lowercase letter, or digit,
               except the last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PublicAdvertisedPrefixArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a PublicAdvertisedPrefix for use with bring your own IP addresses (BYOIP).

        To get more information about PublicAdvertisedPrefix, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes)
        * How-to Guides
            * [Using bring your own IP](https://cloud.google.com/vpc/docs/using-bring-your-own-ip)

        ## Example Usage
        ### Public Advertised Prefixes Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        prefixes = gcp.compute.PublicAdvertisedPrefix("prefixes",
            description="description",
            dns_verification_ip="127.127.0.0",
            ip_cidr_range="127.127.0.0/16")
        ```

        ## Import

        PublicAdvertisedPrefix can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default projects/{{project}}/global/publicAdvertisedPrefixes/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default {{project}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param PublicAdvertisedPrefixArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PublicAdvertisedPrefixArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_verification_ip: Optional[pulumi.Input[str]] = None,
                 ip_cidr_range: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PublicAdvertisedPrefixArgs.__new__(PublicAdvertisedPrefixArgs)

            __props__.__dict__["description"] = description
            if dns_verification_ip is None and not opts.urn:
                raise TypeError("Missing required property 'dns_verification_ip'")
            __props__.__dict__["dns_verification_ip"] = dns_verification_ip
            if ip_cidr_range is None and not opts.urn:
                raise TypeError("Missing required property 'ip_cidr_range'")
            __props__.__dict__["ip_cidr_range"] = ip_cidr_range
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["self_link"] = None
        super(PublicAdvertisedPrefix, __self__).__init__(
            'gcp:compute/publicAdvertisedPrefix:PublicAdvertisedPrefix',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_verification_ip: Optional[pulumi.Input[str]] = None,
            ip_cidr_range: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'PublicAdvertisedPrefix':
        """
        Get an existing PublicAdvertisedPrefix resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] dns_verification_ip: The IPv4 address to be used for reverse DNS verification.
        :param pulumi.Input[str] ip_cidr_range: The IPv4 address range, in CIDR format, represented by this public advertised prefix.
               
               
               - - -
        :param pulumi.Input[str] name: Name of the resource. The name must be 1-63 characters long, and
               comply with RFC1035. Specifically, the name must be 1-63 characters
               long and match the regular expression `a-z?`
               which means the first character must be a lowercase letter, and all
               following characters must be a dash, lowercase letter, or digit,
               except the last character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PublicAdvertisedPrefixState.__new__(_PublicAdvertisedPrefixState)

        __props__.__dict__["description"] = description
        __props__.__dict__["dns_verification_ip"] = dns_verification_ip
        __props__.__dict__["ip_cidr_range"] = ip_cidr_range
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["self_link"] = self_link
        return PublicAdvertisedPrefix(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsVerificationIp")
    def dns_verification_ip(self) -> pulumi.Output[str]:
        """
        The IPv4 address to be used for reverse DNS verification.
        """
        return pulumi.get(self, "dns_verification_ip")

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[str]:
        """
        The IPv4 address range, in CIDR format, represented by this public advertised prefix.


        - - -
        """
        return pulumi.get(self, "ip_cidr_range")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. The name must be 1-63 characters long, and
        comply with RFC1035. Specifically, the name must be 1-63 characters
        long and match the regular expression `a-z?`
        which means the first character must be a lowercase letter, and all
        following characters must be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

