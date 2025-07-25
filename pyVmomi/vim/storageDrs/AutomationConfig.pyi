# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class AutomationConfig(DynamicData):
   spaceLoadBalanceAutomationMode: Optional[str] = None
   ioLoadBalanceAutomationMode: Optional[str] = None
   ruleEnforcementAutomationMode: Optional[str] = None
   policyEnforcementAutomationMode: Optional[str] = None
   vmEvacuationAutomationMode: Optional[str] = None
