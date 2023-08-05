# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NetworkEndpointArgs', 'NetworkEndpoint']

@pulumi.input_type
class NetworkEndpointArgs:
    def __init__(__self__, *,
                 ip_address: pulumi.Input[str],
                 network_endpoint_group: pulumi.Input[str],
                 instance: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NetworkEndpoint resource.
        :param pulumi.Input[str] ip_address: IPv4 address of network endpoint. The IP address must belong
               to a VM in GCE (either the primary IP or as part of an aliased IP
               range).
        :param pulumi.Input[str] network_endpoint_group: The network endpoint group this endpoint is part of.
               
               
               - - -
        :param pulumi.Input[str] instance: The name for a specific VM instance that the IP address belongs to.
               This is required for network endpoints of type GCE_VM_IP_PORT.
               The instance must be in the same zone of network endpoint group.
        :param pulumi.Input[int] port: Port number of network endpoint.
               **Note** `port` is required unless the Network Endpoint Group is created
               with the type of `GCE_VM_IP`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: Zone where the containing network endpoint group is located.
        """
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "network_endpoint_group", network_endpoint_group)
        if instance is not None:
            pulumi.set(__self__, "instance", instance)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[str]:
        """
        IPv4 address of network endpoint. The IP address must belong
        to a VM in GCE (either the primary IP or as part of an aliased IP
        range).
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> pulumi.Input[str]:
        """
        The network endpoint group this endpoint is part of.


        - - -
        """
        return pulumi.get(self, "network_endpoint_group")

    @network_endpoint_group.setter
    def network_endpoint_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_endpoint_group", value)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        The name for a specific VM instance that the IP address belongs to.
        This is required for network endpoints of type GCE_VM_IP_PORT.
        The instance must be in the same zone of network endpoint group.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port number of network endpoint.
        **Note** `port` is required unless the Network Endpoint Group is created
        with the type of `GCE_VM_IP`
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

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
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Zone where the containing network endpoint group is located.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _NetworkEndpointState:
    def __init__(__self__, *,
                 instance: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network_endpoint_group: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NetworkEndpoint resources.
        :param pulumi.Input[str] instance: The name for a specific VM instance that the IP address belongs to.
               This is required for network endpoints of type GCE_VM_IP_PORT.
               The instance must be in the same zone of network endpoint group.
        :param pulumi.Input[str] ip_address: IPv4 address of network endpoint. The IP address must belong
               to a VM in GCE (either the primary IP or as part of an aliased IP
               range).
        :param pulumi.Input[str] network_endpoint_group: The network endpoint group this endpoint is part of.
               
               
               - - -
        :param pulumi.Input[int] port: Port number of network endpoint.
               **Note** `port` is required unless the Network Endpoint Group is created
               with the type of `GCE_VM_IP`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: Zone where the containing network endpoint group is located.
        """
        if instance is not None:
            pulumi.set(__self__, "instance", instance)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if network_endpoint_group is not None:
            pulumi.set(__self__, "network_endpoint_group", network_endpoint_group)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[str]]:
        """
        The name for a specific VM instance that the IP address belongs to.
        This is required for network endpoints of type GCE_VM_IP_PORT.
        The instance must be in the same zone of network endpoint group.
        """
        return pulumi.get(self, "instance")

    @instance.setter
    def instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4 address of network endpoint. The IP address must belong
        to a VM in GCE (either the primary IP or as part of an aliased IP
        range).
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> Optional[pulumi.Input[str]]:
        """
        The network endpoint group this endpoint is part of.


        - - -
        """
        return pulumi.get(self, "network_endpoint_group")

    @network_endpoint_group.setter
    def network_endpoint_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_endpoint_group", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port number of network endpoint.
        **Note** `port` is required unless the Network Endpoint Group is created
        with the type of `GCE_VM_IP`
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

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
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Zone where the containing network endpoint group is located.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class NetworkEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network_endpoint_group: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Network endpoint represents a IP address and port combination that is
        part of a specific network endpoint group (NEG). NEGs are zonal
        collections of these endpoints for GCP resources within a
        single subnet. **NOTE**: Network endpoints cannot be created outside of a
        network endpoint group.

        To get more information about NetworkEndpoint, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/negs/)

        ## Example Usage
        ### Network Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-11",
            project="debian-cloud")
        default_network = gcp.compute.Network("defaultNetwork", auto_create_subnetworks=False)
        default_subnetwork = gcp.compute.Subnetwork("defaultSubnetwork",
            ip_cidr_range="10.0.0.1/16",
            region="us-central1",
            network=default_network.id)
        endpoint_instance = gcp.compute.Instance("endpoint-instance",
            machine_type="e2-medium",
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image=my_image.self_link,
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                subnetwork=default_subnetwork.id,
                access_configs=[gcp.compute.InstanceNetworkInterfaceAccessConfigArgs()],
            )])
        default_endpoint = gcp.compute.NetworkEndpoint("default-endpoint",
            network_endpoint_group=google_compute_network_endpoint_group["neg"]["name"],
            instance=endpoint_instance.name,
            port=google_compute_network_endpoint_group["neg"]["default_port"],
            ip_address=endpoint_instance.network_interfaces[0].network_ip)
        group = gcp.compute.NetworkEndpointGroup("group",
            network=default_network.id,
            subnetwork=default_subnetwork.id,
            default_port=90,
            zone="us-central1-a")
        ```

        ## Import

        NetworkEndpoint can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default projects/{{project}}/zones/{{zone}}/networkEndpointGroups/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{project}}/{{zone}}/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{zone}}/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance: The name for a specific VM instance that the IP address belongs to.
               This is required for network endpoints of type GCE_VM_IP_PORT.
               The instance must be in the same zone of network endpoint group.
        :param pulumi.Input[str] ip_address: IPv4 address of network endpoint. The IP address must belong
               to a VM in GCE (either the primary IP or as part of an aliased IP
               range).
        :param pulumi.Input[str] network_endpoint_group: The network endpoint group this endpoint is part of.
               
               
               - - -
        :param pulumi.Input[int] port: Port number of network endpoint.
               **Note** `port` is required unless the Network Endpoint Group is created
               with the type of `GCE_VM_IP`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: Zone where the containing network endpoint group is located.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Network endpoint represents a IP address and port combination that is
        part of a specific network endpoint group (NEG). NEGs are zonal
        collections of these endpoints for GCP resources within a
        single subnet. **NOTE**: Network endpoints cannot be created outside of a
        network endpoint group.

        To get more information about NetworkEndpoint, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/negs/)

        ## Example Usage
        ### Network Endpoint

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_image = gcp.compute.get_image(family="debian-11",
            project="debian-cloud")
        default_network = gcp.compute.Network("defaultNetwork", auto_create_subnetworks=False)
        default_subnetwork = gcp.compute.Subnetwork("defaultSubnetwork",
            ip_cidr_range="10.0.0.1/16",
            region="us-central1",
            network=default_network.id)
        endpoint_instance = gcp.compute.Instance("endpoint-instance",
            machine_type="e2-medium",
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image=my_image.self_link,
                ),
            ),
            network_interfaces=[gcp.compute.InstanceNetworkInterfaceArgs(
                subnetwork=default_subnetwork.id,
                access_configs=[gcp.compute.InstanceNetworkInterfaceAccessConfigArgs()],
            )])
        default_endpoint = gcp.compute.NetworkEndpoint("default-endpoint",
            network_endpoint_group=google_compute_network_endpoint_group["neg"]["name"],
            instance=endpoint_instance.name,
            port=google_compute_network_endpoint_group["neg"]["default_port"],
            ip_address=endpoint_instance.network_interfaces[0].network_ip)
        group = gcp.compute.NetworkEndpointGroup("group",
            network=default_network.id,
            subnetwork=default_subnetwork.id,
            default_port=90,
            zone="us-central1-a")
        ```

        ## Import

        NetworkEndpoint can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default projects/{{project}}/zones/{{zone}}/networkEndpointGroups/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{project}}/{{zone}}/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{zone}}/{{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        ```sh
         $ pulumi import gcp:compute/networkEndpoint:NetworkEndpoint default {{network_endpoint_group}}/{{instance}}/{{ip_address}}/{{port}}
        ```

        :param str resource_name: The name of the resource.
        :param NetworkEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network_endpoint_group: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkEndpointArgs.__new__(NetworkEndpointArgs)

            __props__.__dict__["instance"] = instance
            if ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'ip_address'")
            __props__.__dict__["ip_address"] = ip_address
            if network_endpoint_group is None and not opts.urn:
                raise TypeError("Missing required property 'network_endpoint_group'")
            __props__.__dict__["network_endpoint_group"] = network_endpoint_group
            __props__.__dict__["port"] = port
            __props__.__dict__["project"] = project
            __props__.__dict__["zone"] = zone
        super(NetworkEndpoint, __self__).__init__(
            'gcp:compute/networkEndpoint:NetworkEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            network_endpoint_group: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            project: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'NetworkEndpoint':
        """
        Get an existing NetworkEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance: The name for a specific VM instance that the IP address belongs to.
               This is required for network endpoints of type GCE_VM_IP_PORT.
               The instance must be in the same zone of network endpoint group.
        :param pulumi.Input[str] ip_address: IPv4 address of network endpoint. The IP address must belong
               to a VM in GCE (either the primary IP or as part of an aliased IP
               range).
        :param pulumi.Input[str] network_endpoint_group: The network endpoint group this endpoint is part of.
               
               
               - - -
        :param pulumi.Input[int] port: Port number of network endpoint.
               **Note** `port` is required unless the Network Endpoint Group is created
               with the type of `GCE_VM_IP`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] zone: Zone where the containing network endpoint group is located.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkEndpointState.__new__(_NetworkEndpointState)

        __props__.__dict__["instance"] = instance
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["network_endpoint_group"] = network_endpoint_group
        __props__.__dict__["port"] = port
        __props__.__dict__["project"] = project
        __props__.__dict__["zone"] = zone
        return NetworkEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def instance(self) -> pulumi.Output[Optional[str]]:
        """
        The name for a specific VM instance that the IP address belongs to.
        This is required for network endpoints of type GCE_VM_IP_PORT.
        The instance must be in the same zone of network endpoint group.
        """
        return pulumi.get(self, "instance")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        IPv4 address of network endpoint. The IP address must belong
        to a VM in GCE (either the primary IP or as part of an aliased IP
        range).
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="networkEndpointGroup")
    def network_endpoint_group(self) -> pulumi.Output[str]:
        """
        The network endpoint group this endpoint is part of.


        - - -
        """
        return pulumi.get(self, "network_endpoint_group")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        Port number of network endpoint.
        **Note** `port` is required unless the Network Endpoint Group is created
        with the type of `GCE_VM_IP`
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        Zone where the containing network endpoint group is located.
        """
        return pulumi.get(self, "zone")

