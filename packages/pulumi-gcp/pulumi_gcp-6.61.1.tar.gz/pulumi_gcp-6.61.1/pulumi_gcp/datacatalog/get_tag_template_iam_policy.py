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
    'GetTagTemplateIamPolicyResult',
    'AwaitableGetTagTemplateIamPolicyResult',
    'get_tag_template_iam_policy',
    'get_tag_template_iam_policy_output',
]

@pulumi.output_type
class GetTagTemplateIamPolicyResult:
    """
    A collection of values returned by getTagTemplateIamPolicy.
    """
    def __init__(__self__, etag=None, id=None, policy_data=None, project=None, region=None, tag_template=None):
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
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if tag_template and not isinstance(tag_template, str):
            raise TypeError("Expected argument 'tag_template' to be a str")
        pulumi.set(__self__, "tag_template", tag_template)

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
        (Required only by `datacatalog.TagTemplateIamPolicy`) The policy data generated by
        a `organizations_get_iam_policy` data source.
        """
        return pulumi.get(self, "policy_data")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tagTemplate")
    def tag_template(self) -> str:
        return pulumi.get(self, "tag_template")


class AwaitableGetTagTemplateIamPolicyResult(GetTagTemplateIamPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagTemplateIamPolicyResult(
            etag=self.etag,
            id=self.id,
            policy_data=self.policy_data,
            project=self.project,
            region=self.region,
            tag_template=self.tag_template)


def get_tag_template_iam_policy(project: Optional[str] = None,
                                region: Optional[str] = None,
                                tag_template: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagTemplateIamPolicyResult:
    """
    Retrieves the current IAM policy data for tagtemplate

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.datacatalog.get_tag_template_iam_policy(tag_template=google_data_catalog_tag_template["basic_tag_template"]["name"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str tag_template: Used to find the parent resource to bind the IAM policy to
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['region'] = region
    __args__['tagTemplate'] = tag_template
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:datacatalog/getTagTemplateIamPolicy:getTagTemplateIamPolicy', __args__, opts=opts, typ=GetTagTemplateIamPolicyResult).value

    return AwaitableGetTagTemplateIamPolicyResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'),
        project=pulumi.get(__ret__, 'project'),
        region=pulumi.get(__ret__, 'region'),
        tag_template=pulumi.get(__ret__, 'tag_template'))


@_utilities.lift_output_func(get_tag_template_iam_policy)
def get_tag_template_iam_policy_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                                       region: Optional[pulumi.Input[Optional[str]]] = None,
                                       tag_template: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagTemplateIamPolicyResult]:
    """
    Retrieves the current IAM policy data for tagtemplate

    ## example

    ```python
    import pulumi
    import pulumi_gcp as gcp

    policy = gcp.datacatalog.get_tag_template_iam_policy(tag_template=google_data_catalog_tag_template["basic_tag_template"]["name"])
    ```


    :param str project: The ID of the project in which the resource belongs.
           If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
    :param str tag_template: Used to find the parent resource to bind the IAM policy to
    """
    ...
