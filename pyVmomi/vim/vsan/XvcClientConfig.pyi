# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan import DatastoreSpec
from pyVmomi.vim.vsan import XVCClientInfo

class XvcClientConfig(DatastoreSpec):
   xvcClusters: list[XVCClientInfo] = []
