# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanHostHealthSystemVersionResult

class VsanClusterHealthSystemVersionResult(DynamicData):
   hostResults: list[VsanHostHealthSystemVersionResult] = []
   vcVersion: Optional[str] = None
   issueFound: bool
   upgradePossible: Optional[bool] = None
   vcBuild: Optional[str] = None
