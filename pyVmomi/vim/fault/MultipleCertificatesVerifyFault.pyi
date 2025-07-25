# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.fault import HostConnectFault

class MultipleCertificatesVerifyFault(HostConnectFault):
   class ThumbprintData(DynamicData):
      port: int
      thumbprint: str

   thumbprintData: list[ThumbprintData] = []
