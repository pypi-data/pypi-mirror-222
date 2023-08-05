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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 parent: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] parent: The resource name of the private cloud to create a new cluster in.
               Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
               For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        :param pulumi.Input[str] name: The ID of the Cluster.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]] node_type_configs: The map of cluster node types in this cluster,
               where the key is canonical identifier of the node type (corresponds to the NodeType).
               Structure is documented below.
        """
        pulumi.set(__self__, "parent", parent)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_type_configs is not None:
            pulumi.set(__self__, "node_type_configs", node_type_configs)

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Input[str]:
        """
        The resource name of the private cloud to create a new cluster in.
        Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
        For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Cluster.


        - - -
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]]:
        """
        The map of cluster node types in this cluster,
        where the key is canonical identifier of the node type (corresponds to the NodeType).
        Structure is documented below.
        """
        return pulumi.get(self, "node_type_configs")

    @node_type_configs.setter
    def node_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]]):
        pulumi.set(self, "node_type_configs", value)


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *,
                 management: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Cluster resources.
        :param pulumi.Input[bool] management: True if the cluster is a management cluster; false otherwise.
               There can only be one management cluster in a private cloud and it has to be the first one.
        :param pulumi.Input[str] name: The ID of the Cluster.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]] node_type_configs: The map of cluster node types in this cluster,
               where the key is canonical identifier of the node type (corresponds to the NodeType).
               Structure is documented below.
        :param pulumi.Input[str] parent: The resource name of the private cloud to create a new cluster in.
               Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
               For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        :param pulumi.Input[str] state: State of the Cluster.
        :param pulumi.Input[str] uid: System-generated unique identifier for the resource.
        """
        if management is not None:
            pulumi.set(__self__, "management", management)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_type_configs is not None:
            pulumi.set(__self__, "node_type_configs", node_type_configs)
        if parent is not None:
            pulumi.set(__self__, "parent", parent)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[bool]]:
        """
        True if the cluster is a management cluster; false otherwise.
        There can only be one management cluster in a private cloud and it has to be the first one.
        """
        return pulumi.get(self, "management")

    @management.setter
    def management(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "management", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Cluster.


        - - -
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]]:
        """
        The map of cluster node types in this cluster,
        where the key is canonical identifier of the node type (corresponds to the NodeType).
        Structure is documented below.
        """
        return pulumi.get(self, "node_type_configs")

    @node_type_configs.setter
    def node_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeTypeConfigArgs']]]]):
        pulumi.set(self, "node_type_configs", value)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the private cloud to create a new cluster in.
        Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
        For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the Cluster.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        System-generated unique identifier for the resource.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeTypeConfigArgs']]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Vmware Engine Cluster Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster_nw = gcp.vmwareengine.Network("cluster-nw",
            location="us-west1",
            type="LEGACY",
            description="PC network description.",
            opts=pulumi.ResourceOptions(provider=google_beta))
        cluster_pc = gcp.vmwareengine.PrivateCloud("cluster-pc",
            location="us-west1-a",
            description="Sample test PC.",
            network_config=gcp.vmwareengine.PrivateCloudNetworkConfigArgs(
                management_cidr="192.168.30.0/24",
                vmware_engine_network=cluster_nw.id,
            ),
            management_cluster=gcp.vmwareengine.PrivateCloudManagementClusterArgs(
                cluster_id="sample-mgmt-cluster",
                node_type_configs=[gcp.vmwareengine.PrivateCloudManagementClusterNodeTypeConfigArgs(
                    node_type_id="standard-72",
                    node_count=3,
                )],
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        vmw_engine_ext_cluster = gcp.vmwareengine.Cluster("vmw-engine-ext-cluster",
            parent=cluster_pc.id,
            node_type_configs=[gcp.vmwareengine.ClusterNodeTypeConfigArgs(
                node_type_id="standard-72",
                node_count=3,
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Vmware Engine Cluster Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster_nw = gcp.vmwareengine.Network("cluster-nw",
            location="us-west1",
            type="LEGACY",
            description="PC network description.",
            opts=pulumi.ResourceOptions(provider=google_beta))
        cluster_pc = gcp.vmwareengine.PrivateCloud("cluster-pc",
            location="us-west1-a",
            description="Sample test PC.",
            network_config=gcp.vmwareengine.PrivateCloudNetworkConfigArgs(
                management_cidr="192.168.30.0/24",
                vmware_engine_network=cluster_nw.id,
            ),
            management_cluster=gcp.vmwareengine.PrivateCloudManagementClusterArgs(
                cluster_id="sample-mgmt-cluster",
                node_type_configs=[gcp.vmwareengine.PrivateCloudManagementClusterNodeTypeConfigArgs(
                    node_type_id="standard-72",
                    node_count=3,
                    custom_core_count=32,
                )],
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        vmw_ext_cluster = gcp.vmwareengine.Cluster("vmw-ext-cluster",
            parent=cluster_pc.id,
            node_type_configs=[gcp.vmwareengine.ClusterNodeTypeConfigArgs(
                node_type_id="standard-72",
                node_count=3,
                custom_core_count=32,
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Cluster can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:vmwareengine/cluster:Cluster default {{parent}}/clusters/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The ID of the Cluster.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeTypeConfigArgs']]]] node_type_configs: The map of cluster node types in this cluster,
               where the key is canonical identifier of the node type (corresponds to the NodeType).
               Structure is documented below.
        :param pulumi.Input[str] parent: The resource name of the private cloud to create a new cluster in.
               Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
               For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Vmware Engine Cluster Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster_nw = gcp.vmwareengine.Network("cluster-nw",
            location="us-west1",
            type="LEGACY",
            description="PC network description.",
            opts=pulumi.ResourceOptions(provider=google_beta))
        cluster_pc = gcp.vmwareengine.PrivateCloud("cluster-pc",
            location="us-west1-a",
            description="Sample test PC.",
            network_config=gcp.vmwareengine.PrivateCloudNetworkConfigArgs(
                management_cidr="192.168.30.0/24",
                vmware_engine_network=cluster_nw.id,
            ),
            management_cluster=gcp.vmwareengine.PrivateCloudManagementClusterArgs(
                cluster_id="sample-mgmt-cluster",
                node_type_configs=[gcp.vmwareengine.PrivateCloudManagementClusterNodeTypeConfigArgs(
                    node_type_id="standard-72",
                    node_count=3,
                )],
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        vmw_engine_ext_cluster = gcp.vmwareengine.Cluster("vmw-engine-ext-cluster",
            parent=cluster_pc.id,
            node_type_configs=[gcp.vmwareengine.ClusterNodeTypeConfigArgs(
                node_type_id="standard-72",
                node_count=3,
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Vmware Engine Cluster Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster_nw = gcp.vmwareengine.Network("cluster-nw",
            location="us-west1",
            type="LEGACY",
            description="PC network description.",
            opts=pulumi.ResourceOptions(provider=google_beta))
        cluster_pc = gcp.vmwareengine.PrivateCloud("cluster-pc",
            location="us-west1-a",
            description="Sample test PC.",
            network_config=gcp.vmwareengine.PrivateCloudNetworkConfigArgs(
                management_cidr="192.168.30.0/24",
                vmware_engine_network=cluster_nw.id,
            ),
            management_cluster=gcp.vmwareengine.PrivateCloudManagementClusterArgs(
                cluster_id="sample-mgmt-cluster",
                node_type_configs=[gcp.vmwareengine.PrivateCloudManagementClusterNodeTypeConfigArgs(
                    node_type_id="standard-72",
                    node_count=3,
                    custom_core_count=32,
                )],
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        vmw_ext_cluster = gcp.vmwareengine.Cluster("vmw-ext-cluster",
            parent=cluster_pc.id,
            node_type_configs=[gcp.vmwareengine.ClusterNodeTypeConfigArgs(
                node_type_id="standard-72",
                node_count=3,
                custom_core_count=32,
            )],
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Cluster can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:vmwareengine/cluster:Cluster default {{parent}}/clusters/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeTypeConfigArgs']]]]] = None,
                 parent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["node_type_configs"] = node_type_configs
            if parent is None and not opts.urn:
                raise TypeError("Missing required property 'parent'")
            __props__.__dict__["parent"] = parent
            __props__.__dict__["management"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["uid"] = None
        super(Cluster, __self__).__init__(
            'gcp:vmwareengine/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            management: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeTypeConfigArgs']]]]] = None,
            parent: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            uid: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] management: True if the cluster is a management cluster; false otherwise.
               There can only be one management cluster in a private cloud and it has to be the first one.
        :param pulumi.Input[str] name: The ID of the Cluster.
               
               
               - - -
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeTypeConfigArgs']]]] node_type_configs: The map of cluster node types in this cluster,
               where the key is canonical identifier of the node type (corresponds to the NodeType).
               Structure is documented below.
        :param pulumi.Input[str] parent: The resource name of the private cloud to create a new cluster in.
               Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
               For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        :param pulumi.Input[str] state: State of the Cluster.
        :param pulumi.Input[str] uid: System-generated unique identifier for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterState.__new__(_ClusterState)

        __props__.__dict__["management"] = management
        __props__.__dict__["name"] = name
        __props__.__dict__["node_type_configs"] = node_type_configs
        __props__.__dict__["parent"] = parent
        __props__.__dict__["state"] = state
        __props__.__dict__["uid"] = uid
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def management(self) -> pulumi.Output[bool]:
        """
        True if the cluster is a management cluster; false otherwise.
        There can only be one management cluster in a private cloud and it has to be the first one.
        """
        return pulumi.get(self, "management")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The ID of the Cluster.


        - - -
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterNodeTypeConfig']]]:
        """
        The map of cluster node types in this cluster,
        where the key is canonical identifier of the node type (corresponds to the NodeType).
        Structure is documented below.
        """
        return pulumi.get(self, "node_type_configs")

    @property
    @pulumi.getter
    def parent(self) -> pulumi.Output[str]:
        """
        The resource name of the private cloud to create a new cluster in.
        Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names.
        For example: projects/my-project/locations/us-west1-a/privateClouds/my-cloud
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the Cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        System-generated unique identifier for the resource.
        """
        return pulumi.get(self, "uid")

