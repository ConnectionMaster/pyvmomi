# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Network
from pyVmomi.vim import Task

from pyVmomi.vim.vsan import FileServiceDomain
from pyVmomi.vim.vsan import FileServiceDomainConfig
from pyVmomi.vim.vsan import FileServiceDomainQuerySpec
from pyVmomi.vim.vsan import FileShareConfig
from pyVmomi.vim.vsan import FileShareQueryResult
from pyVmomi.vim.vsan import FileShareQuerySpec
from pyVmomi.vim.vsan import FileShareSnapshotConfig
from pyVmomi.vim.vsan import FileShareSnapshotQueryResult
from pyVmomi.vim.vsan import FileShareSnapshotQuerySpec
from pyVmomi.vim.vsan import VsanFileServiceOvfSpec
from pyVmomi.vim.vsan import VsanFileServicePreflightCheckResult

class VsanFileServiceSystem(ManagedObject):
   def DownloadFileServiceOvf(self, downloadUrl: str) -> Task: ...
   def QueryFileServiceOvfs(self) -> list[VsanFileServiceOvfSpec]: ...
   def FindOvfDownloadUrl(self, cluster: ClusterComputeResource) -> str: ...
   def PerformFileServicePreflightCheck(self, cluster: ClusterComputeResource, domainConfig: Optional[FileServiceDomainConfig], network: Optional[Network], scope: Optional[str], domainUuid: Optional[str]) -> VsanFileServicePreflightCheckResult: ...
   def CreateFileServiceDomain(self, domainConfig: FileServiceDomainConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def ReconfigureFileServiceDomain(self, domainUuid: str, domainConfig: FileServiceDomainConfig, cluster: Optional[ClusterComputeResource], deleteDomainConfigFields: list[str]) -> Task: ...
   def RemoveFileServiceDomain(self, domainUuid: str, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def QueryFileServiceDomains(self, querySpec: Optional[FileServiceDomainQuerySpec], cluster: Optional[ClusterComputeResource]) -> list[FileServiceDomain]: ...
   def CreateFileShare(self, config: FileShareConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def ReconfigureFileShare(self, shareUuid: str, config: FileShareConfig, cluster: Optional[ClusterComputeResource], deleteLabelKeys: list[str], force: Optional[bool]) -> Task: ...
   def RemoveFileShare(self, shareUuid: str, cluster: Optional[ClusterComputeResource], force: Optional[bool]) -> Task: ...
   def QueryFileShares(self, querySpec: FileShareQuerySpec, cluster: Optional[ClusterComputeResource]) -> Optional[FileShareQueryResult]: ...
   def UpgradeFsvm(self, cluster: ClusterComputeResource) -> Task: ...
   def RebalanceFileService(self, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def CreateFileShareSnapshot(self, config: FileShareSnapshotConfig, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def RemoveFileShareSnapshot(self, shareUuid: str, snapshotName: str, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def QueryFileShareSnapshots(self, querySpec: FileShareSnapshotQuerySpec, cluster: Optional[ClusterComputeResource]) -> Optional[FileShareSnapshotQueryResult]: ...
