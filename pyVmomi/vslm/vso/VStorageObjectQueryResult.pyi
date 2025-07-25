# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vslm import ID

from pyVmomi.vslm.vso import VStorageObjectResult

class VStorageObjectQueryResult(DynamicData):
   allRecordsReturned: bool
   id: list[ID] = []
   queryResults: list[VStorageObjectResult] = []
