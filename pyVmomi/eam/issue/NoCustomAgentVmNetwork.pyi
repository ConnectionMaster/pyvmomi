# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import Network

from pyVmomi.eam.issue import NoAgentVmNetwork

class NoCustomAgentVmNetwork(NoAgentVmNetwork):
   customAgentVmNetwork: list[Network] = []
   customAgentVmNetworkName: list[str] = []
