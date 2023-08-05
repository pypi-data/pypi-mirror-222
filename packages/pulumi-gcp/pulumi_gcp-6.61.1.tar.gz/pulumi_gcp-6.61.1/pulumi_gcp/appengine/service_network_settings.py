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

__all__ = ['ServiceNetworkSettingsArgs', 'ServiceNetworkSettings']

@pulumi.input_type
class ServiceNetworkSettingsArgs:
    def __init__(__self__, *,
                 network_settings: pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs'],
                 service: pulumi.Input[str],
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServiceNetworkSettings resource.
        :param pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs'] network_settings: Ingress settings for this service. Will apply to all versions.
               Structure is documented below.
        :param pulumi.Input[str] service: The name of the service these settings apply to.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "network_settings", network_settings)
        pulumi.set(__self__, "service", service)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs']:
        """
        Ingress settings for this service. Will apply to all versions.
        Structure is documented below.
        """
        return pulumi.get(self, "network_settings")

    @network_settings.setter
    def network_settings(self, value: pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs']):
        pulumi.set(self, "network_settings", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        The name of the service these settings apply to.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

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
class _ServiceNetworkSettingsState:
    def __init__(__self__, *,
                 network_settings: Optional[pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServiceNetworkSettings resources.
        :param pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs'] network_settings: Ingress settings for this service. Will apply to all versions.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The name of the service these settings apply to.
        """
        if network_settings is not None:
            pulumi.set(__self__, "network_settings", network_settings)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service is not None:
            pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> Optional[pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs']]:
        """
        Ingress settings for this service. Will apply to all versions.
        Structure is documented below.
        """
        return pulumi.get(self, "network_settings")

    @network_settings.setter
    def network_settings(self, value: Optional[pulumi.Input['ServiceNetworkSettingsNetworkSettingsArgs']]):
        pulumi.set(self, "network_settings", value)

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
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service these settings apply to.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)


class ServiceNetworkSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_settings: Optional[pulumi.Input[pulumi.InputType['ServiceNetworkSettingsNetworkSettingsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A NetworkSettings resource is a container for ingress settings for a version or service.

        To get more information about ServiceNetworkSettings, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services)

        ## Example Usage
        ### App Engine Service Network Settings

        ```python
        import pulumi
        import pulumi_gcp as gcp

        bucket = gcp.storage.Bucket("bucket", location="US")
        object = gcp.storage.BucketObject("object",
            bucket=bucket.name,
            source=pulumi.FileAsset("./test-fixtures/appengine/hello-world.zip"))
        internalapp_standard_app_version = gcp.appengine.StandardAppVersion("internalappStandardAppVersion",
            version_id="v1",
            service="internalapp",
            delete_service_on_destroy=True,
            runtime="nodejs10",
            entrypoint=gcp.appengine.StandardAppVersionEntrypointArgs(
                shell="node ./app.js",
            ),
            deployment=gcp.appengine.StandardAppVersionDeploymentArgs(
                zip=gcp.appengine.StandardAppVersionDeploymentZipArgs(
                    source_url=pulumi.Output.all(bucket.name, object.name).apply(lambda bucketName, objectName: f"https://storage.googleapis.com/{bucket_name}/{object_name}"),
                ),
            ),
            env_variables={
                "port": "8080",
            })
        internalapp_service_network_settings = gcp.appengine.ServiceNetworkSettings("internalappServiceNetworkSettings",
            service=internalapp_standard_app_version.service,
            network_settings=gcp.appengine.ServiceNetworkSettingsNetworkSettingsArgs(
                ingress_traffic_allowed="INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
            ))
        ```

        ## Import

        ServiceNetworkSettings can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default apps/{{project}}/services/{{service}}
        ```

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default {{project}}/{{service}}
        ```

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default {{service}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServiceNetworkSettingsNetworkSettingsArgs']] network_settings: Ingress settings for this service. Will apply to all versions.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The name of the service these settings apply to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceNetworkSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A NetworkSettings resource is a container for ingress settings for a version or service.

        To get more information about ServiceNetworkSettings, see:

        * [API documentation](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services)

        ## Example Usage
        ### App Engine Service Network Settings

        ```python
        import pulumi
        import pulumi_gcp as gcp

        bucket = gcp.storage.Bucket("bucket", location="US")
        object = gcp.storage.BucketObject("object",
            bucket=bucket.name,
            source=pulumi.FileAsset("./test-fixtures/appengine/hello-world.zip"))
        internalapp_standard_app_version = gcp.appengine.StandardAppVersion("internalappStandardAppVersion",
            version_id="v1",
            service="internalapp",
            delete_service_on_destroy=True,
            runtime="nodejs10",
            entrypoint=gcp.appengine.StandardAppVersionEntrypointArgs(
                shell="node ./app.js",
            ),
            deployment=gcp.appengine.StandardAppVersionDeploymentArgs(
                zip=gcp.appengine.StandardAppVersionDeploymentZipArgs(
                    source_url=pulumi.Output.all(bucket.name, object.name).apply(lambda bucketName, objectName: f"https://storage.googleapis.com/{bucket_name}/{object_name}"),
                ),
            ),
            env_variables={
                "port": "8080",
            })
        internalapp_service_network_settings = gcp.appengine.ServiceNetworkSettings("internalappServiceNetworkSettings",
            service=internalapp_standard_app_version.service,
            network_settings=gcp.appengine.ServiceNetworkSettingsNetworkSettingsArgs(
                ingress_traffic_allowed="INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY",
            ))
        ```

        ## Import

        ServiceNetworkSettings can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default apps/{{project}}/services/{{service}}
        ```

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default {{project}}/{{service}}
        ```

        ```sh
         $ pulumi import gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings default {{service}}
        ```

        :param str resource_name: The name of the resource.
        :param ServiceNetworkSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceNetworkSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_settings: Optional[pulumi.Input[pulumi.InputType['ServiceNetworkSettingsNetworkSettingsArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceNetworkSettingsArgs.__new__(ServiceNetworkSettingsArgs)

            if network_settings is None and not opts.urn:
                raise TypeError("Missing required property 'network_settings'")
            __props__.__dict__["network_settings"] = network_settings
            __props__.__dict__["project"] = project
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
        super(ServiceNetworkSettings, __self__).__init__(
            'gcp:appengine/serviceNetworkSettings:ServiceNetworkSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_settings: Optional[pulumi.Input[pulumi.InputType['ServiceNetworkSettingsNetworkSettingsArgs']]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'ServiceNetworkSettings':
        """
        Get an existing ServiceNetworkSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServiceNetworkSettingsNetworkSettingsArgs']] network_settings: Ingress settings for this service. Will apply to all versions.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The name of the service these settings apply to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceNetworkSettingsState.__new__(_ServiceNetworkSettingsState)

        __props__.__dict__["network_settings"] = network_settings
        __props__.__dict__["project"] = project
        __props__.__dict__["service"] = service
        return ServiceNetworkSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkSettings")
    def network_settings(self) -> pulumi.Output['outputs.ServiceNetworkSettingsNetworkSettings']:
        """
        Ingress settings for this service. Will apply to all versions.
        Structure is documented below.
        """
        return pulumi.get(self, "network_settings")

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
    def service(self) -> pulumi.Output[str]:
        """
        The name of the service these settings apply to.
        """
        return pulumi.get(self, "service")

