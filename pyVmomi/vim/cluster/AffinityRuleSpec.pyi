# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import RuleInfo

class AffinityRuleSpec(RuleInfo):
   vm: list[VirtualMachine] = []
