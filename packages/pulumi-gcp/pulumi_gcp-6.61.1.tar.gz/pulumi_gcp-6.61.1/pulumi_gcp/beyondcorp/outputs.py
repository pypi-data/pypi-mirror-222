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
    'AppConnectionApplicationEndpoint',
    'AppConnectionGateway',
    'AppConnectorPrincipalInfo',
    'AppConnectorPrincipalInfoServiceAccount',
    'AppGatewayAllocatedConnection',
    'GetAppConnectionApplicationEndpointResult',
    'GetAppConnectionGatewayResult',
    'GetAppConnectorPrincipalInfoResult',
    'GetAppConnectorPrincipalInfoServiceAccountResult',
    'GetAppGatewayAllocatedConnectionResult',
]

@pulumi.output_type
class AppConnectionApplicationEndpoint(dict):
    def __init__(__self__, *,
                 host: str,
                 port: int):
        """
        :param str host: Hostname or IP address of the remote application endpoint.
        :param int port: Port of the remote application endpoint.
               
               - - -
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        Hostname or IP address of the remote application endpoint.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Port of the remote application endpoint.

        - - -
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class AppConnectionGateway(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appGateway":
            suggest = "app_gateway"
        elif key == "ingressPort":
            suggest = "ingress_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppConnectionGateway. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppConnectionGateway.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppConnectionGateway.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_gateway: str,
                 ingress_port: Optional[int] = None,
                 type: Optional[str] = None,
                 uri: Optional[str] = None):
        """
        :param str app_gateway: AppGateway name in following format: projects/{project_id}/locations/{locationId}/appgateways/{gateway_id}.
        :param int ingress_port: (Output)
               Ingress port reserved on the gateways for this AppConnection, if not specified or zero, the default port is 19443.
        :param str type: The type of hosting used by the gateway. Refer to
               https://cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnections#Type_1
               for a list of possible values.
        :param str uri: (Output)
               Server-defined URI for this resource.
        """
        pulumi.set(__self__, "app_gateway", app_gateway)
        if ingress_port is not None:
            pulumi.set(__self__, "ingress_port", ingress_port)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="appGateway")
    def app_gateway(self) -> str:
        """
        AppGateway name in following format: projects/{project_id}/locations/{locationId}/appgateways/{gateway_id}.
        """
        return pulumi.get(self, "app_gateway")

    @property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[int]:
        """
        (Output)
        Ingress port reserved on the gateways for this AppConnection, if not specified or zero, the default port is 19443.
        """
        return pulumi.get(self, "ingress_port")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of hosting used by the gateway. Refer to
        https://cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnections#Type_1
        for a list of possible values.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        (Output)
        Server-defined URI for this resource.
        """
        return pulumi.get(self, "uri")


@pulumi.output_type
class AppConnectorPrincipalInfo(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceAccount":
            suggest = "service_account"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppConnectorPrincipalInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppConnectorPrincipalInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppConnectorPrincipalInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_account: 'outputs.AppConnectorPrincipalInfoServiceAccount'):
        """
        :param 'AppConnectorPrincipalInfoServiceAccountArgs' service_account: ServiceAccount represents a GCP service account.
               Structure is documented below.
        """
        pulumi.set(__self__, "service_account", service_account)

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> 'outputs.AppConnectorPrincipalInfoServiceAccount':
        """
        ServiceAccount represents a GCP service account.
        Structure is documented below.
        """
        return pulumi.get(self, "service_account")


@pulumi.output_type
class AppConnectorPrincipalInfoServiceAccount(dict):
    def __init__(__self__, *,
                 email: str):
        """
        :param str email: Email address of the service account.
               
               - - -
        """
        pulumi.set(__self__, "email", email)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email address of the service account.

        - - -
        """
        return pulumi.get(self, "email")


@pulumi.output_type
class AppGatewayAllocatedConnection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ingressPort":
            suggest = "ingress_port"
        elif key == "pscUri":
            suggest = "psc_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppGatewayAllocatedConnection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppGatewayAllocatedConnection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppGatewayAllocatedConnection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ingress_port: Optional[int] = None,
                 psc_uri: Optional[str] = None):
        """
        :param int ingress_port: The ingress port of an allocated connection.
        :param str psc_uri: The PSC uri of an allocated connection.
        """
        if ingress_port is not None:
            pulumi.set(__self__, "ingress_port", ingress_port)
        if psc_uri is not None:
            pulumi.set(__self__, "psc_uri", psc_uri)

    @property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[int]:
        """
        The ingress port of an allocated connection.
        """
        return pulumi.get(self, "ingress_port")

    @property
    @pulumi.getter(name="pscUri")
    def psc_uri(self) -> Optional[str]:
        """
        The PSC uri of an allocated connection.
        """
        return pulumi.get(self, "psc_uri")


@pulumi.output_type
class GetAppConnectionApplicationEndpointResult(dict):
    def __init__(__self__, *,
                 host: str,
                 port: int):
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def port(self) -> int:
        return pulumi.get(self, "port")


@pulumi.output_type
class GetAppConnectionGatewayResult(dict):
    def __init__(__self__, *,
                 app_gateway: str,
                 ingress_port: int,
                 type: str,
                 uri: str):
        pulumi.set(__self__, "app_gateway", app_gateway)
        pulumi.set(__self__, "ingress_port", ingress_port)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="appGateway")
    def app_gateway(self) -> str:
        return pulumi.get(self, "app_gateway")

    @property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> int:
        return pulumi.get(self, "ingress_port")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> str:
        return pulumi.get(self, "uri")


@pulumi.output_type
class GetAppConnectorPrincipalInfoResult(dict):
    def __init__(__self__, *,
                 service_accounts: Sequence['outputs.GetAppConnectorPrincipalInfoServiceAccountResult']):
        pulumi.set(__self__, "service_accounts", service_accounts)

    @property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(self) -> Sequence['outputs.GetAppConnectorPrincipalInfoServiceAccountResult']:
        return pulumi.get(self, "service_accounts")


@pulumi.output_type
class GetAppConnectorPrincipalInfoServiceAccountResult(dict):
    def __init__(__self__, *,
                 email: str):
        pulumi.set(__self__, "email", email)

    @property
    @pulumi.getter
    def email(self) -> str:
        return pulumi.get(self, "email")


@pulumi.output_type
class GetAppGatewayAllocatedConnectionResult(dict):
    def __init__(__self__, *,
                 ingress_port: int,
                 psc_uri: str):
        pulumi.set(__self__, "ingress_port", ingress_port)
        pulumi.set(__self__, "psc_uri", psc_uri)

    @property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> int:
        return pulumi.get(self, "ingress_port")

    @property
    @pulumi.getter(name="pscUri")
    def psc_uri(self) -> str:
        return pulumi.get(self, "psc_uri")


