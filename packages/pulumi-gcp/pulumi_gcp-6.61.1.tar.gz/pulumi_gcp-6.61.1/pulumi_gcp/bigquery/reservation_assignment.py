# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReservationAssignmentArgs', 'ReservationAssignment']

@pulumi.input_type
class ReservationAssignmentArgs:
    def __init__(__self__, *,
                 assignee: pulumi.Input[str],
                 job_type: pulumi.Input[str],
                 reservation: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReservationAssignment resource.
        :param pulumi.Input[str] assignee: The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        :param pulumi.Input[str] job_type: Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        :param pulumi.Input[str] reservation: The reservation for the resource
               
               
               
               - - -
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] project: The project for the resource
        """
        pulumi.set(__self__, "assignee", assignee)
        pulumi.set(__self__, "job_type", job_type)
        pulumi.set(__self__, "reservation", reservation)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def assignee(self) -> pulumi.Input[str]:
        """
        The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        """
        return pulumi.get(self, "assignee")

    @assignee.setter
    def assignee(self, value: pulumi.Input[str]):
        pulumi.set(self, "assignee", value)

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Input[str]:
        """
        Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        """
        return pulumi.get(self, "job_type")

    @job_type.setter
    def job_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_type", value)

    @property
    @pulumi.getter
    def reservation(self) -> pulumi.Input[str]:
        """
        The reservation for the resource



        - - -
        """
        return pulumi.get(self, "reservation")

    @reservation.setter
    def reservation(self, value: pulumi.Input[str]):
        pulumi.set(self, "reservation", value)

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
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project for the resource
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ReservationAssignmentState:
    def __init__(__self__, *,
                 assignee: Optional[pulumi.Input[str]] = None,
                 job_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ReservationAssignment resources.
        :param pulumi.Input[str] assignee: The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        :param pulumi.Input[str] job_type: Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Output only. The resource name of the assignment.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] reservation: The reservation for the resource
               
               
               
               - - -
        :param pulumi.Input[str] state: Assignment will remain in PENDING state if no active capacity commitment is present. It will become ACTIVE when some capacity commitment becomes active. Possible values: STATE_UNSPECIFIED, PENDING, ACTIVE
        """
        if assignee is not None:
            pulumi.set(__self__, "assignee", assignee)
        if job_type is not None:
            pulumi.set(__self__, "job_type", job_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if reservation is not None:
            pulumi.set(__self__, "reservation", reservation)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def assignee(self) -> Optional[pulumi.Input[str]]:
        """
        The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        """
        return pulumi.get(self, "assignee")

    @assignee.setter
    def assignee(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignee", value)

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[str]]:
        """
        Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        """
        return pulumi.get(self, "job_type")

    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_type", value)

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
        Output only. The resource name of the assignment.
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
    def reservation(self) -> Optional[pulumi.Input[str]]:
        """
        The reservation for the resource



        - - -
        """
        return pulumi.get(self, "reservation")

    @reservation.setter
    def reservation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reservation", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Assignment will remain in PENDING state if no active capacity commitment is present. It will become ACTIVE when some capacity commitment becomes active. Possible values: STATE_UNSPECIFIED, PENDING, ACTIVE
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class ReservationAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignee: Optional[pulumi.Input[str]] = None,
                 job_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The BigqueryReservation Assignment resource

        ## Example Usage
        ### Basic
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.bigquery.Reservation("basic",
            project="my-project-name",
            location="us-central1",
            slot_capacity=0,
            ignore_idle_slots=False)
        primary = gcp.bigquery.ReservationAssignment("primary",
            assignee="projects/my-project-name",
            job_type="PIPELINE",
            reservation=basic.id)
        ```

        ## Import

        Assignment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default projects/{{project}}/locations/{{location}}/reservations/{{reservation}}/assignments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default {{project}}/{{location}}/{{reservation}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default {{location}}/{{reservation}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assignee: The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        :param pulumi.Input[str] job_type: Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] reservation: The reservation for the resource
               
               
               
               - - -
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReservationAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The BigqueryReservation Assignment resource

        ## Example Usage
        ### Basic
        ```python
        import pulumi
        import pulumi_gcp as gcp

        basic = gcp.bigquery.Reservation("basic",
            project="my-project-name",
            location="us-central1",
            slot_capacity=0,
            ignore_idle_slots=False)
        primary = gcp.bigquery.ReservationAssignment("primary",
            assignee="projects/my-project-name",
            job_type="PIPELINE",
            reservation=basic.id)
        ```

        ## Import

        Assignment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default projects/{{project}}/locations/{{location}}/reservations/{{reservation}}/assignments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default {{project}}/{{location}}/{{reservation}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:bigquery/reservationAssignment:ReservationAssignment default {{location}}/{{reservation}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param ReservationAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReservationAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignee: Optional[pulumi.Input[str]] = None,
                 job_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReservationAssignmentArgs.__new__(ReservationAssignmentArgs)

            if assignee is None and not opts.urn:
                raise TypeError("Missing required property 'assignee'")
            __props__.__dict__["assignee"] = assignee
            if job_type is None and not opts.urn:
                raise TypeError("Missing required property 'job_type'")
            __props__.__dict__["job_type"] = job_type
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            if reservation is None and not opts.urn:
                raise TypeError("Missing required property 'reservation'")
            __props__.__dict__["reservation"] = reservation
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
        super(ReservationAssignment, __self__).__init__(
            'gcp:bigquery/reservationAssignment:ReservationAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            assignee: Optional[pulumi.Input[str]] = None,
            job_type: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            reservation: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'ReservationAssignment':
        """
        Get an existing ReservationAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assignee: The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        :param pulumi.Input[str] job_type: Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        :param pulumi.Input[str] location: The location for the resource
        :param pulumi.Input[str] name: Output only. The resource name of the assignment.
        :param pulumi.Input[str] project: The project for the resource
        :param pulumi.Input[str] reservation: The reservation for the resource
               
               
               
               - - -
        :param pulumi.Input[str] state: Assignment will remain in PENDING state if no active capacity commitment is present. It will become ACTIVE when some capacity commitment becomes active. Possible values: STATE_UNSPECIFIED, PENDING, ACTIVE
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReservationAssignmentState.__new__(_ReservationAssignmentState)

        __props__.__dict__["assignee"] = assignee
        __props__.__dict__["job_type"] = job_type
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["reservation"] = reservation
        __props__.__dict__["state"] = state
        return ReservationAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def assignee(self) -> pulumi.Output[str]:
        """
        The resource which will use the reservation. E.g. projects/myproject, folders/123, organizations/456.
        """
        return pulumi.get(self, "assignee")

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[str]:
        """
        Types of job, which could be specified when using the reservation. Possible values: JOB_TYPE_UNSPECIFIED, PIPELINE, QUERY
        """
        return pulumi.get(self, "job_type")

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
        Output only. The resource name of the assignment.
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
    def reservation(self) -> pulumi.Output[str]:
        """
        The reservation for the resource



        - - -
        """
        return pulumi.get(self, "reservation")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Assignment will remain in PENDING state if no active capacity commitment is present. It will become ACTIVE when some capacity commitment becomes active. Possible values: STATE_UNSPECIFIED, PENDING, ACTIVE
        """
        return pulumi.get(self, "state")

