# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vim.profile import Expression

class SimpleExpression(Expression):
   expressionType: str
   parameter: list[KeyAnyValue] = []
