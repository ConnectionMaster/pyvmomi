# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from .VmomiSupport import CreateDataType, CreateManagedType
from .VmomiSupport import CreateEnumType
from .VmomiSupport import AddVersion, AddVersionParent
from .VmomiSupport import AddBreakingChangesInfo
from .VmomiSupport import F_LINK, F_LINKABLE
from .VmomiSupport import F_OPTIONAL, F_SECRET

AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version4", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version3", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version2", "", "", 0, "vim25")
AddVersion("vmodl.query.version.version1", "", "", 0, "vim25")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version4")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version4", "vmodl.version.version2")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version4", "vmodl.query.version.version1")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version3", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version3")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version3", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version2")
AddVersionParent("vmodl.query.version.version2", "vmodl.query.version.version1")
AddVersionParent("vmodl.query.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.query.version.version1", "vmodl.query.version.version1")

from .VmomiSupport import newestVersions
newestVersions.Add("vmodl.query.version.version4")

from .VmomiSupport import ltsVersions
ltsVersions.Add("vmodl.query.version.version4")

from .VmomiSupport import oldestVersions
oldestVersions.Add("vmodl.query.version.version1")

CreateDataType("vmodl.query.InvalidCollectorVersion", "InvalidCollectorVersion", "vmodl.MethodFault", "vmodl.query.version.version1", None)
CreateDataType("vmodl.query.InvalidProperty", "InvalidProperty", "vmodl.MethodFault", "vmodl.query.version.version1", [("name", "vmodl.PropertyPath", "vmodl.query.version.version1", 0)])
CreateManagedType("vmodl.query.PropertyCollector", "PropertyCollector", "vmodl.ManagedObject", "vmodl.query.version.version1", [("filter", "vmodl.query.PropertyCollector.Filter[]", "vmodl.query.version.version1", F_OPTIONAL, "System.View")], [("createFilter", "CreateFilter", "vmodl.query.version.version1", (("spec", "vmodl.query.PropertyCollector.FilterSpec", "vmodl.query.version.version1", 0, None),("partialUpdates", "boolean", "vmodl.query.version.version1", 0, None),), (0, "vmodl.query.PropertyCollector.Filter", "vmodl.query.PropertyCollector.Filter"), "System.View", ["vmodl.query.InvalidProperty", ]), ("retrieveContents", "RetrieveProperties", "vmodl.query.version.version1", (("specSet", "vmodl.query.PropertyCollector.FilterSpec[]", "vmodl.query.version.version1", 0, None),), (F_OPTIONAL, "vmodl.query.PropertyCollector.ObjectContent[]", "vmodl.query.PropertyCollector.ObjectContent[]"), "System.Anonymous", ["vmodl.query.InvalidProperty", ]), ("checkForUpdates", "CheckForUpdates", "vmodl.query.version.version1", (("version", "string", "vmodl.query.version.version1", F_OPTIONAL, None),), (F_OPTIONAL, "vmodl.query.PropertyCollector.UpdateSet", "vmodl.query.PropertyCollector.UpdateSet"), "System.View", ["vmodl.query.InvalidCollectorVersion", ]), ("waitForUpdates", "WaitForUpdates", "vmodl.query.version.version1", (("version", "string", "vmodl.query.version.version1", F_OPTIONAL, None),), (0, "vmodl.query.PropertyCollector.UpdateSet", "vmodl.query.PropertyCollector.UpdateSet"), "System.View", ["vmodl.query.InvalidCollectorVersion", ]), ("cancelWaitForUpdates", "CancelWaitForUpdates", "vmodl.query.version.version1", (), (0, "void", "void"), "System.View", None), ("waitForUpdatesEx", "WaitForUpdatesEx", "vmodl.query.version.version3", (("version", "string", "vmodl.query.version.version3", F_OPTIONAL, None),("options", "vmodl.query.PropertyCollector.WaitOptions", "vmodl.query.version.version3", F_OPTIONAL, None),), (F_OPTIONAL, "vmodl.query.PropertyCollector.UpdateSet", "vmodl.query.PropertyCollector.UpdateSet"), "System.View", ["vmodl.query.InvalidCollectorVersion", ]), ("retrievePropertiesEx", "RetrievePropertiesEx", "vmodl.query.version.version3", (("specSet", "vmodl.query.PropertyCollector.FilterSpec[]", "vmodl.query.version.version3", 0, None),("options", "vmodl.query.PropertyCollector.RetrieveOptions", "vmodl.query.version.version3", 0, None),), (F_OPTIONAL, "vmodl.query.PropertyCollector.RetrieveResult", "vmodl.query.PropertyCollector.RetrieveResult"), "System.Anonymous", ["vmodl.query.InvalidProperty", ]), ("continueRetrievePropertiesEx", "ContinueRetrievePropertiesEx", "vmodl.query.version.version3", (("token", "string", "vmodl.query.version.version3", 0, None),), (0, "vmodl.query.PropertyCollector.RetrieveResult", "vmodl.query.PropertyCollector.RetrieveResult"), "System.View", ["vmodl.query.InvalidProperty", ]), ("cancelRetrievePropertiesEx", "CancelRetrievePropertiesEx", "vmodl.query.version.version3", (("token", "string", "vmodl.query.version.version3", 0, None),), (0, "void", "void"), "System.View", ["vmodl.query.InvalidProperty", ]), ("createPropertyCollector", "CreatePropertyCollector", "vmodl.query.version.version3", (), (0, "vmodl.query.PropertyCollector", "vmodl.query.PropertyCollector"), "System.View", None), ("destroy", "DestroyPropertyCollector", "vmodl.query.version.version3", (), (0, "void", "void"), "System.View", None)])
CreateDataType("vmodl.query.PropertyCollector.FilterSpec", "PropertyFilterSpec", "vmodl.DynamicData", "vmodl.query.version.version1", [("propSet", "vmodl.query.PropertyCollector.PropertySpec[]", "vmodl.query.version.version1", 0), ("objectSet", "vmodl.query.PropertyCollector.ObjectSpec[]", "vmodl.query.version.version1", 0), ("reportMissingObjectsInResults", "boolean", "vmodl.query.version.version3", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.PropertySpec", "PropertySpec", "vmodl.DynamicData", "vmodl.query.version.version1", [("type", "vmodl.TypeName", "vmodl.query.version.version1", 0), ("all", "boolean", "vmodl.query.version.version1", F_OPTIONAL), ("pathSet", "vmodl.PropertyPath[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.ObjectSpec", "ObjectSpec", "vmodl.DynamicData", "vmodl.query.version.version1", [("obj", "vmodl.ManagedObject", "vmodl.query.version.version1", 0), ("skip", "boolean", "vmodl.query.version.version1", F_OPTIONAL), ("selectSet", "vmodl.query.PropertyCollector.SelectionSpec[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.SelectionSpec", "SelectionSpec", "vmodl.DynamicData", "vmodl.query.version.version1", [("name", "string", "vmodl.query.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.TraversalSpec", "TraversalSpec", "vmodl.query.PropertyCollector.SelectionSpec", "vmodl.query.version.version1", [("type", "vmodl.TypeName", "vmodl.query.version.version1", 0), ("path", "vmodl.PropertyPath", "vmodl.query.version.version1", 0), ("skip", "boolean", "vmodl.query.version.version1", F_OPTIONAL), ("selectSet", "vmodl.query.PropertyCollector.SelectionSpec[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateManagedType("vmodl.query.PropertyCollector.Filter", "PropertyFilter", "vmodl.ManagedObject", "vmodl.query.version.version1", [("spec", "vmodl.query.PropertyCollector.FilterSpec", "vmodl.query.version.version1", 0, None), ("partialUpdates", "boolean", "vmodl.query.version.version1", 0, None)], [("destroy", "DestroyPropertyFilter", "vmodl.query.version.version1", (), (0, "void", "void"), None, None)])
CreateDataType("vmodl.query.PropertyCollector.ObjectContent", "ObjectContent", "vmodl.DynamicData", "vmodl.query.version.version1", [("obj", "vmodl.ManagedObject", "vmodl.query.version.version1", 0), ("propSet", "vmodl.DynamicProperty[]", "vmodl.query.version.version1", F_OPTIONAL), ("missingSet", "vmodl.query.PropertyCollector.MissingProperty[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.UpdateSet", "UpdateSet", "vmodl.DynamicData", "vmodl.query.version.version1", [("version", "string", "vmodl.query.version.version1", 0), ("filterSet", "vmodl.query.PropertyCollector.FilterUpdate[]", "vmodl.query.version.version1", F_OPTIONAL), ("truncated", "boolean", "vmodl.query.version.version3", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.FilterUpdate", "PropertyFilterUpdate", "vmodl.DynamicData", "vmodl.query.version.version1", [("filter", "vmodl.query.PropertyCollector.Filter", "vmodl.query.version.version1", 0), ("objectSet", "vmodl.query.PropertyCollector.ObjectUpdate[]", "vmodl.query.version.version1", F_OPTIONAL), ("missingSet", "vmodl.query.PropertyCollector.MissingObject[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.ObjectUpdate", "ObjectUpdate", "vmodl.DynamicData", "vmodl.query.version.version1", [("kind", "vmodl.query.PropertyCollector.ObjectUpdate.Kind", "vmodl.query.version.version1", 0), ("obj", "vmodl.ManagedObject", "vmodl.query.version.version1", 0), ("changeSet", "vmodl.query.PropertyCollector.Change[]", "vmodl.query.version.version1", F_OPTIONAL), ("missingSet", "vmodl.query.PropertyCollector.MissingProperty[]", "vmodl.query.version.version1", F_OPTIONAL)])
CreateEnumType("vmodl.query.PropertyCollector.ObjectUpdate.Kind", "ObjectUpdateKind", "vmodl.query.version.version1", ["modify", "enter", "leave"])
CreateDataType("vmodl.query.PropertyCollector.Change", "PropertyChange", "vmodl.DynamicData", "vmodl.query.version.version1", [("name", "vmodl.PropertyPath", "vmodl.query.version.version1", 0), ("op", "vmodl.query.PropertyCollector.Change.Op", "vmodl.query.version.version1", 0), ("val", "anyType", "vmodl.query.version.version1", F_OPTIONAL)])
CreateEnumType("vmodl.query.PropertyCollector.Change.Op", "PropertyChangeOp", "vmodl.query.version.version1", ["add", "remove", "assign", "indirectRemove"])
CreateDataType("vmodl.query.PropertyCollector.MissingProperty", "MissingProperty", "vmodl.DynamicData", "vmodl.query.version.version1", [("path", "vmodl.PropertyPath", "vmodl.query.version.version1", 0), ("fault", "vmodl.MethodFault", "vmodl.query.version.version1", 0)])
CreateDataType("vmodl.query.PropertyCollector.MissingObject", "MissingObject", "vmodl.DynamicData", "vmodl.query.version.version1", [("obj", "vmodl.ManagedObject", "vmodl.query.version.version1", 0), ("fault", "vmodl.MethodFault", "vmodl.query.version.version1", 0)])
CreateDataType("vmodl.query.PropertyCollector.WaitOptions", "WaitOptions", "vmodl.DynamicData", "vmodl.query.version.version3", [("maxWaitSeconds", "int", "vmodl.query.version.version3", F_OPTIONAL), ("maxObjectUpdates", "int", "vmodl.query.version.version3", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.RetrieveOptions", "RetrieveOptions", "vmodl.DynamicData", "vmodl.query.version.version3", [("maxObjects", "int", "vmodl.query.version.version3", F_OPTIONAL)])
CreateDataType("vmodl.query.PropertyCollector.RetrieveResult", "RetrieveResult", "vmodl.DynamicData", "vmodl.query.version.version3", [("token", "string", "vmodl.query.version.version3", F_OPTIONAL), ("objects", "vmodl.query.PropertyCollector.ObjectContent[]", "vmodl.query.version.version3", 0)])
