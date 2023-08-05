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

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 github_config: Optional[pulumi.Input['ConnectionGithubConfigArgs']] = None,
                 github_enterprise_config: Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']] = None,
                 gitlab_config: Optional[pulumi.Input['ConnectionGitlabConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[bool] disabled: If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        :param pulumi.Input['ConnectionGithubConfigArgs'] github_config: Configuration for connections to github.com.
        :param pulumi.Input['ConnectionGithubEnterpriseConfigArgs'] github_enterprise_config: Configuration for connections to an instance of GitHub Enterprise.
        :param pulumi.Input['ConnectionGitlabConfigArgs'] gitlab_config: Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        :param pulumi.Input[str] name: Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        :param pulumi.Input[str] project: The project for the resource
        """
        pulumi.set(__self__, "location", location)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if github_config is not None:
            pulumi.set(__self__, "github_config", github_config)
        if github_enterprise_config is not None:
            pulumi.set(__self__, "github_enterprise_config", github_enterprise_config)
        if gitlab_config is not None:
            pulumi.set(__self__, "gitlab_config", gitlab_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="githubConfig")
    def github_config(self) -> Optional[pulumi.Input['ConnectionGithubConfigArgs']]:
        """
        Configuration for connections to github.com.
        """
        return pulumi.get(self, "github_config")

    @github_config.setter
    def github_config(self, value: Optional[pulumi.Input['ConnectionGithubConfigArgs']]):
        pulumi.set(self, "github_config", value)

    @property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']]:
        """
        Configuration for connections to an instance of GitHub Enterprise.
        """
        return pulumi.get(self, "github_enterprise_config")

    @github_enterprise_config.setter
    def github_enterprise_config(self, value: Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']]):
        pulumi.set(self, "github_enterprise_config", value)

    @property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(self) -> Optional[pulumi.Input['ConnectionGitlabConfigArgs']]:
        """
        Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        """
        return pulumi.get(self, "gitlab_config")

    @gitlab_config.setter
    def gitlab_config(self, value: Optional[pulumi.Input['ConnectionGitlabConfigArgs']]):
        pulumi.set(self, "gitlab_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 github_config: Optional[pulumi.Input['ConnectionGithubConfigArgs']] = None,
                 github_enterprise_config: Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']] = None,
                 gitlab_config: Optional[pulumi.Input['ConnectionGitlabConfigArgs']] = None,
                 installation_states: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionInstallationStateArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reconciling: Optional[pulumi.Input[bool]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] create_time: Output only. Server assigned timestamp for when the connection was created.
        :param pulumi.Input[bool] disabled: If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input['ConnectionGithubConfigArgs'] github_config: Configuration for connections to github.com.
        :param pulumi.Input['ConnectionGithubEnterpriseConfigArgs'] github_enterprise_config: Configuration for connections to an instance of GitHub Enterprise.
        :param pulumi.Input['ConnectionGitlabConfigArgs'] gitlab_config: Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        :param pulumi.Input[Sequence[pulumi.Input['ConnectionInstallationStateArgs']]] installation_states: Output only. Installation state of the Connection.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[bool] reconciling: Output only. Set to true when the connection is being set up or updated in the background.
        :param pulumi.Input[str] update_time: Output only. Server assigned timestamp for when the connection was updated.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if github_config is not None:
            pulumi.set(__self__, "github_config", github_config)
        if github_enterprise_config is not None:
            pulumi.set(__self__, "github_enterprise_config", github_enterprise_config)
        if gitlab_config is not None:
            pulumi.set(__self__, "gitlab_config", gitlab_config)
        if installation_states is not None:
            pulumi.set(__self__, "installation_states", installation_states)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if reconciling is not None:
            pulumi.set(__self__, "reconciling", reconciling)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Server assigned timestamp for when the connection was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="githubConfig")
    def github_config(self) -> Optional[pulumi.Input['ConnectionGithubConfigArgs']]:
        """
        Configuration for connections to github.com.
        """
        return pulumi.get(self, "github_config")

    @github_config.setter
    def github_config(self, value: Optional[pulumi.Input['ConnectionGithubConfigArgs']]):
        pulumi.set(self, "github_config", value)

    @property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']]:
        """
        Configuration for connections to an instance of GitHub Enterprise.
        """
        return pulumi.get(self, "github_enterprise_config")

    @github_enterprise_config.setter
    def github_enterprise_config(self, value: Optional[pulumi.Input['ConnectionGithubEnterpriseConfigArgs']]):
        pulumi.set(self, "github_enterprise_config", value)

    @property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(self) -> Optional[pulumi.Input['ConnectionGitlabConfigArgs']]:
        """
        Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        """
        return pulumi.get(self, "gitlab_config")

    @gitlab_config.setter
    def gitlab_config(self, value: Optional[pulumi.Input['ConnectionGitlabConfigArgs']]):
        pulumi.set(self, "gitlab_config", value)

    @property
    @pulumi.getter(name="installationStates")
    def installation_states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionInstallationStateArgs']]]]:
        """
        Output only. Installation state of the Connection.
        """
        return pulumi.get(self, "installation_states")

    @installation_states.setter
    def installation_states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConnectionInstallationStateArgs']]]]):
        pulumi.set(self, "installation_states", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[bool]]:
        """
        Output only. Set to true when the connection is being set up or updated in the background.
        """
        return pulumi.get(self, "reconciling")

    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reconciling", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. Server assigned timestamp for when the connection was updated.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 github_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubConfigArgs']]] = None,
                 github_enterprise_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubEnterpriseConfigArgs']]] = None,
                 gitlab_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGitlabConfigArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Cloudbuildv2 Connection resource

        ## Example Usage
        ### Ghe
        ```python
        import pulumi
        import pulumi_gcp as gcp

        private_key_secret = gcp.secretmanager.Secret("private-key-secret",
            secret_id="ghe-pk-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        private_key_secret_version = gcp.secretmanager.SecretVersion("private-key-secret-version",
            secret=private_key_secret.id,
            secret_data=(lambda path: open(path).read())("private-key.pem"))
        webhook_secret_secret = gcp.secretmanager.Secret("webhook-secret-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        webhook_secret_secret_version = gcp.secretmanager.SecretVersion("webhook-secret-secret-version",
            secret=webhook_secret_secret.id,
            secret_data="<webhook-secret-data>")
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy_pk = gcp.secretmanager.SecretIamPolicy("policy-pk",
            secret_id=private_key_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        policy_whs = gcp.secretmanager.SecretIamPolicy("policy-whs",
            secret_id=webhook_secret_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-central1",
            github_enterprise_config=gcp.cloudbuildv2.ConnectionGithubEnterpriseConfigArgs(
                host_uri="https://ghe.com",
                private_key_secret_version=private_key_secret_version.id,
                webhook_secret_secret_version=webhook_secret_secret_version.id,
                app_id=200,
                app_slug="gcb-app",
                app_installation_id=300,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    policy_pk,
                    policy_whs,
                ]))
        ```
        ### GitHub Connection
        Creates a Connection to github.com
        ```python
        import pulumi
        import pulumi_gcp as gcp

        github_token_secret = gcp.secretmanager.Secret("github-token-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        github_token_secret_version = gcp.secretmanager.SecretVersion("github-token-secret-version",
            secret=github_token_secret.id,
            secret_data=(lambda path: open(path).read())("my-github-token.txt"))
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy = gcp.secretmanager.SecretIamPolicy("policy",
            secret_id=github_token_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-west1",
            github_config=gcp.cloudbuildv2.ConnectionGithubConfigArgs(
                app_installation_id=123123,
                authorizer_credential=gcp.cloudbuildv2.ConnectionGithubConfigAuthorizerCredentialArgs(
                    oauth_token_secret_version=github_token_secret_version.id,
                ),
            ))
        ```

        ## Import

        Connection can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default projects/{{project}}/locations/{{location}}/connections/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[bool] disabled: If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        :param pulumi.Input[pulumi.InputType['ConnectionGithubConfigArgs']] github_config: Configuration for connections to github.com.
        :param pulumi.Input[pulumi.InputType['ConnectionGithubEnterpriseConfigArgs']] github_enterprise_config: Configuration for connections to an instance of GitHub Enterprise.
        :param pulumi.Input[pulumi.InputType['ConnectionGitlabConfigArgs']] gitlab_config: Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        :param pulumi.Input[str] project: The project for the resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Cloudbuildv2 Connection resource

        ## Example Usage
        ### Ghe
        ```python
        import pulumi
        import pulumi_gcp as gcp

        private_key_secret = gcp.secretmanager.Secret("private-key-secret",
            secret_id="ghe-pk-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        private_key_secret_version = gcp.secretmanager.SecretVersion("private-key-secret-version",
            secret=private_key_secret.id,
            secret_data=(lambda path: open(path).read())("private-key.pem"))
        webhook_secret_secret = gcp.secretmanager.Secret("webhook-secret-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        webhook_secret_secret_version = gcp.secretmanager.SecretVersion("webhook-secret-secret-version",
            secret=webhook_secret_secret.id,
            secret_data="<webhook-secret-data>")
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy_pk = gcp.secretmanager.SecretIamPolicy("policy-pk",
            secret_id=private_key_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        policy_whs = gcp.secretmanager.SecretIamPolicy("policy-whs",
            secret_id=webhook_secret_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-central1",
            github_enterprise_config=gcp.cloudbuildv2.ConnectionGithubEnterpriseConfigArgs(
                host_uri="https://ghe.com",
                private_key_secret_version=private_key_secret_version.id,
                webhook_secret_secret_version=webhook_secret_secret_version.id,
                app_id=200,
                app_slug="gcb-app",
                app_installation_id=300,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    policy_pk,
                    policy_whs,
                ]))
        ```
        ### GitHub Connection
        Creates a Connection to github.com
        ```python
        import pulumi
        import pulumi_gcp as gcp

        github_token_secret = gcp.secretmanager.Secret("github-token-secret",
            secret_id="github-token-secret",
            replication=gcp.secretmanager.SecretReplicationArgs(
                automatic=True,
            ))
        github_token_secret_version = gcp.secretmanager.SecretVersion("github-token-secret-version",
            secret=github_token_secret.id,
            secret_data=(lambda path: open(path).read())("my-github-token.txt"))
        p4sa_secret_accessor = gcp.organizations.get_iam_policy(bindings=[gcp.organizations.GetIAMPolicyBindingArgs(
            role="roles/secretmanager.secretAccessor",
            members=["serviceAccount:service-123456789@gcp-sa-cloudbuild.iam.gserviceaccount.com"],
        )])
        policy = gcp.secretmanager.SecretIamPolicy("policy",
            secret_id=github_token_secret.secret_id,
            policy_data=p4sa_secret_accessor.policy_data)
        my_connection = gcp.cloudbuildv2.Connection("my-connection",
            location="us-west1",
            github_config=gcp.cloudbuildv2.ConnectionGithubConfigArgs(
                app_installation_id=123123,
                authorizer_credential=gcp.cloudbuildv2.ConnectionGithubConfigAuthorizerCredentialArgs(
                    oauth_token_secret_version=github_token_secret_version.id,
                ),
            ))
        ```

        ## Import

        Connection can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default projects/{{project}}/locations/{{location}}/connections/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:cloudbuildv2/connection:Connection default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 github_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubConfigArgs']]] = None,
                 github_enterprise_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubEnterpriseConfigArgs']]] = None,
                 gitlab_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGitlabConfigArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["github_config"] = github_config
            __props__.__dict__["github_enterprise_config"] = github_enterprise_config
            __props__.__dict__["gitlab_config"] = gitlab_config
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["create_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["installation_states"] = None
            __props__.__dict__["reconciling"] = None
            __props__.__dict__["update_time"] = None
        super(Connection, __self__).__init__(
            'gcp:cloudbuildv2/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            github_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubConfigArgs']]] = None,
            github_enterprise_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGithubEnterpriseConfigArgs']]] = None,
            gitlab_config: Optional[pulumi.Input[pulumi.InputType['ConnectionGitlabConfigArgs']]] = None,
            installation_states: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionInstallationStateArgs']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            reconciling: Optional[pulumi.Input[bool]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Allows clients to store small amounts of arbitrary data.
        :param pulumi.Input[str] create_time: Output only. Server assigned timestamp for when the connection was created.
        :param pulumi.Input[bool] disabled: If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        :param pulumi.Input[str] etag: This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        :param pulumi.Input[pulumi.InputType['ConnectionGithubConfigArgs']] github_config: Configuration for connections to github.com.
        :param pulumi.Input[pulumi.InputType['ConnectionGithubEnterpriseConfigArgs']] github_enterprise_config: Configuration for connections to an instance of GitHub Enterprise.
        :param pulumi.Input[pulumi.InputType['ConnectionGitlabConfigArgs']] gitlab_config: Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ConnectionInstallationStateArgs']]]] installation_states: Output only. Installation state of the Connection.
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[bool] reconciling: Output only. Set to true when the connection is being set up or updated in the background.
        :param pulumi.Input[str] update_time: Output only. Server assigned timestamp for when the connection was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["etag"] = etag
        __props__.__dict__["github_config"] = github_config
        __props__.__dict__["github_enterprise_config"] = github_enterprise_config
        __props__.__dict__["gitlab_config"] = gitlab_config
        __props__.__dict__["installation_states"] = installation_states
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["reconciling"] = reconciling
        __props__.__dict__["update_time"] = update_time
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Allows clients to store small amounts of arbitrary data.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Output only. Server assigned timestamp for when the connection was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="githubConfig")
    def github_config(self) -> pulumi.Output[Optional['outputs.ConnectionGithubConfig']]:
        """
        Configuration for connections to github.com.
        """
        return pulumi.get(self, "github_config")

    @property
    @pulumi.getter(name="githubEnterpriseConfig")
    def github_enterprise_config(self) -> pulumi.Output[Optional['outputs.ConnectionGithubEnterpriseConfig']]:
        """
        Configuration for connections to an instance of GitHub Enterprise.
        """
        return pulumi.get(self, "github_enterprise_config")

    @property
    @pulumi.getter(name="gitlabConfig")
    def gitlab_config(self) -> pulumi.Output[Optional['outputs.ConnectionGitlabConfig']]:
        """
        Configuration for connections to gitlab.com or an instance of GitLab Enterprise.
        """
        return pulumi.get(self, "gitlab_config")

    @property
    @pulumi.getter(name="installationStates")
    def installation_states(self) -> pulumi.Output[Sequence['outputs.ConnectionInstallationState']]:
        """
        Output only. Installation state of the Connection.
        """
        return pulumi.get(self, "installation_states")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location for the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[bool]:
        """
        Output only. Set to true when the connection is being set up or updated in the background.
        """
        return pulumi.get(self, "reconciling")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Output only. Server assigned timestamp for when the connection was updated.
        """
        return pulumi.get(self, "update_time")

