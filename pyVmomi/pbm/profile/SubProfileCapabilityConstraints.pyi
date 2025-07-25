# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.capability import CapabilityInstance

from pyVmomi.pbm.profile import CapabilityConstraints

class SubProfileCapabilityConstraints(CapabilityConstraints):
   class SubProfile(DynamicData):
      name: str
      capability: list[CapabilityInstance] = []
      forceProvision: Optional[bool] = None

   subProfiles: list[SubProfile] = []
