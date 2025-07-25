# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class DnsConfigSpec(DynamicData):
   dhcp: Optional[bool] = None
   hostName: Optional[str] = None
   domainName: Optional[str] = None
   ipAddress: list[str] = []
   searchDomain: list[str] = []
