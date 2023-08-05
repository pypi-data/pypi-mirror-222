# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GameServerDeploymentArgs', 'GameServerDeployment']

@pulumi.input_type
class GameServerDeploymentArgs:
    def __init__(__self__, *,
                 deployment_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GameServerDeployment resource.
        :param pulumi.Input[str] deployment_id: A unique id for the deployment.
               
               
               - - -
        :param pulumi.Input[str] description: Human readable description of the game server deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this game server deployment. Each label is a
               key-value pair.
        :param pulumi.Input[str] location: Location of the Deployment.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "deployment_id", deployment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        A unique id for the deployment.


        - - -
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable description of the game server deployment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels associated with this game server deployment. Each label is a
        key-value pair.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the Deployment.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
class _GameServerDeploymentState:
    def __init__(__self__, *,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GameServerDeployment resources.
        :param pulumi.Input[str] deployment_id: A unique id for the deployment.
               
               
               - - -
        :param pulumi.Input[str] description: Human readable description of the game server deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this game server deployment. Each label is a
               key-value pair.
        :param pulumi.Input[str] location: Location of the Deployment.
        :param pulumi.Input[str] name: The resource id of the game server deployment, eg:
               `projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}`.
               For example,
               `projects/my-project/locations/{location}/gameServerDeployments/my-deployment`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique id for the deployment.


        - - -
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable description of the game server deployment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels associated with this game server deployment. Each label is a
        key-value pair.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the Deployment.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the game server deployment, eg:
        `projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}`.
        For example,
        `projects/my-project/locations/{location}/gameServerDeployments/my-deployment`.
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


class GameServerDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A game server deployment resource.

        To get more information about GameServerDeployment, see:

        * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/game-servers/docs)

        ## Example Usage
        ### Game Service Deployment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.gameservices.GameServerDeployment("default",
            deployment_id="tf-test-deployment",
            description="a deployment description")
        ```

        ## Import

        GameServerDeployment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default projects/{{project}}/locations/{{location}}/gameServerDeployments/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default {{project}}/{{location}}/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default {{location}}/{{deployment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: A unique id for the deployment.
               
               
               - - -
        :param pulumi.Input[str] description: Human readable description of the game server deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this game server deployment. Each label is a
               key-value pair.
        :param pulumi.Input[str] location: Location of the Deployment.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GameServerDeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A game server deployment resource.

        To get more information about GameServerDeployment, see:

        * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/game-servers/docs)

        ## Example Usage
        ### Game Service Deployment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.gameservices.GameServerDeployment("default",
            deployment_id="tf-test-deployment",
            description="a deployment description")
        ```

        ## Import

        GameServerDeployment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default projects/{{project}}/locations/{{location}}/gameServerDeployments/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default {{project}}/{{location}}/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeployment:GameServerDeployment default {{location}}/{{deployment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param GameServerDeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GameServerDeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GameServerDeploymentArgs.__new__(GameServerDeploymentArgs)

            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["name"] = None
        super(GameServerDeployment, __self__).__init__(
            'gcp:gameservices/gameServerDeployment:GameServerDeployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'GameServerDeployment':
        """
        Get an existing GameServerDeployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: A unique id for the deployment.
               
               
               - - -
        :param pulumi.Input[str] description: Human readable description of the game server deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels associated with this game server deployment. Each label is a
               key-value pair.
        :param pulumi.Input[str] location: Location of the Deployment.
        :param pulumi.Input[str] name: The resource id of the game server deployment, eg:
               `projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}`.
               For example,
               `projects/my-project/locations/{location}/gameServerDeployments/my-deployment`.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GameServerDeploymentState.__new__(_GameServerDeploymentState)

        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["description"] = description
        __props__.__dict__["labels"] = labels
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return GameServerDeployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        A unique id for the deployment.


        - - -
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human readable description of the game server deployment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The labels associated with this game server deployment. Each label is a
        key-value pair.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the Deployment.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource id of the game server deployment, eg:
        `projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}`.
        For example,
        `projects/my-project/locations/{location}/gameServerDeployments/my-deployment`.
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

