# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HostingSiteArgs', 'HostingSite']

@pulumi.input_type
class HostingSiteArgs:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HostingSite resource.
        :param pulumi.Input[str] app_id: Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
               associated with the Hosting site.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_id: Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
               used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
               domain name label.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
        associated with the Hosting site.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

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

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
        used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
        domain name label.
        """
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_id", value)


@pulumi.input_type
class _HostingSiteState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 default_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HostingSite resources.
        :param pulumi.Input[str] app_id: Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
               associated with the Hosting site.
        :param pulumi.Input[str] default_url: The default URL for the site in the form of https://{name}.web.app
        :param pulumi.Input[str] name: Output only. The fully-qualified resource name of the Hosting site, in the
               format: projects/PROJECT_IDENTIFIER/sites/SITE_ID PROJECT_IDENTIFIER: the
               Firebase project's
               [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its
               [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id).
               Learn more about using project identifiers in Google's
               [AIP 2510 standard](https://google.aip.dev/cloud/2510).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_id: Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
               used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
               domain name label.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if default_url is not None:
            pulumi.set(__self__, "default_url", default_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
        associated with the Hosting site.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="defaultUrl")
    def default_url(self) -> Optional[pulumi.Input[str]]:
        """
        The default URL for the site in the form of https://{name}.web.app
        """
        return pulumi.get(self, "default_url")

    @default_url.setter
    def default_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Output only. The fully-qualified resource name of the Hosting site, in the
        format: projects/PROJECT_IDENTIFIER/sites/SITE_ID PROJECT_IDENTIFIER: the
        Firebase project's
        [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its
        [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id).
        Learn more about using project identifiers in Google's
        [AIP 2510 standard](https://google.aip.dev/cloud/2510).
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

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
        used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
        domain name label.
        """
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_id", value)


class HostingSite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### Firebasehosting Site Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.firebase.HostingSite("default",
            project="my-project-name",
            site_id="site-no-app",
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Firebasehosting Site Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Test web app for Firebase Hosting",
            deletion_policy="DELETE",
            opts=pulumi.ResourceOptions(provider=google_beta))
        full = gcp.firebase.HostingSite("full",
            project="my-project-name",
            site_id="site-with-app",
            app_id=default.app_id,
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Site can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default projects/{{project}}/sites/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default {{project}}/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default sites/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default {{site_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
               associated with the Hosting site.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_id: Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
               used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
               domain name label.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[HostingSiteArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### Firebasehosting Site Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.firebase.HostingSite("default",
            project="my-project-name",
            site_id="site-no-app",
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```
        ### Firebasehosting Site Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        default = gcp.firebase.WebApp("default",
            project="my-project-name",
            display_name="Test web app for Firebase Hosting",
            deletion_policy="DELETE",
            opts=pulumi.ResourceOptions(provider=google_beta))
        full = gcp.firebase.HostingSite("full",
            project="my-project-name",
            site_id="site-with-app",
            app_id=default.app_id,
            opts=pulumi.ResourceOptions(provider=google_beta))
        ```

        ## Import

        Site can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default projects/{{project}}/sites/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default {{project}}/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default sites/{{site_id}}
        ```

        ```sh
         $ pulumi import gcp:firebase/hostingSite:HostingSite default {{site_id}}
        ```

        :param str resource_name: The name of the resource.
        :param HostingSiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HostingSiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HostingSiteArgs.__new__(HostingSiteArgs)

            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["project"] = project
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["default_url"] = None
            __props__.__dict__["name"] = None
        super(HostingSite, __self__).__init__(
            'gcp:firebase/hostingSite:HostingSite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            default_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            site_id: Optional[pulumi.Input[str]] = None) -> 'HostingSite':
        """
        Get an existing HostingSite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
               associated with the Hosting site.
        :param pulumi.Input[str] default_url: The default URL for the site in the form of https://{name}.web.app
        :param pulumi.Input[str] name: Output only. The fully-qualified resource name of the Hosting site, in the
               format: projects/PROJECT_IDENTIFIER/sites/SITE_ID PROJECT_IDENTIFIER: the
               Firebase project's
               [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its
               [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id).
               Learn more about using project identifiers in Google's
               [AIP 2510 standard](https://google.aip.dev/cloud/2510).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] site_id: Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
               used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
               domain name label.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HostingSiteState.__new__(_HostingSiteState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["default_url"] = default_url
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["site_id"] = site_id
        return HostingSite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id)
        associated with the Hosting site.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="defaultUrl")
    def default_url(self) -> pulumi.Output[str]:
        """
        The default URL for the site in the form of https://{name}.web.app
        """
        return pulumi.get(self, "default_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Output only. The fully-qualified resource name of the Hosting site, in the
        format: projects/PROJECT_IDENTIFIER/sites/SITE_ID PROJECT_IDENTIFIER: the
        Firebase project's
        [`ProjectNumber`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its
        [`ProjectId`](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id).
        Learn more about using project identifiers in Google's
        [AIP 2510 standard](https://google.aip.dev/cloud/2510).
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

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[str]]:
        """
        Required. Immutable. A globally unique identifier for the Hosting site. This identifier is
        used to construct the Firebase-provisioned subdomains for the site, so it must also be a valid
        domain name label.
        """
        return pulumi.get(self, "site_id")

