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

__all__ = [
    'GetResourcesSearchAllResult',
    'AwaitableGetResourcesSearchAllResult',
    'get_resources_search_all',
    'get_resources_search_all_output',
]

@pulumi.output_type
class GetResourcesSearchAllResult:
    """
    A collection of values returned by getResourcesSearchAll.
    """
    def __init__(__self__, asset_types=None, id=None, query=None, results=None, scope=None):
        if asset_types and not isinstance(asset_types, list):
            raise TypeError("Expected argument 'asset_types' to be a list")
        pulumi.set(__self__, "asset_types", asset_types)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if query and not isinstance(query, str):
            raise TypeError("Expected argument 'query' to be a str")
        pulumi.set(__self__, "query", query)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter(name="assetTypes")
    def asset_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "asset_types")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def query(self) -> Optional[str]:
        return pulumi.get(self, "query")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetResourcesSearchAllResultResult']:
        """
        A list of search results based on provided inputs. Structure is defined below.
        """
        return pulumi.get(self, "results")

    @property
    @pulumi.getter
    def scope(self) -> str:
        return pulumi.get(self, "scope")


class AwaitableGetResourcesSearchAllResult(GetResourcesSearchAllResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourcesSearchAllResult(
            asset_types=self.asset_types,
            id=self.id,
            query=self.query,
            results=self.results,
            scope=self.scope)


def get_resources_search_all(asset_types: Optional[Sequence[str]] = None,
                             query: Optional[str] = None,
                             scope: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourcesSearchAllResult:
    """
    ## Example Usage
    ### Searching For All Projects In An Org

    ```python
    import pulumi
    import pulumi_gcp as gcp

    projects = gcp.cloudasset.get_resources_search_all(scope="organizations/0123456789",
        asset_types=["cloudresourcemanager.googleapis.com/Project"])
    ```
    ### Searching For All Projects With CloudBuild API Enabled

    ```python
    import pulumi
    import pulumi_gcp as gcp

    cloud_build_projects = gcp.cloudasset.get_resources_search_all(scope="organizations/0123456789",
        asset_types=["serviceusage.googleapis.com/Service"],
        query="displayName:cloudbuild.googleapis.com AND state:ENABLED")
    ```
    ### Searching For All Service Accounts In A Project

    ```python
    import pulumi
    import pulumi_gcp as gcp

    project_service_accounts = gcp.cloudasset.get_resources_search_all(scope="projects/my-project-id",
        asset_types=["iam.googleapis.com/ServiceAccount"])
    ```


    :param Sequence[str] asset_types: A list of asset types that this request searches for. If empty, it will search all the [supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types).
    :param str query: The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope` and `asset_types`.
    :param str scope: A scope can be a project, a folder, or an organization. The allowed value must be: organization number (such as "organizations/123"), folder number (such as "folders/1234"), project number (such as "projects/12345") or project id (such as "projects/abc")
    """
    __args__ = dict()
    __args__['assetTypes'] = asset_types
    __args__['query'] = query
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:cloudasset/getResourcesSearchAll:getResourcesSearchAll', __args__, opts=opts, typ=GetResourcesSearchAllResult).value

    return AwaitableGetResourcesSearchAllResult(
        asset_types=pulumi.get(__ret__, 'asset_types'),
        id=pulumi.get(__ret__, 'id'),
        query=pulumi.get(__ret__, 'query'),
        results=pulumi.get(__ret__, 'results'),
        scope=pulumi.get(__ret__, 'scope'))


@_utilities.lift_output_func(get_resources_search_all)
def get_resources_search_all_output(asset_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                    query: Optional[pulumi.Input[Optional[str]]] = None,
                                    scope: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourcesSearchAllResult]:
    """
    ## Example Usage
    ### Searching For All Projects In An Org

    ```python
    import pulumi
    import pulumi_gcp as gcp

    projects = gcp.cloudasset.get_resources_search_all(scope="organizations/0123456789",
        asset_types=["cloudresourcemanager.googleapis.com/Project"])
    ```
    ### Searching For All Projects With CloudBuild API Enabled

    ```python
    import pulumi
    import pulumi_gcp as gcp

    cloud_build_projects = gcp.cloudasset.get_resources_search_all(scope="organizations/0123456789",
        asset_types=["serviceusage.googleapis.com/Service"],
        query="displayName:cloudbuild.googleapis.com AND state:ENABLED")
    ```
    ### Searching For All Service Accounts In A Project

    ```python
    import pulumi
    import pulumi_gcp as gcp

    project_service_accounts = gcp.cloudasset.get_resources_search_all(scope="projects/my-project-id",
        asset_types=["iam.googleapis.com/ServiceAccount"])
    ```


    :param Sequence[str] asset_types: A list of asset types that this request searches for. If empty, it will search all the [supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types).
    :param str query: The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope` and `asset_types`.
    :param str scope: A scope can be a project, a folder, or an organization. The allowed value must be: organization number (such as "organizations/123"), folder number (such as "folders/1234"), project number (such as "projects/12345") or project id (such as "projects/abc")
    """
    ...
