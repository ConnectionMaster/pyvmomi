# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import Timedout

class PowerOnFtSecondaryTimedout(Timedout):
   vm: VirtualMachine
   vmName: str
   timeout: int
