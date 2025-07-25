# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vsan.host import ConfigInfo

class PortConfigEx(ConfigInfo.NetworkInfo.PortConfig):
   class TrafficType(Enum):
      vsan: ClassVar['TrafficType'] = 'vsan'
      witness: ClassVar['TrafficType'] = 'witness'
      TrafficType_Unknown: ClassVar['TrafficType'] = 'TrafficType_Unknown'

   class TrafficType90(Enum):
      vsanExternal: ClassVar['TrafficType90'] = 'vsanExternal'

   trafficTypes: list[str] = []
