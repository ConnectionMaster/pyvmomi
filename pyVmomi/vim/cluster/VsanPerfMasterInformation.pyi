# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanPerfMasterInformation(DynamicData):
   secSinceLastStatsWrite: Optional[long] = None
   secSinceLastStatsCollect: Optional[long] = None
   statsIntervalSec: long
   collectionFailureHostUuids: list[str] = []
   renamedStatsDirectories: list[str] = []
   statsDirectoryPercentFree: Optional[long] = None
   verboseMode: Optional[bool] = None
   verboseModeLastUpdate: Optional[datetime] = None
