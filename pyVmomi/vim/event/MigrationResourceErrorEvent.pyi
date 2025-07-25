# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.event import HostEventArgument
from pyVmomi.vim.event import MigrationEvent
from pyVmomi.vim.event import ResourcePoolEventArgument

class MigrationResourceErrorEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument
