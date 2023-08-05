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
    'GetTableIamPolicyResult',
    'AwaitableGetTableIamPolicyResult',
    'get_table_iam_policy',
    'get_table_iam_policy_output',
]

@pulumi.output_type
class GetTableIamPolicyResult:
    """
    A collection of values returned by getTableIamPolicy.
    """
    def __init__(__self__, dataset_id=None, etag=None, id=None, policy_data=None, project=None, table_id=None):
        if dataset_id and not isinstance(dataset_id, str):
            raise TypeError("Expected argument 'dataset_id' to be a str")
        pulumi.set(__self__, "dataset_id", dataset_id)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if table_id and not isinstance(table_id, str):
            raise TypeError("Expected argument 'table_id' to be a str")
        pulumi.set(__self__, "table_id", table_id)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> str:
        return pulumi.get(self, "dataset_id")

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
    @pulumi.getter(name="policyData")
    def policy_data(self) -> str:
        """
        (Required only by `bigquery.IamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="tableId")
    def table_id(self) -> str:
        return pulumi.get(self, "table_id")


class AwaitableGetTableIamPolicyResult(GetTableIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableIamPolicyResult(
            dataset_id=self.dataset_id,
            etag=self.etag,
            id=self.id,
            policy_data=self.policy_data,
            project=self.project,
            table_id=self.table_id)


def get_table_iam_policy(dataset_id: Optional[str] = None,
                         project: Optional[str] = None,
                         table_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableIamPolicyResult:
    """
    Retrieves the current IAM policy data for table

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.bigquery.get_table_iam_policy(project=google_bigquery_table["test"]["project"],
        dataset_id=google_bigquery_table["test"]["dataset_id"],
        table_id=google_bigquery_table["test"]["table_id"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    __args__ = dict()
    __args__['datasetId'] = dataset_id
    __args__['project'] = project
    __args__['tableId'] = table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:bigquery/getTableIamPolicy:getTableIamPolicy', __args__, opts=opts, typ=GetTableIamPolicyResult).value

    return AwaitableGetTableIamPolicyResult(
        dataset_id=pulumi.get(__ret__, 'dataset_id'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'),
        table_id=pulumi.get(__ret__, 'table_id'))


@_utilities.lift_output_func(get_table_iam_policy)
def get_table_iam_policy_output(dataset_id: Optional[pulumi.Input[str]] = None,
                                project: Optional[pulumi.Input[Optional[str]]] = None,
                                table_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableIamPolicyResult]:
    """
    Retrieves the current IAM policy data for table

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.bigquery.get_table_iam_policy(project=google_bigquery_table["test"]["project"],
        dataset_id=google_bigquery_table["test"]["dataset_id"],
        table_id=google_bigquery_table["test"]["table_id"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    """
    ...
