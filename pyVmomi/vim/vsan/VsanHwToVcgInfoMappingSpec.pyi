# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VsanHwToVcgInfoMapping

class VsanHwToVcgInfoMappingSpec(DynamicData):
   entity: str
   vsanHwToVcgInfoMappings: list[VsanHwToVcgInfoMapping] = []
