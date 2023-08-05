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

__all__ = ['KeystoresAliasesKeyCertFileArgs', 'KeystoresAliasesKeyCertFile']

@pulumi.input_type
class KeystoresAliasesKeyCertFileArgs:
    def __init__(__self__, *,
                 alias: pulumi.Input[str],
                 cert: pulumi.Input[str],
                 environment: pulumi.Input[str],
                 keystore: pulumi.Input[str],
                 org_id: pulumi.Input[str],
                 certs_info: Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KeystoresAliasesKeyCertFile resource.
        :param pulumi.Input[str] alias: Alias Name
        :param pulumi.Input[str] cert: Cert content
               
               
               - - -
        :param pulumi.Input[str] environment: Environment associated with the alias
        :param pulumi.Input[str] keystore: Keystore Name
        :param pulumi.Input[str] org_id: Organization ID associated with the alias, without organization/ prefix
        :param pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs'] certs_info: Chain of certificates under this alias.
               Structure is documented below.
        :param pulumi.Input[str] key: Private Key content, omit if uploading to truststore
        :param pulumi.Input[str] password: Password for the Private Key if it's encrypted
        """
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "environment", environment)
        pulumi.set(__self__, "keystore", keystore)
        pulumi.set(__self__, "org_id", org_id)
        if certs_info is not None:
            pulumi.set(__self__, "certs_info", certs_info)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Input[str]:
        """
        Alias Name
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Input[str]:
        """
        Cert content


        - - -
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: pulumi.Input[str]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input[str]:
        """
        Environment associated with the alias
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def keystore(self) -> pulumi.Input[str]:
        """
        Keystore Name
        """
        return pulumi.get(self, "keystore")

    @keystore.setter
    def keystore(self, value: pulumi.Input[str]):
        pulumi.set(self, "keystore", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        Organization ID associated with the alias, without organization/ prefix
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="certsInfo")
    def certs_info(self) -> Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']]:
        """
        Chain of certificates under this alias.
        Structure is documented below.
        """
        return pulumi.get(self, "certs_info")

    @certs_info.setter
    def certs_info(self, value: Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']]):
        pulumi.set(self, "certs_info", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Private Key content, omit if uploading to truststore
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for the Private Key if it's encrypted
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class _KeystoresAliasesKeyCertFileState:
    def __init__(__self__, *,
                 alias: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 certs_info: Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 keystore: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KeystoresAliasesKeyCertFile resources.
        :param pulumi.Input[str] alias: Alias Name
        :param pulumi.Input[str] cert: Cert content
               
               
               - - -
        :param pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs'] certs_info: Chain of certificates under this alias.
               Structure is documented below.
        :param pulumi.Input[str] environment: Environment associated with the alias
        :param pulumi.Input[str] key: Private Key content, omit if uploading to truststore
        :param pulumi.Input[str] keystore: Keystore Name
        :param pulumi.Input[str] org_id: Organization ID associated with the alias, without organization/ prefix
        :param pulumi.Input[str] password: Password for the Private Key if it's encrypted
        :param pulumi.Input[str] type: Optional.Type of Alias
        """
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if certs_info is not None:
            pulumi.set(__self__, "certs_info", certs_info)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if keystore is not None:
            pulumi.set(__self__, "keystore", keystore)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        Alias Name
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        """
        Cert content


        - - -
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter(name="certsInfo")
    def certs_info(self) -> Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']]:
        """
        Chain of certificates under this alias.
        Structure is documented below.
        """
        return pulumi.get(self, "certs_info")

    @certs_info.setter
    def certs_info(self, value: Optional[pulumi.Input['KeystoresAliasesKeyCertFileCertsInfoArgs']]):
        pulumi.set(self, "certs_info", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        Environment associated with the alias
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Private Key content, omit if uploading to truststore
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def keystore(self) -> Optional[pulumi.Input[str]]:
        """
        Keystore Name
        """
        return pulumi.get(self, "keystore")

    @keystore.setter
    def keystore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "keystore", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization ID associated with the alias, without organization/ prefix
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for the Private Key if it's encrypted
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Optional.Type of Alias
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class KeystoresAliasesKeyCertFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 certs_info: Optional[pulumi.Input[pulumi.InputType['KeystoresAliasesKeyCertFileCertsInfoArgs']]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 keystore: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An alias from a key/certificate pair.

        To get more information about KeystoresAliasesKeyCertFile, see:

        * [API documentation](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)
        * How-to Guides
            * [Keystores Aliases](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)

        ## Import

        KeystoresAliasesKeyCertFile can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:apigee/keystoresAliasesKeyCertFile:KeystoresAliasesKeyCertFile default organizations/{{org_id}}/environments/{{environment}}/keystores/{{keystore}}/aliases/{{alias}}
        ```

        ```sh
         $ pulumi import gcp:apigee/keystoresAliasesKeyCertFile:KeystoresAliasesKeyCertFile default {{org_id}}/{{environment}}/{{keystore}}/{{alias}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: Alias Name
        :param pulumi.Input[str] cert: Cert content
               
               
               - - -
        :param pulumi.Input[pulumi.InputType['KeystoresAliasesKeyCertFileCertsInfoArgs']] certs_info: Chain of certificates under this alias.
               Structure is documented below.
        :param pulumi.Input[str] environment: Environment associated with the alias
        :param pulumi.Input[str] key: Private Key content, omit if uploading to truststore
        :param pulumi.Input[str] keystore: Keystore Name
        :param pulumi.Input[str] org_id: Organization ID associated with the alias, without organization/ prefix
        :param pulumi.Input[str] password: Password for the Private Key if it's encrypted
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeystoresAliasesKeyCertFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An alias from a key/certificate pair.

        To get more information about KeystoresAliasesKeyCertFile, see:

        * [API documentation](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)
        * How-to Guides
            * [Keystores Aliases](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases)

        ## Import

        KeystoresAliasesKeyCertFile can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:apigee/keystoresAliasesKeyCertFile:KeystoresAliasesKeyCertFile default organizations/{{org_id}}/environments/{{environment}}/keystores/{{keystore}}/aliases/{{alias}}
        ```

        ```sh
         $ pulumi import gcp:apigee/keystoresAliasesKeyCertFile:KeystoresAliasesKeyCertFile default {{org_id}}/{{environment}}/{{keystore}}/{{alias}}
        ```

        :param str resource_name: The name of the resource.
        :param KeystoresAliasesKeyCertFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeystoresAliasesKeyCertFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 certs_info: Optional[pulumi.Input[pulumi.InputType['KeystoresAliasesKeyCertFileCertsInfoArgs']]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 keystore: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeystoresAliasesKeyCertFileArgs.__new__(KeystoresAliasesKeyCertFileArgs)

            if alias is None and not opts.urn:
                raise TypeError("Missing required property 'alias'")
            __props__.__dict__["alias"] = alias
            if cert is None and not opts.urn:
                raise TypeError("Missing required property 'cert'")
            __props__.__dict__["cert"] = cert
            __props__.__dict__["certs_info"] = certs_info
            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            __props__.__dict__["key"] = None if key is None else pulumi.Output.secret(key)
            if keystore is None and not opts.urn:
                raise TypeError("Missing required property 'keystore'")
            __props__.__dict__["keystore"] = keystore
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["type"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["key", "password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(KeystoresAliasesKeyCertFile, __self__).__init__(
            'gcp:apigee/keystoresAliasesKeyCertFile:KeystoresAliasesKeyCertFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            cert: Optional[pulumi.Input[str]] = None,
            certs_info: Optional[pulumi.Input[pulumi.InputType['KeystoresAliasesKeyCertFileCertsInfoArgs']]] = None,
            environment: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            keystore: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'KeystoresAliasesKeyCertFile':
        """
        Get an existing KeystoresAliasesKeyCertFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: Alias Name
        :param pulumi.Input[str] cert: Cert content
               
               
               - - -
        :param pulumi.Input[pulumi.InputType['KeystoresAliasesKeyCertFileCertsInfoArgs']] certs_info: Chain of certificates under this alias.
               Structure is documented below.
        :param pulumi.Input[str] environment: Environment associated with the alias
        :param pulumi.Input[str] key: Private Key content, omit if uploading to truststore
        :param pulumi.Input[str] keystore: Keystore Name
        :param pulumi.Input[str] org_id: Organization ID associated with the alias, without organization/ prefix
        :param pulumi.Input[str] password: Password for the Private Key if it's encrypted
        :param pulumi.Input[str] type: Optional.Type of Alias
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeystoresAliasesKeyCertFileState.__new__(_KeystoresAliasesKeyCertFileState)

        __props__.__dict__["alias"] = alias
        __props__.__dict__["cert"] = cert
        __props__.__dict__["certs_info"] = certs_info
        __props__.__dict__["environment"] = environment
        __props__.__dict__["key"] = key
        __props__.__dict__["keystore"] = keystore
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["password"] = password
        __props__.__dict__["type"] = type
        return KeystoresAliasesKeyCertFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        Alias Name
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Output[str]:
        """
        Cert content


        - - -
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter(name="certsInfo")
    def certs_info(self) -> pulumi.Output['outputs.KeystoresAliasesKeyCertFileCertsInfo']:
        """
        Chain of certificates under this alias.
        Structure is documented below.
        """
        return pulumi.get(self, "certs_info")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        Environment associated with the alias
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        Private Key content, omit if uploading to truststore
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def keystore(self) -> pulumi.Output[str]:
        """
        Keystore Name
        """
        return pulumi.get(self, "keystore")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        Organization ID associated with the alias, without organization/ prefix
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Password for the Private Key if it's encrypted
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Optional.Type of Alias
        """
        return pulumi.get(self, "type")

