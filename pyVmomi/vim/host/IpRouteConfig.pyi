# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class IpRouteConfig(DynamicData):
   defaultGateway: Optional[str] = None
   gatewayDevice: Optional[str] = None
   ipV6DefaultGateway: Optional[str] = None
   ipV6GatewayDevice: Optional[str] = None
