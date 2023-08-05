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
    'ExtensionsInstanceConfig',
    'ExtensionsInstanceErrorStatus',
    'ExtensionsInstanceRuntimeData',
    'ExtensionsInstanceRuntimeDataFatalError',
    'ExtensionsInstanceRuntimeDataProcessingState',
    'HostingVersionConfig',
    'HostingVersionConfigRedirect',
    'HostingVersionConfigRewrite',
    'HostingVersionConfigRewriteRun',
]

@pulumi.output_type
class ExtensionsInstanceConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "extensionRef":
            suggest = "extension_ref"
        elif key == "allowedEventTypes":
            suggest = "allowed_event_types"
        elif key == "createTime":
            suggest = "create_time"
        elif key == "eventarcChannel":
            suggest = "eventarc_channel"
        elif key == "extensionVersion":
            suggest = "extension_version"
        elif key == "populatedPostinstallContent":
            suggest = "populated_postinstall_content"
        elif key == "systemParams":
            suggest = "system_params"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionsInstanceConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionsInstanceConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionsInstanceConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 extension_ref: str,
                 params: Mapping[str, str],
                 allowed_event_types: Optional[Sequence[str]] = None,
                 create_time: Optional[str] = None,
                 eventarc_channel: Optional[str] = None,
                 extension_version: Optional[str] = None,
                 name: Optional[str] = None,
                 populated_postinstall_content: Optional[str] = None,
                 system_params: Optional[Mapping[str, str]] = None):
        """
        :param str extension_ref: The ref of the Extension from the Registry (e.g. publisher-id/awesome-extension)
        :param Mapping[str, str] params: Environment variables that may be configured for the Extension
        :param Sequence[str] allowed_event_types: List of extension events selected by consumer that extension is allowed to
               emit, identified by their types.
        :param str create_time: (Output)
               The time at which the Extension Instance Config was created.
        :param str eventarc_channel: Fully qualified Eventarc resource name that consumers should use for event triggers.
        :param str extension_version: The version of the Extension from the Registry (e.g. 1.0.3). If left blank, latest is assumed.
        :param str name: (Output)
               The unique identifier for this configuration.
        :param str populated_postinstall_content: (Output)
               Postinstall instructions to be shown for this Extension, with
               template strings representing function and parameter values substituted
               with actual values. These strings include: ${param:FOO},
               ${function:myFunc.url},
               ${function:myFunc.name}, and ${function:myFunc.location}
               
               - - -
        :param Mapping[str, str] system_params: Params whose values are only available at deployment time.
               Unlike other params, these will not be set as environment variables on
               functions.
        """
        pulumi.set(__self__, "extension_ref", extension_ref)
        pulumi.set(__self__, "params", params)
        if allowed_event_types is not None:
            pulumi.set(__self__, "allowed_event_types", allowed_event_types)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if eventarc_channel is not None:
            pulumi.set(__self__, "eventarc_channel", eventarc_channel)
        if extension_version is not None:
            pulumi.set(__self__, "extension_version", extension_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if populated_postinstall_content is not None:
            pulumi.set(__self__, "populated_postinstall_content", populated_postinstall_content)
        if system_params is not None:
            pulumi.set(__self__, "system_params", system_params)

    @property
    @pulumi.getter(name="extensionRef")
    def extension_ref(self) -> str:
        """
        The ref of the Extension from the Registry (e.g. publisher-id/awesome-extension)
        """
        return pulumi.get(self, "extension_ref")

    @property
    @pulumi.getter
    def params(self) -> Mapping[str, str]:
        """
        Environment variables that may be configured for the Extension
        """
        return pulumi.get(self, "params")

    @property
    @pulumi.getter(name="allowedEventTypes")
    def allowed_event_types(self) -> Optional[Sequence[str]]:
        """
        List of extension events selected by consumer that extension is allowed to
        emit, identified by their types.
        """
        return pulumi.get(self, "allowed_event_types")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        """
        (Output)
        The time at which the Extension Instance Config was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="eventarcChannel")
    def eventarc_channel(self) -> Optional[str]:
        """
        Fully qualified Eventarc resource name that consumers should use for event triggers.
        """
        return pulumi.get(self, "eventarc_channel")

    @property
    @pulumi.getter(name="extensionVersion")
    def extension_version(self) -> Optional[str]:
        """
        The version of the Extension from the Registry (e.g. 1.0.3). If left blank, latest is assumed.
        """
        return pulumi.get(self, "extension_version")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        (Output)
        The unique identifier for this configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="populatedPostinstallContent")
    def populated_postinstall_content(self) -> Optional[str]:
        """
        (Output)
        Postinstall instructions to be shown for this Extension, with
        template strings representing function and parameter values substituted
        with actual values. These strings include: ${param:FOO},
        ${function:myFunc.url},
        ${function:myFunc.name}, and ${function:myFunc.location}

        - - -
        """
        return pulumi.get(self, "populated_postinstall_content")

    @property
    @pulumi.getter(name="systemParams")
    def system_params(self) -> Optional[Mapping[str, str]]:
        """
        Params whose values are only available at deployment time.
        Unlike other params, these will not be set as environment variables on
        functions.
        """
        return pulumi.get(self, "system_params")


@pulumi.output_type
class ExtensionsInstanceErrorStatus(dict):
    def __init__(__self__, *,
                 code: Optional[int] = None,
                 details: Optional[Sequence[Mapping[str, Any]]] = None,
                 message: Optional[str] = None):
        """
        :param int code: The status code, which should be an enum value of google.rpc.Code.
        :param Sequence[Mapping[str, Any]] details: A list of messages that carry the error details.
        :param str message: A developer-facing error message, which should be in English.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[int]:
        """
        The status code, which should be an enum value of google.rpc.Code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, Any]]]:
        """
        A list of messages that carry the error details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A developer-facing error message, which should be in English.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class ExtensionsInstanceRuntimeData(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fatalError":
            suggest = "fatal_error"
        elif key == "processingState":
            suggest = "processing_state"
        elif key == "stateUpdateTime":
            suggest = "state_update_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionsInstanceRuntimeData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionsInstanceRuntimeData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionsInstanceRuntimeData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fatal_error: Optional['outputs.ExtensionsInstanceRuntimeDataFatalError'] = None,
                 processing_state: Optional['outputs.ExtensionsInstanceRuntimeDataProcessingState'] = None,
                 state_update_time: Optional[str] = None):
        """
        :param 'ExtensionsInstanceRuntimeDataFatalErrorArgs' fatal_error: The fatal error state for the extension instance
               Structure is documented below.
        :param 'ExtensionsInstanceRuntimeDataProcessingStateArgs' processing_state: The processing state for the extension instance
               Structure is documented below.
        :param str state_update_time: The time of the last state update.
        """
        if fatal_error is not None:
            pulumi.set(__self__, "fatal_error", fatal_error)
        if processing_state is not None:
            pulumi.set(__self__, "processing_state", processing_state)
        if state_update_time is not None:
            pulumi.set(__self__, "state_update_time", state_update_time)

    @property
    @pulumi.getter(name="fatalError")
    def fatal_error(self) -> Optional['outputs.ExtensionsInstanceRuntimeDataFatalError']:
        """
        The fatal error state for the extension instance
        Structure is documented below.
        """
        return pulumi.get(self, "fatal_error")

    @property
    @pulumi.getter(name="processingState")
    def processing_state(self) -> Optional['outputs.ExtensionsInstanceRuntimeDataProcessingState']:
        """
        The processing state for the extension instance
        Structure is documented below.
        """
        return pulumi.get(self, "processing_state")

    @property
    @pulumi.getter(name="stateUpdateTime")
    def state_update_time(self) -> Optional[str]:
        """
        The time of the last state update.
        """
        return pulumi.get(self, "state_update_time")


@pulumi.output_type
class ExtensionsInstanceRuntimeDataFatalError(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "errorMessage":
            suggest = "error_message"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionsInstanceRuntimeDataFatalError. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionsInstanceRuntimeDataFatalError.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionsInstanceRuntimeDataFatalError.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 error_message: Optional[str] = None):
        """
        :param str error_message: The error message. This is set by the extension developer to give
               more detail on why the extension is unusable and must be re-installed
               or reconfigured.
        """
        if error_message is not None:
            pulumi.set(__self__, "error_message", error_message)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[str]:
        """
        The error message. This is set by the extension developer to give
        more detail on why the extension is unusable and must be re-installed
        or reconfigured.
        """
        return pulumi.get(self, "error_message")


@pulumi.output_type
class ExtensionsInstanceRuntimeDataProcessingState(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "detailMessage":
            suggest = "detail_message"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionsInstanceRuntimeDataProcessingState. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionsInstanceRuntimeDataProcessingState.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionsInstanceRuntimeDataProcessingState.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 detail_message: Optional[str] = None,
                 state: Optional[str] = None):
        """
        :param str detail_message: Details about the processing. e.g. This could include the type of
               processing in progress or it could list errors or failures.
               This information will be shown in the console on the detail page
               for the extension instance.
        :param str state: The processing state of the extension instance.
        """
        if detail_message is not None:
            pulumi.set(__self__, "detail_message", detail_message)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="detailMessage")
    def detail_message(self) -> Optional[str]:
        """
        Details about the processing. e.g. This could include the type of
        processing in progress or it could list errors or failures.
        This information will be shown in the console on the detail page
        for the extension instance.
        """
        return pulumi.get(self, "detail_message")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The processing state of the extension instance.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class HostingVersionConfig(dict):
    def __init__(__self__, *,
                 redirects: Optional[Sequence['outputs.HostingVersionConfigRedirect']] = None,
                 rewrites: Optional[Sequence['outputs.HostingVersionConfigRewrite']] = None):
        """
        :param Sequence['HostingVersionConfigRedirectArgs'] redirects: An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path,
               triggers Hosting to respond with a redirect to the specified destination path.
               Structure is documented below.
        :param Sequence['HostingVersionConfigRewriteArgs'] rewrites: An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the
               request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
               Structure is documented below.
        """
        if redirects is not None:
            pulumi.set(__self__, "redirects", redirects)
        if rewrites is not None:
            pulumi.set(__self__, "rewrites", rewrites)

    @property
    @pulumi.getter
    def redirects(self) -> Optional[Sequence['outputs.HostingVersionConfigRedirect']]:
        """
        An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path,
        triggers Hosting to respond with a redirect to the specified destination path.
        Structure is documented below.
        """
        return pulumi.get(self, "redirects")

    @property
    @pulumi.getter
    def rewrites(self) -> Optional[Sequence['outputs.HostingVersionConfigRewrite']]:
        """
        An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the
        request URL path, triggers Hosting to respond as if the service were given the specified destination URL.
        Structure is documented below.
        """
        return pulumi.get(self, "rewrites")


@pulumi.output_type
class HostingVersionConfigRedirect(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "statusCode":
            suggest = "status_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostingVersionConfigRedirect. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostingVersionConfigRedirect.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostingVersionConfigRedirect.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 location: str,
                 status_code: int,
                 glob: Optional[str] = None,
                 regex: Optional[str] = None):
        """
        :param str location: The value to put in the HTTP location header of the response.
               The location can contain capture group values from the pattern using a : prefix to identify
               the segment and an optional * to capture the rest of the URL. For example:
               ```python
               import pulumi
               ```
        :param int status_code: The status HTTP code to return in the response. It must be a valid 3xx status code.
        :param str glob: The user-supplied glob to match against the request URL path.
        :param str regex: The user-supplied RE2 regular expression to match against the request URL path.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "status_code", status_code)
        if glob is not None:
            pulumi.set(__self__, "glob", glob)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The value to put in the HTTP location header of the response.
        The location can contain capture group values from the pattern using a : prefix to identify
        the segment and an optional * to capture the rest of the URL. For example:
        ```python
        import pulumi
        ```
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> int:
        """
        The status HTTP code to return in the response. It must be a valid 3xx status code.
        """
        return pulumi.get(self, "status_code")

    @property
    @pulumi.getter
    def glob(self) -> Optional[str]:
        """
        The user-supplied glob to match against the request URL path.
        """
        return pulumi.get(self, "glob")

    @property
    @pulumi.getter
    def regex(self) -> Optional[str]:
        """
        The user-supplied RE2 regular expression to match against the request URL path.
        """
        return pulumi.get(self, "regex")


@pulumi.output_type
class HostingVersionConfigRewrite(dict):
    def __init__(__self__, *,
                 function: Optional[str] = None,
                 glob: Optional[str] = None,
                 regex: Optional[str] = None,
                 run: Optional['outputs.HostingVersionConfigRewriteRun'] = None):
        """
        :param str function: The function to proxy requests to. Must match the exported function name exactly.
        :param str glob: The user-supplied glob to match against the request URL path.
        :param str regex: The user-supplied RE2 regular expression to match against the request URL path.
        :param 'HostingVersionConfigRewriteRunArgs' run: The request will be forwarded to Cloud Run.
               Structure is documented below.
        """
        if function is not None:
            pulumi.set(__self__, "function", function)
        if glob is not None:
            pulumi.set(__self__, "glob", glob)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)
        if run is not None:
            pulumi.set(__self__, "run", run)

    @property
    @pulumi.getter
    def function(self) -> Optional[str]:
        """
        The function to proxy requests to. Must match the exported function name exactly.
        """
        return pulumi.get(self, "function")

    @property
    @pulumi.getter
    def glob(self) -> Optional[str]:
        """
        The user-supplied glob to match against the request URL path.
        """
        return pulumi.get(self, "glob")

    @property
    @pulumi.getter
    def regex(self) -> Optional[str]:
        """
        The user-supplied RE2 regular expression to match against the request URL path.
        """
        return pulumi.get(self, "regex")

    @property
    @pulumi.getter
    def run(self) -> Optional['outputs.HostingVersionConfigRewriteRun']:
        """
        The request will be forwarded to Cloud Run.
        Structure is documented below.
        """
        return pulumi.get(self, "run")


@pulumi.output_type
class HostingVersionConfigRewriteRun(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceId":
            suggest = "service_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostingVersionConfigRewriteRun. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostingVersionConfigRewriteRun.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostingVersionConfigRewriteRun.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_id: str,
                 region: Optional[str] = None):
        """
        :param str service_id: User-defined ID of the Cloud Run service.
        :param str region: Optional. User-provided region where the Cloud Run service is hosted. Defaults to `us-central1` if not supplied.
        """
        pulumi.set(__self__, "service_id", service_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        User-defined ID of the Cloud Run service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        Optional. User-provided region where the Cloud Run service is hosted. Defaults to `us-central1` if not supplied.
        """
        return pulumi.get(self, "region")


