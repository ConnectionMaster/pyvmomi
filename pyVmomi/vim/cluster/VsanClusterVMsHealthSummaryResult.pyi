# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanClusterVMsHealthSummaryResult(DynamicData):
   numVMs: int
   state: Optional[str] = None
   health: str
   vmInstanceUuids: list[str] = []
