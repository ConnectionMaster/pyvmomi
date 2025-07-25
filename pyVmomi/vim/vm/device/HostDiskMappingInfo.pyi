# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class HostDiskMappingInfo(DynamicData):
   class PartitionInfo(DynamicData):
      name: str
      fileSystem: str
      capacityInKb: long

   physicalPartition: Optional[PartitionInfo] = None
   name: str
   exclusive: Optional[bool] = None
