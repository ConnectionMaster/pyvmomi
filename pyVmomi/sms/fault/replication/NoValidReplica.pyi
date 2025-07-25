# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.sms.fault.replication import ReplicationFault

from pyVmomi.sms.storage.replication import DeviceId

class NoValidReplica(ReplicationFault):
   deviceId: Optional[DeviceId] = None
