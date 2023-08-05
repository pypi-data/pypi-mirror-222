# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DefaultObjectACLArgs', 'DefaultObjectACL']

@pulumi.input_type
class DefaultObjectACLArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DefaultObjectACL resource.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`.
               See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Omitting the field is the same as providing an empty list.
        """
        pulumi.set(__self__, "bucket", bucket)
        if role_entities is not None:
            pulumi.set(__self__, "role_entities", role_entities)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket it applies to.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of role/entity pairs in the form `ROLE:entity`.
        See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Omitting the field is the same as providing an empty list.
        """
        return pulumi.get(self, "role_entities")

    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_entities", value)


@pulumi.input_type
class _DefaultObjectACLState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DefaultObjectACL resources.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`.
               See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Omitting the field is the same as providing an empty list.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if role_entities is not None:
            pulumi.set(__self__, "role_entities", role_entities)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket it applies to.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of role/entity pairs in the form `ROLE:entity`.
        See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Omitting the field is the same as providing an empty list.
        """
        return pulumi.get(self, "role_entities")

    @role_entities.setter
    def role_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_entities", value)


class DefaultObjectACL(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Authoritatively manages the default object ACLs for a Google Cloud Storage bucket
        without managing the bucket itself.

        > Note that for each object, its creator will have the `"OWNER"` role in addition
        to the default ACL that has been defined.

        For more information see
        [the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
        and
        [API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).

        > Want fine-grained control over default object ACLs? Use `storage.DefaultObjectAccessControl`
        to control individual role entity pairs.

        ## Example Usage

        Example creating a default object ACL on a bucket with one owner, and one reader.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        image_store = gcp.storage.Bucket("image-store", location="EU")
        image_store_default_acl = gcp.storage.DefaultObjectACL("image-store-default-acl",
            bucket=image_store.name,
            role_entities=[
                "OWNER:user-my.email@gmail.com",
                "READER:group-mygroup",
            ])
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`.
               See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Omitting the field is the same as providing an empty list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefaultObjectACLArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authoritatively manages the default object ACLs for a Google Cloud Storage bucket
        without managing the bucket itself.

        > Note that for each object, its creator will have the `"OWNER"` role in addition
        to the default ACL that has been defined.

        For more information see
        [the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
        and
        [API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).

        > Want fine-grained control over default object ACLs? Use `storage.DefaultObjectAccessControl`
        to control individual role entity pairs.

        ## Example Usage

        Example creating a default object ACL on a bucket with one owner, and one reader.

        ```python
        import pulumi
        import pulumi_gcp as gcp

        image_store = gcp.storage.Bucket("image-store", location="EU")
        image_store_default_acl = gcp.storage.DefaultObjectACL("image-store-default-acl",
            bucket=image_store.name,
            role_entities=[
                "OWNER:user-my.email@gmail.com",
                "READER:group-mygroup",
            ])
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param DefaultObjectACLArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefaultObjectACLArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefaultObjectACLArgs.__new__(DefaultObjectACLArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["role_entities"] = role_entities
        super(DefaultObjectACL, __self__).__init__(
            'gcp:storage/defaultObjectACL:DefaultObjectACL',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            role_entities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'DefaultObjectACL':
        """
        Get an existing DefaultObjectACL resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_entities: List of role/entity pairs in the form `ROLE:entity`.
               See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
               Omitting the field is the same as providing an empty list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefaultObjectACLState.__new__(_DefaultObjectACLState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["role_entities"] = role_entities
        return DefaultObjectACL(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket it applies to.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="roleEntities")
    def role_entities(self) -> pulumi.Output[Sequence[str]]:
        """
        List of role/entity pairs in the form `ROLE:entity`.
        See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        Omitting the field is the same as providing an empty list.
        """
        return pulumi.get(self, "role_entities")

