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

# This is an ingredient file. It is not meant to be run directly. Check the samples/snippets 
# folder for complete code samples that are ready to be used.
# Disabling flake8 for the ingredients file, as it would fail F821 - undefined name check.
# flake8: noqa
from collections import namedtuple
from enum import Enum, unique


# <INGREDIENT custom_machine_type_helper_class>
def gb_to_mb(value: int) -> int:
    return value << 10


class CustomMachineType:
    """
    Allows to create custom machine types to be used with the VM instances.
    """

    @unique
    class CPUSeries(Enum):
        N1 = "custom"
        N2 = "n2-custom"
        N2D = "n2d-custom"
        E2 = "e2-custom"
        E2_MICRO = "e2-custom-micro"
        E2_SMALL = "e2-custom-small"
        E2_MEDIUM = "e2-custom-medium"

    TypeLimits = namedtuple(
        "TypeLimits",
        [
            "allowed_cores",
            "min_mem_per_core",
            "max_mem_per_core",
            "allow_extra_memory",
            "extra_memory_limit",
        ],
    )

    # The limits for various CPU types are described on:
    # https://cloud.google.com/compute/docs/general-purpose-machines
    LIMITS = {
        CPUSeries.E2: TypeLimits(frozenset(range(2, 33, 2)), 512, 8192, False, 0),
        CPUSeries.E2_MICRO: TypeLimits(frozenset(), 1024, 2048, False, 0),
        CPUSeries.E2_SMALL: TypeLimits(frozenset(), 2048, 4096, False, 0),
        CPUSeries.E2_MEDIUM: TypeLimits(frozenset(), 4096, 8192, False, 0),
        CPUSeries.N2: TypeLimits(
            frozenset(range(2, 33, 2)).union(set(range(36, 129, 4))),
            512,
            8192,
            True,
            gb_to_mb(624),
        ),
        CPUSeries.N2D: TypeLimits(
            frozenset({2, 4, 8, 16, 32, 48, 64, 80, 96}), 512, 8192, True, gb_to_mb(768)
        ),
        CPUSeries.N1: TypeLimits(
            frozenset({1}.union(range(2, 97, 2))), 922, 6656, True, gb_to_mb(624)
        ),
    }

    def __init__(
        self, zone: str, cpu_series: CPUSeries, memory_mb: int, core_count: int = 0
    ):
        self.zone = zone
        self.cpu_series = cpu_series
        self.limits = self.LIMITS[self.cpu_series]
        # Shared machine types (e2-small, e2-medium and e2-micro) always have
        # 2 vCPUs: https://cloud.google.com/compute/docs/general-purpose-machines#e2_limitations
        self.core_count = 2 if self.is_shared() else core_count
        self.memory_mb = memory_mb
        self._checked = False
        self._check_parameters()
        self.extra_memory_used = self._check_extra_memory()

    def is_shared(self):
        return self.cpu_series in (
            CustomMachineType.CPUSeries.E2_SMALL,
            CustomMachineType.CPUSeries.E2_MICRO,
            CustomMachineType.CPUSeries.E2_MEDIUM,
        )

    def _check_extra_memory(self) -> bool:
        if self._checked:
            return self.memory_mb > self.core_count * self.limits.max_mem_per_core
        else:
            raise RuntimeError("You need to call _check_parameters() before calling _check_extra_memory()")

    def _check_parameters(self):
        """
        Check whether the requested parameters are allowed. Find more information about limitations of custom machine
        types at: https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
        """
        # Check the number of cores
        if (
            self.limits.allowed_cores
            and self.core_count not in self.limits.allowed_cores
        ):
            raise RuntimeError(
                f"Invalid number of cores requested. Allowed number of cores for {self.cpu_series.name} is: {sorted(self.limits.allowed_cores)}"
            )

        # Memory must be a multiple of 256 MB
        if self.memory_mb % 256 != 0:
            raise RuntimeError("Requested memory must be a multiple of 256 MB.")

        # Check if the requested memory isn't too little
        if self.memory_mb < self.core_count * self.limits.min_mem_per_core:
            raise RuntimeError(
                f"Requested memory is too low. Minimal memory for {self.cpu_series.name} is {self.limits.min_mem_per_core} MB per core."
            )

        # Check if the requested memory isn't too much
        if self.memory_mb > self.core_count * self.limits.max_mem_per_core:
            if self.limits.allow_extra_memory:
                if self.memory_mb > self.limits.extra_memory_limit:
                    raise RuntimeError(
                        f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.extra_memory_limit} MB."
                    )
            else:
                raise RuntimeError(
                    f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.max_mem_per_core} MB per core."
                )

        self._checked = True

    def __str__(self) -> str:
        """
        Return the custom machine type in form of a string acceptable by Compute Engine API.
        """
        if self.cpu_series in {
            self.CPUSeries.E2_SMALL,
            self.CPUSeries.E2_MICRO,
            self.CPUSeries.E2_MEDIUM,
        }:
            return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.memory_mb}"

        if self.extra_memory_used:
            return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}-ext"

        return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}"

    def short_type_str(self) -> str:
        """
        Return machine type in a format without the zone. For example, n2-custom-0-10240.
        This format is used to create instance templates.
        """
        return str(self).rsplit("/", maxsplit=1)[1]

    @classmethod
    def from_str(cls, machine_type: str):
        """
        Construct a new object from a string. The string needs to be a valid custom machine type like:
         - https://www.googleapis.com/compute/v1/projects/diregapic-mestiv/zones/us-central1-b/machineTypes/e2-custom-4-8192
         - zones/us-central1-b/machineTypes/e2-custom-4-8192
         - e2-custom-4-8192 (in this case, the zone parameter will not be set)
        """
        zone = None
        if machine_type.startswith("http"):
            machine_type = machine_type[machine_type.find("zones/") :]

        if machine_type.startswith("zones/"):
            _, zone, _, machine_type = machine_type.split("/")

        extra_mem = machine_type.endswith("-ext")

        if machine_type.startswith("custom"):
            cpu = cls.CPUSeries.N1
            _, cores, memory = machine_type.rsplit("-", maxsplit=2)
        else:
            if extra_mem:
                cpu_series, _, cores, memory, _ = machine_type.split("-")
            else:
                cpu_series, _, cores, memory = machine_type.split("-")
            if cpu_series == "n2":
                cpu = cls.CPUSeries.N2
            elif cpu_series == "n2d":
                cpu = cls.CPUSeries.N2D
            elif cpu_series == "e2":
                cpu = cls.CPUSeries.E2
                if cores == "micro":
                    cpu = cls.CPUSeries.E2_MICRO
                    cores = 2
                elif cores == "small":
                    cpu = cls.CPUSeries.E2_SMALL
                    cores = 2
                elif cores == "medium":
                    cpu = cls.CPUSeries.E2_MEDIUM
                    cores = 2
            else:
                raise RuntimeError("Unknown CPU series.")

        cores = int(cores)
        memory = int(memory)

        return cls(zone, cpu, memory, cores)
# </INGREDIENT>
