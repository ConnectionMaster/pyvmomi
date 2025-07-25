# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.pbm.capability import CapabilityMetadata
from pyVmomi.pbm.capability import PropertyInstance

from pyVmomi.pbm.fault import CompatibilityCheckFault

class PropertyMismatchFault(CompatibilityCheckFault):
   capabilityInstanceId: CapabilityMetadata.UniqueId
   requirementPropertyInstance: PropertyInstance
