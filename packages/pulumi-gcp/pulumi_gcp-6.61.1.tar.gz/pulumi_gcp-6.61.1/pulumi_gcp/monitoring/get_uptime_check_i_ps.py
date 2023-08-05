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
    'GetUptimeCheckIPsResult',
    'AwaitableGetUptimeCheckIPsResult',
    'get_uptime_check_i_ps',
]

@pulumi.output_type
class GetUptimeCheckIPsResult:
    """
    A collection of values returned by getUptimeCheckIPs.
    """
    def __init__(__self__, id=None, uptime_check_ips=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if uptime_check_ips and not isinstance(uptime_check_ips, list):
            raise TypeError("Expected argument 'uptime_check_ips' to be a list")
        pulumi.set(__self__, "uptime_check_ips", uptime_check_ips)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="uptimeCheckIps")
    def uptime_check_ips(self) -> Sequence['outputs.GetUptimeCheckIPsUptimeCheckIpResult']:
        """
        A list of uptime check IPs used by Stackdriver Monitoring. Each `uptime_check_ip` contains:
        """
        return pulumi.get(self, "uptime_check_ips")


class AwaitableGetUptimeCheckIPsResult(GetUptimeCheckIPsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUptimeCheckIPsResult(
            id=self.id,
            uptime_check_ips=self.uptime_check_ips)


def get_uptime_check_i_ps(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUptimeCheckIPsResult:
    """
    Returns the list of IP addresses that checkers run from. For more information see
    the [official documentation](https://cloud.google.com/monitoring/uptime-checks#get-ips).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gcp as gcp

    ips = gcp.monitoring.get_uptime_check_i_ps()
    pulumi.export("ipList", ips.uptime_check_ips)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:monitoring/getUptimeCheckIPs:getUptimeCheckIPs', __args__, opts=opts, typ=GetUptimeCheckIPsResult).value

    return AwaitableGetUptimeCheckIPsResult(
        id=pulumi.get(__ret__, 'id'),
        uptime_check_ips=pulumi.get(__ret__, 'uptime_check_ips'))
