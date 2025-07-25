# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.action import Action

from pyVmomi.vim.scheduler import TaskScheduler

class ScheduledTaskSpec(DynamicData):
   name: str
   description: str
   enabled: bool
   scheduler: TaskScheduler
   action: Action
   notification: Optional[str] = None
