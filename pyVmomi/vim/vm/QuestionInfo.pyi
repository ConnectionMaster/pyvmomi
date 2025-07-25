# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import ChoiceOption

from pyVmomi.vim.vm import Message

class QuestionInfo(DynamicData):
   id: str
   text: str
   choice: ChoiceOption
   message: list[Message] = []
