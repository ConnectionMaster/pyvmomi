# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.encryption import CryptoKeyId

class CryptoKeyPlain(DynamicData):
   keyId: CryptoKeyId
   algorithm: str
   keyData: str
