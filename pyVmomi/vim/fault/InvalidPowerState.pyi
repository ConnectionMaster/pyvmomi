# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import InvalidState

class InvalidPowerState(InvalidState):
   requestedState: Optional[VirtualMachine.PowerState] = None
   existingState: VirtualMachine.PowerState
