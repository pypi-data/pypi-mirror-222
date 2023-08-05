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
    'GCPolicyMaxAgeArgs',
    'GCPolicyMaxVersionArgs',
    'InstanceClusterArgs',
    'InstanceClusterAutoscalingConfigArgs',
    'InstanceIamBindingConditionArgs',
    'InstanceIamMemberConditionArgs',
    'TableColumnFamilyArgs',
    'TableIamBindingConditionArgs',
    'TableIamMemberConditionArgs',
]

@pulumi.input_type
class GCPolicyMaxAgeArgs:
    def __init__(__self__, *,
                 days: Optional[pulumi.Input[int]] = None,
                 duration: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] days: Number of days before applying GC policy.
        :param pulumi.Input[str] duration: Duration before applying GC policy (ex. "8h"). This is required when `days` isn't set
               
               -----
        """
        if days is not None:
            warnings.warn("""Deprecated in favor of duration""", DeprecationWarning)
            pulumi.log.warn("""days is deprecated: Deprecated in favor of duration""")
        if days is not None:
            pulumi.set(__self__, "days", days)
        if duration is not None:
            pulumi.set(__self__, "duration", duration)

    @property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[int]]:
        """
        Number of days before applying GC policy.
        """
        warnings.warn("""Deprecated in favor of duration""", DeprecationWarning)
        pulumi.log.warn("""days is deprecated: Deprecated in favor of duration""")

        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[str]]:
        """
        Duration before applying GC policy (ex. "8h"). This is required when `days` isn't set

        -----
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration", value)


@pulumi.input_type
class GCPolicyMaxVersionArgs:
    def __init__(__self__, *,
                 number: pulumi.Input[int]):
        """
        :param pulumi.Input[int] number: Number of version before applying the GC policy.
               
               -----
               `gc_rules` include 2 fields:
        """
        pulumi.set(__self__, "number", number)

    @property
    @pulumi.getter
    def number(self) -> pulumi.Input[int]:
        """
        Number of version before applying the GC policy.

        -----
        `gc_rules` include 2 fields:
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: pulumi.Input[int]):
        pulumi.set(self, "number", value)


@pulumi.input_type
class InstanceClusterArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 autoscaling_config: Optional[pulumi.Input['InstanceClusterAutoscalingConfigArgs']] = None,
                 kms_key_name: Optional[pulumi.Input[str]] = None,
                 num_nodes: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cluster_id: The ID of the Cloud Bigtable cluster. Must be 6-30 characters and must only contain hyphens, lowercase letters and numbers.
        :param pulumi.Input['InstanceClusterAutoscalingConfigArgs'] autoscaling_config: [Autoscaling](https://cloud.google.com/bigtable/docs/autoscaling#parameters) config for the cluster, contains the following arguments:
        :param pulumi.Input[str] kms_key_name: Describes the Cloud KMS encryption key that will be used to protect the destination Bigtable cluster. The requirements for this key are: 1) The Cloud Bigtable service account associated with the project that contains this cluster must be granted the `cloudkms.cryptoKeyEncrypterDecrypter` role on the CMEK key. 2) Only regional keys can be used and the region of the CMEK key must match the region of the cluster.
               
               > **Note**: Removing the field entirely from the config will cause the provider to default to the backend value.
               
               !> **Warning**: Modifying this field will cause the provider to delete/recreate the entire resource.
               
               !> **Warning:** Modifying the `storage_type`, `zone` or `kms_key_name` of an existing cluster (by
               `cluster_id`) will cause the provider to delete/recreate the entire
               `bigtable.Instance` resource. If these values are changing, use a new
               `cluster_id`.
        :param pulumi.Input[int] num_nodes: The number of nodes in the cluster.
               If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.
        :param pulumi.Input[str] storage_type: The storage type to use. One of `"SSD"` or
               `"HDD"`. Defaults to `"SSD"`.
        :param pulumi.Input[str] zone: The zone to create the Cloud Bigtable cluster in. If it not
               specified, the provider zone is used. Each cluster must have a different zone in the same region. Zones that support
               Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        if autoscaling_config is not None:
            pulumi.set(__self__, "autoscaling_config", autoscaling_config)
        if kms_key_name is not None:
            pulumi.set(__self__, "kms_key_name", kms_key_name)
        if num_nodes is not None:
            pulumi.set(__self__, "num_nodes", num_nodes)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Cloud Bigtable cluster. Must be 6-30 characters and must only contain hyphens, lowercase letters and numbers.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[pulumi.Input['InstanceClusterAutoscalingConfigArgs']]:
        """
        [Autoscaling](https://cloud.google.com/bigtable/docs/autoscaling#parameters) config for the cluster, contains the following arguments:
        """
        return pulumi.get(self, "autoscaling_config")

    @autoscaling_config.setter
    def autoscaling_config(self, value: Optional[pulumi.Input['InstanceClusterAutoscalingConfigArgs']]):
        pulumi.set(self, "autoscaling_config", value)

    @property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the Cloud KMS encryption key that will be used to protect the destination Bigtable cluster. The requirements for this key are: 1) The Cloud Bigtable service account associated with the project that contains this cluster must be granted the `cloudkms.cryptoKeyEncrypterDecrypter` role on the CMEK key. 2) Only regional keys can be used and the region of the CMEK key must match the region of the cluster.

        > **Note**: Removing the field entirely from the config will cause the provider to default to the backend value.

        !> **Warning**: Modifying this field will cause the provider to delete/recreate the entire resource.

        !> **Warning:** Modifying the `storage_type`, `zone` or `kms_key_name` of an existing cluster (by
        `cluster_id`) will cause the provider to delete/recreate the entire
        `bigtable.Instance` resource. If these values are changing, use a new
        `cluster_id`.
        """
        return pulumi.get(self, "kms_key_name")

    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_name", value)

    @property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes in the cluster.
        If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.
        """
        return pulumi.get(self, "num_nodes")

    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_nodes", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The storage type to use. One of `"SSD"` or
        `"HDD"`. Defaults to `"SSD"`.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone to create the Cloud Bigtable cluster in. If it not
        specified, the provider zone is used. Each cluster must have a different zone in the same region. Zones that support
        Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class InstanceClusterAutoscalingConfigArgs:
    def __init__(__self__, *,
                 cpu_target: pulumi.Input[int],
                 max_nodes: pulumi.Input[int],
                 min_nodes: pulumi.Input[int],
                 storage_target: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cpu_target: The target CPU utilization for autoscaling, in percentage. Must be between 10 and 80.
        :param pulumi.Input[int] max_nodes: The maximum number of nodes for autoscaling.
        :param pulumi.Input[int] min_nodes: The minimum number of nodes for autoscaling.
        :param pulumi.Input[int] storage_target: The target storage utilization for autoscaling, in GB, for each node in a cluster. This number is limited between 2560 (2.5TiB) and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16 TiB) for an HDD cluster. If not set, whatever is already set for the cluster will not change, or if the cluster is just being created, it will use the default value of 2560 for SSD clusters and 8192 for HDD clusters.
               
               !> **Warning**: Only one of `autoscaling_config` or `num_nodes` should be set for a cluster. If both are set, `num_nodes` is ignored. If none is set, autoscaling will be disabled and sized to the current node count.
        """
        pulumi.set(__self__, "cpu_target", cpu_target)
        pulumi.set(__self__, "max_nodes", max_nodes)
        pulumi.set(__self__, "min_nodes", min_nodes)
        if storage_target is not None:
            pulumi.set(__self__, "storage_target", storage_target)

    @property
    @pulumi.getter(name="cpuTarget")
    def cpu_target(self) -> pulumi.Input[int]:
        """
        The target CPU utilization for autoscaling, in percentage. Must be between 10 and 80.
        """
        return pulumi.get(self, "cpu_target")

    @cpu_target.setter
    def cpu_target(self, value: pulumi.Input[int]):
        pulumi.set(self, "cpu_target", value)

    @property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> pulumi.Input[int]:
        """
        The maximum number of nodes for autoscaling.
        """
        return pulumi.get(self, "max_nodes")

    @max_nodes.setter
    def max_nodes(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_nodes", value)

    @property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> pulumi.Input[int]:
        """
        The minimum number of nodes for autoscaling.
        """
        return pulumi.get(self, "min_nodes")

    @min_nodes.setter
    def min_nodes(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_nodes", value)

    @property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> Optional[pulumi.Input[int]]:
        """
        The target storage utilization for autoscaling, in GB, for each node in a cluster. This number is limited between 2560 (2.5TiB) and 5120 (5TiB) for a SSD cluster and between 8192 (8TiB) and 16384 (16 TiB) for an HDD cluster. If not set, whatever is already set for the cluster will not change, or if the cluster is just being created, it will use the default value of 2560 for SSD clusters and 8192 for HDD clusters.

        !> **Warning**: Only one of `autoscaling_config` or `num_nodes` should be set for a cluster. If both are set, `num_nodes` is ignored. If none is set, autoscaling will be disabled and sized to the current node count.
        """
        return pulumi.get(self, "storage_target")

    @storage_target.setter
    def storage_target(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_target", value)


@pulumi.input_type
class InstanceIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class InstanceIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class TableColumnFamilyArgs:
    def __init__(__self__, *,
                 family: pulumi.Input[str]):
        """
        :param pulumi.Input[str] family: The name of the column family.
        """
        pulumi.set(__self__, "family", family)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[str]:
        """
        The name of the column family.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[str]):
        pulumi.set(self, "family", value)


@pulumi.input_type
class TableIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class TableIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


