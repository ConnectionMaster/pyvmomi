# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.encryption import CryptoKeyId

class CryptoKeyResult(DynamicData):
   keyId: CryptoKeyId
   success: bool
   reason: Optional[str] = None
   fault: Optional[MethodFault] = None
