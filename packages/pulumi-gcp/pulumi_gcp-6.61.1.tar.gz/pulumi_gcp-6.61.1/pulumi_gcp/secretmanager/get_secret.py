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
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, create_time=None, expire_time=None, id=None, labels=None, name=None, project=None, replications=None, rotations=None, secret_id=None, topics=None, ttl=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if expire_time and not isinstance(expire_time, str):
            raise TypeError("Expected argument 'expire_time' to be a str")
        pulumi.set(__self__, "expire_time", expire_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if replications and not isinstance(replications, list):
            raise TypeError("Expected argument 'replications' to be a list")
        pulumi.set(__self__, "replications", replications)
        if rotations and not isinstance(rotations, list):
            raise TypeError("Expected argument 'rotations' to be a list")
        pulumi.set(__self__, "rotations", rotations)
        if secret_id and not isinstance(secret_id, str):
            raise TypeError("Expected argument 'secret_id' to be a str")
        pulumi.set(__self__, "secret_id", secret_id)
        if topics and not isinstance(topics, list):
            raise TypeError("Expected argument 'topics' to be a list")
        pulumi.set(__self__, "topics", topics)
        if ttl and not isinstance(ttl, str):
            raise TypeError("Expected argument 'ttl' to be a str")
        pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        return pulumi.get(self, "expire_time")

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
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def replications(self) -> Sequence['outputs.GetSecretReplicationResult']:
        return pulumi.get(self, "replications")

    @property
    @pulumi.getter
    def rotations(self) -> Sequence['outputs.GetSecretRotationResult']:
        return pulumi.get(self, "rotations")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> str:
        return pulumi.get(self, "secret_id")

    @property
    @pulumi.getter
    def topics(self) -> Sequence['outputs.GetSecretTopicResult']:
        return pulumi.get(self, "topics")

    @property
    @pulumi.getter
    def ttl(self) -> str:
        return pulumi.get(self, "ttl")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            create_time=self.create_time,
            expire_time=self.expire_time,
            id=self.id,
            labels=self.labels,
            name=self.name,
            project=self.project,
            replications=self.replications,
            rotations=self.rotations,
            secret_id=self.secret_id,
            topics=self.topics,
            ttl=self.ttl)


def get_secret(project: Optional[str] = None,
               secret_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Use this data source to get information about a Secret Manager Secret

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.secretmanager.get_secret(secret_id="foobar")
    ```


    :param str project: The ID of the project in which the resource belongs.
    :param str secret_id: The name of the secret.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['secretId'] = secret_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:secretmanager/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        create_time=pulumi.get(__ret__, 'create_time'),
        expire_time=pulumi.get(__ret__, 'expire_time'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        project=pulumi.get(__ret__, 'project'),
        replications=pulumi.get(__ret__, 'replications'),
        rotations=pulumi.get(__ret__, 'rotations'),
        secret_id=pulumi.get(__ret__, 'secret_id'),
        topics=pulumi.get(__ret__, 'topics'),
        ttl=pulumi.get(__ret__, 'ttl'))


@_utilities.lift_output_func(get_secret)
def get_secret_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                      secret_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Use this data source to get information about a Secret Manager Secret

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.secretmanager.get_secret(secret_id="foobar")
    ```


    :param str project: The ID of the project in which the resource belongs.
    :param str secret_id: The name of the secret.
    """
    ...
