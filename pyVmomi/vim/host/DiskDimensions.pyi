# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class DiskDimensions(DynamicData):
   class Chs(DynamicData):
      cylinder: long
      head: int
      sector: int

   class Lba(DynamicData):
      blockSize: int
      block: long
