# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.event import AlarmEvent
from pyVmomi.vim.event import ManagedEntityEventArgument

class AlarmSnmpFailedEvent(AlarmEvent):
   entity: ManagedEntityEventArgument
   reason: MethodFault
