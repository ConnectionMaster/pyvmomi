# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanPerfMetricSeriesCSV

class VsanPerfEntityMetricCSV(DynamicData):
   entityRefId: str
   sampleInfo: Optional[str] = None
   value: list[VsanPerfMetricSeriesCSV] = []
