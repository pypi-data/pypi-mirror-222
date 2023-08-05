#  Copyright 2022 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# flake8: noqa


# This file is automatically generated. Please do not modify it directly.
# Find the relevant recipe file in the samples/recipes or samples/ingredients
# directory and apply your changes there.


# [START compute_instances_create_from_template_with_overrides]
from __future__ import annotations

import sys
from typing import Any

from google.api_core.extended_operation import ExtendedOperation
from google.cloud import compute_v1


def wait_for_extended_operation(
    operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
) -> Any:
    """
    Waits for the extended (long-running) operation to complete.

    If the operation is successful, it will return its result.
    If the operation ends with an error, an exception will be raised.
    If there were any warnings during the execution of the operation
    they will be printed to sys.stderr.

    Args:
        operation: a long-running operation you want to wait on.
        verbose_name: (optional) a more verbose name of the operation,
            used only during error and warning reporting.
        timeout: how long (in seconds) to wait for operation to finish.
            If None, wait indefinitely.

    Returns:
        Whatever the operation.result() returns.

    Raises:
        This method will raise the exception received from `operation.exception()`
        or RuntimeError if there is no exception set, but there is an `error_code`
        set for the `operation`.

        In case of an operation taking longer than `timeout` seconds to complete,
        a `concurrent.futures.TimeoutError` will be raised.
    """
    result = operation.result(timeout=timeout)

    if operation.error_code:
        print(
            f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
            file=sys.stderr,
            flush=True,
        )
        print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
        raise operation.exception() or RuntimeError(operation.error_message)

    if operation.warnings:
        print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
        for warning in operation.warnings:
            print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)

    return result


def create_instance_from_template_with_overrides(
    project_id: str,
    zone: str,
    instance_name: str,
    instance_template_name: str,
    machine_type: str,
    new_disk_source_image: str,
) -> compute_v1.Instance:
    """
    Creates a Compute Engine VM instance from an instance template, changing the machine type and
    adding a new disk created from a source image.

    Args:
        project_id: ID or number of the project you want to use.
        zone: Name of the zone you want to check, for example: us-west3-b
        instance_name: Name of the new instance.
        instance_template_name: Name of the instance template used for creating the new instance.
        machine_type: Machine type you want to set in following format:
            "zones/{zone}/machineTypes/{type_name}". For example:
            - "zones/europe-west3-c/machineTypes/f1-micro"
            - You can find the list of available machine types using:
              https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
        new_disk_source_image: Path the the disk image you want to use for your new
            disk. This can be one of the public images
            (like "projects/debian-cloud/global/images/family/debian-10")
            or a private image you have access to.
            For a list of available public images, see the documentation:
            http://cloud.google.com/compute/docs/images

    Returns:
        Instance object.
    """
    instance_client = compute_v1.InstancesClient()
    instance_template_client = compute_v1.InstanceTemplatesClient()

    # Retrieve an instance template by name.
    instance_template = instance_template_client.get(
        project=project_id, instance_template=instance_template_name
    )

    # Adjust diskType field of the instance template to use the URL formatting required by instances.insert.diskType
    # For instance template, there is only a name, not URL.
    for disk in instance_template.properties.disks:
        if disk.initialize_params.disk_type:
            disk.initialize_params.disk_type = (
                f"zones/{zone}/diskTypes/{disk.initialize_params.disk_type}"
            )

    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = machine_type
    instance.disks = list(instance_template.properties.disks)

    new_disk = compute_v1.AttachedDisk()
    new_disk.initialize_params.disk_size_gb = 50
    new_disk.initialize_params.source_image = new_disk_source_image
    new_disk.auto_delete = True
    new_disk.boot = False
    new_disk.type_ = "PERSISTENT"

    instance.disks.append(new_disk)

    instance_insert_request = compute_v1.InsertInstanceRequest()
    instance_insert_request.project = project_id
    instance_insert_request.zone = zone
    instance_insert_request.instance_resource = instance
    instance_insert_request.source_instance_template = instance_template.self_link

    operation = instance_client.insert(instance_insert_request)
    wait_for_extended_operation(operation, "instance creation")

    return instance_client.get(project=project_id, zone=zone, instance=instance_name)


# [END compute_instances_create_from_template_with_overrides]
