# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

class VsanHostVirtualApplianceInfo(DynamicData):
   hostKey: HostSystem
   isVirtualApp: bool
   isDeployedFromOVF: Optional[bool] = None
