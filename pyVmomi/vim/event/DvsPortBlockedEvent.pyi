# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.dvs import DistributedVirtualPort

from pyVmomi.vim.event import DvsEvent

class DvsPortBlockedEvent(DvsEvent):
   portKey: str
   statusDetail: Optional[str] = None
   runtimeInfo: Optional[DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: Optional[str] = None
