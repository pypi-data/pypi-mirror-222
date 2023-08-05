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

__all__ = ['FeatureMembershipArgs', 'FeatureMembership']

@pulumi.input_type
class FeatureMembershipArgs:
    def __init__(__self__, *,
                 feature: pulumi.Input[str],
                 location: pulumi.Input[str],
                 membership: pulumi.Input[str],
                 configmanagement: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']] = None,
                 mesh: Optional[pulumi.Input['FeatureMembershipMeshArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FeatureMembership resource.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input['FeatureMembershipConfigmanagementArgs'] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input['FeatureMembershipMeshArgs'] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        pulumi.set(__self__, "feature", feature)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "membership", membership)
        if configmanagement is not None:
            pulumi.set(__self__, "configmanagement", configmanagement)
        if mesh is not None:
            pulumi.set(__self__, "mesh", mesh)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def feature(self) -> pulumi.Input[str]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @feature.setter
    def feature(self, value: pulumi.Input[str]):
        pulumi.set(self, "feature", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def membership(self) -> pulumi.Input[str]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @membership.setter
    def membership(self, value: pulumi.Input[str]):
        pulumi.set(self, "membership", value)

    @property
    @pulumi.getter
    def configmanagement(self) -> Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @configmanagement.setter
    def configmanagement(self, value: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]):
        pulumi.set(self, "configmanagement", value)

    @property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input['FeatureMembershipMeshArgs']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input['FeatureMembershipMeshArgs']]):
        pulumi.set(self, "mesh", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _FeatureMembershipState:
    def __init__(__self__, *,
                 configmanagement: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input['FeatureMembershipMeshArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FeatureMembership resources.
        :param pulumi.Input['FeatureMembershipConfigmanagementArgs'] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input['FeatureMembershipMeshArgs'] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        if configmanagement is not None:
            pulumi.set(__self__, "configmanagement", configmanagement)
        if feature is not None:
            pulumi.set(__self__, "feature", feature)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if membership is not None:
            pulumi.set(__self__, "membership", membership)
        if mesh is not None:
            pulumi.set(__self__, "mesh", mesh)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def configmanagement(self) -> Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @configmanagement.setter
    def configmanagement(self, value: Optional[pulumi.Input['FeatureMembershipConfigmanagementArgs']]):
        pulumi.set(self, "configmanagement", value)

    @property
    @pulumi.getter
    def feature(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @feature.setter
    def feature(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @membership.setter
    def membership(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "membership", value)

    @property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input['FeatureMembershipMeshArgs']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input['FeatureMembershipMeshArgs']]):
        pulumi.set(self, "mesh", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class FeatureMembership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configmanagement: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipConfigmanagementArgs']]] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipMeshArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Config Management

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement=gcp.gkehub.FeatureMembershipConfigmanagementArgs(
                version="1.6.2",
                config_sync=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncArgs(
                    git=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncGitArgs(
                        sync_repo="https://github.com/hashicorp/terraform",
                    ),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Config Management With OCI

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement=gcp.gkehub.FeatureMembershipConfigmanagementArgs(
                version="1.15.1",
                config_sync=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncArgs(
                    oci=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncOciArgs(
                        sync_repo="us-central1-docker.pkg.dev/sample-project/config-repo/config-sync-gke:latest",
                        policy_dir="config-connector",
                        sync_wait_secs="20",
                        secret_type="gcpserviceaccount",
                        gcp_service_account_email="sa@project-id.iam.gserviceaccount.com",
                    ),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Multi Cluster Service Discovery

        ```python
        import pulumi
        import pulumi_gcp as gcp

        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Service Mesh

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature", location="global",
        opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            mesh=gcp.gkehub.FeatureMembershipMeshArgs(
                management="MANAGEMENT_AUTOMATIC",
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        FeatureMembership can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{project}}/{{location}}/{{feature}}/{{membership}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{location}}/{{feature}}/{{membership}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FeatureMembershipConfigmanagementArgs']] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input[pulumi.InputType['FeatureMembershipMeshArgs']] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FeatureMembershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Config Management

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement=gcp.gkehub.FeatureMembershipConfigmanagementArgs(
                version="1.6.2",
                config_sync=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncArgs(
                    git=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncGitArgs(
                        sync_repo="https://github.com/hashicorp/terraform",
                    ),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Config Management With OCI

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            configmanagement=gcp.gkehub.FeatureMembershipConfigmanagementArgs(
                version="1.15.1",
                config_sync=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncArgs(
                    oci=gcp.gkehub.FeatureMembershipConfigmanagementConfigSyncOciArgs(
                        sync_repo="us-central1-docker.pkg.dev/sample-project/config-repo/config-sync-gke:latest",
                        policy_dir="config-connector",
                        sync_wait_secs="20",
                        secret_type="gcpserviceaccount",
                        gcp_service_account_email="sa@project-id.iam.gserviceaccount.com",
                    ),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Multi Cluster Service Discovery

        ```python
        import pulumi
        import pulumi_gcp as gcp

        feature = gcp.gkehub.Feature("feature",
            location="global",
            labels={
                "foo": "bar",
            },
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Service Mesh

        ```python
        import pulumi
        import pulumi_gcp as gcp

        cluster = gcp.container.Cluster("cluster",
            location="us-central1-a",
            initial_node_count=1,
            opts=pulumi.ResourceOptions(provider=google_beta))
        membership = gcp.gkehub.Membership("membership",
            membership_id="my-membership",
            endpoint=gcp.gkehub.MembershipEndpointArgs(
                gke_cluster=gcp.gkehub.MembershipEndpointGkeClusterArgs(
                    resource_link=cluster.id.apply(lambda id: f"//container.googleapis.com/{id}"),
                ),
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        feature = gcp.gkehub.Feature("feature", location="global",
        opts=pulumi.ResourceOptions(provider=google_beta))
        feature_member = gcp.gkehub.FeatureMembership("featureMember",
            location="global",
            feature=feature.name,
            membership=membership.membership_id,
            mesh=gcp.gkehub.FeatureMembershipMeshArgs(
                management="MANAGEMENT_AUTOMATIC",
            ),
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        FeatureMembership can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default projects/{{project}}/locations/{{location}}/features/{{feature}}/membershipId/{{membership}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{project}}/{{location}}/{{feature}}/{{membership}}
        ```

        ```sh
         $ pulumi import gcp:gkehub/featureMembership:FeatureMembership default {{location}}/{{feature}}/{{membership}}
        ```

        :param str resource_name: The name of the resource.
        :param FeatureMembershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FeatureMembershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configmanagement: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipConfigmanagementArgs']]] = None,
                 feature: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 membership: Optional[pulumi.Input[str]] = None,
                 mesh: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipMeshArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FeatureMembershipArgs.__new__(FeatureMembershipArgs)

            __props__.__dict__["configmanagement"] = configmanagement
            if feature is None and not opts.urn:
                raise TypeError("Missing required property 'feature'")
            __props__.__dict__["feature"] = feature
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            if membership is None and not opts.urn:
                raise TypeError("Missing required property 'membership'")
            __props__.__dict__["membership"] = membership
            __props__.__dict__["mesh"] = mesh
            __props__.__dict__["project"] = project
        super(FeatureMembership, __self__).__init__(
            'gcp:gkehub/featureMembership:FeatureMembership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configmanagement: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipConfigmanagementArgs']]] = None,
            feature: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            membership: Optional[pulumi.Input[str]] = None,
            mesh: Optional[pulumi.Input[pulumi.InputType['FeatureMembershipMeshArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'FeatureMembership':
        """
        Get an existing FeatureMembership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['FeatureMembershipConfigmanagementArgs']] configmanagement: Config Management-specific spec. Structure is documented below.
        :param pulumi.Input[str] feature: The name of the feature
        :param pulumi.Input[str] location: The location of the feature
        :param pulumi.Input[str] membership: The name of the membership
        :param pulumi.Input[pulumi.InputType['FeatureMembershipMeshArgs']] mesh: Service mesh specific spec. Structure is documented below.
        :param pulumi.Input[str] project: The project of the feature
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FeatureMembershipState.__new__(_FeatureMembershipState)

        __props__.__dict__["configmanagement"] = configmanagement
        __props__.__dict__["feature"] = feature
        __props__.__dict__["location"] = location
        __props__.__dict__["membership"] = membership
        __props__.__dict__["mesh"] = mesh
        __props__.__dict__["project"] = project
        return FeatureMembership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def configmanagement(self) -> pulumi.Output[Optional['outputs.FeatureMembershipConfigmanagement']]:
        """
        Config Management-specific spec. Structure is documented below.
        """
        return pulumi.get(self, "configmanagement")

    @property
    @pulumi.getter
    def feature(self) -> pulumi.Output[str]:
        """
        The name of the feature
        """
        return pulumi.get(self, "feature")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the feature
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def membership(self) -> pulumi.Output[str]:
        """
        The name of the membership
        """
        return pulumi.get(self, "membership")

    @property
    @pulumi.getter
    def mesh(self) -> pulumi.Output[Optional['outputs.FeatureMembershipMesh']]:
        """
        Service mesh specific spec. Structure is documented below.
        """
        return pulumi.get(self, "mesh")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project of the feature
        """
        return pulumi.get(self, "project")

