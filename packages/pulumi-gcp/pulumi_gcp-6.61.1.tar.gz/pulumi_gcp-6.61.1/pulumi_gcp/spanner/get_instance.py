# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, config=None, display_name=None, force_destroy=None, id=None, labels=None, name=None, num_nodes=None, processing_units=None, project=None, state=None):
        if config and not isinstance(config, str):
            raise TypeError("Expected argument 'config' to be a str")
        pulumi.set(__self__, "config", config)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if force_destroy and not isinstance(force_destroy, bool):
            raise TypeError("Expected argument 'force_destroy' to be a bool")
        pulumi.set(__self__, "force_destroy", force_destroy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if num_nodes and not isinstance(num_nodes, int):
            raise TypeError("Expected argument 'num_nodes' to be a int")
        pulumi.set(__self__, "num_nodes", num_nodes)
        if processing_units and not isinstance(processing_units, int):
            raise TypeError("Expected argument 'processing_units' to be a int")
        pulumi.set(__self__, "processing_units", processing_units)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def config(self) -> Optional[str]:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> bool:
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> int:
        return pulumi.get(self, "num_nodes")

    @property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> int:
        return pulumi.get(self, "processing_units")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            config=self.config,
            display_name=self.display_name,
            force_destroy=self.force_destroy,
            id=self.id,
            labels=self.labels,
            name=self.name,
            num_nodes=self.num_nodes,
            processing_units=self.processing_units,
            project=self.project,
            state=self.state)


def get_instance(config: Optional[str] = None,
                 display_name: Optional[str] = None,
                 name: Optional[str] = None,
                 project: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Get a spanner instance from Google Cloud by its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    foo = gcp.spanner.get_instance(name="bar")
    ```


    :param str name: The name of the spanner instance.
           
           - - -
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    """
    __args__ = dict()
    __args__['config'] = config
    __args__['displayName'] = display_name
    __args__['name'] = name
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:spanner/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        config=pulumi.get(__ret__, 'config'),
        display_name=pulumi.get(__ret__, 'display_name'),
        force_destroy=pulumi.get(__ret__, 'force_destroy'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        num_nodes=pulumi.get(__ret__, 'num_nodes'),
        processing_units=pulumi.get(__ret__, 'processing_units'),
        project=pulumi.get(__ret__, 'project'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_instance)
def get_instance_output(config: Optional[pulumi.Input[Optional[str]]] = None,
                        display_name: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Get a spanner instance from Google Cloud by its name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    foo = gcp.spanner.get_instance(name="bar")
    ```


    :param str name: The name of the spanner instance.
           
           - - -
    :param str project: The project in which the resource belongs. If it
           is not provided, the provider project is used.
    """
    ...
