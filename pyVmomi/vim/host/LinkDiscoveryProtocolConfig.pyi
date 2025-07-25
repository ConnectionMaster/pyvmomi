# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class LinkDiscoveryProtocolConfig(DynamicData):
   class ProtocolType(Enum):
      cdp: ClassVar['ProtocolType'] = 'cdp'
      lldp: ClassVar['ProtocolType'] = 'lldp'

   class OperationType(Enum):
      none: ClassVar['OperationType'] = 'none'
      listen: ClassVar['OperationType'] = 'listen'
      advertise: ClassVar['OperationType'] = 'advertise'
      both: ClassVar['OperationType'] = 'both'

   protocol: str
   operation: str
