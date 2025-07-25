# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.cns import FileCreateSpec

from pyVmomi.vim.vsan import FileShareNetPermission

class VSANFileCreateSpec(FileCreateSpec):
   softQuotaInMb: Optional[long] = None
   permission: list[FileShareNetPermission] = []
