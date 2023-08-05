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

__all__ = ['AssetArgs', 'Asset']

@pulumi.input_type
class AssetArgs:
    def __init__(__self__, *,
                 dataplex_zone: pulumi.Input[str],
                 discovery_spec: pulumi.Input['AssetDiscoverySpecArgs'],
                 lake: pulumi.Input[str],
                 location: pulumi.Input[str],
                 resource_spec: pulumi.Input['AssetResourceSpecArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Asset resource.
        :param pulumi.Input[str] dataplex_zone: The zone for the resource
        :param pulumi.Input['AssetDiscoverySpecArgs'] discovery_spec: Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        :param pulumi.Input[str] lake: The lake for the resource
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input['AssetResourceSpecArgs'] resource_spec: Required. Immutable. Specification of the resource that is referenced by this asset.
        :param pulumi.Input[str] description: Optional. Description of the asset.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the asset.
        :param pulumi.Input[str] name: The name of the asset.
        :param pulumi.Input[str] project: The project for the resource
        """
        pulumi.set(__self__, "dataplex_zone", dataplex_zone)
        pulumi.set(__self__, "discovery_spec", discovery_spec)
        pulumi.set(__self__, "lake", lake)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "resource_spec", resource_spec)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Input[str]:
        """
        The zone for the resource
        """
        return pulumi.get(self, "dataplex_zone")

    @dataplex_zone.setter
    def dataplex_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataplex_zone", value)

    @property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> pulumi.Input['AssetDiscoverySpecArgs']:
        """
        Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        """
        return pulumi.get(self, "discovery_spec")

    @discovery_spec.setter
    def discovery_spec(self, value: pulumi.Input['AssetDiscoverySpecArgs']):
        pulumi.set(self, "discovery_spec", value)

    @property
    @pulumi.getter
    def lake(self) -> pulumi.Input[str]:
        """
        The lake for the resource
        """
        return pulumi.get(self, "lake")

    @lake.setter
    def lake(self, value: pulumi.Input[str]):
        pulumi.set(self, "lake", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Input['AssetResourceSpecArgs']:
        """
        Required. Immutable. Specification of the resource that is referenced by this asset.
        """
        return pulumi.get(self, "resource_spec")

    @resource_spec.setter
    def resource_spec(self, value: pulumi.Input['AssetResourceSpecArgs']):
        pulumi.set(self, "resource_spec", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the asset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. User defined labels for the asset.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the asset.
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


@pulumi.input_type
class _AssetState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 dataplex_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input['AssetDiscoverySpecArgs']] = None,
                 discovery_statuses: Optional[pulumi.Input[Sequence[pulumi.Input['AssetDiscoveryStatusArgs']]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lake: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input['AssetResourceSpecArgs']] = None,
                 resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input['AssetResourceStatusArgs']]]] = None,
                 security_statuses: Optional[pulumi.Input[Sequence[pulumi.Input['AssetSecurityStatusArgs']]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Asset resources.
        :param pulumi.Input[str] create_time: Output only. The time when the asset was created.
        :param pulumi.Input[str] dataplex_zone: The zone for the resource
        :param pulumi.Input[str] description: Optional. Description of the asset.
        :param pulumi.Input['AssetDiscoverySpecArgs'] discovery_spec: Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        :param pulumi.Input[Sequence[pulumi.Input['AssetDiscoveryStatusArgs']]] discovery_statuses: Output only. Status of the discovery feature applied to data referenced by this asset.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the asset.
        :param pulumi.Input[str] lake: The lake for the resource
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: The name of the asset.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input['AssetResourceSpecArgs'] resource_spec: Required. Immutable. Specification of the resource that is referenced by this asset.
        :param pulumi.Input[Sequence[pulumi.Input['AssetResourceStatusArgs']]] resource_statuses: Output only. Status of the resource referenced by this asset.
        :param pulumi.Input[Sequence[pulumi.Input['AssetSecurityStatusArgs']]] security_statuses: Output only. Status of the security policy applied to resource referenced by this asset.
        :param pulumi.Input[str] state: Output only. Current state of the asset. Possible values: STATE_UNSPECIFIED, ACTIVE, CREATING, DELETING, ACTION_REQUIRED
        :param pulumi.Input[str] uid: Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.
        :param pulumi.Input[str] update_time: Output only. The time when the asset was last updated.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if dataplex_zone is not None:
            pulumi.set(__self__, "dataplex_zone", dataplex_zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if discovery_spec is not None:
            pulumi.set(__self__, "discovery_spec", discovery_spec)
        if discovery_statuses is not None:
            pulumi.set(__self__, "discovery_statuses", discovery_statuses)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if lake is not None:
            pulumi.set(__self__, "lake", lake)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if resource_spec is not None:
            pulumi.set(__self__, "resource_spec", resource_spec)
        if resource_statuses is not None:
            pulumi.set(__self__, "resource_statuses", resource_statuses)
        if security_statuses is not None:
            pulumi.set(__self__, "security_statuses", security_statuses)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The time when the asset was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone for the resource
        """
        return pulumi.get(self, "dataplex_zone")

    @dataplex_zone.setter
    def dataplex_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataplex_zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Description of the asset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> Optional[pulumi.Input['AssetDiscoverySpecArgs']]:
        """
        Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        """
        return pulumi.get(self, "discovery_spec")

    @discovery_spec.setter
    def discovery_spec(self, value: Optional[pulumi.Input['AssetDiscoverySpecArgs']]):
        pulumi.set(self, "discovery_spec", value)

    @property
    @pulumi.getter(name="discoveryStatuses")
    def discovery_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetDiscoveryStatusArgs']]]]:
        """
        Output only. Status of the discovery feature applied to data referenced by this asset.
        """
        return pulumi.get(self, "discovery_statuses")

    @discovery_statuses.setter
    def discovery_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetDiscoveryStatusArgs']]]]):
        pulumi.set(self, "discovery_statuses", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. User defined labels for the asset.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def lake(self) -> Optional[pulumi.Input[str]]:
        """
        The lake for the resource
        """
        return pulumi.get(self, "lake")

    @lake.setter
    def lake(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lake", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the asset.
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
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> Optional[pulumi.Input['AssetResourceSpecArgs']]:
        """
        Required. Immutable. Specification of the resource that is referenced by this asset.
        """
        return pulumi.get(self, "resource_spec")

    @resource_spec.setter
    def resource_spec(self, value: Optional[pulumi.Input['AssetResourceSpecArgs']]):
        pulumi.set(self, "resource_spec", value)

    @property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetResourceStatusArgs']]]]:
        """
        Output only. Status of the resource referenced by this asset.
        """
        return pulumi.get(self, "resource_statuses")

    @resource_statuses.setter
    def resource_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetResourceStatusArgs']]]]):
        pulumi.set(self, "resource_statuses", value)

    @property
    @pulumi.getter(name="securityStatuses")
    def security_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssetSecurityStatusArgs']]]]:
        """
        Output only. Status of the security policy applied to resource referenced by this asset.
        """
        return pulumi.get(self, "security_statuses")

    @security_statuses.setter
    def security_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssetSecurityStatusArgs']]]]):
        pulumi.set(self, "security_statuses", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Current state of the asset. Possible values: STATE_UNSPECIFIED, ACTIVE, CREATING, DELETING, ACTION_REQUIRED
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The time when the asset was last updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Asset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataplex_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input[pulumi.InputType['AssetDiscoverySpecArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lake: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['AssetResourceSpecArgs']]] = None,
                 __props__=None):
        """
        The Dataplex Asset resource

        ## Example Usage
        ### Basic_asset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic_bucket = gcp.storage.Bucket("basicBucket",
            location="us-west1",
            uniform_bucket_level_access=True,
            project="my-project-name")
        basic_lake = gcp.dataplex.Lake("basicLake",
            location="us-west1",
            project="my-project-name")
        basic_zone = gcp.dataplex.Zone("basicZone",
            location="us-west1",
            lake=basic_lake.name,
            type="RAW",
            discovery_spec=gcp.dataplex.ZoneDiscoverySpecArgs(
                enabled=False,
            ),
            resource_spec=gcp.dataplex.ZoneResourceSpecArgs(
                location_type="SINGLE_REGION",
            ),
            project="my-project-name")
        primary = gcp.dataplex.Asset("primary",
            location="us-west1",
            lake=basic_lake.name,
            dataplex_zone=basic_zone.name,
            discovery_spec=gcp.dataplex.AssetDiscoverySpecArgs(
                enabled=False,
            ),
            resource_spec=gcp.dataplex.AssetResourceSpecArgs(
                name="projects/my-project-name/buckets/bucket",
                type="STORAGE_BUCKET",
            ),
            project="my-project-name",
            opts=pulumi.ResourceOptions(depends_on=[basic_bucket]))
        ```

        ## Import

        Asset can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default projects/{{project}}/locations/{{location}}/lakes/{{lake}}/zones/{{dataplex_zone}}/assets/{{name}}
        ```

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default {{project}}/{{location}}/{{lake}}/{{dataplex_zone}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default {{location}}/{{lake}}/{{dataplex_zone}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataplex_zone: The zone for the resource
        :param pulumi.Input[str] description: Optional. Description of the asset.
        :param pulumi.Input[pulumi.InputType['AssetDiscoverySpecArgs']] discovery_spec: Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the asset.
        :param pulumi.Input[str] lake: The lake for the resource
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: The name of the asset.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[pulumi.InputType['AssetResourceSpecArgs']] resource_spec: Required. Immutable. Specification of the resource that is referenced by this asset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Dataplex Asset resource

        ## Example Usage
        ### Basic_asset
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic_bucket = gcp.storage.Bucket("basicBucket",
            location="us-west1",
            uniform_bucket_level_access=True,
            project="my-project-name")
        basic_lake = gcp.dataplex.Lake("basicLake",
            location="us-west1",
            project="my-project-name")
        basic_zone = gcp.dataplex.Zone("basicZone",
            location="us-west1",
            lake=basic_lake.name,
            type="RAW",
            discovery_spec=gcp.dataplex.ZoneDiscoverySpecArgs(
                enabled=False,
            ),
            resource_spec=gcp.dataplex.ZoneResourceSpecArgs(
                location_type="SINGLE_REGION",
            ),
            project="my-project-name")
        primary = gcp.dataplex.Asset("primary",
            location="us-west1",
            lake=basic_lake.name,
            dataplex_zone=basic_zone.name,
            discovery_spec=gcp.dataplex.AssetDiscoverySpecArgs(
                enabled=False,
            ),
            resource_spec=gcp.dataplex.AssetResourceSpecArgs(
                name="projects/my-project-name/buckets/bucket",
                type="STORAGE_BUCKET",
            ),
            project="my-project-name",
            opts=pulumi.ResourceOptions(depends_on=[basic_bucket]))
        ```

        ## Import

        Asset can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default projects/{{project}}/locations/{{location}}/lakes/{{lake}}/zones/{{dataplex_zone}}/assets/{{name}}
        ```

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default {{project}}/{{location}}/{{lake}}/{{dataplex_zone}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:dataplex/asset:Asset default {{location}}/{{lake}}/{{dataplex_zone}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param AssetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataplex_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 discovery_spec: Optional[pulumi.Input[pulumi.InputType['AssetDiscoverySpecArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 lake: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 resource_spec: Optional[pulumi.Input[pulumi.InputType['AssetResourceSpecArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssetArgs.__new__(AssetArgs)

            if dataplex_zone is None and not opts.urn:
                raise TypeError("Missing required property 'dataplex_zone'")
            __props__.__dict__["dataplex_zone"] = dataplex_zone
            __props__.__dict__["description"] = description
            if discovery_spec is None and not opts.urn:
                raise TypeError("Missing required property 'discovery_spec'")
            __props__.__dict__["discovery_spec"] = discovery_spec
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["labels"] = labels
            if lake is None and not opts.urn:
                raise TypeError("Missing required property 'lake'")
            __props__.__dict__["lake"] = lake
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if resource_spec is None and not opts.urn:
                raise TypeError("Missing required property 'resource_spec'")
            __props__.__dict__["resource_spec"] = resource_spec
            __props__.__dict__["create_time"] = None
            __props__.__dict__["discovery_statuses"] = None
            __props__.__dict__["resource_statuses"] = None
            __props__.__dict__["security_statuses"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["update_time"] = None
        super(Asset, __self__).__init__(
            'gcp:dataplex/asset:Asset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            dataplex_zone: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            discovery_spec: Optional[pulumi.Input[pulumi.InputType['AssetDiscoverySpecArgs']]] = None,
            discovery_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetDiscoveryStatusArgs']]]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            lake: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            resource_spec: Optional[pulumi.Input[pulumi.InputType['AssetResourceSpecArgs']]] = None,
            resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetResourceStatusArgs']]]]] = None,
            security_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetSecurityStatusArgs']]]]] = None,
            state: Optional[pulumi.Input[str]] = None,
            uid: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'Asset':
        """
        Get an existing Asset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: Output only. The time when the asset was created.
        :param pulumi.Input[str] dataplex_zone: The zone for the resource
        :param pulumi.Input[str] description: Optional. Description of the asset.
        :param pulumi.Input[pulumi.InputType['AssetDiscoverySpecArgs']] discovery_spec: Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetDiscoveryStatusArgs']]]] discovery_statuses: Output only. Status of the discovery feature applied to data referenced by this asset.
        :param pulumi.Input[str] display_name: Optional. User friendly display name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. User defined labels for the asset.
        :param pulumi.Input[str] lake: The lake for the resource
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: The name of the asset.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[pulumi.InputType['AssetResourceSpecArgs']] resource_spec: Required. Immutable. Specification of the resource that is referenced by this asset.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetResourceStatusArgs']]]] resource_statuses: Output only. Status of the resource referenced by this asset.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssetSecurityStatusArgs']]]] security_statuses: Output only. Status of the security policy applied to resource referenced by this asset.
        :param pulumi.Input[str] state: Output only. Current state of the asset. Possible values: STATE_UNSPECIFIED, ACTIVE, CREATING, DELETING, ACTION_REQUIRED
        :param pulumi.Input[str] uid: Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.
        :param pulumi.Input[str] update_time: Output only. The time when the asset was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AssetState.__new__(_AssetState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["dataplex_zone"] = dataplex_zone
        __props__.__dict__["description"] = description
        __props__.__dict__["discovery_spec"] = discovery_spec
        __props__.__dict__["discovery_statuses"] = discovery_statuses
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["labels"] = labels
        __props__.__dict__["lake"] = lake
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["resource_spec"] = resource_spec
        __props__.__dict__["resource_statuses"] = resource_statuses
        __props__.__dict__["security_statuses"] = security_statuses
        __props__.__dict__["state"] = state
        __props__.__dict__["uid"] = uid
        __props__.__dict__["update_time"] = update_time
        return Asset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. The time when the asset was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataplexZone")
    def dataplex_zone(self) -> pulumi.Output[str]:
        """
        The zone for the resource
        """
        return pulumi.get(self, "dataplex_zone")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. Description of the asset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discoverySpec")
    def discovery_spec(self) -> pulumi.Output['outputs.AssetDiscoverySpec']:
        """
        Required. Specification of the discovery feature applied to data referenced by this asset. When this spec is left unset, the asset will use the spec set on the parent zone.
        """
        return pulumi.get(self, "discovery_spec")

    @property
    @pulumi.getter(name="discoveryStatuses")
    def discovery_statuses(self) -> pulumi.Output[Sequence['outputs.AssetDiscoveryStatus']]:
        """
        Output only. Status of the discovery feature applied to data referenced by this asset.
        """
        return pulumi.get(self, "discovery_statuses")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. User friendly display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Optional. User defined labels for the asset.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def lake(self) -> pulumi.Output[str]:
        """
        The lake for the resource
        """
        return pulumi.get(self, "lake")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the asset.
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
    @pulumi.getter(name="resourceSpec")
    def resource_spec(self) -> pulumi.Output['outputs.AssetResourceSpec']:
        """
        Required. Immutable. Specification of the resource that is referenced by this asset.
        """
        return pulumi.get(self, "resource_spec")

    @property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> pulumi.Output[Sequence['outputs.AssetResourceStatus']]:
        """
        Output only. Status of the resource referenced by this asset.
        """
        return pulumi.get(self, "resource_statuses")

    @property
    @pulumi.getter(name="securityStatuses")
    def security_statuses(self) -> pulumi.Output[Sequence['outputs.AssetSecurityStatus']]:
        """
        Output only. Status of the security policy applied to resource referenced by this asset.
        """
        return pulumi.get(self, "security_statuses")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Output only. Current state of the asset. Possible values: STATE_UNSPECIFIED, ACTIVE, CREATING, DELETING, ACTION_REQUIRED
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Output only. The time when the asset was last updated.
        """
        return pulumi.get(self, "update_time")

