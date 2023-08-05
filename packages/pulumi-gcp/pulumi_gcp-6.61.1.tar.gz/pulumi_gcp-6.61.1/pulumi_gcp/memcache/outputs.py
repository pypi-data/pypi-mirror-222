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
    'InstanceMaintenancePolicy',
    'InstanceMaintenancePolicyWeeklyMaintenanceWindow',
    'InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime',
    'InstanceMaintenanceSchedule',
    'InstanceMemcacheNode',
    'InstanceMemcacheParameters',
    'InstanceNodeConfig',
]

@pulumi.output_type
class InstanceMaintenancePolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "weeklyMaintenanceWindows":
            suggest = "weekly_maintenance_windows"
        elif key == "createTime":
            suggest = "create_time"
        elif key == "updateTime":
            suggest = "update_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceMaintenancePolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceMaintenancePolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceMaintenancePolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 weekly_maintenance_windows: Sequence['outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow'],
                 create_time: Optional[str] = None,
                 description: Optional[str] = None,
                 update_time: Optional[str] = None):
        """
        :param Sequence['InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs'] weekly_maintenance_windows: Required. Maintenance window that is applied to resources covered by this policy.
               Minimum 1. For the current version, the maximum number of weekly_maintenance_windows
               is expected to be one.
               Structure is documented below.
        :param str create_time: (Output)
               Output only. The time when the policy was created.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits
        :param str description: Optional. Description of what this policy is for.
               Create/Update methods return INVALID_ARGUMENT if the
               length is greater than 512.
        :param str update_time: (Output)
               Output only. The time when the policy was updated.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits.
        """
        pulumi.set(__self__, "weekly_maintenance_windows", weekly_maintenance_windows)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(self) -> Sequence['outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow']:
        """
        Required. Maintenance window that is applied to resources covered by this policy.
        Minimum 1. For the current version, the maximum number of weekly_maintenance_windows
        is expected to be one.
        Structure is documented below.
        """
        return pulumi.get(self, "weekly_maintenance_windows")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The time when the policy was created.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional. Description of what this policy is for.
        Create/Update methods return INVALID_ARGUMENT if the
        length is greater than 512.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The time when the policy was updated.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "update_time")


@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceMaintenancePolicyWeeklyMaintenanceWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceMaintenancePolicyWeeklyMaintenanceWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceMaintenancePolicyWeeklyMaintenanceWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day: str,
                 duration: str,
                 start_time: 'outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime'):
        """
        :param str day: Required. The day of week that maintenance updates occur.
               - DAY_OF_WEEK_UNSPECIFIED: The day of the week is unspecified.
               - MONDAY: Monday
               - TUESDAY: Tuesday
               - WEDNESDAY: Wednesday
               - THURSDAY: Thursday
               - FRIDAY: Friday
               - SATURDAY: Saturday
               - SUNDAY: Sunday
               Possible values are: `DAY_OF_WEEK_UNSPECIFIED`, `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`.
        :param str duration: Required. The length of the maintenance window, ranging from 3 hours to 8 hours.
               A duration in seconds with up to nine fractional digits,
               terminated by 's'. Example: "3.5s".
        :param 'InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs' start_time: Required. Start time of the window in UTC time.
               Structure is documented below.
        """
        pulumi.set(__self__, "day", day)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def day(self) -> str:
        """
        Required. The day of week that maintenance updates occur.
        - DAY_OF_WEEK_UNSPECIFIED: The day of the week is unspecified.
        - MONDAY: Monday
        - TUESDAY: Tuesday
        - WEDNESDAY: Wednesday
        - THURSDAY: Thursday
        - FRIDAY: Friday
        - SATURDAY: Saturday
        - SUNDAY: Sunday
        Possible values are: `DAY_OF_WEEK_UNSPECIFIED`, `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`.
        """
        return pulumi.get(self, "day")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Required. The length of the maintenance window, ranging from 3 hours to 8 hours.
        A duration in seconds with up to nine fractional digits,
        terminated by 's'. Example: "3.5s".
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> 'outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime':
        """
        Required. Start time of the window in UTC time.
        Structure is documented below.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(dict):
    def __init__(__self__, *,
                 hours: Optional[int] = None,
                 minutes: Optional[int] = None,
                 nanos: Optional[int] = None,
                 seconds: Optional[int] = None):
        """
        :param int hours: Hours of day in 24 hour format. Should be from 0 to 23.
               An API may choose to allow the value "24:00:00" for scenarios like business closing time.
        :param int minutes: Minutes of hour of day. Must be from 0 to 59.
        :param int nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
        :param int seconds: Seconds of minutes of the time. Must normally be from 0 to 59.
               An API may allow the value 60 if it allows leap-seconds.
        """
        if hours is not None:
            pulumi.set(__self__, "hours", hours)
        if minutes is not None:
            pulumi.set(__self__, "minutes", minutes)
        if nanos is not None:
            pulumi.set(__self__, "nanos", nanos)
        if seconds is not None:
            pulumi.set(__self__, "seconds", seconds)

    @property
    @pulumi.getter
    def hours(self) -> Optional[int]:
        """
        Hours of day in 24 hour format. Should be from 0 to 23.
        An API may choose to allow the value "24:00:00" for scenarios like business closing time.
        """
        return pulumi.get(self, "hours")

    @property
    @pulumi.getter
    def minutes(self) -> Optional[int]:
        """
        Minutes of hour of day. Must be from 0 to 59.
        """
        return pulumi.get(self, "minutes")

    @property
    @pulumi.getter
    def nanos(self) -> Optional[int]:
        """
        Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
        """
        return pulumi.get(self, "nanos")

    @property
    @pulumi.getter
    def seconds(self) -> Optional[int]:
        """
        Seconds of minutes of the time. Must normally be from 0 to 59.
        An API may allow the value 60 if it allows leap-seconds.
        """
        return pulumi.get(self, "seconds")


@pulumi.output_type
class InstanceMaintenanceSchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endTime":
            suggest = "end_time"
        elif key == "scheduleDeadlineTime":
            suggest = "schedule_deadline_time"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceMaintenanceSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceMaintenanceSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceMaintenanceSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_time: Optional[str] = None,
                 schedule_deadline_time: Optional[str] = None,
                 start_time: Optional[str] = None):
        """
        :param str end_time: (Output)
               Output only. The end time of any upcoming scheduled maintenance for this instance.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits.
        :param str schedule_deadline_time: (Output)
               Output only. The deadline that the maintenance schedule start time
               can not go beyond, including reschedule.
               A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
               resolution and up to nine fractional digits.
        :param str start_time: Required. Start time of the window in UTC time.
               Structure is documented below.
        """
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if schedule_deadline_time is not None:
            pulumi.set(__self__, "schedule_deadline_time", schedule_deadline_time)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The end time of any upcoming scheduled maintenance for this instance.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[str]:
        """
        (Output)
        Output only. The deadline that the maintenance schedule start time
        can not go beyond, including reschedule.
        A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
        resolution and up to nine fractional digits.
        """
        return pulumi.get(self, "schedule_deadline_time")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Required. Start time of the window in UTC time.
        Structure is documented below.
        """
        return pulumi.get(self, "start_time")


@pulumi.output_type
class InstanceMemcacheNode(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nodeId":
            suggest = "node_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceMemcacheNode. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceMemcacheNode.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceMemcacheNode.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host: Optional[str] = None,
                 node_id: Optional[str] = None,
                 port: Optional[int] = None,
                 state: Optional[str] = None,
                 zone: Optional[str] = None):
        """
        :param str host: (Output)
               Hostname or IP address of the Memcached node used by the clients to connect to the Memcached server on this node.
        :param str node_id: (Output)
               Identifier of the Memcached node. The node id does not include project or location like the Memcached instance name.
        :param int port: (Output)
               The port number of the Memcached server on this node.
        :param str state: (Output)
               Current state of the Memcached node.
        :param str zone: (Output)
               Location (GCP Zone) for the Memcached node.
        """
        if host is not None:
            pulumi.set(__self__, "host", host)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def host(self) -> Optional[str]:
        """
        (Output)
        Hostname or IP address of the Memcached node used by the clients to connect to the Memcached server on this node.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[str]:
        """
        (Output)
        Identifier of the Memcached node. The node id does not include project or location like the Memcached instance name.
        """
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        (Output)
        The port number of the Memcached server on this node.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        (Output)
        Current state of the Memcached node.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        """
        (Output)
        Location (GCP Zone) for the Memcached node.
        """
        return pulumi.get(self, "zone")


@pulumi.output_type
class InstanceMemcacheParameters(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 params: Optional[Mapping[str, str]] = None):
        """
        :param str id: (Output)
               This is a unique ID associated with this set of parameters.
        :param Mapping[str, str] params: User-defined set of parameters to use in the memcache process.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if params is not None:
            pulumi.set(__self__, "params", params)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        (Output)
        This is a unique ID associated with this set of parameters.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def params(self) -> Optional[Mapping[str, str]]:
        """
        User-defined set of parameters to use in the memcache process.
        """
        return pulumi.get(self, "params")


@pulumi.output_type
class InstanceNodeConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cpuCount":
            suggest = "cpu_count"
        elif key == "memorySizeMb":
            suggest = "memory_size_mb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceNodeConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceNodeConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceNodeConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cpu_count: int,
                 memory_size_mb: int):
        """
        :param int cpu_count: Number of CPUs per node.
        :param int memory_size_mb: Memory size in Mebibytes for each memcache node.
               
               - - -
        """
        pulumi.set(__self__, "cpu_count", cpu_count)
        pulumi.set(__self__, "memory_size_mb", memory_size_mb)

    @property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> int:
        """
        Number of CPUs per node.
        """
        return pulumi.get(self, "cpu_count")

    @property
    @pulumi.getter(name="memorySizeMb")
    def memory_size_mb(self) -> int:
        """
        Memory size in Mebibytes for each memcache node.

        - - -
        """
        return pulumi.get(self, "memory_size_mb")


