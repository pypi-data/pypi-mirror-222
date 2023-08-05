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

__all__ = [
    'GetIAMPolicyResult',
    'AwaitableGetIAMPolicyResult',
    'get_iam_policy',
    'get_iam_policy_output',
]

@pulumi.output_type
class GetIAMPolicyResult:
    """
    A collection of values returned by getIAMPolicy.
    """
    def __init__(__self__, audit_configs=None, bindings=None, id=None, policy_data=None):
        if audit_configs and not isinstance(audit_configs, list):
            raise TypeError("Expected argument 'audit_configs' to be a list")
        pulumi.set(__self__, "audit_configs", audit_configs)
        if bindings and not isinstance(bindings, list):
            raise TypeError("Expected argument 'bindings' to be a list")
        pulumi.set(__self__, "bindings", bindings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_data and not isinstance(policy_data, str):
            raise TypeError("Expected argument 'policy_data' to be a str")
        pulumi.set(__self__, "policy_data", policy_data)

    @property
    @pulumi.getter(name="auditConfigs")
    def audit_configs(self) -> Optional[Sequence['outputs.GetIAMPolicyAuditConfigResult']]:
        return pulumi.get(self, "audit_configs")

    @property
    @pulumi.getter
    def bindings(self) -> Optional[Sequence['outputs.GetIAMPolicyBindingResult']]:
        return pulumi.get(self, "bindings")

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
        The above bindings serialized in a format suitable for
        referencing from a resource that supports IAM.
        """
        return pulumi.get(self, "policy_data")


class AwaitableGetIAMPolicyResult(GetIAMPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIAMPolicyResult(
            audit_configs=self.audit_configs,
            bindings=self.bindings,
            id=self.id,
            policy_data=self.policy_data)


def get_iam_policy(audit_configs: Optional[Sequence[pulumi.InputType['GetIAMPolicyAuditConfigArgs']]] = None,
                   bindings: Optional[Sequence[pulumi.InputType['GetIAMPolicyBindingArgs']]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIAMPolicyResult:
    """
    Generates an IAM policy document that may be referenced by and applied to
    other Google Cloud Platform IAM resources, such as the `projects.IAMPolicy` resource.

    **Note:** Please review the documentation of the resource that you will be using the datasource with. Some resources such as `projects.IAMPolicy` and others have limitations in their API methods which are noted on their respective page.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    admin = gcp.organizations.get_iam_policy(audit_configs=[gcp.organizations.GetIAMPolicyAuditConfigArgs(
            audit_log_configs=[
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    exempted_members=["user:you@domain.com"],
                    log_type="DATA_READ",
                ),
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    log_type="DATA_WRITE",
                ),
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    log_type="ADMIN_READ",
                ),
            ],
            service="cloudkms.googleapis.com",
        )],
        bindings=[
            gcp.organizations.GetIAMPolicyBindingArgs(
                members=["serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com"],
                role="roles/compute.instanceAdmin",
            ),
            gcp.organizations.GetIAMPolicyBindingArgs(
                members=["user:alice@gmail.com"],
                role="roles/storage.objectViewer",
            ),
        ])
    ```

    This data source is used to define IAM policies to apply to other resources.
    Currently, defining a policy through a datasource and referencing that policy
    from another resource is the only way to apply an IAM policy to a resource.


    :param Sequence[pulumi.InputType['GetIAMPolicyAuditConfigArgs']] audit_configs: A nested configuration block that defines logging additional configuration for your project. This field is only supported on `projects.IAMPolicy`, `folder.IAMPolicy` and `organizations.IAMPolicy`.
    :param Sequence[pulumi.InputType['GetIAMPolicyBindingArgs']] bindings: A nested configuration block (described below)
           defining a binding to be included in the policy document. Multiple
           `binding` arguments are supported.
           
           Each document configuration must have one or more `binding` blocks, which
           each accept the following arguments:
    """
    __args__ = dict()
    __args__['auditConfigs'] = audit_configs
    __args__['bindings'] = bindings
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:organizations/getIAMPolicy:getIAMPolicy', __args__, opts=opts, typ=GetIAMPolicyResult).value

    return AwaitableGetIAMPolicyResult(
        audit_configs=pulumi.get(__ret__, 'audit_configs'),
        bindings=pulumi.get(__ret__, 'bindings'),
        id=pulumi.get(__ret__, 'id'),
        policy_data=pulumi.get(__ret__, 'policy_data'))


@_utilities.lift_output_func(get_iam_policy)
def get_iam_policy_output(audit_configs: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIAMPolicyAuditConfigArgs']]]]] = None,
                          bindings: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIAMPolicyBindingArgs']]]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIAMPolicyResult]:
    """
    Generates an IAM policy document that may be referenced by and applied to
    other Google Cloud Platform IAM resources, such as the `projects.IAMPolicy` resource.

    **Note:** Please review the documentation of the resource that you will be using the datasource with. Some resources such as `projects.IAMPolicy` and others have limitations in their API methods which are noted on their respective page.

    ```python
    import pulumi
    import pulumi_gcp as gcp

    admin = gcp.organizations.get_iam_policy(audit_configs=[gcp.organizations.GetIAMPolicyAuditConfigArgs(
            audit_log_configs=[
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    exempted_members=["user:you@domain.com"],
                    log_type="DATA_READ",
                ),
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    log_type="DATA_WRITE",
                ),
                gcp.organizations.GetIAMPolicyAuditConfigAuditLogConfigArgs(
                    log_type="ADMIN_READ",
                ),
            ],
            service="cloudkms.googleapis.com",
        )],
        bindings=[
            gcp.organizations.GetIAMPolicyBindingArgs(
                members=["serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com"],
                role="roles/compute.instanceAdmin",
            ),
            gcp.organizations.GetIAMPolicyBindingArgs(
                members=["user:alice@gmail.com"],
                role="roles/storage.objectViewer",
            ),
        ])
    ```

    This data source is used to define IAM policies to apply to other resources.
    Currently, defining a policy through a datasource and referencing that policy
    from another resource is the only way to apply an IAM policy to a resource.


    :param Sequence[pulumi.InputType['GetIAMPolicyAuditConfigArgs']] audit_configs: A nested configuration block that defines logging additional configuration for your project. This field is only supported on `projects.IAMPolicy`, `folder.IAMPolicy` and `organizations.IAMPolicy`.
    :param Sequence[pulumi.InputType['GetIAMPolicyBindingArgs']] bindings: A nested configuration block (described below)
           defining a binding to be included in the policy document. Multiple
           `binding` arguments are supported.
           
           Each document configuration must have one or more `binding` blocks, which
           each accept the following arguments:
    """
    ...
