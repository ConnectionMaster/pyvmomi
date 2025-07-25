# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.pbm.placement import PlacementHub

from pyVmomi.pbm.profile import CapabilityBasedProfileCreateSpec
from pyVmomi.pbm.profile import CapabilityBasedProfileUpdateSpec
from pyVmomi.pbm.profile import DefaultProfileInfo
from pyVmomi.pbm.profile import Profile
from pyVmomi.pbm.profile import ProfileId
from pyVmomi.pbm.profile import ProfileOperationOutcome
from pyVmomi.pbm.profile import QueryProfileResult
from pyVmomi.pbm.profile import ResourceType

from pyVmomi.pbm.capability.provider import CapabilityObjectMetadataPerCategory
from pyVmomi.pbm.capability.provider import CapabilityObjectSchema

from pyVmomi.pbm.profile.provider import DatastoreSpaceStatistics

class ProfileManager(ManagedObject):
   def FetchResourceType(self) -> list[ResourceType]: ...
   def FetchVendorInfo(self, resourceType: Optional[ResourceType]) -> list[CapabilityObjectSchema.VendorResourceTypeInfo]: ...
   def FetchCapabilityMetadata(self, resourceType: Optional[ResourceType], vendorUuid: Optional[str]) -> list[CapabilityObjectMetadataPerCategory]: ...
   def FetchCapabilitySchema(self, vendorUuid: Optional[str], lineOfService: list[str]) -> list[CapabilityObjectSchema]: ...
   def Create(self, createSpec: CapabilityBasedProfileCreateSpec) -> ProfileId: ...
   def Update(self, profileId: ProfileId, updateSpec: CapabilityBasedProfileUpdateSpec) -> NoReturn: ...
   def Delete(self, profileId: list[ProfileId]) -> list[ProfileOperationOutcome]: ...
   def QueryProfile(self, resourceType: ResourceType, profileCategory: Optional[str]) -> list[ProfileId]: ...
   def RetrieveContent(self, profileIds: list[ProfileId]) -> list[Profile]: ...
   def QueryAssociatedProfiles(self, entities: list[ServerObjectRef]) -> list[QueryProfileResult]: ...
   def QueryAssociatedProfile(self, entity: ServerObjectRef) -> list[ProfileId]: ...
   def QueryAssociatedEntity(self, profile: ProfileId, entityType: Optional[str]) -> list[ServerObjectRef]: ...
   def QueryDefaultRequirementProfile(self, hub: PlacementHub) -> Optional[ProfileId]: ...
   def ResetDefaultRequirementProfile(self, profile: Optional[ProfileId]) -> NoReturn: ...
   def AssignDefaultRequirementProfile(self, profile: ProfileId, datastores: list[PlacementHub]) -> NoReturn: ...
   def FindApplicableDefaultProfile(self, datastores: list[PlacementHub]) -> list[Profile]: ...
   def QueryDefaultRequirementProfiles(self, datastores: list[PlacementHub]) -> list[DefaultProfileInfo]: ...
   def ResetVSanDefaultProfile(self) -> NoReturn: ...
   def QuerySpaceStatsForStorageContainer(self, datastore: ServerObjectRef, capabilityProfileId: list[ProfileId]) -> list[DatastoreSpaceStatistics]: ...
   def QueryAssociatedEntities(self, profiles: list[ProfileId]) -> list[QueryProfileResult]: ...
