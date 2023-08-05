# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RegionTargetHttpsProxyArgs', 'RegionTargetHttpsProxy']

@pulumi.input_type
class RegionTargetHttpsProxyArgs:
    def __init__(__self__, *,
                 ssl_certificates: pulumi.Input[Sequence[pulumi.Input[str]]],
                 url_map: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ssl_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegionTargetHttpsProxy resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssl_certificates: A list of RegionSslCertificate resources that are used to authenticate
               connections between users and the load balancer. Currently, exactly
               one SSL certificate must be specified.
        :param pulumi.Input[str] url_map: A reference to the RegionUrlMap resource that defines the mapping from URL
               to the RegionBackendService.
               
               
               - - -
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created target https proxy should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] ssl_policy: A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
               TargetHttpsProxy resource will not have any SSL policy configured.
        """
        pulumi.set(__self__, "ssl_certificates", ssl_certificates)
        pulumi.set(__self__, "url_map", url_map)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if ssl_policy is not None:
            pulumi.set(__self__, "ssl_policy", ssl_policy)

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of RegionSslCertificate resources that are used to authenticate
        connections between users and the load balancer. Currently, exactly
        one SSL certificate must be specified.
        """
        return pulumi.get(self, "ssl_certificates")

    @ssl_certificates.setter
    def ssl_certificates(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "ssl_certificates", value)

    @property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> pulumi.Input[str]:
        """
        A reference to the RegionUrlMap resource that defines the mapping from URL
        to the RegionBackendService.


        - - -
        """
        return pulumi.get(self, "url_map")

    @url_map.setter
    def url_map(self, value: pulumi.Input[str]):
        pulumi.set(self, "url_map", value)

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
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The Region in which the created target https proxy should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
        TargetHttpsProxy resource will not have any SSL policy configured.
        """
        return pulumi.get(self, "ssl_policy")

    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_policy", value)


@pulumi.input_type
class _RegionTargetHttpsProxyState:
    def __init__(__self__, *,
                 creation_timestamp: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 proxy_id: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_policy: Optional[pulumi.Input[str]] = None,
                 url_map: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RegionTargetHttpsProxy resources.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[int] proxy_id: The unique identifier for the resource.
        :param pulumi.Input[str] region: The Region in which the created target https proxy should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssl_certificates: A list of RegionSslCertificate resources that are used to authenticate
               connections between users and the load balancer. Currently, exactly
               one SSL certificate must be specified.
        :param pulumi.Input[str] ssl_policy: A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
               TargetHttpsProxy resource will not have any SSL policy configured.
        :param pulumi.Input[str] url_map: A reference to the RegionUrlMap resource that defines the mapping from URL
               to the RegionBackendService.
               
               
               - - -
        """
        if creation_timestamp is not None:
            pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if proxy_id is not None:
            pulumi.set(__self__, "proxy_id", proxy_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if ssl_certificates is not None:
            pulumi.set(__self__, "ssl_certificates", ssl_certificates)
        if ssl_policy is not None:
            pulumi.set(__self__, "ssl_policy", ssl_policy)
        if url_map is not None:
            pulumi.set(__self__, "url_map", url_map)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_timestamp", value)

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
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
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
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> Optional[pulumi.Input[int]]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "proxy_id")

    @proxy_id.setter
    def proxy_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "proxy_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The Region in which the created target https proxy should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

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

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of RegionSslCertificate resources that are used to authenticate
        connections between users and the load balancer. Currently, exactly
        one SSL certificate must be specified.
        """
        return pulumi.get(self, "ssl_certificates")

    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ssl_certificates", value)

    @property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
        TargetHttpsProxy resource will not have any SSL policy configured.
        """
        return pulumi.get(self, "ssl_policy")

    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_policy", value)

    @property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the RegionUrlMap resource that defines the mapping from URL
        to the RegionBackendService.


        - - -
        """
        return pulumi.get(self, "url_map")

    @url_map.setter
    def url_map(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_map", value)


class RegionTargetHttpsProxy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_policy: Optional[pulumi.Input[str]] = None,
                 url_map: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a RegionTargetHttpsProxy resource, which is used by one or more
        forwarding rules to route incoming HTTPS requests to a URL map.

        To get more information about RegionTargetHttpsProxy, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/target-proxies)

        ## Example Usage

        ## Import

        RegionTargetHttpsProxy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default projects/{{project}}/regions/{{region}}/targetHttpsProxies/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region: The Region in which the created target https proxy should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssl_certificates: A list of RegionSslCertificate resources that are used to authenticate
               connections between users and the load balancer. Currently, exactly
               one SSL certificate must be specified.
        :param pulumi.Input[str] ssl_policy: A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
               TargetHttpsProxy resource will not have any SSL policy configured.
        :param pulumi.Input[str] url_map: A reference to the RegionUrlMap resource that defines the mapping from URL
               to the RegionBackendService.
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegionTargetHttpsProxyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a RegionTargetHttpsProxy resource, which is used by one or more
        forwarding rules to route incoming HTTPS requests to a URL map.

        To get more information about RegionTargetHttpsProxy, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/target-proxies)

        ## Example Usage

        ## Import

        RegionTargetHttpsProxy can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default projects/{{project}}/regions/{{region}}/targetHttpsProxies/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{project}}/{{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{region}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy default {{name}}
        ```

        :param str resource_name: The name of the resource.
        :param RegionTargetHttpsProxyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegionTargetHttpsProxyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssl_policy: Optional[pulumi.Input[str]] = None,
                 url_map: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegionTargetHttpsProxyArgs.__new__(RegionTargetHttpsProxyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["region"] = region
            if ssl_certificates is None and not opts.urn:
                raise TypeError("Missing required property 'ssl_certificates'")
            __props__.__dict__["ssl_certificates"] = ssl_certificates
            __props__.__dict__["ssl_policy"] = ssl_policy
            if url_map is None and not opts.urn:
                raise TypeError("Missing required property 'url_map'")
            __props__.__dict__["url_map"] = url_map
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["proxy_id"] = None
            __props__.__dict__["self_link"] = None
        super(RegionTargetHttpsProxy, __self__).__init__(
            'gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_timestamp: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            proxy_id: Optional[pulumi.Input[int]] = None,
            region: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ssl_policy: Optional[pulumi.Input[str]] = None,
            url_map: Optional[pulumi.Input[str]] = None) -> 'RegionTargetHttpsProxy':
        """
        Get an existing RegionTargetHttpsProxy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_timestamp: Creation timestamp in RFC3339 text format.
        :param pulumi.Input[str] description: An optional description of this resource.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is
               created. The name must be 1-63 characters long, and comply with
               RFC1035. Specifically, the name must be 1-63 characters long and match
               the regular expression `a-z?` which means the
               first character must be a lowercase letter, and all following
               characters must be a dash, lowercase letter, or digit, except the last
               character, which cannot be a dash.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[int] proxy_id: The unique identifier for the resource.
        :param pulumi.Input[str] region: The Region in which the created target https proxy should reside.
               If it is not provided, the provider region is used.
        :param pulumi.Input[str] self_link: The URI of the created resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssl_certificates: A list of RegionSslCertificate resources that are used to authenticate
               connections between users and the load balancer. Currently, exactly
               one SSL certificate must be specified.
        :param pulumi.Input[str] ssl_policy: A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
               TargetHttpsProxy resource will not have any SSL policy configured.
        :param pulumi.Input[str] url_map: A reference to the RegionUrlMap resource that defines the mapping from URL
               to the RegionBackendService.
               
               
               - - -
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegionTargetHttpsProxyState.__new__(_RegionTargetHttpsProxyState)

        __props__.__dict__["creation_timestamp"] = creation_timestamp
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["proxy_id"] = proxy_id
        __props__.__dict__["region"] = region
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["ssl_certificates"] = ssl_certificates
        __props__.__dict__["ssl_policy"] = ssl_policy
        __props__.__dict__["url_map"] = url_map
        return RegionTargetHttpsProxy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression `a-z?` which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.
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
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Output[int]:
        """
        The unique identifier for the resource.
        """
        return pulumi.get(self, "proxy_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The Region in which the created target https proxy should reside.
        If it is not provided, the provider region is used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        The URI of the created resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of RegionSslCertificate resources that are used to authenticate
        connections between users and the load balancer. Currently, exactly
        one SSL certificate must be specified.
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[Optional[str]]:
        """
        A reference to the Region SslPolicy resource that will be associated with the TargetHttpsProxy resource. If not set, the
        TargetHttpsProxy resource will not have any SSL policy configured.
        """
        return pulumi.get(self, "ssl_policy")

    @property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> pulumi.Output[str]:
        """
        A reference to the RegionUrlMap resource that defines the mapping from URL
        to the RegionBackendService.


        - - -
        """
        return pulumi.get(self, "url_map")

