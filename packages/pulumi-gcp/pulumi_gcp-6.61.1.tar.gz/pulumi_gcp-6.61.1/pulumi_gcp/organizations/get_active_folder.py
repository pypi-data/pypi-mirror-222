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
    'GetActiveFolderResult',
    'AwaitableGetActiveFolderResult',
    'get_active_folder',
    'get_active_folder_output',
]

@pulumi.output_type
class GetActiveFolderResult:
    """
    A collection of values returned by getActiveFolder.
    """
    def __init__(__self__, display_name=None, id=None, name=None, parent=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the Folder. This uniquely identifies the folder.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        return pulumi.get(self, "parent")


class AwaitableGetActiveFolderResult(GetActiveFolderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActiveFolderResult(
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            parent=self.parent)


def get_active_folder(display_name: Optional[str] = None,
                      parent: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActiveFolderResult:
    """
    Get an active folder within GCP by `display_name` and `parent`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    department1 = gcp.organizations.get_active_folder(display_name="Department 1",
        parent="organizations/1234567")
    ```


    :param str display_name: The folder's display name.
    :param str parent: The resource name of the parent Folder or Organization.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['parent'] = parent
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:organizations/getActiveFolder:getActiveFolder', __args__, opts=opts, typ=GetActiveFolderResult).value

    return AwaitableGetActiveFolderResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        parent=pulumi.get(__ret__, 'parent'))


@_utilities.lift_output_func(get_active_folder)
def get_active_folder_output(display_name: Optional[pulumi.Input[str]] = None,
                             parent: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActiveFolderResult]:
    """
    Get an active folder within GCP by `display_name` and `parent`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    department1 = gcp.organizations.get_active_folder(display_name="Department 1",
        parent="organizations/1234567")
    ```


    :param str display_name: The folder's display name.
    :param str parent: The resource name of the parent Folder or Organization.
    """
    ...
