# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from pyVmomi.vmodl.fault import NotEnoughLicenses

class ExpiredFeatureLicense(NotEnoughLicenses):
   feature: str
   count: int
   expirationDate: datetime
