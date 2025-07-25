# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.event import AuthorizationEvent
from pyVmomi.vim.event import ManagedEntityEventArgument

class PermissionEvent(AuthorizationEvent):
   entity: ManagedEntityEventArgument
   principal: str
   group: bool
