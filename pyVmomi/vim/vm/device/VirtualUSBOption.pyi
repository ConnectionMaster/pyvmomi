# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualUSBOption(VirtualDeviceOption):
   class USBBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteHostBackingOption(VirtualDeviceOption.DeviceBackingOption):
      pass

   class RemoteClientBackingOption(VirtualDeviceOption.RemoteDeviceBackingOption):
      pass
