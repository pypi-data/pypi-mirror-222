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
    'GetMetastoreServiceIamPolicyResult',
    'AwaitableGetMetastoreServiceIamPolicyResult',
    'get_metastore_service_iam_policy',
    'get_metastore_service_iam_policy_output',
]

@pulumi.output_type
class GetMetastoreServiceIamPolicyResult:
    """
    A collection of values returned by getMetastoreServiceIamPolicy.
    """
    def __init__(__self__, etag=None, id=None, location=None, policy_data=None, project=None, service_id=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if service_id and not isinstance(service_id, str):
            raise TypeError("Expected argument 'service_id' to be a str")
        pulumi.set(__self__, "service_id", service_id)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        (Computed) The etag of the IAM policy.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `dataproc.MetastoreServiceIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        return pulumi.get(self, "service_id")


class AwaitableGetMetastoreServiceIamPolicyResult(GetMetastoreServiceIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetastoreServiceIamPolicyResult(
            etag=self.etag,
            id=self.id,
            location=self.location,
            policy_data=self.policy_data,
            project=self.project,
            service_id=self.service_id)


def get_metastore_service_iam_policy(location: Optional[str] = None,
                                     project: Optional[str] = None,
                                     service_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetastoreServiceIamPolicyResult:
    """
    Retrieves the current IAM policy data for service

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.dataproc.get_metastore_service_iam_policy(project=google_dataproc_metastore_service["default"]["project"],
        location=google_dataproc_metastore_service["default"]["location"],
        service_id=google_dataproc_metastore_service["default"]["service_id"])
    ```


    :param str location: The location where the metastore service should reside.
           The default value is `global`.
           Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['serviceId'] = service_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:dataproc/getMetastoreServiceIamPolicy:getMetastoreServiceIamPolicy', __args__, opts=opts, typ=GetMetastoreServiceIamPolicyResult).value

    return AwaitableGetMetastoreServiceIamPolicyResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'),
        service_id=pulumi.get(__ret__, 'service_id'))


@_utilities.lift_output_func(get_metastore_service_iam_policy)
def get_metastore_service_iam_policy_output(location: Optional[pulumi.Input[Optional[str]]] = None,
                                            project: Optional[pulumi.Input[Optional[str]]] = None,
                                            service_id: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetastoreServiceIamPolicyResult]:
    """
    Retrieves the current IAM policy data for service

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.dataproc.get_metastore_service_iam_policy(project=google_dataproc_metastore_service["default"]["project"],
        location=google_dataproc_metastore_service["default"]["location"],
        service_id=google_dataproc_metastore_service["default"]["service_id"])
    ```


    :param str location: The location where the metastore service should reside.
           The default value is `global`.
           Used to find the parent resource to bind the IAM policy to
    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    ...
