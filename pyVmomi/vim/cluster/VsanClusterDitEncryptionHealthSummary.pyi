# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanDitEncryptionHealthSummary

class VsanClusterDitEncryptionHealthSummary(DynamicData):
   overallHealth: str
   enabled: Optional[bool] = None
   hostResults: list[VsanDitEncryptionHealthSummary] = []
