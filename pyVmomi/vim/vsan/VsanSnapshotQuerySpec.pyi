# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanSnapshotQuerySpec(DynamicData):
   datastoreUuid: str
   objectUuids: list[str] = []
   snapshotType: Optional[str] = None
   creator: Optional[str] = None
   includeDescriptorPath: Optional[bool] = None
