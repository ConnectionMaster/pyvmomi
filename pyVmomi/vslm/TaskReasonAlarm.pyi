# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import ManagedEntity

from pyVmomi.vslm import TaskReason

from pyVmomi.vim.alarm import Alarm

class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: Alarm
   entityName: str
   entity: ManagedEntity
