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
    'GetDatabaseInstanceResult',
    'AwaitableGetDatabaseInstanceResult',
    'get_database_instance',
    'get_database_instance_output',
]

@pulumi.output_type
class GetDatabaseInstanceResult:
    """
    A collection of values returned by getDatabaseInstance.
    """
    def __init__(__self__, available_maintenance_versions=None, clones=None, connection_name=None, database_version=None, deletion_protection=None, encryption_key_name=None, first_ip_address=None, id=None, instance_type=None, ip_addresses=None, maintenance_version=None, master_instance_name=None, name=None, private_ip_address=None, project=None, public_ip_address=None, region=None, replica_configurations=None, restore_backup_contexts=None, root_password=None, self_link=None, server_ca_certs=None, service_account_email_address=None, settings=None):
        if available_maintenance_versions and not isinstance(available_maintenance_versions, list):
            raise TypeError("Expected argument 'available_maintenance_versions' to be a list")
        pulumi.set(__self__, "available_maintenance_versions", available_maintenance_versions)
        if clones and not isinstance(clones, list):
            raise TypeError("Expected argument 'clones' to be a list")
        pulumi.set(__self__, "clones", clones)
        if connection_name and not isinstance(connection_name, str):
            raise TypeError("Expected argument 'connection_name' to be a str")
        pulumi.set(__self__, "connection_name", connection_name)
        if database_version and not isinstance(database_version, str):
            raise TypeError("Expected argument 'database_version' to be a str")
        pulumi.set(__self__, "database_version", database_version)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if encryption_key_name and not isinstance(encryption_key_name, str):
            raise TypeError("Expected argument 'encryption_key_name' to be a str")
        pulumi.set(__self__, "encryption_key_name", encryption_key_name)
        if first_ip_address and not isinstance(first_ip_address, str):
            raise TypeError("Expected argument 'first_ip_address' to be a str")
        pulumi.set(__self__, "first_ip_address", first_ip_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if ip_addresses and not isinstance(ip_addresses, list):
            raise TypeError("Expected argument 'ip_addresses' to be a list")
        pulumi.set(__self__, "ip_addresses", ip_addresses)
        if maintenance_version and not isinstance(maintenance_version, str):
            raise TypeError("Expected argument 'maintenance_version' to be a str")
        pulumi.set(__self__, "maintenance_version", maintenance_version)
        if master_instance_name and not isinstance(master_instance_name, str):
            raise TypeError("Expected argument 'master_instance_name' to be a str")
        pulumi.set(__self__, "master_instance_name", master_instance_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_ip_address and not isinstance(private_ip_address, str):
            raise TypeError("Expected argument 'private_ip_address' to be a str")
        pulumi.set(__self__, "private_ip_address", private_ip_address)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if public_ip_address and not isinstance(public_ip_address, str):
            raise TypeError("Expected argument 'public_ip_address' to be a str")
        pulumi.set(__self__, "public_ip_address", public_ip_address)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if replica_configurations and not isinstance(replica_configurations, list):
            raise TypeError("Expected argument 'replica_configurations' to be a list")
        pulumi.set(__self__, "replica_configurations", replica_configurations)
        if restore_backup_contexts and not isinstance(restore_backup_contexts, list):
            raise TypeError("Expected argument 'restore_backup_contexts' to be a list")
        pulumi.set(__self__, "restore_backup_contexts", restore_backup_contexts)
        if root_password and not isinstance(root_password, str):
            raise TypeError("Expected argument 'root_password' to be a str")
        pulumi.set(__self__, "root_password", root_password)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if server_ca_certs and not isinstance(server_ca_certs, list):
            raise TypeError("Expected argument 'server_ca_certs' to be a list")
        pulumi.set(__self__, "server_ca_certs", server_ca_certs)
        if service_account_email_address and not isinstance(service_account_email_address, str):
            raise TypeError("Expected argument 'service_account_email_address' to be a str")
        pulumi.set(__self__, "service_account_email_address", service_account_email_address)
        if settings and not isinstance(settings, list):
            raise TypeError("Expected argument 'settings' to be a list")
        pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> Sequence[str]:
        return pulumi.get(self, "available_maintenance_versions")

    @property
    @pulumi.getter
    def clones(self) -> Sequence['outputs.GetDatabaseInstanceCloneResult']:
        return pulumi.get(self, "clones")

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> str:
        return pulumi.get(self, "connection_name")

    @property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> str:
        return pulumi.get(self, "database_version")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> bool:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> str:
        return pulumi.get(self, "encryption_key_name")

    @property
    @pulumi.getter(name="firstIpAddress")
    def first_ip_address(self) -> str:
        return pulumi.get(self, "first_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence['outputs.GetDatabaseInstanceIpAddressResult']:
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> str:
        return pulumi.get(self, "maintenance_version")

    @property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> str:
        return pulumi.get(self, "master_instance_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> str:
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter
    def project(self) -> Optional[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> str:
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="replicaConfigurations")
    def replica_configurations(self) -> Sequence['outputs.GetDatabaseInstanceReplicaConfigurationResult']:
        return pulumi.get(self, "replica_configurations")

    @property
    @pulumi.getter(name="restoreBackupContexts")
    def restore_backup_contexts(self) -> Sequence['outputs.GetDatabaseInstanceRestoreBackupContextResult']:
        return pulumi.get(self, "restore_backup_contexts")

    @property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> str:
        return pulumi.get(self, "root_password")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> Sequence['outputs.GetDatabaseInstanceServerCaCertResult']:
        return pulumi.get(self, "server_ca_certs")

    @property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> str:
        return pulumi.get(self, "service_account_email_address")

    @property
    @pulumi.getter
    def settings(self) -> Sequence['outputs.GetDatabaseInstanceSettingResult']:
        return pulumi.get(self, "settings")


class AwaitableGetDatabaseInstanceResult(GetDatabaseInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseInstanceResult(
            available_maintenance_versions=self.available_maintenance_versions,
            clones=self.clones,
            connection_name=self.connection_name,
            database_version=self.database_version,
            deletion_protection=self.deletion_protection,
            encryption_key_name=self.encryption_key_name,
            first_ip_address=self.first_ip_address,
            id=self.id,
            instance_type=self.instance_type,
            ip_addresses=self.ip_addresses,
            maintenance_version=self.maintenance_version,
            master_instance_name=self.master_instance_name,
            name=self.name,
            private_ip_address=self.private_ip_address,
            project=self.project,
            public_ip_address=self.public_ip_address,
            region=self.region,
            replica_configurations=self.replica_configurations,
            restore_backup_contexts=self.restore_backup_contexts,
            root_password=self.root_password,
            self_link=self.self_link,
            server_ca_certs=self.server_ca_certs,
            service_account_email_address=self.service_account_email_address,
            settings=self.settings)


def get_database_instance(name: Optional[str] = None,
                          project: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseInstanceResult:
    """
    Use this data source to get information about a Cloud SQL instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.sql.get_database_instance(name="test-sql-instance")
    ```


    :param str name: The name of the instance.
    :param str project: The ID of the project in which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['project'] = project
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:sql/getDatabaseInstance:getDatabaseInstance', __args__, opts=opts, typ=GetDatabaseInstanceResult).value

    return AwaitableGetDatabaseInstanceResult(
        available_maintenance_versions=pulumi.get(__ret__, 'available_maintenance_versions'),
        clones=pulumi.get(__ret__, 'clones'),
        connection_name=pulumi.get(__ret__, 'connection_name'),
        database_version=pulumi.get(__ret__, 'database_version'),
        deletion_protection=pulumi.get(__ret__, 'deletion_protection'),
        encryption_key_name=pulumi.get(__ret__, 'encryption_key_name'),
        first_ip_address=pulumi.get(__ret__, 'first_ip_address'),
        id=pulumi.get(__ret__, 'id'),
        instance_type=pulumi.get(__ret__, 'instance_type'),
        ip_addresses=pulumi.get(__ret__, 'ip_addresses'),
        maintenance_version=pulumi.get(__ret__, 'maintenance_version'),
        master_instance_name=pulumi.get(__ret__, 'master_instance_name'),
        name=pulumi.get(__ret__, 'name'),
        private_ip_address=pulumi.get(__ret__, 'private_ip_address'),
        project=pulumi.get(__ret__, 'project'),
        public_ip_address=pulumi.get(__ret__, 'public_ip_address'),
        region=pulumi.get(__ret__, 'region'),
        replica_configurations=pulumi.get(__ret__, 'replica_configurations'),
        restore_backup_contexts=pulumi.get(__ret__, 'restore_backup_contexts'),
        root_password=pulumi.get(__ret__, 'root_password'),
        self_link=pulumi.get(__ret__, 'self_link'),
        server_ca_certs=pulumi.get(__ret__, 'server_ca_certs'),
        service_account_email_address=pulumi.get(__ret__, 'service_account_email_address'),
        settings=pulumi.get(__ret__, 'settings'))


@_utilities.lift_output_func(get_database_instance)
def get_database_instance_output(name: Optional[pulumi.Input[str]] = None,
                                 project: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseInstanceResult]:
    """
    Use this data source to get information about a Cloud SQL instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    qa = gcp.sql.get_database_instance(name="test-sql-instance")
    ```


    :param str name: The name of the instance.
    :param str project: The ID of the project in which the resource belongs.
    """
    ...
