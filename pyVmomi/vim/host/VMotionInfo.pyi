# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import IpConfig
from pyVmomi.vim.host import VMotionSystem

class VMotionInfo(DynamicData):
   netConfig: Optional[VMotionSystem.NetConfig] = None
   ipConfig: Optional[IpConfig] = None
