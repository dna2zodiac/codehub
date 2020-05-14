from enum import Enum

class vim(object): # (unknown name)

   class AboutInfo(vmodl.DynamicData): # vim.AboutInfo
      name = ""
      fullName = ""
      vendor = ""
      version = ""
      build = ""
      localeVersion = ""
      localeBuild = ""
      osType = ""
      productLineId = ""
      apiType = ""
      apiVersion = ""
      instanceUuid = ""
      licenseProductName = ""
      licenseProductVersion = ""

   class AuthorizationDescription(vmodl.DynamicData): # vim.AuthorizationDescription
      privilege = [ vim.ElementDescription() ]
      privilegeGroup = [ vim.ElementDescription() ]

   class BatchResult(vmodl.DynamicData): # vim.BatchResult
      result = ""
      hostKey = ""
      ds = vim.Datastore()
      fault = vmodl.MethodFault()

      class Result(Enum): # vim.BatchResult.Result
         success = 0
         fail = 1

   class Capability(vmodl.DynamicData): # vim.Capability
      provisioningSupported = False
      multiHostSupported = False
      userShellAccessSupported = False
      supportedEVCMode = [ vim.EVCMode() ]
      networkBackupAndRestoreSupported = False
      ftDrsWithoutEvcSupported = False
      hciWorkflowSupported = False
      computePolicyVersion = 0
      clusterPlacementSupported = False
      lifecycleManagementSupported = False
      scalableSharesSupported = False

   class CertificateManager(vmodl.ManagedObject): # vim.CertificateManager

      def refreshCACertificatesAndCRLs(host=[ vim.HostSystem() ]): # vim.CertificateManager.refreshCACertificatesAndCRLs
         return vim.Task()

      def refreshCertificates(host=[ vim.HostSystem() ]): # vim.CertificateManager.refreshCertificates
         return vim.Task()

      def revokeCertificates(host=[ vim.HostSystem() ]): # vim.CertificateManager.revokeCertificates
         return vim.Task()

   class ConfigSpecOperation(Enum): # vim.ConfigSpecOperation
      add = 0
      edit = 1
      remove = 2

   class CustomFieldsManager(vmodl.ManagedObject): # vim.CustomFieldsManager
      field = [ vim.CustomFieldsManager.FieldDef() ]

      def addFieldDefinition(name="", moType=vmodl.TypeName() or None, fieldDefPolicy=vim.PrivilegePolicyDef() or None, fieldPolicy=vim.PrivilegePolicyDef() or None): # vim.CustomFieldsManager.addFieldDefinition
         # throws vim.fault.DuplicateName, vim.fault.InvalidPrivilege
         return vim.CustomFieldsManager.FieldDef()

      def removeFieldDefinition(key=0): # vim.CustomFieldsManager.removeFieldDefinition
         return None

      def renameFieldDefinition(key=0, name=""): # vim.CustomFieldsManager.renameFieldDefinition
         # throws vim.fault.DuplicateName
         return None

      def setField(entity=vim.ManagedEntity(), key=0, value=""): # vim.CustomFieldsManager.setField
         return None

      class FieldDef(vmodl.DynamicData): # vim.CustomFieldsManager.FieldDef
         key = 0
         name = ""
         type = vmodl.TypeName()
         managedObjectType = vmodl.TypeName()
         fieldDefPrivileges = vim.PrivilegePolicyDef()
         fieldInstancePrivileges = vim.PrivilegePolicyDef()

      class Value(vmodl.DynamicData): # vim.CustomFieldsManager.Value
         key = 0

      class StringValue(vim.CustomFieldsManager.Value): # vim.CustomFieldsManager.StringValue
         value = ""

   class CustomizationSpecInfo(vmodl.DynamicData): # vim.CustomizationSpecInfo
      name = ""
      description = ""
      type = ""
      changeVersion = ""
      lastUpdateTime = vmodl.DateTime()

   class CustomizationSpecItem(vmodl.DynamicData): # vim.CustomizationSpecItem
      info = vim.CustomizationSpecInfo()
      spec = vim.vm.customization.Specification()

   class CustomizationSpecManager(vmodl.ManagedObject): # vim.CustomizationSpecManager
      info = [ vim.CustomizationSpecInfo() ]
      encryptionKey = [ 0x00 ]

      def exists(name=""): # vim.CustomizationSpecManager.exists
         return False

      def get(name=""): # vim.CustomizationSpecManager.get
         # throws vim.fault.NotFound
         return vim.CustomizationSpecItem()

      def create(item=vim.CustomizationSpecItem()): # vim.CustomizationSpecManager.create
         # throws vim.fault.CustomizationFault, vim.fault.AlreadyExists
         return None

      def overwrite(item=vim.CustomizationSpecItem()): # vim.CustomizationSpecManager.overwrite
         # throws vim.fault.CustomizationFault, vim.fault.NotFound, vim.fault.ConcurrentAccess
         return None

      def delete(name=""): # vim.CustomizationSpecManager.delete
         # throws vim.fault.NotFound
         return None

      def duplicate(name="", newName=""): # vim.CustomizationSpecManager.duplicate
         # throws vim.fault.NotFound, vim.fault.AlreadyExists
         return None

      def rename(name="", newName=""): # vim.CustomizationSpecManager.rename
         # throws vim.fault.NotFound, vim.fault.AlreadyExists
         return None

      def specItemToXml(item=vim.CustomizationSpecItem()): # vim.CustomizationSpecManager.specItemToXml
         return ""

      def xmlToSpecItem(specItemXml=""): # vim.CustomizationSpecManager.xmlToSpecItem
         # throws vim.fault.CustomizationFault
         return vim.CustomizationSpecItem()

      def checkResources(guestOs=""): # vim.CustomizationSpecManager.checkResources
         # throws vim.fault.CustomizationFault
         return None

   class DatastoreNamespaceManager(vmodl.ManagedObject): # vim.DatastoreNamespaceManager

      def CreateDirectory(datastore=vim.Datastore(), displayName="" or None, policy="" or None): # vim.DatastoreNamespaceManager.CreateDirectory
         # throws vim.fault.CannotCreateFile, vim.fault.FileAlreadyExists, vim.fault.InvalidDatastore
         return ""

      def DeleteDirectory(datacenter=vim.Datacenter() or None, datastorePath=""): # vim.DatastoreNamespaceManager.DeleteDirectory
         # throws vim.fault.FileFault, vim.fault.FileNotFound, vim.fault.InvalidDatastore, vim.fault.InvalidDatastorePath
         return None

      def ConvertNamespacePathToUuidPath(datacenter=vim.Datacenter() or None, namespaceUrl=""): # vim.DatastoreNamespaceManager.ConvertNamespacePathToUuidPath
         # throws vim.fault.InvalidDatastore, vim.fault.InvalidDatastorePath
         return ""

   class Description(vmodl.DynamicData): # vim.Description
      label = ""
      summary = ""

   class DesiredSoftwareSpec(vmodl.DynamicData): # vim.DesiredSoftwareSpec
      baseImageSpec = vim.DesiredSoftwareSpec.BaseImageSpec()
      vendorAddOnSpec = vim.DesiredSoftwareSpec.VendorAddOnSpec()

      class BaseImageSpec(vmodl.DynamicData): # vim.DesiredSoftwareSpec.BaseImageSpec
         version = ""

      class VendorAddOnSpec(vmodl.DynamicData): # vim.DesiredSoftwareSpec.VendorAddOnSpec
         name = ""
         version = ""

   class DiagnosticManager(vmodl.ManagedObject): # vim.DiagnosticManager

      def queryDescriptions(host=vim.HostSystem() or None): # vim.DiagnosticManager.queryDescriptions
         return [ vim.DiagnosticManager.LogDescriptor() ]

      def browse(host=vim.HostSystem() or None, key="", start=0 or None, lines=0 or None): # vim.DiagnosticManager.browse
         # throws vim.fault.CannotAccessFile
         return vim.DiagnosticManager.LogHeader()

      def generateLogBundles(includeDefault=False, host=[ vim.HostSystem() ] or None): # vim.DiagnosticManager.generateLogBundles
         # throws vim.fault.LogBundlingFailed, vim.fault.TaskInProgress
         return vim.Task()

      class LogDescriptor(vmodl.DynamicData): # vim.DiagnosticManager.LogDescriptor
         key = ""
         fileName = ""
         creator = ""
         format = ""
         mimeType = ""
         info = vim.Description()

         class Creator(Enum): # vim.DiagnosticManager.LogDescriptor.Creator
            vpxd = 0
            vpxa = 1
            hostd = 2
            serverd = 3
            install = 4
            vpxClient = 5
            recordLog = 6

         class Format(Enum): # vim.DiagnosticManager.LogDescriptor.Format
            plain = 0

      class LogHeader(vmodl.DynamicData): # vim.DiagnosticManager.LogHeader
         lineStart = 0
         lineEnd = 0
         lineText = [ "" ]

      class BundleInfo(vmodl.DynamicData): # vim.DiagnosticManager.BundleInfo
         system = vim.HostSystem()
         url = ""

   class DrsStatsManager(object): # (unknown name)

      class InjectorWorkload(object): # (unknown name)

         class CorrelationState(Enum): # vim.DrsStatsManager.InjectorWorkload.CorrelationState
            Correlated = 0
            Uncorrelated = 1

   class ElementDescription(vim.Description): # vim.ElementDescription
      key = ""

   class EnumDescription(vmodl.DynamicData): # vim.EnumDescription
      key = vmodl.TypeName()
      tags = [ vim.ElementDescription() ]

   class EnvironmentBrowser(vmodl.ManagedObject): # vim.EnvironmentBrowser
      datastoreBrowser = vim.host.DatastoreBrowser()

      def queryConfigOptionDescriptor(): # vim.EnvironmentBrowser.queryConfigOptionDescriptor
         return [ vim.vm.ConfigOptionDescriptor() ]

      def queryConfigOption(key="" or None, host=vim.HostSystem() or None): # vim.EnvironmentBrowser.queryConfigOption
         return vim.vm.ConfigOption()

      def queryConfigOptionEx(spec=vim.EnvironmentBrowser.ConfigOptionQuerySpec() or None): # vim.EnvironmentBrowser.queryConfigOptionEx
         return vim.vm.ConfigOption()

      def queryConfigTarget(host=vim.HostSystem() or None): # vim.EnvironmentBrowser.queryConfigTarget
         return vim.vm.ConfigTarget()

      def queryTargetCapabilities(host=vim.HostSystem() or None): # vim.EnvironmentBrowser.queryTargetCapabilities
         return vim.host.Capability()

      class ConfigOptionQuerySpec(vmodl.DynamicData): # vim.EnvironmentBrowser.ConfigOptionQuerySpec
         key = ""
         host = vim.HostSystem()
         guestId = [ "" ]

   class ExtendedDescription(vim.Description): # vim.ExtendedDescription
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ExtendedElementDescription(vim.ElementDescription): # vim.ExtendedElementDescription
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ExtensibleManagedObject(vmodl.ManagedObject): # vim.ExtensibleManagedObject
      value = [ vim.CustomFieldsManager.Value() ]
      availableField = [ vim.CustomFieldsManager.FieldDef() ]

      def setCustomValue(key="", value=""): # vim.ExtensibleManagedObject.setCustomValue
         return None

   class Extension(vmodl.DynamicData): # vim.Extension
      description = vim.Description()
      key = ""
      company = ""
      type = ""
      version = ""
      subjectName = ""
      server = [ vim.Extension.ServerInfo() ]
      client = [ vim.Extension.ClientInfo() ]
      taskList = [ vim.Extension.TaskTypeInfo() ]
      eventList = [ vim.Extension.EventTypeInfo() ]
      faultList = [ vim.Extension.FaultTypeInfo() ]
      privilegeList = [ vim.Extension.PrivilegeInfo() ]
      resourceList = [ vim.Extension.ResourceInfo() ]
      lastHeartbeatTime = vmodl.DateTime()
      healthInfo = vim.Extension.HealthInfo()
      ovfConsumerInfo = vim.Extension.OvfConsumerInfo()
      extendedProductInfo = vim.ext.ExtendedProductInfo()
      managedEntityInfo = [ vim.ext.ManagedEntityInfo() ]
      shownInSolutionManager = False
      solutionManagerInfo = vim.ext.SolutionManagerInfo()

      class ServerInfo(vmodl.DynamicData): # vim.Extension.ServerInfo
         url = ""
         description = vim.Description()
         company = ""
         type = ""
         adminEmail = [ "" ]
         serverThumbprint = ""

      class ClientInfo(vmodl.DynamicData): # vim.Extension.ClientInfo
         version = ""
         description = vim.Description()
         company = ""
         type = ""
         url = ""

      class TaskTypeInfo(vmodl.DynamicData): # vim.Extension.TaskTypeInfo
         taskID = ""

      class EventTypeInfo(vmodl.DynamicData): # vim.Extension.EventTypeInfo
         eventID = ""
         eventTypeSchema = ""

      class FaultTypeInfo(vmodl.DynamicData): # vim.Extension.FaultTypeInfo
         faultID = ""

      class PrivilegeInfo(vmodl.DynamicData): # vim.Extension.PrivilegeInfo
         privID = ""
         privGroupName = ""

      class ResourceInfo(vmodl.DynamicData): # vim.Extension.ResourceInfo
         locale = ""
         module = ""
         data = [ vim.KeyValue() ]

      class HealthInfo(vmodl.DynamicData): # vim.Extension.HealthInfo
         url = ""

      class OvfConsumerInfo(vmodl.DynamicData): # vim.Extension.OvfConsumerInfo
         callbackUrl = ""
         sectionType = [ "" ]

   class ExtensionManager(vmodl.ManagedObject): # vim.ExtensionManager
      extensionList = [ vim.Extension() ]

      def unregisterExtension(extensionKey=""): # vim.ExtensionManager.unregisterExtension
         # throws vim.fault.NotFound
         return None

      def findExtension(extensionKey=""): # vim.ExtensionManager.findExtension
         return vim.Extension()

      def registerExtension(extension=vim.Extension()): # vim.ExtensionManager.registerExtension
         return None

      def updateExtension(extension=vim.Extension()): # vim.ExtensionManager.updateExtension
         # throws vim.fault.NotFound
         return None

      def getPublicKey(): # vim.ExtensionManager.getPublicKey
         return ""

      def setPublicKey(extensionKey="", publicKey=""): # vim.ExtensionManager.setPublicKey
         return None

      def setCertificate(extensionKey="", certificatePem="" or None): # vim.ExtensionManager.setCertificate
         # throws vim.fault.NotFound, vim.fault.NoClientCertificate
         return None

      def queryManagedBy(extensionKey=""): # vim.ExtensionManager.queryManagedBy
         return [ vim.ManagedEntity() ]

      def queryExtensionIpAllocationUsage(extensionKeys=[ "" ] or None): # vim.ExtensionManager.queryExtensionIpAllocationUsage
         return [ vim.ExtensionManager.IpAllocationUsage() ]

      class IpAllocationUsage(vmodl.DynamicData): # vim.ExtensionManager.IpAllocationUsage
         extensionKey = ""
         numAddresses = 0

   class FaultsByHost(vmodl.DynamicData): # vim.FaultsByHost
      host = vim.HostSystem()
      faults = [ vmodl.MethodFault() ]

   class FaultsByVM(vmodl.DynamicData): # vim.FaultsByVM
      vm = vim.VirtualMachine()
      faults = [ vmodl.MethodFault() ]

   class FileManager(vmodl.ManagedObject): # vim.FileManager

      def moveFile(sourceName="", sourceDatacenter=vim.Datacenter() or None, destinationName="", destinationDatacenter=vim.Datacenter() or None, force=False or None): # vim.FileManager.moveFile
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def copyFile(sourceName="", sourceDatacenter=vim.Datacenter() or None, destinationName="", destinationDatacenter=vim.Datacenter() or None, force=False or None): # vim.FileManager.copyFile
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def deleteFile(name="", datacenter=vim.Datacenter() or None): # vim.FileManager.deleteFile
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def makeDirectory(name="", datacenter=vim.Datacenter() or None, createParentDirectories=False or None): # vim.FileManager.makeDirectory
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return None

      def changeOwner(name="", datacenter=vim.Datacenter() or None, owner=""): # vim.FileManager.changeOwner
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault, vim.fault.UserNotFound
         return None

   class HbrManager(object): # (unknown name)

      class ReplicationVmInfo(vmodl.DynamicData): # vim.HbrManager.ReplicationVmInfo
         state = ""
         progressInfo = vim.HbrManager.ReplicationVmInfo.ProgressInfo()
         imageId = ""
         lastError = vmodl.MethodFault()

         class State(Enum): # vim.HbrManager.ReplicationVmInfo.State
            none = 0
            paused = 1
            syncing = 2
            idle = 3
            active = 4
            error = 5

         class ProgressInfo(vmodl.DynamicData): # vim.HbrManager.ReplicationVmInfo.ProgressInfo
            progress = 0
            bytesTransferred = 0
            bytesToTransfer = 0
            checksumTotalBytes = 0
            checksumComparedBytes = 0

      class VmReplicationCapability(vmodl.DynamicData): # vim.HbrManager.VmReplicationCapability
         vm = vim.VirtualMachine()
         supportedQuiesceMode = ""
         compressionSupported = False
         maxSupportedSourceDiskCapacity = 0
         minRpo = 0
         fault = vmodl.MethodFault()

         class QuiesceMode(Enum): # vim.HbrManager.VmReplicationCapability.QuiesceMode
            application = 0
            filesystem = 1
            none = 2

   class HealthUpdateInfo(vmodl.DynamicData): # vim.HealthUpdateInfo
      id = ""
      componentType = ""
      description = ""

      class ComponentType(Enum): # vim.HealthUpdateInfo.ComponentType
         Memory = 0
         Power = 1
         Fan = 2
         Network = 3
         Storage = 4

   class HealthUpdateManager(vmodl.ManagedObject): # vim.HealthUpdateManager

      def registerProvider(name="", healthUpdateInfo=[ vim.HealthUpdateInfo() ] or None): # vim.HealthUpdateManager.registerProvider
         return ""

      def unregisterProvider(providerId=""): # vim.HealthUpdateManager.unregisterProvider
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return None

      def queryProviderList(): # vim.HealthUpdateManager.queryProviderList
         return [ "" ]

      def hasProvider(id=""): # vim.HealthUpdateManager.hasProvider
         return False

      def queryProviderName(id=""): # vim.HealthUpdateManager.queryProviderName
         # throws vim.fault.NotFound
         return ""

      def queryHealthUpdateInfos(providerId=""): # vim.HealthUpdateManager.queryHealthUpdateInfos
         # throws vim.fault.NotFound
         return [ vim.HealthUpdateInfo() ]

      def addMonitoredEntities(providerId="", entities=[ vim.ManagedEntity() ] or None): # vim.HealthUpdateManager.addMonitoredEntities
         # throws vim.fault.NotFound
         return None

      def removeMonitoredEntities(providerId="", entities=[ vim.ManagedEntity() ] or None): # vim.HealthUpdateManager.removeMonitoredEntities
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return None

      def queryMonitoredEntities(providerId=""): # vim.HealthUpdateManager.queryMonitoredEntities
         # throws vim.fault.NotFound
         return [ vim.ManagedEntity() ]

      def hasMonitoredEntity(providerId="", entity=vim.ManagedEntity()): # vim.HealthUpdateManager.hasMonitoredEntity
         # throws vim.fault.NotFound
         return False

      def queryUnmonitoredHosts(providerId="", cluster=vim.ClusterComputeResource()): # vim.HealthUpdateManager.queryUnmonitoredHosts
         # throws vim.fault.NotFound
         return [ vim.HostSystem() ]

      def postHealthUpdates(providerId="", updates=[ vim.HealthUpdate() ] or None): # vim.HealthUpdateManager.postHealthUpdates
         # throws vim.fault.NotFound
         return None

      def queryHealthUpdates(providerId=""): # vim.HealthUpdateManager.queryHealthUpdates
         # throws vim.fault.NotFound
         return [ vim.HealthUpdate() ]

      def addFilter(providerId="", filterName="", infoIds=[ "" ] or None): # vim.HealthUpdateManager.addFilter
         # throws vim.fault.NotFound
         return ""

      def queryFilterList(providerId=""): # vim.HealthUpdateManager.queryFilterList
         # throws vim.fault.NotFound
         return [ "" ]

      def queryFilterName(filterId=""): # vim.HealthUpdateManager.queryFilterName
         # throws vim.fault.NotFound
         return ""

      def queryFilterInfoIds(filterId=""): # vim.HealthUpdateManager.queryFilterInfoIds
         # throws vim.fault.NotFound
         return [ "" ]

      def queryFilterEntities(filterId=""): # vim.HealthUpdateManager.queryFilterEntities
         # throws vim.fault.NotFound
         return [ vim.ManagedEntity() ]

      def addFilterEntities(filterId="", entities=[ vim.ManagedEntity() ] or None): # vim.HealthUpdateManager.addFilterEntities
         # throws vim.fault.NotFound
         return None

      def removeFilterEntities(filterId="", entities=[ vim.ManagedEntity() ] or None): # vim.HealthUpdateManager.removeFilterEntities
         # throws vim.fault.NotFound
         return None

      def removeFilter(filterId=""): # vim.HealthUpdateManager.removeFilter
         # throws vim.fault.NotFound
         return None

   class HistoricalInterval(vmodl.DynamicData): # vim.HistoricalInterval
      key = 0
      samplingPeriod = 0
      name = ""
      length = 0
      level = 0
      enabled = False

   class HistoryCollector(vmodl.ManagedObject): # vim.HistoryCollector
      filter = {}

      def setLatestPageSize(maxCount=0): # vim.HistoryCollector.setLatestPageSize
         return None

      def rewind(): # vim.HistoryCollector.rewind
         return None

      def reset(): # vim.HistoryCollector.reset
         return None

      def remove(): # vim.HistoryCollector.remove
         return None

   class HostServiceTicket(vmodl.DynamicData): # vim.HostServiceTicket
      host = ""
      port = 0
      sslThumbprint = ""
      service = ""
      serviceVersion = ""
      sessionId = ""

   class HttpNfcLease(vmodl.ManagedObject): # vim.HttpNfcLease
      initializeProgress = 0
      transferProgress = 0
      mode = ""
      capabilities = vim.HttpNfcLease.Capabilities()
      info = vim.HttpNfcLease.Info()
      state = vim.HttpNfcLease.State()
      error = vmodl.MethodFault()

      def getManifest(): # vim.HttpNfcLease.getManifest
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return [ vim.HttpNfcLease.ManifestEntry() ]

      def setManifestChecksumType(deviceUrlsToChecksumTypes=[ vim.KeyValue() ] or None): # vim.HttpNfcLease.setManifestChecksumType
         # throws vim.fault.InvalidState
         return None

      def complete(): # vim.HttpNfcLease.complete
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return None

      def abort(fault=vmodl.MethodFault() or None): # vim.HttpNfcLease.abort
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return None

      def progress(percent=0): # vim.HttpNfcLease.progress
         # throws vim.fault.Timedout
         return None

      def pullFromUrls(files=[ vim.HttpNfcLease.SourceFile() ] or None): # vim.HttpNfcLease.pullFromUrls
         # throws vim.fault.InvalidState, vim.fault.HttpFault, vim.fault.SSLVerifyFault
         return vim.Task()

      class State(Enum): # vim.HttpNfcLease.State
         initializing = 0
         ready = 1
         done = 2
         error = 3

      class Mode(Enum): # vim.HttpNfcLease.Mode
         pushOrGet = 0
         pull = 1

      class DatastoreLeaseInfo(vmodl.DynamicData): # vim.HttpNfcLease.DatastoreLeaseInfo
         datastoreKey = ""
         hosts = [ vim.HttpNfcLease.HostInfo() ]

      class HostInfo(vmodl.DynamicData): # vim.HttpNfcLease.HostInfo
         url = ""
         sslThumbprint = ""

      class Info(vmodl.DynamicData): # vim.HttpNfcLease.Info
         lease = vim.HttpNfcLease()
         entity = vim.ManagedEntity()
         deviceUrl = [ vim.HttpNfcLease.DeviceUrl() ]
         totalDiskCapacityInKB = 0
         leaseTimeout = 0
         hostMap = [ vim.HttpNfcLease.DatastoreLeaseInfo() ]

      class DeviceUrl(vmodl.DynamicData): # vim.HttpNfcLease.DeviceUrl
         key = ""
         importKey = ""
         url = ""
         sslThumbprint = ""
         disk = False
         targetId = ""
         datastoreKey = ""
         fileSize = 0

      class ManifestEntry(vmodl.DynamicData): # vim.HttpNfcLease.ManifestEntry
         key = ""
         sha1 = ""
         checksum = ""
         checksumType = ""
         size = 0
         disk = False
         capacity = 0
         populatedSize = 0

         class ChecksumType(Enum): # vim.HttpNfcLease.ManifestEntry.ChecksumType
            sha1 = 0
            sha256 = 1

      class SourceFile(vmodl.DynamicData): # vim.HttpNfcLease.SourceFile
         targetDeviceId = ""
         url = ""
         memberName = ""
         create = False
         sslThumbprint = ""
         httpHeaders = [ vim.KeyValue() ]
         size = 0

      class Capabilities(vmodl.DynamicData): # vim.HttpNfcLease.Capabilities
         pullModeSupported = False
         corsSupported = False

   class InheritablePolicy(vmodl.DynamicData): # vim.InheritablePolicy
      inherited = False

   class IntPolicy(vim.InheritablePolicy): # vim.IntPolicy
      value = 0

   class IoFilterManager(vmodl.ManagedObject): # vim.IoFilterManager

      def installIoFilter(vibUrl="", compRes=vim.ComputeResource()): # vim.IoFilterManager.installIoFilter
         # throws vim.fault.AlreadyExists
         return vim.Task()

      def uninstallIoFilter(filterId="", compRes=vim.ComputeResource()): # vim.IoFilterManager.uninstallIoFilter
         # throws vim.fault.NotFound, vim.fault.FilterInUse, vim.fault.InvalidState
         return vim.Task()

      def upgradeIoFilter(filterId="", compRes=vim.ComputeResource(), vibUrl=""): # vim.IoFilterManager.upgradeIoFilter
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return vim.Task()

      def queryIssue(filterId="", compRes=vim.ComputeResource()): # vim.IoFilterManager.queryIssue
         # throws vim.fault.NotFound
         return vim.IoFilterManager.QueryIssueResult()

      def queryIoFilterInfo(compRes=vim.ComputeResource()): # vim.IoFilterManager.queryIoFilterInfo
         return [ vim.IoFilterManager.ClusterIoFilterInfo() ]

      def resolveInstallationErrorsOnHost(filterId="", host=vim.HostSystem()): # vim.IoFilterManager.resolveInstallationErrorsOnHost
         # throws vim.fault.NotFound
         return vim.Task()

      def resolveInstallationErrorsOnCluster(filterId="", cluster=vim.ClusterComputeResource()): # vim.IoFilterManager.resolveInstallationErrorsOnCluster
         # throws vim.fault.NotFound
         return vim.Task()

      def queryDisksUsingFilter(filterId="", compRes=vim.ComputeResource()): # vim.IoFilterManager.queryDisksUsingFilter
         # throws vim.fault.NotFound
         return [ vim.vm.device.VirtualDiskId() ]

      class IoFilterInfo(vmodl.DynamicData): # vim.IoFilterManager.IoFilterInfo
         id = ""
         name = ""
         vendor = ""
         version = ""
         type = ""
         summary = ""
         releaseDate = ""

      class HostIoFilterInfo(vim.IoFilterManager.IoFilterInfo): # vim.IoFilterManager.HostIoFilterInfo
         available = False

      class OperationType(Enum): # vim.IoFilterManager.OperationType
         install = 0
         uninstall = 1
         upgrade = 2

      class ClusterIoFilterInfo(vim.IoFilterManager.IoFilterInfo): # vim.IoFilterManager.ClusterIoFilterInfo
         opType = ""
         vibUrl = ""

      class IoFilterType(Enum): # vim.IoFilterManager.IoFilterType
         cache = 0
         replication = 1
         encryption = 2
         compression = 3
         inspection = 4
         datastoreIoControl = 5
         dataProvider = 6

      class QueryIssueResult(vmodl.DynamicData): # vim.IoFilterManager.QueryIssueResult
         opType = ""
         hostIssue = [ vim.IoFilterManager.QueryIssueResult.HostIssue() ]

         class HostIssue(vmodl.DynamicData): # vim.IoFilterManager.QueryIssueResult.HostIssue
            host = vim.HostSystem()
            issue = [ vmodl.MethodFault() ]

   class IpPoolManager(vmodl.ManagedObject): # vim.IpPoolManager

      def queryIpPools(dc=vim.Datacenter()): # vim.IpPoolManager.queryIpPools
         return [ vim.vApp.IpPool() ]

      def createIpPool(dc=vim.Datacenter(), pool=vim.vApp.IpPool()): # vim.IpPoolManager.createIpPool
         return 0

      def updateIpPool(dc=vim.Datacenter(), pool=vim.vApp.IpPool()): # vim.IpPoolManager.updateIpPool
         return None

      def destroyIpPool(dc=vim.Datacenter(), id=0, force=False): # vim.IpPoolManager.destroyIpPool
         # throws vim.fault.InvalidState
         return None

      def allocateIpv4Address(dc=vim.Datacenter(), poolId=0, allocationId=""): # vim.IpPoolManager.allocateIpv4Address
         return ""

      def allocateIpv6Address(dc=vim.Datacenter(), poolId=0, allocationId=""): # vim.IpPoolManager.allocateIpv6Address
         return ""

      def releaseIpAllocation(dc=vim.Datacenter(), poolId=0, allocationId=""): # vim.IpPoolManager.releaseIpAllocation
         return None

      def queryIPAllocations(dc=vim.Datacenter(), poolId=0, extensionKey=""): # vim.IpPoolManager.queryIPAllocations
         return [ vim.IpPoolManager.IpAllocation() ]

      class IpAllocation(vmodl.DynamicData): # vim.IpPoolManager.IpAllocation
         ipAddress = ""
         allocationId = ""

   class KeyValue(vmodl.DynamicData): # vim.KeyValue
      key = ""
      value = ""

   class LatencySensitivity(vmodl.DynamicData): # vim.LatencySensitivity
      level = vim.LatencySensitivity.SensitivityLevel()
      sensitivity = 0

      class SensitivityLevel(Enum): # vim.LatencySensitivity.SensitivityLevel
         low = 0
         normal = 1
         medium = 2
         high = 3
         custom = 4

   class LicenseManager(vmodl.ManagedObject): # vim.LicenseManager
      source = vim.LicenseManager.LicenseSource()
      sourceAvailable = False
      diagnostics = vim.LicenseManager.DiagnosticInfo()
      featureInfo = [ vim.LicenseManager.FeatureInfo() ]
      licensedEdition = ""
      licenses = [ vim.LicenseManager.LicenseInfo() ]
      licenseAssignmentManager = vim.LicenseAssignmentManager()
      evaluation = vim.LicenseManager.EvaluationInfo()

      def querySupportedFeatures(host=vim.HostSystem() or None): # vim.LicenseManager.querySupportedFeatures
         return [ vim.LicenseManager.FeatureInfo() ]

      def querySourceAvailability(host=vim.HostSystem() or None): # vim.LicenseManager.querySourceAvailability
         return [ vim.LicenseManager.AvailabilityInfo() ]

      def queryUsage(host=vim.HostSystem() or None): # vim.LicenseManager.queryUsage
         return vim.LicenseManager.LicenseUsageInfo()

      def setEdition(host=vim.HostSystem() or None, featureKey="" or None): # vim.LicenseManager.setEdition
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return None

      def checkFeature(host=vim.HostSystem() or None, featureKey=""): # vim.LicenseManager.checkFeature
         # throws vim.fault.InvalidState
         return False

      def enable(host=vim.HostSystem() or None, featureKey=""): # vim.LicenseManager.enable
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return False

      def disable(host=vim.HostSystem() or None, featureKey=""): # vim.LicenseManager.disable
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return False

      def configureSource(host=vim.HostSystem() or None, licenseSource=vim.LicenseManager.LicenseSource()): # vim.LicenseManager.configureSource
         # throws vim.fault.CannotAccessLocalSource, vim.fault.InvalidLicense, vim.fault.LicenseServerUnavailable
         return None

      def updateLicense(licenseKey="", labels=[ vim.KeyValue() ] or None): # vim.LicenseManager.updateLicense
         return vim.LicenseManager.LicenseInfo()

      def addLicense(licenseKey="", labels=[ vim.KeyValue() ] or None): # vim.LicenseManager.addLicense
         return vim.LicenseManager.LicenseInfo()

      def removeLicense(licenseKey=""): # vim.LicenseManager.removeLicense
         return None

      def decodeLicense(licenseKey=""): # vim.LicenseManager.decodeLicense
         return vim.LicenseManager.LicenseInfo()

      def updateLabel(licenseKey="", labelKey="", labelValue=""): # vim.LicenseManager.updateLabel
         return None

      def removeLabel(licenseKey="", labelKey=""): # vim.LicenseManager.removeLabel
         return None

      class LicenseState(Enum): # vim.LicenseManager.LicenseState
         initializing = 0
         normal = 1
         marginal = 2
         fault = 3

      class LicenseKey(Enum): # vim.LicenseManager.LicenseKey
         esxFull = 0
         esxVmtn = 1
         esxExpress = 2
         san = 3
         iscsi = 4
         nas = 5
         vsmp = 6
         backup = 7
         vc = 8
         vcExpress = 9
         esxHost = 10
         gsxHost = 11
         serverHost = 12
         drsPower = 13
         vmotion = 14
         drs = 15
         das = 16

      class LicenseSource(vmodl.DynamicData): # vim.LicenseManager.LicenseSource
         pass

      class LicenseServer(vim.LicenseManager.LicenseSource): # vim.LicenseManager.LicenseServer
         licenseServer = ""

      class LocalLicense(vim.LicenseManager.LicenseSource): # vim.LicenseManager.LocalLicense
         licenseKeys = ""

      class EvaluationLicense(vim.LicenseManager.LicenseSource): # vim.LicenseManager.EvaluationLicense
         remainingHours = 0

      class FeatureInfo(vmodl.DynamicData): # vim.LicenseManager.FeatureInfo
         key = ""
         featureName = ""
         featureDescription = ""
         state = vim.LicenseManager.FeatureInfo.State()
         costUnit = ""
         sourceRestriction = ""
         dependentKey = [ "" ]
         edition = False
         expiresOn = vmodl.DateTime()

         class CostUnit(Enum): # vim.LicenseManager.FeatureInfo.CostUnit
            host = 0
            cpuCore = 1
            cpuPackage = 2
            server = 3
            vm = 4

         class State(Enum): # vim.LicenseManager.FeatureInfo.State
            enabled = 0
            disabled = 1
            optional = 2

         class SourceRestriction(Enum): # vim.LicenseManager.FeatureInfo.SourceRestriction
            unrestricted = 0
            served = 1
            file = 2

      class ReservationInfo(vmodl.DynamicData): # vim.LicenseManager.ReservationInfo
         key = ""
         state = vim.LicenseManager.ReservationInfo.State()
         required = 0

         class State(Enum): # vim.LicenseManager.ReservationInfo.State
            notUsed = 0
            noLicense = 1
            unlicensedUse = 2
            licensed = 3

      class AvailabilityInfo(vmodl.DynamicData): # vim.LicenseManager.AvailabilityInfo
         feature = vim.LicenseManager.FeatureInfo()
         total = 0
         available = 0

      class DiagnosticInfo(vmodl.DynamicData): # vim.LicenseManager.DiagnosticInfo
         sourceLastChanged = vmodl.DateTime()
         sourceLost = ""
         sourceLatency = 0.0
         licenseRequests = ""
         licenseRequestFailures = ""
         licenseFeatureUnknowns = ""
         opState = vim.LicenseManager.LicenseState()
         lastStatusUpdate = vmodl.DateTime()
         opFailureMessage = ""

      class LicenseUsageInfo(vmodl.DynamicData): # vim.LicenseManager.LicenseUsageInfo
         source = vim.LicenseManager.LicenseSource()
         sourceAvailable = False
         reservationInfo = [ vim.LicenseManager.ReservationInfo() ]
         featureInfo = [ vim.LicenseManager.FeatureInfo() ]

      class EvaluationInfo(vmodl.DynamicData): # vim.LicenseManager.EvaluationInfo
         properties = [ vmodl.KeyAnyValue() ]

      class LicensableResourceInfo(vmodl.DynamicData): # vim.LicenseManager.LicensableResourceInfo
         resource = [ vmodl.KeyAnyValue() ]

         class ResourceKey(Enum): # vim.LicenseManager.LicensableResourceInfo.ResourceKey
            numCpuPackages = 0
            numCpuCores = 1
            memorySize = 2
            memoryForVms = 3
            numVmsStarted = 4
            numVmsStarting = 5

      class LicenseInfo(vmodl.DynamicData): # vim.LicenseManager.LicenseInfo
         licenseKey = ""
         editionKey = ""
         name = ""
         total = 0
         used = 0
         costUnit = ""
         properties = [ vmodl.KeyAnyValue() ]
         labels = [ vim.KeyValue() ]

   class LocalizationManager(vmodl.ManagedObject): # vim.LocalizationManager
      catalog = [ vim.LocalizationManager.MessageCatalog() ]

      class MessageCatalog(vmodl.DynamicData): # vim.LocalizationManager.MessageCatalog
         moduleName = ""
         catalogName = ""
         locale = ""
         catalogUri = ""
         lastModified = vmodl.DateTime()
         md5sum = ""
         version = ""

   class LongPolicy(vim.InheritablePolicy): # vim.LongPolicy
      value = 0

   class MethodDescription(vim.Description): # vim.MethodDescription
      key = vmodl.MethodName()

   class NegatableExpression(vmodl.DynamicData): # vim.NegatableExpression
      negate = False

   class NumericRange(vmodl.DynamicData): # vim.NumericRange
      start = 0
      end = 0

   class OverheadMemoryManager(vmodl.ManagedObject): # vim.OverheadMemoryManager

      def lookupVmOverheadMemory(vm=vim.VirtualMachine(), host=vim.HostSystem()): # vim.OverheadMemoryManager.lookupVmOverheadMemory
         # throws vim.fault.NotFound, vmodl.fault.InvalidArgument, vmodl.fault.ManagedObjectNotFound, vmodl.fault.InvalidType
         return 0

   class OvfConsumer(object): # (unknown name)

      class OvfSection(vmodl.DynamicData): # vim.OvfConsumer.OvfSection
         lineNumber = 0
         xml = ""

      class OstNodeType(Enum): # vim.OvfConsumer.OstNodeType
         envelope = 0
         virtualSystem = 1
         virtualSystemCollection = 2

      class OstNode(vmodl.DynamicData): # vim.OvfConsumer.OstNode
         id = ""
         type = ""
         section = [ vim.OvfConsumer.OvfSection() ]
         child = [ vim.OvfConsumer.OstNode() ]
         entity = vim.ManagedEntity()

   class OvfManager(vmodl.ManagedObject): # vim.OvfManager
      ovfImportOption = [ vim.OvfManager.OvfOptionInfo() ]
      ovfExportOption = [ vim.OvfManager.OvfOptionInfo() ]

      def validateHost(ovfDescriptor="", host=vim.HostSystem(), vhp=vim.OvfManager.ValidateHostParams()): # vim.OvfManager.validateHost
         # throws vim.fault.TaskInProgress, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.ValidateHostResult()

      def parseDescriptor(ovfDescriptor="", pdp=vim.OvfManager.ParseDescriptorParams()): # vim.OvfManager.parseDescriptor
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.ParseDescriptorResult()

      def createImportSpec(ovfDescriptor="", resourcePool=vim.ResourcePool(), datastore=vim.Datastore(), cisp=vim.OvfManager.CreateImportSpecParams()): # vim.OvfManager.createImportSpec
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.InvalidDatastore
         return vim.OvfManager.CreateImportSpecResult()

      def createDescriptor(obj=vim.ManagedEntity(), cdp=vim.OvfManager.CreateDescriptorParams()): # vim.OvfManager.createDescriptor
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.CreateDescriptorResult()

      class OvfOptionInfo(vmodl.DynamicData): # vim.OvfManager.OvfOptionInfo
         option = ""
         description = vmodl.LocalizableMessage()

      class DeploymentOption(vmodl.DynamicData): # vim.OvfManager.DeploymentOption
         key = ""
         label = ""
         description = ""

      class CommonParams(vmodl.DynamicData): # vim.OvfManager.CommonParams
         locale = ""
         deploymentOption = ""
         msgBundle = [ vim.KeyValue() ]
         importOption = [ "" ]

      class ValidateHostParams(vim.OvfManager.CommonParams): # vim.OvfManager.ValidateHostParams
         pass

      class ValidateHostResult(vmodl.DynamicData): # vim.OvfManager.ValidateHostResult
         downloadSize = 0
         flatDeploymentSize = 0
         sparseDeploymentSize = 0
         error = [ vmodl.MethodFault() ]
         warning = [ vmodl.MethodFault() ]
         supportedDiskProvisioning = [ "" ]

      class ParseDescriptorParams(vim.OvfManager.CommonParams): # vim.OvfManager.ParseDescriptorParams
         pass

      class ParseDescriptorResult(vmodl.DynamicData): # vim.OvfManager.ParseDescriptorResult
         eula = [ "" ]
         network = [ vim.OvfManager.NetworkInfo() ]
         ipAllocationScheme = [ "" ]
         ipProtocols = [ "" ]
         property = [ vim.vApp.PropertyInfo() ]
         productInfo = vim.vApp.ProductInfo()
         annotation = ""
         approximateDownloadSize = 0
         approximateFlatDeploymentSize = 0
         approximateSparseDeploymentSize = 0
         defaultEntityName = ""
         virtualApp = False
         deploymentOption = [ vim.OvfManager.DeploymentOption() ]
         defaultDeploymentOption = ""
         entityName = [ vim.KeyValue() ]
         annotatedOst = vim.OvfConsumer.OstNode()
         error = [ vmodl.MethodFault() ]
         warning = [ vmodl.MethodFault() ]

      class NetworkInfo(vmodl.DynamicData): # vim.OvfManager.NetworkInfo
         name = ""
         description = ""

      class CreateImportSpecParams(vim.OvfManager.CommonParams): # vim.OvfManager.CreateImportSpecParams
         entityName = ""
         hostSystem = vim.HostSystem()
         networkMapping = [ vim.OvfManager.NetworkMapping() ]
         ipAllocationPolicy = ""
         ipProtocol = ""
         propertyMapping = [ vim.KeyValue() ]
         resourceMapping = [ vim.OvfManager.ResourceMap() ]
         diskProvisioning = ""
         instantiationOst = vim.OvfConsumer.OstNode()

         class DiskProvisioningType(Enum): # vim.OvfManager.CreateImportSpecParams.DiskProvisioningType
            monolithicSparse = 0
            monolithicFlat = 1
            twoGbMaxExtentSparse = 2
            twoGbMaxExtentFlat = 3
            thin = 4
            thick = 5
            seSparse = 6
            eagerZeroedThick = 7
            sparse = 8
            flat = 9

      class ResourceMap(vmodl.DynamicData): # vim.OvfManager.ResourceMap
         source = ""
         parent = vim.ResourcePool()
         resourceSpec = vim.ResourceConfigSpec()
         datastore = vim.Datastore()

      class NetworkMapping(vmodl.DynamicData): # vim.OvfManager.NetworkMapping
         name = ""
         network = vim.Network()

      class CreateImportSpecResult(vmodl.DynamicData): # vim.OvfManager.CreateImportSpecResult
         importSpec = vim.ImportSpec()
         fileItem = [ vim.OvfManager.FileItem() ]
         warning = [ vmodl.MethodFault() ]
         error = [ vmodl.MethodFault() ]

      class FileItem(vmodl.DynamicData): # vim.OvfManager.FileItem
         deviceId = ""
         path = ""
         compressionMethod = ""
         chunkSize = 0
         size = 0
         cimType = 0
         create = False

      class CreateDescriptorParams(vmodl.DynamicData): # vim.OvfManager.CreateDescriptorParams
         ovfFiles = [ vim.OvfManager.OvfFile() ]
         name = ""
         description = ""
         includeImageFiles = False
         exportOption = [ "" ]
         snapshot = vim.vm.Snapshot()

      class CreateDescriptorResult(vmodl.DynamicData): # vim.OvfManager.CreateDescriptorResult
         ovfDescriptor = ""
         error = [ vmodl.MethodFault() ]
         warning = [ vmodl.MethodFault() ]
         includeImageFiles = False

      class OvfFile(vmodl.DynamicData): # vim.OvfManager.OvfFile
         deviceId = ""
         path = ""
         compressionMethod = ""
         chunkSize = 0
         size = 0
         capacity = 0
         populatedSize = 0

   class PasswordField(vmodl.DynamicData): # vim.PasswordField
      value = ""

   class PerformanceDescription(vmodl.DynamicData): # vim.PerformanceDescription
      counterType = [ vim.ElementDescription() ]
      statsType = [ vim.ElementDescription() ]

   class PerformanceManager(vmodl.ManagedObject): # vim.PerformanceManager
      description = vim.PerformanceDescription()
      historicalInterval = [ vim.HistoricalInterval() ]
      perfCounter = [ vim.PerformanceManager.CounterInfo() ]

      def queryProviderSummary(entity=vmodl.ManagedObject()): # vim.PerformanceManager.queryProviderSummary
         return vim.PerformanceManager.ProviderSummary()

      def queryAvailableMetric(entity=vmodl.ManagedObject(), beginTime=vmodl.DateTime() or None, endTime=vmodl.DateTime() or None, intervalId=0 or None): # vim.PerformanceManager.queryAvailableMetric
         return [ vim.PerformanceManager.MetricId() ]

      def queryCounter(counterId=[ 0 ]): # vim.PerformanceManager.queryCounter
         return [ vim.PerformanceManager.CounterInfo() ]

      def queryCounterByLevel(level=0): # vim.PerformanceManager.queryCounterByLevel
         return [ vim.PerformanceManager.CounterInfo() ]

      def queryStats(querySpec=[ vim.PerformanceManager.QuerySpec() ]): # vim.PerformanceManager.queryStats
         return [ vim.PerformanceManager.EntityMetricBase() ]

      def queryCompositeStats(querySpec=vim.PerformanceManager.QuerySpec()): # vim.PerformanceManager.queryCompositeStats
         return vim.PerformanceManager.CompositeEntityMetric()

      def createHistoricalInterval(intervalId=vim.HistoricalInterval()): # vim.PerformanceManager.createHistoricalInterval
         return None

      def removeHistoricalInterval(samplePeriod=0): # vim.PerformanceManager.removeHistoricalInterval
         return None

      def updateHistoricalInterval(interval=vim.HistoricalInterval()): # vim.PerformanceManager.updateHistoricalInterval
         return None

      def updateCounterLevelMapping(counterLevelMap=[ vim.PerformanceManager.CounterLevelMapping() ]): # vim.PerformanceManager.updateCounterLevelMapping
         return None

      def resetCounterLevelMapping(counters=[ 0 ]): # vim.PerformanceManager.resetCounterLevelMapping
         return None

      class Format(Enum): # vim.PerformanceManager.Format
         normal = 0
         csv = 1

      class ProviderSummary(vmodl.DynamicData): # vim.PerformanceManager.ProviderSummary
         entity = vmodl.ManagedObject()
         currentSupported = False
         summarySupported = False
         refreshRate = 0

      class CounterInfo(vmodl.DynamicData): # vim.PerformanceManager.CounterInfo
         key = 0
         nameInfo = vim.ElementDescription()
         groupInfo = vim.ElementDescription()
         unitInfo = vim.ElementDescription()
         rollupType = vim.PerformanceManager.CounterInfo.RollupType()
         statsType = vim.PerformanceManager.CounterInfo.StatsType()
         level = 0
         perDeviceLevel = 0
         associatedCounterId = [ 0 ]

         class RollupType(Enum): # vim.PerformanceManager.CounterInfo.RollupType
            average = 0
            maximum = 1
            minimum = 2
            latest = 3
            summation = 4
            none = 5

         class StatsType(Enum): # vim.PerformanceManager.CounterInfo.StatsType
            absolute = 0
            delta = 1
            rate = 2

         class Unit(Enum): # vim.PerformanceManager.CounterInfo.Unit
            percent = 0
            kiloBytes = 1
            megaBytes = 2
            megaHertz = 3
            number = 4
            microsecond = 5
            millisecond = 6
            second = 7
            kiloBytesPerSecond = 8
            megaBytesPerSecond = 9
            watt = 10
            joule = 11
            teraBytes = 12
            celsius = 13

      class MetricId(vmodl.DynamicData): # vim.PerformanceManager.MetricId
         counterId = 0
         instance = ""

      class QuerySpec(vmodl.DynamicData): # vim.PerformanceManager.QuerySpec
         entity = vmodl.ManagedObject()
         startTime = vmodl.DateTime()
         endTime = vmodl.DateTime()
         maxSample = 0
         metricId = [ vim.PerformanceManager.MetricId() ]
         intervalId = 0
         format = ""

      class SampleInfo(vmodl.DynamicData): # vim.PerformanceManager.SampleInfo
         timestamp = vmodl.DateTime()
         interval = 0

      class MetricSeries(vmodl.DynamicData): # vim.PerformanceManager.MetricSeries
         id = vim.PerformanceManager.MetricId()

      class IntSeries(vim.PerformanceManager.MetricSeries): # vim.PerformanceManager.IntSeries
         value = [ 0 ]

      class MetricSeriesCSV(vim.PerformanceManager.MetricSeries): # vim.PerformanceManager.MetricSeriesCSV
         value = ""

      class EntityMetricBase(vmodl.DynamicData): # vim.PerformanceManager.EntityMetricBase
         entity = vmodl.ManagedObject()

      class EntityMetric(vim.PerformanceManager.EntityMetricBase): # vim.PerformanceManager.EntityMetric
         sampleInfo = [ vim.PerformanceManager.SampleInfo() ]
         value = [ vim.PerformanceManager.MetricSeries() ]

      class EntityMetricCSV(vim.PerformanceManager.EntityMetricBase): # vim.PerformanceManager.EntityMetricCSV
         sampleInfoCSV = ""
         value = [ vim.PerformanceManager.MetricSeriesCSV() ]

      class CompositeEntityMetric(vmodl.DynamicData): # vim.PerformanceManager.CompositeEntityMetric
         entity = vim.PerformanceManager.EntityMetricBase()
         childEntity = [ vim.PerformanceManager.EntityMetricBase() ]

      class CounterLevelMapping(vmodl.DynamicData): # vim.PerformanceManager.CounterLevelMapping
         counterId = 0
         aggregateLevel = 0
         perDeviceLevel = 0

   class PrivilegePolicyDef(vmodl.DynamicData): # vim.PrivilegePolicyDef
      createPrivilege = ""
      readPrivilege = ""
      updatePrivilege = ""
      deletePrivilege = ""

   class ResourceAllocationInfo(vmodl.DynamicData): # vim.ResourceAllocationInfo
      reservation = 0
      expandableReservation = False
      limit = 0
      shares = vim.SharesInfo()
      overheadLimit = 0

   class ResourceAllocationOption(vmodl.DynamicData): # vim.ResourceAllocationOption
      sharesOption = vim.SharesOption()

   class ResourceConfigOption(vmodl.DynamicData): # vim.ResourceConfigOption
      cpuAllocationOption = vim.ResourceAllocationOption()
      memoryAllocationOption = vim.ResourceAllocationOption()

   class ResourceConfigSpec(vmodl.DynamicData): # vim.ResourceConfigSpec
      entity = vim.ManagedEntity()
      changeVersion = ""
      lastModified = vmodl.DateTime()
      cpuAllocation = vim.ResourceAllocationInfo()
      memoryAllocation = vim.ResourceAllocationInfo()
      scaleDescendantsShares = ""

      class ScaleSharesBehavior(Enum): # vim.ResourceConfigSpec.ScaleSharesBehavior
         disabled = 0
         scaleCpuAndMemoryShares = 1

   class ResourcePlanningManager(vmodl.ManagedObject): # vim.ResourcePlanningManager

      def estimateDatabaseSize(dbSizeParam=vim.ResourcePlanningManager.DatabaseSizeParam()): # vim.ResourcePlanningManager.estimateDatabaseSize
         return vim.ResourcePlanningManager.DatabaseSizeEstimate()

      class DatabaseSizeParam(vmodl.DynamicData): # vim.ResourcePlanningManager.DatabaseSizeParam
         inventoryDesc = vim.ResourcePlanningManager.InventoryDescription()
         perfStatsDesc = vim.ResourcePlanningManager.PerfStatsDescription()

      class InventoryDescription(vmodl.DynamicData): # vim.ResourcePlanningManager.InventoryDescription
         numHosts = 0
         numVirtualMachines = 0
         numResourcePools = 0
         numClusters = 0
         numCpuDev = 0
         numNetDev = 0
         numDiskDev = 0
         numvCpuDev = 0
         numvNetDev = 0
         numvDiskDev = 0

      class PerfStatsDescription(vmodl.DynamicData): # vim.ResourcePlanningManager.PerfStatsDescription
         intervals = [ vim.HistoricalInterval() ]

      class DatabaseSizeEstimate(vmodl.DynamicData): # vim.ResourcePlanningManager.DatabaseSizeEstimate
         size = 0

   class SDDCBase(vmodl.DynamicData): # vim.SDDCBase
      pass

   class SearchIndex(vmodl.ManagedObject): # vim.SearchIndex

      def findByUuid(datacenter=vim.Datacenter() or None, uuid="", vmSearch=False, instanceUuid=False or None): # vim.SearchIndex.findByUuid
         return vim.ManagedEntity()

      def findByDatastorePath(datacenter=vim.Datacenter(), path=""): # vim.SearchIndex.findByDatastorePath
         # throws vim.fault.InvalidDatastore
         return vim.VirtualMachine()

      def findByDnsName(datacenter=vim.Datacenter() or None, dnsName="", vmSearch=False): # vim.SearchIndex.findByDnsName
         return vim.ManagedEntity()

      def findByIp(datacenter=vim.Datacenter() or None, ip="", vmSearch=False): # vim.SearchIndex.findByIp
         return vim.ManagedEntity()

      def findByInventoryPath(inventoryPath=""): # vim.SearchIndex.findByInventoryPath
         return vim.ManagedEntity()

      def findChild(entity=vim.ManagedEntity(), name=""): # vim.SearchIndex.findChild
         return vim.ManagedEntity()

      def findAllByUuid(datacenter=vim.Datacenter() or None, uuid="", vmSearch=False, instanceUuid=False or None): # vim.SearchIndex.findAllByUuid
         return [ vim.ManagedEntity() ]

      def findAllByDnsName(datacenter=vim.Datacenter() or None, dnsName="", vmSearch=False): # vim.SearchIndex.findAllByDnsName
         return [ vim.ManagedEntity() ]

      def findAllByIp(datacenter=vim.Datacenter() or None, ip="", vmSearch=False): # vim.SearchIndex.findAllByIp
         return [ vim.ManagedEntity() ]

   class SelectionSet(vmodl.DynamicData): # vim.SelectionSet
      pass

   class ServiceInstanceContent(vmodl.DynamicData): # vim.ServiceInstanceContent
      rootFolder = vim.Folder()
      propertyCollector = vmodl.query.PropertyCollector()
      viewManager = vim.view.ViewManager()
      about = vim.AboutInfo()
      setting = vim.option.OptionManager()
      userDirectory = vim.UserDirectory()
      sessionManager = vim.SessionManager()
      authorizationManager = vim.AuthorizationManager()
      serviceManager = vim.ServiceManager()
      perfManager = vim.PerformanceManager()
      scheduledTaskManager = vim.scheduler.ScheduledTaskManager()
      alarmManager = vim.alarm.AlarmManager()
      eventManager = vim.event.EventManager()
      taskManager = vim.TaskManager()
      extensionManager = vim.ExtensionManager()
      customizationSpecManager = vim.CustomizationSpecManager()
      guestCustomizationManager = vim.vm.GuestCustomizationManager()
      customFieldsManager = vim.CustomFieldsManager()
      accountManager = vim.host.LocalAccountManager()
      diagnosticManager = vim.DiagnosticManager()
      licenseManager = vim.LicenseManager()
      searchIndex = vim.SearchIndex()
      fileManager = vim.FileManager()
      datastoreNamespaceManager = vim.DatastoreNamespaceManager()
      virtualDiskManager = vim.VirtualDiskManager()
      virtualizationManager = vim.VirtualizationManager()
      snmpSystem = vim.host.SnmpSystem()
      vmProvisioningChecker = vim.vm.check.ProvisioningChecker()
      vmCompatibilityChecker = vim.vm.check.CompatibilityChecker()
      ovfManager = vim.OvfManager()
      ipPoolManager = vim.IpPoolManager()
      dvSwitchManager = vim.dvs.DistributedVirtualSwitchManager()
      hostProfileManager = vim.profile.host.ProfileManager()
      clusterProfileManager = vim.profile.cluster.ProfileManager()
      complianceManager = vim.profile.ComplianceManager()
      localizationManager = vim.LocalizationManager()
      storageResourceManager = vim.StorageResourceManager()
      guestOperationsManager = vim.vm.guest.GuestOperationsManager()
      overheadMemoryManager = vim.OverheadMemoryManager()
      certificateManager = vim.CertificateManager()
      ioFilterManager = vim.IoFilterManager()
      vStorageObjectManager = vim.vslm.VStorageObjectManagerBase()
      hostSpecManager = vim.profile.host.HostSpecificationManager()
      cryptoManager = vim.encryption.CryptoManager()
      healthUpdateManager = vim.HealthUpdateManager()
      failoverClusterConfigurator = vim.vcha.FailoverClusterConfigurator()
      failoverClusterManager = vim.vcha.FailoverClusterManager()
      tenantManager = vim.tenant.TenantManager()
      siteInfoManager = vim.SiteInfoManager()
      storageQueryManager = vim.StorageQueryManager()

   class ServiceLocator(vmodl.DynamicData): # vim.ServiceLocator
      instanceUuid = ""
      url = ""
      credential = vim.ServiceLocator.Credential()
      sslThumbprint = ""

      class Credential(vmodl.DynamicData): # vim.ServiceLocator.Credential
         pass

      class NamePassword(vim.ServiceLocator.Credential): # vim.ServiceLocator.NamePassword
         username = ""
         password = ""

      class SAMLCredential(vim.ServiceLocator.Credential): # vim.ServiceLocator.SAMLCredential
         token = ""

   class ServiceManager(vmodl.ManagedObject): # vim.ServiceManager
      service = [ vim.ServiceManager.ServiceInfo() ]

      def queryServiceList(serviceName="" or None, location=[ "" ] or None): # vim.ServiceManager.queryServiceList
         return [ vim.ServiceManager.ServiceInfo() ]

      class ServiceInfo(vmodl.DynamicData): # vim.ServiceManager.ServiceInfo
         serviceName = ""
         location = [ "" ]
         service = vmodl.ManagedObject()
         description = ""

   class SessionManager(vmodl.ManagedObject): # vim.SessionManager
      sessionList = [ vim.UserSession() ]
      currentSession = vim.UserSession()
      message = ""
      messageLocaleList = [ "" ]
      supportedLocaleList = [ "" ]
      defaultLocale = ""

      def updateMessage(message=""): # vim.SessionManager.updateMessage
         return None

      def loginByToken(locale="" or None): # vim.SessionManager.loginByToken
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def login(userName="", password="", locale="" or None): # vim.SessionManager.login
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def loginBySSPI(base64Token="", locale="" or None): # vim.SessionManager.loginBySSPI
         # throws vim.fault.SSPIChallenge, vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def logout(): # vim.SessionManager.logout
         return None

      def acquireLocalTicket(userName=""): # vim.SessionManager.acquireLocalTicket
         # throws vim.fault.InvalidLogin
         return vim.SessionManager.LocalTicket()

      def acquireGenericServiceTicket(spec=vim.SessionManager.ServiceRequestSpec()): # vim.SessionManager.acquireGenericServiceTicket
         return vim.SessionManager.GenericServiceTicket()

      def terminate(sessionId=[ "" ]): # vim.SessionManager.terminate
         # throws vim.fault.NotFound
         return None

      def setLocale(locale=""): # vim.SessionManager.setLocale
         # throws vim.fault.InvalidLocale
         return None

      def loginExtensionBySubjectName(extensionKey="", locale="" or None): # vim.SessionManager.loginExtensionBySubjectName
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale, vim.fault.NotFound, vim.fault.NoClientCertificate, vim.fault.NoSubjectName
         return vim.UserSession()

      def loginExtensionByCertificate(extensionKey="", locale="" or None): # vim.SessionManager.loginExtensionByCertificate
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale, vim.fault.NoClientCertificate
         return vim.UserSession()

      def impersonateUser(userName="", locale="" or None): # vim.SessionManager.impersonateUser
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def sessionIsActive(sessionID="", userName=""): # vim.SessionManager.sessionIsActive
         return False

      def acquireCloneTicket(): # vim.SessionManager.acquireCloneTicket
         return ""

      def cloneSession(cloneTicket=""): # vim.SessionManager.cloneSession
         # throws vim.fault.InvalidLogin
         return vim.UserSession()

      class LocalTicket(vmodl.DynamicData): # vim.SessionManager.LocalTicket
         userName = ""
         passwordFilePath = ""

      class GenericServiceTicket(vmodl.DynamicData): # vim.SessionManager.GenericServiceTicket
         id = ""
         hostName = ""
         sslThumbprint = ""

      class ServiceRequestSpec(vmodl.DynamicData): # vim.SessionManager.ServiceRequestSpec
         pass

      class VmomiServiceRequestSpec(vim.SessionManager.ServiceRequestSpec): # vim.SessionManager.VmomiServiceRequestSpec
         method = vmodl.MethodName()

      class HttpServiceRequestSpec(vim.SessionManager.ServiceRequestSpec): # vim.SessionManager.HttpServiceRequestSpec
         method = ""
         url = ""

         class Method(Enum): # vim.SessionManager.HttpServiceRequestSpec.Method
            httpOptions = 0
            httpGet = 1
            httpHead = 2
            httpPost = 3
            httpPut = 4
            httpDelete = 5
            httpTrace = 6
            httpConnect = 7

   class SharesInfo(vmodl.DynamicData): # vim.SharesInfo
      shares = 0
      level = vim.SharesInfo.Level()

      class Level(Enum): # vim.SharesInfo.Level
         low = 0
         normal = 1
         high = 2
         custom = 3

   class SharesOption(vmodl.DynamicData): # vim.SharesOption
      sharesOption = vim.option.IntOption()
      defaultLevel = vim.SharesInfo.Level()

   class SimpleCommand(vmodl.ManagedObject): # vim.SimpleCommand
      encodingType = vim.SimpleCommand.Encoding()
      entity = vim.ServiceManager.ServiceInfo()

      def Execute(arguments=[ "" ] or None): # vim.SimpleCommand.Execute
         return ""

      class Encoding(Enum): # vim.SimpleCommand.Encoding
         CSV = 0
         HEX = 1
         STRING = 2

   class SiteInfo(vmodl.DynamicData): # vim.SiteInfo
      pass

   class SiteInfoManager(vmodl.ManagedObject): # vim.SiteInfoManager

      def GetSiteInfo(): # vim.SiteInfoManager.GetSiteInfo
         return vim.SiteInfo()

   class StorageQueryManager(vmodl.ManagedObject): # vim.StorageQueryManager

      def queryHostsWithAttachedLun(lunUuid=""): # vim.StorageQueryManager.queryHostsWithAttachedLun
         return [ vim.HostSystem() ]

   class StorageResourceManager(vmodl.ManagedObject): # vim.StorageResourceManager

      def ConfigureDatastoreIORM(datastore=vim.Datastore(), spec=vim.StorageResourceManager.IORMConfigSpec()): # vim.StorageResourceManager.ConfigureDatastoreIORM
         # throws vim.fault.IORMNotSupportedHostOnDatastore, vim.fault.InaccessibleDatastore
         return vim.Task()

      def QueryIORMConfigOption(host=vim.HostSystem()): # vim.StorageResourceManager.QueryIORMConfigOption
         return vim.StorageResourceManager.IORMConfigOption()

      def queryDatastorePerformanceSummary(datastore=vim.Datastore()): # vim.StorageResourceManager.queryDatastorePerformanceSummary
         # throws vim.fault.NotFound
         return [ vim.StorageResourceManager.StoragePerformanceSummary() ]

      def applyRecommendationToPod(pod=vim.StoragePod(), key=""): # vim.StorageResourceManager.applyRecommendationToPod
         return vim.Task()

      def applyRecommendation(key=[ "" ]): # vim.StorageResourceManager.applyRecommendation
         return vim.Task()

      def cancelRecommendation(key=[ "" ]): # vim.StorageResourceManager.cancelRecommendation
         return None

      def refreshRecommendation(pod=vim.StoragePod()): # vim.StorageResourceManager.refreshRecommendation
         return None

      def refreshRecommendationsForPod(pod=vim.StoragePod()): # vim.StorageResourceManager.refreshRecommendationsForPod
         # throws vmodl.fault.InvalidArgument
         return vim.Task()

      def configureStorageDrsForPod(pod=vim.StoragePod(), spec=vim.storageDrs.ConfigSpec(), modify=False): # vim.StorageResourceManager.configureStorageDrsForPod
         return vim.Task()

      def validateStoragePodConfig(pod=vim.StoragePod(), spec=vim.storageDrs.ConfigSpec()): # vim.StorageResourceManager.validateStoragePodConfig
         return vmodl.MethodFault()

      def recommendDatastores(storageSpec=vim.storageDrs.StoragePlacementSpec()): # vim.StorageResourceManager.recommendDatastores
         return vim.storageDrs.StoragePlacementResult()

      class IOAllocationInfo(vmodl.DynamicData): # vim.StorageResourceManager.IOAllocationInfo
         limit = 0
         shares = vim.SharesInfo()
         reservation = 0

      class IOAllocationOption(vmodl.DynamicData): # vim.StorageResourceManager.IOAllocationOption
         limitOption = vim.option.LongOption()
         sharesOption = vim.SharesOption()

      class CongestionThresholdMode(Enum): # vim.StorageResourceManager.CongestionThresholdMode
         automatic = 0
         manual = 1

      class IORMConfigInfo(vmodl.DynamicData): # vim.StorageResourceManager.IORMConfigInfo
         enabled = False
         congestionThresholdMode = ""
         congestionThreshold = 0
         percentOfPeakThroughput = 0
         statsCollectionEnabled = False
         reservationEnabled = False
         statsAggregationDisabled = False
         reservableIopsThreshold = 0

      class IORMConfigSpec(vmodl.DynamicData): # vim.StorageResourceManager.IORMConfigSpec
         enabled = False
         congestionThresholdMode = ""
         congestionThreshold = 0
         percentOfPeakThroughput = 0
         statsCollectionEnabled = False
         reservationEnabled = False
         statsAggregationDisabled = False
         reservableIopsThreshold = 0

      class IORMConfigOption(vmodl.DynamicData): # vim.StorageResourceManager.IORMConfigOption
         enabledOption = vim.option.BoolOption()
         congestionThresholdOption = vim.option.IntOption()
         statsCollectionEnabledOption = vim.option.BoolOption()
         reservationEnabledOption = vim.option.BoolOption()

      class StoragePerformanceSummary(vmodl.DynamicData): # vim.StorageResourceManager.StoragePerformanceSummary
         interval = 0
         percentile = [ 0 ]
         datastoreReadLatency = [ 0.0 ]
         datastoreWriteLatency = [ 0.0 ]
         datastoreVmLatency = [ 0.0 ]
         datastoreReadIops = [ 0.0 ]
         datastoreWriteIops = [ 0.0 ]
         siocActivityDuration = 0

      class PodStorageDrsEntry(vmodl.DynamicData): # vim.StorageResourceManager.PodStorageDrsEntry
         storageDrsConfig = vim.storageDrs.ConfigInfo()
         recommendation = [ vim.cluster.Recommendation() ]
         drsFault = [ vim.cluster.DrsFaults() ]
         actionHistory = [ vim.cluster.ActionHistory() ]

      class StorageProfileStatistics(vmodl.DynamicData): # vim.StorageResourceManager.StorageProfileStatistics
         profileId = ""
         totalSpaceMB = 0
         usedSpaceMB = 0

   class StringExpression(vim.NegatableExpression): # vim.StringExpression
      value = ""

   class StringPolicy(vim.InheritablePolicy): # vim.StringPolicy
      value = ""

   class Tag(vmodl.DynamicData): # vim.Tag
      key = ""

   class TaskDescription(vmodl.DynamicData): # vim.TaskDescription
      methodInfo = [ vim.ElementDescription() ]
      state = [ vim.ElementDescription() ]
      reason = [ vim.TypeDescription() ]

   class TaskHistoryCollector(vim.HistoryCollector): # vim.TaskHistoryCollector
      latestPage = [ vim.TaskInfo() ]

      def readNext(maxCount=0): # vim.TaskHistoryCollector.readNext
         return [ vim.TaskInfo() ]

      def readPrev(maxCount=0): # vim.TaskHistoryCollector.readPrev
         return [ vim.TaskInfo() ]

   class TaskInfo(vmodl.DynamicData): # vim.TaskInfo
      key = ""
      task = vim.Task()
      description = vmodl.LocalizableMessage()
      name = vmodl.MethodName()
      descriptionId = ""
      entity = vim.ManagedEntity()
      entityName = ""
      locked = [ vim.ManagedEntity() ]
      state = vim.TaskInfo.State()
      cancelled = False
      cancelable = False
      error = vmodl.MethodFault()
      result = {}
      progress = 0
      reason = vim.TaskReason()
      queueTime = vmodl.DateTime()
      startTime = vmodl.DateTime()
      completeTime = vmodl.DateTime()
      eventChainId = 0
      changeTag = ""
      parentTaskKey = ""
      rootTaskKey = ""
      activationId = ""

      class State(Enum): # vim.TaskInfo.State
         queued = 0
         running = 1
         success = 2
         error = 3

   class TaskManager(vmodl.ManagedObject): # vim.TaskManager
      recentTask = [ vim.Task() ]
      description = vim.TaskDescription()
      maxCollector = 0

      def createCollector(filter=vim.TaskFilterSpec()): # vim.TaskManager.createCollector
         # throws vim.fault.InvalidState
         return vim.TaskHistoryCollector()

      def createTask(obj=vmodl.ManagedObject(), taskTypeId="", initiatedBy="" or None, cancelable=False, parentTaskKey="" or None, activationId="" or None): # vim.TaskManager.createTask
         return vim.TaskInfo()

   class TaskReason(vmodl.DynamicData): # vim.TaskReason
      pass

   class TaskReasonAlarm(vim.TaskReason): # vim.TaskReasonAlarm
      alarmName = ""
      alarm = vim.alarm.Alarm()
      entityName = ""
      entity = vim.ManagedEntity()

   class TaskReasonSchedule(vim.TaskReason): # vim.TaskReasonSchedule
      name = ""
      scheduledTask = vim.scheduler.ScheduledTask()

   class TaskReasonSystem(vim.TaskReason): # vim.TaskReasonSystem
      pass

   class TaskReasonUser(vim.TaskReason): # vim.TaskReasonUser
      userName = ""

   class TypeDescription(vim.Description): # vim.TypeDescription
      key = vmodl.TypeName()

   class UpdateVirtualMachineFilesResult(vmodl.DynamicData): # vim.UpdateVirtualMachineFilesResult
      failedVmFile = [ vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo() ]

      class FailedVmFileInfo(vmodl.DynamicData): # vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo
         vmFile = ""
         fault = vmodl.MethodFault()

   class UserDirectory(vmodl.ManagedObject): # vim.UserDirectory
      domainList = [ "" ]

      def retrieveUserGroups(domain="" or None, searchStr="", belongsToGroup="" or None, belongsToUser="" or None, exactMatch=False, findUsers=False, findGroups=False): # vim.UserDirectory.retrieveUserGroups
         # throws vim.fault.NotFound
         return [ vim.UserSearchResult() ]

   class UserSearchResult(vmodl.DynamicData): # vim.UserSearchResult
      principal = ""
      fullName = ""
      group = False

   class UserSession(vmodl.DynamicData): # vim.UserSession
      key = ""
      userName = ""
      fullName = ""
      loginTime = vmodl.DateTime()
      lastActiveTime = vmodl.DateTime()
      locale = ""
      messageLocale = ""
      extensionSession = False
      ipAddress = ""
      userAgent = ""
      callCount = 0

   class VVolVmConfigFileUpdateResult(vmodl.DynamicData): # vim.VVolVmConfigFileUpdateResult
      succeededVmConfigFile = [ vim.KeyValue() ]
      failedVmConfigFile = [ vim.VVolVmConfigFileUpdateResult.FailedVmConfigFileInfo() ]

      class FailedVmConfigFileInfo(vmodl.DynamicData): # vim.VVolVmConfigFileUpdateResult.FailedVmConfigFileInfo
         targetConfigVVolId = ""
         dsPath = ""
         fault = vmodl.MethodFault()

   class VasaStorageArray(vmodl.DynamicData): # vim.VasaStorageArray
      name = ""
      uuid = ""
      vendorId = ""
      modelId = ""

   class VimVasaProvider(vmodl.DynamicData): # vim.VimVasaProvider
      uid = ""
      url = ""
      name = ""
      selfSignedCertificate = ""

      class StatePerArray(vmodl.DynamicData): # vim.VimVasaProvider.StatePerArray
         priority = 0
         arrayId = ""
         active = False

   class VimVasaProviderInfo(vmodl.DynamicData): # vim.VimVasaProviderInfo
      provider = vim.VimVasaProvider()
      arrayState = [ vim.VimVasaProvider.StatePerArray() ]

   class VirtualizationManager(vmodl.ManagedObject): # vim.VirtualizationManager
      pass

   class VsanUpgradeSystem(vmodl.ManagedObject): # vim.VsanUpgradeSystem

      def performUpgradePreflightCheck(cluster=vim.ClusterComputeResource(), downgradeFormat=False or None): # vim.VsanUpgradeSystem.performUpgradePreflightCheck
         # throws vim.fault.VsanFault
         return vim.VsanUpgradeSystem.PreflightCheckResult()

      def queryUpgradeStatus(cluster=vim.ClusterComputeResource()): # vim.VsanUpgradeSystem.queryUpgradeStatus
         # throws vim.fault.VsanFault
         return vim.VsanUpgradeSystem.UpgradeStatus()

      def performUpgrade(cluster=vim.ClusterComputeResource(), performObjectUpgrade=False or None, downgradeFormat=False or None, allowReducedRedundancy=False or None, excludeHosts=[ vim.HostSystem() ] or None): # vim.VsanUpgradeSystem.performUpgrade
         # throws vim.fault.VsanFault
         return vim.Task()

      class PreflightCheckIssue(vmodl.DynamicData): # vim.VsanUpgradeSystem.PreflightCheckIssue
         msg = ""

      class HostsDisconnectedIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.HostsDisconnectedIssue
         hosts = [ vim.HostSystem() ]

      class MissingHostsInClusterIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.MissingHostsInClusterIssue
         hosts = [ vim.HostSystem() ]

      class RogueHostsInClusterIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.RogueHostsInClusterIssue
         uuids = [ "" ]

      class WrongEsxVersionIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.WrongEsxVersionIssue
         hosts = [ vim.HostSystem() ]

      class AutoClaimEnabledOnHostsIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.AutoClaimEnabledOnHostsIssue
         hosts = [ vim.HostSystem() ]

      class APIBrokenIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.APIBrokenIssue
         hosts = [ vim.HostSystem() ]

      class V2ObjectsPresentDuringDowngradeIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.V2ObjectsPresentDuringDowngradeIssue
         uuids = [ "" ]

      class NotEnoughFreeCapacityIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.NotEnoughFreeCapacityIssue
         reducedRedundancyUpgradePossible = False

      class NetworkPartitionInfo(vmodl.DynamicData): # vim.VsanUpgradeSystem.NetworkPartitionInfo
         hosts = [ vim.HostSystem() ]

      class NetworkPartitionIssue(vim.VsanUpgradeSystem.PreflightCheckIssue): # vim.VsanUpgradeSystem.NetworkPartitionIssue
         partitions = [ vim.VsanUpgradeSystem.NetworkPartitionInfo() ]

      class PreflightCheckResult(vmodl.DynamicData): # vim.VsanUpgradeSystem.PreflightCheckResult
         issues = [ vim.VsanUpgradeSystem.PreflightCheckIssue() ]
         diskMappingToRestore = vim.vsan.host.DiskMapping()

      class UpgradeHistoryItem(vmodl.DynamicData): # vim.VsanUpgradeSystem.UpgradeHistoryItem
         timestamp = vmodl.DateTime()
         host = vim.HostSystem()
         message = ""
         task = vim.Task()

      class UpgradeHistoryDiskGroupOpType(Enum): # vim.VsanUpgradeSystem.UpgradeHistoryDiskGroupOpType
         add = 0
         remove = 1

      class UpgradeHistoryDiskGroupOp(vim.VsanUpgradeSystem.UpgradeHistoryItem): # vim.VsanUpgradeSystem.UpgradeHistoryDiskGroupOp
         operation = ""
         diskMapping = vim.vsan.host.DiskMapping()

      class UpgradeHistoryPreflightFail(vim.VsanUpgradeSystem.UpgradeHistoryItem): # vim.VsanUpgradeSystem.UpgradeHistoryPreflightFail
         preflightResult = vim.VsanUpgradeSystem.PreflightCheckResult()

      class UpgradeStatus(vmodl.DynamicData): # vim.VsanUpgradeSystem.UpgradeStatus
         inProgress = False
         history = [ vim.VsanUpgradeSystem.UpgradeHistoryItem() ]
         aborted = False
         completed = False
         progress = 0

   class action(object): # (unknown name)

      class Action(vmodl.DynamicData): # vim.action.Action

         class ActionParameter(Enum): # vim.action.Action.ActionParameter
            targetName = 0
            alarmName = 1
            oldStatus = 2
            newStatus = 3
            triggeringSummary = 4
            declaringSummary = 5
            eventDescription = 6
            target = 7
            alarm = 8

      class CreateTaskAction(vim.action.Action): # vim.action.CreateTaskAction
         taskTypeId = ""
         cancelable = False

      class MethodAction(vim.action.Action): # vim.action.MethodAction
         name = vmodl.MethodName()
         argument = [ vim.action.MethodActionArgument() ]

      class MethodActionArgument(vmodl.DynamicData): # vim.action.MethodActionArgument
         value = {}

      class RunScriptAction(vim.action.Action): # vim.action.RunScriptAction
         script = ""

      class SendEmailAction(vim.action.Action): # vim.action.SendEmailAction
         toList = ""
         ccList = ""
         subject = ""
         body = ""

      class SendSNMPAction(vim.action.Action): # vim.action.SendSNMPAction
         pass

   class alarm(object): # (unknown name)

      class Alarm(vim.ExtensibleManagedObject): # vim.alarm.Alarm
         info = vim.alarm.AlarmInfo()

         def remove(): # vim.alarm.Alarm.remove
            return None

         def reconfigure(spec=vim.alarm.AlarmSpec()): # vim.alarm.Alarm.reconfigure
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return None

      class AlarmAction(vmodl.DynamicData): # vim.alarm.AlarmAction
         pass

      class AlarmDescription(vmodl.DynamicData): # vim.alarm.AlarmDescription
         expr = [ vim.TypeDescription() ]
         stateOperator = [ vim.ElementDescription() ]
         metricOperator = [ vim.ElementDescription() ]
         hostSystemConnectionState = [ vim.ElementDescription() ]
         virtualMachinePowerState = [ vim.ElementDescription() ]
         datastoreConnectionState = [ vim.ElementDescription() ]
         hostSystemPowerState = [ vim.ElementDescription() ]
         virtualMachineGuestHeartbeatStatus = [ vim.ElementDescription() ]
         entityStatus = [ vim.ElementDescription() ]
         action = [ vim.TypeDescription() ]

      class AlarmExpression(vmodl.DynamicData): # vim.alarm.AlarmExpression
         pass

      class AlarmSetting(vmodl.DynamicData): # vim.alarm.AlarmSetting
         toleranceRange = 0
         reportingFrequency = 0

      class AlarmSpec(vmodl.DynamicData): # vim.alarm.AlarmSpec
         name = ""
         systemName = ""
         description = ""
         enabled = False
         expression = vim.alarm.AlarmExpression()
         action = vim.alarm.AlarmAction()
         actionFrequency = 0
         setting = vim.alarm.AlarmSetting()

      class AndAlarmExpression(vim.alarm.AlarmExpression): # vim.alarm.AndAlarmExpression
         expression = [ vim.alarm.AlarmExpression() ]

      class GroupAlarmAction(vim.alarm.AlarmAction): # vim.alarm.GroupAlarmAction
         action = [ vim.alarm.AlarmAction() ]

      class MetricAlarmExpression(vim.alarm.AlarmExpression): # vim.alarm.MetricAlarmExpression
         operator = vim.alarm.MetricAlarmExpression.MetricOperator()
         type = vmodl.TypeName()
         metric = vim.PerformanceManager.MetricId()
         yellow = 0
         yellowInterval = 0
         red = 0
         redInterval = 0

         class MetricOperator(Enum): # vim.alarm.MetricAlarmExpression.MetricOperator
            isAbove = 0
            isBelow = 1

      class OrAlarmExpression(vim.alarm.AlarmExpression): # vim.alarm.OrAlarmExpression
         expression = [ vim.alarm.AlarmExpression() ]

      class StateAlarmExpression(vim.alarm.AlarmExpression): # vim.alarm.StateAlarmExpression
         operator = vim.alarm.StateAlarmExpression.StateOperator()
         type = vmodl.TypeName()
         statePath = vmodl.PropertyPath()
         yellow = ""
         red = ""

         class StateOperator(Enum): # vim.alarm.StateAlarmExpression.StateOperator
            isEqual = 0
            isUnequal = 1

      class AlarmFilterSpec(vmodl.DynamicData): # vim.alarm.AlarmFilterSpec
         status = [ vim.ManagedEntity.Status() ]
         typeEntity = ""
         typeTrigger = ""

         class AlarmTypeByEntity(Enum): # vim.alarm.AlarmFilterSpec.AlarmTypeByEntity
            entityTypeAll = 0
            entityTypeHost = 1
            entityTypeVm = 2

         class AlarmTypeByTrigger(Enum): # vim.alarm.AlarmFilterSpec.AlarmTypeByTrigger
            triggerTypeAll = 0
            triggerTypeEvent = 1
            triggerTypeMetric = 2

      class AlarmInfo(vim.alarm.AlarmSpec): # vim.alarm.AlarmInfo
         key = ""
         alarm = vim.alarm.Alarm()
         entity = vim.ManagedEntity()
         lastModifiedTime = vmodl.DateTime()
         lastModifiedUser = ""
         creationEventId = 0

      class AlarmManager(vmodl.ManagedObject): # vim.alarm.AlarmManager
         defaultExpression = [ vim.alarm.AlarmExpression() ]
         description = vim.alarm.AlarmDescription()

         def create(entity=vim.ManagedEntity(), spec=vim.alarm.AlarmSpec()): # vim.alarm.AlarmManager.create
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.alarm.Alarm()

         def getAlarm(entity=vim.ManagedEntity() or None): # vim.alarm.AlarmManager.getAlarm
            return [ vim.alarm.Alarm() ]

         def getAlarmActionsEnabled(entity=vim.ManagedEntity()): # vim.alarm.AlarmManager.getAlarmActionsEnabled
            return False

         def setAlarmActionsEnabled(entity=vim.ManagedEntity(), enabled=False): # vim.alarm.AlarmManager.setAlarmActionsEnabled
            return None

         def getAlarmState(entity=vim.ManagedEntity()): # vim.alarm.AlarmManager.getAlarmState
            return [ vim.alarm.AlarmState() ]

         def acknowledgeAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()): # vim.alarm.AlarmManager.acknowledgeAlarm
            return None

         def clearTriggeredAlarms(filter=vim.alarm.AlarmFilterSpec()): # vim.alarm.AlarmManager.clearTriggeredAlarms
            return None

         def disableAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()): # vim.alarm.AlarmManager.disableAlarm
            return None

         def enableAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()): # vim.alarm.AlarmManager.enableAlarm
            return None

      class AlarmState(vmodl.DynamicData): # vim.alarm.AlarmState
         key = ""
         entity = vim.ManagedEntity()
         alarm = vim.alarm.Alarm()
         overallStatus = vim.ManagedEntity.Status()
         time = vmodl.DateTime()
         acknowledged = False
         acknowledgedByUser = ""
         acknowledgedTime = vmodl.DateTime()
         eventKey = 0
         disabled = False

      class AlarmTriggeringAction(vim.alarm.AlarmAction): # vim.alarm.AlarmTriggeringAction
         action = vim.action.Action()
         transitionSpecs = [ vim.alarm.AlarmTriggeringAction.TransitionSpec() ]
         green2yellow = False
         yellow2red = False
         red2yellow = False
         yellow2green = False

         class TransitionSpec(vmodl.DynamicData): # vim.alarm.AlarmTriggeringAction.TransitionSpec
            startState = vim.ManagedEntity.Status()
            finalState = vim.ManagedEntity.Status()
            repeats = False

      class EventAlarmExpression(vim.alarm.AlarmExpression): # vim.alarm.EventAlarmExpression
         comparisons = [ vim.alarm.EventAlarmExpression.Comparison() ]
         eventType = vmodl.TypeName()
         eventTypeId = ""
         objectType = vmodl.TypeName()
         status = vim.ManagedEntity.Status()

         class ComparisonOperator(Enum): # vim.alarm.EventAlarmExpression.ComparisonOperator
            equals = 0
            notEqualTo = 1
            startsWith = 2
            doesNotStartWith = 3
            endsWith = 4
            doesNotEndWith = 5

         class Comparison(vmodl.DynamicData): # vim.alarm.EventAlarmExpression.Comparison
            attributeName = ""
            operator = ""
            value = ""

   class cluster(object): # (unknown name)

      class Action(vmodl.DynamicData): # vim.cluster.Action
         type = ""
         target = vmodl.ManagedObject()

         class ActionType(Enum): # vim.cluster.Action.ActionType
            MigrationV1 = 0
            VmPowerV1 = 1
            HostPowerV1 = 2
            IncreaseLimitV1 = 3
            IncreaseSizeV1 = 4
            IncreaseSharesV1 = 5
            IncreaseReservationV1 = 6
            DecreaseOthersReservationV1 = 7
            IncreaseClusterCapacityV1 = 8
            DecreaseMigrationThresholdV1 = 9
            HostMaintenanceV1 = 10
            StorageMigrationV1 = 11
            StoragePlacementV1 = 12
            PlacementV1 = 13
            HostInfraUpdateHaV1 = 14

      class ActionHistory(vmodl.DynamicData): # vim.cluster.ActionHistory
         action = vim.cluster.Action()
         time = vmodl.DateTime()

      class AttemptedVmInfo(vmodl.DynamicData): # vim.cluster.AttemptedVmInfo
         vm = vim.VirtualMachine()
         task = vim.Task()

      class ConfigInfo(vmodl.DynamicData): # vim.cluster.ConfigInfo
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfig = [ vim.cluster.DasVmConfigInfo() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfig = [ vim.cluster.DrsVmConfigInfo() ]
         rule = [ vim.cluster.RuleInfo() ]

      class ConfigSpec(vmodl.DynamicData): # vim.cluster.ConfigSpec
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfigSpec = [ vim.cluster.DasVmConfigSpec() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfigSpec = [ vim.cluster.DrsVmConfigSpec() ]
         rulesSpec = [ vim.cluster.RuleSpec() ]

      class CryptoConfigInfo(vmodl.DynamicData): # vim.cluster.CryptoConfigInfo
         cryptoMode = ""

         class CryptoMode(Enum): # vim.cluster.CryptoConfigInfo.CryptoMode
            onDemand = 0
            forceEnable = 1

      class DasAamNodeState(vmodl.DynamicData): # vim.cluster.DasAamNodeState
         host = vim.HostSystem()
         name = ""
         configState = ""
         runtimeState = ""

         class DasState(Enum): # vim.cluster.DasAamNodeState.DasState
            uninitialized = 0
            initialized = 1
            configuring = 2
            unconfiguring = 3
            running = 4
            error = 5
            agentShutdown = 6
            nodeFailed = 7

      class DasAdmissionControlInfo(vmodl.DynamicData): # vim.cluster.DasAdmissionControlInfo
         pass

      class DasAdmissionControlPolicy(vmodl.DynamicData): # vim.cluster.DasAdmissionControlPolicy
         resourceReductionToToleratePercent = 0

      class DasAdvancedRuntimeInfo(vmodl.DynamicData): # vim.cluster.DasAdvancedRuntimeInfo
         dasHostInfo = vim.cluster.DasHostInfo()
         vmcpSupported = vim.cluster.DasAdvancedRuntimeInfo.VmcpCapabilityInfo()
         heartbeatDatastoreInfo = [ vim.cluster.DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo() ]

         class VmcpCapabilityInfo(vmodl.DynamicData): # vim.cluster.DasAdvancedRuntimeInfo.VmcpCapabilityInfo
            storageAPDSupported = False
            storagePDLSupported = False

         class HeartbeatDatastoreInfo(vmodl.DynamicData): # vim.cluster.DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo
            datastore = vim.Datastore()
            hosts = [ vim.HostSystem() ]

      class DasConfigInfo(vmodl.DynamicData): # vim.cluster.DasConfigInfo
         enabled = False
         vmMonitoring = ""
         hostMonitoring = ""
         vmComponentProtecting = ""
         failoverLevel = 0
         admissionControlPolicy = vim.cluster.DasAdmissionControlPolicy()
         admissionControlEnabled = False
         defaultVmSettings = vim.cluster.DasVmSettings()
         option = [ vim.option.OptionValue() ]
         heartbeatDatastore = [ vim.Datastore() ]
         hBDatastoreCandidatePolicy = ""

         class ServiceState(Enum): # vim.cluster.DasConfigInfo.ServiceState
            disabled = 0
            enabled = 1

         class VmMonitoringState(Enum): # vim.cluster.DasConfigInfo.VmMonitoringState
            vmMonitoringDisabled = 0
            vmMonitoringOnly = 1
            vmAndAppMonitoring = 2

         class HBDatastoreCandidate(Enum): # vim.cluster.DasConfigInfo.HBDatastoreCandidate
            userSelectedDs = 0
            allFeasibleDs = 1
            allFeasibleDsWithUserPreference = 2

      class DasData(vmodl.DynamicData): # vim.cluster.DasData
         pass

      class DasDataSummary(vim.cluster.DasData): # vim.cluster.DasDataSummary
         hostListVersion = 0
         clusterConfigVersion = 0
         compatListVersion = 0

      class DasFailoverLevelAdvancedRuntimeInfo(vim.cluster.DasAdvancedRuntimeInfo): # vim.cluster.DasFailoverLevelAdvancedRuntimeInfo
         slotInfo = vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.SlotInfo()
         totalSlots = 0
         usedSlots = 0
         unreservedSlots = 0
         totalVms = 0
         totalHosts = 0
         totalGoodHosts = 0
         hostSlots = [ vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.HostSlots() ]
         vmsRequiringMultipleSlots = [ vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.VmSlots() ]

         class SlotInfo(vmodl.DynamicData): # vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.SlotInfo
            numVcpus = 0
            cpuMHz = 0
            memoryMB = 0

         class HostSlots(vmodl.DynamicData): # vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.HostSlots
            host = vim.HostSystem()
            slots = 0

         class VmSlots(vmodl.DynamicData): # vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.VmSlots
            vm = vim.VirtualMachine()
            slots = 0

      class DasFdmAvailabilityState(Enum): # vim.cluster.DasFdmAvailabilityState
         uninitialized = 0
         election = 1
         master = 2
         connectedToMaster = 3
         networkPartitionedFromMaster = 4
         networkIsolated = 5
         hostDown = 6
         initializationError = 7
         uninitializationError = 8
         fdmUnreachable = 9

      class DasFdmHostState(vmodl.DynamicData): # vim.cluster.DasFdmHostState
         state = ""
         stateReporter = vim.HostSystem()

      class DasHostInfo(vmodl.DynamicData): # vim.cluster.DasHostInfo
         pass

      class DasHostRecommendation(vmodl.DynamicData): # vim.cluster.DasHostRecommendation
         host = vim.HostSystem()
         drsRating = 0

      class DasVmConfigInfo(vmodl.DynamicData): # vim.cluster.DasVmConfigInfo
         key = vim.VirtualMachine()
         restartPriority = vim.cluster.DasVmConfigInfo.Priority()
         powerOffOnIsolation = False
         dasSettings = vim.cluster.DasVmSettings()

         class Priority(Enum): # vim.cluster.DasVmConfigInfo.Priority
            disabled = 0
            low = 1
            medium = 2
            high = 3

      class DasVmSettings(vmodl.DynamicData): # vim.cluster.DasVmSettings
         restartPriority = ""
         restartPriorityTimeout = 0
         isolationResponse = ""
         vmToolsMonitoringSettings = vim.cluster.VmToolsMonitoringSettings()
         vmComponentProtectionSettings = vim.cluster.VmComponentProtectionSettings()

         class RestartPriority(Enum): # vim.cluster.DasVmSettings.RestartPriority
            disabled = 0
            lowest = 1
            low = 2
            medium = 3
            high = 4
            highest = 5
            clusterRestartPriority = 6

         class IsolationResponse(Enum): # vim.cluster.DasVmSettings.IsolationResponse
            none = 0
            powerOff = 1
            shutdown = 2
            clusterIsolationResponse = 3

      class DpmConfigInfo(vmodl.DynamicData): # vim.cluster.DpmConfigInfo
         enabled = False
         defaultDpmBehavior = vim.cluster.DpmConfigInfo.DpmBehavior()
         hostPowerActionRate = 0
         option = [ vim.option.OptionValue() ]

         class DpmBehavior(Enum): # vim.cluster.DpmConfigInfo.DpmBehavior
            manual = 0
            automated = 1

      class DpmHostConfigInfo(vmodl.DynamicData): # vim.cluster.DpmHostConfigInfo
         key = vim.HostSystem()
         enabled = False
         behavior = vim.cluster.DpmConfigInfo.DpmBehavior()

      class DrsConfigInfo(vmodl.DynamicData): # vim.cluster.DrsConfigInfo
         enabled = False
         enableVmBehaviorOverrides = False
         defaultVmBehavior = vim.cluster.DrsConfigInfo.DrsBehavior()
         vmotionRate = 0
         scaleDescendantsShares = ""
         option = [ vim.option.OptionValue() ]

         class DrsBehavior(Enum): # vim.cluster.DrsConfigInfo.DrsBehavior
            manual = 0
            partiallyAutomated = 1
            fullyAutomated = 2

      class DrsFaults(vmodl.DynamicData): # vim.cluster.DrsFaults
         reason = ""
         faultsByVm = [ vim.cluster.DrsFaults.FaultsByVm() ]

         class FaultsByVm(vmodl.DynamicData): # vim.cluster.DrsFaults.FaultsByVm
            vm = vim.VirtualMachine()
            fault = [ vmodl.MethodFault() ]

         class FaultsByVirtualDisk(vim.cluster.DrsFaults.FaultsByVm): # vim.cluster.DrsFaults.FaultsByVirtualDisk
            disk = vim.vm.device.VirtualDiskId()

      class DrsMigration(vmodl.DynamicData): # vim.cluster.DrsMigration
         key = ""
         time = vmodl.DateTime()
         vm = vim.VirtualMachine()
         cpuLoad = 0
         memoryLoad = 0
         source = vim.HostSystem()
         sourceCpuLoad = 0
         sourceMemoryLoad = 0
         destination = vim.HostSystem()
         destinationCpuLoad = 0
         destinationMemoryLoad = 0

      class DrsRecommendation(vmodl.DynamicData): # vim.cluster.DrsRecommendation
         key = ""
         rating = 0
         reason = ""
         reasonText = ""
         migrationList = [ vim.cluster.DrsMigration() ]

         class ReasonCode(Enum): # vim.cluster.DrsRecommendation.ReasonCode
            fairnessCpuAvg = 0
            fairnessMemAvg = 1
            jointAffin = 2
            antiAffin = 3
            hostMaint = 4

      class DrsVmConfigInfo(vmodl.DynamicData): # vim.cluster.DrsVmConfigInfo
         key = vim.VirtualMachine()
         enabled = False
         behavior = vim.cluster.DrsConfigInfo.DrsBehavior()

      class EVCManager(vim.ExtensibleManagedObject): # vim.cluster.EVCManager
         managedCluster = vim.ClusterComputeResource()
         evcState = vim.cluster.EVCManager.EVCState()

         def configureEvc(evcModeKey=""): # vim.cluster.EVCManager.configureEvc
            # throws vim.fault.EVCConfigFault
            return vim.Task()

         def disableEvc(): # vim.cluster.EVCManager.disableEvc
            return vim.Task()

         def checkConfigureEvc(evcModeKey=""): # vim.cluster.EVCManager.checkConfigureEvc
            return vim.Task()

         def checkAddHostEvc(cnxSpec=vim.host.ConnectSpec()): # vim.cluster.EVCManager.checkAddHostEvc
            # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
            return vim.Task()

         class EVCState(vmodl.DynamicData): # vim.cluster.EVCManager.EVCState
            supportedEVCMode = [ vim.EVCMode() ]
            currentEVCModeKey = ""
            guaranteedCPUFeatures = [ vim.host.CpuIdInfo() ]
            featureCapability = [ vim.host.FeatureCapability() ]
            featureMask = [ vim.host.FeatureMask() ]
            featureRequirement = [ vim.vm.FeatureRequirement() ]

         class CheckResult(vmodl.DynamicData): # vim.cluster.EVCManager.CheckResult
            evcModeKey = ""
            error = vmodl.MethodFault()
            host = [ vim.HostSystem() ]

      class EnterMaintenanceResult(vmodl.DynamicData): # vim.cluster.EnterMaintenanceResult
         recommendations = [ vim.cluster.Recommendation() ]
         fault = vim.cluster.DrsFaults()

      class FailoverHostAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy): # vim.cluster.FailoverHostAdmissionControlPolicy
         failoverHosts = [ vim.HostSystem() ]
         failoverLevel = 0

      class FailoverLevelAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo): # vim.cluster.FailoverLevelAdmissionControlInfo
         currentFailoverLevel = 0

      class FailoverLevelAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy): # vim.cluster.FailoverLevelAdmissionControlPolicy
         failoverLevel = 0
         slotPolicy = vim.cluster.SlotPolicy()

      class FailoverResourcesAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo): # vim.cluster.FailoverResourcesAdmissionControlInfo
         currentCpuFailoverResourcesPercent = 0
         currentMemoryFailoverResourcesPercent = 0

      class FailoverResourcesAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy): # vim.cluster.FailoverResourcesAdmissionControlPolicy
         cpuFailoverResourcesPercent = 0
         memoryFailoverResourcesPercent = 0
         failoverLevel = 0
         autoComputePercentages = False

      class GroupInfo(vmodl.DynamicData): # vim.cluster.GroupInfo
         name = ""
         userCreated = False
         uniqueID = ""

      class HostGroup(vim.cluster.GroupInfo): # vim.cluster.HostGroup
         host = [ vim.HostSystem() ]

      class HostInfraUpdateHaModeAction(vim.cluster.Action): # vim.cluster.HostInfraUpdateHaModeAction
         operationType = ""

         class OperationType(Enum): # vim.cluster.HostInfraUpdateHaModeAction.OperationType
            enterQuarantine = 0
            exitQuarantine = 1
            enterMaintenance = 2

      class HostPowerAction(vim.cluster.Action): # vim.cluster.HostPowerAction
         operationType = vim.cluster.HostPowerAction.OperationType()
         powerConsumptionWatt = 0
         cpuCapacityMHz = 0
         memCapacityMB = 0

         class OperationType(Enum): # vim.cluster.HostPowerAction.OperationType
            powerOn = 0
            powerOff = 1

      class HostRecommendation(vmodl.DynamicData): # vim.cluster.HostRecommendation
         host = vim.HostSystem()
         rating = 0

      class InfraUpdateHaConfigInfo(vmodl.DynamicData): # vim.cluster.InfraUpdateHaConfigInfo
         enabled = False
         behavior = ""
         moderateRemediation = ""
         severeRemediation = ""
         providers = [ "" ]

         class BehaviorType(Enum): # vim.cluster.InfraUpdateHaConfigInfo.BehaviorType
            Manual = 0
            Automated = 1

         class RemediationType(Enum): # vim.cluster.InfraUpdateHaConfigInfo.RemediationType
            QuarantineMode = 0
            MaintenanceMode = 1

      class InitialPlacementAction(vim.cluster.Action): # vim.cluster.InitialPlacementAction
         targetHost = vim.HostSystem()
         pool = vim.ResourcePool()

      class MigrationAction(vim.cluster.Action): # vim.cluster.MigrationAction
         drsMigration = vim.cluster.DrsMigration()

      class NotAttemptedVmInfo(vmodl.DynamicData): # vim.cluster.NotAttemptedVmInfo
         vm = vim.VirtualMachine()
         fault = vmodl.MethodFault()

      class OrchestrationInfo(vmodl.DynamicData): # vim.cluster.OrchestrationInfo
         defaultVmReadiness = vim.cluster.VmReadiness()

      class PlacementAction(vim.cluster.Action): # vim.cluster.PlacementAction
         vm = vim.VirtualMachine()
         targetHost = vim.HostSystem()
         relocateSpec = vim.vm.RelocateSpec()

      class PlacementResult(vmodl.DynamicData): # vim.cluster.PlacementResult
         recommendations = [ vim.cluster.Recommendation() ]
         drsFault = vim.cluster.DrsFaults()

      class PowerOnVmOption(Enum): # vim.cluster.PowerOnVmOption
         OverrideAutomationLevel = 0
         ReserveResources = 1

      class PowerOnVmResult(vmodl.DynamicData): # vim.cluster.PowerOnVmResult
         attempted = [ vim.cluster.AttemptedVmInfo() ]
         notAttempted = [ vim.cluster.NotAttemptedVmInfo() ]
         recommendations = [ vim.cluster.Recommendation() ]

      class ProactiveDrsConfigInfo(vmodl.DynamicData): # vim.cluster.ProactiveDrsConfigInfo
         enabled = False

      class Recommendation(vmodl.DynamicData): # vim.cluster.Recommendation
         key = ""
         type = ""
         time = vmodl.DateTime()
         rating = 0
         reason = ""
         reasonText = ""
         warningText = ""
         warningDetails = vmodl.LocalizableMessage()
         prerequisite = [ "" ]
         action = [ vim.cluster.Action() ]
         target = vmodl.ManagedObject()

         class RecommendationType(Enum): # vim.cluster.Recommendation.RecommendationType
            V1 = 0

         class ReasonCode(Enum): # vim.cluster.Recommendation.ReasonCode
            fairnessCpuAvg = 0
            fairnessMemAvg = 1
            jointAffin = 2
            antiAffin = 3
            hostMaint = 4
            enterStandby = 5
            reservationCpu = 6
            reservationMem = 7
            powerOnVm = 8
            powerSaving = 9
            increaseCapacity = 10
            checkResource = 11
            unreservedCapacity = 12
            colocateCommunicatingVM = 13
            balanceNetworkBandwidthUsage = 14
            vmHostHardAffinity = 15
            vmHostSoftAffinity = 16
            increaseAllocation = 17
            balanceDatastoreSpaceUsage = 18
            balanceDatastoreIOLoad = 19
            balanceDatastoreIOPSReservation = 20
            datastoreMaint = 21
            virtualDiskJointAffin = 22
            virtualDiskAntiAffin = 23
            datastoreSpaceOutage = 24
            storagePlacement = 25
            iolbDisabledInternal = 26
            xvmotionPlacement = 27
            networkBandwidthReservation = 28
            hostInDegradation = 29
            hostExitDegradation = 30
            maxVmsConstraint = 31
            ftConstraints = 32
            vmHostAffinityPolicy = 33
            vmHostAntiAffinityPolicy = 34
            vmAntiAffinityPolicy = 35
            predictiveDRS = 36
            balanceVsanUsage = 37

      class ResourceUsageSummary(vmodl.DynamicData): # vim.cluster.ResourceUsageSummary
         cpuUsedMHz = 0
         cpuCapacityMHz = 0
         memUsedMB = 0
         memCapacityMB = 0
         pMemAvailableMB = 0
         pMemCapacityMB = 0
         storageUsedMB = 0
         storageCapacityMB = 0

      class SlotPolicy(vmodl.DynamicData): # vim.cluster.SlotPolicy
         pass

      class UsageSummary(vmodl.DynamicData): # vim.cluster.UsageSummary
         totalCpuCapacityMhz = 0
         totalMemCapacityMB = 0
         cpuReservationMhz = 0
         memReservationMB = 0
         poweredOffCpuReservationMhz = 0
         poweredOffMemReservationMB = 0
         cpuDemandMhz = 0
         memDemandMB = 0
         statsGenNumber = 0
         cpuEntitledMhz = 0
         memEntitledMB = 0
         poweredOffVmCount = 0
         totalVmCount = 0

      class VmComponentProtectionSettings(vmodl.DynamicData): # vim.cluster.VmComponentProtectionSettings
         vmStorageProtectionForAPD = ""
         enableAPDTimeoutForHosts = False
         vmTerminateDelayForAPDSec = 0
         vmReactionOnAPDCleared = ""
         vmStorageProtectionForPDL = ""

         class StorageVmReaction(Enum): # vim.cluster.VmComponentProtectionSettings.StorageVmReaction
            disabled = 0
            warning = 1
            restartConservative = 2
            restartAggressive = 3
            clusterDefault = 4

         class VmReactionOnAPDCleared(Enum): # vim.cluster.VmComponentProtectionSettings.VmReactionOnAPDCleared
            none = 0
            reset = 1
            useClusterDefault = 2

      class VmGroup(vim.cluster.GroupInfo): # vim.cluster.VmGroup
         vm = [ vim.VirtualMachine() ]

      class VmOrchestrationInfo(vmodl.DynamicData): # vim.cluster.VmOrchestrationInfo
         vm = vim.VirtualMachine()
         vmReadiness = vim.cluster.VmReadiness()

      class VmReadiness(vmodl.DynamicData): # vim.cluster.VmReadiness
         readyCondition = ""
         postReadyDelay = 0

         class ReadyCondition(Enum): # vim.cluster.VmReadiness.ReadyCondition
            none = 0
            poweredOn = 1
            guestHbStatusGreen = 2
            appHbStatusGreen = 3
            useClusterDefault = 4

      class VmToolsMonitoringSettings(vmodl.DynamicData): # vim.cluster.VmToolsMonitoringSettings
         enabled = False
         vmMonitoring = ""
         clusterSettings = False
         failureInterval = 0
         minUpTime = 0
         maxFailures = 0
         maxFailureWindow = 0

      class DasAamHostInfo(vim.cluster.DasHostInfo): # vim.cluster.DasAamHostInfo
         hostDasState = [ vim.cluster.DasAamNodeState() ]
         primaryHosts = [ "" ]

      class DasVmConfigSpec(vim.option.ArrayUpdateSpec): # vim.cluster.DasVmConfigSpec
         info = vim.cluster.DasVmConfigInfo()

      class DpmHostConfigSpec(vim.option.ArrayUpdateSpec): # vim.cluster.DpmHostConfigSpec
         info = vim.cluster.DpmHostConfigInfo()

      class DrsVmConfigSpec(vim.option.ArrayUpdateSpec): # vim.cluster.DrsVmConfigSpec
         info = vim.cluster.DrsVmConfigInfo()

      class FailoverHostAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo): # vim.cluster.FailoverHostAdmissionControlInfo
         hostStatus = [ vim.cluster.FailoverHostAdmissionControlInfo.HostStatus() ]

         class HostStatus(vmodl.DynamicData): # vim.cluster.FailoverHostAdmissionControlInfo.HostStatus
            host = vim.HostSystem()
            status = vim.ManagedEntity.Status()

      class FixedSizeSlotPolicy(vim.cluster.SlotPolicy): # vim.cluster.FixedSizeSlotPolicy
         cpu = 0
         memory = 0

      class GroupSpec(vim.option.ArrayUpdateSpec): # vim.cluster.GroupSpec
         info = vim.cluster.GroupInfo()

      class PlacementSpec(vmodl.DynamicData): # vim.cluster.PlacementSpec
         priority = vim.VirtualMachine.MovePriority()
         vm = vim.VirtualMachine()
         configSpec = vim.vm.ConfigSpec()
         relocateSpec = vim.vm.RelocateSpec()
         hosts = [ vim.HostSystem() ]
         datastores = [ vim.Datastore() ]
         storagePods = [ vim.StoragePod() ]
         disallowPrerequisiteMoves = False
         rules = [ vim.cluster.RuleInfo() ]
         key = ""
         placementType = ""
         cloneSpec = vim.vm.CloneSpec()
         cloneName = ""

         class PlacementType(Enum): # vim.cluster.PlacementSpec.PlacementType
            create = 0
            reconfigure = 1
            relocate = 2
            clone = 3

      class RuleInfo(vmodl.DynamicData): # vim.cluster.RuleInfo
         key = 0
         status = vim.ManagedEntity.Status()
         enabled = False
         name = ""
         mandatory = False
         userCreated = False
         inCompliance = False
         ruleUuid = ""

      class RuleSpec(vim.option.ArrayUpdateSpec): # vim.cluster.RuleSpec
         info = vim.cluster.RuleInfo()

      class VmHostRuleInfo(vim.cluster.RuleInfo): # vim.cluster.VmHostRuleInfo
         vmGroupName = ""
         affineHostGroupName = ""
         antiAffineHostGroupName = ""

      class VmOrchestrationSpec(vim.option.ArrayUpdateSpec): # vim.cluster.VmOrchestrationSpec
         info = vim.cluster.VmOrchestrationInfo()

      class AffinityRuleSpec(vim.cluster.RuleInfo): # vim.cluster.AffinityRuleSpec
         vm = [ vim.VirtualMachine() ]

      class AntiAffinityRuleSpec(vim.cluster.RuleInfo): # vim.cluster.AntiAffinityRuleSpec
         vm = [ vim.VirtualMachine() ]

      class ConfigInfoEx(vim.ComputeResource.ConfigInfo): # vim.cluster.ConfigInfoEx
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfig = [ vim.cluster.DasVmConfigInfo() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfig = [ vim.cluster.DrsVmConfigInfo() ]
         rule = [ vim.cluster.RuleInfo() ]
         orchestration = vim.cluster.OrchestrationInfo()
         vmOrchestration = [ vim.cluster.VmOrchestrationInfo() ]
         dpmConfigInfo = vim.cluster.DpmConfigInfo()
         dpmHostConfig = [ vim.cluster.DpmHostConfigInfo() ]
         vsanConfigInfo = vim.vsan.cluster.ConfigInfo()
         vsanHostConfig = [ vim.vsan.host.ConfigInfo() ]
         group = [ vim.cluster.GroupInfo() ]
         infraUpdateHaConfig = vim.cluster.InfraUpdateHaConfigInfo()
         proactiveDrsConfig = vim.cluster.ProactiveDrsConfigInfo()
         cryptoConfig = vim.cluster.CryptoConfigInfo()

      class ConfigSpecEx(vim.ComputeResource.ConfigSpec): # vim.cluster.ConfigSpecEx
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfigSpec = [ vim.cluster.DasVmConfigSpec() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfigSpec = [ vim.cluster.DrsVmConfigSpec() ]
         rulesSpec = [ vim.cluster.RuleSpec() ]
         orchestration = vim.cluster.OrchestrationInfo()
         vmOrchestrationSpec = [ vim.cluster.VmOrchestrationSpec() ]
         dpmConfig = vim.cluster.DpmConfigInfo()
         dpmHostConfigSpec = [ vim.cluster.DpmHostConfigSpec() ]
         vsanConfig = vim.vsan.cluster.ConfigInfo()
         vsanHostConfigSpec = [ vim.vsan.host.ConfigInfo() ]
         groupSpec = [ vim.cluster.GroupSpec() ]
         infraUpdateHaConfig = vim.cluster.InfraUpdateHaConfigInfo()
         proactiveDrsConfig = vim.cluster.ProactiveDrsConfigInfo()
         inHciWorkflow = False
         cryptoConfig = vim.cluster.CryptoConfigInfo()

      class DependencyRuleInfo(vim.cluster.RuleInfo): # vim.cluster.DependencyRuleInfo
         vmGroup = ""
         dependsOnVmGroup = ""

   class dvs(object): # (unknown name)

      class DistributedVirtualPort(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort
         key = ""
         config = vim.dvs.DistributedVirtualPort.ConfigInfo()
         dvsUuid = ""
         portgroupKey = ""
         proxyHost = vim.HostSystem()
         connectee = vim.dvs.PortConnectee()
         conflict = False
         conflictPortKey = ""
         state = vim.dvs.DistributedVirtualPort.State()
         connectionCookie = 0
         lastStatusChange = vmodl.DateTime()
         hostLocalPort = False
         externalId = ""
         segmentPortId = ""

         class ConfigSpec(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.ConfigSpec
            operation = ""
            key = ""
            name = ""
            scope = [ vim.ManagedEntity() ]
            description = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            configVersion = ""

         class ConfigInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.ConfigInfo
            name = ""
            scope = [ vim.ManagedEntity() ]
            description = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            configVersion = ""

         class TrafficShapingPolicy(vim.InheritablePolicy): # vim.dvs.DistributedVirtualPort.TrafficShapingPolicy
            enabled = vim.BoolPolicy()
            averageBandwidth = vim.LongPolicy()
            peakBandwidth = vim.LongPolicy()
            burstSize = vim.LongPolicy()

         class HostLocalPortInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.HostLocalPortInfo
            switchUuid = ""
            portKey = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            vnic = ""

         class VendorSpecificConfig(vim.InheritablePolicy): # vim.dvs.DistributedVirtualPort.VendorSpecificConfig
            keyValue = [ vim.dvs.KeyedOpaqueBlob() ]

         class FilterParameter(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.FilterParameter
            parameters = [ "" ]

         class FilterOnFailure(Enum): # vim.dvs.DistributedVirtualPort.FilterOnFailure
            failOpen = 0
            failClosed = 1

         class FilterConfig(vim.InheritablePolicy): # vim.dvs.DistributedVirtualPort.FilterConfig
            key = ""
            agentName = ""
            slotNumber = ""
            parameters = vim.dvs.DistributedVirtualPort.FilterParameter()
            onFailure = ""

         class TrafficFilterConfig(vim.dvs.DistributedVirtualPort.FilterConfig): # vim.dvs.DistributedVirtualPort.TrafficFilterConfig
            trafficRuleset = vim.dvs.TrafficRuleset()

         class FilterConfigSpec(vim.dvs.DistributedVirtualPort.FilterConfig): # vim.dvs.DistributedVirtualPort.FilterConfigSpec
            operation = ""

         class TrafficFilterConfigSpec(vim.dvs.DistributedVirtualPort.TrafficFilterConfig): # vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec
            operation = ""

         class FilterPolicy(vim.InheritablePolicy): # vim.dvs.DistributedVirtualPort.FilterPolicy
            filterConfig = [ vim.dvs.DistributedVirtualPort.FilterConfig() ]

         class Setting(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.Setting
            blocked = vim.BoolPolicy()
            vmDirectPathGen2Allowed = vim.BoolPolicy()
            inShapingPolicy = vim.dvs.DistributedVirtualPort.TrafficShapingPolicy()
            outShapingPolicy = vim.dvs.DistributedVirtualPort.TrafficShapingPolicy()
            vendorSpecificConfig = vim.dvs.DistributedVirtualPort.VendorSpecificConfig()
            networkResourcePoolKey = vim.StringPolicy()
            filterPolicy = vim.dvs.DistributedVirtualPort.FilterPolicy()

         class RuntimeInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.RuntimeInfo
            linkUp = False
            blocked = False
            vlanIds = [ vim.NumericRange() ]
            trunkingMode = False
            mtu = 0
            linkPeer = ""
            macAddress = ""
            statusDetail = ""
            vmDirectPathGen2Active = False
            vmDirectPathGen2InactiveReasonNetwork = [ "" ]
            vmDirectPathGen2InactiveReasonOther = [ "" ]
            vmDirectPathGen2InactiveReasonExtended = ""

            class VmDirectPathGen2InactiveReasonNetwork(Enum): # vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonNetwork
               portNptIncompatibleDvs = 0
               portNptNoCompatibleNics = 1
               portNptNoVirtualFunctionsAvailable = 2
               portNptDisabledForPort = 3

            class VmDirectPathGen2InactiveReasonOther(Enum): # vim.dvs.DistributedVirtualPort.RuntimeInfo.VmDirectPathGen2InactiveReasonOther
               portNptIncompatibleHost = 0
               portNptIncompatibleConnectee = 1

         class State(vmodl.DynamicData): # vim.dvs.DistributedVirtualPort.State
            runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
            stats = vim.dvs.PortStatistics()
            vendorSpecificState = [ vim.dvs.KeyedOpaqueBlob() ]

      class DistributedVirtualPortgroupInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroupInfo
         switchName = ""
         switchUuid = ""
         portgroupName = ""
         portgroupKey = ""
         portgroupType = ""
         uplinkPortgroup = False
         portgroup = vim.dvs.DistributedVirtualPortgroup()
         networkReservationSupported = False
         backingType = ""
         logicalSwitchUuid = ""
         segmentId = ""

      class DistributedVirtualPortgroupSelection(vim.SelectionSet): # vim.dvs.DistributedVirtualPortgroupSelection
         dvsUuid = ""
         portgroupKey = [ "" ]

      class DistributedVirtualSwitchInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchInfo
         switchName = ""
         switchUuid = ""
         distributedVirtualSwitch = vim.DistributedVirtualSwitch()
         networkReservationSupported = False

      class DistributedVirtualSwitchSelection(vim.SelectionSet): # vim.dvs.DistributedVirtualSwitchSelection
         dvsUuid = ""

      class EntityBackup(vmodl.DynamicData): # vim.dvs.EntityBackup

         class Config(vmodl.DynamicData): # vim.dvs.EntityBackup.Config
            entityType = ""
            configBlob = vmodl.Binary()
            key = ""
            name = ""
            container = vim.ManagedEntity()
            configVersion = ""

         class EntityType(Enum): # vim.dvs.EntityBackup.EntityType
            distributedVirtualSwitch = 0
            distributedVirtualPortgroup = 1

         class ImportType(Enum): # vim.dvs.EntityBackup.ImportType
            createEntityWithNewIdentifier = 0
            createEntityWithOriginalIdentifier = 1
            applyToEntitySpecified = 2

      class HostMember(vmodl.DynamicData): # vim.dvs.HostMember
         runtimeState = vim.dvs.HostMember.RuntimeState()
         config = vim.dvs.HostMember.ConfigInfo()
         productInfo = vim.dvs.ProductSpec()
         uplinkPortKey = [ "" ]
         status = ""
         statusDetail = ""

         class HostComponentState(Enum): # vim.dvs.HostMember.HostComponentState
            up = 0
            pending = 1
            outOfSync = 2
            warning = 3
            disconnected = 4
            down = 5

         class ConfigSpec(vmodl.DynamicData): # vim.dvs.HostMember.ConfigSpec
            operation = ""
            host = vim.HostSystem()
            backing = vim.dvs.HostMember.Backing()
            maxProxySwitchPorts = 0
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]

         class PnicSpec(vmodl.DynamicData): # vim.dvs.HostMember.PnicSpec
            pnicDevice = ""
            uplinkPortKey = ""
            uplinkPortgroupKey = ""
            connectionCookie = 0

         class Backing(vmodl.DynamicData): # vim.dvs.HostMember.Backing
            pass

         class PnicBacking(vim.dvs.HostMember.Backing): # vim.dvs.HostMember.PnicBacking
            pnicSpec = [ vim.dvs.HostMember.PnicSpec() ]

         class RuntimeState(vmodl.DynamicData): # vim.dvs.HostMember.RuntimeState
            currentMaxProxySwitchPorts = 0

         class TransportZoneType(Enum): # vim.dvs.HostMember.TransportZoneType
            vlan = 0
            overlay = 1

         class TransportZoneInfo(vmodl.DynamicData): # vim.dvs.HostMember.TransportZoneInfo
            uuid = ""
            type = ""

         class ConfigInfo(vmodl.DynamicData): # vim.dvs.HostMember.ConfigInfo
            host = vim.HostSystem()
            maxProxySwitchPorts = 0
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
            backing = vim.dvs.HostMember.Backing()
            nsxSwitch = False
            ensEnabled = False
            ensInterruptEnabled = False
            transportZones = [ vim.dvs.HostMember.TransportZoneInfo() ]
            nsxtUsedUplinkNames = [ "" ]

         class RuntimeInfo(vmodl.DynamicData): # vim.dvs.HostMember.RuntimeInfo
            host = vim.HostSystem()
            status = ""
            statusDetail = ""
            nsxtStatus = ""
            nsxtStatusDetail = ""
            healthCheckResult = [ vim.dvs.HostMember.HealthCheckResult() ]

         class HealthCheckResult(vmodl.DynamicData): # vim.dvs.HostMember.HealthCheckResult
            summary = ""

         class UplinkHealthCheckResult(vim.dvs.HostMember.HealthCheckResult): # vim.dvs.HostMember.UplinkHealthCheckResult
            uplinkPortKey = ""

      class HostProductSpec(vmodl.DynamicData): # vim.dvs.HostProductSpec
         productLineId = ""
         version = ""

      class KeyedOpaqueBlob(vmodl.DynamicData): # vim.dvs.KeyedOpaqueBlob
         key = ""
         opaqueData = ""

      class NetworkResourcePool(vmodl.DynamicData): # vim.dvs.NetworkResourcePool
         key = ""
         name = ""
         description = ""
         configVersion = ""
         allocationInfo = vim.dvs.NetworkResourcePool.AllocationInfo()

         class AllocationInfo(vmodl.DynamicData): # vim.dvs.NetworkResourcePool.AllocationInfo
            limit = 0
            shares = vim.SharesInfo()
            priorityTag = 0

         class ConfigSpec(vmodl.DynamicData): # vim.dvs.NetworkResourcePool.ConfigSpec
            key = ""
            configVersion = ""
            allocationInfo = vim.dvs.NetworkResourcePool.AllocationInfo()
            name = ""
            description = ""

      class PortConnectee(vmodl.DynamicData): # vim.dvs.PortConnectee
         connectedEntity = vim.ManagedEntity()
         nicKey = ""
         type = ""
         addressHint = ""

         class ConnecteeType(Enum): # vim.dvs.PortConnectee.ConnecteeType
            pnic = 0
            vmVnic = 1
            hostConsoleVnic = 2
            hostVmkVnic = 3

      class PortConnection(vmodl.DynamicData): # vim.dvs.PortConnection
         switchUuid = ""
         portgroupKey = ""
         portKey = ""
         connectionCookie = 0

      class PortCriteria(vmodl.DynamicData): # vim.dvs.PortCriteria
         connected = False
         active = False
         uplinkPort = False
         nsxPort = False
         scope = vim.ManagedEntity()
         portgroupKey = [ "" ]
         inside = False
         portKey = [ "" ]
         host = [ vim.HostSystem() ]

      class PortStatistics(vmodl.DynamicData): # vim.dvs.PortStatistics
         packetsInMulticast = 0
         packetsOutMulticast = 0
         bytesInMulticast = 0
         bytesOutMulticast = 0
         packetsInUnicast = 0
         packetsOutUnicast = 0
         bytesInUnicast = 0
         bytesOutUnicast = 0
         packetsInBroadcast = 0
         packetsOutBroadcast = 0
         bytesInBroadcast = 0
         bytesOutBroadcast = 0
         packetsInDropped = 0
         packetsOutDropped = 0
         packetsInException = 0
         packetsOutException = 0
         bytesInFromPnic = 0
         bytesOutToPnic = 0

      class ProductSpec(vmodl.DynamicData): # vim.dvs.ProductSpec
         name = ""
         vendor = ""
         version = ""
         build = ""
         forwardingClass = ""
         bundleId = ""
         bundleUrl = ""

      class TrafficRule(vmodl.DynamicData): # vim.dvs.TrafficRule
         key = ""
         description = ""
         sequence = 0
         qualifier = [ vim.dvs.TrafficRule.Qualifier() ]
         action = vim.dvs.TrafficRule.Action()
         direction = ""

         class Qualifier(vmodl.DynamicData): # vim.dvs.TrafficRule.Qualifier
            key = ""

         class Action(vmodl.DynamicData): # vim.dvs.TrafficRule.Action
            pass

         class RuleDirectionType(Enum): # vim.dvs.TrafficRule.RuleDirectionType
            incomingPackets = 0
            outgoingPackets = 1
            both = 2

         class IpQualifier(vim.dvs.TrafficRule.Qualifier): # vim.dvs.TrafficRule.IpQualifier
            sourceAddress = vim.IpAddress()
            destinationAddress = vim.IpAddress()
            protocol = vim.IntExpression()
            sourceIpPort = vim.dvs.TrafficRule.IpPort()
            destinationIpPort = vim.dvs.TrafficRule.IpPort()
            tcpFlags = vim.IntExpression()

         class IpPort(vim.NegatableExpression): # vim.dvs.TrafficRule.IpPort
            pass

         class SingleIpPort(vim.dvs.TrafficRule.IpPort): # vim.dvs.TrafficRule.SingleIpPort
            portNumber = 0

         class IpPortRange(vim.dvs.TrafficRule.IpPort): # vim.dvs.TrafficRule.IpPortRange
            startPortNumber = 0
            endPortNumber = 0

         class MacQualifier(vim.dvs.TrafficRule.Qualifier): # vim.dvs.TrafficRule.MacQualifier
            sourceAddress = vim.MacAddress()
            destinationAddress = vim.MacAddress()
            protocol = vim.IntExpression()
            vlanId = vim.IntExpression()

         class SystemTrafficQualifier(vim.dvs.TrafficRule.Qualifier): # vim.dvs.TrafficRule.SystemTrafficQualifier
            typeOfSystemTraffic = vim.StringExpression()

         class DropAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.DropAction
            pass

         class AcceptAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.AcceptAction
            pass

         class UpdateTagAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.UpdateTagAction
            qosTag = 0
            dscpTag = 0

         class RateLimitAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.RateLimitAction
            packetsPerSecond = 0

         class LogAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.LogAction
            pass

         class GreAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.GreAction
            encapsulationIp = vim.SingleIp()

         class MacRewriteAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.MacRewriteAction
            rewriteMac = ""

         class PuntAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.PuntAction
            pass

         class CopyAction(vim.dvs.TrafficRule.Action): # vim.dvs.TrafficRule.CopyAction
            pass

      class TrafficRuleset(vmodl.DynamicData): # vim.dvs.TrafficRuleset
         key = ""
         enabled = False
         precedence = 0
         rules = [ vim.dvs.TrafficRule() ]

      class VmVnicNetworkResourcePool(vmodl.DynamicData): # vim.dvs.VmVnicNetworkResourcePool
         key = ""
         name = ""
         description = ""
         configVersion = ""
         allocationInfo = vim.dvs.VmVnicNetworkResourcePool.ResourceAllocation()

         class ResourceAllocation(vmodl.DynamicData): # vim.dvs.VmVnicNetworkResourcePool.ResourceAllocation
            reservationQuota = 0

         class ConfigSpec(vmodl.DynamicData): # vim.dvs.VmVnicNetworkResourcePool.ConfigSpec
            operation = ""
            key = ""
            configVersion = ""
            allocationInfo = vim.dvs.VmVnicNetworkResourcePool.ResourceAllocation()
            name = ""
            description = ""

         class VnicAllocatedResource(vmodl.DynamicData): # vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource
            vm = vim.VirtualMachine()
            vnicKey = ""
            reservation = 0

         class RuntimeInfo(vmodl.DynamicData): # vim.dvs.VmVnicNetworkResourcePool.RuntimeInfo
            key = ""
            name = ""
            capacity = 0
            usage = 0
            available = 0
            status = ""
            allocatedResource = [ vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource() ]

      class DistributedVirtualPortgroup(vim.Network): # vim.dvs.DistributedVirtualPortgroup
         key = ""
         config = vim.dvs.DistributedVirtualPortgroup.ConfigInfo()
         portKeys = [ "" ]

         def reconfigure(spec=vim.dvs.DistributedVirtualPortgroup.ConfigSpec()): # vim.dvs.DistributedVirtualPortgroup.reconfigure
            # throws vim.fault.DvsFault, vim.fault.ConcurrentAccess, vim.fault.DuplicateName, vim.fault.InvalidName
            return vim.Task()

         def rollback(entityBackup=vim.dvs.EntityBackup.Config() or None): # vim.dvs.DistributedVirtualPortgroup.rollback
            # throws vim.fault.DvsFault, vim.fault.RollbackFailure
            return vim.Task()

         class PortgroupType(Enum): # vim.dvs.DistributedVirtualPortgroup.PortgroupType
            earlyBinding = 0
            lateBinding = 1
            ephemeral = 2

         class BackingType(Enum): # vim.dvs.DistributedVirtualPortgroup.BackingType
            standard = 0
            nsx = 1

         class PortgroupPolicy(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy
            blockOverrideAllowed = False
            shapingOverrideAllowed = False
            vendorConfigOverrideAllowed = False
            livePortMovingAllowed = False
            portConfigResetAtDisconnect = False
            networkResourcePoolOverrideAllowed = False
            trafficFilterOverrideAllowed = False

         class MetaTagName(Enum): # vim.dvs.DistributedVirtualPortgroup.MetaTagName
            dvsName = 0
            portgroupName = 1
            portIndex = 2

         class ConfigSpec(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroup.ConfigSpec
            configVersion = ""
            name = ""
            numPorts = 0
            portNameFormat = ""
            defaultPortConfig = vim.dvs.DistributedVirtualPort.Setting()
            description = ""
            type = ""
            backingType = ""
            scope = [ vim.ManagedEntity() ]
            policy = vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy()
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
            autoExpand = False
            vmVnicNetworkResourcePoolKey = ""
            transportZoneUuid = ""
            transportZoneName = ""
            logicalSwitchUuid = ""
            segmentId = ""

         class ConfigInfo(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroup.ConfigInfo
            key = ""
            name = ""
            numPorts = 0
            distributedVirtualSwitch = vim.DistributedVirtualSwitch()
            defaultPortConfig = vim.dvs.DistributedVirtualPort.Setting()
            description = ""
            type = ""
            backingType = ""
            policy = vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy()
            portNameFormat = ""
            scope = [ vim.ManagedEntity() ]
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
            configVersion = ""
            autoExpand = False
            vmVnicNetworkResourcePoolKey = ""
            uplink = False
            transportZoneUuid = ""
            transportZoneName = ""
            logicalSwitchUuid = ""
            segmentId = ""

         class Problem(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroup.Problem
            logicalSwitchUuid = ""
            fault = vmodl.MethodFault()

         class NsxPortgroupOperationResult(vmodl.DynamicData): # vim.dvs.DistributedVirtualPortgroup.NsxPortgroupOperationResult
            portgroups = [ vim.dvs.DistributedVirtualPortgroup() ]
            problems = [ vim.dvs.DistributedVirtualPortgroup.Problem() ]

      class DistributedVirtualSwitchManager(vmodl.ManagedObject): # vim.dvs.DistributedVirtualSwitchManager

         def querySupportedSwitchSpec(recommended=False or None): # vim.dvs.DistributedVirtualSwitchManager.querySupportedSwitchSpec
            return [ vim.dvs.ProductSpec() ]

         def queryCompatibleHostForNewDvs(container=vim.ManagedEntity(), recursive=False, switchProductSpec=vim.dvs.ProductSpec() or None): # vim.dvs.DistributedVirtualSwitchManager.queryCompatibleHostForNewDvs
            return [ vim.HostSystem() ]

         def queryCompatibleHostForExistingDvs(container=vim.ManagedEntity(), recursive=False, dvs=vim.DistributedVirtualSwitch()): # vim.dvs.DistributedVirtualSwitchManager.queryCompatibleHostForExistingDvs
            return [ vim.HostSystem() ]

         def queryCompatibleHostSpec(switchProductSpec=vim.dvs.ProductSpec() or None): # vim.dvs.DistributedVirtualSwitchManager.queryCompatibleHostSpec
            return [ vim.dvs.HostProductSpec() ]

         def queryFeatureCapability(switchProductSpec=vim.dvs.ProductSpec() or None): # vim.dvs.DistributedVirtualSwitchManager.queryFeatureCapability
            return vim.DistributedVirtualSwitch.FeatureCapability()

         def querySwitchByUuid(uuid=""): # vim.dvs.DistributedVirtualSwitchManager.querySwitchByUuid
            # throws vim.fault.NotFound
            return vim.DistributedVirtualSwitch()

         def queryDvsConfigTarget(host=vim.HostSystem() or None, dvs=vim.DistributedVirtualSwitch() or None): # vim.dvs.DistributedVirtualSwitchManager.queryDvsConfigTarget
            return vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget()

         def checkCompatibility(hostContainer=vim.dvs.DistributedVirtualSwitchManager.HostContainer(), dvsProductSpec=vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec() or None, hostFilterSpec=[ vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec() ] or None): # vim.dvs.DistributedVirtualSwitchManager.checkCompatibility
            return [ vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult() ]

         def rectifyHost(hosts=[ vim.HostSystem() ]): # vim.dvs.DistributedVirtualSwitchManager.rectifyHost
            # throws vim.fault.DvsFault
            return vim.Task()

         def exportEntity(selectionSet=[ vim.SelectionSet() ]): # vim.dvs.DistributedVirtualSwitchManager.exportEntity
            # throws vim.fault.NotFound, vim.fault.BackupBlobWriteFailure
            return vim.Task()

         def importEntity(entityBackup=[ vim.dvs.EntityBackup.Config() ], importType=""): # vim.dvs.DistributedVirtualSwitchManager.importEntity
            # throws vim.fault.DvsFault, vim.fault.NotFound
            return vim.Task()

         def lookupPortgroup(switchUuid="", portgroupKey=""): # vim.dvs.DistributedVirtualSwitchManager.lookupPortgroup
            # throws vim.fault.NotFound
            return vim.dvs.DistributedVirtualPortgroup()

         class DvsConfigTarget(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget
            distributedVirtualPortgroup = [ vim.dvs.DistributedVirtualPortgroupInfo() ]
            distributedVirtualSwitch = [ vim.dvs.DistributedVirtualSwitchInfo() ]

         class CompatibilityResult(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult
            host = vim.HostSystem()
            error = [ vmodl.MethodFault() ]

         class HostContainer(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.HostContainer
            container = vim.ManagedEntity()
            recursive = False

         class HostDvsFilterSpec(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec
            inclusive = False

         class HostArrayFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec): # vim.dvs.DistributedVirtualSwitchManager.HostArrayFilter
            host = [ vim.HostSystem() ]

         class HostContainerFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec): # vim.dvs.DistributedVirtualSwitchManager.HostContainerFilter
            hostContainer = vim.dvs.DistributedVirtualSwitchManager.HostContainer()

         class HostDvsMembershipFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec): # vim.dvs.DistributedVirtualSwitchManager.HostDvsMembershipFilter
            distributedVirtualSwitch = vim.DistributedVirtualSwitch()

         class DvsProductSpec(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec
            newSwitchProductSpec = vim.dvs.ProductSpec()
            distributedVirtualSwitch = vim.DistributedVirtualSwitch()

         class ImportResult(vmodl.DynamicData): # vim.dvs.DistributedVirtualSwitchManager.ImportResult
            distributedVirtualSwitch = [ vim.DistributedVirtualSwitch() ]
            distributedVirtualPortgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
            importFault = [ vim.fault.ImportOperationBulkFault.FaultOnImport() ]

      class VmwareDistributedVirtualSwitch(vim.DistributedVirtualSwitch): # vim.dvs.VmwareDistributedVirtualSwitch

         def updateLacpGroupConfig(lacpGroupSpec=[ vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec() ]): # vim.dvs.VmwareDistributedVirtualSwitch.updateLacpGroupConfig
            # throws vim.fault.DvsFault
            return vim.Task()

         class FeatureCapability(vim.DistributedVirtualSwitch.FeatureCapability): # vim.dvs.VmwareDistributedVirtualSwitch.FeatureCapability
            vspanSupported = False
            lldpSupported = False
            ipfixSupported = False
            ipfixCapability = vim.dvs.VmwareDistributedVirtualSwitch.IpfixFeatureCapability()
            multicastSnoopingSupported = False
            vspanCapability = vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability()
            lacpCapability = vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability()
            nsxSupported = False

         class IpfixFeatureCapability(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.IpfixFeatureCapability
            ipfixSupported = False
            ipv6ForIpfixSupported = False
            observationDomainIdSupported = False

         class LacpFeatureCapability(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability
            lacpSupported = False
            multiLacpGroupSupported = False

         class VmwareHealthCheckFeatureCapability(vim.DistributedVirtualSwitch.HealthCheckFeatureCapability): # vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckFeatureCapability
            vlanMtuSupported = False
            teamingSupported = False

         class VspanFeatureCapability(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability
            mixedDestSupported = False
            dvportSupported = False
            remoteSourceSupported = False
            remoteDestSupported = False
            encapRemoteSourceSupported = False
            erspanProtocolSupported = False
            mirrorNetstackSupported = False

         class VspanPorts(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts
            portKey = [ "" ]
            uplinkPortName = [ "" ]
            wildcardPortConnecteeType = [ "" ]
            vlans = [ 0 ]
            ipAddress = [ "" ]

         class VspanSession(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.VspanSession
            key = ""
            name = ""
            description = ""
            enabled = False
            sourcePortTransmitted = vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts()
            sourcePortReceived = vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts()
            destinationPort = vim.dvs.VmwareDistributedVirtualSwitch.VspanPorts()
            encapsulationVlanId = 0
            stripOriginalVlan = False
            mirroredPacketLength = 0
            normalTrafficAllowed = False
            sessionType = ""
            samplingRate = 0
            encapType = ""
            erspanId = 0
            erspanCOS = 0
            erspanGraNanosec = False
            netstack = ""

         class IpfixConfig(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig
            collectorIpAddress = ""
            collectorPort = 0
            observationDomainId = 0
            activeFlowTimeout = 0
            idleFlowTimeout = 0
            samplingRate = 0
            internalFlowsOnly = False

         class ConfigInfo(vim.DistributedVirtualSwitch.ConfigInfo): # vim.dvs.VmwareDistributedVirtualSwitch.ConfigInfo
            vspanSession = [ vim.dvs.VmwareDistributedVirtualSwitch.VspanSession() ]
            pvlanConfig = [ vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry() ]
            maxMtu = 0
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()
            ipfixConfig = vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig()
            lacpGroupConfig = [ vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig() ]
            lacpApiVersion = ""
            multicastFilteringMode = ""

         class ConfigSpec(vim.DistributedVirtualSwitch.ConfigSpec): # vim.dvs.VmwareDistributedVirtualSwitch.ConfigSpec
            pvlanConfigSpec = [ vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec() ]
            vspanConfigSpec = [ vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec() ]
            maxMtu = 0
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()
            ipfixConfig = vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig()
            lacpApiVersion = ""
            multicastFilteringMode = ""

         class UplinkPortOrderPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy
            activeUplinkPort = [ "" ]
            standbyUplinkPort = [ "" ]

         class FailureCriteria(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria
            checkSpeed = vim.StringPolicy()
            speed = vim.IntPolicy()
            checkDuplex = vim.BoolPolicy()
            fullDuplex = vim.BoolPolicy()
            checkErrorPercent = vim.BoolPolicy()
            percentage = vim.IntPolicy()
            checkBeacon = vim.BoolPolicy()

         class UplinkPortTeamingPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy
            policy = vim.StringPolicy()
            reversePolicy = vim.BoolPolicy()
            notifySwitches = vim.BoolPolicy()
            rollingOrder = vim.BoolPolicy()
            failureCriteria = vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria()
            uplinkPortOrder = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy()

         class VlanSpec(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec
            pass

         class PvlanSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec): # vim.dvs.VmwareDistributedVirtualSwitch.PvlanSpec
            pvlanId = 0

         class VlanIdSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec): # vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec
            vlanId = 0

         class TrunkVlanSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec): # vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec
            vlanId = [ vim.NumericRange() ]

         class SecurityPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy
            allowPromiscuous = vim.BoolPolicy()
            macChanges = vim.BoolPolicy()
            forgedTransmits = vim.BoolPolicy()

         class MacLimitPolicyType(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.MacLimitPolicyType
            allow = 0
            drop = 1

         class MacLearningPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.MacLearningPolicy
            enabled = False
            allowUnicastFlooding = False
            limit = 0
            limitPolicy = ""

         class MacManagementPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.MacManagementPolicy
            allowPromiscuous = False
            macChanges = False
            forgedTransmits = False
            macLearningPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacLearningPolicy()

         class VmwarePortConfigPolicy(vim.dvs.DistributedVirtualPort.Setting): # vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy
            vlan = vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec()
            qosTag = vim.IntPolicy()
            uplinkTeamingPolicy = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy()
            securityPolicy = vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy()
            ipfixEnabled = vim.BoolPolicy()
            txUplink = vim.BoolPolicy()
            lacpPolicy = vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy()
            macManagementPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacManagementPolicy()
            VNI = vim.IntPolicy()

         class VMwarePortgroupPolicy(vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy): # vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy
            vlanOverrideAllowed = False
            uplinkTeamingOverrideAllowed = False
            securityPolicyOverrideAllowed = False
            ipfixOverrideAllowed = False
            macManagementOverrideAllowed = False

         class PvlanPortType(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.PvlanPortType
            promiscuous = 0
            isolated = 1
            community = 2

         class PvlanConfigSpec(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec
            pvlanEntry = vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry()
            operation = ""

         class PvlanMapEntry(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry
            primaryVlanId = 0
            secondaryVlanId = 0
            pvlanType = ""

         class VspanConfigSpec(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec
            vspanSession = vim.dvs.VmwareDistributedVirtualSwitch.VspanSession()
            operation = ""

         class VspanSessionEncapType(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionEncapType
            gre = 0
            erspan2 = 1
            erspan3 = 2

         class VspanSessionType(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.VspanSessionType
            mixedDestMirror = 0
            dvPortMirror = 1
            remoteMirrorSource = 2
            remoteMirrorDest = 3
            encapsulatedRemoteMirrorSource = 4

         class VmwareHealthCheckConfig(vim.DistributedVirtualSwitch.HealthCheckConfig): # vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig
            pass

         class VlanMtuHealthCheckConfig(vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig): # vim.dvs.VmwareDistributedVirtualSwitch.VlanMtuHealthCheckConfig
            pass

         class TeamingHealthCheckConfig(vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig): # vim.dvs.VmwareDistributedVirtualSwitch.TeamingHealthCheckConfig
            pass

         class VlanHealthCheckResult(vim.dvs.HostMember.UplinkHealthCheckResult): # vim.dvs.VmwareDistributedVirtualSwitch.VlanHealthCheckResult
            trunkedVlan = [ vim.NumericRange() ]
            untrunkedVlan = [ vim.NumericRange() ]

         class MtuHealthCheckResult(vim.dvs.HostMember.UplinkHealthCheckResult): # vim.dvs.VmwareDistributedVirtualSwitch.MtuHealthCheckResult
            mtuMismatch = False
            vlanSupportSwitchMtu = [ vim.NumericRange() ]
            vlanNotSupportSwitchMtu = [ vim.NumericRange() ]

         class TeamingMatchStatus(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.TeamingMatchStatus
            iphashMatch = 0
            nonIphashMatch = 1
            iphashMismatch = 2
            nonIphashMismatch = 3

         class TeamingHealthCheckResult(vim.dvs.HostMember.HealthCheckResult): # vim.dvs.VmwareDistributedVirtualSwitch.TeamingHealthCheckResult
            teamingStatus = ""

         class UplinkLacpPolicy(vim.InheritablePolicy): # vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy
            enable = vim.BoolPolicy()
            mode = vim.StringPolicy()

         class LacpGroupConfig(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig
            key = ""
            name = ""
            mode = ""
            uplinkNum = 0
            loadbalanceAlgorithm = ""
            vlan = vim.dvs.VmwareDistributedVirtualSwitch.LagVlanConfig()
            ipfix = vim.dvs.VmwareDistributedVirtualSwitch.LagIpfixConfig()
            uplinkName = [ "" ]
            uplinkPortKey = [ "" ]

         class LagVlanConfig(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.LagVlanConfig
            vlanId = [ vim.NumericRange() ]

         class LagIpfixConfig(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.LagIpfixConfig
            ipfixEnabled = False

         class UplinkLacpMode(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpMode
            active = 0
            passive = 1

         class LacpGroupSpec(vmodl.DynamicData): # vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec
            lacpGroupConfig = vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig()
            operation = ""

         class LacpLoadBalanceAlgorithm(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.LacpLoadBalanceAlgorithm
            srcMac = 0
            destMac = 1
            srcDestMac = 2
            destIpVlan = 3
            srcIpVlan = 4
            srcDestIpVlan = 5
            destTcpUdpPort = 6
            srcTcpUdpPort = 7
            srcDestTcpUdpPort = 8
            destIpTcpUdpPort = 9
            srcIpTcpUdpPort = 10
            srcDestIpTcpUdpPort = 11
            destIpTcpUdpPortVlan = 12
            srcIpTcpUdpPortVlan = 13
            srcDestIpTcpUdpPortVlan = 14
            destIp = 15
            srcIp = 16
            srcDestIp = 17
            vlan = 18
            srcPortId = 19

         class LacpApiVersion(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.LacpApiVersion
            singleLag = 0
            multipleLag = 1

         class MulticastFilteringMode(Enum): # vim.dvs.VmwareDistributedVirtualSwitch.MulticastFilteringMode
            legacyFiltering = 0
            snooping = 1

   class encryption(object): # (unknown name)

      class CryptoKeyId(vmodl.DynamicData): # vim.encryption.CryptoKeyId
         keyId = ""
         providerId = vim.encryption.KeyProviderId()

      class CryptoKeyPlain(vmodl.DynamicData): # vim.encryption.CryptoKeyPlain
         keyId = vim.encryption.CryptoKeyId()
         algorithm = ""
         keyData = ""

      class CryptoKeyResult(vmodl.DynamicData): # vim.encryption.CryptoKeyResult
         keyId = vim.encryption.CryptoKeyId()
         success = False
         reason = ""

      class CryptoManager(vmodl.ManagedObject): # vim.encryption.CryptoManager
         enabled = False

         def addKey(key=vim.encryption.CryptoKeyPlain()): # vim.encryption.CryptoManager.addKey
            # throws vim.fault.AlreadyExists, vim.fault.InvalidState
            return None

         def addKeys(keys=[ vim.encryption.CryptoKeyPlain() ] or None): # vim.encryption.CryptoManager.addKeys
            # throws vim.fault.InvalidState
            return [ vim.encryption.CryptoKeyResult() ]

         def removeKey(key=vim.encryption.CryptoKeyId(), force=False): # vim.encryption.CryptoManager.removeKey
            # throws vim.fault.ResourceInUse
            return None

         def removeKeys(keys=[ vim.encryption.CryptoKeyId() ] or None, force=False): # vim.encryption.CryptoManager.removeKeys
            return [ vim.encryption.CryptoKeyResult() ]

         def listKeys(limit=0 or None): # vim.encryption.CryptoManager.listKeys
            return [ vim.encryption.CryptoKeyId() ]

      class CryptoManagerHost(vim.encryption.CryptoManager): # vim.encryption.CryptoManagerHost

         def prepare(): # vim.encryption.CryptoManagerHost.prepare
            # throws vim.fault.InvalidState
            return None

         def enable(initialKey=vim.encryption.CryptoKeyPlain()): # vim.encryption.CryptoManagerHost.enable
            # throws vim.fault.InvalidState, vim.fault.AlreadyExists
            return None

         def changeKey(newKey=vim.encryption.CryptoKeyPlain()): # vim.encryption.CryptoManagerHost.changeKey
            # throws vim.fault.InvalidState
            return vim.Task()

         def disable(): # vim.encryption.CryptoManagerHost.disable
            # throws vim.fault.InvalidState
            return None

      class CryptoManagerHostKMS(vim.encryption.CryptoManagerHost): # vim.encryption.CryptoManagerHostKMS
         pass

      class CryptoSpec(vmodl.DynamicData): # vim.encryption.CryptoSpec
         pass

      class CryptoSpecDecrypt(vim.encryption.CryptoSpec): # vim.encryption.CryptoSpecDecrypt
         pass

      class CryptoSpecDeepRecrypt(vim.encryption.CryptoSpec): # vim.encryption.CryptoSpecDeepRecrypt
         newKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecEncrypt(vim.encryption.CryptoSpec): # vim.encryption.CryptoSpecEncrypt
         cryptoKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecNoOp(vim.encryption.CryptoSpec): # vim.encryption.CryptoSpecNoOp
         pass

      class CryptoSpecRegister(vim.encryption.CryptoSpecNoOp): # vim.encryption.CryptoSpecRegister
         cryptoKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecShallowRecrypt(vim.encryption.CryptoSpec): # vim.encryption.CryptoSpecShallowRecrypt
         newKeyId = vim.encryption.CryptoKeyId()

      class KeyProviderId(vmodl.DynamicData): # vim.encryption.KeyProviderId
         id = ""

      class KmipClusterInfo(vmodl.DynamicData): # vim.encryption.KmipClusterInfo
         clusterId = vim.encryption.KeyProviderId()
         servers = [ vim.encryption.KmipServerInfo() ]
         useAsDefault = False
         managementType = ""
         useAsEntityDefault = [ vim.ManagedEntity() ]

         class KmsManagementType(Enum): # vim.encryption.KmipClusterInfo.KmsManagementType
            unknown = 0
            vCenter = 1
            trustAuthority = 2

      class KmipServerInfo(vmodl.DynamicData): # vim.encryption.KmipServerInfo
         name = ""
         address = ""
         port = 0
         proxyAddress = ""
         proxyPort = 0
         reconnect = 0
         protocol = ""
         nbio = 0
         timeout = 0
         userName = ""

      class KmipServerSpec(vmodl.DynamicData): # vim.encryption.KmipServerSpec
         clusterId = vim.encryption.KeyProviderId()
         info = vim.encryption.KmipServerInfo()
         password = ""

      class CryptoManagerKmip(vim.encryption.CryptoManager): # vim.encryption.CryptoManagerKmip
         kmipServers = [ vim.encryption.KmipClusterInfo() ]

         def registerKmipServer(server=vim.encryption.KmipServerSpec()): # vim.encryption.CryptoManagerKmip.registerKmipServer
            return None

         def markDefault(clusterId=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.markDefault
            return None

         def updateKmipServer(server=vim.encryption.KmipServerSpec()): # vim.encryption.CryptoManagerKmip.updateKmipServer
            return None

         def removeKmipServer(clusterId=vim.encryption.KeyProviderId(), serverName=""): # vim.encryption.CryptoManagerKmip.removeKmipServer
            return None

         def listKmipServers(limit=0 or None): # vim.encryption.CryptoManagerKmip.listKmipServers
            return [ vim.encryption.KmipClusterInfo() ]

         def retrieveKmipServersStatus(clusters=[ vim.encryption.KmipClusterInfo() ] or None): # vim.encryption.CryptoManagerKmip.retrieveKmipServersStatus
            return vim.Task()

         def generateKey(keyProvider=vim.encryption.KeyProviderId() or None): # vim.encryption.CryptoManagerKmip.generateKey
            return vim.encryption.CryptoKeyResult()

         def retrieveKmipServerCert(keyProvider=vim.encryption.KeyProviderId(), server=vim.encryption.KmipServerInfo()): # vim.encryption.CryptoManagerKmip.retrieveKmipServerCert
            return vim.encryption.CryptoManagerKmip.ServerCertInfo()

         def uploadKmipServerCert(cluster=vim.encryption.KeyProviderId(), certificate=""): # vim.encryption.CryptoManagerKmip.uploadKmipServerCert
            return None

         def generateSelfSignedClientCert(cluster=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.generateSelfSignedClientCert
            return ""

         def generateClientCsr(cluster=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.generateClientCsr
            return ""

         def retrieveSelfSignedClientCert(cluster=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.retrieveSelfSignedClientCert
            return ""

         def retrieveClientCsr(cluster=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.retrieveClientCsr
            return ""

         def retrieveClientCert(cluster=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.retrieveClientCert
            return ""

         def updateSelfSignedClientCert(cluster=vim.encryption.KeyProviderId(), certificate=""): # vim.encryption.CryptoManagerKmip.updateSelfSignedClientCert
            return None

         def updateKmsSignedCsrClientCert(cluster=vim.encryption.KeyProviderId(), certificate=""): # vim.encryption.CryptoManagerKmip.updateKmsSignedCsrClientCert
            return None

         def uploadClientCert(cluster=vim.encryption.KeyProviderId(), certificate="", privateKey=""): # vim.encryption.CryptoManagerKmip.uploadClientCert
            return None

         def IsKmsClusterActive(cluster=vim.encryption.KeyProviderId() or None): # vim.encryption.CryptoManagerKmip.IsKmsClusterActive
            # throws vmodl.fault.InvalidArgument
            return False

         def setDefaultKmsCluster(entity=vim.ManagedEntity() or None, clusterId=vim.encryption.KeyProviderId() or None): # vim.encryption.CryptoManagerKmip.setDefaultKmsCluster
            return None

         def getDefaultKmsCluster(entity=vim.ManagedEntity() or None, defaultsToParent=False or None): # vim.encryption.CryptoManagerKmip.getDefaultKmsCluster
            return vim.encryption.KeyProviderId()

         def queryCryptoKeyStatus(keyIds=[ vim.encryption.CryptoKeyId() ] or None, checkKeyBitMap=0): # vim.encryption.CryptoManagerKmip.queryCryptoKeyStatus
            return [ vim.encryption.CryptoManagerKmip.CryptoKeyStatus() ]

         def registerKmsCluster(clusterId=vim.encryption.KeyProviderId(), managementType="" or None): # vim.encryption.CryptoManagerKmip.registerKmsCluster
            return None

         def unregisterKmsCluster(clusterId=vim.encryption.KeyProviderId()): # vim.encryption.CryptoManagerKmip.unregisterKmsCluster
            return None

         def listKmsClusters(includeKmsServers=False or None, managementTypeFilter=0 or None, statusFilter=0 or None): # vim.encryption.CryptoManagerKmip.listKmsClusters
            return [ vim.encryption.KmipClusterInfo() ]

         class CertificateInfo(vmodl.DynamicData): # vim.encryption.CryptoManagerKmip.CertificateInfo
            subject = ""
            issuer = ""
            serialNumber = ""
            notBefore = vmodl.DateTime()
            notAfter = vmodl.DateTime()
            fingerprint = ""
            checkTime = vmodl.DateTime()
            secondsSinceValid = 0
            secondsBeforeExpire = 0

         class ServerStatus(vmodl.DynamicData): # vim.encryption.CryptoManagerKmip.ServerStatus
            name = ""
            status = vim.ManagedEntity.Status()
            connectionStatus = ""
            certInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()
            clientTrustServer = False
            serverTrustClient = False

         class ClusterStatus(vmodl.DynamicData): # vim.encryption.CryptoManagerKmip.ClusterStatus
            clusterId = vim.encryption.KeyProviderId()
            overallStatus = vim.ManagedEntity.Status()
            managementType = ""
            servers = [ vim.encryption.CryptoManagerKmip.ServerStatus() ]
            clientCertInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()

         class ServerCertInfo(vmodl.DynamicData): # vim.encryption.CryptoManagerKmip.ServerCertInfo
            certificate = ""
            certInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()
            clientTrustServer = False

         class CryptoKeyStatus(vmodl.DynamicData): # vim.encryption.CryptoManagerKmip.CryptoKeyStatus
            keyId = vim.encryption.CryptoKeyId()
            keyAvailable = False
            reason = ""
            encryptedVMs = [ vim.VirtualMachine() ]
            affectedHosts = [ vim.HostSystem() ]
            referencedByTags = [ "" ]

            class KeyUnavailableReason(Enum): # vim.encryption.CryptoManagerKmip.CryptoKeyStatus.KeyUnavailableReason
               KeyStateMissingInCache = 0
               KeyStateClusterInvalid = 1
               KeyStateClusterUnreachable = 2
               KeyStateMissingInKMS = 3
               KeyStateNotActiveOrEnabled = 4
               KeyStateManagedByTrustAuthority = 5

      class KmipServerStatus(vmodl.DynamicData): # vim.encryption.KmipServerStatus
         clusterId = vim.encryption.KeyProviderId()
         name = ""
         status = vim.ManagedEntity.Status()
         description = ""

   class event(object): # (unknown name)

      class ChangesInfoEventArgument(vmodl.DynamicData): # vim.event.ChangesInfoEventArgument
         modified = ""
         added = ""
         deleted = ""

      class DvsOutOfSyncHostArgument(vmodl.DynamicData): # vim.event.DvsOutOfSyncHostArgument
         outOfSyncHost = vim.event.HostEventArgument()
         configParamters = [ "" ]

      class Event(vmodl.DynamicData): # vim.event.Event
         key = 0
         chainId = 0
         createdTime = vmodl.DateTime()
         userName = ""
         datacenter = vim.event.DatacenterEventArgument()
         computeResource = vim.event.ComputeResourceEventArgument()
         host = vim.event.HostEventArgument()
         vm = vim.event.VmEventArgument()
         ds = vim.event.DatastoreEventArgument()
         net = vim.event.NetworkEventArgument()
         dvs = vim.event.DvsEventArgument()
         fullFormattedMessage = ""
         changeTag = ""

         class EventSeverity(Enum): # vim.event.Event.EventSeverity
            error = 0
            warning = 1
            info = 2
            user = 3

      class EventArgument(vmodl.DynamicData): # vim.event.EventArgument
         pass

      class EventDescription(vmodl.DynamicData): # vim.event.EventDescription
         category = [ vim.ElementDescription() ]
         eventInfo = [ vim.event.EventDescription.EventDetail() ]
         enumeratedTypes = [ vim.EnumDescription() ]

         class EventCategory(Enum): # vim.event.EventDescription.EventCategory
            info = 0
            warning = 1
            error = 2
            user = 3

         class EventArgDesc(vmodl.DynamicData): # vim.event.EventDescription.EventArgDesc
            name = ""
            type = ""
            description = vim.ElementDescription()

         class EventDetail(vmodl.DynamicData): # vim.event.EventDescription.EventDetail
            key = vmodl.TypeName()
            description = ""
            category = ""
            formatOnDatacenter = ""
            formatOnComputeResource = ""
            formatOnHost = ""
            formatOnVm = ""
            fullFormat = ""
            longDescription = ""

      class EventEx(vim.event.Event): # vim.event.EventEx
         eventTypeId = ""
         severity = ""
         message = ""
         arguments = [ vmodl.KeyAnyValue() ]
         objectId = ""
         objectType = vmodl.TypeName()
         objectName = ""
         fault = vmodl.MethodFault()

      class EventFilterSpec(vmodl.DynamicData): # vim.event.EventFilterSpec
         entity = vim.event.EventFilterSpec.ByEntity()
         time = vim.event.EventFilterSpec.ByTime()
         userName = vim.event.EventFilterSpec.ByUsername()
         eventChainId = 0
         alarm = vim.alarm.Alarm()
         scheduledTask = vim.scheduler.ScheduledTask()
         disableFullMessage = False
         category = [ "" ]
         type = [ vmodl.TypeName() ]
         tag = [ "" ]
         eventTypeId = [ "" ]
         maxCount = 0

         class RecursionOption(Enum): # vim.event.EventFilterSpec.RecursionOption
            self = 0
            children = 1
            all = 2

         class ByEntity(vmodl.DynamicData): # vim.event.EventFilterSpec.ByEntity
            entity = vim.ManagedEntity()
            recursion = vim.event.EventFilterSpec.RecursionOption()

         class ByTime(vmodl.DynamicData): # vim.event.EventFilterSpec.ByTime
            beginTime = vmodl.DateTime()
            endTime = vmodl.DateTime()

         class ByUsername(vmodl.DynamicData): # vim.event.EventFilterSpec.ByUsername
            systemUser = False
            userList = [ "" ]

      class EventHistoryCollector(vim.HistoryCollector): # vim.event.EventHistoryCollector
         latestPage = [ vim.event.Event() ]

         def readNext(maxCount=0): # vim.event.EventHistoryCollector.readNext
            return [ vim.event.Event() ]

         def readPrev(maxCount=0): # vim.event.EventHistoryCollector.readPrev
            return [ vim.event.Event() ]

      class EventManager(vmodl.ManagedObject): # vim.event.EventManager
         description = vim.event.EventDescription()
         latestEvent = vim.event.Event()
         maxCollector = 0

         def retrieveArgumentDescription(eventTypeId=""): # vim.event.EventManager.retrieveArgumentDescription
            return [ vim.event.EventDescription.EventArgDesc() ]

         def createCollector(filter=vim.event.EventFilterSpec()): # vim.event.EventManager.createCollector
            # throws vim.fault.InvalidState
            return vim.event.EventHistoryCollector()

         def logUserEvent(entity=vim.ManagedEntity(), msg=""): # vim.event.EventManager.logUserEvent
            return None

         def QueryEvent(filter=vim.event.EventFilterSpec()): # vim.event.EventManager.QueryEvent
            return [ vim.event.Event() ]

         def postEvent(eventToPost=vim.event.Event(), taskInfo=vim.TaskInfo() or None): # vim.event.EventManager.postEvent
            # throws vim.fault.InvalidEvent
            return None

      class GeneralEvent(vim.event.Event): # vim.event.GeneralEvent
         message = ""

      class GeneralHostErrorEvent(vim.event.GeneralEvent): # vim.event.GeneralHostErrorEvent
         pass

      class GeneralHostInfoEvent(vim.event.GeneralEvent): # vim.event.GeneralHostInfoEvent
         pass

      class GeneralHostWarningEvent(vim.event.GeneralEvent): # vim.event.GeneralHostWarningEvent
         pass

      class GeneralUserEvent(vim.event.GeneralEvent): # vim.event.GeneralUserEvent
         entity = vim.event.ManagedEntityEventArgument()

      class GeneralVmErrorEvent(vim.event.GeneralEvent): # vim.event.GeneralVmErrorEvent
         pass

      class GeneralVmInfoEvent(vim.event.GeneralEvent): # vim.event.GeneralVmInfoEvent
         pass

      class GeneralVmWarningEvent(vim.event.GeneralEvent): # vim.event.GeneralVmWarningEvent
         pass

      class HealthStatusChangedEvent(vim.event.Event): # vim.event.HealthStatusChangedEvent
         componentId = ""
         oldStatus = ""
         newStatus = ""
         componentName = ""
         serviceId = ""

      class HostEvent(vim.event.Event): # vim.event.HostEvent
         pass

      class HostGetShortNameFailedEvent(vim.event.HostEvent): # vim.event.HostGetShortNameFailedEvent
         pass

      class HostInAuditModeEvent(vim.event.HostEvent): # vim.event.HostInAuditModeEvent
         pass

      class HostInventoryUnreadableEvent(vim.event.Event): # vim.event.HostInventoryUnreadableEvent
         pass

      class HostIpChangedEvent(vim.event.HostEvent): # vim.event.HostIpChangedEvent
         oldIP = ""
         newIP = ""

      class HostIpInconsistentEvent(vim.event.HostEvent): # vim.event.HostIpInconsistentEvent
         ipAddress = ""
         ipAddress2 = ""

      class HostIpToShortNameFailedEvent(vim.event.HostEvent): # vim.event.HostIpToShortNameFailedEvent
         pass

      class HostNonCompliantEvent(vim.event.HostEvent): # vim.event.HostNonCompliantEvent
         pass

      class HostProfileAppliedEvent(vim.event.HostEvent): # vim.event.HostProfileAppliedEvent
         profile = vim.event.ProfileEventArgument()

      class HostReconnectionFailedEvent(vim.event.HostEvent): # vim.event.HostReconnectionFailedEvent
         pass

      class HostRemovedEvent(vim.event.HostEvent): # vim.event.HostRemovedEvent
         pass

      class HostShortNameToIpFailedEvent(vim.event.HostEvent): # vim.event.HostShortNameToIpFailedEvent
         shortName = ""

      class HostShutdownEvent(vim.event.HostEvent): # vim.event.HostShutdownEvent
         reason = ""

      class HostSpecificationChangedEvent(vim.event.HostEvent): # vim.event.HostSpecificationChangedEvent
         pass

      class HostSpecificationRequireEvent(vim.event.HostEvent): # vim.event.HostSpecificationRequireEvent
         pass

      class HostSpecificationUpdateEvent(vim.event.HostEvent): # vim.event.HostSpecificationUpdateEvent
         hostSpec = vim.profile.host.HostSpecification()

      class HostSubSpecificationDeleteEvent(vim.event.HostEvent): # vim.event.HostSubSpecificationDeleteEvent
         subSpecName = ""

      class HostSubSpecificationUpdateEvent(vim.event.HostEvent): # vim.event.HostSubSpecificationUpdateEvent
         hostSubSpec = vim.profile.host.HostSubSpecification()

      class HostSyncFailedEvent(vim.event.HostEvent): # vim.event.HostSyncFailedEvent
         reason = vmodl.MethodFault()

      class HostUpgradeFailedEvent(vim.event.HostEvent): # vim.event.HostUpgradeFailedEvent
         pass

      class HostUserWorldSwapNotEnabledEvent(vim.event.HostEvent): # vim.event.HostUserWorldSwapNotEnabledEvent
         pass

      class HostVnicConnectedToCustomizedDVPortEvent(vim.event.HostEvent): # vim.event.HostVnicConnectedToCustomizedDVPortEvent
         vnic = vim.event.VnicPortArgument()
         prevPortKey = ""

      class HostWwnChangedEvent(vim.event.HostEvent): # vim.event.HostWwnChangedEvent
         oldNodeWwns = [ 0 ]
         oldPortWwns = [ 0 ]
         newNodeWwns = [ 0 ]
         newPortWwns = [ 0 ]

      class HostWwnConflictEvent(vim.event.HostEvent): # vim.event.HostWwnConflictEvent
         conflictedVms = [ vim.event.VmEventArgument() ]
         conflictedHosts = [ vim.event.HostEventArgument() ]
         wwn = 0

      class LicenseEvent(vim.event.Event): # vim.event.LicenseEvent
         pass

      class LicenseExpiredEvent(vim.event.Event): # vim.event.LicenseExpiredEvent
         feature = vim.LicenseManager.FeatureInfo()

      class LicenseNonComplianceEvent(vim.event.LicenseEvent): # vim.event.LicenseNonComplianceEvent
         url = ""

      class LicenseRestrictedEvent(vim.event.LicenseEvent): # vim.event.LicenseRestrictedEvent
         pass

      class LicenseServerAvailableEvent(vim.event.LicenseEvent): # vim.event.LicenseServerAvailableEvent
         licenseServer = ""

      class LicenseServerUnavailableEvent(vim.event.LicenseEvent): # vim.event.LicenseServerUnavailableEvent
         licenseServer = ""

      class LocalDatastoreCreatedEvent(vim.event.HostEvent): # vim.event.LocalDatastoreCreatedEvent
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class LocalTSMEnabledEvent(vim.event.HostEvent): # vim.event.LocalTSMEnabledEvent
         pass

      class LockerMisconfiguredEvent(vim.event.Event): # vim.event.LockerMisconfiguredEvent
         datastore = vim.event.DatastoreEventArgument()

      class LockerReconfiguredEvent(vim.event.Event): # vim.event.LockerReconfiguredEvent
         oldDatastore = vim.event.DatastoreEventArgument()
         newDatastore = vim.event.DatastoreEventArgument()

      class NASDatastoreCreatedEvent(vim.event.HostEvent): # vim.event.NASDatastoreCreatedEvent
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class NetworkRollbackEvent(vim.event.Event): # vim.event.NetworkRollbackEvent
         methodName = ""
         transactionId = ""

      class NoDatastoresConfiguredEvent(vim.event.HostEvent): # vim.event.NoDatastoresConfiguredEvent
         pass

      class NoLicenseEvent(vim.event.LicenseEvent): # vim.event.NoLicenseEvent
         feature = vim.LicenseManager.FeatureInfo()

      class ProfileEvent(vim.event.Event): # vim.event.ProfileEvent
         profile = vim.event.ProfileEventArgument()

      class ProfileEventArgument(vim.event.EventArgument): # vim.event.ProfileEventArgument
         profile = vim.profile.Profile()
         name = ""

      class ProfileReferenceHostChangedEvent(vim.event.ProfileEvent): # vim.event.ProfileReferenceHostChangedEvent
         referenceHost = vim.HostSystem()
         referenceHostName = ""
         prevReferenceHostName = ""

      class ProfileRemovedEvent(vim.event.ProfileEvent): # vim.event.ProfileRemovedEvent
         pass

      class RemoteTSMEnabledEvent(vim.event.HostEvent): # vim.event.RemoteTSMEnabledEvent
         pass

      class ResourcePoolEvent(vim.event.Event): # vim.event.ResourcePoolEvent
         resourcePool = vim.event.ResourcePoolEventArgument()

      class ResourcePoolMovedEvent(vim.event.ResourcePoolEvent): # vim.event.ResourcePoolMovedEvent
         oldParent = vim.event.ResourcePoolEventArgument()
         newParent = vim.event.ResourcePoolEventArgument()

      class ResourcePoolReconfiguredEvent(vim.event.ResourcePoolEvent): # vim.event.ResourcePoolReconfiguredEvent
         configChanges = vim.event.ChangesInfoEventArgument()

      class ResourceViolatedEvent(vim.event.ResourcePoolEvent): # vim.event.ResourceViolatedEvent
         pass

      class RoleEventArgument(vim.event.EventArgument): # vim.event.RoleEventArgument
         roleId = 0
         name = ""

      class ScheduledTaskEvent(vim.event.Event): # vim.event.ScheduledTaskEvent
         scheduledTask = vim.event.ScheduledTaskEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class ScheduledTaskFailedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskFailedEvent
         reason = vmodl.MethodFault()

      class ScheduledTaskReconfiguredEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskReconfiguredEvent
         configChanges = vim.event.ChangesInfoEventArgument()

      class ScheduledTaskRemovedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskRemovedEvent
         pass

      class ScheduledTaskStartedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskStartedEvent
         pass

      class ServerLicenseExpiredEvent(vim.event.LicenseEvent): # vim.event.ServerLicenseExpiredEvent
         product = ""

      class SessionEvent(vim.event.Event): # vim.event.SessionEvent
         pass

      class SessionTerminatedEvent(vim.event.SessionEvent): # vim.event.SessionTerminatedEvent
         sessionId = ""
         terminatedUsername = ""

      class TaskEvent(vim.event.Event): # vim.event.TaskEvent
         info = vim.TaskInfo()

      class TaskTimeoutEvent(vim.event.TaskEvent): # vim.event.TaskTimeoutEvent
         pass

      class TemplateUpgradeEvent(vim.event.Event): # vim.event.TemplateUpgradeEvent
         legacyTemplate = ""

      class TemplateUpgradeFailedEvent(vim.event.TemplateUpgradeEvent): # vim.event.TemplateUpgradeFailedEvent
         reason = vmodl.MethodFault()

      class TemplateUpgradedEvent(vim.event.TemplateUpgradeEvent): # vim.event.TemplateUpgradedEvent
         pass

      class TimedOutHostOperationEvent(vim.event.HostEvent): # vim.event.TimedOutHostOperationEvent
         pass

      class UnlicensedVirtualMachinesEvent(vim.event.LicenseEvent): # vim.event.UnlicensedVirtualMachinesEvent
         unlicensed = 0
         available = 0

      class UnlicensedVirtualMachinesFoundEvent(vim.event.LicenseEvent): # vim.event.UnlicensedVirtualMachinesFoundEvent
         available = 0

      class UpdatedAgentBeingRestartedEvent(vim.event.HostEvent): # vim.event.UpdatedAgentBeingRestartedEvent
         pass

      class UpgradeEvent(vim.event.Event): # vim.event.UpgradeEvent
         message = ""

      class UserAssignedToGroup(vim.event.HostEvent): # vim.event.UserAssignedToGroup
         userLogin = ""
         group = ""

      class UserLoginSessionEvent(vim.event.SessionEvent): # vim.event.UserLoginSessionEvent
         ipAddress = ""
         userAgent = ""
         locale = ""
         sessionId = ""

      class UserLogoutSessionEvent(vim.event.SessionEvent): # vim.event.UserLogoutSessionEvent
         ipAddress = ""
         userAgent = ""
         callCount = 0
         sessionId = ""
         loginTime = vmodl.DateTime()

      class UserPasswordChanged(vim.event.HostEvent): # vim.event.UserPasswordChanged
         userLogin = ""

      class UserUnassignedFromGroup(vim.event.HostEvent): # vim.event.UserUnassignedFromGroup
         userLogin = ""
         group = ""

      class UserUpgradeEvent(vim.event.UpgradeEvent): # vim.event.UserUpgradeEvent
         pass

      class VMFSDatastoreCreatedEvent(vim.event.HostEvent): # vim.event.VMFSDatastoreCreatedEvent
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class VMFSDatastoreExpandedEvent(vim.event.HostEvent): # vim.event.VMFSDatastoreExpandedEvent
         datastore = vim.event.DatastoreEventArgument()

      class VMFSDatastoreExtendedEvent(vim.event.HostEvent): # vim.event.VMFSDatastoreExtendedEvent
         datastore = vim.event.DatastoreEventArgument()

      class VMotionLicenseExpiredEvent(vim.event.LicenseEvent): # vim.event.VMotionLicenseExpiredEvent
         pass

      class VcAgentUninstallFailedEvent(vim.event.HostEvent): # vim.event.VcAgentUninstallFailedEvent
         reason = ""

      class VcAgentUninstalledEvent(vim.event.HostEvent): # vim.event.VcAgentUninstalledEvent
         pass

      class VcAgentUpgradeFailedEvent(vim.event.HostEvent): # vim.event.VcAgentUpgradeFailedEvent
         reason = ""

      class VcAgentUpgradedEvent(vim.event.HostEvent): # vim.event.VcAgentUpgradedEvent
         pass

      class VimAccountPasswordChangedEvent(vim.event.HostEvent): # vim.event.VimAccountPasswordChangedEvent
         pass

      class VmEvent(vim.event.Event): # vim.event.VmEvent
         template = False

      class VmFailedMigrateEvent(vim.event.VmEvent): # vim.event.VmFailedMigrateEvent
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmFailedRelayoutEvent(vim.event.VmEvent): # vim.event.VmFailedRelayoutEvent
         reason = vmodl.MethodFault()

      class VmFailedRelayoutOnVmfs2DatastoreEvent(vim.event.VmEvent): # vim.event.VmFailedRelayoutOnVmfs2DatastoreEvent
         pass

      class VmFailedStartingSecondaryEvent(vim.event.VmEvent): # vim.event.VmFailedStartingSecondaryEvent
         reason = ""

         class FailureReason(Enum): # vim.event.VmFailedStartingSecondaryEvent.FailureReason
            incompatibleHost = 0
            loginFailed = 1
            registerVmFailed = 2
            migrateFailed = 3

      class VmFailedToPowerOffEvent(vim.event.VmEvent): # vim.event.VmFailedToPowerOffEvent
         reason = vmodl.MethodFault()

      class VmFailedToPowerOnEvent(vim.event.VmEvent): # vim.event.VmFailedToPowerOnEvent
         reason = vmodl.MethodFault()

      class VmFailedToRebootGuestEvent(vim.event.VmEvent): # vim.event.VmFailedToRebootGuestEvent
         reason = vmodl.MethodFault()

      class VmFailedToResetEvent(vim.event.VmEvent): # vim.event.VmFailedToResetEvent
         reason = vmodl.MethodFault()

      class VmFailedToShutdownGuestEvent(vim.event.VmEvent): # vim.event.VmFailedToShutdownGuestEvent
         reason = vmodl.MethodFault()

      class VmFailedToStandbyGuestEvent(vim.event.VmEvent): # vim.event.VmFailedToStandbyGuestEvent
         reason = vmodl.MethodFault()

      class VmFailedToSuspendEvent(vim.event.VmEvent): # vim.event.VmFailedToSuspendEvent
         reason = vmodl.MethodFault()

      class VmFailedUpdatingSecondaryConfig(vim.event.VmEvent): # vim.event.VmFailedUpdatingSecondaryConfig
         pass

      class VmFailoverFailed(vim.event.VmEvent): # vim.event.VmFailoverFailed
         reason = vmodl.MethodFault()

      class VmFaultToleranceTurnedOffEvent(vim.event.VmEvent): # vim.event.VmFaultToleranceTurnedOffEvent
         pass

      class VmFaultToleranceVmTerminatedEvent(vim.event.VmEvent): # vim.event.VmFaultToleranceVmTerminatedEvent
         reason = ""

      class VmGuestOSCrashedEvent(vim.event.VmEvent): # vim.event.VmGuestOSCrashedEvent
         pass

      class VmGuestRebootEvent(vim.event.VmEvent): # vim.event.VmGuestRebootEvent
         pass

      class VmGuestShutdownEvent(vim.event.VmEvent): # vim.event.VmGuestShutdownEvent
         pass

      class VmGuestStandbyEvent(vim.event.VmEvent): # vim.event.VmGuestStandbyEvent
         pass

      class VmInstanceUuidAssignedEvent(vim.event.VmEvent): # vim.event.VmInstanceUuidAssignedEvent
         instanceUuid = ""

      class VmInstanceUuidChangedEvent(vim.event.VmEvent): # vim.event.VmInstanceUuidChangedEvent
         oldInstanceUuid = ""
         newInstanceUuid = ""

      class VmInstanceUuidConflictEvent(vim.event.VmEvent): # vim.event.VmInstanceUuidConflictEvent
         conflictedVm = vim.event.VmEventArgument()
         instanceUuid = ""

      class VmMacAssignedEvent(vim.event.VmEvent): # vim.event.VmMacAssignedEvent
         adapter = ""
         mac = ""

      class VmMacChangedEvent(vim.event.VmEvent): # vim.event.VmMacChangedEvent
         adapter = ""
         oldMac = ""
         newMac = ""

      class VmMacConflictEvent(vim.event.VmEvent): # vim.event.VmMacConflictEvent
         conflictedVm = vim.event.VmEventArgument()
         mac = ""

      class VmMaxFTRestartCountReached(vim.event.VmEvent): # vim.event.VmMaxFTRestartCountReached
         pass

      class VmMaxRestartCountReached(vim.event.VmEvent): # vim.event.VmMaxRestartCountReached
         pass

      class VmMessageErrorEvent(vim.event.VmEvent): # vim.event.VmMessageErrorEvent
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMessageEvent(vim.event.VmEvent): # vim.event.VmMessageEvent
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMessageWarningEvent(vim.event.VmEvent): # vim.event.VmMessageWarningEvent
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMigratedEvent(vim.event.VmEvent): # vim.event.VmMigratedEvent
         sourceHost = vim.event.HostEventArgument()
         sourceDatacenter = vim.event.DatacenterEventArgument()
         sourceDatastore = vim.event.DatastoreEventArgument()

      class VmNoCompatibleHostForSecondaryEvent(vim.event.VmEvent): # vim.event.VmNoCompatibleHostForSecondaryEvent
         pass

      class VmNoNetworkAccessEvent(vim.event.VmEvent): # vim.event.VmNoNetworkAccessEvent
         destHost = vim.event.HostEventArgument()

      class VmOrphanedEvent(vim.event.VmEvent): # vim.event.VmOrphanedEvent
         pass

      class VmPoweredOffEvent(vim.event.VmEvent): # vim.event.VmPoweredOffEvent
         pass

      class VmPoweredOnEvent(vim.event.VmEvent): # vim.event.VmPoweredOnEvent
         pass

      class VmPoweringOnWithCustomizedDVPortEvent(vim.event.VmEvent): # vim.event.VmPoweringOnWithCustomizedDVPortEvent
         vnic = [ vim.event.VnicPortArgument() ]

      class VmPrimaryFailoverEvent(vim.event.VmEvent): # vim.event.VmPrimaryFailoverEvent
         reason = ""

      class VmReconfiguredEvent(vim.event.VmEvent): # vim.event.VmReconfiguredEvent
         configSpec = vim.vm.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class VmRegisteredEvent(vim.event.VmEvent): # vim.event.VmRegisteredEvent
         pass

      class VmRelayoutSuccessfulEvent(vim.event.VmEvent): # vim.event.VmRelayoutSuccessfulEvent
         pass

      class VmRelayoutUpToDateEvent(vim.event.VmEvent): # vim.event.VmRelayoutUpToDateEvent
         pass

      class VmReloadFromPathEvent(vim.event.VmEvent): # vim.event.VmReloadFromPathEvent
         configPath = ""

      class VmReloadFromPathFailedEvent(vim.event.VmEvent): # vim.event.VmReloadFromPathFailedEvent
         configPath = ""

      class VmRelocateSpecEvent(vim.event.VmEvent): # vim.event.VmRelocateSpecEvent
         pass

      class VmRelocatedEvent(vim.event.VmRelocateSpecEvent): # vim.event.VmRelocatedEvent
         sourceHost = vim.event.HostEventArgument()
         sourceDatacenter = vim.event.DatacenterEventArgument()
         sourceDatastore = vim.event.DatastoreEventArgument()

      class VmRemoteConsoleConnectedEvent(vim.event.VmEvent): # vim.event.VmRemoteConsoleConnectedEvent
         pass

      class VmRemoteConsoleDisconnectedEvent(vim.event.VmEvent): # vim.event.VmRemoteConsoleDisconnectedEvent
         pass

      class VmRemovedEvent(vim.event.VmEvent): # vim.event.VmRemovedEvent
         pass

      class VmRenamedEvent(vim.event.VmEvent): # vim.event.VmRenamedEvent
         oldName = ""
         newName = ""

      class VmRequirementsExceedCurrentEVCModeEvent(vim.event.VmEvent): # vim.event.VmRequirementsExceedCurrentEVCModeEvent
         pass

      class VmResettingEvent(vim.event.VmEvent): # vim.event.VmResettingEvent
         pass

      class VmResourcePoolMovedEvent(vim.event.VmEvent): # vim.event.VmResourcePoolMovedEvent
         oldParent = vim.event.ResourcePoolEventArgument()
         newParent = vim.event.ResourcePoolEventArgument()

      class VmResourceReallocatedEvent(vim.event.VmEvent): # vim.event.VmResourceReallocatedEvent
         configChanges = vim.event.ChangesInfoEventArgument()

      class VmRestartedOnAlternateHostEvent(vim.event.VmPoweredOnEvent): # vim.event.VmRestartedOnAlternateHostEvent
         sourceHost = vim.event.HostEventArgument()

      class VmResumingEvent(vim.event.VmEvent): # vim.event.VmResumingEvent
         pass

      class VmSecondaryAddedEvent(vim.event.VmEvent): # vim.event.VmSecondaryAddedEvent
         pass

      class VmSecondaryDisabledBySystemEvent(vim.event.VmEvent): # vim.event.VmSecondaryDisabledBySystemEvent
         reason = vmodl.MethodFault()

      class VmSecondaryDisabledEvent(vim.event.VmEvent): # vim.event.VmSecondaryDisabledEvent
         pass

      class VmSecondaryEnabledEvent(vim.event.VmEvent): # vim.event.VmSecondaryEnabledEvent
         pass

      class VmSecondaryStartedEvent(vim.event.VmEvent): # vim.event.VmSecondaryStartedEvent
         pass

      class VmShutdownOnIsolationEvent(vim.event.VmPoweredOffEvent): # vim.event.VmShutdownOnIsolationEvent
         isolatedHost = vim.event.HostEventArgument()
         shutdownResult = ""

         class Operation(Enum): # vim.event.VmShutdownOnIsolationEvent.Operation
            shutdown = 0
            poweredOff = 1

      class VmStartRecordingEvent(vim.event.VmEvent): # vim.event.VmStartRecordingEvent
         pass

      class VmStartReplayingEvent(vim.event.VmEvent): # vim.event.VmStartReplayingEvent
         pass

      class VmStartingEvent(vim.event.VmEvent): # vim.event.VmStartingEvent
         pass

      class VmStartingSecondaryEvent(vim.event.VmEvent): # vim.event.VmStartingSecondaryEvent
         pass

      class VmStaticMacConflictEvent(vim.event.VmEvent): # vim.event.VmStaticMacConflictEvent
         conflictedVm = vim.event.VmEventArgument()
         mac = ""

      class VmStoppingEvent(vim.event.VmEvent): # vim.event.VmStoppingEvent
         pass

      class VmSuspendedEvent(vim.event.VmEvent): # vim.event.VmSuspendedEvent
         pass

      class VmSuspendingEvent(vim.event.VmEvent): # vim.event.VmSuspendingEvent
         pass

      class VmTimedoutStartingSecondaryEvent(vim.event.VmEvent): # vim.event.VmTimedoutStartingSecondaryEvent
         timeout = 0

      class VmUnsupportedStartingEvent(vim.event.VmStartingEvent): # vim.event.VmUnsupportedStartingEvent
         guestId = ""

      class VmUpgradeCompleteEvent(vim.event.VmEvent): # vim.event.VmUpgradeCompleteEvent
         version = ""

      class VmUpgradeFailedEvent(vim.event.VmEvent): # vim.event.VmUpgradeFailedEvent
         pass

      class VmUpgradingEvent(vim.event.VmEvent): # vim.event.VmUpgradingEvent
         version = ""

      class VmUuidAssignedEvent(vim.event.VmEvent): # vim.event.VmUuidAssignedEvent
         uuid = ""

      class VmUuidChangedEvent(vim.event.VmEvent): # vim.event.VmUuidChangedEvent
         oldUuid = ""
         newUuid = ""

      class VmUuidConflictEvent(vim.event.VmEvent): # vim.event.VmUuidConflictEvent
         conflictedVm = vim.event.VmEventArgument()
         uuid = ""

      class VmWwnAssignedEvent(vim.event.VmEvent): # vim.event.VmWwnAssignedEvent
         nodeWwns = [ 0 ]
         portWwns = [ 0 ]

      class VmWwnChangedEvent(vim.event.VmEvent): # vim.event.VmWwnChangedEvent
         oldNodeWwns = [ 0 ]
         oldPortWwns = [ 0 ]
         newNodeWwns = [ 0 ]
         newPortWwns = [ 0 ]

      class VmWwnConflictEvent(vim.event.VmEvent): # vim.event.VmWwnConflictEvent
         conflictedVms = [ vim.event.VmEventArgument() ]
         conflictedHosts = [ vim.event.HostEventArgument() ]
         wwn = 0

      class VnicPortArgument(vmodl.DynamicData): # vim.event.VnicPortArgument
         vnic = ""
         port = vim.dvs.PortConnection()

      class WarningUpgradeEvent(vim.event.UpgradeEvent): # vim.event.WarningUpgradeEvent
         pass

      class iScsiBootFailureEvent(vim.event.HostEvent): # vim.event.iScsiBootFailureEvent
         pass

      class AccountCreatedEvent(vim.event.HostEvent): # vim.event.AccountCreatedEvent
         spec = vim.host.LocalAccountManager.AccountSpecification()
         group = False

      class AccountRemovedEvent(vim.event.HostEvent): # vim.event.AccountRemovedEvent
         account = ""
         group = False

      class AccountUpdatedEvent(vim.event.HostEvent): # vim.event.AccountUpdatedEvent
         spec = vim.host.LocalAccountManager.AccountSpecification()
         group = False
         prevDescription = ""

      class AdminPasswordNotChangedEvent(vim.event.HostEvent): # vim.event.AdminPasswordNotChangedEvent
         pass

      class AlarmEvent(vim.event.Event): # vim.event.AlarmEvent
         alarm = vim.event.AlarmEventArgument()

      class AlarmReconfiguredEvent(vim.event.AlarmEvent): # vim.event.AlarmReconfiguredEvent
         entity = vim.event.ManagedEntityEventArgument()
         configChanges = vim.event.ChangesInfoEventArgument()

      class AlarmRemovedEvent(vim.event.AlarmEvent): # vim.event.AlarmRemovedEvent
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmScriptCompleteEvent(vim.event.AlarmEvent): # vim.event.AlarmScriptCompleteEvent
         entity = vim.event.ManagedEntityEventArgument()
         script = ""

      class AlarmScriptFailedEvent(vim.event.AlarmEvent): # vim.event.AlarmScriptFailedEvent
         entity = vim.event.ManagedEntityEventArgument()
         script = ""
         reason = vmodl.MethodFault()

      class AlarmSnmpCompletedEvent(vim.event.AlarmEvent): # vim.event.AlarmSnmpCompletedEvent
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmSnmpFailedEvent(vim.event.AlarmEvent): # vim.event.AlarmSnmpFailedEvent
         entity = vim.event.ManagedEntityEventArgument()
         reason = vmodl.MethodFault()

      class AlarmStatusChangedEvent(vim.event.AlarmEvent): # vim.event.AlarmStatusChangedEvent
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()
         from = ""
         to = ""

      class AllVirtualMachinesLicensedEvent(vim.event.LicenseEvent): # vim.event.AllVirtualMachinesLicensedEvent
         pass

      class AlreadyAuthenticatedSessionEvent(vim.event.SessionEvent): # vim.event.AlreadyAuthenticatedSessionEvent
         pass

      class AuthorizationEvent(vim.event.Event): # vim.event.AuthorizationEvent
         pass

      class BadUsernameSessionEvent(vim.event.SessionEvent): # vim.event.BadUsernameSessionEvent
         ipAddress = ""

      class CanceledHostOperationEvent(vim.event.HostEvent): # vim.event.CanceledHostOperationEvent
         pass

      class ClusterEvent(vim.event.Event): # vim.event.ClusterEvent
         pass

      class ClusterOvercommittedEvent(vim.event.ClusterEvent): # vim.event.ClusterOvercommittedEvent
         pass

      class ClusterReconfiguredEvent(vim.event.ClusterEvent): # vim.event.ClusterReconfiguredEvent
         configChanges = vim.event.ChangesInfoEventArgument()

      class ClusterStatusChangedEvent(vim.event.ClusterEvent): # vim.event.ClusterStatusChangedEvent
         oldStatus = ""
         newStatus = ""

      class CustomFieldEvent(vim.event.Event): # vim.event.CustomFieldEvent
         pass

      class CustomFieldValueChangedEvent(vim.event.CustomFieldEvent): # vim.event.CustomFieldValueChangedEvent
         entity = vim.event.ManagedEntityEventArgument()
         fieldKey = 0
         name = ""
         value = ""
         prevState = ""

      class CustomizationEvent(vim.event.VmEvent): # vim.event.CustomizationEvent
         logLocation = ""

      class CustomizationFailed(vim.event.CustomizationEvent): # vim.event.CustomizationFailed
         reason = ""

         class ReasonCode(Enum): # vim.event.CustomizationFailed.ReasonCode
            userDefinedScriptDisabled = 0

      class CustomizationLinuxIdentityFailed(vim.event.CustomizationFailed): # vim.event.CustomizationLinuxIdentityFailed
         pass

      class CustomizationNetworkSetupFailed(vim.event.CustomizationFailed): # vim.event.CustomizationNetworkSetupFailed
         pass

      class CustomizationStartedEvent(vim.event.CustomizationEvent): # vim.event.CustomizationStartedEvent
         pass

      class CustomizationSucceeded(vim.event.CustomizationEvent): # vim.event.CustomizationSucceeded
         pass

      class CustomizationSysprepFailed(vim.event.CustomizationFailed): # vim.event.CustomizationSysprepFailed
         sysprepVersion = ""
         systemVersion = ""

      class CustomizationUnknownFailure(vim.event.CustomizationFailed): # vim.event.CustomizationUnknownFailure
         pass

      class DVPortgroupEvent(vim.event.Event): # vim.event.DVPortgroupEvent
         pass

      class DVPortgroupReconfiguredEvent(vim.event.DVPortgroupEvent): # vim.event.DVPortgroupReconfiguredEvent
         configSpec = vim.dvs.DistributedVirtualPortgroup.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class DVPortgroupRenamedEvent(vim.event.DVPortgroupEvent): # vim.event.DVPortgroupRenamedEvent
         oldName = ""
         newName = ""

      class DasAdmissionControlDisabledEvent(vim.event.ClusterEvent): # vim.event.DasAdmissionControlDisabledEvent
         pass

      class DasAdmissionControlEnabledEvent(vim.event.ClusterEvent): # vim.event.DasAdmissionControlEnabledEvent
         pass

      class DasAgentFoundEvent(vim.event.ClusterEvent): # vim.event.DasAgentFoundEvent
         pass

      class DasAgentUnavailableEvent(vim.event.ClusterEvent): # vim.event.DasAgentUnavailableEvent
         pass

      class DasClusterIsolatedEvent(vim.event.ClusterEvent): # vim.event.DasClusterIsolatedEvent
         pass

      class DasDisabledEvent(vim.event.ClusterEvent): # vim.event.DasDisabledEvent
         pass

      class DasEnabledEvent(vim.event.ClusterEvent): # vim.event.DasEnabledEvent
         pass

      class DasHostFailedEvent(vim.event.ClusterEvent): # vim.event.DasHostFailedEvent
         failedHost = vim.event.HostEventArgument()

      class DasHostIsolatedEvent(vim.event.ClusterEvent): # vim.event.DasHostIsolatedEvent
         isolatedHost = vim.event.HostEventArgument()

      class DatacenterEvent(vim.event.Event): # vim.event.DatacenterEvent
         pass

      class DatacenterRenamedEvent(vim.event.DatacenterEvent): # vim.event.DatacenterRenamedEvent
         oldName = ""
         newName = ""

      class DatastoreDiscoveredEvent(vim.event.HostEvent): # vim.event.DatastoreDiscoveredEvent
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreEvent(vim.event.Event): # vim.event.DatastoreEvent
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreFileEvent(vim.event.DatastoreEvent): # vim.event.DatastoreFileEvent
         targetFile = ""
         sourceOfOperation = ""
         succeeded = False

      class DatastoreFileMovedEvent(vim.event.DatastoreFileEvent): # vim.event.DatastoreFileMovedEvent
         sourceDatastore = vim.event.DatastoreEventArgument()
         sourceFile = ""

      class DatastoreIORMReconfiguredEvent(vim.event.DatastoreEvent): # vim.event.DatastoreIORMReconfiguredEvent
         pass

      class DatastorePrincipalConfigured(vim.event.HostEvent): # vim.event.DatastorePrincipalConfigured
         datastorePrincipal = ""

      class DatastoreRemovedOnHostEvent(vim.event.HostEvent): # vim.event.DatastoreRemovedOnHostEvent
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreRenamedEvent(vim.event.DatastoreEvent): # vim.event.DatastoreRenamedEvent
         oldName = ""
         newName = ""

      class DatastoreRenamedOnHostEvent(vim.event.HostEvent): # vim.event.DatastoreRenamedOnHostEvent
         oldName = ""
         newName = ""

      class DrsDisabledEvent(vim.event.ClusterEvent): # vim.event.DrsDisabledEvent
         pass

      class DrsEnabledEvent(vim.event.ClusterEvent): # vim.event.DrsEnabledEvent
         behavior = ""

      class DrsInvocationFailedEvent(vim.event.ClusterEvent): # vim.event.DrsInvocationFailedEvent
         pass

      class DrsRecoveredFromFailureEvent(vim.event.ClusterEvent): # vim.event.DrsRecoveredFromFailureEvent
         pass

      class DrsResourceConfigureFailedEvent(vim.event.HostEvent): # vim.event.DrsResourceConfigureFailedEvent
         reason = vmodl.MethodFault()

      class DrsResourceConfigureSyncedEvent(vim.event.HostEvent): # vim.event.DrsResourceConfigureSyncedEvent
         pass

      class DrsRuleComplianceEvent(vim.event.VmEvent): # vim.event.DrsRuleComplianceEvent
         pass

      class DrsRuleViolationEvent(vim.event.VmEvent): # vim.event.DrsRuleViolationEvent
         pass

      class DrsSoftRuleViolationEvent(vim.event.VmEvent): # vim.event.DrsSoftRuleViolationEvent
         pass

      class DrsVmMigratedEvent(vim.event.VmMigratedEvent): # vim.event.DrsVmMigratedEvent
         pass

      class DrsVmPoweredOnEvent(vim.event.VmPoweredOnEvent): # vim.event.DrsVmPoweredOnEvent
         pass

      class DuplicateIpDetectedEvent(vim.event.HostEvent): # vim.event.DuplicateIpDetectedEvent
         duplicateIP = ""
         macAddress = ""

      class DvpgImportEvent(vim.event.DVPortgroupEvent): # vim.event.DvpgImportEvent
         importType = ""

      class DvpgRestoreEvent(vim.event.DVPortgroupEvent): # vim.event.DvpgRestoreEvent
         pass

      class DvsEvent(vim.event.Event): # vim.event.DvsEvent

         class PortBlockState(Enum): # vim.event.DvsEvent.PortBlockState
            unset = 0
            blocked = 1
            unblocked = 2
            unknown = 3

      class DvsHealthStatusChangeEvent(vim.event.HostEvent): # vim.event.DvsHealthStatusChangeEvent
         switchUuid = ""
         healthResult = vim.dvs.HostMember.HealthCheckResult()

      class DvsHostBackInSyncEvent(vim.event.DvsEvent): # vim.event.DvsHostBackInSyncEvent
         hostBackInSync = vim.event.HostEventArgument()

      class DvsHostJoinedEvent(vim.event.DvsEvent): # vim.event.DvsHostJoinedEvent
         hostJoined = vim.event.HostEventArgument()

      class DvsHostLeftEvent(vim.event.DvsEvent): # vim.event.DvsHostLeftEvent
         hostLeft = vim.event.HostEventArgument()

      class DvsHostStatusUpdated(vim.event.DvsEvent): # vim.event.DvsHostStatusUpdated
         hostMember = vim.event.HostEventArgument()
         oldStatus = ""
         newStatus = ""
         oldStatusDetail = ""
         newStatusDetail = ""

      class DvsHostWentOutOfSyncEvent(vim.event.DvsEvent): # vim.event.DvsHostWentOutOfSyncEvent
         hostOutOfSync = vim.event.DvsOutOfSyncHostArgument()

      class DvsImportEvent(vim.event.DvsEvent): # vim.event.DvsImportEvent
         importType = ""

      class DvsMergedEvent(vim.event.DvsEvent): # vim.event.DvsMergedEvent
         sourceDvs = vim.event.DvsEventArgument()
         destinationDvs = vim.event.DvsEventArgument()

      class DvsPortBlockedEvent(vim.event.DvsEvent): # vim.event.DvsPortBlockedEvent
         portKey = ""
         statusDetail = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
         prevBlockState = ""

      class DvsPortConnectedEvent(vim.event.DvsEvent): # vim.event.DvsPortConnectedEvent
         portKey = ""
         connectee = vim.dvs.PortConnectee()

      class DvsPortCreatedEvent(vim.event.DvsEvent): # vim.event.DvsPortCreatedEvent
         portKey = [ "" ]

      class DvsPortDeletedEvent(vim.event.DvsEvent): # vim.event.DvsPortDeletedEvent
         portKey = [ "" ]

      class DvsPortDisconnectedEvent(vim.event.DvsEvent): # vim.event.DvsPortDisconnectedEvent
         portKey = ""
         connectee = vim.dvs.PortConnectee()

      class DvsPortEnteredPassthruEvent(vim.event.DvsEvent): # vim.event.DvsPortEnteredPassthruEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortExitedPassthruEvent(vim.event.DvsEvent): # vim.event.DvsPortExitedPassthruEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortJoinPortgroupEvent(vim.event.DvsEvent): # vim.event.DvsPortJoinPortgroupEvent
         portKey = ""
         portgroupKey = ""
         portgroupName = ""

      class DvsPortLeavePortgroupEvent(vim.event.DvsEvent): # vim.event.DvsPortLeavePortgroupEvent
         portKey = ""
         portgroupKey = ""
         portgroupName = ""

      class DvsPortLinkDownEvent(vim.event.DvsEvent): # vim.event.DvsPortLinkDownEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortLinkUpEvent(vim.event.DvsEvent): # vim.event.DvsPortLinkUpEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortReconfiguredEvent(vim.event.DvsEvent): # vim.event.DvsPortReconfiguredEvent
         portKey = [ "" ]
         configChanges = [ vim.event.ChangesInfoEventArgument() ]

      class DvsPortRuntimeChangeEvent(vim.event.DvsEvent): # vim.event.DvsPortRuntimeChangeEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortUnblockedEvent(vim.event.DvsEvent): # vim.event.DvsPortUnblockedEvent
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
         prevBlockState = ""

      class DvsPortVendorSpecificStateChangeEvent(vim.event.DvsEvent): # vim.event.DvsPortVendorSpecificStateChangeEvent
         portKey = ""

      class DvsRenamedEvent(vim.event.DvsEvent): # vim.event.DvsRenamedEvent
         oldName = ""
         newName = ""

      class DvsRestoreEvent(vim.event.DvsEvent): # vim.event.DvsRestoreEvent
         pass

      class DvsUpgradeAvailableEvent(vim.event.DvsEvent): # vim.event.DvsUpgradeAvailableEvent
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradeInProgressEvent(vim.event.DvsEvent): # vim.event.DvsUpgradeInProgressEvent
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradeRejectedEvent(vim.event.DvsEvent): # vim.event.DvsUpgradeRejectedEvent
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradedEvent(vim.event.DvsEvent): # vim.event.DvsUpgradedEvent
         productInfo = vim.dvs.ProductSpec()

      class EnteredMaintenanceModeEvent(vim.event.HostEvent): # vim.event.EnteredMaintenanceModeEvent
         pass

      class EnteredStandbyModeEvent(vim.event.HostEvent): # vim.event.EnteredStandbyModeEvent
         pass

      class EnteringMaintenanceModeEvent(vim.event.HostEvent): # vim.event.EnteringMaintenanceModeEvent
         pass

      class EnteringStandbyModeEvent(vim.event.HostEvent): # vim.event.EnteringStandbyModeEvent
         pass

      class EntityEventArgument(vim.event.EventArgument): # vim.event.EntityEventArgument
         name = ""

      class ErrorUpgradeEvent(vim.event.UpgradeEvent): # vim.event.ErrorUpgradeEvent
         pass

      class ExitMaintenanceModeEvent(vim.event.HostEvent): # vim.event.ExitMaintenanceModeEvent
         pass

      class ExitStandbyModeFailedEvent(vim.event.HostEvent): # vim.event.ExitStandbyModeFailedEvent
         pass

      class ExitedStandbyModeEvent(vim.event.HostEvent): # vim.event.ExitedStandbyModeEvent
         pass

      class ExitingStandbyModeEvent(vim.event.HostEvent): # vim.event.ExitingStandbyModeEvent
         pass

      class ExtendedEvent(vim.event.GeneralEvent): # vim.event.ExtendedEvent
         eventTypeId = ""
         managedObject = vmodl.ManagedObject()
         data = [ vim.event.ExtendedEvent.Pair() ]

         class Pair(vmodl.DynamicData): # vim.event.ExtendedEvent.Pair
            key = ""
            value = ""

      class FailoverLevelRestored(vim.event.ClusterEvent): # vim.event.FailoverLevelRestored
         pass

      class FolderEventArgument(vim.event.EntityEventArgument): # vim.event.FolderEventArgument
         folder = vim.Folder()

      class GhostDvsProxySwitchDetectedEvent(vim.event.HostEvent): # vim.event.GhostDvsProxySwitchDetectedEvent
         switchUuid = [ "" ]

      class GhostDvsProxySwitchRemovedEvent(vim.event.HostEvent): # vim.event.GhostDvsProxySwitchRemovedEvent
         switchUuid = [ "" ]

      class GlobalMessageChangedEvent(vim.event.SessionEvent): # vim.event.GlobalMessageChangedEvent
         message = ""
         prevMessage = ""

      class HostAddFailedEvent(vim.event.HostEvent): # vim.event.HostAddFailedEvent
         hostname = ""

      class HostAddedEvent(vim.event.HostEvent): # vim.event.HostAddedEvent
         pass

      class HostAdminDisableEvent(vim.event.HostEvent): # vim.event.HostAdminDisableEvent
         pass

      class HostAdminEnableEvent(vim.event.HostEvent): # vim.event.HostAdminEnableEvent
         pass

      class HostCnxFailedAccountFailedEvent(vim.event.HostEvent): # vim.event.HostCnxFailedAccountFailedEvent
         pass

      class HostCnxFailedAlreadyManagedEvent(vim.event.HostEvent): # vim.event.HostCnxFailedAlreadyManagedEvent
         serverName = ""

      class HostCnxFailedBadCcagentEvent(vim.event.HostEvent): # vim.event.HostCnxFailedBadCcagentEvent
         pass

      class HostCnxFailedBadUsernameEvent(vim.event.HostEvent): # vim.event.HostCnxFailedBadUsernameEvent
         pass

      class HostCnxFailedBadVersionEvent(vim.event.HostEvent): # vim.event.HostCnxFailedBadVersionEvent
         pass

      class HostCnxFailedCcagentUpgradeEvent(vim.event.HostEvent): # vim.event.HostCnxFailedCcagentUpgradeEvent
         pass

      class HostCnxFailedEvent(vim.event.HostEvent): # vim.event.HostCnxFailedEvent
         pass

      class HostCnxFailedNetworkErrorEvent(vim.event.HostEvent): # vim.event.HostCnxFailedNetworkErrorEvent
         pass

      class HostCnxFailedNoAccessEvent(vim.event.HostEvent): # vim.event.HostCnxFailedNoAccessEvent
         pass

      class HostCnxFailedNoConnectionEvent(vim.event.HostEvent): # vim.event.HostCnxFailedNoConnectionEvent
         pass

      class HostCnxFailedNoLicenseEvent(vim.event.HostEvent): # vim.event.HostCnxFailedNoLicenseEvent
         pass

      class HostCnxFailedNotFoundEvent(vim.event.HostEvent): # vim.event.HostCnxFailedNotFoundEvent
         pass

      class HostCnxFailedTimeoutEvent(vim.event.HostEvent): # vim.event.HostCnxFailedTimeoutEvent
         pass

      class HostComplianceCheckedEvent(vim.event.HostEvent): # vim.event.HostComplianceCheckedEvent
         profile = vim.event.ProfileEventArgument()

      class HostCompliantEvent(vim.event.HostEvent): # vim.event.HostCompliantEvent
         pass

      class HostConfigAppliedEvent(vim.event.HostEvent): # vim.event.HostConfigAppliedEvent
         pass

      class HostConnectedEvent(vim.event.HostEvent): # vim.event.HostConnectedEvent
         pass

      class HostConnectionLostEvent(vim.event.HostEvent): # vim.event.HostConnectionLostEvent
         pass

      class HostDasDisabledEvent(vim.event.HostEvent): # vim.event.HostDasDisabledEvent
         pass

      class HostDasDisablingEvent(vim.event.HostEvent): # vim.event.HostDasDisablingEvent
         pass

      class HostDasEnabledEvent(vim.event.HostEvent): # vim.event.HostDasEnabledEvent
         pass

      class HostDasEnablingEvent(vim.event.HostEvent): # vim.event.HostDasEnablingEvent
         pass

      class HostDasErrorEvent(vim.event.HostEvent): # vim.event.HostDasErrorEvent
         message = ""
         reason = ""

         class HostDasErrorReason(Enum): # vim.event.HostDasErrorEvent.HostDasErrorReason
            configFailed = 0
            timeout = 1
            communicationInitFailed = 2
            healthCheckScriptFailed = 3
            agentFailed = 4
            agentShutdown = 5
            isolationAddressUnpingable = 6
            other = 7

      class HostDasEvent(vim.event.HostEvent): # vim.event.HostDasEvent
         pass

      class HostDasOkEvent(vim.event.HostEvent): # vim.event.HostDasOkEvent
         pass

      class HostDisconnectedEvent(vim.event.HostEvent): # vim.event.HostDisconnectedEvent
         reason = ""

         class ReasonCode(Enum): # vim.event.HostDisconnectedEvent.ReasonCode
            sslThumbprintVerifyFailed = 0
            licenseExpired = 1
            agentUpgrade = 2
            userRequest = 3
            insufficientLicenses = 4
            agentOutOfDate = 5
            passwordDecryptFailure = 6
            unknown = 7
            vcVRAMCapacityExceeded = 8

      class HostEnableAdminFailedEvent(vim.event.HostEvent): # vim.event.HostEnableAdminFailedEvent
         permissions = [ vim.AuthorizationManager.Permission() ]

      class HostEventArgument(vim.event.EntityEventArgument): # vim.event.HostEventArgument
         host = vim.HostSystem()

      class HostExtraNetworksEvent(vim.event.HostDasEvent): # vim.event.HostExtraNetworksEvent
         ips = ""

      class HostInventoryFullEvent(vim.event.LicenseEvent): # vim.event.HostInventoryFullEvent
         capacity = 0

      class HostIsolationIpPingFailedEvent(vim.event.HostDasEvent): # vim.event.HostIsolationIpPingFailedEvent
         isolationIp = ""

      class HostLicenseExpiredEvent(vim.event.LicenseEvent): # vim.event.HostLicenseExpiredEvent
         pass

      class HostLocalPortCreatedEvent(vim.event.DvsEvent): # vim.event.HostLocalPortCreatedEvent
         hostLocalPort = vim.dvs.DistributedVirtualPort.HostLocalPortInfo()

      class HostMissingNetworksEvent(vim.event.HostDasEvent): # vim.event.HostMissingNetworksEvent
         ips = ""

      class HostMonitoringStateChangedEvent(vim.event.ClusterEvent): # vim.event.HostMonitoringStateChangedEvent
         state = ""
         prevState = ""

      class HostNoAvailableNetworksEvent(vim.event.HostDasEvent): # vim.event.HostNoAvailableNetworksEvent
         ips = ""

      class HostNoHAEnabledPortGroupsEvent(vim.event.HostDasEvent): # vim.event.HostNoHAEnabledPortGroupsEvent
         pass

      class HostNoRedundantManagementNetworkEvent(vim.event.HostDasEvent): # vim.event.HostNoRedundantManagementNetworkEvent
         pass

      class HostNotInClusterEvent(vim.event.HostDasEvent): # vim.event.HostNotInClusterEvent
         pass

      class HostOvercommittedEvent(vim.event.ClusterOvercommittedEvent): # vim.event.HostOvercommittedEvent
         pass

      class HostPrimaryAgentNotShortNameEvent(vim.event.HostDasEvent): # vim.event.HostPrimaryAgentNotShortNameEvent
         primaryAgent = ""

      class HostShortNameInconsistentEvent(vim.event.HostDasEvent): # vim.event.HostShortNameInconsistentEvent
         shortName = ""
         shortName2 = ""

      class HostStatusChangedEvent(vim.event.ClusterStatusChangedEvent): # vim.event.HostStatusChangedEvent
         pass

      class IncorrectHostInformationEvent(vim.event.LicenseEvent): # vim.event.IncorrectHostInformationEvent
         pass

      class InfoUpgradeEvent(vim.event.UpgradeEvent): # vim.event.InfoUpgradeEvent
         pass

      class InsufficientFailoverResourcesEvent(vim.event.ClusterEvent): # vim.event.InsufficientFailoverResourcesEvent
         pass

      class InvalidEditionEvent(vim.event.LicenseEvent): # vim.event.InvalidEditionEvent
         feature = ""

      class ManagedEntityEventArgument(vim.event.EntityEventArgument): # vim.event.ManagedEntityEventArgument
         entity = vim.ManagedEntity()

      class MigrationEvent(vim.event.VmEvent): # vim.event.MigrationEvent
         fault = vmodl.MethodFault()

      class MigrationHostErrorEvent(vim.event.MigrationEvent): # vim.event.MigrationHostErrorEvent
         dstHost = vim.event.HostEventArgument()

      class MigrationHostWarningEvent(vim.event.MigrationEvent): # vim.event.MigrationHostWarningEvent
         dstHost = vim.event.HostEventArgument()

      class MigrationResourceErrorEvent(vim.event.MigrationEvent): # vim.event.MigrationResourceErrorEvent
         dstPool = vim.event.ResourcePoolEventArgument()
         dstHost = vim.event.HostEventArgument()

      class MigrationResourceWarningEvent(vim.event.MigrationEvent): # vim.event.MigrationResourceWarningEvent
         dstPool = vim.event.ResourcePoolEventArgument()
         dstHost = vim.event.HostEventArgument()

      class MigrationWarningEvent(vim.event.MigrationEvent): # vim.event.MigrationWarningEvent
         pass

      class MtuMatchEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.MtuMatchEvent
         pass

      class MtuMismatchEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.MtuMismatchEvent
         pass

      class NetworkEventArgument(vim.event.EntityEventArgument): # vim.event.NetworkEventArgument
         network = vim.Network()

      class NoAccessUserEvent(vim.event.SessionEvent): # vim.event.NoAccessUserEvent
         ipAddress = ""

      class NoMaintenanceModeDrsRecommendationForVM(vim.event.VmEvent): # vim.event.NoMaintenanceModeDrsRecommendationForVM
         pass

      class NonVIWorkloadDetectedOnDatastoreEvent(vim.event.DatastoreEvent): # vim.event.NonVIWorkloadDetectedOnDatastoreEvent
         pass

      class NotEnoughResourcesToStartVmEvent(vim.event.VmEvent): # vim.event.NotEnoughResourcesToStartVmEvent
         reason = ""

      class OutOfSyncDvsHost(vim.event.DvsEvent): # vim.event.OutOfSyncDvsHost
         hostOutOfSync = [ vim.event.DvsOutOfSyncHostArgument() ]

      class PermissionEvent(vim.event.AuthorizationEvent): # vim.event.PermissionEvent
         entity = vim.event.ManagedEntityEventArgument()
         principal = ""
         group = False

      class PermissionRemovedEvent(vim.event.PermissionEvent): # vim.event.PermissionRemovedEvent
         pass

      class PermissionUpdatedEvent(vim.event.PermissionEvent): # vim.event.PermissionUpdatedEvent
         role = vim.event.RoleEventArgument()
         propagate = False
         prevRole = vim.event.RoleEventArgument()
         prevPropagate = False

      class ProfileAssociatedEvent(vim.event.ProfileEvent): # vim.event.ProfileAssociatedEvent
         pass

      class ProfileChangedEvent(vim.event.ProfileEvent): # vim.event.ProfileChangedEvent
         pass

      class ProfileCreatedEvent(vim.event.ProfileEvent): # vim.event.ProfileCreatedEvent
         pass

      class ProfileDissociatedEvent(vim.event.ProfileEvent): # vim.event.ProfileDissociatedEvent
         pass

      class RecoveryEvent(vim.event.DvsEvent): # vim.event.RecoveryEvent
         hostName = ""
         portKey = ""
         dvsUuid = ""
         vnic = ""

      class ResourcePoolCreatedEvent(vim.event.ResourcePoolEvent): # vim.event.ResourcePoolCreatedEvent
         parent = vim.event.ResourcePoolEventArgument()

      class ResourcePoolDestroyedEvent(vim.event.ResourcePoolEvent): # vim.event.ResourcePoolDestroyedEvent
         pass

      class ResourcePoolEventArgument(vim.event.EntityEventArgument): # vim.event.ResourcePoolEventArgument
         resourcePool = vim.ResourcePool()

      class RoleEvent(vim.event.AuthorizationEvent): # vim.event.RoleEvent
         role = vim.event.RoleEventArgument()

      class RoleRemovedEvent(vim.event.RoleEvent): # vim.event.RoleRemovedEvent
         pass

      class RoleUpdatedEvent(vim.event.RoleEvent): # vim.event.RoleUpdatedEvent
         privilegeList = [ "" ]
         prevRoleName = ""
         privilegesAdded = [ "" ]
         privilegesRemoved = [ "" ]

      class RollbackEvent(vim.event.DvsEvent): # vim.event.RollbackEvent
         hostName = ""
         methodName = ""

      class ScheduledTaskCompletedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskCompletedEvent
         pass

      class ScheduledTaskCreatedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskCreatedEvent
         pass

      class ScheduledTaskEmailCompletedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskEmailCompletedEvent
         to = ""

      class ScheduledTaskEmailFailedEvent(vim.event.ScheduledTaskEvent): # vim.event.ScheduledTaskEmailFailedEvent
         to = ""
         reason = vmodl.MethodFault()

      class ScheduledTaskEventArgument(vim.event.EntityEventArgument): # vim.event.ScheduledTaskEventArgument
         scheduledTask = vim.scheduler.ScheduledTask()

      class ServerStartedSessionEvent(vim.event.SessionEvent): # vim.event.ServerStartedSessionEvent
         pass

      class TeamingMatchEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.TeamingMatchEvent
         pass

      class TeamingMisMatchEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.TeamingMisMatchEvent
         pass

      class TemplateBeingUpgradedEvent(vim.event.TemplateUpgradeEvent): # vim.event.TemplateBeingUpgradedEvent
         pass

      class UplinkPortMtuNotSupportEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.UplinkPortMtuNotSupportEvent
         pass

      class UplinkPortMtuSupportEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.UplinkPortMtuSupportEvent
         pass

      class UplinkPortVlanTrunkedEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.UplinkPortVlanTrunkedEvent
         pass

      class UplinkPortVlanUntrunkedEvent(vim.event.DvsHealthStatusChangeEvent): # vim.event.UplinkPortVlanUntrunkedEvent
         pass

      class VmAcquiredMksTicketEvent(vim.event.VmEvent): # vim.event.VmAcquiredMksTicketEvent
         pass

      class VmAcquiredTicketEvent(vim.event.VmEvent): # vim.event.VmAcquiredTicketEvent
         ticketType = ""

      class VmAutoRenameEvent(vim.event.VmEvent): # vim.event.VmAutoRenameEvent
         oldName = ""
         newName = ""

      class VmBeingCreatedEvent(vim.event.VmEvent): # vim.event.VmBeingCreatedEvent
         configSpec = vim.vm.ConfigSpec()

      class VmBeingDeployedEvent(vim.event.VmEvent): # vim.event.VmBeingDeployedEvent
         srcTemplate = vim.event.VmEventArgument()

      class VmBeingHotMigratedEvent(vim.event.VmEvent): # vim.event.VmBeingHotMigratedEvent
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmBeingMigratedEvent(vim.event.VmEvent): # vim.event.VmBeingMigratedEvent
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmBeingRelocatedEvent(vim.event.VmRelocateSpecEvent): # vim.event.VmBeingRelocatedEvent
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmCloneEvent(vim.event.VmEvent): # vim.event.VmCloneEvent
         pass

      class VmCloneFailedEvent(vim.event.VmCloneEvent): # vim.event.VmCloneFailedEvent
         destFolder = vim.event.FolderEventArgument()
         destName = ""
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()

      class VmClonedEvent(vim.event.VmCloneEvent): # vim.event.VmClonedEvent
         sourceVm = vim.event.VmEventArgument()

      class VmConfigMissingEvent(vim.event.VmEvent): # vim.event.VmConfigMissingEvent
         pass

      class VmConnectedEvent(vim.event.VmEvent): # vim.event.VmConnectedEvent
         pass

      class VmCreatedEvent(vim.event.VmEvent): # vim.event.VmCreatedEvent
         pass

      class VmDasBeingResetEvent(vim.event.VmEvent): # vim.event.VmDasBeingResetEvent
         reason = ""

         class ReasonCode(Enum): # vim.event.VmDasBeingResetEvent.ReasonCode
            vmtoolsHeartbeatFailure = 0
            appHeartbeatFailure = 1
            appImmediateResetRequest = 2
            vmcpResetApdCleared = 3
            guestOsCrashFailure = 4

      class VmDasBeingResetWithScreenshotEvent(vim.event.VmDasBeingResetEvent): # vim.event.VmDasBeingResetWithScreenshotEvent
         screenshotFilePath = ""

      class VmDasResetFailedEvent(vim.event.VmEvent): # vim.event.VmDasResetFailedEvent
         pass

      class VmDasUpdateErrorEvent(vim.event.VmEvent): # vim.event.VmDasUpdateErrorEvent
         pass

      class VmDasUpdateOkEvent(vim.event.VmEvent): # vim.event.VmDasUpdateOkEvent
         pass

      class VmDateRolledBackEvent(vim.event.VmEvent): # vim.event.VmDateRolledBackEvent
         pass

      class VmDeployFailedEvent(vim.event.VmEvent): # vim.event.VmDeployFailedEvent
         destDatastore = vim.event.EntityEventArgument()
         reason = vmodl.MethodFault()

      class VmDeployedEvent(vim.event.VmEvent): # vim.event.VmDeployedEvent
         srcTemplate = vim.event.VmEventArgument()

      class VmDisconnectedEvent(vim.event.VmEvent): # vim.event.VmDisconnectedEvent
         pass

      class VmDiscoveredEvent(vim.event.VmEvent): # vim.event.VmDiscoveredEvent
         pass

      class VmDiskFailedEvent(vim.event.VmEvent): # vim.event.VmDiskFailedEvent
         disk = ""
         reason = vmodl.MethodFault()

      class VmEmigratingEvent(vim.event.VmEvent): # vim.event.VmEmigratingEvent
         pass

      class VmEndRecordingEvent(vim.event.VmEvent): # vim.event.VmEndRecordingEvent
         pass

      class VmEndReplayingEvent(vim.event.VmEvent): # vim.event.VmEndReplayingEvent
         pass

      class VmEventArgument(vim.event.EntityEventArgument): # vim.event.VmEventArgument
         vm = vim.VirtualMachine()

      class VmFaultToleranceStateChangedEvent(vim.event.VmEvent): # vim.event.VmFaultToleranceStateChangedEvent
         oldState = vim.VirtualMachine.FaultToleranceState()
         newState = vim.VirtualMachine.FaultToleranceState()

      class VmHealthMonitoringStateChangedEvent(vim.event.ClusterEvent): # vim.event.VmHealthMonitoringStateChangedEvent
         state = ""
         prevState = ""

      class VmPowerOffOnIsolationEvent(vim.event.VmPoweredOffEvent): # vim.event.VmPowerOffOnIsolationEvent
         isolatedHost = vim.event.HostEventArgument()

      class VmRelocateFailedEvent(vim.event.VmRelocateSpecEvent): # vim.event.VmRelocateFailedEvent
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmVnicPoolReservationViolationClearEvent(vim.event.DvsEvent): # vim.event.VmVnicPoolReservationViolationClearEvent
         vmVnicResourcePoolKey = ""
         vmVnicResourcePoolName = ""

      class VmVnicPoolReservationViolationRaiseEvent(vim.event.DvsEvent): # vim.event.VmVnicPoolReservationViolationRaiseEvent
         vmVnicResourcePoolKey = ""
         vmVnicResourcePoolName = ""

      class AlarmAcknowledgedEvent(vim.event.AlarmEvent): # vim.event.AlarmAcknowledgedEvent
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmActionTriggeredEvent(vim.event.AlarmEvent): # vim.event.AlarmActionTriggeredEvent
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmClearedEvent(vim.event.AlarmEvent): # vim.event.AlarmClearedEvent
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()
         from = ""

      class AlarmCreatedEvent(vim.event.AlarmEvent): # vim.event.AlarmCreatedEvent
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmEmailCompletedEvent(vim.event.AlarmEvent): # vim.event.AlarmEmailCompletedEvent
         entity = vim.event.ManagedEntityEventArgument()
         to = ""

      class AlarmEmailFailedEvent(vim.event.AlarmEvent): # vim.event.AlarmEmailFailedEvent
         entity = vim.event.ManagedEntityEventArgument()
         to = ""
         reason = vmodl.MethodFault()

      class AlarmEventArgument(vim.event.EntityEventArgument): # vim.event.AlarmEventArgument
         alarm = vim.alarm.Alarm()

      class ClusterComplianceCheckedEvent(vim.event.ClusterEvent): # vim.event.ClusterComplianceCheckedEvent
         profile = vim.event.ProfileEventArgument()

      class ClusterCreatedEvent(vim.event.ClusterEvent): # vim.event.ClusterCreatedEvent
         parent = vim.event.FolderEventArgument()

      class ClusterDestroyedEvent(vim.event.ClusterEvent): # vim.event.ClusterDestroyedEvent
         pass

      class ComputeResourceEventArgument(vim.event.EntityEventArgument): # vim.event.ComputeResourceEventArgument
         computeResource = vim.ComputeResource()

      class CustomFieldDefEvent(vim.event.CustomFieldEvent): # vim.event.CustomFieldDefEvent
         fieldKey = 0
         name = ""

      class CustomFieldDefRemovedEvent(vim.event.CustomFieldDefEvent): # vim.event.CustomFieldDefRemovedEvent
         pass

      class CustomFieldDefRenamedEvent(vim.event.CustomFieldDefEvent): # vim.event.CustomFieldDefRenamedEvent
         newName = ""

      class DVPortgroupCreatedEvent(vim.event.DVPortgroupEvent): # vim.event.DVPortgroupCreatedEvent
         pass

      class DVPortgroupDestroyedEvent(vim.event.DVPortgroupEvent): # vim.event.DVPortgroupDestroyedEvent
         pass

      class DatacenterCreatedEvent(vim.event.DatacenterEvent): # vim.event.DatacenterCreatedEvent
         parent = vim.event.FolderEventArgument()

      class DatacenterEventArgument(vim.event.EntityEventArgument): # vim.event.DatacenterEventArgument
         datacenter = vim.Datacenter()

      class DatastoreCapacityIncreasedEvent(vim.event.DatastoreEvent): # vim.event.DatastoreCapacityIncreasedEvent
         oldCapacity = 0
         newCapacity = 0

      class DatastoreDestroyedEvent(vim.event.DatastoreEvent): # vim.event.DatastoreDestroyedEvent
         pass

      class DatastoreDuplicatedEvent(vim.event.DatastoreEvent): # vim.event.DatastoreDuplicatedEvent
         pass

      class DatastoreEventArgument(vim.event.EntityEventArgument): # vim.event.DatastoreEventArgument
         datastore = vim.Datastore()

      class DatastoreFileCopiedEvent(vim.event.DatastoreFileEvent): # vim.event.DatastoreFileCopiedEvent
         sourceDatastore = vim.event.DatastoreEventArgument()
         sourceFile = ""

      class DatastoreFileDeletedEvent(vim.event.DatastoreFileEvent): # vim.event.DatastoreFileDeletedEvent
         pass

      class DrsEnteredStandbyModeEvent(vim.event.EnteredStandbyModeEvent): # vim.event.DrsEnteredStandbyModeEvent
         pass

      class DrsEnteringStandbyModeEvent(vim.event.EnteringStandbyModeEvent): # vim.event.DrsEnteringStandbyModeEvent
         pass

      class DrsExitStandbyModeFailedEvent(vim.event.ExitStandbyModeFailedEvent): # vim.event.DrsExitStandbyModeFailedEvent
         pass

      class DrsExitedStandbyModeEvent(vim.event.ExitedStandbyModeEvent): # vim.event.DrsExitedStandbyModeEvent
         pass

      class DrsExitingStandbyModeEvent(vim.event.ExitingStandbyModeEvent): # vim.event.DrsExitingStandbyModeEvent
         pass

      class DvsCreatedEvent(vim.event.DvsEvent): # vim.event.DvsCreatedEvent
         parent = vim.event.FolderEventArgument()

      class DvsDestroyedEvent(vim.event.DvsEvent): # vim.event.DvsDestroyedEvent
         pass

      class DvsEventArgument(vim.event.EntityEventArgument): # vim.event.DvsEventArgument
         dvs = vim.DistributedVirtualSwitch()

      class DvsReconfiguredEvent(vim.event.DvsEvent): # vim.event.DvsReconfiguredEvent
         configSpec = vim.DistributedVirtualSwitch.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class MigrationErrorEvent(vim.event.MigrationEvent): # vim.event.MigrationErrorEvent
         pass

      class PermissionAddedEvent(vim.event.PermissionEvent): # vim.event.PermissionAddedEvent
         role = vim.event.RoleEventArgument()
         propagate = False

      class RoleAddedEvent(vim.event.RoleEvent): # vim.event.RoleAddedEvent
         privilegeList = [ "" ]

      class VmBeingClonedEvent(vim.event.VmCloneEvent): # vim.event.VmBeingClonedEvent
         destFolder = vim.event.FolderEventArgument()
         destName = ""
         destHost = vim.event.HostEventArgument()

      class VmBeingClonedNoFolderEvent(vim.event.VmCloneEvent): # vim.event.VmBeingClonedNoFolderEvent
         destName = ""
         destHost = vim.event.HostEventArgument()

      class CustomFieldDefAddedEvent(vim.event.CustomFieldDefEvent): # vim.event.CustomFieldDefAddedEvent
         pass

   class ext(object): # (unknown name)

      class ExtendedProductInfo(vmodl.DynamicData): # vim.ext.ExtendedProductInfo
         companyUrl = ""
         productUrl = ""
         managementUrl = ""
         self = vim.ManagedEntity()

      class ManagedByInfo(vmodl.DynamicData): # vim.ext.ManagedByInfo
         extensionKey = ""
         type = ""

      class ManagedEntityInfo(vmodl.DynamicData): # vim.ext.ManagedEntityInfo
         type = ""
         smallIconUrl = ""
         iconUrl = ""
         description = ""

      class SolutionManagerInfo(vmodl.DynamicData): # vim.ext.SolutionManagerInfo
         tab = [ vim.ext.SolutionManagerInfo.TabInfo() ]
         smallIconUrl = ""

         class TabInfo(vmodl.DynamicData): # vim.ext.SolutionManagerInfo.TabInfo
            label = ""
            url = ""

   class fault(object): # (unknown name)

      class CannotDisableDrsOnClustersWithVApps(vmodl.RuntimeFault): # vim.fault.CannotDisableDrsOnClustersWithVApps
         pass

      class ConflictingDatastoreFound(vmodl.RuntimeFault): # vim.fault.ConflictingDatastoreFound
         name = ""
         url = ""

      class DatabaseError(vmodl.RuntimeFault): # vim.fault.DatabaseError
         pass

      class DisallowedChangeByService(vmodl.RuntimeFault): # vim.fault.DisallowedChangeByService
         serviceName = ""
         disallowedChange = ""

         class DisallowedChange(Enum): # vim.fault.DisallowedChangeByService.DisallowedChange
            hotExtendDisk = 0

      class DisallowedOperationOnFailoverHost(vmodl.RuntimeFault): # vim.fault.DisallowedOperationOnFailoverHost
         host = vim.HostSystem()
         hostname = ""

      class ExpiredFeatureLicense(vmodl.fault.NotEnoughLicenses): # vim.fault.ExpiredFeatureLicense
         feature = ""
         count = 0
         expirationDate = vmodl.DateTime()

      class FailToLockFaultToleranceVMs(vmodl.RuntimeFault): # vim.fault.FailToLockFaultToleranceVMs
         vmName = ""
         vm = vim.VirtualMachine()
         alreadyLockedVm = vim.VirtualMachine()

      class HostAccessRestrictedToManagementServer(vmodl.fault.NotSupported): # vim.fault.HostAccessRestrictedToManagementServer
         managementServer = ""

      class HostInventoryFull(vmodl.fault.NotEnoughLicenses): # vim.fault.HostInventoryFull
         capacity = 0

      class InUseFeatureManipulationDisallowed(vmodl.fault.NotEnoughLicenses): # vim.fault.InUseFeatureManipulationDisallowed
         pass

      class IncompatibleSetting(vmodl.fault.InvalidArgument): # vim.fault.IncompatibleSetting
         conflictingProperty = vmodl.PropertyPath()

      class IncorrectHostInformation(vmodl.fault.NotEnoughLicenses): # vim.fault.IncorrectHostInformation
         pass

      class InvalidDasConfigArgument(vmodl.fault.InvalidArgument): # vim.fault.InvalidDasConfigArgument
         entry = ""
         clusterName = ""

         class EntryForInvalidArgument(Enum): # vim.fault.InvalidDasConfigArgument.EntryForInvalidArgument
            admissionControl = 0
            userHeartbeatDs = 1
            vmConfig = 2

      class InvalidDasRestartPriorityForFtVm(vmodl.fault.InvalidArgument): # vim.fault.InvalidDasRestartPriorityForFtVm
         vm = vim.VirtualMachine()
         vmName = ""

      class InvalidDrsBehaviorForFtVm(vmodl.fault.InvalidArgument): # vim.fault.InvalidDrsBehaviorForFtVm
         vm = vim.VirtualMachine()
         vmName = ""

      class InvalidEditionLicense(vmodl.fault.NotEnoughLicenses): # vim.fault.InvalidEditionLicense
         feature = ""

      class InvalidIndexArgument(vmodl.fault.InvalidArgument): # vim.fault.InvalidIndexArgument
         key = ""

      class InvalidProfileReferenceHost(vmodl.RuntimeFault): # vim.fault.InvalidProfileReferenceHost
         reason = ""
         host = vim.HostSystem()
         profile = vim.profile.Profile()
         profileName = ""

         class Reason(Enum): # vim.fault.InvalidProfileReferenceHost.Reason
            incompatibleVersion = 0
            missingReferenceHost = 1

      class InventoryHasStandardAloneHosts(vmodl.fault.NotEnoughLicenses): # vim.fault.InventoryHasStandardAloneHosts
         hosts = [ "" ]

      class LicenseAssignmentFailed(vmodl.RuntimeFault): # vim.fault.LicenseAssignmentFailed
         reason = ""

         class Reason(Enum): # vim.fault.LicenseAssignmentFailed.Reason
            keyEntityMismatch = 0
            downgradeDisallowed = 1
            inventoryNotManageableByVirtualCenter = 2
            hostsUnmanageableByVirtualCenterWithoutLicenseServer = 3

      class LicenseDowngradeDisallowed(vmodl.fault.NotEnoughLicenses): # vim.fault.LicenseDowngradeDisallowed
         edition = ""
         entityId = ""
         features = [ vmodl.KeyAnyValue() ]

      class LicenseExpired(vmodl.fault.NotEnoughLicenses): # vim.fault.LicenseExpired
         licenseKey = ""

      class LicenseKeyEntityMismatch(vmodl.fault.NotEnoughLicenses): # vim.fault.LicenseKeyEntityMismatch
         pass

      class LicenseRestricted(vmodl.fault.NotEnoughLicenses): # vim.fault.LicenseRestricted
         pass

      class LicenseSourceUnavailable(vmodl.fault.NotEnoughLicenses): # vim.fault.LicenseSourceUnavailable
         licenseSource = vim.LicenseManager.LicenseSource()

      class MethodAlreadyDisabledFault(vmodl.RuntimeFault): # vim.fault.MethodAlreadyDisabledFault
         sourceId = ""

      class MethodDisabled(vmodl.RuntimeFault): # vim.fault.MethodDisabled
         source = ""

      class NoLicenseServerConfigured(vmodl.fault.NotEnoughLicenses): # vim.fault.NoLicenseServerConfigured
         pass

      class NoPermission(vmodl.fault.SecurityError): # vim.fault.NoPermission
         object = vmodl.ManagedObject()
         privilegeId = ""

      class NotAuthenticated(vim.fault.NoPermission): # vim.fault.NotAuthenticated
         pass

      class OperationDisallowedOnHost(vmodl.RuntimeFault): # vim.fault.OperationDisallowedOnHost
         pass

      class RestrictedByAdministrator(vmodl.RuntimeFault): # vim.fault.RestrictedByAdministrator
         details = ""

      class RestrictedVersion(vmodl.fault.SecurityError): # vim.fault.RestrictedVersion
         pass

      class SolutionUserRequired(vmodl.fault.SecurityError): # vim.fault.SolutionUserRequired
         pass

      class ThirdPartyLicenseAssignmentFailed(vmodl.RuntimeFault): # vim.fault.ThirdPartyLicenseAssignmentFailed
         host = vim.HostSystem()
         module = ""
         reason = ""

         class Reason(Enum): # vim.fault.ThirdPartyLicenseAssignmentFailed.Reason
            licenseAssignmentFailed = 0
            moduleNotInstalled = 1

      class VAppOperationInProgress(vmodl.RuntimeFault): # vim.fault.VAppOperationInProgress
         pass

      class VimFault(vmodl.MethodFault): # vim.fault.VimFault
         pass

      class VmConfigFault(vim.fault.VimFault): # vim.fault.VmConfigFault
         pass

      class VmConfigIncompatibleForFaultTolerance(vim.fault.VmConfigFault): # vim.fault.VmConfigIncompatibleForFaultTolerance
         fault = vmodl.MethodFault()

      class VmConfigIncompatibleForRecordReplay(vim.fault.VmConfigFault): # vim.fault.VmConfigIncompatibleForRecordReplay
         fault = vmodl.MethodFault()

      class VmFaultToleranceIssue(vim.fault.VimFault): # vim.fault.VmFaultToleranceIssue
         pass

      class VmFaultToleranceOpIssuesList(vim.fault.VmFaultToleranceIssue): # vim.fault.VmFaultToleranceOpIssuesList
         errors = [ vmodl.MethodFault() ]
         warnings = [ vmodl.MethodFault() ]

      class VmHostAffinityRuleViolation(vim.fault.VmConfigFault): # vim.fault.VmHostAffinityRuleViolation
         vmName = ""
         hostName = ""

      class VmLimitLicense(vmodl.fault.NotEnoughLicenses): # vim.fault.VmLimitLicense
         limit = 0

      class VmMetadataManagerFault(vim.fault.VimFault): # vim.fault.VmMetadataManagerFault
         pass

      class VmMonitorIncompatibleForFaultTolerance(vim.fault.VimFault): # vim.fault.VmMonitorIncompatibleForFaultTolerance
         pass

      class VmToolsUpgradeFault(vim.fault.VimFault): # vim.fault.VmToolsUpgradeFault
         pass

      class VmValidateMaxDevice(vim.fault.VimFault): # vim.fault.VmValidateMaxDevice
         device = ""
         max = 0
         count = 0

      class VramLimitLicense(vmodl.fault.NotEnoughLicenses): # vim.fault.VramLimitLicense
         limit = 0

      class VsanFault(vim.fault.VimFault): # vim.fault.VsanFault
         pass

      class WipeDiskFault(vim.fault.VimFault): # vim.fault.WipeDiskFault
         pass

      class ActiveDirectoryFault(vim.fault.VimFault): # vim.fault.ActiveDirectoryFault
         errorCode = 0

      class AlreadyExists(vim.fault.VimFault): # vim.fault.AlreadyExists
         name = ""

      class AlreadyUpgraded(vim.fault.VimFault): # vim.fault.AlreadyUpgraded
         pass

      class AnswerFileUpdateFailed(vim.fault.VimFault): # vim.fault.AnswerFileUpdateFailed
         failure = [ vim.fault.AnswerFileUpdateFailed.UpdateFailure() ]

         class UpdateFailure(vmodl.DynamicData): # vim.fault.AnswerFileUpdateFailed.UpdateFailure
            userInputPath = vim.profile.ProfilePropertyPath()
            errMsg = vmodl.LocalizableMessage()

      class AuthMinimumAdminPermission(vim.fault.VimFault): # vim.fault.AuthMinimumAdminPermission
         pass

      class CannotAccessLocalSource(vim.fault.VimFault): # vim.fault.CannotAccessLocalSource
         pass

      class CannotAccessVmComponent(vim.fault.VmConfigFault): # vim.fault.CannotAccessVmComponent
         pass

      class CannotAccessVmConfig(vim.fault.CannotAccessVmComponent): # vim.fault.CannotAccessVmConfig
         reason = vmodl.MethodFault()

      class CannotAccessVmDevice(vim.fault.CannotAccessVmComponent): # vim.fault.CannotAccessVmDevice
         device = ""
         backing = ""
         connected = False

      class CannotAccessVmDisk(vim.fault.CannotAccessVmDevice): # vim.fault.CannotAccessVmDisk
         fault = vmodl.MethodFault()

      class CannotChangeDrsBehaviorForFtSecondary(vim.fault.VmFaultToleranceIssue): # vim.fault.CannotChangeDrsBehaviorForFtSecondary
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotChangeHaSettingsForFtSecondary(vim.fault.VmFaultToleranceIssue): # vim.fault.CannotChangeHaSettingsForFtSecondary
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotChangeVsanClusterUuid(vim.fault.VsanFault): # vim.fault.CannotChangeVsanClusterUuid
         pass

      class CannotChangeVsanNodeUuid(vim.fault.VsanFault): # vim.fault.CannotChangeVsanNodeUuid
         pass

      class CannotComputeFTCompatibleHosts(vim.fault.VmFaultToleranceIssue): # vim.fault.CannotComputeFTCompatibleHosts
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotDisableSnapshot(vim.fault.VmConfigFault): # vim.fault.CannotDisableSnapshot
         pass

      class CannotDisconnectHostWithFaultToleranceVm(vim.fault.VimFault): # vim.fault.CannotDisconnectHostWithFaultToleranceVm
         hostName = ""

      class CannotEnableVmcpForCluster(vim.fault.VimFault): # vim.fault.CannotEnableVmcpForCluster
         host = vim.HostSystem()
         hostName = ""
         reason = ""

         class Reason(Enum): # vim.fault.CannotEnableVmcpForCluster.Reason
            APDTimeoutDisabled = 0

      class CannotMoveFaultToleranceVm(vim.fault.VimFault): # vim.fault.CannotMoveFaultToleranceVm
         moveType = ""
         vmName = ""

         class MoveType(Enum): # vim.fault.CannotMoveFaultToleranceVm.MoveType
            resourcePool = 0
            cluster = 1

      class CannotMoveHostWithFaultToleranceVm(vim.fault.VimFault): # vim.fault.CannotMoveHostWithFaultToleranceVm
         pass

      class CannotMoveVsanEnabledHost(vim.fault.VsanFault): # vim.fault.CannotMoveVsanEnabledHost
         pass

      class CannotPlaceWithoutPrerequisiteMoves(vim.fault.VimFault): # vim.fault.CannotPlaceWithoutPrerequisiteMoves
         pass

      class CannotReconfigureVsanWhenHaEnabled(vim.fault.VsanFault): # vim.fault.CannotReconfigureVsanWhenHaEnabled
         pass

      class CannotUseNetwork(vim.fault.VmConfigFault): # vim.fault.CannotUseNetwork
         device = ""
         backing = ""
         connected = False
         reason = ""
         network = vim.Network()

         class Reason(Enum): # vim.fault.CannotUseNetwork.Reason
            NetworkReservationNotSupported = 0
            MismatchedNetworkPolicies = 1
            MismatchedDvsVersionOrVendor = 2
            VMotionToUnsupportedNetworkType = 3
            NetworkUnderMaintenance = 4
            MismatchedEnsMode = 5

      class ConcurrentAccess(vim.fault.VimFault): # vim.fault.ConcurrentAccess
         pass

      class CpuHotPlugNotSupported(vim.fault.VmConfigFault): # vim.fault.CpuHotPlugNotSupported
         pass

      class CustomizationFault(vim.fault.VimFault): # vim.fault.CustomizationFault
         pass

      class CustomizationPending(vim.fault.CustomizationFault): # vim.fault.CustomizationPending
         pass

      class DasConfigFault(vim.fault.VimFault): # vim.fault.DasConfigFault
         reason = ""
         output = ""
         event = [ vim.event.Event() ]

         class DasConfigFaultReason(Enum): # vim.fault.DasConfigFault.DasConfigFaultReason
            HostNetworkMisconfiguration = 0
            HostMisconfiguration = 1
            InsufficientPrivileges = 2
            NoPrimaryAgentAvailable = 3
            Other = 4
            NoDatastoresConfigured = 5
            CreateConfigVvolFailed = 6
            VSanNotSupportedOnHost = 7
            DasNetworkMisconfiguration = 8
            SetDesiredImageSpecFailed = 9
            ApplyHAVibsOnClusterFailed = 10

      class DeltaDiskFormatNotSupported(vim.fault.VmConfigFault): # vim.fault.DeltaDiskFormatNotSupported
         datastore = [ vim.Datastore() ]
         deltaDiskFormat = ""

      class DestinationVsanDisabled(vim.fault.CannotMoveVsanEnabledHost): # vim.fault.DestinationVsanDisabled
         destinationCluster = ""

      class DomainNotFound(vim.fault.ActiveDirectoryFault): # vim.fault.DomainNotFound
         domainName = ""

      class DrsDisabledOnVm(vim.fault.VimFault): # vim.fault.DrsDisabledOnVm
         pass

      class DuplicateName(vim.fault.VimFault): # vim.fault.DuplicateName
         name = ""
         object = vmodl.ManagedObject()

      class DuplicateVsanNetworkInterface(vim.fault.VsanFault): # vim.fault.DuplicateVsanNetworkInterface
         device = ""

      class DvsFault(vim.fault.VimFault): # vim.fault.DvsFault
         pass

      class DvsNotAuthorized(vim.fault.DvsFault): # vim.fault.DvsNotAuthorized
         sessionExtensionKey = ""
         dvsExtensionKey = ""

      class DvsOperationBulkFault(vim.fault.DvsFault): # vim.fault.DvsOperationBulkFault
         hostFault = [ vim.fault.DvsOperationBulkFault.FaultOnHost() ]

         class FaultOnHost(vmodl.DynamicData): # vim.fault.DvsOperationBulkFault.FaultOnHost
            host = vim.HostSystem()
            fault = vmodl.MethodFault()

      class DvsScopeViolated(vim.fault.DvsFault): # vim.fault.DvsScopeViolated
         scope = [ vim.ManagedEntity() ]
         entity = vim.ManagedEntity()

      class EVCConfigFault(vim.fault.VimFault): # vim.fault.EVCConfigFault
         faults = [ vmodl.MethodFault() ]

      class EVCModeIllegalByVendor(vim.fault.EVCConfigFault): # vim.fault.EVCModeIllegalByVendor
         clusterCPUVendor = ""
         modeCPUVendor = ""

      class EVCModeUnsupportedByHosts(vim.fault.EVCConfigFault): # vim.fault.EVCModeUnsupportedByHosts
         evcMode = ""
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EVCUnsupportedByHostHardware(vim.fault.EVCConfigFault): # vim.fault.EVCUnsupportedByHostHardware
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EVCUnsupportedByHostSoftware(vim.fault.EVCConfigFault): # vim.fault.EVCUnsupportedByHostSoftware
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EightHostLimitViolated(vim.fault.VmConfigFault): # vim.fault.EightHostLimitViolated
         pass

      class ExpiredAddonLicense(vim.fault.ExpiredFeatureLicense): # vim.fault.ExpiredAddonLicense
         pass

      class ExpiredEditionLicense(vim.fault.ExpiredFeatureLicense): # vim.fault.ExpiredEditionLicense
         pass

      class ExtendedFault(vim.fault.VimFault): # vim.fault.ExtendedFault
         faultTypeId = ""
         data = [ vim.KeyValue() ]

      class FaultToleranceCannotEditMem(vim.fault.VmConfigFault): # vim.fault.FaultToleranceCannotEditMem
         vmName = ""
         vm = vim.VirtualMachine()

      class FaultToleranceNotLicensed(vim.fault.VmFaultToleranceIssue): # vim.fault.FaultToleranceNotLicensed
         hostName = ""

      class FaultTolerancePrimaryPowerOnNotAttempted(vim.fault.VmFaultToleranceIssue): # vim.fault.FaultTolerancePrimaryPowerOnNotAttempted
         secondaryVm = vim.VirtualMachine()
         primaryVm = vim.VirtualMachine()

      class FaultToleranceVmNotDasProtected(vim.fault.VimFault): # vim.fault.FaultToleranceVmNotDasProtected
         vm = vim.VirtualMachine()
         vmName = ""

      class FcoeFault(vim.fault.VimFault): # vim.fault.FcoeFault
         pass

      class FcoeFaultPnicHasNoPortSet(vim.fault.FcoeFault): # vim.fault.FcoeFaultPnicHasNoPortSet
         nicDevice = ""

      class FileFault(vim.fault.VimFault): # vim.fault.FileFault
         file = ""

      class FileLocked(vim.fault.FileFault): # vim.fault.FileLocked
         pass

      class FileNameTooLong(vim.fault.FileFault): # vim.fault.FileNameTooLong
         pass

      class FileNotFound(vim.fault.FileFault): # vim.fault.FileNotFound
         pass

      class FileNotWritable(vim.fault.FileFault): # vim.fault.FileNotWritable
         pass

      class FileTooLarge(vim.fault.FileFault): # vim.fault.FileTooLarge
         datastore = ""
         fileSize = 0
         maxFileSize = 0

      class FtIssuesOnHost(vim.fault.VmFaultToleranceIssue): # vim.fault.FtIssuesOnHost
         host = vim.HostSystem()
         hostName = ""
         errors = [ vmodl.MethodFault() ]

         class HostSelectionType(Enum): # vim.fault.FtIssuesOnHost.HostSelectionType
            user = 0
            vc = 1
            drs = 2

      class GenericDrsFault(vim.fault.VimFault): # vim.fault.GenericDrsFault
         hostFaults = [ vmodl.MethodFault() ]

      class GenericVmConfigFault(vim.fault.VmConfigFault): # vim.fault.GenericVmConfigFault
         reason = ""

      class GuestOperationsFault(vim.fault.VimFault): # vim.fault.GuestOperationsFault
         pass

      class GuestOperationsUnavailable(vim.fault.GuestOperationsFault): # vim.fault.GuestOperationsUnavailable
         pass

      class GuestPermissionDenied(vim.fault.GuestOperationsFault): # vim.fault.GuestPermissionDenied
         pass

      class GuestProcessNotFound(vim.fault.GuestOperationsFault): # vim.fault.GuestProcessNotFound
         pid = 0

      class GuestRegistryFault(vim.fault.GuestOperationsFault): # vim.fault.GuestRegistryFault
         windowsSystemErrorCode = 0

      class GuestRegistryKeyFault(vim.fault.GuestRegistryFault): # vim.fault.GuestRegistryKeyFault
         keyName = ""

      class GuestRegistryKeyHasSubkeys(vim.fault.GuestRegistryKeyFault): # vim.fault.GuestRegistryKeyHasSubkeys
         pass

      class GuestRegistryKeyInvalid(vim.fault.GuestRegistryKeyFault): # vim.fault.GuestRegistryKeyInvalid
         pass

      class GuestRegistryKeyParentVolatile(vim.fault.GuestRegistryKeyFault): # vim.fault.GuestRegistryKeyParentVolatile
         pass

      class GuestRegistryValueFault(vim.fault.GuestRegistryFault): # vim.fault.GuestRegistryValueFault
         keyName = ""
         valueName = ""

      class GuestRegistryValueNotFound(vim.fault.GuestRegistryValueFault): # vim.fault.GuestRegistryValueNotFound
         pass

      class HeterogenousHostsBlockingEVC(vim.fault.EVCConfigFault): # vim.fault.HeterogenousHostsBlockingEVC
         pass

      class HostConfigFault(vim.fault.VimFault): # vim.fault.HostConfigFault
         pass

      class HostConnectFault(vim.fault.VimFault): # vim.fault.HostConnectFault
         pass

      class HostHasComponentFailure(vim.fault.VimFault): # vim.fault.HostHasComponentFailure
         hostName = ""
         componentType = ""
         componentName = ""

         class HostComponentType(Enum): # vim.fault.HostHasComponentFailure.HostComponentType
            Datastore = 0

      class HostInDomain(vim.fault.HostConfigFault): # vim.fault.HostInDomain
         pass

      class HostIncompatibleForFaultTolerance(vim.fault.VmFaultToleranceIssue): # vim.fault.HostIncompatibleForFaultTolerance
         hostName = ""
         reason = ""

         class Reason(Enum): # vim.fault.HostIncompatibleForFaultTolerance.Reason
            product = 0
            processor = 1

      class HostIncompatibleForRecordReplay(vim.fault.VimFault): # vim.fault.HostIncompatibleForRecordReplay
         hostName = ""
         reason = ""

         class Reason(Enum): # vim.fault.HostIncompatibleForRecordReplay.Reason
            product = 0
            processor = 1

      class HostPowerOpFailed(vim.fault.VimFault): # vim.fault.HostPowerOpFailed
         pass

      class HostSpecificationOperationFailed(vim.fault.VimFault): # vim.fault.HostSpecificationOperationFailed
         host = vim.HostSystem()

      class HttpFault(vim.fault.VimFault): # vim.fault.HttpFault
         statusCode = 0
         statusMessage = ""

      class IORMNotSupportedHostOnDatastore(vim.fault.VimFault): # vim.fault.IORMNotSupportedHostOnDatastore
         datastore = vim.Datastore()
         datastoreName = ""
         host = [ vim.HostSystem() ]

      class ImportHostAddFailure(vim.fault.DvsFault): # vim.fault.ImportHostAddFailure
         hostIp = [ "" ]

      class ImportOperationBulkFault(vim.fault.DvsFault): # vim.fault.ImportOperationBulkFault
         importFaults = [ vim.fault.ImportOperationBulkFault.FaultOnImport() ]

         class FaultOnImport(vmodl.DynamicData): # vim.fault.ImportOperationBulkFault.FaultOnImport
            entityType = ""
            key = ""
            fault = vmodl.MethodFault()

      class InaccessibleVFlashSource(vim.fault.VimFault): # vim.fault.InaccessibleVFlashSource
         hostName = ""

      class IncompatibleHostForFtSecondary(vim.fault.VmFaultToleranceIssue): # vim.fault.IncompatibleHostForFtSecondary
         host = vim.HostSystem()
         error = [ vmodl.MethodFault() ]

      class IncorrectFileType(vim.fault.FileFault): # vim.fault.IncorrectFileType
         pass

      class InsufficientResourcesFault(vim.fault.VimFault): # vim.fault.InsufficientResourcesFault
         pass

      class InsufficientStandbyResource(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientStandbyResource
         pass

      class InsufficientStorageIops(vim.fault.VimFault): # vim.fault.InsufficientStorageIops
         unreservedIops = 0
         requestedIops = 0
         datastoreName = ""

      class InsufficientStorageSpace(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientStorageSpace
         pass

      class InsufficientVFlashResourcesFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientVFlashResourcesFault
         freeSpaceInMB = 0
         freeSpace = 0
         requestedSpaceInMB = 0
         requestedSpace = 0

      class InvalidAffinitySettingFault(vim.fault.VimFault): # vim.fault.InvalidAffinitySettingFault
         pass

      class InvalidBmcRole(vim.fault.VimFault): # vim.fault.InvalidBmcRole
         pass

      class InvalidCAMServer(vim.fault.ActiveDirectoryFault): # vim.fault.InvalidCAMServer
         camServer = ""

      class InvalidDatastore(vim.fault.VimFault): # vim.fault.InvalidDatastore
         datastore = vim.Datastore()
         name = ""

      class InvalidDatastorePath(vim.fault.InvalidDatastore): # vim.fault.InvalidDatastorePath
         datastorePath = ""

      class InvalidEvent(vim.fault.VimFault): # vim.fault.InvalidEvent
         pass

      class InvalidFolder(vim.fault.VimFault): # vim.fault.InvalidFolder
         target = vim.ManagedEntity()

      class InvalidFormat(vim.fault.VmConfigFault): # vim.fault.InvalidFormat
         pass

      class InvalidGuestLogin(vim.fault.GuestOperationsFault): # vim.fault.InvalidGuestLogin
         pass

      class InvalidHostName(vim.fault.HostConfigFault): # vim.fault.InvalidHostName
         pass

      class InvalidIpfixConfig(vim.fault.DvsFault): # vim.fault.InvalidIpfixConfig
         property = vmodl.PropertyPath()

      class InvalidIpmiLoginInfo(vim.fault.VimFault): # vim.fault.InvalidIpmiLoginInfo
         pass

      class InvalidIpmiMacAddress(vim.fault.VimFault): # vim.fault.InvalidIpmiMacAddress
         userProvidedMacAddress = ""
         observedMacAddress = ""

      class InvalidLicense(vim.fault.VimFault): # vim.fault.InvalidLicense
         licenseContent = ""

      class InvalidLocale(vim.fault.VimFault): # vim.fault.InvalidLocale
         pass

      class InvalidLogin(vim.fault.VimFault): # vim.fault.InvalidLogin
         pass

      class InvalidName(vim.fault.VimFault): # vim.fault.InvalidName
         name = ""
         entity = vim.ManagedEntity()

      class InvalidOperationOnSecondaryVm(vim.fault.VmFaultToleranceIssue): # vim.fault.InvalidOperationOnSecondaryVm
         instanceUuid = ""

      class InvalidPrivilege(vim.fault.VimFault): # vim.fault.InvalidPrivilege
         privilege = ""

      class InvalidResourcePoolStructureFault(vim.fault.InsufficientResourcesFault): # vim.fault.InvalidResourcePoolStructureFault
         pass

      class InvalidSnapshotFormat(vim.fault.InvalidFormat): # vim.fault.InvalidSnapshotFormat
         pass

      class InvalidState(vim.fault.VimFault): # vim.fault.InvalidState
         pass

      class InvalidVmConfig(vim.fault.VmConfigFault): # vim.fault.InvalidVmConfig
         property = vmodl.PropertyPath()

      class InvalidVmState(vim.fault.InvalidState): # vim.fault.InvalidVmState
         vm = vim.VirtualMachine()

      class IpHostnameGeneratorError(vim.fault.CustomizationFault): # vim.fault.IpHostnameGeneratorError
         pass

      class IscsiFault(vim.fault.VimFault): # vim.fault.IscsiFault
         pass

      class IscsiFaultInvalidVnic(vim.fault.IscsiFault): # vim.fault.IscsiFaultInvalidVnic
         vnicDevice = ""

      class IscsiFaultPnicInUse(vim.fault.IscsiFault): # vim.fault.IscsiFaultPnicInUse
         pnicDevice = ""

      class IscsiFaultVnicAlreadyBound(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicAlreadyBound
         vnicDevice = ""

      class IscsiFaultVnicHasActivePaths(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicHasActivePaths
         vnicDevice = ""

      class IscsiFaultVnicHasMultipleUplinks(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicHasMultipleUplinks
         vnicDevice = ""

      class IscsiFaultVnicHasNoUplinks(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicHasNoUplinks
         vnicDevice = ""

      class IscsiFaultVnicHasWrongUplink(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicHasWrongUplink
         vnicDevice = ""

      class IscsiFaultVnicInUse(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicInUse
         vnicDevice = ""

      class IscsiFaultVnicIsLastPath(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicIsLastPath
         vnicDevice = ""

      class IscsiFaultVnicNotBound(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicNotBound
         vnicDevice = ""

      class IscsiFaultVnicNotFound(vim.fault.IscsiFault): # vim.fault.IscsiFaultVnicNotFound
         vnicDevice = ""

      class KeyNotFound(vim.fault.VimFault): # vim.fault.KeyNotFound
         key = ""

      class LargeRDMNotSupportedOnDatastore(vim.fault.VmConfigFault): # vim.fault.LargeRDMNotSupportedOnDatastore
         device = ""
         datastore = vim.Datastore()
         datastoreName = ""

      class LicenseEntityNotFound(vim.fault.VimFault): # vim.fault.LicenseEntityNotFound
         entityId = ""

      class LicenseServerUnavailable(vim.fault.VimFault): # vim.fault.LicenseServerUnavailable
         licenseServer = ""

      class LimitExceeded(vim.fault.VimFault): # vim.fault.LimitExceeded
         property = vmodl.PropertyPath()
         limit = 0

      class LinuxVolumeNotClean(vim.fault.CustomizationFault): # vim.fault.LinuxVolumeNotClean
         pass

      class LogBundlingFailed(vim.fault.VimFault): # vim.fault.LogBundlingFailed
         pass

      class MemoryHotPlugNotSupported(vim.fault.VmConfigFault): # vim.fault.MemoryHotPlugNotSupported
         pass

      class MigrationFault(vim.fault.VimFault): # vim.fault.MigrationFault
         pass

      class MigrationFeatureNotSupported(vim.fault.MigrationFault): # vim.fault.MigrationFeatureNotSupported
         atSourceHost = False
         failedHostName = ""
         failedHost = vim.HostSystem()

      class MigrationNotReady(vim.fault.MigrationFault): # vim.fault.MigrationNotReady
         reason = ""

      class MismatchedBundle(vim.fault.VimFault): # vim.fault.MismatchedBundle
         bundleUuid = ""
         hostUuid = ""
         bundleBuildNumber = 0
         hostBuildNumber = 0

      class MismatchedNetworkPolicies(vim.fault.MigrationFault): # vim.fault.MismatchedNetworkPolicies
         device = ""
         backing = ""
         connected = False

      class MismatchedVMotionNetworkNames(vim.fault.MigrationFault): # vim.fault.MismatchedVMotionNetworkNames
         sourceNetwork = ""
         destNetwork = ""

      class MissingBmcSupport(vim.fault.VimFault): # vim.fault.MissingBmcSupport
         pass

      class MissingLinuxCustResources(vim.fault.CustomizationFault): # vim.fault.MissingLinuxCustResources
         pass

      class MissingWindowsCustResources(vim.fault.CustomizationFault): # vim.fault.MissingWindowsCustResources
         pass

      class MksConnectionLimitReached(vim.fault.InvalidState): # vim.fault.MksConnectionLimitReached
         connectionLimit = 0

      class MountError(vim.fault.CustomizationFault): # vim.fault.MountError
         vm = vim.VirtualMachine()
         diskIndex = 0

      class MultipleCertificatesVerifyFault(vim.fault.HostConnectFault): # vim.fault.MultipleCertificatesVerifyFault
         thumbprintData = [ vim.fault.MultipleCertificatesVerifyFault.ThumbprintData() ]

         class ThumbprintData(vmodl.DynamicData): # vim.fault.MultipleCertificatesVerifyFault.ThumbprintData
            port = 0
            thumbprint = ""

      class NamespaceFull(vim.fault.VimFault): # vim.fault.NamespaceFull
         name = ""
         currentMaxSize = 0
         requiredSize = 0

      class NamespaceLimitReached(vim.fault.VimFault): # vim.fault.NamespaceLimitReached
         limit = 0

      class NamespaceWriteProtected(vim.fault.VimFault): # vim.fault.NamespaceWriteProtected
         name = ""

      class NasConfigFault(vim.fault.HostConfigFault): # vim.fault.NasConfigFault
         name = ""

      class NasConnectionLimitReached(vim.fault.NasConfigFault): # vim.fault.NasConnectionLimitReached
         remoteHost = ""
         remotePath = ""

      class NasSessionCredentialConflict(vim.fault.NasConfigFault): # vim.fault.NasSessionCredentialConflict
         remoteHost = ""
         remotePath = ""
         userName = ""

      class NasVolumeNotMounted(vim.fault.NasConfigFault): # vim.fault.NasVolumeNotMounted
         remoteHost = ""
         remotePath = ""

      class NetworkCopyFault(vim.fault.FileFault): # vim.fault.NetworkCopyFault
         pass

      class NetworkDisruptedAndConfigRolledBack(vim.fault.VimFault): # vim.fault.NetworkDisruptedAndConfigRolledBack
         host = ""

      class NetworkInaccessible(vim.fault.NasConfigFault): # vim.fault.NetworkInaccessible
         pass

      class NetworksMayNotBeTheSame(vim.fault.MigrationFault): # vim.fault.NetworksMayNotBeTheSame
         name = ""

      class NicSettingMismatch(vim.fault.CustomizationFault): # vim.fault.NicSettingMismatch
         numberOfNicsInSpec = 0
         numberOfNicsInVM = 0

      class NoActiveHostInCluster(vim.fault.InvalidState): # vim.fault.NoActiveHostInCluster
         computeResource = vim.ComputeResource()

      class NoClientCertificate(vim.fault.VimFault): # vim.fault.NoClientCertificate
         pass

      class NoCompatibleDatastore(vim.fault.VimFault): # vim.fault.NoCompatibleDatastore
         pass

      class NoCompatibleHardAffinityHost(vim.fault.VmConfigFault): # vim.fault.NoCompatibleHardAffinityHost
         vmName = ""

      class NoCompatibleHost(vim.fault.VimFault): # vim.fault.NoCompatibleHost
         host = [ vim.HostSystem() ]
         error = [ vmodl.MethodFault() ]

      class NoCompatibleHostWithAccessToDevice(vim.fault.NoCompatibleHost): # vim.fault.NoCompatibleHostWithAccessToDevice
         pass

      class NoCompatibleSoftAffinityHost(vim.fault.VmConfigFault): # vim.fault.NoCompatibleSoftAffinityHost
         vmName = ""

      class NoConnectedDatastore(vim.fault.VimFault): # vim.fault.NoConnectedDatastore
         pass

      class NoDiskFound(vim.fault.VimFault): # vim.fault.NoDiskFound
         pass

      class NoDiskSpace(vim.fault.FileFault): # vim.fault.NoDiskSpace
         datastore = ""

      class NoDisksToCustomize(vim.fault.CustomizationFault): # vim.fault.NoDisksToCustomize
         pass

      class NoGateway(vim.fault.HostConfigFault): # vim.fault.NoGateway
         pass

      class NoGuestHeartbeat(vim.fault.MigrationFault): # vim.fault.NoGuestHeartbeat
         pass

      class NoHost(vim.fault.HostConnectFault): # vim.fault.NoHost
         name = ""

      class NoHostSuitableForFtSecondary(vim.fault.VmFaultToleranceIssue): # vim.fault.NoHostSuitableForFtSecondary
         vm = vim.VirtualMachine()
         vmName = ""

      class NoPeerHostFound(vim.fault.HostPowerOpFailed): # vim.fault.NoPeerHostFound
         pass

      class NoPermissionOnAD(vim.fault.ActiveDirectoryFault): # vim.fault.NoPermissionOnAD
         pass

      class NoPermissionOnHost(vim.fault.HostConnectFault): # vim.fault.NoPermissionOnHost
         pass

      class NoPermissionOnNasVolume(vim.fault.NasConfigFault): # vim.fault.NoPermissionOnNasVolume
         userName = ""

      class NoSubjectName(vim.fault.VimFault): # vim.fault.NoSubjectName
         pass

      class NoVirtualNic(vim.fault.HostConfigFault): # vim.fault.NoVirtualNic
         pass

      class NonADUserRequired(vim.fault.ActiveDirectoryFault): # vim.fault.NonADUserRequired
         pass

      class NonHomeRDMVMotionNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.NonHomeRDMVMotionNotSupported
         device = ""

      class NotADirectory(vim.fault.FileFault): # vim.fault.NotADirectory
         pass

      class NotAFile(vim.fault.FileFault): # vim.fault.NotAFile
         pass

      class NotFound(vim.fault.VimFault): # vim.fault.NotFound
         pass

      class NotSupportedDeviceForFT(vim.fault.VmFaultToleranceIssue): # vim.fault.NotSupportedDeviceForFT
         host = vim.HostSystem()
         hostName = ""
         vm = vim.VirtualMachine()
         vmName = ""
         deviceType = ""
         deviceLabel = ""

         class DeviceType(Enum): # vim.fault.NotSupportedDeviceForFT.DeviceType
            virtualVmxnet3 = 0
            paraVirtualSCSIController = 1

      class NotSupportedHost(vim.fault.HostConnectFault): # vim.fault.NotSupportedHost
         productName = ""
         productVersion = ""

      class NotSupportedHostForChecksum(vim.fault.VimFault): # vim.fault.NotSupportedHostForChecksum
         pass

      class NotSupportedHostForVFlash(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostForVFlash
         hostName = ""

      class NotSupportedHostForVmcp(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostForVmcp
         hostName = ""

      class NotSupportedHostForVmemFile(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostForVmemFile
         hostName = ""

      class NotSupportedHostForVsan(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostForVsan
         hostName = ""

      class NotSupportedHostInCluster(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostInCluster
         pass

      class NotSupportedHostInDvs(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostInDvs
         switchProductSpec = vim.dvs.ProductSpec()

      class NotSupportedHostInHACluster(vim.fault.NotSupportedHost): # vim.fault.NotSupportedHostInHACluster
         hostName = ""
         build = ""

      class NumVirtualCpusExceedsLimit(vim.fault.InsufficientResourcesFault): # vim.fault.NumVirtualCpusExceedsLimit
         maxSupportedVcpus = 0

      class NumVirtualCpusIncompatible(vim.fault.VmConfigFault): # vim.fault.NumVirtualCpusIncompatible
         reason = ""
         numCpu = 0

         class Reason(Enum): # vim.fault.NumVirtualCpusIncompatible.Reason
            recordReplay = 0
            faultTolerance = 1

      class OperationDisabledByGuest(vim.fault.GuestOperationsFault): # vim.fault.OperationDisabledByGuest
         pass

      class OperationNotSupportedByGuest(vim.fault.GuestOperationsFault): # vim.fault.OperationNotSupportedByGuest
         pass

      class OutOfBounds(vim.fault.VimFault): # vim.fault.OutOfBounds
         argumentName = vmodl.PropertyPath()

      class OvfConsumerPowerOnFault(vim.fault.InvalidState): # vim.fault.OvfConsumerPowerOnFault
         extensionKey = ""
         extensionName = ""
         description = ""

      class OvfConsumerValidationFault(vim.fault.VmConfigFault): # vim.fault.OvfConsumerValidationFault
         extensionKey = ""
         extensionName = ""
         message = ""

      class OvfFault(vim.fault.VimFault): # vim.fault.OvfFault
         pass

      class OvfImport(vim.fault.OvfFault): # vim.fault.OvfImport
         pass

      class OvfImportFailed(vim.fault.OvfImport): # vim.fault.OvfImportFailed
         pass

      class OvfInvalidPackage(vim.fault.OvfFault): # vim.fault.OvfInvalidPackage
         lineNumber = 0

      class OvfMappedOsId(vim.fault.OvfImport): # vim.fault.OvfMappedOsId
         ovfId = 0
         ovfDescription = ""
         targetDescription = ""

      class OvfMissingHardware(vim.fault.OvfImport): # vim.fault.OvfMissingHardware
         name = ""
         resourceType = 0

      class OvfNetworkMappingNotSupported(vim.fault.OvfImport): # vim.fault.OvfNetworkMappingNotSupported
         pass

      class OvfProperty(vim.fault.OvfInvalidPackage): # vim.fault.OvfProperty
         type = ""
         value = ""

      class OvfPropertyNetwork(vim.fault.OvfProperty): # vim.fault.OvfPropertyNetwork
         pass

      class OvfPropertyQualifier(vim.fault.OvfProperty): # vim.fault.OvfPropertyQualifier
         qualifier = ""

      class OvfPropertyQualifierDuplicate(vim.fault.OvfProperty): # vim.fault.OvfPropertyQualifierDuplicate
         qualifier = ""

      class OvfPropertyQualifierIgnored(vim.fault.OvfProperty): # vim.fault.OvfPropertyQualifierIgnored
         qualifier = ""

      class OvfPropertyType(vim.fault.OvfProperty): # vim.fault.OvfPropertyType
         pass

      class OvfPropertyValue(vim.fault.OvfProperty): # vim.fault.OvfPropertyValue
         pass

      class OvfSystemFault(vim.fault.OvfFault): # vim.fault.OvfSystemFault
         pass

      class OvfToXmlUnsupportedElement(vim.fault.OvfSystemFault): # vim.fault.OvfToXmlUnsupportedElement
         name = ""

      class OvfUnknownDevice(vim.fault.OvfSystemFault): # vim.fault.OvfUnknownDevice
         device = vim.vm.device.VirtualDevice()
         vmName = ""

      class OvfUnknownEntity(vim.fault.OvfSystemFault): # vim.fault.OvfUnknownEntity
         lineNumber = 0

      class OvfUnsupportedDeviceBackingInfo(vim.fault.OvfSystemFault): # vim.fault.OvfUnsupportedDeviceBackingInfo
         elementName = ""
         instanceId = ""
         deviceName = ""
         backingName = ""

      class OvfUnsupportedDeviceBackingOption(vim.fault.OvfSystemFault): # vim.fault.OvfUnsupportedDeviceBackingOption
         elementName = ""
         instanceId = ""
         deviceName = ""
         backingName = ""

      class OvfUnsupportedDiskProvisioning(vim.fault.OvfImport): # vim.fault.OvfUnsupportedDiskProvisioning
         diskProvisioning = ""
         supportedDiskProvisioning = ""

      class OvfUnsupportedPackage(vim.fault.OvfFault): # vim.fault.OvfUnsupportedPackage
         lineNumber = 0

      class OvfUnsupportedSubType(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfUnsupportedSubType
         elementName = ""
         instanceId = ""
         deviceType = 0
         deviceSubType = ""

      class OvfUnsupportedType(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfUnsupportedType
         name = ""
         instanceId = ""
         deviceType = 0

      class OvfWrongNamespace(vim.fault.OvfInvalidPackage): # vim.fault.OvfWrongNamespace
         namespaceName = ""

      class OvfXmlFormat(vim.fault.OvfInvalidPackage): # vim.fault.OvfXmlFormat
         description = ""

      class PasswordExpired(vim.fault.InvalidLogin): # vim.fault.PasswordExpired
         pass

      class PatchBinariesNotFound(vim.fault.VimFault): # vim.fault.PatchBinariesNotFound
         patchID = ""
         binary = [ "" ]

      class PatchMetadataInvalid(vim.fault.VimFault): # vim.fault.PatchMetadataInvalid
         patchID = ""
         metaData = [ "" ]

      class PatchMetadataNotFound(vim.fault.PatchMetadataInvalid): # vim.fault.PatchMetadataNotFound
         pass

      class PatchNotApplicable(vim.fault.VimFault): # vim.fault.PatchNotApplicable
         patchID = ""

      class PatchSuperseded(vim.fault.PatchNotApplicable): # vim.fault.PatchSuperseded
         supersede = [ "" ]

      class PlatformConfigFault(vim.fault.HostConfigFault): # vim.fault.PlatformConfigFault
         text = ""

      class PowerOnFtSecondaryFailed(vim.fault.VmFaultToleranceIssue): # vim.fault.PowerOnFtSecondaryFailed
         vm = vim.VirtualMachine()
         vmName = ""
         hostSelectionBy = vim.fault.FtIssuesOnHost.HostSelectionType()
         hostErrors = [ vmodl.MethodFault() ]
         rootCause = vmodl.MethodFault()

      class ProfileUpdateFailed(vim.fault.VimFault): # vim.fault.ProfileUpdateFailed
         failure = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]
         warnings = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]

         class UpdateFailure(vmodl.DynamicData): # vim.fault.ProfileUpdateFailed.UpdateFailure
            profilePath = vim.profile.ProfilePropertyPath()
            errMsg = vmodl.LocalizableMessage()

      class QuarantineModeFault(vim.fault.VmConfigFault): # vim.fault.QuarantineModeFault
         vmName = ""
         faultType = ""

         class FaultType(Enum): # vim.fault.QuarantineModeFault.FaultType
            NoCompatibleNonQuarantinedHost = 0
            CorrectionDisallowed = 1
            CorrectionImpact = 2

      class QuestionPending(vim.fault.InvalidState): # vim.fault.QuestionPending
         text = ""

      class RDMConversionNotSupported(vim.fault.MigrationFault): # vim.fault.RDMConversionNotSupported
         device = ""

      class RDMNotPreserved(vim.fault.MigrationFault): # vim.fault.RDMNotPreserved
         device = ""

      class RDMNotSupportedOnDatastore(vim.fault.VmConfigFault): # vim.fault.RDMNotSupportedOnDatastore
         device = ""
         datastore = vim.Datastore()
         datastoreName = ""

      class RDMPointsToInaccessibleDisk(vim.fault.CannotAccessVmDisk): # vim.fault.RDMPointsToInaccessibleDisk
         pass

      class ReadHostResourcePoolTreeFailed(vim.fault.HostConnectFault): # vim.fault.ReadHostResourcePoolTreeFailed
         pass

      class ReadOnlyDisksWithLegacyDestination(vim.fault.MigrationFault): # vim.fault.ReadOnlyDisksWithLegacyDestination
         roDiskCount = 0
         timeoutDanger = False

      class RebootRequired(vim.fault.VimFault): # vim.fault.RebootRequired
         patch = ""

      class RecordReplayDisabled(vim.fault.VimFault): # vim.fault.RecordReplayDisabled
         pass

      class RemoveFailed(vim.fault.VimFault): # vim.fault.RemoveFailed
         pass

      class ReplicationFault(vim.fault.VimFault): # vim.fault.ReplicationFault
         pass

      class ReplicationIncompatibleWithFT(vim.fault.ReplicationFault): # vim.fault.ReplicationIncompatibleWithFT
         pass

      class ReplicationInvalidOptions(vim.fault.ReplicationFault): # vim.fault.ReplicationInvalidOptions
         options = ""
         entity = vim.ManagedEntity()

      class ReplicationNotSupportedOnHost(vim.fault.ReplicationFault): # vim.fault.ReplicationNotSupportedOnHost
         pass

      class ReplicationVmFault(vim.fault.ReplicationFault): # vim.fault.ReplicationVmFault
         reason = ""
         state = ""
         instanceId = ""
         vm = vim.VirtualMachine()

         class ReasonForFault(Enum): # vim.fault.ReplicationVmFault.ReasonForFault
            notConfigured = 0
            poweredOff = 1
            suspended = 2
            poweredOn = 3
            offlineReplicating = 4
            invalidState = 5
            invalidInstanceId = 6
            closeDiskError = 7
            groupExist = 8

      class ReplicationVmInProgressFault(vim.fault.ReplicationVmFault): # vim.fault.ReplicationVmInProgressFault
         requestedActivity = ""
         inProgressActivity = ""

         class Activity(Enum): # vim.fault.ReplicationVmInProgressFault.Activity
            fullSync = 0
            delta = 1

      class ResourceInUse(vim.fault.VimFault): # vim.fault.ResourceInUse
         type = vmodl.TypeName()
         name = ""

      class ResourceNotAvailable(vim.fault.VimFault): # vim.fault.ResourceNotAvailable
         containerType = vmodl.TypeName()
         containerName = ""
         type = vmodl.TypeName()

      class RollbackFailure(vim.fault.DvsFault): # vim.fault.RollbackFailure
         entityName = ""
         entityType = ""

      class RuleViolation(vim.fault.VmConfigFault): # vim.fault.RuleViolation
         host = vim.HostSystem()
         rule = vim.cluster.RuleInfo()

      class SSLDisabledFault(vim.fault.HostConnectFault): # vim.fault.SSLDisabledFault
         pass

      class SSLVerifyFault(vim.fault.HostConnectFault): # vim.fault.SSLVerifyFault
         selfSigned = False
         thumbprint = ""

      class SSPIChallenge(vim.fault.VimFault): # vim.fault.SSPIChallenge
         base64Token = ""

      class SecondaryVmAlreadyDisabled(vim.fault.VmFaultToleranceIssue): # vim.fault.SecondaryVmAlreadyDisabled
         instanceUuid = ""

      class SecondaryVmAlreadyEnabled(vim.fault.VmFaultToleranceIssue): # vim.fault.SecondaryVmAlreadyEnabled
         instanceUuid = ""

      class SecondaryVmAlreadyRegistered(vim.fault.VmFaultToleranceIssue): # vim.fault.SecondaryVmAlreadyRegistered
         instanceUuid = ""

      class SecondaryVmNotRegistered(vim.fault.VmFaultToleranceIssue): # vim.fault.SecondaryVmNotRegistered
         instanceUuid = ""

      class ShrinkDiskFault(vim.fault.VimFault): # vim.fault.ShrinkDiskFault
         diskId = 0

      class SnapshotCopyNotSupported(vim.fault.MigrationFault): # vim.fault.SnapshotCopyNotSupported
         pass

      class SnapshotFault(vim.fault.VimFault): # vim.fault.SnapshotFault
         pass

      class SnapshotIncompatibleDeviceInVm(vim.fault.SnapshotFault): # vim.fault.SnapshotIncompatibleDeviceInVm
         fault = vmodl.MethodFault()

      class SnapshotLocked(vim.fault.SnapshotFault): # vim.fault.SnapshotLocked
         pass

      class SnapshotMoveFromNonHomeNotSupported(vim.fault.SnapshotCopyNotSupported): # vim.fault.SnapshotMoveFromNonHomeNotSupported
         pass

      class SnapshotMoveNotSupported(vim.fault.SnapshotCopyNotSupported): # vim.fault.SnapshotMoveNotSupported
         pass

      class SnapshotMoveToNonHomeNotSupported(vim.fault.SnapshotCopyNotSupported): # vim.fault.SnapshotMoveToNonHomeNotSupported
         pass

      class SnapshotNoChange(vim.fault.SnapshotFault): # vim.fault.SnapshotNoChange
         pass

      class SnapshotRevertIssue(vim.fault.MigrationFault): # vim.fault.SnapshotRevertIssue
         snapshotName = ""
         event = [ vim.event.Event() ]
         errors = False

      class SoftRuleVioCorrectionDisallowed(vim.fault.VmConfigFault): # vim.fault.SoftRuleVioCorrectionDisallowed
         vmName = ""

      class SoftRuleVioCorrectionImpact(vim.fault.VmConfigFault): # vim.fault.SoftRuleVioCorrectionImpact
         vmName = ""

      class SsdDiskNotAvailable(vim.fault.VimFault): # vim.fault.SsdDiskNotAvailable
         devicePath = ""

      class StorageDrsCannotMoveDiskInMultiWriterMode(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveDiskInMultiWriterMode
         pass

      class StorageDrsCannotMoveFTVm(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveFTVm
         pass

      class StorageDrsCannotMoveIndependentDisk(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveIndependentDisk
         pass

      class StorageDrsCannotMoveManuallyPlacedSwapFile(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveManuallyPlacedSwapFile
         pass

      class StorageDrsCannotMoveManuallyPlacedVm(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveManuallyPlacedVm
         pass

      class StorageDrsCannotMoveSharedDisk(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveSharedDisk
         pass

      class StorageDrsCannotMoveTemplate(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveTemplate
         pass

      class StorageDrsCannotMoveVmInUserFolder(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveVmInUserFolder
         pass

      class StorageDrsCannotMoveVmWithMountedCDROM(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveVmWithMountedCDROM
         pass

      class StorageDrsCannotMoveVmWithNoFilesInLayout(vim.fault.VimFault): # vim.fault.StorageDrsCannotMoveVmWithNoFilesInLayout
         pass

      class StorageDrsDatacentersCannotShareDatastore(vim.fault.VimFault): # vim.fault.StorageDrsDatacentersCannotShareDatastore
         pass

      class StorageDrsDisabledOnVm(vim.fault.VimFault): # vim.fault.StorageDrsDisabledOnVm
         pass

      class StorageDrsHbrDiskNotMovable(vim.fault.VimFault): # vim.fault.StorageDrsHbrDiskNotMovable
         nonMovableDiskIds = ""

      class StorageDrsHmsMoveInProgress(vim.fault.VimFault): # vim.fault.StorageDrsHmsMoveInProgress
         pass

      class StorageDrsHmsUnreachable(vim.fault.VimFault): # vim.fault.StorageDrsHmsUnreachable
         pass

      class StorageDrsIolbDisabledInternally(vim.fault.VimFault): # vim.fault.StorageDrsIolbDisabledInternally
         pass

      class StorageDrsRelocateDisabled(vim.fault.VimFault): # vim.fault.StorageDrsRelocateDisabled
         pass

      class StorageDrsStaleHmsCollection(vim.fault.VimFault): # vim.fault.StorageDrsStaleHmsCollection
         pass

      class StorageDrsUnableToMoveFiles(vim.fault.VimFault): # vim.fault.StorageDrsUnableToMoveFiles
         pass

      class StorageVMotionNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.StorageVMotionNotSupported
         pass

      class SuspendedRelocateNotSupported(vim.fault.MigrationFault): # vim.fault.SuspendedRelocateNotSupported
         pass

      class SwapDatastoreUnset(vim.fault.VimFault): # vim.fault.SwapDatastoreUnset
         pass

      class SwapPlacementOverrideNotSupported(vim.fault.InvalidVmConfig): # vim.fault.SwapPlacementOverrideNotSupported
         pass

      class SwitchIpUnset(vim.fault.DvsFault): # vim.fault.SwitchIpUnset
         pass

      class SwitchNotInUpgradeMode(vim.fault.DvsFault): # vim.fault.SwitchNotInUpgradeMode
         pass

      class TaskInProgress(vim.fault.VimFault): # vim.fault.TaskInProgress
         task = vim.Task()

      class Timedout(vim.fault.VimFault): # vim.fault.Timedout
         pass

      class TooManyConcurrentNativeClones(vim.fault.FileFault): # vim.fault.TooManyConcurrentNativeClones
         pass

      class TooManyConsecutiveOverrides(vim.fault.VimFault): # vim.fault.TooManyConsecutiveOverrides
         pass

      class TooManyDevices(vim.fault.InvalidVmConfig): # vim.fault.TooManyDevices
         pass

      class TooManyDisksOnLegacyHost(vim.fault.MigrationFault): # vim.fault.TooManyDisksOnLegacyHost
         diskCount = 0
         timeoutDanger = False

      class TooManyGuestLogons(vim.fault.GuestOperationsFault): # vim.fault.TooManyGuestLogons
         pass

      class TooManyHosts(vim.fault.HostConnectFault): # vim.fault.TooManyHosts
         pass

      class TooManyNativeCloneLevels(vim.fault.FileFault): # vim.fault.TooManyNativeCloneLevels
         pass

      class TooManyNativeClonesOnFile(vim.fault.FileFault): # vim.fault.TooManyNativeClonesOnFile
         pass

      class TooManySnapshotLevels(vim.fault.SnapshotFault): # vim.fault.TooManySnapshotLevels
         pass

      class ToolsAlreadyUpgraded(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsAlreadyUpgraded
         pass

      class ToolsAutoUpgradeNotSupported(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsAutoUpgradeNotSupported
         pass

      class ToolsImageCopyFailed(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsImageCopyFailed
         pass

      class ToolsImageNotAvailable(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsImageNotAvailable
         pass

      class ToolsImageSignatureCheckFailed(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsImageSignatureCheckFailed
         pass

      class ToolsInstallationInProgress(vim.fault.MigrationFault): # vim.fault.ToolsInstallationInProgress
         pass

      class ToolsUnavailable(vim.fault.VimFault): # vim.fault.ToolsUnavailable
         pass

      class ToolsUpgradeCancelled(vim.fault.VmToolsUpgradeFault): # vim.fault.ToolsUpgradeCancelled
         pass

      class UncommittedUndoableDisk(vim.fault.MigrationFault): # vim.fault.UncommittedUndoableDisk
         pass

      class UncustomizableGuest(vim.fault.CustomizationFault): # vim.fault.UncustomizableGuest
         uncustomizableGuestOS = ""

      class UnexpectedCustomizationFault(vim.fault.CustomizationFault): # vim.fault.UnexpectedCustomizationFault
         pass

      class UnrecognizedHost(vim.fault.VimFault): # vim.fault.UnrecognizedHost
         hostName = ""

      class UnsharedSwapVMotionNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.UnsharedSwapVMotionNotSupported
         pass

      class UnsupportedDatastore(vim.fault.VmConfigFault): # vim.fault.UnsupportedDatastore
         datastore = vim.Datastore()

      class UnsupportedGuest(vim.fault.InvalidVmConfig): # vim.fault.UnsupportedGuest
         unsupportedGuestOS = ""

      class UnsupportedVimApiVersion(vim.fault.VimFault): # vim.fault.UnsupportedVimApiVersion
         version = ""

      class UnsupportedVmxLocation(vim.fault.VmConfigFault): # vim.fault.UnsupportedVmxLocation
         pass

      class UserNotFound(vim.fault.VimFault): # vim.fault.UserNotFound
         principal = ""
         unresolved = False

      class VAppConfigFault(vim.fault.VimFault): # vim.fault.VAppConfigFault
         pass

      class VAppNotRunning(vim.fault.VmConfigFault): # vim.fault.VAppNotRunning
         pass

      class VAppPropertyFault(vim.fault.VmConfigFault): # vim.fault.VAppPropertyFault
         id = ""
         category = ""
         label = ""
         type = ""
         value = ""

      class VAppTaskInProgress(vim.fault.TaskInProgress): # vim.fault.VAppTaskInProgress
         pass

      class VFlashCacheHotConfigNotSupported(vim.fault.VmConfigFault): # vim.fault.VFlashCacheHotConfigNotSupported
         pass

      class VFlashModuleNotSupported(vim.fault.VmConfigFault): # vim.fault.VFlashModuleNotSupported
         vmName = ""
         moduleName = ""
         reason = ""
         hostName = ""

         class Reason(Enum): # vim.fault.VFlashModuleNotSupported.Reason
            CacheModeNotSupported = 0
            CacheConsistencyTypeNotSupported = 1
            CacheBlockSizeNotSupported = 2
            CacheReservationNotSupported = 3
            DiskSizeNotSupported = 4

      class VFlashModuleVersionIncompatible(vim.fault.VimFault): # vim.fault.VFlashModuleVersionIncompatible
         moduleName = ""
         vmRequestModuleVersion = ""
         hostMinSupportedVerson = ""
         hostModuleVersion = ""

      class VMotionAcrossNetworkNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.VMotionAcrossNetworkNotSupported
         pass

      class VMotionInterfaceIssue(vim.fault.MigrationFault): # vim.fault.VMotionInterfaceIssue
         atSourceHost = False
         failedHost = ""
         failedHostEntity = vim.HostSystem()

      class VMotionLinkCapacityLow(vim.fault.VMotionInterfaceIssue): # vim.fault.VMotionLinkCapacityLow
         network = ""

      class VMotionLinkDown(vim.fault.VMotionInterfaceIssue): # vim.fault.VMotionLinkDown
         network = ""

      class VMotionNotConfigured(vim.fault.VMotionInterfaceIssue): # vim.fault.VMotionNotConfigured
         pass

      class VMotionNotLicensed(vim.fault.VMotionInterfaceIssue): # vim.fault.VMotionNotLicensed
         pass

      class VMotionNotSupported(vim.fault.VMotionInterfaceIssue): # vim.fault.VMotionNotSupported
         pass

      class VMotionProtocolIncompatible(vim.fault.MigrationFault): # vim.fault.VMotionProtocolIncompatible
         pass

      class VirtualHardwareCompatibilityIssue(vim.fault.VmConfigFault): # vim.fault.VirtualHardwareCompatibilityIssue
         pass

      class VirtualHardwareVersionNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.VirtualHardwareVersionNotSupported
         hostName = ""
         host = vim.HostSystem()

      class VmAlreadyExistsInDatacenter(vim.fault.InvalidFolder): # vim.fault.VmAlreadyExistsInDatacenter
         host = vim.HostSystem()
         hostname = ""
         vm = [ vim.VirtualMachine() ]

      class VmFaultToleranceConfigIssue(vim.fault.VmFaultToleranceIssue): # vim.fault.VmFaultToleranceConfigIssue
         reason = ""
         entityName = ""
         entity = vim.ManagedEntity()

         class ReasonForIssue(Enum): # vim.fault.VmFaultToleranceConfigIssue.ReasonForIssue
            haNotEnabled = 0
            moreThanOneSecondary = 1
            recordReplayNotSupported = 2
            replayNotSupported = 3
            templateVm = 4
            multipleVCPU = 5
            hostInactive = 6
            ftUnsupportedHardware = 7
            ftUnsupportedProduct = 8
            missingVMotionNic = 9
            missingFTLoggingNic = 10
            thinDisk = 11
            verifySSLCertificateFlagNotSet = 12
            hasSnapshots = 13
            noConfig = 14
            ftSecondaryVm = 15
            hasLocalDisk = 16
            esxAgentVm = 17
            video3dEnabled = 18
            hasUnsupportedDisk = 19
            insufficientBandwidth = 20
            hasNestedHVConfiguration = 21
            hasVFlashConfiguration = 22
            unsupportedProduct = 23
            cpuHvUnsupported = 24
            cpuHwmmuUnsupported = 25
            cpuHvDisabled = 26
            hasEFIFirmware = 27
            tooManyVCPUs = 28
            tooMuchMemory = 29
            vMotionNotLicensed = 30
            ftNotLicensed = 31
            haAgentIssue = 32
            unsupportedSPBM = 33

      class VmFaultToleranceConfigIssueWrapper(vim.fault.VmFaultToleranceIssue): # vim.fault.VmFaultToleranceConfigIssueWrapper
         entityName = ""
         entity = vim.ManagedEntity()
         error = vmodl.MethodFault()

      class VmFaultToleranceInvalidFileBacking(vim.fault.VmFaultToleranceIssue): # vim.fault.VmFaultToleranceInvalidFileBacking
         backingType = ""
         backingFilename = ""

         class DeviceType(Enum): # vim.fault.VmFaultToleranceInvalidFileBacking.DeviceType
            virtualFloppy = 0
            virtualCdrom = 1
            virtualSerialPort = 2
            virtualParallelPort = 3
            virtualDisk = 4

      class VmFaultToleranceTooManyFtVcpusOnHost(vim.fault.InsufficientResourcesFault): # vim.fault.VmFaultToleranceTooManyFtVcpusOnHost
         hostName = ""
         maxNumFtVcpus = 0

      class VmFaultToleranceTooManyVMsOnHost(vim.fault.InsufficientResourcesFault): # vim.fault.VmFaultToleranceTooManyVMsOnHost
         hostName = ""
         maxNumFtVms = 0

      class VmPowerOnDisabled(vim.fault.InvalidState): # vim.fault.VmPowerOnDisabled
         pass

      class VmSmpFaultToleranceTooManyVMsOnHost(vim.fault.InsufficientResourcesFault): # vim.fault.VmSmpFaultToleranceTooManyVMsOnHost
         hostName = ""
         maxNumSmpFtVms = 0

      class VmWwnConflict(vim.fault.InvalidVmConfig): # vim.fault.VmWwnConflict
         vm = vim.VirtualMachine()
         host = vim.HostSystem()
         name = ""
         wwn = 0

      class VmfsMountFault(vim.fault.HostConfigFault): # vim.fault.VmfsMountFault
         uuid = ""

      class VmotionInterfaceNotEnabled(vim.fault.HostPowerOpFailed): # vim.fault.VmotionInterfaceNotEnabled
         pass

      class VolumeEditorError(vim.fault.CustomizationFault): # vim.fault.VolumeEditorError
         pass

      class VsanClusterUuidMismatch(vim.fault.CannotMoveVsanEnabledHost): # vim.fault.VsanClusterUuidMismatch
         hostClusterUuid = ""
         destinationClusterUuid = ""

      class VsanDiskFault(vim.fault.VsanFault): # vim.fault.VsanDiskFault
         device = ""

      class VsanIncompatibleDiskMapping(vim.fault.VsanDiskFault): # vim.fault.VsanIncompatibleDiskMapping
         pass

      class VspanDestPortConflict(vim.fault.DvsFault): # vim.fault.VspanDestPortConflict
         vspanSessionKey1 = ""
         vspanSessionKey2 = ""
         portKey = ""

      class VspanPortConflict(vim.fault.DvsFault): # vim.fault.VspanPortConflict
         vspanSessionKey1 = ""
         vspanSessionKey2 = ""
         portKey = ""

      class VspanPortMoveFault(vim.fault.DvsFault): # vim.fault.VspanPortMoveFault
         srcPortgroupName = ""
         destPortgroupName = ""
         portKey = ""

      class VspanPortPromiscChangeFault(vim.fault.DvsFault): # vim.fault.VspanPortPromiscChangeFault
         portKey = ""

      class VspanPortgroupPromiscChangeFault(vim.fault.DvsFault): # vim.fault.VspanPortgroupPromiscChangeFault
         portgroupName = ""

      class VspanPortgroupTypeChangeFault(vim.fault.DvsFault): # vim.fault.VspanPortgroupTypeChangeFault
         portgroupName = ""

      class VspanPromiscuousPortNotSupported(vim.fault.DvsFault): # vim.fault.VspanPromiscuousPortNotSupported
         vspanSessionKey = ""
         portKey = ""

      class VspanSameSessionPortConflict(vim.fault.DvsFault): # vim.fault.VspanSameSessionPortConflict
         vspanSessionKey = ""
         portKey = ""

      class WakeOnLanNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.WakeOnLanNotSupported
         pass

      class WakeOnLanNotSupportedByVmotionNIC(vim.fault.HostPowerOpFailed): # vim.fault.WakeOnLanNotSupportedByVmotionNIC
         pass

      class WillLoseHAProtection(vim.fault.MigrationFault): # vim.fault.WillLoseHAProtection
         resolution = ""

         class Resolution(Enum): # vim.fault.WillLoseHAProtection.Resolution
            svmotion = 0
            relocate = 1

      class WillModifyConfigCpuRequirements(vim.fault.MigrationFault): # vim.fault.WillModifyConfigCpuRequirements
         pass

      class WillResetSnapshotDirectory(vim.fault.MigrationFault): # vim.fault.WillResetSnapshotDirectory
         pass

      class ActiveVMsBlockingEVC(vim.fault.EVCConfigFault): # vim.fault.ActiveVMsBlockingEVC
         evcMode = ""
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class AdminDisabled(vim.fault.HostConfigFault): # vim.fault.AdminDisabled
         pass

      class AdminNotDisabled(vim.fault.HostConfigFault): # vim.fault.AdminNotDisabled
         pass

      class AffinityConfigured(vim.fault.MigrationFault): # vim.fault.AffinityConfigured
         configuredAffinity = [ "" ]

         class Affinity(Enum): # vim.fault.AffinityConfigured.Affinity
            memory = 0
            cpu = 1

      class AgentInstallFailed(vim.fault.HostConnectFault): # vim.fault.AgentInstallFailed
         reason = ""
         statusCode = 0
         installerOutput = ""

         class Reason(Enum): # vim.fault.AgentInstallFailed.Reason
            NotEnoughSpaceOnDevice = 0
            PrepareToUpgradeFailed = 1
            AgentNotRunning = 2
            AgentNotReachable = 3
            InstallTimedout = 4
            SignatureVerificationFailed = 5
            AgentUploadFailed = 6
            AgentUploadTimedout = 7
            UnknownInstallerError = 8

      class AlreadyBeingManaged(vim.fault.HostConnectFault): # vim.fault.AlreadyBeingManaged
         ipAddress = ""

      class AlreadyConnected(vim.fault.HostConnectFault): # vim.fault.AlreadyConnected
         name = ""

      class ApplicationQuiesceFault(vim.fault.SnapshotFault): # vim.fault.ApplicationQuiesceFault
         pass

      class BackupBlobReadFailure(vim.fault.DvsFault): # vim.fault.BackupBlobReadFailure
         entityName = ""
         entityType = ""
         fault = vmodl.MethodFault()

      class BackupBlobWriteFailure(vim.fault.DvsFault): # vim.fault.BackupBlobWriteFailure
         entityName = ""
         entityType = ""
         fault = vmodl.MethodFault()

      class BlockedByFirewall(vim.fault.HostConfigFault): # vim.fault.BlockedByFirewall
         pass

      class CAMServerRefusedConnection(vim.fault.InvalidCAMServer): # vim.fault.CAMServerRefusedConnection
         pass

      class CannotAccessFile(vim.fault.FileFault): # vim.fault.CannotAccessFile
         pass

      class CannotAccessNetwork(vim.fault.CannotAccessVmDevice): # vim.fault.CannotAccessNetwork
         network = vim.Network()

      class CannotAddHostWithFTVmAsStandalone(vim.fault.HostConnectFault): # vim.fault.CannotAddHostWithFTVmAsStandalone
         pass

      class CannotAddHostWithFTVmToDifferentCluster(vim.fault.HostConnectFault): # vim.fault.CannotAddHostWithFTVmToDifferentCluster
         pass

      class CannotAddHostWithFTVmToNonHACluster(vim.fault.HostConnectFault): # vim.fault.CannotAddHostWithFTVmToNonHACluster
         pass

      class CannotCreateFile(vim.fault.FileFault): # vim.fault.CannotCreateFile
         pass

      class CannotDecryptPasswords(vim.fault.CustomizationFault): # vim.fault.CannotDecryptPasswords
         pass

      class CannotDeleteFile(vim.fault.FileFault): # vim.fault.CannotDeleteFile
         pass

      class CannotModifyConfigCpuRequirements(vim.fault.MigrationFault): # vim.fault.CannotModifyConfigCpuRequirements
         pass

      class CannotMoveVmWithDeltaDisk(vim.fault.MigrationFault): # vim.fault.CannotMoveVmWithDeltaDisk
         device = ""

      class CannotMoveVmWithNativeDeltaDisk(vim.fault.MigrationFault): # vim.fault.CannotMoveVmWithNativeDeltaDisk
         pass

      class CannotPowerOffVmInCluster(vim.fault.InvalidState): # vim.fault.CannotPowerOffVmInCluster
         operation = ""
         vm = vim.VirtualMachine()
         vmName = ""

         class Operation(Enum): # vim.fault.CannotPowerOffVmInCluster.Operation
            suspend = 0
            powerOff = 1
            guestShutdown = 2
            guestSuspend = 3

      class ClockSkew(vim.fault.HostConfigFault): # vim.fault.ClockSkew
         pass

      class CloneFromSnapshotNotSupported(vim.fault.MigrationFault): # vim.fault.CloneFromSnapshotNotSupported
         pass

      class CollectorAddressUnset(vim.fault.DvsFault): # vim.fault.CollectorAddressUnset
         pass

      class ConflictingConfiguration(vim.fault.DvsFault): # vim.fault.ConflictingConfiguration
         configInConflict = [ vim.fault.ConflictingConfiguration.Config() ]

         class Config(vmodl.DynamicData): # vim.fault.ConflictingConfiguration.Config
            entity = vim.ManagedEntity()
            propertyPath = ""

      class CpuIncompatible(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.CpuIncompatible
         level = 0
         registerName = ""
         registerBits = ""
         desiredBits = ""
         host = vim.HostSystem()

      class CpuIncompatible1ECX(vim.fault.CpuIncompatible): # vim.fault.CpuIncompatible1ECX
         sse3 = False
         pclmulqdq = False
         ssse3 = False
         sse41 = False
         sse42 = False
         aes = False
         other = False
         otherOnly = False

      class CpuIncompatible81EDX(vim.fault.CpuIncompatible): # vim.fault.CpuIncompatible81EDX
         nx = False
         ffxsr = False
         rdtscp = False
         lm = False
         other = False
         otherOnly = False

      class DatacenterMismatch(vim.fault.MigrationFault): # vim.fault.DatacenterMismatch
         invalidArgument = [ vim.fault.DatacenterMismatch.Argument() ]
         expectedDatacenter = vim.Datacenter()

         class Argument(vmodl.DynamicData): # vim.fault.DatacenterMismatch.Argument
            entity = vim.ManagedEntity()
            inputDatacenter = vim.Datacenter()

      class DatastoreNotWritableOnHost(vim.fault.InvalidDatastore): # vim.fault.DatastoreNotWritableOnHost
         host = vim.HostSystem()

      class DestinationSwitchFull(vim.fault.CannotAccessNetwork): # vim.fault.DestinationSwitchFull
         pass

      class DeviceNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.DeviceNotSupported
         device = ""
         reason = ""

         class Reason(Enum): # vim.fault.DeviceNotSupported.Reason
            host = 0
            guest = 1
            ft = 2

      class DigestNotSupported(vim.fault.DeviceNotSupported): # vim.fault.DigestNotSupported
         pass

      class DirectoryNotEmpty(vim.fault.FileFault): # vim.fault.DirectoryNotEmpty
         pass

      class DisableAdminNotSupported(vim.fault.HostConfigFault): # vim.fault.DisableAdminNotSupported
         pass

      class DisallowedMigrationDeviceAttached(vim.fault.MigrationFault): # vim.fault.DisallowedMigrationDeviceAttached
         fault = vmodl.MethodFault()

      class DisconnectedHostsBlockingEVC(vim.fault.EVCConfigFault): # vim.fault.DisconnectedHostsBlockingEVC
         pass

      class DiskHasPartitions(vim.fault.VsanDiskFault): # vim.fault.DiskHasPartitions
         pass

      class DiskIsLastRemainingNonSSD(vim.fault.VsanDiskFault): # vim.fault.DiskIsLastRemainingNonSSD
         pass

      class DiskIsNonLocal(vim.fault.VsanDiskFault): # vim.fault.DiskIsNonLocal
         pass

      class DiskIsUSB(vim.fault.VsanDiskFault): # vim.fault.DiskIsUSB
         pass

      class DiskMoveTypeNotSupported(vim.fault.MigrationFault): # vim.fault.DiskMoveTypeNotSupported
         pass

      class DiskNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.DiskNotSupported
         disk = 0

      class DiskTooSmall(vim.fault.VsanDiskFault): # vim.fault.DiskTooSmall
         pass

      class DrsVmotionIncompatibleFault(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.DrsVmotionIncompatibleFault
         host = vim.HostSystem()

      class DuplicateDisks(vim.fault.VsanDiskFault): # vim.fault.DuplicateDisks
         pass

      class DvsApplyOperationFault(vim.fault.DvsFault): # vim.fault.DvsApplyOperationFault
         objectFault = [ vim.fault.DvsApplyOperationFault.FaultOnObject() ]

         class FaultOnObject(vmodl.DynamicData): # vim.fault.DvsApplyOperationFault.FaultOnObject
            objectId = ""
            type = vmodl.TypeName()
            fault = vmodl.MethodFault()

      class EVCAdmissionFailed(vim.fault.NotSupportedHostInCluster): # vim.fault.EVCAdmissionFailed
         faults = [ vmodl.MethodFault() ]

      class EVCAdmissionFailedCPUFeaturesForMode(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedCPUFeaturesForMode
         currentEVCModeKey = ""

      class EVCAdmissionFailedCPUModel(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedCPUModel
         pass

      class EVCAdmissionFailedCPUModelForMode(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedCPUModelForMode
         currentEVCModeKey = ""

      class EVCAdmissionFailedCPUVendor(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedCPUVendor
         clusterCPUVendor = ""
         hostCPUVendor = ""

      class EVCAdmissionFailedCPUVendorUnknown(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedCPUVendorUnknown
         pass

      class EVCAdmissionFailedHostDisconnected(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedHostDisconnected
         pass

      class EVCAdmissionFailedHostSoftware(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedHostSoftware
         pass

      class EVCAdmissionFailedHostSoftwareForMode(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedHostSoftwareForMode
         pass

      class EVCAdmissionFailedVmActive(vim.fault.EVCAdmissionFailed): # vim.fault.EVCAdmissionFailedVmActive
         pass

      class EncryptionKeyRequired(vim.fault.InvalidState): # vim.fault.EncryptionKeyRequired
         requiredKey = [ vim.encryption.CryptoKeyId() ]

      class FailToEnableSPBM(vmodl.fault.NotEnoughLicenses): # vim.fault.FailToEnableSPBM
         cs = vim.ComputeResource()
         csName = ""
         hostLicenseStates = [ vim.ComputeResource.HostSPBMLicenseInfo() ]

      class FaultToleranceAntiAffinityViolated(vim.fault.MigrationFault): # vim.fault.FaultToleranceAntiAffinityViolated
         hostName = ""
         host = vim.HostSystem()

      class FaultToleranceCpuIncompatible(vim.fault.CpuIncompatible): # vim.fault.FaultToleranceCpuIncompatible
         model = False
         family = False
         stepping = False

      class FaultToleranceNeedsThickDisk(vim.fault.MigrationFault): # vim.fault.FaultToleranceNeedsThickDisk
         vmName = ""

      class FaultToleranceNotSameBuild(vim.fault.MigrationFault): # vim.fault.FaultToleranceNotSameBuild
         build = ""

      class FeatureRequirementsNotMet(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.FeatureRequirementsNotMet
         featureRequirement = [ vim.vm.FeatureRequirement() ]
         vm = vim.VirtualMachine()
         host = vim.HostSystem()

      class FileAlreadyExists(vim.fault.FileFault): # vim.fault.FileAlreadyExists
         pass

      class FileBackedPortNotSupported(vim.fault.DeviceNotSupported): # vim.fault.FileBackedPortNotSupported
         pass

      class FilesystemQuiesceFault(vim.fault.SnapshotFault): # vim.fault.FilesystemQuiesceFault
         pass

      class FilterInUse(vim.fault.ResourceInUse): # vim.fault.FilterInUse
         disk = [ vim.vm.device.VirtualDiskId() ]

      class FullStorageVMotionNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.FullStorageVMotionNotSupported
         pass

      class GatewayConnectFault(vim.fault.HostConnectFault): # vim.fault.GatewayConnectFault
         gatewayType = ""
         gatewayId = ""
         gatewayInfo = ""
         details = vmodl.LocalizableMessage()

      class GatewayNotFound(vim.fault.GatewayConnectFault): # vim.fault.GatewayNotFound
         pass

      class GatewayNotReachable(vim.fault.GatewayConnectFault): # vim.fault.GatewayNotReachable
         pass

      class GatewayOperationRefused(vim.fault.GatewayConnectFault): # vim.fault.GatewayOperationRefused
         pass

      class GatewayToHostConnectFault(vim.fault.GatewayConnectFault): # vim.fault.GatewayToHostConnectFault
         hostname = ""
         port = 0

      class GatewayToHostTrustVerifyFault(vim.fault.GatewayToHostConnectFault): # vim.fault.GatewayToHostTrustVerifyFault
         verificationToken = ""
         propertiesToVerify = [ vim.KeyValue() ]

      class GuestAuthenticationChallenge(vim.fault.GuestOperationsFault): # vim.fault.GuestAuthenticationChallenge
         serverChallenge = vim.vm.guest.GuestAuthentication()
         sessionID = 0

      class GuestComponentsOutOfDate(vim.fault.GuestOperationsFault): # vim.fault.GuestComponentsOutOfDate
         pass

      class GuestMultipleMappings(vim.fault.GuestOperationsFault): # vim.fault.GuestMultipleMappings
         pass

      class GuestRegistryKeyAlreadyExists(vim.fault.GuestRegistryKeyFault): # vim.fault.GuestRegistryKeyAlreadyExists
         pass

      class HAErrorsAtDest(vim.fault.MigrationFault): # vim.fault.HAErrorsAtDest
         pass

      class HostConfigFailed(vim.fault.HostConfigFault): # vim.fault.HostConfigFailed
         failure = [ vmodl.MethodFault() ]

      class HotSnapshotMoveNotSupported(vim.fault.SnapshotCopyNotSupported): # vim.fault.HotSnapshotMoveNotSupported
         pass

      class IDEDiskNotSupported(vim.fault.DiskNotSupported): # vim.fault.IDEDiskNotSupported
         pass

      class InaccessibleDatastore(vim.fault.InvalidDatastore): # vim.fault.InaccessibleDatastore
         detail = ""

      class InaccessibleFTMetadataDatastore(vim.fault.InaccessibleDatastore): # vim.fault.InaccessibleFTMetadataDatastore
         pass

      class IncompatibleDefaultDevice(vim.fault.MigrationFault): # vim.fault.IncompatibleDefaultDevice
         device = ""

      class IncompatibleHostForVmReplication(vim.fault.ReplicationFault): # vim.fault.IncompatibleHostForVmReplication
         vmName = ""
         hostName = ""
         reason = ""

         class IncompatibleReason(Enum): # vim.fault.IncompatibleHostForVmReplication.IncompatibleReason
            rpo = 0
            netCompression = 1

      class IndependentDiskVMotionNotSupported(vim.fault.MigrationFeatureNotSupported): # vim.fault.IndependentDiskVMotionNotSupported
         pass

      class InsufficientAgentVmsDeployed(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientAgentVmsDeployed
         hostName = ""
         requiredNumAgentVms = 0
         currentNumAgentVms = 0

      class InsufficientCpuResourcesFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientCpuResourcesFault
         unreserved = 0
         requested = 0

      class InsufficientDisks(vim.fault.VsanDiskFault): # vim.fault.InsufficientDisks
         pass

      class InsufficientFailoverResourcesFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientFailoverResourcesFault
         pass

      class InsufficientGraphicsResourcesFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientGraphicsResourcesFault
         pass

      class InsufficientHostCapacityFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientHostCapacityFault
         host = vim.HostSystem()

      class InsufficientHostCpuCapacityFault(vim.fault.InsufficientHostCapacityFault): # vim.fault.InsufficientHostCpuCapacityFault
         unreserved = 0
         requested = 0

      class InsufficientHostMemoryCapacityFault(vim.fault.InsufficientHostCapacityFault): # vim.fault.InsufficientHostMemoryCapacityFault
         unreserved = 0
         requested = 0

      class InsufficientMemoryResourcesFault(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientMemoryResourcesFault
         unreserved = 0
         requested = 0

      class InsufficientNetworkCapacity(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientNetworkCapacity
         pass

      class InsufficientNetworkResourcePoolCapacity(vim.fault.InsufficientResourcesFault): # vim.fault.InsufficientNetworkResourcePoolCapacity
         dvsName = ""
         dvsUuid = ""
         resourcePoolKey = ""
         available = 0
         requested = 0
         device = [ "" ]

      class InsufficientPerCpuCapacity(vim.fault.InsufficientHostCapacityFault): # vim.fault.InsufficientPerCpuCapacity
         pass

      class InsufficientStandbyCpuResource(vim.fault.InsufficientStandbyResource): # vim.fault.InsufficientStandbyCpuResource
         available = 0
         requested = 0

      class InsufficientStandbyMemoryResource(vim.fault.InsufficientStandbyResource): # vim.fault.InsufficientStandbyMemoryResource
         available = 0
         requested = 0

      class InvalidBundle(vim.fault.PlatformConfigFault): # vim.fault.InvalidBundle
         pass

      class InvalidCAMCertificate(vim.fault.InvalidCAMServer): # vim.fault.InvalidCAMCertificate
         pass

      class InvalidClientCertificate(vim.fault.InvalidLogin): # vim.fault.InvalidClientCertificate
         pass

      class InvalidDatastoreState(vim.fault.InvalidState): # vim.fault.InvalidDatastoreState
         datastoreName = ""

      class InvalidDeviceSpec(vim.fault.InvalidVmConfig): # vim.fault.InvalidDeviceSpec
         deviceIndex = 0

      class InvalidDiskFormat(vim.fault.InvalidFormat): # vim.fault.InvalidDiskFormat
         pass

      class InvalidHostState(vim.fault.InvalidState): # vim.fault.InvalidHostState
         host = vim.HostSystem()

      class InvalidNasCredentials(vim.fault.NasConfigFault): # vim.fault.InvalidNasCredentials
         userName = ""

      class InvalidNetworkInType(vim.fault.VAppPropertyFault): # vim.fault.InvalidNetworkInType
         pass

      class InvalidNetworkResource(vim.fault.NasConfigFault): # vim.fault.InvalidNetworkResource
         remoteHost = ""
         remotePath = ""

      class InvalidPowerState(vim.fault.InvalidState): # vim.fault.InvalidPowerState
         requestedState = vim.VirtualMachine.PowerState()
         existingState = vim.VirtualMachine.PowerState()

      class InvalidPropertyType(vim.fault.VAppPropertyFault): # vim.fault.InvalidPropertyType
         pass

      class InvalidPropertyValue(vim.fault.VAppPropertyFault): # vim.fault.InvalidPropertyValue
         pass

      class LargeRDMConversionNotSupported(vim.fault.MigrationFault): # vim.fault.LargeRDMConversionNotSupported
         device = ""

      class LegacyNetworkInterfaceInUse(vim.fault.CannotAccessNetwork): # vim.fault.LegacyNetworkInterfaceInUse
         pass

      class MaintenanceModeFileMove(vim.fault.MigrationFault): # vim.fault.MaintenanceModeFileMove
         pass

      class MemoryFileFormatNotSupportedByDatastore(vim.fault.UnsupportedDatastore): # vim.fault.MemoryFileFormatNotSupportedByDatastore
         datastoreName = ""
         type = ""

      class MemorySizeNotRecommended(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.MemorySizeNotRecommended
         memorySizeMB = 0
         minMemorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySizeNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.MemorySizeNotSupported
         memorySizeMB = 0
         minMemorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySizeNotSupportedByDatastore(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.MemorySizeNotSupportedByDatastore
         datastore = vim.Datastore()
         memorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySnapshotOnIndependentDisk(vim.fault.SnapshotFault): # vim.fault.MemorySnapshotOnIndependentDisk
         pass

      class MigrationDisabled(vim.fault.MigrationFault): # vim.fault.MigrationDisabled
         pass

      class MissingController(vim.fault.InvalidDeviceSpec): # vim.fault.MissingController
         pass

      class MissingIpPool(vim.fault.VAppPropertyFault): # vim.fault.MissingIpPool
         pass

      class MissingNetworkIpConfig(vim.fault.VAppPropertyFault): # vim.fault.MissingNetworkIpConfig
         pass

      class MissingPowerOffConfiguration(vim.fault.VAppConfigFault): # vim.fault.MissingPowerOffConfiguration
         pass

      class MissingPowerOnConfiguration(vim.fault.VAppConfigFault): # vim.fault.MissingPowerOnConfiguration
         pass

      class MultiWriterNotSupported(vim.fault.DeviceNotSupported): # vim.fault.MultiWriterNotSupported
         pass

      class MultipleSnapshotsNotSupported(vim.fault.SnapshotFault): # vim.fault.MultipleSnapshotsNotSupported
         pass

      class NoAvailableIp(vim.fault.VAppPropertyFault): # vim.fault.NoAvailableIp
         network = vim.Network()

      class NoVcManagedIpConfigured(vim.fault.VAppPropertyFault): # vim.fault.NoVcManagedIpConfigured
         pass

      class NoVmInVApp(vim.fault.VAppConfigFault): # vim.fault.NoVmInVApp
         pass

      class NonPersistentDisksNotSupported(vim.fault.DeviceNotSupported): # vim.fault.NonPersistentDisksNotSupported
         pass

      class NonVmwareOuiMacNotSupportedHost(vim.fault.NotSupportedHost): # vim.fault.NonVmwareOuiMacNotSupportedHost
         hostName = ""

      class NotEnoughCpus(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.NotEnoughCpus
         numCpuDest = 0
         numCpuVm = 0

      class NotEnoughLogicalCpus(vim.fault.NotEnoughCpus): # vim.fault.NotEnoughLogicalCpus
         host = vim.HostSystem()

      class NotUserConfigurableProperty(vim.fault.VAppPropertyFault): # vim.fault.NotUserConfigurableProperty
         pass

      class NumVirtualCoresPerSocketNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.NumVirtualCoresPerSocketNotSupported
         maxSupportedCoresPerSocketDest = 0
         numCoresPerSocketVm = 0

      class NumVirtualCpusNotSupported(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.NumVirtualCpusNotSupported
         maxSupportedVcpusDest = 0
         numCpuVm = 0

      class OvfAttribute(vim.fault.OvfInvalidPackage): # vim.fault.OvfAttribute
         elementName = ""
         attributeName = ""

      class OvfConstraint(vim.fault.OvfInvalidPackage): # vim.fault.OvfConstraint
         name = ""

      class OvfConsumerCallbackFault(vim.fault.OvfFault): # vim.fault.OvfConsumerCallbackFault
         extensionKey = ""
         extensionName = ""

      class OvfConsumerCommunicationError(vim.fault.OvfConsumerCallbackFault): # vim.fault.OvfConsumerCommunicationError
         description = ""

      class OvfConsumerFault(vim.fault.OvfConsumerCallbackFault): # vim.fault.OvfConsumerFault
         errorKey = ""
         message = ""
         params = [ vim.KeyValue() ]

      class OvfConsumerInvalidSection(vim.fault.OvfConsumerCallbackFault): # vim.fault.OvfConsumerInvalidSection
         lineNumber = 0
         description = ""

      class OvfConsumerUndeclaredSection(vim.fault.OvfConsumerCallbackFault): # vim.fault.OvfConsumerUndeclaredSection
         qualifiedSectionType = ""

      class OvfConsumerUndefinedPrefix(vim.fault.OvfConsumerCallbackFault): # vim.fault.OvfConsumerUndefinedPrefix
         prefix = ""

      class OvfCpuCompatibility(vim.fault.OvfImport): # vim.fault.OvfCpuCompatibility
         registerName = ""
         level = 0
         registerValue = ""
         desiredRegisterValue = ""

      class OvfCpuCompatibilityCheckNotSupported(vim.fault.OvfImport): # vim.fault.OvfCpuCompatibilityCheckNotSupported
         pass

      class OvfDiskMappingNotFound(vim.fault.OvfSystemFault): # vim.fault.OvfDiskMappingNotFound
         diskName = ""
         vmName = ""

      class OvfDiskOrderConstraint(vim.fault.OvfConstraint): # vim.fault.OvfDiskOrderConstraint
         pass

      class OvfElement(vim.fault.OvfInvalidPackage): # vim.fault.OvfElement
         name = ""

      class OvfElementInvalidValue(vim.fault.OvfElement): # vim.fault.OvfElementInvalidValue
         value = ""

      class OvfExport(vim.fault.OvfFault): # vim.fault.OvfExport
         pass

      class OvfExportFailed(vim.fault.OvfExport): # vim.fault.OvfExportFailed
         pass

      class OvfHardwareCheck(vim.fault.OvfImport): # vim.fault.OvfHardwareCheck
         pass

      class OvfHardwareExport(vim.fault.OvfExport): # vim.fault.OvfHardwareExport
         device = vim.vm.device.VirtualDevice()
         vmPath = ""

      class OvfHostResourceConstraint(vim.fault.OvfConstraint): # vim.fault.OvfHostResourceConstraint
         value = ""

      class OvfHostValueNotParsed(vim.fault.OvfSystemFault): # vim.fault.OvfHostValueNotParsed
         property = ""
         value = ""

      class OvfInternalError(vim.fault.OvfSystemFault): # vim.fault.OvfInternalError
         pass

      class OvfInvalidValue(vim.fault.OvfAttribute): # vim.fault.OvfInvalidValue
         value = ""

      class OvfInvalidValueConfiguration(vim.fault.OvfInvalidValue): # vim.fault.OvfInvalidValueConfiguration
         pass

      class OvfInvalidValueEmpty(vim.fault.OvfInvalidValue): # vim.fault.OvfInvalidValueEmpty
         pass

      class OvfInvalidValueFormatMalformed(vim.fault.OvfInvalidValue): # vim.fault.OvfInvalidValueFormatMalformed
         pass

      class OvfInvalidValueReference(vim.fault.OvfInvalidValue): # vim.fault.OvfInvalidValueReference
         pass

      class OvfInvalidVmName(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfInvalidVmName
         name = ""

      class OvfMissingAttribute(vim.fault.OvfAttribute): # vim.fault.OvfMissingAttribute
         pass

      class OvfMissingElement(vim.fault.OvfElement): # vim.fault.OvfMissingElement
         pass

      class OvfMissingElementNormalBoundary(vim.fault.OvfMissingElement): # vim.fault.OvfMissingElementNormalBoundary
         boundary = ""

      class OvfNoHostNic(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfNoHostNic
         pass

      class OvfNoSupportedHardwareFamily(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfNoSupportedHardwareFamily
         version = ""

      class OvfPropertyExport(vim.fault.OvfExport): # vim.fault.OvfPropertyExport
         type = ""
         value = ""

      class OvfPropertyNetworkExport(vim.fault.OvfExport): # vim.fault.OvfPropertyNetworkExport
         network = ""

      class OvfUnableToExportDisk(vim.fault.OvfHardwareExport): # vim.fault.OvfUnableToExportDisk
         diskName = ""

      class OvfUnexpectedElement(vim.fault.OvfElement): # vim.fault.OvfUnexpectedElement
         pass

      class OvfUnknownDeviceBacking(vim.fault.OvfHardwareExport): # vim.fault.OvfUnknownDeviceBacking
         backing = vim.vm.device.VirtualDevice.BackingInfo()

      class OvfUnsupportedAttribute(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfUnsupportedAttribute
         elementName = ""
         attributeName = ""

      class OvfUnsupportedAttributeValue(vim.fault.OvfUnsupportedAttribute): # vim.fault.OvfUnsupportedAttributeValue
         value = ""

      class OvfUnsupportedDeviceExport(vim.fault.OvfHardwareExport): # vim.fault.OvfUnsupportedDeviceExport
         pass

      class OvfUnsupportedElement(vim.fault.OvfUnsupportedPackage): # vim.fault.OvfUnsupportedElement
         name = ""

      class OvfUnsupportedElementValue(vim.fault.OvfUnsupportedElement): # vim.fault.OvfUnsupportedElementValue
         value = ""

      class OvfUnsupportedSection(vim.fault.OvfUnsupportedElement): # vim.fault.OvfUnsupportedSection
         info = ""

      class OvfWrongElement(vim.fault.OvfElement): # vim.fault.OvfWrongElement
         pass

      class PatchAlreadyInstalled(vim.fault.PatchNotApplicable): # vim.fault.PatchAlreadyInstalled
         pass

      class PatchInstallFailed(vim.fault.PlatformConfigFault): # vim.fault.PatchInstallFailed
         rolledBack = False

      class PatchIntegrityError(vim.fault.PlatformConfigFault): # vim.fault.PatchIntegrityError
         pass

      class PatchMetadataCorrupted(vim.fault.PatchMetadataInvalid): # vim.fault.PatchMetadataCorrupted
         pass

      class PatchMissingDependencies(vim.fault.PatchNotApplicable): # vim.fault.PatchMissingDependencies
         prerequisitePatch = [ "" ]
         prerequisiteLib = [ "" ]

      class PowerOnFtSecondaryTimedout(vim.fault.Timedout): # vim.fault.PowerOnFtSecondaryTimedout
         vm = vim.VirtualMachine()
         vmName = ""
         timeout = 0

      class QuiesceDatastoreIOForHAFailed(vim.fault.ResourceInUse): # vim.fault.QuiesceDatastoreIOForHAFailed
         host = vim.HostSystem()
         hostName = ""
         ds = vim.Datastore()
         dsName = ""

      class RDMNotSupported(vim.fault.DeviceNotSupported): # vim.fault.RDMNotSupported
         pass

      class RawDiskNotSupported(vim.fault.DeviceNotSupported): # vim.fault.RawDiskNotSupported
         pass

      class RemoteDeviceNotSupported(vim.fault.DeviceNotSupported): # vim.fault.RemoteDeviceNotSupported
         pass

      class ReplicationConfigFault(vim.fault.ReplicationFault): # vim.fault.ReplicationConfigFault
         pass

      class ReplicationDiskConfigFault(vim.fault.ReplicationConfigFault): # vim.fault.ReplicationDiskConfigFault
         reason = ""
         vmRef = vim.VirtualMachine()
         key = 0

         class ReasonForFault(Enum): # vim.fault.ReplicationDiskConfigFault.ReasonForFault
            diskNotFound = 0
            diskTypeNotSupported = 1
            invalidDiskKey = 2
            invalidDiskReplicationId = 3
            duplicateDiskReplicationId = 4
            invalidPersistentFilePath = 5
            reconfigureDiskReplicationIdNotAllowed = 6

      class ReplicationVmConfigFault(vim.fault.ReplicationConfigFault): # vim.fault.ReplicationVmConfigFault
         reason = ""
         vmRef = vim.VirtualMachine()

         class ReasonForFault(Enum): # vim.fault.ReplicationVmConfigFault.ReasonForFault
            incompatibleHwVersion = 0
            invalidVmReplicationId = 1
            invalidGenerationNumber = 2
            outOfBoundsRpoValue = 3
            invalidDestinationIpAddress = 4
            invalidDestinationPort = 5
            invalidExtraVmOptions = 6
            staleGenerationNumber = 7
            reconfigureVmReplicationIdNotAllowed = 8
            cannotRetrieveVmReplicationConfiguration = 9
            replicationAlreadyEnabled = 10
            invalidPriorConfiguration = 11
            replicationNotEnabled = 12
            replicationConfigurationFailed = 13
            encryptedVm = 14
            invalidThumbprint = 15
            incompatibleDevice = 16

      class SharedBusControllerNotSupported(vim.fault.DeviceNotSupported): # vim.fault.SharedBusControllerNotSupported
         pass

      class SnapshotCloneNotSupported(vim.fault.SnapshotCopyNotSupported): # vim.fault.SnapshotCloneNotSupported
         pass

      class SnapshotDisabled(vim.fault.SnapshotFault): # vim.fault.SnapshotDisabled
         pass

      class StorageVmotionIncompatible(vim.fault.VirtualHardwareCompatibilityIssue): # vim.fault.StorageVmotionIncompatible
         datastore = vim.Datastore()

      class SwapDatastoreNotWritableOnHost(vim.fault.DatastoreNotWritableOnHost): # vim.fault.SwapDatastoreNotWritableOnHost
         pass

      class UnSupportedDatastoreForVFlash(vim.fault.UnsupportedDatastore): # vim.fault.UnSupportedDatastoreForVFlash
         datastoreName = ""
         type = ""

      class UnconfiguredPropertyValue(vim.fault.InvalidPropertyValue): # vim.fault.UnconfiguredPropertyValue
         pass

      class VMINotSupported(vim.fault.DeviceNotSupported): # vim.fault.VMINotSupported
         pass

      class VMOnConflictDVPort(vim.fault.CannotAccessNetwork): # vim.fault.VMOnConflictDVPort
         pass

      class VMOnVirtualIntranet(vim.fault.CannotAccessNetwork): # vim.fault.VMOnVirtualIntranet
         pass

      class VirtualDiskModeNotSupported(vim.fault.DeviceNotSupported): # vim.fault.VirtualDiskModeNotSupported
         mode = ""

      class VirtualEthernetCardNotSupported(vim.fault.DeviceNotSupported): # vim.fault.VirtualEthernetCardNotSupported
         pass

      class VmfsAlreadyMounted(vim.fault.VmfsMountFault): # vim.fault.VmfsAlreadyMounted
         pass

      class VmfsAmbiguousMount(vim.fault.VmfsMountFault): # vim.fault.VmfsAmbiguousMount
         pass

      class ConnectedIso(vim.fault.OvfExport): # vim.fault.ConnectedIso
         cdrom = vim.vm.device.VirtualCdrom()
         filename = ""

      class CpuCompatibilityUnknown(vim.fault.CpuIncompatible): # vim.fault.CpuCompatibilityUnknown
         pass

      class DeviceBackingNotSupported(vim.fault.DeviceNotSupported): # vim.fault.DeviceBackingNotSupported
         backing = ""

      class DeviceControllerNotSupported(vim.fault.DeviceNotSupported): # vim.fault.DeviceControllerNotSupported
         controller = ""

      class DeviceHotPlugNotSupported(vim.fault.InvalidDeviceSpec): # vim.fault.DeviceHotPlugNotSupported
         pass

      class DeviceNotFound(vim.fault.InvalidDeviceSpec): # vim.fault.DeviceNotFound
         pass

      class DeviceUnsupportedForVmPlatform(vim.fault.InvalidDeviceSpec): # vim.fault.DeviceUnsupportedForVmPlatform
         pass

      class DeviceUnsupportedForVmVersion(vim.fault.InvalidDeviceSpec): # vim.fault.DeviceUnsupportedForVmVersion
         currentVersion = ""
         expectedVersion = ""

      class DisallowedDiskModeChange(vim.fault.InvalidDeviceSpec): # vim.fault.DisallowedDiskModeChange
         pass

      class GatewayHostNotReachable(vim.fault.GatewayToHostConnectFault): # vim.fault.GatewayHostNotReachable
         pass

      class GatewayToHostAuthFault(vim.fault.GatewayToHostConnectFault): # vim.fault.GatewayToHostAuthFault
         invalidProperties = [ "" ]
         missingProperties = [ "" ]

      class InvalidController(vim.fault.InvalidDeviceSpec): # vim.fault.InvalidController
         controllerKey = 0

      class InvalidDeviceBacking(vim.fault.InvalidDeviceSpec): # vim.fault.InvalidDeviceBacking
         pass

      class InvalidDeviceOperation(vim.fault.InvalidDeviceSpec): # vim.fault.InvalidDeviceOperation
         badOp = vim.vm.device.VirtualDeviceSpec.Operation()
         badFileOp = vim.vm.device.VirtualDeviceSpec.FileOperation()

      class InvalidHostConnectionState(vim.fault.InvalidHostState): # vim.fault.InvalidHostConnectionState
         pass

      class OvfConnectedDevice(vim.fault.OvfHardwareExport): # vim.fault.OvfConnectedDevice
         pass

      class OvfConnectedDeviceFloppy(vim.fault.OvfConnectedDevice): # vim.fault.OvfConnectedDeviceFloppy
         filename = ""

      class OvfConnectedDeviceIso(vim.fault.OvfConnectedDevice): # vim.fault.OvfConnectedDeviceIso
         filename = ""

      class OvfDuplicateElement(vim.fault.OvfElement): # vim.fault.OvfDuplicateElement
         pass

      class OvfDuplicatedElementBoundary(vim.fault.OvfElement): # vim.fault.OvfDuplicatedElementBoundary
         boundary = ""

      class OvfDuplicatedPropertyIdExport(vim.fault.OvfExport): # vim.fault.OvfDuplicatedPropertyIdExport
         fqid = ""

      class OvfDuplicatedPropertyIdImport(vim.fault.OvfExport): # vim.fault.OvfDuplicatedPropertyIdImport
         pass

      class OvfNoSpaceOnController(vim.fault.OvfUnsupportedElement): # vim.fault.OvfNoSpaceOnController
         parent = ""

      class PhysCompatRDMNotSupported(vim.fault.RDMNotSupported): # vim.fault.PhysCompatRDMNotSupported
         pass

      class UnusedVirtualDiskBlocksNotScrubbed(vim.fault.DeviceBackingNotSupported): # vim.fault.UnusedVirtualDiskBlocksNotScrubbed
         pass

      class VirtualDiskBlocksNotFullyProvisioned(vim.fault.DeviceBackingNotSupported): # vim.fault.VirtualDiskBlocksNotFullyProvisioned
         pass

      class DVPortNotSupported(vim.fault.DeviceBackingNotSupported): # vim.fault.DVPortNotSupported
         pass

   class host(object): # (unknown name)

      class ActiveDirectorySpec(vmodl.DynamicData): # vim.host.ActiveDirectorySpec
         changeOperation = ""
         spec = vim.host.ActiveDirectorySpec.Specification()

         class Specification(vmodl.DynamicData): # vim.host.ActiveDirectorySpec.Specification
            domainName = ""
            userName = ""
            password = ""
            camServer = ""
            thumbprint = ""
            smartCardAuthenticationEnabled = False
            smartCardTrustAnchors = [ "" ]

      class AssignableHardwareBinding(vmodl.DynamicData): # vim.host.AssignableHardwareBinding
         instanceId = ""
         vm = vim.VirtualMachine()

      class AssignableHardwareConfig(vmodl.DynamicData): # vim.host.AssignableHardwareConfig
         attributeOverride = [ vim.host.AssignableHardwareConfig.AttributeOverride() ]

         class AttributeOverride(vmodl.DynamicData): # vim.host.AssignableHardwareConfig.AttributeOverride
            instanceId = ""
            name = ""
            value = {}

      class AssignableHardwareManager(vmodl.ManagedObject): # vim.host.AssignableHardwareManager
         binding = [ vim.host.AssignableHardwareBinding() ]
         config = vim.host.AssignableHardwareConfig()

         def downloadDescriptionTree(): # vim.host.AssignableHardwareManager.downloadDescriptionTree
            return vmodl.Binary()

         def retrieveDynamicPassthroughInfo(): # vim.host.AssignableHardwareManager.retrieveDynamicPassthroughInfo
            return [ vim.vm.DynamicPassthroughInfo() ]

         def updateConfig(config=vim.host.AssignableHardwareConfig()): # vim.host.AssignableHardwareManager.updateConfig
            # throws vim.fault.HostConfigFault
            return None

      class AuthenticationManager(vmodl.ManagedObject): # vim.host.AuthenticationManager
         info = vim.host.AuthenticationManagerInfo()
         supportedStore = [ vim.host.AuthenticationStore() ]

      class AuthenticationManagerInfo(vmodl.DynamicData): # vim.host.AuthenticationManagerInfo
         authConfig = [ vim.host.AuthenticationStoreInfo() ]

      class AuthenticationStore(vmodl.ManagedObject): # vim.host.AuthenticationStore
         info = vim.host.AuthenticationStoreInfo()

      class AuthenticationStoreInfo(vmodl.DynamicData): # vim.host.AuthenticationStoreInfo
         enabled = False

      class AutoStartManager(vmodl.ManagedObject): # vim.host.AutoStartManager
         config = vim.host.AutoStartManager.Config()

         def reconfigure(spec=vim.host.AutoStartManager.Config()): # vim.host.AutoStartManager.reconfigure
            return None

         def autoPowerOn(): # vim.host.AutoStartManager.autoPowerOn
            return None

         def autoPowerOff(): # vim.host.AutoStartManager.autoPowerOff
            return None

         class Action(Enum): # vim.host.AutoStartManager.Action
            none = 0
            systemDefault = 1
            powerOn = 2
            powerOff = 3
            guestShutdown = 4
            suspend = 5

         class SystemDefaults(vmodl.DynamicData): # vim.host.AutoStartManager.SystemDefaults
            enabled = False
            startDelay = 0
            stopDelay = 0
            waitForHeartbeat = False
            stopAction = ""

         class AutoPowerInfo(vmodl.DynamicData): # vim.host.AutoStartManager.AutoPowerInfo
            key = vim.VirtualMachine()
            startOrder = 0
            startDelay = 0
            waitForHeartbeat = vim.host.AutoStartManager.AutoPowerInfo.WaitHeartbeatSetting()
            startAction = ""
            stopDelay = 0
            stopAction = ""

            class WaitHeartbeatSetting(Enum): # vim.host.AutoStartManager.AutoPowerInfo.WaitHeartbeatSetting
               yes = 0
               no = 1
               systemDefault = 2

         class Config(vmodl.DynamicData): # vim.host.AutoStartManager.Config
            defaults = vim.host.AutoStartManager.SystemDefaults()
            powerInfo = [ vim.host.AutoStartManager.AutoPowerInfo() ]

      class BIOSInfo(vmodl.DynamicData): # vim.host.BIOSInfo
         biosVersion = ""
         releaseDate = vmodl.DateTime()
         vendor = ""
         majorRelease = 0
         minorRelease = 0
         firmwareMajorRelease = 0
         firmwareMinorRelease = 0

      class BootDeviceSystem(vmodl.ManagedObject): # vim.host.BootDeviceSystem

         def queryBootDevices(): # vim.host.BootDeviceSystem.queryBootDevices
            return vim.host.BootDeviceInfo()

         def updateBootDevice(key=""): # vim.host.BootDeviceSystem.updateBootDevice
            return None

         class BootDevice(vmodl.DynamicData): # vim.host.BootDeviceSystem.BootDevice
            key = ""
            description = ""

      class CacheConfigurationManager(vmodl.ManagedObject): # vim.host.CacheConfigurationManager
         cacheConfigurationInfo = [ vim.host.CacheConfigurationManager.CacheConfigurationInfo() ]

         def configureCache(spec=vim.host.CacheConfigurationManager.CacheConfigurationSpec()): # vim.host.CacheConfigurationManager.configureCache
            return vim.Task()

         class CacheConfigurationSpec(vmodl.DynamicData): # vim.host.CacheConfigurationManager.CacheConfigurationSpec
            datastore = vim.Datastore()
            swapSize = 0

         class CacheConfigurationInfo(vmodl.DynamicData): # vim.host.CacheConfigurationManager.CacheConfigurationInfo
            key = vim.Datastore()
            swapSize = 0

      class Capability(vmodl.DynamicData): # vim.host.Capability
         recursiveResourcePoolsSupported = False
         cpuMemoryResourceConfigurationSupported = False
         rebootSupported = False
         shutdownSupported = False
         vmotionSupported = False
         standbySupported = False
         ipmiSupported = False
         maxSupportedVMs = 0
         maxRunningVMs = 0
         maxSupportedVcpus = 0
         maxRegisteredVMs = 0
         datastorePrincipalSupported = False
         sanSupported = False
         nfsSupported = False
         iscsiSupported = False
         vlanTaggingSupported = False
         nicTeamingSupported = False
         highGuestMemSupported = False
         maintenanceModeSupported = False
         suspendedRelocateSupported = False
         restrictedSnapshotRelocateSupported = False
         perVmSwapFiles = False
         localSwapDatastoreSupported = False
         unsharedSwapVMotionSupported = False
         backgroundSnapshotsSupported = False
         preAssignedPCIUnitNumbersSupported = False
         screenshotSupported = False
         scaledScreenshotSupported = False
         storageVMotionSupported = False
         vmotionWithStorageVMotionSupported = False
         vmotionAcrossNetworkSupported = False
         maxNumDisksSVMotion = 0
         hbrNicSelectionSupported = False
         vrNfcNicSelectionSupported = False
         recordReplaySupported = False
         ftSupported = False
         replayUnsupportedReason = ""
         replayCompatibilityIssues = [ "" ]
         smpFtSupported = False
         ftCompatibilityIssues = [ "" ]
         smpFtCompatibilityIssues = [ "" ]
         maxVcpusPerFtVm = 0
         loginBySSLThumbprintSupported = False
         cloneFromSnapshotSupported = False
         deltaDiskBackingsSupported = False
         perVMNetworkTrafficShapingSupported = False
         tpmSupported = False
         tpmVersion = ""
         txtEnabled = False
         supportedCpuFeature = [ vim.host.CpuIdInfo() ]
         virtualExecUsageSupported = False
         storageIORMSupported = False
         vmDirectPathGen2Supported = False
         vmDirectPathGen2UnsupportedReason = [ "" ]
         vmDirectPathGen2UnsupportedReasonExtended = ""
         supportedVmfsMajorVersion = [ 0 ]
         vStorageCapable = False
         snapshotRelayoutSupported = False
         firewallIpRulesSupported = False
         servicePackageInfoSupported = False
         maxHostRunningVms = 0
         maxHostSupportedVcpus = 0
         vmfsDatastoreMountCapable = False
         eightPlusHostVmfsSharedAccessSupported = False
         nestedHVSupported = False
         vPMCSupported = False
         interVMCommunicationThroughVMCISupported = False
         scheduledHardwareUpgradeSupported = False
         featureCapabilitiesSupported = False
         latencySensitivitySupported = False
         storagePolicySupported = False
         accel3dSupported = False
         reliableMemoryAware = False
         multipleNetworkStackInstanceSupported = False
         messageBusProxySupported = False
         vsanSupported = False
         vFlashSupported = False
         hostAccessManagerSupported = False
         provisioningNicSelectionSupported = False
         nfs41Supported = False
         nfs41Krb5iSupported = False
         turnDiskLocatorLedSupported = False
         virtualVolumeDatastoreSupported = False
         markAsSsdSupported = False
         markAsLocalSupported = False
         smartCardAuthenticationSupported = False
         pMemSupported = False
         pMemSnapshotSupported = False
         cryptoSupported = False
         oneKVolumeAPIsSupported = False
         gatewayOnNicSupported = False
         upitSupported = False
         cpuHwMmuSupported = False
         encryptedVMotionSupported = False
         encryptionChangeOnAddRemoveSupported = False
         encryptionHotOperationSupported = False
         encryptionWithSnapshotsSupported = False
         encryptionFaultToleranceSupported = False
         encryptionMemorySaveSupported = False
         encryptionRDMSupported = False
         encryptionVFlashSupported = False
         encryptionCBRCSupported = False
         encryptionHBRSupported = False
         ftEfiSupported = False
         unmapMethodSupported = ""
         maxMemMBPerFtVm = 0
         virtualMmuUsageIgnored = False
         virtualExecUsageIgnored = False
         vmCreateDateSupported = False
         vmfs3EOLSupported = False
         ftVmcpSupported = False
         quickBootSupported = False
         assignableHardwareSupported = False
         useFeatureReqsForOldHWv = False
         markPerenniallyReservedSupported = False
         hppPspSupported = False
         deviceRebindWithoutRebootSupported = False
         storagePolicyChangeSupported = False
         precisionTimeProtocolSupported = False
         remoteDeviceVMotionSupported = False
         maxSupportedVmMemory = 0

         class ReplayUnsupportedReason(Enum): # vim.host.Capability.ReplayUnsupportedReason
            incompatibleProduct = 0
            incompatibleCpu = 1
            hvDisabled = 2
            cpuidLimitSet = 3
            oldBIOS = 4
            unknown = 5

         class FtUnsupportedReason(Enum): # vim.host.Capability.FtUnsupportedReason
            vMotionNotLicensed = 0
            missingVMotionNic = 1
            missingFTLoggingNic = 2
            ftNotLicensed = 3
            haAgentIssue = 4
            unsupportedProduct = 5
            cpuHvUnsupported = 6
            cpuHwmmuUnsupported = 7
            cpuHvDisabled = 8

         class VmDirectPathGen2UnsupportedReason(Enum): # vim.host.Capability.VmDirectPathGen2UnsupportedReason
            hostNptIncompatibleProduct = 0
            hostNptIncompatibleHardware = 1
            hostNptDisabled = 2

         class UnmapMethodSupported(Enum): # vim.host.Capability.UnmapMethodSupported
            priority = 0
            fixed = 1
            dynamic = 2

      class CertificateManager(vmodl.ManagedObject): # vim.host.CertificateManager
         certificateInfo = vim.host.CertificateManager.CertificateInfo()

         def generateCertificateSigningRequest(useIpAddressAsCommonName=False): # vim.host.CertificateManager.generateCertificateSigningRequest
            # throws vim.fault.HostConfigFault
            return ""

         def generateCertificateSigningRequestByDn(distinguishedName=""): # vim.host.CertificateManager.generateCertificateSigningRequestByDn
            # throws vim.fault.HostConfigFault
            return ""

         def installServerCertificate(cert=""): # vim.host.CertificateManager.installServerCertificate
            # throws vim.fault.HostConfigFault
            return None

         def replaceCACertificatesAndCRLs(caCert=[ "" ], caCrl=[ "" ] or None): # vim.host.CertificateManager.replaceCACertificatesAndCRLs
            # throws vim.fault.HostConfigFault
            return None

         def listCACertificates(): # vim.host.CertificateManager.listCACertificates
            # throws vim.fault.HostConfigFault
            return [ "" ]

         def listCACertificateRevocationLists(): # vim.host.CertificateManager.listCACertificateRevocationLists
            # throws vim.fault.HostConfigFault
            return [ "" ]

         class CertificateInfo(vmodl.DynamicData): # vim.host.CertificateManager.CertificateInfo
            issuer = ""
            notBefore = vmodl.DateTime()
            notAfter = vmodl.DateTime()
            subject = ""
            status = ""

            class CertificateStatus(Enum): # vim.host.CertificateManager.CertificateInfo.CertificateStatus
               unknown = 0
               expired = 1
               expiring = 2
               expiringShortly = 3
               expirationImminent = 4
               good = 5
               revoked = 6

      class ConfigChange(vmodl.DynamicData): # vim.host.ConfigChange

         class Mode(Enum): # vim.host.ConfigChange.Mode
            modify = 0
            replace = 1

         class Operation(Enum): # vim.host.ConfigChange.Operation
            add = 0
            remove = 1
            edit = 2
            ignore = 3

      class ConfigManager(vmodl.DynamicData): # vim.host.ConfigManager
         cpuScheduler = vim.host.CpuSchedulerSystem()
         datastoreSystem = vim.host.DatastoreSystem()
         memoryManager = vim.host.MemoryManagerSystem()
         storageSystem = vim.host.StorageSystem()
         networkSystem = vim.host.NetworkSystem()
         vmotionSystem = vim.host.VMotionSystem()
         virtualNicManager = vim.host.VirtualNicManager()
         serviceSystem = vim.host.ServiceSystem()
         firewallSystem = vim.host.FirewallSystem()
         advancedOption = vim.option.OptionManager()
         diagnosticSystem = vim.host.DiagnosticSystem()
         autoStartManager = vim.host.AutoStartManager()
         snmpSystem = vim.host.SnmpSystem()
         dateTimeSystem = vim.host.DateTimeSystem()
         patchManager = vim.host.PatchManager()
         imageConfigManager = vim.host.ImageConfigManager()
         bootDeviceSystem = vim.host.BootDeviceSystem()
         firmwareSystem = vim.host.FirmwareSystem()
         healthStatusSystem = vim.host.HealthStatusSystem()
         pciPassthruSystem = vim.host.PciPassthruSystem()
         licenseManager = vim.LicenseManager()
         kernelModuleSystem = vim.host.KernelModuleSystem()
         authenticationManager = vim.host.AuthenticationManager()
         powerSystem = vim.host.PowerSystem()
         cacheConfigurationManager = vim.host.CacheConfigurationManager()
         esxAgentHostManager = vim.host.EsxAgentHostManager()
         iscsiManager = vim.host.IscsiManager()
         vFlashManager = vim.host.VFlashManager()
         vsanSystem = vim.host.VsanSystem()
         messageBusProxy = vim.host.MessageBusProxy()
         userDirectory = vim.UserDirectory()
         accountManager = vim.host.LocalAccountManager()
         hostAccessManager = vim.host.HostAccessManager()
         graphicsManager = vim.host.GraphicsManager()
         vsanInternalSystem = vim.host.VsanInternalSystem()
         certificateManager = vim.host.CertificateManager()
         cryptoManager = vim.encryption.CryptoManager()
         nvdimmSystem = vim.host.NvdimmSystem()
         assignableHardwareManager = vim.host.AssignableHardwareManager()

      class CpuIdInfo(vmodl.DynamicData): # vim.host.CpuIdInfo
         level = 0
         vendor = ""
         eax = ""
         ebx = ""
         ecx = ""
         edx = ""

      class CpuInfo(vmodl.DynamicData): # vim.host.CpuInfo
         numCpuPackages = 0
         numCpuCores = 0
         numCpuThreads = 0
         hz = 0

      class CpuPackage(vmodl.DynamicData): # vim.host.CpuPackage
         index = 0
         vendor = ""
         hz = 0
         busHz = 0
         description = ""
         threadId = [ 0 ]
         cpuFeature = [ vim.host.CpuIdInfo() ]

         class Vendor(Enum): # vim.host.CpuPackage.Vendor
            unknown = 0
            intel = 1
            amd = 2
            hygon = 3
            arm = 4

      class CpuPowerManagementInfo(vmodl.DynamicData): # vim.host.CpuPowerManagementInfo
         currentPolicy = ""
         hardwareSupport = ""

         class PolicyType(Enum): # vim.host.CpuPowerManagementInfo.PolicyType
            off = 0
            staticPolicy = 1
            dynamicPolicy = 2

      class CpuSchedulerSystem(vim.ExtensibleManagedObject): # vim.host.CpuSchedulerSystem
         hyperthreadInfo = vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo()

         def enableHyperThreading(): # vim.host.CpuSchedulerSystem.enableHyperThreading
            return None

         def disableHyperThreading(): # vim.host.CpuSchedulerSystem.disableHyperThreading
            return None

         class HyperThreadScheduleInfo(vmodl.DynamicData): # vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo
            available = False
            active = False
            config = False

      class DatastoreBrowser(vmodl.ManagedObject): # vim.host.DatastoreBrowser
         datastore = [ vim.Datastore() ]
         supportedType = [ vim.host.DatastoreBrowser.Query() ]

         def search(datastorePath="", searchSpec=vim.host.DatastoreBrowser.SearchSpec() or None): # vim.host.DatastoreBrowser.search
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return vim.Task()

         def searchSubFolders(datastorePath="", searchSpec=vim.host.DatastoreBrowser.SearchSpec() or None): # vim.host.DatastoreBrowser.searchSubFolders
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return vim.Task()

         def deleteFile(datastorePath=""): # vim.host.DatastoreBrowser.deleteFile
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return None

         class FileInfo(vmodl.DynamicData): # vim.host.DatastoreBrowser.FileInfo
            path = ""
            friendlyName = ""
            fileSize = 0
            modification = vmodl.DateTime()
            owner = ""

            class Details(vmodl.DynamicData): # vim.host.DatastoreBrowser.FileInfo.Details
               fileType = False
               fileSize = False
               modification = False
               fileOwner = False

         class Query(vmodl.DynamicData): # vim.host.DatastoreBrowser.Query
            pass

         class VmConfigQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.VmConfigQuery
            filter = vim.host.DatastoreBrowser.VmConfigQuery.Filter()
            details = vim.host.DatastoreBrowser.VmConfigQuery.Details()

            class Filter(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmConfigQuery.Filter
               matchConfigVersion = [ 0 ]
               encrypted = False

            class Details(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmConfigQuery.Details
               configVersion = False
               encryption = False

         class TemplateVmConfigQuery(vim.host.DatastoreBrowser.VmConfigQuery): # vim.host.DatastoreBrowser.TemplateVmConfigQuery
            pass

         class VmDiskQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.VmDiskQuery
            filter = vim.host.DatastoreBrowser.VmDiskQuery.Filter()
            details = vim.host.DatastoreBrowser.VmDiskQuery.Details()

            class Filter(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmDiskQuery.Filter
               diskType = [ vmodl.TypeName() ]
               matchHardwareVersion = [ 0 ]
               controllerType = [ vmodl.TypeName() ]
               thin = False
               encrypted = False

            class Details(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmDiskQuery.Details
               diskType = False
               capacityKb = False
               hardwareVersion = False
               controllerType = False
               diskExtents = False
               thin = False
               encryption = False

         class FolderQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.FolderQuery
            pass

         class VmSnapshotQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.VmSnapshotQuery
            pass

         class IsoImageQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.IsoImageQuery
            pass

         class FloppyImageQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.FloppyImageQuery
            pass

         class VmNvramQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.VmNvramQuery
            pass

         class VmLogQuery(vim.host.DatastoreBrowser.Query): # vim.host.DatastoreBrowser.VmLogQuery
            pass

         class VmConfigInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.VmConfigInfo
            configVersion = 0
            encryption = vim.host.DatastoreBrowser.VmConfigInfo.VmConfigEncryptionInfo()

            class VmConfigEncryptionInfo(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmConfigInfo.VmConfigEncryptionInfo
               keyId = vim.encryption.CryptoKeyId()

         class TemplateVmConfigInfo(vim.host.DatastoreBrowser.VmConfigInfo): # vim.host.DatastoreBrowser.TemplateVmConfigInfo
            pass

         class VmDiskInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.VmDiskInfo
            diskType = vmodl.TypeName()
            capacityKb = 0
            hardwareVersion = 0
            controllerType = vmodl.TypeName()
            diskExtents = [ "" ]
            thin = False
            encryption = vim.host.DatastoreBrowser.VmDiskInfo.VmDiskEncryptionInfo()

            class VmDiskEncryptionInfo(vmodl.DynamicData): # vim.host.DatastoreBrowser.VmDiskInfo.VmDiskEncryptionInfo
               keyId = vim.encryption.CryptoKeyId()

         class FolderInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.FolderInfo
            pass

         class VmSnapshotInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.VmSnapshotInfo
            pass

         class IsoImageInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.IsoImageInfo
            pass

         class FloppyImageInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.FloppyImageInfo
            pass

         class VmNvramInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.VmNvramInfo
            pass

         class VmLogInfo(vim.host.DatastoreBrowser.FileInfo): # vim.host.DatastoreBrowser.VmLogInfo
            pass

         class SearchSpec(vmodl.DynamicData): # vim.host.DatastoreBrowser.SearchSpec
            query = [ vim.host.DatastoreBrowser.Query() ]
            details = vim.host.DatastoreBrowser.FileInfo.Details()
            searchCaseInsensitive = False
            matchPattern = [ "" ]
            sortFoldersFirst = False

         class SearchResults(vmodl.DynamicData): # vim.host.DatastoreBrowser.SearchResults
            datastore = vim.Datastore()
            folderPath = ""
            file = [ vim.host.DatastoreBrowser.FileInfo() ]

      class DateTimeConfig(vmodl.DynamicData): # vim.host.DateTimeConfig
         timeZone = ""
         ntpConfig = vim.host.NtpConfig()

      class DateTimeSystem(vmodl.ManagedObject): # vim.host.DateTimeSystem
         dateTimeInfo = vim.host.DateTimeInfo()

         def updateConfig(config=vim.host.DateTimeConfig()): # vim.host.DateTimeSystem.updateConfig
            # throws vim.fault.HostConfigFault
            return None

         def queryAvailableTimeZones(): # vim.host.DateTimeSystem.queryAvailableTimeZones
            return [ vim.host.DateTimeSystem.TimeZone() ]

         def queryDateTime(): # vim.host.DateTimeSystem.queryDateTime
            return vmodl.DateTime()

         def updateDateTime(dateTime=vmodl.DateTime()): # vim.host.DateTimeSystem.updateDateTime
            # throws vim.fault.HostConfigFault
            return None

         def refresh(): # vim.host.DateTimeSystem.refresh
            return None

         class TimeZone(vmodl.DynamicData): # vim.host.DateTimeSystem.TimeZone
            key = ""
            name = ""
            description = ""
            gmtOffset = 0

      class DeploymentInfo(vmodl.DynamicData): # vim.host.DeploymentInfo
         bootedFromStatelessCache = False

      class Device(vmodl.DynamicData): # vim.host.Device
         deviceName = ""
         deviceType = ""

      class DhcpService(vmodl.DynamicData): # vim.host.DhcpService
         key = ""
         spec = vim.host.DhcpService.Specification()

         class Specification(vmodl.DynamicData): # vim.host.DhcpService.Specification
            virtualSwitch = ""
            defaultLeaseDuration = 0
            leaseBeginIp = ""
            leaseEndIp = ""
            maxLeaseDuration = 0
            unlimitedLease = False
            ipSubnetAddr = ""
            ipSubnetMask = ""

         class Config(vmodl.DynamicData): # vim.host.DhcpService.Config
            changeOperation = ""
            key = ""
            spec = vim.host.DhcpService.Specification()

      class DigestInfo(vmodl.DynamicData): # vim.host.DigestInfo
         digestMethod = ""
         digestValue = [ 0x00 ]
         objectName = ""

         class DigestMethodType(Enum): # vim.host.DigestInfo.DigestMethodType
            SHA1 = 0
            MD5 = 1
            SHA256 = 2
            SHA384 = 3
            SHA512 = 4
            SM3_256 = 5

      class DirectoryStore(vim.host.AuthenticationStore): # vim.host.DirectoryStore
         pass

      class DirectoryStoreInfo(vim.host.AuthenticationStoreInfo): # vim.host.DirectoryStoreInfo
         pass

      class DiskConfigurationResult(vmodl.DynamicData): # vim.host.DiskConfigurationResult
         devicePath = ""
         success = False
         fault = vmodl.MethodFault()

      class DiskDimensions(vmodl.DynamicData): # vim.host.DiskDimensions

         class Chs(vmodl.DynamicData): # vim.host.DiskDimensions.Chs
            cylinder = 0
            head = 0
            sector = 0

         class Lba(vmodl.DynamicData): # vim.host.DiskDimensions.Lba
            blockSize = 0
            block = 0

      class DiskPartitionInfo(vmodl.DynamicData): # vim.host.DiskPartitionInfo
         deviceName = ""
         spec = vim.host.DiskPartitionInfo.Specification()
         layout = vim.host.DiskPartitionInfo.Layout()

         class PartitionFormat(Enum): # vim.host.DiskPartitionInfo.PartitionFormat
            gpt = 0
            mbr = 1
            unknown = 2

         class Type(Enum): # vim.host.DiskPartitionInfo.Type
            none = 0
            vmfs = 1
            linuxNative = 2
            linuxSwap = 3
            extended = 4
            ntfs = 5
            vmkDiagnostic = 6
            vffs = 7

         class Partition(vmodl.DynamicData): # vim.host.DiskPartitionInfo.Partition
            partition = 0
            startSector = 0
            endSector = 0
            type = ""
            guid = ""
            logical = False
            attributes = 0x00
            partitionAlignment = 0

         class BlockRange(vmodl.DynamicData): # vim.host.DiskPartitionInfo.BlockRange
            partition = 0
            type = ""
            start = vim.host.DiskDimensions.Lba()
            end = vim.host.DiskDimensions.Lba()

         class Specification(vmodl.DynamicData): # vim.host.DiskPartitionInfo.Specification
            partitionFormat = ""
            chs = vim.host.DiskDimensions.Chs()
            totalSectors = 0
            partition = [ vim.host.DiskPartitionInfo.Partition() ]

         class Layout(vmodl.DynamicData): # vim.host.DiskPartitionInfo.Layout
            total = vim.host.DiskDimensions.Lba()
            partition = [ vim.host.DiskPartitionInfo.BlockRange() ]

      class DnsConfig(vmodl.DynamicData): # vim.host.DnsConfig
         dhcp = False
         virtualNicDevice = ""
         ipv6VirtualNicDevice = ""
         hostName = ""
         domainName = ""
         address = [ "" ]
         searchDomain = [ "" ]

      class DnsConfigSpec(vim.host.DnsConfig): # vim.host.DnsConfigSpec
         virtualNicConnection = vim.host.VirtualNicConnection()
         virtualNicConnectionV6 = vim.host.VirtualNicConnection()

      class EnterMaintenanceResult(vmodl.DynamicData): # vim.host.EnterMaintenanceResult
         vmFaults = [ vim.FaultsByVM() ]
         hostFaults = [ vim.FaultsByHost() ]

      class EsxAgentHostManager(vmodl.ManagedObject): # vim.host.EsxAgentHostManager
         configInfo = vim.host.EsxAgentHostManager.ConfigInfo()

         def updateConfig(configInfo=vim.host.EsxAgentHostManager.ConfigInfo()): # vim.host.EsxAgentHostManager.updateConfig
            # throws vim.fault.HostConfigFault
            return None

         class ConfigInfo(vmodl.DynamicData): # vim.host.EsxAgentHostManager.ConfigInfo
            agentVmDatastore = vim.Datastore()
            agentVmNetwork = vim.Network()

      class FaultToleranceManager(object): # (unknown name)

         class ComponentHealthInfo(vmodl.DynamicData): # vim.host.FaultToleranceManager.ComponentHealthInfo
            isStorageHealthy = False
            isNetworkHealthy = False

      class FcoeConfig(vmodl.DynamicData): # vim.host.FcoeConfig
         priorityClass = 0
         sourceMac = ""
         vlanRange = [ vim.host.FcoeConfig.VlanRange() ]
         capabilities = vim.host.FcoeConfig.FcoeCapabilities()
         fcoeActive = False

         class VlanRange(vmodl.DynamicData): # vim.host.FcoeConfig.VlanRange
            vlanLow = 0
            vlanHigh = 0

         class FcoeCapabilities(vmodl.DynamicData): # vim.host.FcoeConfig.FcoeCapabilities
            priorityClass = False
            sourceMacAddress = False
            vlanRange = False

         class FcoeSpecification(vmodl.DynamicData): # vim.host.FcoeConfig.FcoeSpecification
            underlyingPnic = ""
            priorityClass = 0
            sourceMac = ""
            vlanRange = [ vim.host.FcoeConfig.VlanRange() ]

      class FeatureCapability(vmodl.DynamicData): # vim.host.FeatureCapability
         key = ""
         featureName = ""
         value = ""

      class FeatureMask(vmodl.DynamicData): # vim.host.FeatureMask
         key = ""
         featureName = ""
         value = ""

      class FeatureVersionInfo(vmodl.DynamicData): # vim.host.FeatureVersionInfo
         key = ""
         value = ""

         class FeatureVersionKey(Enum): # vim.host.FeatureVersionInfo.FeatureVersionKey
            faultTolerance = 0

      class FileAccess(vmodl.DynamicData): # vim.host.FileAccess
         who = ""
         what = ""

         class Modes(vmodl.DynamicData): # vim.host.FileAccess.Modes
            browse = ""
            read = ""
            modify = ""
            use = ""
            admin = ""
            full = ""

      class FileSystemMountInfo(vmodl.DynamicData): # vim.host.FileSystemMountInfo
         mountInfo = vim.host.MountInfo()
         volume = vim.host.FileSystemVolume()
         vStorageSupport = ""

         class VStorageSupportStatus(Enum): # vim.host.FileSystemMountInfo.VStorageSupportStatus
            vStorageSupported = 0
            vStorageUnsupported = 1
            vStorageUnknown = 2

      class FileSystemVolume(vmodl.DynamicData): # vim.host.FileSystemVolume
         type = ""
         name = ""
         capacity = 0

         class FileSystemType(Enum): # vim.host.FileSystemVolume.FileSystemType
            VMFS = 0
            NFS = 1
            NFS41 = 2
            CIFS = 3
            vsan = 4
            VFFS = 5
            VVOL = 6
            PMEM = 7
            OTHER = 8

      class FileSystemVolumeInfo(vmodl.DynamicData): # vim.host.FileSystemVolumeInfo
         volumeTypeList = [ "" ]
         mountInfo = [ vim.host.FileSystemMountInfo() ]

      class FirewallInfo(vmodl.DynamicData): # vim.host.FirewallInfo
         defaultPolicy = vim.host.FirewallInfo.DefaultPolicy()
         ruleset = [ vim.host.Ruleset() ]

         class DefaultPolicy(vmodl.DynamicData): # vim.host.FirewallInfo.DefaultPolicy
            incomingBlocked = False
            outgoingBlocked = False

      class FirmwareSystem(vmodl.ManagedObject): # vim.host.FirmwareSystem

         def resetToFactoryDefaults(): # vim.host.FirmwareSystem.resetToFactoryDefaults
            # throws vim.fault.InvalidState
            return None

         def backupConfiguration(): # vim.host.FirmwareSystem.backupConfiguration
            return ""

         def queryConfigUploadURL(): # vim.host.FirmwareSystem.queryConfigUploadURL
            return ""

         def restoreConfiguration(force=False): # vim.host.FirmwareSystem.restoreConfiguration
            # throws vim.fault.InvalidState, vim.fault.FileFault, vim.fault.MismatchedBundle, vim.fault.InvalidBundle
            return None

      class FlagInfo(vmodl.DynamicData): # vim.host.FlagInfo
         backgroundSnapshotsEnabled = False

      class ForceMountedInfo(vmodl.DynamicData): # vim.host.ForceMountedInfo
         persist = False
         mounted = False

      class GatewaySpec(vmodl.DynamicData): # vim.host.GatewaySpec
         gatewayType = ""
         gatewayId = ""
         trustVerificationToken = ""
         hostAuthParams = [ vim.KeyValue() ]

      class GraphicsConfig(vmodl.DynamicData): # vim.host.GraphicsConfig
         hostDefaultGraphicsType = ""
         sharedPassthruAssignmentPolicy = ""
         deviceType = [ vim.host.GraphicsConfig.DeviceType() ]

         class GraphicsType(Enum): # vim.host.GraphicsConfig.GraphicsType
            shared = 0
            sharedDirect = 1

         class SharedPassthruAssignmentPolicy(Enum): # vim.host.GraphicsConfig.SharedPassthruAssignmentPolicy
            performance = 0
            consolidation = 1

         class DeviceType(vmodl.DynamicData): # vim.host.GraphicsConfig.DeviceType
            deviceId = ""
            graphicsType = ""

      class GraphicsInfo(vmodl.DynamicData): # vim.host.GraphicsInfo
         deviceName = ""
         vendorName = ""
         pciId = ""
         graphicsType = ""
         memorySizeInKB = 0
         vm = [ vim.VirtualMachine() ]

         class GraphicsType(Enum): # vim.host.GraphicsInfo.GraphicsType
            basic = 0
            shared = 1
            direct = 2
            sharedDirect = 3

      class GraphicsManager(vim.ExtensibleManagedObject): # vim.host.GraphicsManager
         graphicsInfo = [ vim.host.GraphicsInfo() ]
         graphicsConfig = vim.host.GraphicsConfig()
         sharedPassthruGpuTypes = [ "" ]
         sharedGpuCapabilities = [ vim.host.SharedGpuCapabilities() ]

         def refresh(): # vim.host.GraphicsManager.refresh
            return None

         def isSharedGraphicsActive(): # vim.host.GraphicsManager.isSharedGraphicsActive
            return False

         def updateGraphicsConfig(config=vim.host.GraphicsConfig()): # vim.host.GraphicsManager.updateGraphicsConfig
            return None

      class HardwareInfo(vmodl.DynamicData): # vim.host.HardwareInfo
         systemInfo = vim.host.SystemInfo()
         cpuPowerManagementInfo = vim.host.CpuPowerManagementInfo()
         cpuInfo = vim.host.CpuInfo()
         cpuPkg = [ vim.host.CpuPackage() ]
         memorySize = 0
         numaInfo = vim.host.NumaInfo()
         smcPresent = False
         pciDevice = [ vim.host.PciDevice() ]
         cpuFeature = [ vim.host.CpuIdInfo() ]
         biosInfo = vim.host.BIOSInfo()
         reliableMemoryInfo = vim.host.ReliableMemoryInfo()
         persistentMemoryInfo = vim.host.PersistentMemoryInfo()
         sgxInfo = vim.host.SgxInfo()

      class HardwareStatusInfo(vmodl.DynamicData): # vim.host.HardwareStatusInfo
         memoryStatusInfo = [ vim.host.HardwareStatusInfo.HardwareElementInfo() ]
         cpuStatusInfo = [ vim.host.HardwareStatusInfo.HardwareElementInfo() ]
         storageStatusInfo = [ vim.host.HardwareStatusInfo.StorageStatusInfo() ]

         class Status(Enum): # vim.host.HardwareStatusInfo.Status
            Unknown = 0
            Green = 1
            Yellow = 2
            Red = 3

         class HardwareElementInfo(vmodl.DynamicData): # vim.host.HardwareStatusInfo.HardwareElementInfo
            name = ""
            status = vim.ElementDescription()

         class StorageStatusInfo(vim.host.HardwareStatusInfo.HardwareElementInfo): # vim.host.HardwareStatusInfo.StorageStatusInfo
            operationalInfo = [ vim.host.HardwareStatusInfo.StorageStatusInfo.OperationalInfo() ]

            class OperationalInfo(vmodl.DynamicData): # vim.host.HardwareStatusInfo.StorageStatusInfo.OperationalInfo
               property = ""
               value = ""

      class HealthStatusSystem(vmodl.ManagedObject): # vim.host.HealthStatusSystem
         runtime = vim.host.HealthStatusSystem.Runtime()

         def refresh(): # vim.host.HealthStatusSystem.refresh
            return None

         def resetSystemHealthInfo(): # vim.host.HealthStatusSystem.resetSystemHealthInfo
            return None

         def clearSystemEventLog(): # vim.host.HealthStatusSystem.clearSystemEventLog
            return None

         def FetchSystemEventLog(): # vim.host.HealthStatusSystem.FetchSystemEventLog
            return [ vim.host.SystemEventInfo() ]

         class Runtime(vmodl.DynamicData): # vim.host.HealthStatusSystem.Runtime
            systemHealthInfo = vim.host.SystemHealthInfo()
            hardwareStatusInfo = vim.host.HardwareStatusInfo()

      class HostAccessManager(vmodl.ManagedObject): # vim.host.HostAccessManager
         lockdownMode = vim.host.HostAccessManager.LockdownMode()

         def retrieveAccessEntries(): # vim.host.HostAccessManager.retrieveAccessEntries
            return [ vim.host.HostAccessManager.AccessEntry() ]

         def changeAccessMode(principal="", isGroup=False, accessMode=vim.host.HostAccessManager.AccessMode()): # vim.host.HostAccessManager.changeAccessMode
            # throws vim.fault.AuthMinimumAdminPermission, vim.fault.UserNotFound
            return None

         def querySystemUsers(): # vim.host.HostAccessManager.querySystemUsers
            return [ "" ]

         def updateSystemUsers(users=[ "" ] or None): # vim.host.HostAccessManager.updateSystemUsers
            # throws vim.fault.UserNotFound
            return None

         def queryLockdownExceptions(): # vim.host.HostAccessManager.queryLockdownExceptions
            return [ "" ]

         def updateLockdownExceptions(users=[ "" ] or None): # vim.host.HostAccessManager.updateLockdownExceptions
            # throws vim.fault.AuthMinimumAdminPermission, vim.fault.UserNotFound
            return None

         def changeLockdownMode(mode=vim.host.HostAccessManager.LockdownMode()): # vim.host.HostAccessManager.changeLockdownMode
            # throws vim.fault.AuthMinimumAdminPermission
            return None

         class AccessMode(Enum): # vim.host.HostAccessManager.AccessMode
            accessNone = 0
            accessAdmin = 1
            accessNoAccess = 2
            accessReadOnly = 3
            accessOther = 4

         class AccessEntry(vmodl.DynamicData): # vim.host.HostAccessManager.AccessEntry
            principal = ""
            group = False
            accessMode = vim.host.HostAccessManager.AccessMode()

         class LockdownMode(Enum): # vim.host.HostAccessManager.LockdownMode
            lockdownDisabled = 0
            lockdownNormal = 1
            lockdownStrict = 2

      class HostBusAdapter(vmodl.DynamicData): # vim.host.HostBusAdapter
         key = ""
         device = ""
         bus = 0
         status = ""
         model = ""
         driver = ""
         pci = ""
         storageProtocol = ""

      class HostProxySwitch(vmodl.DynamicData): # vim.host.HostProxySwitch
         dvsUuid = ""
         dvsName = ""
         key = ""
         numPorts = 0
         configNumPorts = 0
         numPortsAvailable = 0
         uplinkPort = [ vim.KeyValue() ]
         mtu = 0
         pnic = [ vim.host.PhysicalNic() ]
         spec = vim.host.HostProxySwitch.Specification()
         hostLag = [ vim.host.HostProxySwitch.HostLagConfig() ]
         networkReservationSupported = False
         nsxtEnabled = False
         ensEnabled = False
         ensInterruptEnabled = False
         transportZones = [ vim.dvs.HostMember.TransportZoneInfo() ]
         nsxUsedUplinkPort = [ "" ]
         nsxtStatus = ""
         nsxtStatusDetail = ""

         class Specification(vmodl.DynamicData): # vim.host.HostProxySwitch.Specification
            backing = vim.dvs.HostMember.Backing()

         class Config(vmodl.DynamicData): # vim.host.HostProxySwitch.Config
            changeOperation = ""
            uuid = ""
            spec = vim.host.HostProxySwitch.Specification()

         class HostLagConfig(vmodl.DynamicData): # vim.host.HostProxySwitch.HostLagConfig
            lagKey = ""
            lagName = ""
            uplinkPort = [ vim.KeyValue() ]

      class ImageConfigManager(vmodl.ManagedObject): # vim.host.ImageConfigManager

         def queryHostAcceptanceLevel(): # vim.host.ImageConfigManager.queryHostAcceptanceLevel
            # throws vim.fault.HostConfigFault
            return ""

         def queryHostImageProfile(): # vim.host.ImageConfigManager.queryHostImageProfile
            return vim.host.ImageConfigManager.ImageProfileSummary()

         def updateAcceptanceLevel(newAcceptanceLevel=""): # vim.host.ImageConfigManager.updateAcceptanceLevel
            # throws vim.fault.HostConfigFault
            return None

         def fetchSoftwarePackages(): # vim.host.ImageConfigManager.fetchSoftwarePackages
            return [ vim.host.SoftwarePackage() ]

         def installDate(): # vim.host.ImageConfigManager.installDate
            return vmodl.DateTime()

         class AcceptanceLevel(Enum): # vim.host.ImageConfigManager.AcceptanceLevel
            vmware_certified = 0
            vmware_accepted = 1
            partner = 2
            community = 3

         class ImageProfileSummary(vmodl.DynamicData): # vim.host.ImageConfigManager.ImageProfileSummary
            name = ""
            vendor = ""

      class IpConfig(vmodl.DynamicData): # vim.host.IpConfig
         dhcp = False
         ipAddress = ""
         subnetMask = ""
         ipV6Config = vim.host.IpConfig.IpV6AddressConfiguration()

         class IpV6AddressConfigType(Enum): # vim.host.IpConfig.IpV6AddressConfigType
            other = 0
            manual = 1
            dhcp = 2
            linklayer = 3
            random = 4

         class IpV6AddressStatus(Enum): # vim.host.IpConfig.IpV6AddressStatus
            preferred = 0
            deprecated = 1
            invalid = 2
            inaccessible = 3
            unknown = 4
            tentative = 5
            duplicate = 6

         class IpV6Address(vmodl.DynamicData): # vim.host.IpConfig.IpV6Address
            ipAddress = ""
            prefixLength = 0
            origin = ""
            dadState = ""
            lifetime = vmodl.DateTime()
            operation = ""

         class IpV6AddressConfiguration(vmodl.DynamicData): # vim.host.IpConfig.IpV6AddressConfiguration
            ipV6Address = [ vim.host.IpConfig.IpV6Address() ]
            autoConfigurationEnabled = False
            dhcpV6Enabled = False

      class IpRouteConfig(vmodl.DynamicData): # vim.host.IpRouteConfig
         defaultGateway = ""
         gatewayDevice = ""
         ipV6DefaultGateway = ""
         ipV6GatewayDevice = ""

      class IpRouteConfigSpec(vim.host.IpRouteConfig): # vim.host.IpRouteConfigSpec
         gatewayDeviceConnection = vim.host.VirtualNicConnection()
         ipV6GatewayDeviceConnection = vim.host.VirtualNicConnection()

      class IpRouteEntry(vmodl.DynamicData): # vim.host.IpRouteEntry
         network = ""
         prefixLength = 0
         gateway = ""
         deviceName = ""

      class IpRouteOp(vmodl.DynamicData): # vim.host.IpRouteOp
         changeOperation = ""
         route = vim.host.IpRouteEntry()

      class IpRouteTableConfig(vmodl.DynamicData): # vim.host.IpRouteTableConfig
         ipRoute = [ vim.host.IpRouteOp() ]
         ipv6Route = [ vim.host.IpRouteOp() ]

      class IpRouteTableInfo(vmodl.DynamicData): # vim.host.IpRouteTableInfo
         ipRoute = [ vim.host.IpRouteEntry() ]
         ipv6Route = [ vim.host.IpRouteEntry() ]

      class IpmiInfo(vmodl.DynamicData): # vim.host.IpmiInfo
         bmcIpAddress = ""
         bmcMacAddress = ""
         login = ""
         password = ""

      class IscsiManager(vmodl.ManagedObject): # vim.host.IscsiManager

         def queryVnicStatus(vnicDevice=""): # vim.host.IscsiManager.queryVnicStatus
            # throws vim.fault.IscsiFault
            return vim.host.IscsiManager.IscsiStatus()

         def queryPnicStatus(pnicDevice=""): # vim.host.IscsiManager.queryPnicStatus
            # throws vim.fault.IscsiFault
            return vim.host.IscsiManager.IscsiStatus()

         def queryBoundVnics(iScsiHbaName=""): # vim.host.IscsiManager.queryBoundVnics
            # throws vim.fault.IscsiFault, vim.fault.NotFound
            return [ vim.host.IscsiManager.IscsiPortInfo() ]

         def queryCandidateNics(iScsiHbaName=""): # vim.host.IscsiManager.queryCandidateNics
            # throws vim.fault.IscsiFault, vim.fault.NotFound
            return [ vim.host.IscsiManager.IscsiPortInfo() ]

         def bindVnic(iScsiHbaName="", vnicDevice=""): # vim.host.IscsiManager.bindVnic
            # throws vim.fault.IscsiFaultVnicAlreadyBound, vim.fault.IscsiFaultVnicHasNoUplinks, vim.fault.IscsiFaultVnicHasMultipleUplinks, vim.fault.IscsiFaultVnicHasWrongUplink, vim.fault.IscsiFaultVnicNotFound, vim.fault.IscsiFaultInvalidVnic, vim.fault.PlatformConfigFault, vim.fault.IscsiFault, vim.fault.NotFound
            return None

         def unbindVnic(iScsiHbaName="", vnicDevice="", force=False): # vim.host.IscsiManager.unbindVnic
            # throws vim.fault.IscsiFaultVnicNotBound, vim.fault.IscsiFaultVnicHasActivePaths, vim.fault.IscsiFaultVnicIsLastPath, vim.fault.PlatformConfigFault, vim.fault.IscsiFault, vim.fault.NotFound
            return None

         def queryMigrationDependencies(pnicDevice=[ "" ]): # vim.host.IscsiManager.queryMigrationDependencies
            return vim.host.IscsiManager.IscsiMigrationDependency()

         class IscsiStatus(vmodl.DynamicData): # vim.host.IscsiManager.IscsiStatus
            reason = [ vmodl.MethodFault() ]

         class IscsiPortInfo(vmodl.DynamicData): # vim.host.IscsiManager.IscsiPortInfo
            vnicDevice = ""
            vnic = vim.host.VirtualNic()
            pnicDevice = ""
            pnic = vim.host.PhysicalNic()
            switchName = ""
            switchUuid = ""
            portgroupName = ""
            portgroupKey = ""
            portKey = ""
            opaqueNetworkId = ""
            opaqueNetworkType = ""
            opaqueNetworkName = ""
            externalId = ""
            complianceStatus = vim.host.IscsiManager.IscsiStatus()
            pathStatus = ""

            class PathStatus(Enum): # vim.host.IscsiManager.IscsiPortInfo.PathStatus
               notUsed = 0
               active = 1
               standBy = 2
               lastActive = 3

         class IscsiDependencyEntity(vmodl.DynamicData): # vim.host.IscsiManager.IscsiDependencyEntity
            pnicDevice = ""
            vnicDevice = ""
            vmhbaName = ""

         class IscsiMigrationDependency(vmodl.DynamicData): # vim.host.IscsiManager.IscsiMigrationDependency
            migrationAllowed = False
            disallowReason = vim.host.IscsiManager.IscsiStatus()
            dependency = [ vim.host.IscsiManager.IscsiDependencyEntity() ]

      class KernelModuleSystem(vmodl.ManagedObject): # vim.host.KernelModuleSystem

         def queryModules(): # vim.host.KernelModuleSystem.queryModules
            return [ vim.host.KernelModuleSystem.ModuleInfo() ]

         def updateModuleOptionString(name="", options=""): # vim.host.KernelModuleSystem.updateModuleOptionString
            # throws vim.fault.NotFound
            return None

         def queryConfiguredModuleOptionString(name=""): # vim.host.KernelModuleSystem.queryConfiguredModuleOptionString
            # throws vim.fault.NotFound
            return ""

         class ModuleInfo(vmodl.DynamicData): # vim.host.KernelModuleSystem.ModuleInfo
            id = 0
            name = ""
            version = ""
            filename = ""
            optionString = ""
            loaded = False
            enabled = False
            useCount = 0
            readOnlySection = vim.host.KernelModuleSystem.ModuleInfo.SectionInfo()
            writableSection = vim.host.KernelModuleSystem.ModuleInfo.SectionInfo()
            textSection = vim.host.KernelModuleSystem.ModuleInfo.SectionInfo()
            dataSection = vim.host.KernelModuleSystem.ModuleInfo.SectionInfo()
            bssSection = vim.host.KernelModuleSystem.ModuleInfo.SectionInfo()

            class SectionInfo(vmodl.DynamicData): # vim.host.KernelModuleSystem.ModuleInfo.SectionInfo
               address = 0
               length = 0

      class LicenseSpec(vmodl.DynamicData): # vim.host.LicenseSpec
         source = vim.LicenseManager.LicenseSource()
         editionKey = ""
         disabledFeatureKey = [ "" ]
         enabledFeatureKey = [ "" ]

      class LinkDiscoveryProtocolConfig(vmodl.DynamicData): # vim.host.LinkDiscoveryProtocolConfig
         protocol = ""
         operation = ""

         class ProtocolType(Enum): # vim.host.LinkDiscoveryProtocolConfig.ProtocolType
            cdp = 0
            lldp = 1

         class OperationType(Enum): # vim.host.LinkDiscoveryProtocolConfig.OperationType
            none = 0
            listen = 1
            advertise = 2
            both = 3

      class LocalAccountManager(vmodl.ManagedObject): # vim.host.LocalAccountManager

         def createUser(user=vim.host.LocalAccountManager.AccountSpecification()): # vim.host.LocalAccountManager.createUser
            # throws vim.fault.AlreadyExists
            return None

         def updateUser(user=vim.host.LocalAccountManager.AccountSpecification()): # vim.host.LocalAccountManager.updateUser
            # throws vim.fault.UserNotFound, vim.fault.AlreadyExists
            return None

         def createGroup(group=vim.host.LocalAccountManager.AccountSpecification()): # vim.host.LocalAccountManager.createGroup
            # throws vim.fault.AlreadyExists
            return None

         def removeUser(userName=""): # vim.host.LocalAccountManager.removeUser
            # throws vim.fault.UserNotFound
            return None

         def removeGroup(groupName=""): # vim.host.LocalAccountManager.removeGroup
            # throws vim.fault.UserNotFound
            return None

         def assignUserToGroup(user="", group=""): # vim.host.LocalAccountManager.assignUserToGroup
            # throws vim.fault.UserNotFound, vim.fault.AlreadyExists
            return None

         def unassignUserFromGroup(user="", group=""): # vim.host.LocalAccountManager.unassignUserFromGroup
            # throws vim.fault.UserNotFound
            return None

         def changePassword(user="", oldPassword="", newPassword=""): # vim.host.LocalAccountManager.changePassword
            # throws vim.fault.InvalidLogin
            return None

         class AccountSpecification(vmodl.DynamicData): # vim.host.LocalAccountManager.AccountSpecification
            id = ""
            password = ""
            description = ""

         class PosixAccountSpecification(vim.host.LocalAccountManager.AccountSpecification): # vim.host.LocalAccountManager.PosixAccountSpecification
            posixId = 0
            shellAccess = False

      class LocalAuthentication(vim.host.AuthenticationStore): # vim.host.LocalAuthentication
         pass

      class LocalAuthenticationInfo(vim.host.AuthenticationStoreInfo): # vim.host.LocalAuthenticationInfo
         pass

      class LocalFileSystemVolume(vim.host.FileSystemVolume): # vim.host.LocalFileSystemVolume
         device = ""

         class Specification(vmodl.DynamicData): # vim.host.LocalFileSystemVolume.Specification
            device = ""
            localPath = ""

      class LowLevelProvisioningManager(object): # (unknown name)

         class VmRecoveryInfo(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.VmRecoveryInfo
            version = ""
            biosUUID = ""
            instanceUUID = ""
            ftInfo = vim.vm.FaultToleranceConfigInfo()

         class VmMigrationStatus(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.VmMigrationStatus
            migrationId = 0
            type = ""
            source = False
            consideredSuccessful = False

         class ReloadTarget(Enum): # vim.host.LowLevelProvisioningManager.ReloadTarget
            currentConfig = 0
            snapshotConfig = 1

         class DiskLayoutSpec(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.DiskLayoutSpec
            controllerType = vmodl.TypeName()
            busNumber = 0
            unitNumber = 0
            srcFilename = ""
            dstFilename = ""

         class SnapshotLayoutSpec(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.SnapshotLayoutSpec
            id = 0
            srcFilename = ""
            dstFilename = ""
            disk = [ vim.host.LowLevelProvisioningManager.DiskLayoutSpec() ]

         class FileType(Enum): # vim.host.LowLevelProvisioningManager.FileType
            File = 0
            VirtualDisk = 1
            Directory = 2

         class FileReserveSpec(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.FileReserveSpec
            baseName = ""
            parentDir = ""
            fileType = ""
            storageProfile = ""

         class FileReserveResult(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.FileReserveResult
            baseName = ""
            parentDir = ""
            reservedName = ""

         class FileDeleteSpec(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.FileDeleteSpec
            fileName = ""
            fileType = ""

         class FileDeleteResult(vmodl.DynamicData): # vim.host.LowLevelProvisioningManager.FileDeleteResult
            fileName = ""
            fault = vmodl.MethodFault()

      class MaintenanceSpec(vmodl.DynamicData): # vim.host.MaintenanceSpec
         vsanMode = vim.vsan.host.DecommissionMode()
         purpose = ""

         class Purpose(Enum): # vim.host.MaintenanceSpec.Purpose
            hostUpgrade = 0

      class MemoryManagerSystem(vim.ExtensibleManagedObject): # vim.host.MemoryManagerSystem
         consoleReservationInfo = vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo()
         virtualMachineReservationInfo = vim.host.MemoryManagerSystem.VirtualMachineReservationInfo()

         def reconfigureServiceConsoleReservation(cfgBytes=0): # vim.host.MemoryManagerSystem.reconfigureServiceConsoleReservation
            return None

         def reconfigureVirtualMachineReservation(spec=vim.host.MemoryManagerSystem.VirtualMachineReservationSpec()): # vim.host.MemoryManagerSystem.reconfigureVirtualMachineReservation
            return None

         class ServiceConsoleReservationInfo(vmodl.DynamicData): # vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo
            serviceConsoleReservedCfg = 0
            serviceConsoleReserved = 0
            unreserved = 0

         class VirtualMachineReservationInfo(vmodl.DynamicData): # vim.host.MemoryManagerSystem.VirtualMachineReservationInfo
            virtualMachineMin = 0
            virtualMachineMax = 0
            virtualMachineReserved = 0
            allocationPolicy = ""

            class AllocationPolicy(Enum): # vim.host.MemoryManagerSystem.VirtualMachineReservationInfo.AllocationPolicy
               swapNone = 0
               swapSome = 1
               swapMost = 2

         class VirtualMachineReservationSpec(vmodl.DynamicData): # vim.host.MemoryManagerSystem.VirtualMachineReservationSpec
            virtualMachineReserved = 0
            allocationPolicy = ""

      class MemorySpec(vmodl.DynamicData): # vim.host.MemorySpec
         serviceConsoleReservation = 0

      class MessageBusProxy(vmodl.ManagedObject): # vim.host.MessageBusProxy
         pass

      class MountInfo(vmodl.DynamicData): # vim.host.MountInfo
         path = ""
         accessMode = ""
         mounted = False
         accessible = False
         inaccessibleReason = ""

         class AccessMode(Enum): # vim.host.MountInfo.AccessMode
            readWrite = 0
            readOnly = 1

         class InaccessibleReason(Enum): # vim.host.MountInfo.InaccessibleReason
            AllPathsDown_Start = 0
            AllPathsDown_Timeout = 1
            PermanentDeviceLoss = 2

      class MultipathInfo(vmodl.DynamicData): # vim.host.MultipathInfo
         lun = [ vim.host.MultipathInfo.LogicalUnit() ]

         class PathState(Enum): # vim.host.MultipathInfo.PathState
            standby = 0
            active = 1
            disabled = 2
            dead = 3
            unknown = 4

         class LogicalUnitPolicy(vmodl.DynamicData): # vim.host.MultipathInfo.LogicalUnitPolicy
            policy = ""

         class HppLogicalUnitPolicy(vim.host.MultipathInfo.LogicalUnitPolicy): # vim.host.MultipathInfo.HppLogicalUnitPolicy
            bytes = 0
            iops = 0
            path = ""
            latencyEvalTime = 0
            samplingIosPerPath = 0

         class LogicalUnitStorageArrayTypePolicy(vmodl.DynamicData): # vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy
            policy = ""

         class FixedLogicalUnitPolicy(vim.host.MultipathInfo.LogicalUnitPolicy): # vim.host.MultipathInfo.FixedLogicalUnitPolicy
            prefer = ""

         class LogicalUnit(vmodl.DynamicData): # vim.host.MultipathInfo.LogicalUnit
            key = ""
            id = ""
            lun = vim.host.ScsiLun()
            path = [ vim.host.MultipathInfo.Path() ]
            policy = vim.host.MultipathInfo.LogicalUnitPolicy()
            storageArrayTypePolicy = vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy()

         class Path(vmodl.DynamicData): # vim.host.MultipathInfo.Path
            key = ""
            name = ""
            pathState = ""
            state = ""
            isWorkingPath = False
            adapter = vim.host.HostBusAdapter()
            lun = vim.host.MultipathInfo.LogicalUnit()
            transport = vim.host.TargetTransport()

      class MultipathStateInfo(vmodl.DynamicData): # vim.host.MultipathStateInfo
         path = [ vim.host.MultipathStateInfo.Path() ]

         class Path(vmodl.DynamicData): # vim.host.MultipathStateInfo.Path
            name = ""
            pathState = ""

      class NasVolume(vim.host.FileSystemVolume): # vim.host.NasVolume
         remoteHost = ""
         remotePath = ""
         userName = ""
         remoteHostNames = [ "" ]
         securityType = ""
         protocolEndpoint = False

         class UserInfo(vmodl.DynamicData): # vim.host.NasVolume.UserInfo
            user = ""

         class SecurityType(Enum): # vim.host.NasVolume.SecurityType
            AUTH_SYS = 0
            SEC_KRB5 = 1
            SEC_KRB5I = 2

         class Specification(vmodl.DynamicData): # vim.host.NasVolume.Specification
            remoteHost = ""
            remotePath = ""
            localPath = ""
            accessMode = ""
            type = ""
            userName = ""
            password = ""
            remoteHostNames = [ "" ]
            securityType = ""

         class Config(vmodl.DynamicData): # vim.host.NasVolume.Config
            changeOperation = ""
            spec = vim.host.NasVolume.Specification()

      class NatService(vmodl.DynamicData): # vim.host.NatService
         key = ""
         spec = vim.host.NatService.Specification()

         class PortForwardSpecification(vmodl.DynamicData): # vim.host.NatService.PortForwardSpecification
            type = ""
            name = ""
            hostPort = 0
            guestPort = 0
            guestIpAddress = ""

         class NameServiceSpec(vmodl.DynamicData): # vim.host.NatService.NameServiceSpec
            dnsAutoDetect = False
            dnsPolicy = ""
            dnsRetries = 0
            dnsTimeout = 0
            dnsNameServer = [ "" ]
            nbdsTimeout = 0
            nbnsRetries = 0
            nbnsTimeout = 0

         class Specification(vmodl.DynamicData): # vim.host.NatService.Specification
            virtualSwitch = ""
            activeFtp = False
            allowAnyOui = False
            configPort = False
            ipGatewayAddress = ""
            udpTimeout = 0
            portForward = [ vim.host.NatService.PortForwardSpecification() ]
            nameService = vim.host.NatService.NameServiceSpec()

         class Config(vmodl.DynamicData): # vim.host.NatService.Config
            changeOperation = ""
            key = ""
            spec = vim.host.NatService.Specification()

      class NetCapabilities(vmodl.DynamicData): # vim.host.NetCapabilities
         canSetPhysicalNicLinkSpeed = False
         supportsNicTeaming = False
         nicTeamingPolicy = [ "" ]
         supportsVlan = False
         usesServiceConsoleNic = False
         supportsNetworkHints = False
         maxPortGroupsPerVswitch = 0
         vswitchConfigSupported = False
         vnicConfigSupported = False
         ipRouteConfigSupported = False
         dnsConfigSupported = False
         dhcpOnVnicSupported = False
         ipV6Supported = False

      class NetOffloadCapabilities(vmodl.DynamicData): # vim.host.NetOffloadCapabilities
         csumOffload = False
         tcpSegmentation = False
         zeroCopyXmit = False

      class NetStackInstance(vmodl.DynamicData): # vim.host.NetStackInstance
         key = ""
         name = ""
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         requestedMaxNumberOfConnections = 0
         congestionControlAlgorithm = ""
         ipV6Enabled = False
         routeTableConfig = vim.host.IpRouteTableConfig()

         class SystemStackKey(Enum): # vim.host.NetStackInstance.SystemStackKey
            defaultTcpipStack = 0
            vmotion = 1
            vSphereProvisioning = 2

         class CongestionControlAlgorithmType(Enum): # vim.host.NetStackInstance.CongestionControlAlgorithmType
            newreno = 0
            cubic = 1

      class NetworkInfo(vmodl.DynamicData): # vim.host.NetworkInfo
         vswitch = [ vim.host.VirtualSwitch() ]
         proxySwitch = [ vim.host.HostProxySwitch() ]
         portgroup = [ vim.host.PortGroup() ]
         pnic = [ vim.host.PhysicalNic() ]
         rdmaDevice = [ vim.host.RdmaDevice() ]
         vnic = [ vim.host.VirtualNic() ]
         consoleVnic = [ vim.host.VirtualNic() ]
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         consoleIpRouteConfig = vim.host.IpRouteConfig()
         routeTableInfo = vim.host.IpRouteTableInfo()
         dhcp = [ vim.host.DhcpService() ]
         nat = [ vim.host.NatService() ]
         ipV6Enabled = False
         atBootIpV6Enabled = False
         netStackInstance = [ vim.host.NetStackInstance() ]
         opaqueSwitch = [ vim.host.OpaqueSwitch() ]
         opaqueNetwork = [ vim.host.OpaqueNetworkInfo() ]
         nsxTransportNodeId = ""

      class NetworkPolicy(vmodl.DynamicData): # vim.host.NetworkPolicy
         security = vim.host.NetworkPolicy.SecurityPolicy()
         nicTeaming = vim.host.NetworkPolicy.NicTeamingPolicy()
         offloadPolicy = vim.host.NetOffloadCapabilities()
         shapingPolicy = vim.host.NetworkPolicy.TrafficShapingPolicy()

         class SecurityPolicy(vmodl.DynamicData): # vim.host.NetworkPolicy.SecurityPolicy
            allowPromiscuous = False
            macChanges = False
            forgedTransmits = False

         class TrafficShapingPolicy(vmodl.DynamicData): # vim.host.NetworkPolicy.TrafficShapingPolicy
            enabled = False
            averageBandwidth = 0
            peakBandwidth = 0
            burstSize = 0

         class NicFailureCriteria(vmodl.DynamicData): # vim.host.NetworkPolicy.NicFailureCriteria
            checkSpeed = ""
            speed = 0
            checkDuplex = False
            fullDuplex = False
            checkErrorPercent = False
            percentage = 0
            checkBeacon = False

         class NicOrderPolicy(vmodl.DynamicData): # vim.host.NetworkPolicy.NicOrderPolicy
            activeNic = [ "" ]
            standbyNic = [ "" ]

         class NicTeamingPolicy(vmodl.DynamicData): # vim.host.NetworkPolicy.NicTeamingPolicy
            policy = ""
            reversePolicy = False
            notifySwitches = False
            rollingOrder = False
            failureCriteria = vim.host.NetworkPolicy.NicFailureCriteria()
            nicOrder = vim.host.NetworkPolicy.NicOrderPolicy()

      class NtpConfig(vmodl.DynamicData): # vim.host.NtpConfig
         server = [ "" ]
         configFile = [ "" ]

      class NumaInfo(vmodl.DynamicData): # vim.host.NumaInfo
         type = ""
         numNodes = 0
         numaNode = [ vim.host.NumaNode() ]

      class NumaNode(vmodl.DynamicData): # vim.host.NumaNode
         typeId = 0x00
         cpuID = [ 0 ]
         memoryRangeBegin = 0
         memoryRangeLength = 0
         pciId = [ "" ]

      class NumericSensorInfo(vmodl.DynamicData): # vim.host.NumericSensorInfo
         name = ""
         healthState = vim.ElementDescription()
         currentReading = 0
         unitModifier = 0
         baseUnits = ""
         rateUnits = ""
         sensorType = ""
         id = ""
         timeStamp = ""

         class HealthState(Enum): # vim.host.NumericSensorInfo.HealthState
            unknown = 0
            green = 1
            yellow = 2
            red = 3

         class SensorType(Enum): # vim.host.NumericSensorInfo.SensorType
            fan = 0
            power = 1
            temperature = 2
            voltage = 3
            other = 4
            processor = 5
            memory = 6
            storage = 7
            systemBoard = 8
            battery = 9
            bios = 10
            cable = 11
            watchdog = 12

      class NvdimmSystem(vmodl.ManagedObject): # vim.host.NvdimmSystem
         nvdimmSystemInfo = vim.host.NvdimmSystem.NvdimmSystemInfo()

         def createNamespace(createSpec=vim.host.NvdimmSystem.NamespaceCreateSpec()): # vim.host.NvdimmSystem.createNamespace
            # throws vim.fault.InvalidHostState, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Task()

         def createPMemNamespace(createSpec=vim.host.NvdimmSystem.PMemNamespaceCreateSpec()): # vim.host.NvdimmSystem.createPMemNamespace
            # throws vim.fault.InvalidHostState, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Task()

         def deleteNamespace(deleteSpec=vim.host.NvdimmSystem.NamespaceDeleteSpec()): # vim.host.NvdimmSystem.deleteNamespace
            # throws vim.fault.NotFound, vim.fault.InvalidHostState, vim.fault.HostConfigFault
            return vim.Task()

         def deleteBlockNamespaces(): # vim.host.NvdimmSystem.deleteBlockNamespaces
            # throws vim.fault.NotFound, vim.fault.InvalidHostState, vim.fault.HostConfigFault
            return vim.Task()

         class RangeType(Enum): # vim.host.NvdimmSystem.RangeType
            volatileRange = 0
            persistentRange = 1
            controlRange = 2
            blockRange = 3
            volatileVirtualDiskRange = 4
            volatileVirtualCDRange = 5
            persistentVirtualDiskRange = 6
            persistentVirtualCDRange = 7

         class NamespaceType(Enum): # vim.host.NvdimmSystem.NamespaceType
            blockNamespace = 0
            persistentNamespace = 1

         class HealthInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.HealthInfo
            healthStatus = ""
            healthInformation = ""
            stateFlagInfo = [ "" ]
            dimmTemperature = 0
            dimmTemperatureThreshold = 0
            spareBlocksPercentage = 0
            spareBlockThreshold = 0
            dimmLifespanPercentage = 0
            esTemperature = 0
            esTemperatureThreshold = 0
            esLifespanPercentage = 0

            class StateFlag(Enum): # vim.host.NvdimmSystem.HealthInfo.StateFlag
               normal = 0
               error = 1

         class RegionInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.RegionInfo
            regionId = 0
            setId = 0
            rangeType = ""
            startAddr = 0
            size = 0
            offset = 0

         class Summary(vmodl.DynamicData): # vim.host.NvdimmSystem.Summary
            numDimms = 0
            healthStatus = ""
            totalCapacity = 0
            persistentCapacity = 0
            blockCapacity = 0
            availableCapacity = 0
            numInterleavesets = 0
            numNamespaces = 0

         class DimmInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.DimmInfo
            dimmHandle = 0
            healthInfo = vim.host.NvdimmSystem.HealthInfo()
            totalCapacity = 0
            persistentCapacity = 0
            availablePersistentCapacity = 0
            volatileCapacity = 0
            availableVolatileCapacity = 0
            blockCapacity = 0
            regionInfo = [ vim.host.NvdimmSystem.RegionInfo() ]
            representationString = ""

         class InterleaveSetInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.InterleaveSetInfo
            setId = 0
            rangeType = ""
            baseAddress = 0
            size = 0
            availableSize = 0
            deviceList = [ 0 ]
            state = ""

            class InterleaveSetState(Enum): # vim.host.NvdimmSystem.InterleaveSetInfo.InterleaveSetState
               invalid = 0
               active = 1

         class Guid(vmodl.DynamicData): # vim.host.NvdimmSystem.Guid
            uuid = ""

         class NamespaceInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.NamespaceInfo
            uuid = ""
            friendlyName = ""
            blockSize = 0
            blockCount = 0
            type = ""
            namespaceHealthStatus = ""
            locationID = 0
            state = ""

            class NamespaceHealthStatus(Enum): # vim.host.NvdimmSystem.NamespaceInfo.NamespaceHealthStatus
               normal = 0
               missing = 1
               labelMissing = 2
               interleaveBroken = 3
               labelInconsistent = 4
               bttCorrupt = 5
               badBlockSize = 6

            class NamespaceState(Enum): # vim.host.NvdimmSystem.NamespaceInfo.NamespaceState
               invalid = 0
               notInUse = 1
               inUse = 2

         class NamespaceDetails(vmodl.DynamicData): # vim.host.NvdimmSystem.NamespaceDetails
            uuid = ""
            friendlyName = ""
            size = 0
            type = ""
            namespaceHealthStatus = ""
            interleavesetID = 0
            state = ""

            class NamespaceHealthStatus(Enum): # vim.host.NvdimmSystem.NamespaceDetails.NamespaceHealthStatus
               normal = 0
               missing = 1
               labelMissing = 2
               interleaveBroken = 3
               labelInconsistent = 4

            class NamespaceState(Enum): # vim.host.NvdimmSystem.NamespaceDetails.NamespaceState
               invalid = 0
               notInUse = 1
               inUse = 2

         class NamespaceCreateSpec(vmodl.DynamicData): # vim.host.NvdimmSystem.NamespaceCreateSpec
            friendlyName = ""
            blockSize = 0
            blockCount = 0
            type = ""
            locationID = 0

         class PMemNamespaceCreateSpec(vmodl.DynamicData): # vim.host.NvdimmSystem.PMemNamespaceCreateSpec
            friendlyName = ""
            size = 0
            interleavesetID = 0

         class NamespaceDeleteSpec(vmodl.DynamicData): # vim.host.NvdimmSystem.NamespaceDeleteSpec
            uuid = ""

         class NvdimmSystemInfo(vmodl.DynamicData): # vim.host.NvdimmSystem.NvdimmSystemInfo
            summary = vim.host.NvdimmSystem.Summary()
            dimms = [ 0 ]
            dimmInfo = [ vim.host.NvdimmSystem.DimmInfo() ]
            interleaveSet = [ 0 ]
            iSetInfo = [ vim.host.NvdimmSystem.InterleaveSetInfo() ]
            namespace = [ vim.host.NvdimmSystem.Guid() ]
            nsInfo = [ vim.host.NvdimmSystem.NamespaceInfo() ]
            nsDetails = [ vim.host.NvdimmSystem.NamespaceDetails() ]

      class NvmeController(vmodl.DynamicData): # vim.host.NvmeController
         key = ""
         controllerNumber = 0
         subnqn = ""
         name = ""
         associatedAdapter = vim.host.HostBusAdapter()
         transportType = ""
         fusedOperationSupported = False
         numberOfQueues = 0
         queueSize = 0
         attachedNamespace = [ vim.host.NvmeNamespace() ]
         vendorId = ""
         model = ""
         serialNumber = ""
         firmwareVersion = ""

      class NvmeDisconnectSpec(vmodl.DynamicData): # vim.host.NvmeDisconnectSpec
         hbaName = ""
         subnqn = ""
         controllerNumber = 0

      class NvmeDiscoveryLog(vmodl.DynamicData): # vim.host.NvmeDiscoveryLog
         entry = [ vim.host.NvmeDiscoveryLog.Entry() ]
         complete = False

         class SubsystemType(Enum): # vim.host.NvmeDiscoveryLog.SubsystemType
            discovery = 0
            nvm = 1

         class TransportRequirements(Enum): # vim.host.NvmeDiscoveryLog.TransportRequirements
            secureChannelRequired = 0
            secureChannelNotRequired = 1
            requirementsNotSpecified = 2

         class Entry(vmodl.DynamicData): # vim.host.NvmeDiscoveryLog.Entry
            subnqn = ""
            subsystemType = ""
            subsystemPortId = 0
            controllerId = 0
            adminQueueMaxSize = 0
            transportParameters = vim.host.NvmeTransportParameters()
            transportRequirements = ""
            connected = False

      class NvmeNamespace(vmodl.DynamicData): # vim.host.NvmeNamespace
         key = ""
         name = ""
         id = 0
         blockSize = 0
         capacityInBlocks = 0

      class NvmeSpec(vmodl.DynamicData): # vim.host.NvmeSpec
         hbaName = ""
         transportParameters = vim.host.NvmeTransportParameters()

      class NvmeTopology(vmodl.DynamicData): # vim.host.NvmeTopology
         adapter = [ vim.host.NvmeTopology.Interface() ]

         class Interface(vmodl.DynamicData): # vim.host.NvmeTopology.Interface
            key = ""
            adapter = vim.host.HostBusAdapter()
            connectedController = [ vim.host.NvmeController() ]

      class NvmeTransportParameters(vmodl.DynamicData): # vim.host.NvmeTransportParameters

         class NvmeAddressFamily(Enum): # vim.host.NvmeTransportParameters.NvmeAddressFamily
            ipv4 = 0
            ipv6 = 1
            infiniBand = 2
            fc = 3
            loopback = 4
            unknown = 5

      class NvmeTransportType(Enum): # vim.host.NvmeTransportType
         pcie = 0
         fibreChannel = 1
         rdma = 2
         loopback = 3
         unsupported = 4

      class OpaqueSwitch(vmodl.DynamicData): # vim.host.OpaqueSwitch
         key = ""
         name = ""
         pnic = [ vim.host.PhysicalNic() ]
         pnicZone = [ vim.host.OpaqueSwitch.PhysicalNicZone() ]
         status = ""
         vtep = [ vim.host.VirtualNic() ]
         extraConfig = [ vim.option.OptionValue() ]
         featureCapability = [ vim.host.FeatureCapability() ]

         class OpaqueSwitchState(Enum): # vim.host.OpaqueSwitch.OpaqueSwitchState
            up = 0
            warning = 1
            down = 2
            maintenance = 3

         class PhysicalNicZone(vmodl.DynamicData): # vim.host.OpaqueSwitch.PhysicalNicZone
            key = ""
            pnicDevice = [ "" ]

      class PMemVolume(vim.host.FileSystemVolume): # vim.host.PMemVolume
         uuid = ""
         version = ""

      class ParallelScsiHba(vim.host.HostBusAdapter): # vim.host.ParallelScsiHba
         pass

      class PatchManager(vmodl.ManagedObject): # vim.host.PatchManager

         def Check(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.Check
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Scan(repository=vim.host.PatchManager.Locator(), updateID=[ "" ] or None): # vim.host.PatchManager.Scan
            # throws vmodl.fault.RequestCanceled, vim.fault.PatchMetadataInvalid, vim.fault.PlatformConfigFault
            return vim.Task()

         def ScanV2(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.ScanV2
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Stage(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, vibUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.Stage
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Install(repository=vim.host.PatchManager.Locator(), updateID="", force=False or None): # vim.host.PatchManager.Install
            # throws vim.fault.PatchMetadataInvalid, vim.fault.PatchBinariesNotFound, vim.fault.PatchNotApplicable, vim.fault.NoDiskSpace, vim.fault.PatchInstallFailed, vim.fault.RebootRequired, vim.fault.InvalidState, vim.fault.TaskInProgress
            return vim.Task()

         def InstallV2(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, vibUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.InstallV2
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Uninstall(bulletinIds=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.Uninstall
            # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Query(spec=vim.host.PatchManager.PatchManagerOperationSpec() or None): # vim.host.PatchManager.Query
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         class Result(vmodl.DynamicData): # vim.host.PatchManager.Result
            version = ""
            status = [ vim.host.PatchManager.Status() ]
            xmlResult = ""

         class Status(vmodl.DynamicData): # vim.host.PatchManager.Status
            id = ""
            applicable = False
            reason = [ "" ]
            integrity = ""
            installed = False
            installState = [ "" ]
            prerequisitePatch = [ vim.host.PatchManager.Status.PrerequisitePatch() ]
            restartRequired = False
            reconnectRequired = False
            vmOffRequired = False
            supersededPatchIds = [ "" ]

            class Reason(Enum): # vim.host.PatchManager.Status.Reason
               obsoleted = 0
               missingPatch = 1
               missingLib = 2
               hasDependentPatch = 3
               conflictPatch = 4
               conflictLib = 5

            class Integrity(Enum): # vim.host.PatchManager.Status.Integrity
               validated = 0
               keyNotFound = 1
               keyRevoked = 2
               keyExpired = 3
               digestMismatch = 4
               notEnoughSignatures = 5
               validationError = 6

            class InstallState(Enum): # vim.host.PatchManager.Status.InstallState
               hostRestarted = 0
               imageActive = 1

            class PrerequisitePatch(vmodl.DynamicData): # vim.host.PatchManager.Status.PrerequisitePatch
               id = ""
               installState = [ "" ]

         class Locator(vmodl.DynamicData): # vim.host.PatchManager.Locator
            url = ""
            proxy = ""

         class PatchManagerOperationSpec(vmodl.DynamicData): # vim.host.PatchManager.PatchManagerOperationSpec
            proxy = ""
            port = 0
            userName = ""
            password = ""
            cmdOption = ""

      class PathSelectionPolicyOption(vmodl.DynamicData): # vim.host.PathSelectionPolicyOption
         policy = vim.ElementDescription()

      class PciDevice(vmodl.DynamicData): # vim.host.PciDevice
         id = ""
         classId = 0
         bus = 0x00
         slot = 0x00
         function = 0x00
         vendorId = 0
         subVendorId = 0
         vendorName = ""
         deviceId = 0
         subDeviceId = 0
         parentBridge = ""
         deviceName = ""

      class PciPassthruConfig(vmodl.DynamicData): # vim.host.PciPassthruConfig
         id = ""
         passthruEnabled = False
         applyNow = False

      class PciPassthruInfo(vmodl.DynamicData): # vim.host.PciPassthruInfo
         id = ""
         dependentDevice = ""
         passthruEnabled = False
         passthruCapable = False
         passthruActive = False

      class PciPassthruSystem(vim.ExtensibleManagedObject): # vim.host.PciPassthruSystem
         pciPassthruInfo = [ vim.host.PciPassthruInfo() ]
         sriovDevicePoolInfo = [ vim.host.SriovDevicePoolInfo() ]

         def refresh(): # vim.host.PciPassthruSystem.refresh
            return None

         def updatePassthruConfig(config=[ vim.host.PciPassthruConfig() ]): # vim.host.PciPassthruSystem.updatePassthruConfig
            # throws vim.fault.HostConfigFault
            return None

      class PcieHba(vim.host.HostBusAdapter): # vim.host.PcieHba
         pass

      class PersistentMemoryInfo(vmodl.DynamicData): # vim.host.PersistentMemoryInfo
         capacityInMB = 0
         volumeUUID = ""

      class PhysicalNic(vmodl.DynamicData): # vim.host.PhysicalNic
         key = ""
         device = ""
         pci = ""
         driver = ""
         linkSpeed = vim.host.PhysicalNic.LinkSpeedDuplex()
         validLinkSpecification = [ vim.host.PhysicalNic.LinkSpeedDuplex() ]
         spec = vim.host.PhysicalNic.Specification()
         wakeOnLanSupported = False
         mac = ""
         fcoeConfiguration = vim.host.FcoeConfig()
         vmDirectPathGen2Supported = False
         vmDirectPathGen2SupportedMode = ""
         resourcePoolSchedulerAllowed = False
         resourcePoolSchedulerDisallowedReason = [ "" ]
         autoNegotiateSupported = False
         enhancedNetworkingStackSupported = False
         ensInterruptSupported = False
         rdmaDevice = vim.host.RdmaDevice()

         class Specification(vmodl.DynamicData): # vim.host.PhysicalNic.Specification
            ip = vim.host.IpConfig()
            linkSpeed = vim.host.PhysicalNic.LinkSpeedDuplex()
            enableEnhancedNetworkingStack = False
            ensInterruptEnabled = False

         class Config(vmodl.DynamicData): # vim.host.PhysicalNic.Config
            device = ""
            spec = vim.host.PhysicalNic.Specification()

         class LinkSpeedDuplex(vmodl.DynamicData): # vim.host.PhysicalNic.LinkSpeedDuplex
            speedMb = 0
            duplex = False

         class NetworkHint(vmodl.DynamicData): # vim.host.PhysicalNic.NetworkHint
            device = ""
            subnet = [ vim.host.PhysicalNic.NetworkHint.IpNetwork() ]
            network = [ vim.host.PhysicalNic.NetworkHint.NamedNetwork() ]
            connectedSwitchPort = vim.host.PhysicalNic.CdpInfo()
            lldpInfo = vim.host.PhysicalNic.LldpInfo()

            class HintElement(vmodl.DynamicData): # vim.host.PhysicalNic.NetworkHint.HintElement
               vlanId = 0

            class IpNetwork(vim.host.PhysicalNic.NetworkHint.HintElement): # vim.host.PhysicalNic.NetworkHint.IpNetwork
               ipSubnet = ""

            class NamedNetwork(vim.host.PhysicalNic.NetworkHint.HintElement): # vim.host.PhysicalNic.NetworkHint.NamedNetwork
               network = ""

         class CdpDeviceCapability(vmodl.DynamicData): # vim.host.PhysicalNic.CdpDeviceCapability
            router = False
            transparentBridge = False
            sourceRouteBridge = False
            networkSwitch = False
            host = False
            igmpEnabled = False
            repeater = False

         class CdpInfo(vmodl.DynamicData): # vim.host.PhysicalNic.CdpInfo
            cdpVersion = 0
            timeout = 0
            ttl = 0
            samples = 0
            devId = ""
            address = ""
            portId = ""
            deviceCapability = vim.host.PhysicalNic.CdpDeviceCapability()
            softwareVersion = ""
            hardwarePlatform = ""
            ipPrefix = ""
            ipPrefixLen = 0
            vlan = 0
            fullDuplex = False
            mtu = 0
            systemName = ""
            systemOID = ""
            mgmtAddr = ""
            location = ""

         class LldpInfo(vmodl.DynamicData): # vim.host.PhysicalNic.LldpInfo
            chassisId = ""
            portId = ""
            timeToLive = 0
            parameter = [ vmodl.KeyAnyValue() ]

         class VmDirectPathGen2SupportedMode(Enum): # vim.host.PhysicalNic.VmDirectPathGen2SupportedMode
            upt = 0

         class ResourcePoolSchedulerDisallowedReason(Enum): # vim.host.PhysicalNic.ResourcePoolSchedulerDisallowedReason
            userOptOut = 0
            hardwareUnsupported = 1

      class PlugStoreTopology(vmodl.DynamicData): # vim.host.PlugStoreTopology
         adapter = [ vim.host.PlugStoreTopology.Adapter() ]
         path = [ vim.host.PlugStoreTopology.Path() ]
         target = [ vim.host.PlugStoreTopology.Target() ]
         device = [ vim.host.PlugStoreTopology.Device() ]
         plugin = [ vim.host.PlugStoreTopology.Plugin() ]

         class Adapter(vmodl.DynamicData): # vim.host.PlugStoreTopology.Adapter
            key = ""
            adapter = vim.host.HostBusAdapter()
            path = [ vim.host.PlugStoreTopology.Path() ]

         class Path(vmodl.DynamicData): # vim.host.PlugStoreTopology.Path
            key = ""
            name = ""
            channelNumber = 0
            targetNumber = 0
            lunNumber = 0
            adapter = vim.host.PlugStoreTopology.Adapter()
            target = vim.host.PlugStoreTopology.Target()
            device = vim.host.PlugStoreTopology.Device()

         class Device(vmodl.DynamicData): # vim.host.PlugStoreTopology.Device
            key = ""
            lun = vim.host.ScsiLun()
            path = [ vim.host.PlugStoreTopology.Path() ]

         class Plugin(vmodl.DynamicData): # vim.host.PlugStoreTopology.Plugin
            key = ""
            name = ""
            device = [ vim.host.PlugStoreTopology.Device() ]
            claimedPath = [ vim.host.PlugStoreTopology.Path() ]

         class Target(vmodl.DynamicData): # vim.host.PlugStoreTopology.Target
            key = ""
            transport = vim.host.TargetTransport()

      class PortGroup(vmodl.DynamicData): # vim.host.PortGroup
         key = ""
         port = [ vim.host.PortGroup.Port() ]
         vswitch = vim.host.VirtualSwitch()
         computedPolicy = vim.host.NetworkPolicy()
         spec = vim.host.PortGroup.Specification()

         class PortConnecteeType(Enum): # vim.host.PortGroup.PortConnecteeType
            virtualMachine = 0
            systemManagement = 1
            host = 2
            unknown = 3

         class Specification(vmodl.DynamicData): # vim.host.PortGroup.Specification
            name = ""
            vlanId = 0
            vswitchName = ""
            policy = vim.host.NetworkPolicy()

         class Config(vmodl.DynamicData): # vim.host.PortGroup.Config
            changeOperation = ""
            spec = vim.host.PortGroup.Specification()

         class Port(vmodl.DynamicData): # vim.host.PortGroup.Port
            key = ""
            mac = [ "" ]
            type = ""

      class PowerSystem(vmodl.ManagedObject): # vim.host.PowerSystem
         capability = vim.host.PowerSystem.Capability()
         info = vim.host.PowerSystem.Info()

         def configurePolicy(key=0): # vim.host.PowerSystem.configurePolicy
            # throws vim.fault.HostConfigFault
            return None

         class PowerPolicy(vmodl.DynamicData): # vim.host.PowerSystem.PowerPolicy
            key = 0
            name = ""
            shortName = ""
            description = ""

         class Capability(vmodl.DynamicData): # vim.host.PowerSystem.Capability
            availablePolicy = [ vim.host.PowerSystem.PowerPolicy() ]

         class Info(vmodl.DynamicData): # vim.host.PowerSystem.Info
            currentPolicy = vim.host.PowerSystem.PowerPolicy()

      class ProtocolEndpoint(vmodl.DynamicData): # vim.host.ProtocolEndpoint
         peType = ""
         type = ""
         uuid = ""
         hostKey = [ vim.HostSystem() ]
         storageArray = ""
         nfsServer = ""
         nfsDir = ""
         nfsServerScope = ""
         nfsServerMajor = ""
         nfsServerAuthType = ""
         nfsServerUser = ""
         deviceId = ""

         class PEType(Enum): # vim.host.ProtocolEndpoint.PEType
            block = 0
            nas = 1

         class ProtocolEndpointType(Enum): # vim.host.ProtocolEndpoint.ProtocolEndpointType
            scsi = 0
            nfs = 1
            nfs4x = 2

      class RdmaDevice(vmodl.DynamicData): # vim.host.RdmaDevice
         key = ""
         device = ""
         driver = ""
         description = ""
         backing = vim.host.RdmaDevice.Backing()
         connectionInfo = vim.host.RdmaDevice.ConnectionInfo()
         capability = vim.host.RdmaDevice.Capability()

         class Backing(vmodl.DynamicData): # vim.host.RdmaDevice.Backing
            pass

         class PnicBacking(vim.host.RdmaDevice.Backing): # vim.host.RdmaDevice.PnicBacking
            pairedUplink = vim.host.PhysicalNic()

         class ConnectionState(Enum): # vim.host.RdmaDevice.ConnectionState
            unknown = 0
            down = 1
            init = 2
            armed = 3
            active = 4
            activeDefer = 5

         class ConnectionInfo(vmodl.DynamicData): # vim.host.RdmaDevice.ConnectionInfo
            state = ""
            mtu = 0
            speedInMbps = 0

         class Capability(vmodl.DynamicData): # vim.host.RdmaDevice.Capability
            roceV1Capable = False
            roceV2Capable = False
            iWarpCapable = False

      class RdmaHba(vim.host.HostBusAdapter): # vim.host.RdmaHba
         associatedRdmaDevice = ""

      class ReliableMemoryInfo(vmodl.DynamicData): # vim.host.ReliableMemoryInfo
         memorySize = 0

      class ResignatureRescanResult(vmodl.DynamicData): # vim.host.ResignatureRescanResult
         rescan = [ vim.host.VmfsRescanResult() ]
         result = vim.Datastore()

      class Ruleset(vmodl.DynamicData): # vim.host.Ruleset
         key = ""
         label = ""
         required = False
         rule = [ vim.host.Ruleset.Rule() ]
         service = ""
         enabled = False
         allowedHosts = vim.host.Ruleset.IpList()

         class IpNetwork(vmodl.DynamicData): # vim.host.Ruleset.IpNetwork
            network = ""
            prefixLength = 0

         class IpList(vmodl.DynamicData): # vim.host.Ruleset.IpList
            ipAddress = [ "" ]
            ipNetwork = [ vim.host.Ruleset.IpNetwork() ]
            allIp = False

         class RulesetSpec(vmodl.DynamicData): # vim.host.Ruleset.RulesetSpec
            allowedHosts = vim.host.Ruleset.IpList()

         class Rule(vmodl.DynamicData): # vim.host.Ruleset.Rule
            port = 0
            endPort = 0
            direction = vim.host.Ruleset.Rule.Direction()
            portType = vim.host.Ruleset.Rule.PortType()
            protocol = ""

            class Direction(Enum): # vim.host.Ruleset.Rule.Direction
               inbound = 0
               outbound = 1

            class PortType(Enum): # vim.host.Ruleset.Rule.PortType
               src = 0
               dst = 1

            class Protocol(Enum): # vim.host.Ruleset.Rule.Protocol
               tcp = 0
               udp = 1

      class ScsiLun(vim.host.Device): # vim.host.ScsiLun
         key = ""
         uuid = ""
         descriptor = [ vim.host.ScsiLun.Descriptor() ]
         canonicalName = ""
         displayName = ""
         lunType = ""
         vendor = ""
         model = ""
         revision = ""
         scsiLevel = 0
         serialNumber = ""
         durableName = vim.host.ScsiLun.DurableName()
         alternateName = [ vim.host.ScsiLun.DurableName() ]
         standardInquiry = [ 0x00 ]
         queueDepth = 0
         operationalState = [ "" ]
         capabilities = vim.host.ScsiLun.Capabilities()
         vStorageSupport = ""
         protocolEndpoint = False
         perenniallyReserved = False
         clusteredVmdkSupported = False

         class ScsiLunType(Enum): # vim.host.ScsiLun.ScsiLunType
            disk = 0
            tape = 1
            printer = 2
            processor = 3
            worm = 4
            cdrom = 5
            scanner = 6
            opticalDevice = 7
            mediaChanger = 8
            communications = 9
            storageArrayController = 10
            enclosure = 11
            unknown = 12

         class Capabilities(vmodl.DynamicData): # vim.host.ScsiLun.Capabilities
            updateDisplayNameSupported = False

         class DurableName(vmodl.DynamicData): # vim.host.ScsiLun.DurableName
            namespace = ""
            namespaceId = 0x00
            data = [ 0x00 ]

         class State(Enum): # vim.host.ScsiLun.State
            unknownState = 0
            ok = 1
            error = 2
            off = 3
            quiesced = 4
            degraded = 5
            lostCommunication = 6
            timeout = 7

         class DescriptorQuality(Enum): # vim.host.ScsiLun.DescriptorQuality
            highQuality = 0
            mediumQuality = 1
            lowQuality = 2
            unknownQuality = 3

         class Descriptor(vmodl.DynamicData): # vim.host.ScsiLun.Descriptor
            quality = ""
            id = ""

         class VStorageSupportStatus(Enum): # vim.host.ScsiLun.VStorageSupportStatus
            vStorageSupported = 0
            vStorageUnsupported = 1
            vStorageUnknown = 2

      class ScsiTopology(vmodl.DynamicData): # vim.host.ScsiTopology
         adapter = [ vim.host.ScsiTopology.Interface() ]

         class Interface(vmodl.DynamicData): # vim.host.ScsiTopology.Interface
            key = ""
            adapter = vim.host.HostBusAdapter()
            target = [ vim.host.ScsiTopology.Target() ]

         class Target(vmodl.DynamicData): # vim.host.ScsiTopology.Target
            key = ""
            target = 0
            lun = [ vim.host.ScsiTopology.Lun() ]
            transport = vim.host.TargetTransport()

         class Lun(vmodl.DynamicData): # vim.host.ScsiTopology.Lun
            key = ""
            lun = 0
            scsiLun = vim.host.ScsiLun()

      class SerialAttachedHba(vim.host.HostBusAdapter): # vim.host.SerialAttachedHba
         nodeWorldWideName = ""

      class Service(vmodl.DynamicData): # vim.host.Service
         key = ""
         label = ""
         required = False
         uninstallable = False
         running = False
         ruleset = [ "" ]
         policy = ""
         sourcePackage = vim.host.Service.SourcePackage()

         class Policy(Enum): # vim.host.Service.Policy
            on = 0
            automatic = 1
            off = 2

         class SourcePackage(vmodl.DynamicData): # vim.host.Service.SourcePackage
            sourcePackageName = ""
            description = ""

      class ServiceConfig(vmodl.DynamicData): # vim.host.ServiceConfig
         serviceId = ""
         startupPolicy = ""

      class ServiceInfo(vmodl.DynamicData): # vim.host.ServiceInfo
         service = [ vim.host.Service() ]

      class ServiceSystem(vim.ExtensibleManagedObject): # vim.host.ServiceSystem
         serviceInfo = vim.host.ServiceInfo()

         def updatePolicy(id="", policy=""): # vim.host.ServiceSystem.updatePolicy
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def start(id=""): # vim.host.ServiceSystem.start
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def stop(id=""): # vim.host.ServiceSystem.stop
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def restart(id=""): # vim.host.ServiceSystem.restart
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def uninstall(id=""): # vim.host.ServiceSystem.uninstall
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh(): # vim.host.ServiceSystem.refresh
            return None

      class SgxInfo(vmodl.DynamicData): # vim.host.SgxInfo
         sgxState = ""
         totalEpcMemory = 0
         flcMode = ""
         lePubKeyHash = ""

         class SgxStates(Enum): # vim.host.SgxInfo.SgxStates
            notPresent = 0
            disabledBIOS = 1
            disabledCFW101 = 2
            disabledCPUMismatch = 3
            disabledNoFLC = 4
            disabledNUMAUnsup = 5
            disabledMaxEPCRegs = 6
            enabled = 7

         class FlcModes(Enum): # vim.host.SgxInfo.FlcModes
            off = 0
            locked = 1
            unlocked = 2

      class SharedGpuCapabilities(vmodl.DynamicData): # vim.host.SharedGpuCapabilities
         vgpu = ""
         diskSnapshotSupported = False
         memorySnapshotSupported = False
         suspendSupported = False
         migrateSupported = False

      class SnmpSystem(vmodl.ManagedObject): # vim.host.SnmpSystem
         configuration = vim.host.SnmpSystem.SnmpConfigSpec()
         limits = vim.host.SnmpSystem.AgentLimits()

         def reconfigureSnmpAgent(spec=vim.host.SnmpSystem.SnmpConfigSpec()): # vim.host.SnmpSystem.reconfigureSnmpAgent
            # throws vim.fault.NotFound, vim.fault.InsufficientResourcesFault
            return None

         def sendTestNotification(): # vim.host.SnmpSystem.sendTestNotification
            # throws vim.fault.NotFound, vim.fault.InsufficientResourcesFault
            return None

         class SnmpConfigSpec(vmodl.DynamicData): # vim.host.SnmpSystem.SnmpConfigSpec
            enabled = False
            port = 0
            readOnlyCommunities = [ "" ]
            trapTargets = [ vim.host.SnmpSystem.SnmpConfigSpec.Destination() ]
            option = [ vim.KeyValue() ]

            class Destination(vmodl.DynamicData): # vim.host.SnmpSystem.SnmpConfigSpec.Destination
               hostName = ""
               port = 0
               community = ""

         class AgentLimits(vmodl.DynamicData): # vim.host.SnmpSystem.AgentLimits
            maxReadOnlyCommunities = 0
            maxTrapDestinations = 0
            maxCommunityLength = 0
            maxBufferSize = 0
            capability = vim.host.SnmpSystem.AgentLimits.Capability()

            class Capability(Enum): # vim.host.SnmpSystem.AgentLimits.Capability
               COMPLETE = 0
               DIAGNOSTICS = 1
               CONFIGURATION = 2

      class SoftwarePackage(vmodl.DynamicData): # vim.host.SoftwarePackage
         name = ""
         version = ""
         type = ""
         vendor = ""
         acceptanceLevel = ""
         summary = ""
         description = ""
         referenceURL = [ "" ]
         creationDate = vmodl.DateTime()
         depends = [ vim.host.SoftwarePackage.Relation() ]
         conflicts = [ vim.host.SoftwarePackage.Relation() ]
         replaces = [ vim.host.SoftwarePackage.Relation() ]
         provides = [ "" ]
         maintenanceModeRequired = False
         hardwarePlatformsRequired = [ "" ]
         capability = vim.host.SoftwarePackage.Capability()
         tag = [ "" ]
         payload = [ "" ]

         class VibType(Enum): # vim.host.SoftwarePackage.VibType
            bootbank = 0
            tools = 1
            meta = 2

         class Capability(vmodl.DynamicData): # vim.host.SoftwarePackage.Capability
            liveInstallAllowed = False
            liveRemoveAllowed = False
            statelessReady = False
            overlay = False

         class Constraint(Enum): # vim.host.SoftwarePackage.Constraint
            equals = 0
            lessThan = 1
            lessThanEqual = 2
            greaterThanEqual = 3
            greaterThan = 4

         class Relation(vmodl.DynamicData): # vim.host.SoftwarePackage.Relation
            constraint = ""
            name = ""
            version = ""

      class SriovConfig(vim.host.PciPassthruConfig): # vim.host.SriovConfig
         sriovEnabled = False
         numVirtualFunction = 0

      class SriovDevicePoolInfo(vmodl.DynamicData): # vim.host.SriovDevicePoolInfo
         key = ""

      class SriovInfo(vim.host.PciPassthruInfo): # vim.host.SriovInfo
         sriovEnabled = False
         sriovCapable = False
         sriovActive = False
         numVirtualFunctionRequested = 0
         numVirtualFunction = 0
         maxVirtualFunctionSupported = 0

      class SriovNetworkDevicePoolInfo(vim.host.SriovDevicePoolInfo): # vim.host.SriovNetworkDevicePoolInfo
         switchKey = ""
         switchUuid = ""
         pnic = [ vim.host.PhysicalNic() ]

      class SslThumbprintInfo(vmodl.DynamicData): # vim.host.SslThumbprintInfo
         principal = ""
         ownerTag = ""
         sslThumbprints = [ "" ]

      class StorageArrayTypePolicyOption(vmodl.DynamicData): # vim.host.StorageArrayTypePolicyOption
         policy = vim.ElementDescription()

      class StorageDeviceInfo(vmodl.DynamicData): # vim.host.StorageDeviceInfo
         hostBusAdapter = [ vim.host.HostBusAdapter() ]
         scsiLun = [ vim.host.ScsiLun() ]
         scsiTopology = vim.host.ScsiTopology()
         nvmeTopology = vim.host.NvmeTopology()
         multipathInfo = vim.host.MultipathInfo()
         plugStoreTopology = vim.host.PlugStoreTopology()
         softwareInternetScsiEnabled = False

      class StorageProtocol(Enum): # vim.host.StorageProtocol
         scsi = 0
         nvme = 1

      class SystemEventInfo(vmodl.DynamicData): # vim.host.SystemEventInfo
         recordId = 0
         when = ""
         selType = 0
         message = ""
         sensorNumber = 0

      class SystemHealthInfo(vmodl.DynamicData): # vim.host.SystemHealthInfo
         numericSensorInfo = [ vim.host.NumericSensorInfo() ]

      class SystemIdentificationInfo(vmodl.DynamicData): # vim.host.SystemIdentificationInfo
         identifierValue = ""
         identifierType = vim.ElementDescription()

         class Identifier(Enum): # vim.host.SystemIdentificationInfo.Identifier
            AssetTag = 0
            ServiceTag = 1
            OemSpecificString = 2
            EnclosureSerialNumberTag = 3
            SerialNumberTag = 4

      class SystemInfo(vmodl.DynamicData): # vim.host.SystemInfo
         vendor = ""
         model = ""
         uuid = ""
         otherIdentifyingInfo = [ vim.host.SystemIdentificationInfo() ]
         serialNumber = ""

      class SystemResourceInfo(vmodl.DynamicData): # vim.host.SystemResourceInfo
         key = ""
         config = vim.ResourceConfigSpec()
         child = [ vim.host.SystemResourceInfo() ]

      class SystemSwapConfiguration(vmodl.DynamicData): # vim.host.SystemSwapConfiguration
         option = [ vim.host.SystemSwapConfiguration.SystemSwapOption() ]

         class SystemSwapOption(vmodl.DynamicData): # vim.host.SystemSwapConfiguration.SystemSwapOption
            key = 0

         class DisabledOption(vim.host.SystemSwapConfiguration.SystemSwapOption): # vim.host.SystemSwapConfiguration.DisabledOption
            pass

         class HostCacheOption(vim.host.SystemSwapConfiguration.SystemSwapOption): # vim.host.SystemSwapConfiguration.HostCacheOption
            pass

         class HostLocalSwapOption(vim.host.SystemSwapConfiguration.SystemSwapOption): # vim.host.SystemSwapConfiguration.HostLocalSwapOption
            pass

         class DatastoreOption(vim.host.SystemSwapConfiguration.SystemSwapOption): # vim.host.SystemSwapConfiguration.DatastoreOption
            datastore = ""

      class TargetTransport(vmodl.DynamicData): # vim.host.TargetTransport
         pass

      class TpmAttestationInfo(vmodl.DynamicData): # vim.host.TpmAttestationInfo
         time = vmodl.DateTime()
         status = vim.host.TpmAttestationInfo.AcceptanceStatus()
         message = vmodl.LocalizableMessage()

         class AcceptanceStatus(Enum): # vim.host.TpmAttestationInfo.AcceptanceStatus
            notAccepted = 0
            accepted = 1

      class TpmAttestationReport(vmodl.DynamicData): # vim.host.TpmAttestationReport
         tpmPcrValues = [ vim.host.TpmDigestInfo() ]
         tpmEvents = [ vim.host.TpmEventLogEntry() ]
         tpmLogReliable = False

      class TpmDigestInfo(vim.host.DigestInfo): # vim.host.TpmDigestInfo
         pcrNumber = 0

      class TpmEventDetails(vmodl.DynamicData): # vim.host.TpmEventDetails
         dataHash = [ 0x00 ]
         dataHashMethod = ""

      class TpmEventLogEntry(vmodl.DynamicData): # vim.host.TpmEventLogEntry
         pcrIndex = 0
         eventDetails = vim.host.TpmEventDetails()

      class TpmOptionEventDetails(vim.host.TpmEventDetails): # vim.host.TpmOptionEventDetails
         optionsFileName = ""
         bootOptions = [ 0x00 ]

      class TpmSoftwareComponentEventDetails(vim.host.TpmEventDetails): # vim.host.TpmSoftwareComponentEventDetails
         componentName = ""
         vibName = ""
         vibVersion = ""
         vibVendor = ""

      class UnresolvedVmfsResignatureSpec(vmodl.DynamicData): # vim.host.UnresolvedVmfsResignatureSpec
         extentDevicePath = [ "" ]

      class UnresolvedVmfsResolutionResult(vmodl.DynamicData): # vim.host.UnresolvedVmfsResolutionResult
         spec = vim.host.UnresolvedVmfsResolutionSpec()
         vmfs = vim.host.VmfsVolume()
         fault = vmodl.MethodFault()

      class UnresolvedVmfsResolutionSpec(vmodl.DynamicData): # vim.host.UnresolvedVmfsResolutionSpec
         extentDevicePath = [ "" ]
         uuidResolution = ""

         class VmfsUuidResolution(Enum): # vim.host.UnresolvedVmfsResolutionSpec.VmfsUuidResolution
            resignature = 0
            forceMount = 1

      class UnresolvedVmfsVolume(vmodl.DynamicData): # vim.host.UnresolvedVmfsVolume
         extent = [ vim.host.UnresolvedVmfsExtent() ]
         vmfsLabel = ""
         vmfsUuid = ""
         totalBlocks = 0
         resolveStatus = vim.host.UnresolvedVmfsVolume.ResolveStatus()

         class ResolveStatus(vmodl.DynamicData): # vim.host.UnresolvedVmfsVolume.ResolveStatus
            resolvable = False
            incompleteExtents = False
            multipleCopies = False

      class VFlashResourceConfigurationResult(vmodl.DynamicData): # vim.host.VFlashResourceConfigurationResult
         devicePath = [ "" ]
         vffs = vim.host.VffsVolume()
         diskConfigurationResult = [ vim.host.DiskConfigurationResult() ]

      class VMotionConfig(vmodl.DynamicData): # vim.host.VMotionConfig
         vmotionNicKey = ""
         enabled = False

      class VMotionSystem(vim.ExtensibleManagedObject): # vim.host.VMotionSystem
         netConfig = vim.host.VMotionSystem.NetConfig()
         ipConfig = vim.host.IpConfig()

         def updateIpConfig(ipConfig=vim.host.IpConfig()): # vim.host.VMotionSystem.updateIpConfig
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def selectVnic(device=""): # vim.host.VMotionSystem.selectVnic
            # throws vim.fault.HostConfigFault
            return None

         def deselectVnic(): # vim.host.VMotionSystem.deselectVnic
            # throws vim.fault.HostConfigFault
            return None

         class NetConfig(vmodl.DynamicData): # vim.host.VMotionSystem.NetConfig
            candidateVnic = [ vim.host.VirtualNic() ]
            selectedVnic = vim.host.VirtualNic()

      class VfatVolume(vim.host.FileSystemVolume): # vim.host.VfatVolume
         pass

      class VirtualNic(vmodl.DynamicData): # vim.host.VirtualNic
         device = ""
         key = ""
         portgroup = ""
         spec = vim.host.VirtualNic.Specification()
         port = vim.host.PortGroup.Port()

         class Specification(vmodl.DynamicData): # vim.host.VirtualNic.Specification
            ip = vim.host.IpConfig()
            mac = ""
            distributedVirtualPort = vim.dvs.PortConnection()
            portgroup = ""
            mtu = 0
            tsoEnabled = False
            netStackInstanceKey = ""
            opaqueNetwork = vim.host.VirtualNic.OpaqueNetworkSpec()
            externalId = ""
            pinnedPnic = ""
            ipRouteSpec = vim.host.VirtualNic.IpRouteSpec()
            systemOwned = False

         class Config(vmodl.DynamicData): # vim.host.VirtualNic.Config
            changeOperation = ""
            device = ""
            portgroup = ""
            spec = vim.host.VirtualNic.Specification()

         class OpaqueNetworkSpec(vmodl.DynamicData): # vim.host.VirtualNic.OpaqueNetworkSpec
            opaqueNetworkId = ""
            opaqueNetworkType = ""

         class IpRouteSpec(vmodl.DynamicData): # vim.host.VirtualNic.IpRouteSpec
            ipRouteConfig = vim.host.IpRouteConfig()

      class VirtualNicConnection(vmodl.DynamicData): # vim.host.VirtualNicConnection
         portgroup = ""
         dvPort = vim.dvs.PortConnection()
         opNetwork = vim.host.VirtualNic.OpaqueNetworkSpec()

      class VirtualNicManager(vim.ExtensibleManagedObject): # vim.host.VirtualNicManager
         info = vim.host.VirtualNicManagerInfo()

         def queryNetConfig(nicType=""): # vim.host.VirtualNicManager.queryNetConfig
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return vim.host.VirtualNicManager.NetConfig()

         def selectVnic(nicType="", device=""): # vim.host.VirtualNicManager.selectVnic
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return None

         def deselectVnic(nicType="", device=""): # vim.host.VirtualNicManager.deselectVnic
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return None

         class NicType(Enum): # vim.host.VirtualNicManager.NicType
            vmotion = 0
            faultToleranceLogging = 1
            vSphereReplication = 2
            vSphereReplicationNFC = 3
            management = 4
            vsan = 5
            vSphereProvisioning = 6
            vsanWitness = 7
            vSphereBackupNFC = 8
            ptp = 9
            vsanReplication = 10

         class NicTypeSelection(vmodl.DynamicData): # vim.host.VirtualNicManager.NicTypeSelection
            vnic = vim.host.VirtualNicConnection()
            nicType = [ "" ]

         class NetConfig(vmodl.DynamicData): # vim.host.VirtualNicManager.NetConfig
            nicType = ""
            multiSelectAllowed = False
            candidateVnic = [ vim.host.VirtualNic() ]
            selectedVnic = [ vim.host.VirtualNic() ]

      class VirtualNicManagerInfo(vmodl.DynamicData): # vim.host.VirtualNicManagerInfo
         netConfig = [ vim.host.VirtualNicManager.NetConfig() ]

      class VirtualSwitch(vmodl.DynamicData): # vim.host.VirtualSwitch
         name = ""
         key = ""
         numPorts = 0
         numPortsAvailable = 0
         mtu = 0
         portgroup = [ vim.host.PortGroup() ]
         pnic = [ vim.host.PhysicalNic() ]
         spec = vim.host.VirtualSwitch.Specification()

         class Bridge(vmodl.DynamicData): # vim.host.VirtualSwitch.Bridge
            pass

         class AutoBridge(vim.host.VirtualSwitch.Bridge): # vim.host.VirtualSwitch.AutoBridge
            excludedNicDevice = [ "" ]

         class SimpleBridge(vim.host.VirtualSwitch.Bridge): # vim.host.VirtualSwitch.SimpleBridge
            nicDevice = ""

         class BondBridge(vim.host.VirtualSwitch.Bridge): # vim.host.VirtualSwitch.BondBridge
            nicDevice = [ "" ]
            beacon = vim.host.VirtualSwitch.BeaconConfig()
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()

         class BeaconConfig(vmodl.DynamicData): # vim.host.VirtualSwitch.BeaconConfig
            interval = 0

         class Specification(vmodl.DynamicData): # vim.host.VirtualSwitch.Specification
            numPorts = 0
            bridge = vim.host.VirtualSwitch.Bridge()
            policy = vim.host.NetworkPolicy()
            mtu = 0

         class Config(vmodl.DynamicData): # vim.host.VirtualSwitch.Config
            changeOperation = ""
            name = ""
            spec = vim.host.VirtualSwitch.Specification()

      class VmciAccessManager(object): # (unknown name)

         class Mode(Enum): # vim.host.VmciAccessManager.Mode
            grant = 0
            replace = 1
            revoke = 2

         class AccessSpec(vmodl.DynamicData): # vim.host.VmciAccessManager.AccessSpec
            vm = vim.VirtualMachine()
            services = [ "" ]
            mode = ""

      class VmfsDatastoreOption(vmodl.DynamicData): # vim.host.VmfsDatastoreOption
         info = vim.host.VmfsDatastoreOption.Info()
         spec = vim.host.VmfsDatastoreSpec()

         class Info(vmodl.DynamicData): # vim.host.VmfsDatastoreOption.Info
            layout = vim.host.DiskPartitionInfo.Layout()
            partitionFormatChange = False

         class SingleExtentInfo(vim.host.VmfsDatastoreOption.Info): # vim.host.VmfsDatastoreOption.SingleExtentInfo
            vmfsExtent = vim.host.DiskPartitionInfo.BlockRange()

         class AllExtentInfo(vim.host.VmfsDatastoreOption.SingleExtentInfo): # vim.host.VmfsDatastoreOption.AllExtentInfo
            pass

         class MultipleExtentInfo(vim.host.VmfsDatastoreOption.Info): # vim.host.VmfsDatastoreOption.MultipleExtentInfo
            vmfsExtent = [ vim.host.DiskPartitionInfo.BlockRange() ]

      class VmfsDatastoreSpec(vmodl.DynamicData): # vim.host.VmfsDatastoreSpec
         diskUuid = ""

      class VmfsRescanResult(vmodl.DynamicData): # vim.host.VmfsRescanResult
         host = vim.HostSystem()
         fault = vmodl.MethodFault()

      class VsanInternalSystem(vmodl.ManagedObject): # vim.host.VsanInternalSystem

         def queryCmmds(queries=[ vim.host.VsanInternalSystem.CmmdsQuery() ]): # vim.host.VsanInternalSystem.queryCmmds
            return ""

         def queryPhysicalVsanDisks(props=[ "" ] or None): # vim.host.VsanInternalSystem.queryPhysicalVsanDisks
            return ""

         def queryVsanObjects(uuids=[ "" ] or None): # vim.host.VsanInternalSystem.queryVsanObjects
            return ""

         def queryObjectsOnPhysicalVsanDisk(disks=[ "" ]): # vim.host.VsanInternalSystem.queryObjectsOnPhysicalVsanDisk
            return ""

         def abdicateDomOwnership(uuids=[ "" ]): # vim.host.VsanInternalSystem.abdicateDomOwnership
            return [ "" ]

         def queryVsanStatistics(labels=[ "" ]): # vim.host.VsanInternalSystem.queryVsanStatistics
            return ""

         def reconfigureDomObject(uuid="", policy=""): # vim.host.VsanInternalSystem.reconfigureDomObject
            return None

         def querySyncingVsanObjects(uuids=[ "" ] or None): # vim.host.VsanInternalSystem.querySyncingVsanObjects
            return ""

         def runVsanPhysicalDiskDiagnostics(disks=[ "" ] or None): # vim.host.VsanInternalSystem.runVsanPhysicalDiskDiagnostics
            return [ vim.host.VsanInternalSystem.VsanPhysicalDiskDiagnosticsResult() ]

         def getVsanObjExtAttrs(uuids=[ "" ]): # vim.host.VsanInternalSystem.getVsanObjExtAttrs
            # throws vim.fault.VimFault
            return ""

         def reconfigurationSatisfiable(pcbs=[ vim.host.VsanInternalSystem.PolicyChangeBatch() ], ignoreSatisfiability=False or None): # vim.host.VsanInternalSystem.reconfigurationSatisfiable
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.PolicySatisfiability() ]

         def canProvisionObjects(npbs=[ vim.host.VsanInternalSystem.NewPolicyBatch() ], ignoreSatisfiability=False or None): # vim.host.VsanInternalSystem.canProvisionObjects
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.PolicySatisfiability() ]

         def deleteVsanObjects(uuids=[ "" ], force=False or None): # vim.host.VsanInternalSystem.deleteVsanObjects
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.DeleteVsanObjectsResult() ]

         def upgradeVsanObjects(uuids=[ "" ], newVersion=0): # vim.host.VsanInternalSystem.upgradeVsanObjects
            # throws vim.fault.VsanFault
            return [ vim.host.VsanInternalSystem.VsanObjectOperationResult() ]

         def queryVsanObjectUuidsByFilter(uuids=[ "" ] or None, limit=0 or None, version=0 or None): # vim.host.VsanInternalSystem.queryVsanObjectUuidsByFilter
            # throws vim.fault.VsanFault
            return [ "" ]

         class CmmdsQuery(vmodl.DynamicData): # vim.host.VsanInternalSystem.CmmdsQuery
            type = ""
            uuid = ""
            owner = ""

         class PolicyCost(vmodl.DynamicData): # vim.host.VsanInternalSystem.PolicyCost
            changeDataSize = 0
            currentDataSize = 0
            tempDataSize = 0
            copyDataSize = 0
            changeFlashReadCacheSize = 0
            currentFlashReadCacheSize = 0
            currentDiskSpaceToAddressSpaceRatio = 0.0
            diskSpaceToAddressSpaceRatio = 0.0

         class PolicySatisfiability(vmodl.DynamicData): # vim.host.VsanInternalSystem.PolicySatisfiability
            uuid = ""
            isSatisfiable = False
            reason = vmodl.LocalizableMessage()
            cost = vim.host.VsanInternalSystem.PolicyCost()

         class PolicyChangeBatch(vmodl.DynamicData): # vim.host.VsanInternalSystem.PolicyChangeBatch
            uuid = [ "" ]
            policy = ""

         class NewPolicyBatch(vmodl.DynamicData): # vim.host.VsanInternalSystem.NewPolicyBatch
            size = [ 0 ]
            policy = ""

         class VsanPhysicalDiskDiagnosticsResult(vmodl.DynamicData): # vim.host.VsanInternalSystem.VsanPhysicalDiskDiagnosticsResult
            diskUuid = ""
            success = False
            failureReason = ""

         class DeleteVsanObjectsResult(vmodl.DynamicData): # vim.host.VsanInternalSystem.DeleteVsanObjectsResult
            uuid = ""
            success = False
            failureReason = [ vmodl.LocalizableMessage() ]

         class VsanObjectOperationResult(vmodl.DynamicData): # vim.host.VsanInternalSystem.VsanObjectOperationResult
            uuid = ""
            failureReason = [ vmodl.LocalizableMessage() ]

      class VsanSystem(vmodl.ManagedObject): # vim.host.VsanSystem
         config = vim.vsan.host.ConfigInfo()

         def queryDisksForVsan(canonicalName=[ "" ] or None): # vim.host.VsanSystem.queryDisksForVsan
            return [ vim.vsan.host.DiskResult() ]

         def addDisks(disk=[ vim.host.ScsiDisk() ]): # vim.host.VsanSystem.addDisks
            return vim.Task()

         def initializeDisks(mapping=[ vim.vsan.host.DiskMapping() ]): # vim.host.VsanSystem.initializeDisks
            return vim.Task()

         def removeDisk(disk=[ vim.host.ScsiDisk() ], maintenanceSpec=vim.host.MaintenanceSpec() or None, timeout=0 or None): # vim.host.VsanSystem.removeDisk
            return vim.Task()

         def removeDiskMapping(mapping=[ vim.vsan.host.DiskMapping() ], maintenanceSpec=vim.host.MaintenanceSpec() or None, timeout=0 or None): # vim.host.VsanSystem.removeDiskMapping
            return vim.Task()

         def unmountDiskMapping(mapping=[ vim.vsan.host.DiskMapping() ]): # vim.host.VsanSystem.unmountDiskMapping
            # throws vim.fault.InvalidState, vim.fault.VsanFault
            return vim.Task()

         def update(config=vim.vsan.host.ConfigInfo()): # vim.host.VsanSystem.update
            return vim.Task()

         def queryHostStatus(): # vim.host.VsanSystem.queryHostStatus
            return vim.vsan.host.ClusterStatus()

         def evacuateNode(maintenanceSpec=vim.host.MaintenanceSpec(), timeout=0): # vim.host.VsanSystem.evacuateNode
            # throws vim.fault.InvalidState, vmodl.fault.RequestCanceled, vim.fault.Timedout, vim.fault.VsanFault
            return vim.Task()

         def recommissionNode(): # vim.host.VsanSystem.recommissionNode
            # throws vim.fault.InvalidState, vim.fault.VsanFault
            return vim.Task()

      class VvolVolume(vim.host.FileSystemVolume): # vim.host.VvolVolume
         scId = ""
         hostPE = [ vim.host.VvolVolume.HostProtocolEndpoint() ]
         vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
         storageArray = [ vim.VasaStorageArray() ]

         class Specification(vmodl.DynamicData): # vim.host.VvolVolume.Specification
            maxSizeInMB = 0
            volumeName = ""
            vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
            storageArray = [ vim.VasaStorageArray() ]
            uuid = ""

         class HostProtocolEndpoint(vmodl.DynamicData): # vim.host.VvolVolume.HostProtocolEndpoint
            key = vim.HostSystem()
            protocolEndpoint = [ vim.host.ProtocolEndpoint() ]

      class ActiveDirectoryAuthentication(vim.host.DirectoryStore): # vim.host.ActiveDirectoryAuthentication

         def joinDomain(domainName="", userName="", password=""): # vim.host.ActiveDirectoryAuthentication.joinDomain
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.InvalidLogin, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def joinDomainWithCAM(domainName="", camServer=""): # vim.host.ActiveDirectoryAuthentication.joinDomainWithCAM
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def importCertificateForCAM(certPath="", camServer=""): # vim.host.ActiveDirectoryAuthentication.importCertificateForCAM
            # throws vim.fault.FileNotFound, vim.fault.ActiveDirectoryFault
            return vim.Task()

         def leaveCurrentDomain(force=False): # vim.host.ActiveDirectoryAuthentication.leaveCurrentDomain
            # throws vim.fault.InvalidState, vim.fault.AuthMinimumAdminPermission, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def enableSmartCardAuthentication(): # vim.host.ActiveDirectoryAuthentication.enableSmartCardAuthentication
            # throws vim.fault.ActiveDirectoryFault, vim.fault.HostConfigFault
            return None

         def installSmartCardTrustAnchor(cert=""): # vim.host.ActiveDirectoryAuthentication.installSmartCardTrustAnchor
            # throws vim.fault.HostConfigFault
            return None

         def replaceSmartCardTrustAnchors(certs=[ "" ] or None): # vim.host.ActiveDirectoryAuthentication.replaceSmartCardTrustAnchors
            return None

         def removeSmartCardTrustAnchor(issuer="", serial=""): # vim.host.ActiveDirectoryAuthentication.removeSmartCardTrustAnchor
            # throws vim.fault.HostConfigFault
            return None

         def removeSmartCardTrustAnchorByFingerprint(fingerprint="", digest=""): # vim.host.ActiveDirectoryAuthentication.removeSmartCardTrustAnchorByFingerprint
            # throws vim.fault.HostConfigFault
            return None

         def listSmartCardTrustAnchors(): # vim.host.ActiveDirectoryAuthentication.listSmartCardTrustAnchors
            # throws vim.fault.HostConfigFault
            return [ "" ]

         def disableSmartCardAuthentication(): # vim.host.ActiveDirectoryAuthentication.disableSmartCardAuthentication
            # throws vim.fault.ActiveDirectoryFault, vim.fault.HostConfigFault
            return None

         class CertificateDigest(Enum): # vim.host.ActiveDirectoryAuthentication.CertificateDigest
            SHA1 = 0

      class ActiveDirectoryInfo(vim.host.DirectoryStoreInfo): # vim.host.ActiveDirectoryInfo
         joinedDomain = ""
         trustedDomain = [ "" ]
         domainMembershipStatus = ""
         smartCardAuthenticationEnabled = False

         class DomainMembershipStatus(Enum): # vim.host.ActiveDirectoryInfo.DomainMembershipStatus
            unknown = 0
            ok = 1
            noServers = 2
            clientTrustBroken = 3
            serverTrustBroken = 4
            inconsistentTrust = 5
            otherProblem = 6

      class BlockAdapterTargetTransport(vim.host.TargetTransport): # vim.host.BlockAdapterTargetTransport
         pass

      class BlockHba(vim.host.HostBusAdapter): # vim.host.BlockHba
         pass

      class BootDeviceInfo(vmodl.DynamicData): # vim.host.BootDeviceInfo
         bootDevices = [ vim.host.BootDeviceSystem.BootDevice() ]
         currentBootDeviceKey = ""

      class ConfigSpec(vmodl.DynamicData): # vim.host.ConfigSpec
         nasDatastore = [ vim.host.NasVolume.Config() ]
         network = vim.host.NetworkConfig()
         nicTypeSelection = [ vim.host.VirtualNicManager.NicTypeSelection() ]
         service = [ vim.host.ServiceConfig() ]
         firewall = vim.host.FirewallConfig()
         option = [ vim.option.OptionValue() ]
         datastorePrincipal = ""
         datastorePrincipalPasswd = ""
         datetime = vim.host.DateTimeConfig()
         storageDevice = vim.host.StorageDeviceInfo()
         license = vim.host.LicenseSpec()
         security = vim.host.SecuritySpec()
         userAccount = [ vim.host.LocalAccountManager.AccountSpecification() ]
         usergroupAccount = [ vim.host.LocalAccountManager.AccountSpecification() ]
         memory = vim.host.MemorySpec()
         activeDirectory = [ vim.host.ActiveDirectorySpec() ]
         genericConfig = [ vmodl.KeyAnyValue() ]
         graphicsConfig = vim.host.GraphicsConfig()
         assignableHardwareConfig = vim.host.AssignableHardwareConfig()

      class ConnectSpec(vmodl.DynamicData): # vim.host.ConnectSpec
         hostName = ""
         port = 0
         sslThumbprint = ""
         userName = ""
         password = ""
         vmFolder = vim.Folder()
         force = False
         vimAccountName = ""
         vimAccountPassword = ""
         managementIp = ""
         lockdownMode = vim.host.HostAccessManager.LockdownMode()
         hostGateway = vim.host.GatewaySpec()

      class DatastoreSystem(vmodl.ManagedObject): # vim.host.DatastoreSystem
         datastore = [ vim.Datastore() ]
         capabilities = vim.host.DatastoreSystem.Capabilities()

         def updateLocalSwapDatastore(datastore=vim.Datastore() or None): # vim.host.DatastoreSystem.updateLocalSwapDatastore
            # throws vim.fault.InaccessibleDatastore, vim.fault.DatastoreNotWritableOnHost
            return None

         def queryAvailableDisksForVmfs(datastore=vim.Datastore() or None): # vim.host.DatastoreSystem.queryAvailableDisksForVmfs
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.ScsiDisk() ]

         def queryVmfsDatastoreCreateOptions(devicePath="", vmfsMajorVersion=0 or None): # vim.host.DatastoreSystem.queryVmfsDatastoreCreateOptions
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def createVmfsDatastore(spec=vim.host.VmfsDatastoreCreateSpec()): # vim.host.DatastoreSystem.createVmfsDatastore
            # throws vim.fault.DuplicateName, vim.fault.HostConfigFault
            return vim.Datastore()

         def queryVmfsDatastoreExtendOptions(datastore=vim.Datastore(), devicePath="", suppressExpandCandidates=False or None): # vim.host.DatastoreSystem.queryVmfsDatastoreExtendOptions
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def queryVmfsDatastoreExpandOptions(datastore=vim.Datastore()): # vim.host.DatastoreSystem.queryVmfsDatastoreExpandOptions
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def extendVmfsDatastore(datastore=vim.Datastore(), spec=vim.host.VmfsDatastoreExtendSpec()): # vim.host.DatastoreSystem.extendVmfsDatastore
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Datastore()

         def enableClusteredVmdkSupport(datastore=vim.Datastore()): # vim.host.DatastoreSystem.enableClusteredVmdkSupport
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableClusteredVmdkSupport(datastore=vim.Datastore()): # vim.host.DatastoreSystem.disableClusteredVmdkSupport
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def expandVmfsDatastore(datastore=vim.Datastore(), spec=vim.host.VmfsDatastoreExpandSpec()): # vim.host.DatastoreSystem.expandVmfsDatastore
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Datastore()

         def createNasDatastore(spec=vim.host.NasVolume.Specification()): # vim.host.DatastoreSystem.createNasDatastore
            # throws vim.fault.DuplicateName, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Datastore()

         def createLocalDatastore(name="", path=""): # vim.host.DatastoreSystem.createLocalDatastore
            # throws vim.fault.DuplicateName, vim.fault.HostConfigFault, vim.fault.FileNotFound, vim.fault.InvalidName
            return vim.Datastore()

         def createVvolDatastore(spec=vim.host.DatastoreSystem.VvolDatastoreSpec()): # vim.host.DatastoreSystem.createVvolDatastore
            # throws vim.fault.NotFound, vim.fault.DuplicateName, vim.fault.HostConfigFault, vim.fault.InvalidName
            return vim.Datastore()

         def removeDatastore(datastore=vim.Datastore()): # vim.host.DatastoreSystem.removeDatastore
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def removeDatastoreEx(datastore=[ vim.Datastore() ]): # vim.host.DatastoreSystem.removeDatastoreEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def configureDatastorePrincipal(userName="", password="" or None): # vim.host.DatastoreSystem.configureDatastorePrincipal
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault
            return None

         def queryUnresolvedVmfsVolumes(): # vim.host.DatastoreSystem.queryUnresolvedVmfsVolumes
            return [ vim.host.UnresolvedVmfsVolume() ]

         def resignatureUnresolvedVmfsVolume(resolutionSpec=vim.host.UnresolvedVmfsResignatureSpec()): # vim.host.DatastoreSystem.resignatureUnresolvedVmfsVolume
            # throws vim.fault.VmfsAmbiguousMount, vim.fault.HostConfigFault
            return vim.Task()

         class Capabilities(vmodl.DynamicData): # vim.host.DatastoreSystem.Capabilities
            nfsMountCreationRequired = False
            nfsMountCreationSupported = False
            localDatastoreSupported = False
            vmfsExtentExpansionSupported = False

         class VvolDatastoreSpec(vmodl.DynamicData): # vim.host.DatastoreSystem.VvolDatastoreSpec
            name = ""
            scId = ""

         class DatastoreResult(vmodl.DynamicData): # vim.host.DatastoreSystem.DatastoreResult
            key = vim.Datastore()
            fault = vmodl.MethodFault()

      class DateTimeInfo(vmodl.DynamicData): # vim.host.DateTimeInfo
         timeZone = vim.host.DateTimeSystem.TimeZone()
         systemClockProtocol = ""
         ntpConfig = vim.host.NtpConfig()

         class Protocol(Enum): # vim.host.DateTimeInfo.Protocol
            ntp = 0
            ptp = 1

      class FibreChannelHba(vim.host.HostBusAdapter): # vim.host.FibreChannelHba
         portWorldWideName = 0
         nodeWorldWideName = 0
         portType = vim.host.FibreChannelHba.PortType()
         speed = 0

         class PortType(Enum): # vim.host.FibreChannelHba.PortType
            fabric = 0
            loop = 1
            pointToPoint = 2
            unknown = 3

      class FibreChannelOverEthernetHba(vim.host.FibreChannelHba): # vim.host.FibreChannelOverEthernetHba
         underlyingNic = ""
         linkInfo = vim.host.FibreChannelOverEthernetHba.LinkInfo()
         isSoftwareFcoe = False
         markedForRemoval = False

         class LinkInfo(vmodl.DynamicData): # vim.host.FibreChannelOverEthernetHba.LinkInfo
            vnportMac = ""
            fcfMac = ""
            vlanId = 0

      class FibreChannelTargetTransport(vim.host.TargetTransport): # vim.host.FibreChannelTargetTransport
         portWorldWideName = 0
         nodeWorldWideName = 0

      class FirewallConfig(vmodl.DynamicData): # vim.host.FirewallConfig
         rule = [ vim.host.FirewallConfig.RuleSetConfig() ]
         defaultBlockingPolicy = vim.host.FirewallInfo.DefaultPolicy()

         class RuleSetConfig(vmodl.DynamicData): # vim.host.FirewallConfig.RuleSetConfig
            rulesetId = ""
            enabled = False
            allowedHosts = vim.host.Ruleset.IpList()

      class FirewallSystem(vim.ExtensibleManagedObject): # vim.host.FirewallSystem
         firewallInfo = vim.host.FirewallInfo()

         def updateDefaultPolicy(defaultPolicy=vim.host.FirewallInfo.DefaultPolicy()): # vim.host.FirewallSystem.updateDefaultPolicy
            return None

         def enableRuleset(id=""): # vim.host.FirewallSystem.enableRuleset
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableRuleset(id=""): # vim.host.FirewallSystem.disableRuleset
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateRuleset(id="", spec=vim.host.Ruleset.RulesetSpec()): # vim.host.FirewallSystem.updateRuleset
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh(): # vim.host.FirewallSystem.refresh
            return None

      class InternetScsiHba(vim.host.HostBusAdapter): # vim.host.InternetScsiHba
         isSoftwareBased = False
         canBeDisabled = False
         networkBindingSupport = vim.host.InternetScsiHba.NetworkBindingSupportType()
         discoveryCapabilities = vim.host.InternetScsiHba.DiscoveryCapabilities()
         discoveryProperties = vim.host.InternetScsiHba.DiscoveryProperties()
         authenticationCapabilities = vim.host.InternetScsiHba.AuthenticationCapabilities()
         authenticationProperties = vim.host.InternetScsiHba.AuthenticationProperties()
         digestCapabilities = vim.host.InternetScsiHba.DigestCapabilities()
         digestProperties = vim.host.InternetScsiHba.DigestProperties()
         ipCapabilities = vim.host.InternetScsiHba.IPCapabilities()
         ipProperties = vim.host.InternetScsiHba.IPProperties()
         supportedAdvancedOptions = [ vim.option.OptionDef() ]
         advancedOptions = [ vim.host.InternetScsiHba.ParamValue() ]
         iScsiName = ""
         iScsiAlias = ""
         configuredSendTarget = [ vim.host.InternetScsiHba.SendTarget() ]
         configuredStaticTarget = [ vim.host.InternetScsiHba.StaticTarget() ]
         maxSpeedMb = 0
         currentSpeedMb = 0

         class ParamValue(vim.option.OptionValue): # vim.host.InternetScsiHba.ParamValue
            isInherited = False

         class DiscoveryCapabilities(vmodl.DynamicData): # vim.host.InternetScsiHba.DiscoveryCapabilities
            iSnsDiscoverySettable = False
            slpDiscoverySettable = False
            staticTargetDiscoverySettable = False
            sendTargetsDiscoverySettable = False

         class DiscoveryProperties(vmodl.DynamicData): # vim.host.InternetScsiHba.DiscoveryProperties
            iSnsDiscoveryEnabled = False
            iSnsDiscoveryMethod = ""
            iSnsHost = ""
            slpDiscoveryEnabled = False
            slpDiscoveryMethod = ""
            slpHost = ""
            staticTargetDiscoveryEnabled = False
            sendTargetsDiscoveryEnabled = False

            class ISnsDiscoveryMethod(Enum): # vim.host.InternetScsiHba.DiscoveryProperties.ISnsDiscoveryMethod
               isnsStatic = 0
               isnsDhcp = 1
               isnsSlp = 2

            class SlpDiscoveryMethod(Enum): # vim.host.InternetScsiHba.DiscoveryProperties.SlpDiscoveryMethod
               slpDhcp = 0
               slpAutoUnicast = 1
               slpAutoMulticast = 2
               slpManual = 3

         class ChapAuthenticationType(Enum): # vim.host.InternetScsiHba.ChapAuthenticationType
            chapProhibited = 0
            chapDiscouraged = 1
            chapPreferred = 2
            chapRequired = 3

         class AuthenticationCapabilities(vmodl.DynamicData): # vim.host.InternetScsiHba.AuthenticationCapabilities
            chapAuthSettable = False
            krb5AuthSettable = False
            srpAuthSettable = False
            spkmAuthSettable = False
            mutualChapSettable = False
            targetChapSettable = False
            targetMutualChapSettable = False

         class AuthenticationProperties(vmodl.DynamicData): # vim.host.InternetScsiHba.AuthenticationProperties
            chapAuthEnabled = False
            chapName = ""
            chapSecret = ""
            chapAuthenticationType = ""
            chapInherited = False
            mutualChapName = ""
            mutualChapSecret = ""
            mutualChapAuthenticationType = ""
            mutualChapInherited = False

         class DigestType(Enum): # vim.host.InternetScsiHba.DigestType
            digestProhibited = 0
            digestDiscouraged = 1
            digestPreferred = 2
            digestRequired = 3

         class DigestCapabilities(vmodl.DynamicData): # vim.host.InternetScsiHba.DigestCapabilities
            headerDigestSettable = False
            dataDigestSettable = False
            targetHeaderDigestSettable = False
            targetDataDigestSettable = False

         class DigestProperties(vmodl.DynamicData): # vim.host.InternetScsiHba.DigestProperties
            headerDigestType = ""
            headerDigestInherited = False
            dataDigestType = ""
            dataDigestInherited = False

         class IPCapabilities(vmodl.DynamicData): # vim.host.InternetScsiHba.IPCapabilities
            addressSettable = False
            ipConfigurationMethodSettable = False
            subnetMaskSettable = False
            defaultGatewaySettable = False
            primaryDnsServerAddressSettable = False
            alternateDnsServerAddressSettable = False
            ipv6Supported = False
            arpRedirectSettable = False
            mtuSettable = False
            hostNameAsTargetAddress = False
            nameAliasSettable = False
            ipv4EnableSettable = False
            ipv6EnableSettable = False
            ipv6PrefixLengthSettable = False
            ipv6PrefixLength = 0
            ipv6DhcpConfigurationSettable = False
            ipv6LinkLocalAutoConfigurationSettable = False
            ipv6RouterAdvertisementConfigurationSettable = False
            ipv6DefaultGatewaySettable = False
            ipv6MaxStaticAddressesSupported = 0

         class IscsiIpv6Address(vmodl.DynamicData): # vim.host.InternetScsiHba.IscsiIpv6Address
            address = ""
            prefixLength = 0
            origin = ""
            operation = ""

            class AddressConfigurationType(Enum): # vim.host.InternetScsiHba.IscsiIpv6Address.AddressConfigurationType
               DHCP = 0
               AutoConfigured = 1
               Static = 2
               Other = 3

            class IPv6AddressOperation(Enum): # vim.host.InternetScsiHba.IscsiIpv6Address.IPv6AddressOperation
               add = 0
               remove = 1

         class IPv6Properties(vmodl.DynamicData): # vim.host.InternetScsiHba.IPv6Properties
            iscsiIpv6Address = [ vim.host.InternetScsiHba.IscsiIpv6Address() ]
            ipv6DhcpConfigurationEnabled = False
            ipv6LinkLocalAutoConfigurationEnabled = False
            ipv6RouterAdvertisementConfigurationEnabled = False
            ipv6DefaultGateway = ""

         class IPProperties(vmodl.DynamicData): # vim.host.InternetScsiHba.IPProperties
            mac = ""
            address = ""
            dhcpConfigurationEnabled = False
            subnetMask = ""
            defaultGateway = ""
            primaryDnsServerAddress = ""
            alternateDnsServerAddress = ""
            ipv6Address = ""
            ipv6SubnetMask = ""
            ipv6DefaultGateway = ""
            arpRedirectEnabled = False
            mtu = 0
            jumboFramesEnabled = False
            ipv4Enabled = False
            ipv6Enabled = False
            ipv6properties = vim.host.InternetScsiHba.IPv6Properties()

         class SendTarget(vmodl.DynamicData): # vim.host.InternetScsiHba.SendTarget
            address = ""
            port = 0
            authenticationProperties = vim.host.InternetScsiHba.AuthenticationProperties()
            digestProperties = vim.host.InternetScsiHba.DigestProperties()
            supportedAdvancedOptions = [ vim.option.OptionDef() ]
            advancedOptions = [ vim.host.InternetScsiHba.ParamValue() ]
            parent = ""

         class StaticTarget(vmodl.DynamicData): # vim.host.InternetScsiHba.StaticTarget
            address = ""
            port = 0
            iScsiName = ""
            discoveryMethod = ""
            authenticationProperties = vim.host.InternetScsiHba.AuthenticationProperties()
            digestProperties = vim.host.InternetScsiHba.DigestProperties()
            supportedAdvancedOptions = [ vim.option.OptionDef() ]
            advancedOptions = [ vim.host.InternetScsiHba.ParamValue() ]
            parent = ""

            class TargetDiscoveryMethod(Enum): # vim.host.InternetScsiHba.StaticTarget.TargetDiscoveryMethod
               staticMethod = 0
               sendTargetMethod = 1
               slpMethod = 2
               isnsMethod = 3
               unknownMethod = 4

         class TargetSet(vmodl.DynamicData): # vim.host.InternetScsiHba.TargetSet
            staticTargets = [ vim.host.InternetScsiHba.StaticTarget() ]
            sendTargets = [ vim.host.InternetScsiHba.SendTarget() ]

         class NetworkBindingSupportType(Enum): # vim.host.InternetScsiHba.NetworkBindingSupportType
            notsupported = 0
            optional = 1
            required = 2

      class InternetScsiTargetTransport(vim.host.TargetTransport): # vim.host.InternetScsiTargetTransport
         iScsiName = ""
         iScsiAlias = ""
         address = [ "" ]

      class NetworkConfig(vmodl.DynamicData): # vim.host.NetworkConfig
         vswitch = [ vim.host.VirtualSwitch.Config() ]
         proxySwitch = [ vim.host.HostProxySwitch.Config() ]
         portgroup = [ vim.host.PortGroup.Config() ]
         pnic = [ vim.host.PhysicalNic.Config() ]
         vnic = [ vim.host.VirtualNic.Config() ]
         consoleVnic = [ vim.host.VirtualNic.Config() ]
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         consoleIpRouteConfig = vim.host.IpRouteConfig()
         routeTableConfig = vim.host.IpRouteTableConfig()
         dhcp = [ vim.host.DhcpService.Config() ]
         nat = [ vim.host.NatService.Config() ]
         ipV6Enabled = False
         netStackSpec = [ vim.host.NetworkConfig.NetStackSpec() ]

         class Result(vmodl.DynamicData): # vim.host.NetworkConfig.Result
            vnicDevice = [ "" ]
            consoleVnicDevice = [ "" ]

         class NetStackSpec(vmodl.DynamicData): # vim.host.NetworkConfig.NetStackSpec
            netStackInstance = vim.host.NetStackInstance()
            operation = ""

      class NetworkSystem(vim.ExtensibleManagedObject): # vim.host.NetworkSystem
         capabilities = vim.host.NetCapabilities()
         networkInfo = vim.host.NetworkInfo()
         offloadCapabilities = vim.host.NetOffloadCapabilities()
         networkConfig = vim.host.NetworkConfig()
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         consoleIpRouteConfig = vim.host.IpRouteConfig()

         def updateNetworkConfig(config=vim.host.NetworkConfig(), changeMode=""): # vim.host.NetworkSystem.updateNetworkConfig
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return vim.host.NetworkConfig.Result()

         def updateDnsConfig(config=vim.host.DnsConfig()): # vim.host.NetworkSystem.updateDnsConfig
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateIpRouteConfig(config=vim.host.IpRouteConfig()): # vim.host.NetworkSystem.updateIpRouteConfig
            # throws vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def updateConsoleIpRouteConfig(config=vim.host.IpRouteConfig()): # vim.host.NetworkSystem.updateConsoleIpRouteConfig
            # throws vim.fault.HostConfigFault
            return None

         def updateIpRouteTableConfig(config=vim.host.IpRouteTableConfig()): # vim.host.NetworkSystem.updateIpRouteTableConfig
            # throws vim.fault.HostConfigFault
            return None

         def addVirtualSwitch(vswitchName="", spec=vim.host.VirtualSwitch.Specification() or None): # vim.host.NetworkSystem.addVirtualSwitch
            # throws vim.fault.AlreadyExists, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def removeVirtualSwitch(vswitchName=""): # vim.host.NetworkSystem.removeVirtualSwitch
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updateVirtualSwitch(vswitchName="", spec=vim.host.VirtualSwitch.Specification()): # vim.host.NetworkSystem.updateVirtualSwitch
            # throws vim.fault.ResourceInUse, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addPortGroup(portgrp=vim.host.PortGroup.Specification()): # vim.host.NetworkSystem.addPortGroup
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removePortGroup(pgName=""): # vim.host.NetworkSystem.removePortGroup
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updatePortGroup(pgName="", portgrp=vim.host.PortGroup.Specification()): # vim.host.NetworkSystem.updatePortGroup
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updatePhysicalNicLinkSpeed(device="", linkSpeed=vim.host.PhysicalNic.LinkSpeedDuplex() or None): # vim.host.NetworkSystem.updatePhysicalNicLinkSpeed
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryNetworkHint(device=[ "" ] or None): # vim.host.NetworkSystem.queryNetworkHint
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.PhysicalNic.NetworkHint() ]

         def addVirtualNic(portgroup="", nic=vim.host.VirtualNic.Specification()): # vim.host.NetworkSystem.addVirtualNic
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault, vim.fault.InvalidState
            return ""

         def removeVirtualNic(device=""): # vim.host.NetworkSystem.removeVirtualNic
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateVirtualNic(device="", nic=vim.host.VirtualNic.Specification()): # vim.host.NetworkSystem.updateVirtualNic
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def addServiceConsoleVirtualNic(portgroup="", nic=vim.host.VirtualNic.Specification()): # vim.host.NetworkSystem.addServiceConsoleVirtualNic
            # throws vim.fault.HostConfigFault
            return ""

         def removeServiceConsoleVirtualNic(device=""): # vim.host.NetworkSystem.removeServiceConsoleVirtualNic
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updateServiceConsoleVirtualNic(device="", nic=vim.host.VirtualNic.Specification()): # vim.host.NetworkSystem.updateServiceConsoleVirtualNic
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def restartServiceConsoleVirtualNic(device=""): # vim.host.NetworkSystem.restartServiceConsoleVirtualNic
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh(): # vim.host.NetworkSystem.refresh
            return None

      class NvmeConnectSpec(vim.host.NvmeSpec): # vim.host.NvmeConnectSpec
         subnqn = ""
         controllerId = 0
         adminQueueSize = 0
         keepAliveTimeout = 0

      class NvmeDiscoverSpec(vim.host.NvmeSpec): # vim.host.NvmeDiscoverSpec
         autoConnect = False

      class NvmeOpaqueTransportParameters(vim.host.NvmeTransportParameters): # vim.host.NvmeOpaqueTransportParameters
         trtype = ""
         traddr = ""
         adrfam = ""
         trsvcid = ""
         tsas = vmodl.Binary()

      class NvmeOverFibreChannelParameters(vim.host.NvmeTransportParameters): # vim.host.NvmeOverFibreChannelParameters
         nodeWorldWideName = 0
         portWorldWideName = 0

      class NvmeOverRdmaParameters(vim.host.NvmeTransportParameters): # vim.host.NvmeOverRdmaParameters
         address = ""
         addressFamily = ""
         portNumber = 0

      class OpaqueNetworkInfo(vmodl.DynamicData): # vim.host.OpaqueNetworkInfo
         opaqueNetworkId = ""
         opaqueNetworkName = ""
         opaqueNetworkType = ""
         pnicZone = [ "" ]
         capability = vim.OpaqueNetwork.Capability()
         extraConfig = [ vim.option.OptionValue() ]

      class ParallelScsiTargetTransport(vim.host.TargetTransport): # vim.host.ParallelScsiTargetTransport
         pass

      class PcieTargetTransport(vim.host.TargetTransport): # vim.host.PcieTargetTransport
         pass

      class RdmaTargetTransport(vim.host.TargetTransport): # vim.host.RdmaTargetTransport
         pass

      class ScsiDisk(vim.host.ScsiLun): # vim.host.ScsiDisk
         capacity = vim.host.DiskDimensions.Lba()
         devicePath = ""
         ssd = False
         localDisk = False
         physicalLocation = [ "" ]
         emulatedDIXDIFEnabled = False
         vsanDiskInfo = vim.vsan.host.VsanDiskInfo()
         scsiDiskType = ""

         class Partition(vmodl.DynamicData): # vim.host.ScsiDisk.Partition
            diskName = ""
            partition = 0

         class ScsiDiskType(Enum): # vim.host.ScsiDisk.ScsiDiskType
            native512 = 0
            emulated512 = 1
            native4k = 2
            SoftwareEmulated4k = 3
            unknown = 4

      class SecuritySpec(vmodl.DynamicData): # vim.host.SecuritySpec
         adminPassword = ""
         removePermission = [ vim.AuthorizationManager.Permission() ]
         addPermission = [ vim.AuthorizationManager.Permission() ]

      class SerialAttachedTargetTransport(vim.host.TargetTransport): # vim.host.SerialAttachedTargetTransport
         pass

      class Summary(vmodl.DynamicData): # vim.host.Summary
         host = vim.HostSystem()
         hardware = vim.host.Summary.HardwareSummary()
         runtime = vim.host.RuntimeInfo()
         config = vim.host.Summary.ConfigSummary()
         quickStats = vim.host.Summary.QuickStats()
         overallStatus = vim.ManagedEntity.Status()
         rebootRequired = False
         customValue = [ vim.CustomFieldsManager.Value() ]
         managementServerIp = ""
         maxEVCModeKey = ""
         currentEVCModeKey = ""
         gateway = vim.host.Summary.GatewaySummary()
         tpmAttestation = vim.host.TpmAttestationInfo()

         class HardwareSummary(vmodl.DynamicData): # vim.host.Summary.HardwareSummary
            vendor = ""
            model = ""
            uuid = ""
            otherIdentifyingInfo = [ vim.host.SystemIdentificationInfo() ]
            memorySize = 0
            cpuModel = ""
            cpuMhz = 0
            numCpuPkgs = 0
            numCpuCores = 0
            numCpuThreads = 0
            numNics = 0
            numHBAs = 0

         class QuickStats(vmodl.DynamicData): # vim.host.Summary.QuickStats
            overallCpuUsage = 0
            overallMemoryUsage = 0
            distributedCpuFairness = 0
            distributedMemoryFairness = 0
            availablePMemCapacity = 0
            uptime = 0

         class ConfigSummary(vmodl.DynamicData): # vim.host.Summary.ConfigSummary
            name = ""
            port = 0
            sslThumbprint = ""
            product = vim.AboutInfo()
            vmotionEnabled = False
            faultToleranceEnabled = False
            featureVersion = [ vim.host.FeatureVersionInfo() ]
            agentVmDatastore = vim.Datastore()
            agentVmNetwork = vim.Network()

         class GatewaySummary(vmodl.DynamicData): # vim.host.Summary.GatewaySummary
            gatewayType = ""
            gatewayId = ""

      class TpmBootSecurityOptionEventDetails(vim.host.TpmEventDetails): # vim.host.TpmBootSecurityOptionEventDetails
         bootSecurityOption = ""

      class TpmCommandEventDetails(vim.host.TpmEventDetails): # vim.host.TpmCommandEventDetails
         commandLine = ""

      class UnresolvedVmfsExtent(vmodl.DynamicData): # vim.host.UnresolvedVmfsExtent
         device = vim.host.ScsiDisk.Partition()
         devicePath = ""
         vmfsUuid = ""
         isHeadExtent = False
         ordinal = 0
         startBlock = 0
         endBlock = 0
         reason = ""

         class UnresolvedReason(Enum): # vim.host.UnresolvedVmfsExtent.UnresolvedReason
            diskIdMismatch = 0
            uuidConflict = 1

      class VFlashManager(vmodl.ManagedObject): # vim.host.VFlashManager
         vFlashConfigInfo = vim.host.VFlashManager.VFlashConfigInfo()

         def configureVFlashResourceEx(devicePath=[ "" ] or None): # vim.host.VFlashManager.configureVFlashResourceEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def configureVFlashResource(spec=vim.host.VFlashManager.VFlashResourceConfigSpec()): # vim.host.VFlashManager.configureVFlashResource
            # throws vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def removeVFlashResource(): # vim.host.VFlashManager.removeVFlashResource
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def configureHostVFlashCache(spec=vim.host.VFlashManager.VFlashCacheConfigSpec()): # vim.host.VFlashManager.configureHostVFlashCache
            # throws vim.fault.HostConfigFault, vim.fault.InaccessibleVFlashSource, vim.fault.ResourceInUse
            return None

         def getVFlashModuleDefaultConfig(vFlashModule=""): # vim.host.VFlashManager.getVFlashModuleDefaultConfig
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.vm.device.VirtualDisk.VFlashCacheConfigInfo()

         class VFlashResourceConfigSpec(vmodl.DynamicData): # vim.host.VFlashManager.VFlashResourceConfigSpec
            vffsUuid = ""

         class VFlashResourceConfigInfo(vmodl.DynamicData): # vim.host.VFlashManager.VFlashResourceConfigInfo
            vffs = vim.host.VffsVolume()
            capacity = 0

         class VFlashResourceRunTimeInfo(vmodl.DynamicData): # vim.host.VFlashManager.VFlashResourceRunTimeInfo
            usage = 0
            capacity = 0
            accessible = False
            capacityForVmCache = 0
            freeForVmCache = 0

         class VFlashCacheConfigSpec(vmodl.DynamicData): # vim.host.VFlashManager.VFlashCacheConfigSpec
            defaultVFlashModule = ""
            swapCacheReservationInGB = 0

         class VFlashCacheConfigInfo(vmodl.DynamicData): # vim.host.VFlashManager.VFlashCacheConfigInfo
            vFlashModuleConfigOption = [ vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption() ]
            defaultVFlashModule = ""
            swapCacheReservationInGB = 0

            class VFlashModuleConfigOption(vmodl.DynamicData): # vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption
               vFlashModule = ""
               vFlashModuleVersion = ""
               minSupportedModuleVersion = ""
               cacheConsistencyType = vim.option.ChoiceOption()
               cacheMode = vim.option.ChoiceOption()
               blockSizeInKBOption = vim.option.LongOption()
               reservationInMBOption = vim.option.LongOption()
               maxDiskSizeInKB = 0

         class VFlashConfigInfo(vmodl.DynamicData): # vim.host.VFlashManager.VFlashConfigInfo
            vFlashResourceConfigInfo = vim.host.VFlashManager.VFlashResourceConfigInfo()
            vFlashCacheConfigInfo = vim.host.VFlashManager.VFlashCacheConfigInfo()

      class VMotionInfo(vmodl.DynamicData): # vim.host.VMotionInfo
         netConfig = vim.host.VMotionSystem.NetConfig()
         ipConfig = vim.host.IpConfig()

      class VffsVolume(vim.host.FileSystemVolume): # vim.host.VffsVolume
         majorVersion = 0
         version = ""
         uuid = ""
         extent = [ vim.host.ScsiDisk.Partition() ]

         class Specification(vmodl.DynamicData): # vim.host.VffsVolume.Specification
            devicePath = ""
            partition = vim.host.DiskPartitionInfo.Specification()
            majorVersion = 0
            volumeName = ""

      class VmfsDatastoreExpandSpec(vim.host.VmfsDatastoreSpec): # vim.host.VmfsDatastoreExpandSpec
         partition = vim.host.DiskPartitionInfo.Specification()
         extent = vim.host.ScsiDisk.Partition()

      class VmfsDatastoreExtendSpec(vim.host.VmfsDatastoreSpec): # vim.host.VmfsDatastoreExtendSpec
         partition = vim.host.DiskPartitionInfo.Specification()
         extent = [ vim.host.ScsiDisk.Partition() ]

      class VmfsVolume(vim.host.FileSystemVolume): # vim.host.VmfsVolume
         blockSizeMb = 0
         blockSize = 0
         unmapGranularity = 0
         unmapPriority = ""
         unmapBandwidthSpec = vim.host.VmfsVolume.UnmapBandwidthSpec()
         maxBlocks = 0
         majorVersion = 0
         version = ""
         uuid = ""
         extent = [ vim.host.ScsiDisk.Partition() ]
         vmfsUpgradable = False
         forceMountedInfo = vim.host.ForceMountedInfo()
         ssd = False
         local = False
         scsiDiskType = ""

         class Specification(vmodl.DynamicData): # vim.host.VmfsVolume.Specification
            extent = vim.host.ScsiDisk.Partition()
            blockSizeMb = 0
            majorVersion = 0
            volumeName = ""
            blockSize = 0
            unmapGranularity = 0
            unmapPriority = ""
            unmapBandwidthSpec = vim.host.VmfsVolume.UnmapBandwidthSpec()

         class UnmapBandwidthSpec(vmodl.DynamicData): # vim.host.VmfsVolume.UnmapBandwidthSpec
            policy = ""
            fixedValue = 0
            dynamicMin = 0
            dynamicMax = 0

         class UnmapPriority(Enum): # vim.host.VmfsVolume.UnmapPriority
            none = 0
            low = 1

         class UnmapBandwidthPolicy(Enum): # vim.host.VmfsVolume.UnmapBandwidthPolicy
            fixed = 0
            dynamic = 1

         class ConfigOption(vmodl.DynamicData): # vim.host.VmfsVolume.ConfigOption
            blockSizeOption = 0
            unmapGranularityOption = [ 0 ]
            unmapBandwidthFixedValue = vim.option.LongOption()
            unmapBandwidthDynamicMin = vim.option.LongOption()
            unmapBandwidthDynamicMax = vim.option.LongOption()
            unmapBandwidthIncrement = 0

      class ConfigInfo(vmodl.DynamicData): # vim.host.ConfigInfo
         host = vim.HostSystem()
         product = vim.AboutInfo()
         deploymentInfo = vim.host.DeploymentInfo()
         hyperThread = vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo()
         consoleReservation = vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo()
         virtualMachineReservation = vim.host.MemoryManagerSystem.VirtualMachineReservationInfo()
         storageDevice = vim.host.StorageDeviceInfo()
         multipathState = vim.host.MultipathStateInfo()
         fileSystemVolume = vim.host.FileSystemVolumeInfo()
         systemFile = [ "" ]
         network = vim.host.NetworkInfo()
         vmotion = vim.host.VMotionInfo()
         virtualNicManagerInfo = vim.host.VirtualNicManagerInfo()
         capabilities = vim.host.NetCapabilities()
         datastoreCapabilities = vim.host.DatastoreSystem.Capabilities()
         offloadCapabilities = vim.host.NetOffloadCapabilities()
         service = vim.host.ServiceInfo()
         firewall = vim.host.FirewallInfo()
         autoStart = vim.host.AutoStartManager.Config()
         activeDiagnosticPartition = vim.host.DiagnosticPartition()
         option = [ vim.option.OptionValue() ]
         optionDef = [ vim.option.OptionDef() ]
         datastorePrincipal = ""
         localSwapDatastore = vim.Datastore()
         systemSwapConfiguration = vim.host.SystemSwapConfiguration()
         systemResources = vim.host.SystemResourceInfo()
         dateTimeInfo = vim.host.DateTimeInfo()
         flags = vim.host.FlagInfo()
         adminDisabled = False
         lockdownMode = vim.host.HostAccessManager.LockdownMode()
         ipmi = vim.host.IpmiInfo()
         sslThumbprintInfo = vim.host.SslThumbprintInfo()
         sslThumbprintData = [ vim.host.SslThumbprintInfo() ]
         certificate = [ 0x00 ]
         pciPassthruInfo = [ vim.host.PciPassthruInfo() ]
         authenticationManagerInfo = vim.host.AuthenticationManagerInfo()
         featureVersion = [ vim.host.FeatureVersionInfo() ]
         powerSystemCapability = vim.host.PowerSystem.Capability()
         powerSystemInfo = vim.host.PowerSystem.Info()
         cacheConfigurationInfo = [ vim.host.CacheConfigurationManager.CacheConfigurationInfo() ]
         wakeOnLanCapable = False
         featureCapability = [ vim.host.FeatureCapability() ]
         maskedFeatureCapability = [ vim.host.FeatureCapability() ]
         vFlashConfigInfo = vim.host.VFlashManager.VFlashConfigInfo()
         vsanHostConfig = vim.vsan.host.ConfigInfo()
         domainList = [ "" ]
         scriptCheckSum = vmodl.Binary()
         hostConfigCheckSum = vmodl.Binary()
         descriptionTreeCheckSum = vmodl.Binary()
         graphicsInfo = [ vim.host.GraphicsInfo() ]
         sharedPassthruGpuTypes = [ "" ]
         graphicsConfig = vim.host.GraphicsConfig()
         sharedGpuCapabilities = [ vim.host.SharedGpuCapabilities() ]
         ioFilterInfo = [ vim.IoFilterManager.HostIoFilterInfo() ]
         sriovDevicePool = [ vim.host.SriovDevicePoolInfo() ]
         assignableHardwareBinding = [ vim.host.AssignableHardwareBinding() ]
         assignableHardwareConfig = vim.host.AssignableHardwareConfig()

      class ConnectInfo(vmodl.DynamicData): # vim.host.ConnectInfo
         serverIp = ""
         inDasCluster = False
         host = vim.host.Summary()
         vm = [ vim.vm.Summary() ]
         vimAccountNameRequired = False
         clusterSupported = False
         network = [ vim.host.ConnectInfo.NetworkInfo() ]
         datastore = [ vim.host.ConnectInfo.DatastoreInfo() ]
         license = vim.host.ConnectInfo.LicenseInfo()
         capability = vim.host.Capability()

         class NetworkInfo(vmodl.DynamicData): # vim.host.ConnectInfo.NetworkInfo
            summary = vim.Network.Summary()

         class NewNetworkInfo(vim.host.ConnectInfo.NetworkInfo): # vim.host.ConnectInfo.NewNetworkInfo
            pass

         class DatastoreInfo(vmodl.DynamicData): # vim.host.ConnectInfo.DatastoreInfo
            summary = vim.Datastore.Summary()

         class DatastoreExistsInfo(vim.host.ConnectInfo.DatastoreInfo): # vim.host.ConnectInfo.DatastoreExistsInfo
            newDatastoreName = ""

         class DatastoreNameConflictInfo(vim.host.ConnectInfo.DatastoreInfo): # vim.host.ConnectInfo.DatastoreNameConflictInfo
            newDatastoreName = ""

         class LicenseInfo(vmodl.DynamicData): # vim.host.ConnectInfo.LicenseInfo
            license = vim.LicenseManager.LicenseInfo()
            evaluation = vim.LicenseManager.EvaluationInfo()
            resource = vim.LicenseManager.LicensableResourceInfo()

      class DiagnosticPartition(vmodl.DynamicData): # vim.host.DiagnosticPartition
         storageType = ""
         diagnosticType = ""
         slots = 0
         id = vim.host.ScsiDisk.Partition()

         class StorageType(Enum): # vim.host.DiagnosticPartition.StorageType
            directAttached = 0
            networkAttached = 1

         class DiagnosticType(Enum): # vim.host.DiagnosticPartition.DiagnosticType
            singleHost = 0
            multiHost = 1

         class CreateOption(vmodl.DynamicData): # vim.host.DiagnosticPartition.CreateOption
            storageType = ""
            diagnosticType = ""
            disk = vim.host.ScsiDisk()

         class CreateSpec(vmodl.DynamicData): # vim.host.DiagnosticPartition.CreateSpec
            storageType = ""
            diagnosticType = ""
            id = vim.host.ScsiDisk.Partition()
            partition = vim.host.DiskPartitionInfo.Specification()
            active = False

         class CreateDescription(vmodl.DynamicData): # vim.host.DiagnosticPartition.CreateDescription
            layout = vim.host.DiskPartitionInfo.Layout()
            diskUuid = ""
            spec = vim.host.DiagnosticPartition.CreateSpec()

      class DiagnosticSystem(vmodl.ManagedObject): # vim.host.DiagnosticSystem
         activePartition = vim.host.DiagnosticPartition()

         def queryAvailablePartition(): # vim.host.DiagnosticSystem.queryAvailablePartition
            # throws vim.fault.HostConfigFault
            return [ vim.host.DiagnosticPartition() ]

         def selectActivePartition(partition=vim.host.ScsiDisk.Partition() or None): # vim.host.DiagnosticSystem.selectActivePartition
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryPartitionCreateOptions(storageType="", diagnosticType=""): # vim.host.DiagnosticSystem.queryPartitionCreateOptions
            # throws vim.fault.HostConfigFault
            return [ vim.host.DiagnosticPartition.CreateOption() ]

         def queryPartitionCreateDesc(diskUuid="", diagnosticType=""): # vim.host.DiagnosticSystem.queryPartitionCreateDesc
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiagnosticPartition.CreateDescription()

         def createDiagnosticPartition(spec=vim.host.DiagnosticPartition.CreateSpec()): # vim.host.DiagnosticSystem.createDiagnosticPartition
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

      class FibreChannelOverEthernetTargetTransport(vim.host.FibreChannelTargetTransport): # vim.host.FibreChannelOverEthernetTargetTransport
         vnportMac = ""
         fcfMac = ""
         vlanId = 0

      class LocalDatastoreInfo(vim.Datastore.Info): # vim.host.LocalDatastoreInfo
         path = ""

      class NasDatastoreInfo(vim.Datastore.Info): # vim.host.NasDatastoreInfo
         nas = vim.host.NasVolume()

      class PMemDatastoreInfo(vim.Datastore.Info): # vim.host.PMemDatastoreInfo
         pmem = vim.host.PMemVolume()

      class RuntimeInfo(vmodl.DynamicData): # vim.host.RuntimeInfo
         connectionState = vim.HostSystem.ConnectionState()
         powerState = vim.HostSystem.PowerState()
         standbyMode = ""
         inMaintenanceMode = False
         inQuarantineMode = False
         bootTime = vmodl.DateTime()
         healthSystemRuntime = vim.host.HealthStatusSystem.Runtime()
         dasHostState = vim.cluster.DasFdmHostState()
         tpmPcrValues = [ vim.host.TpmDigestInfo() ]
         vsanRuntimeInfo = vim.vsan.host.VsanRuntimeInfo()
         networkRuntimeInfo = vim.host.RuntimeInfo.NetworkRuntimeInfo()
         vFlashResourceRuntimeInfo = vim.host.VFlashManager.VFlashResourceRunTimeInfo()
         hostMaxVirtualDiskCapacity = 0
         cryptoState = ""
         cryptoKeyId = vim.encryption.CryptoKeyId()

         class NetStackInstanceRuntimeInfo(vmodl.DynamicData): # vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo
            netStackInstanceKey = ""
            state = ""
            vmknicKeys = [ "" ]
            maxNumberOfConnections = 0
            currentIpV6Enabled = False

            class State(Enum): # vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo.State
               inactive = 0
               active = 1
               deactivating = 2
               activating = 3

         class PlacedVirtualNicIdentifier(vmodl.DynamicData): # vim.host.RuntimeInfo.PlacedVirtualNicIdentifier
            vm = vim.VirtualMachine()
            vnicKey = ""
            reservation = 0

         class PnicNetworkResourceInfo(vmodl.DynamicData): # vim.host.RuntimeInfo.PnicNetworkResourceInfo
            pnicDevice = ""
            availableBandwidthForVMTraffic = 0
            unusedBandwidthForVMTraffic = 0
            placedVirtualNics = [ vim.host.RuntimeInfo.PlacedVirtualNicIdentifier() ]

         class NetworkResourceRuntimeInfo(vmodl.DynamicData): # vim.host.RuntimeInfo.NetworkResourceRuntimeInfo
            pnicResourceInfo = [ vim.host.RuntimeInfo.PnicNetworkResourceInfo() ]

         class NetworkRuntimeInfo(vmodl.DynamicData): # vim.host.RuntimeInfo.NetworkRuntimeInfo
            netStackInstanceRuntimeInfo = [ vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo() ]
            networkResourceRuntime = vim.host.RuntimeInfo.NetworkResourceRuntimeInfo()

      class StorageSystem(vim.ExtensibleManagedObject): # vim.host.StorageSystem
         storageDeviceInfo = vim.host.StorageDeviceInfo()
         fileSystemVolumeInfo = vim.host.FileSystemVolumeInfo()
         systemFile = [ "" ]
         multipathStateInfo = vim.host.MultipathStateInfo()

         def retrieveDiskPartitionInfo(devicePath=[ "" ]): # vim.host.StorageSystem.retrieveDiskPartitionInfo
            return [ vim.host.DiskPartitionInfo() ]

         def computeDiskPartitionInfo(devicePath="", layout=vim.host.DiskPartitionInfo.Layout(), partitionFormat="" or None): # vim.host.StorageSystem.computeDiskPartitionInfo
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiskPartitionInfo()

         def computeDiskPartitionInfoForResize(partition=vim.host.ScsiDisk.Partition(), blockRange=vim.host.DiskPartitionInfo.BlockRange(), partitionFormat="" or None): # vim.host.StorageSystem.computeDiskPartitionInfoForResize
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiskPartitionInfo()

         def updateDiskPartitions(devicePath="", spec=vim.host.DiskPartitionInfo.Specification()): # vim.host.StorageSystem.updateDiskPartitions
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def formatVmfs(createSpec=vim.host.VmfsVolume.Specification()): # vim.host.StorageSystem.formatVmfs
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.host.VmfsVolume()

         def mountVmfsVolume(vmfsUuid=""): # vim.host.StorageSystem.mountVmfsVolume
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVmfsVolume(vmfsUuid=""): # vim.host.StorageSystem.unmountVmfsVolume
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVmfsVolumeEx(vmfsUuid=[ "" ]): # vim.host.StorageSystem.unmountVmfsVolumeEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def mountVmfsVolumeEx(vmfsUuid=[ "" ]): # vim.host.StorageSystem.mountVmfsVolumeEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def unmapVmfsVolumeEx(vmfsUuid=[ "" ]): # vim.host.StorageSystem.unmapVmfsVolumeEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def deleteVmfsVolumeState(vmfsUuid=""): # vim.host.StorageSystem.deleteVmfsVolumeState
            # throws vim.fault.HostConfigFault
            return None

         def rescanVmfs(): # vim.host.StorageSystem.rescanVmfs
            # throws vim.fault.HostConfigFault
            return None

         def attachVmfsExtent(vmfsPath="", extent=vim.host.ScsiDisk.Partition()): # vim.host.StorageSystem.attachVmfsExtent
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def expandVmfsExtent(vmfsPath="", extent=vim.host.ScsiDisk.Partition()): # vim.host.StorageSystem.expandVmfsExtent
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def upgradeVmfs(vmfsPath=""): # vim.host.StorageSystem.upgradeVmfs
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def upgradeVmLayout(): # vim.host.StorageSystem.upgradeVmLayout
            return None

         def queryUnresolvedVmfsVolume(): # vim.host.StorageSystem.queryUnresolvedVmfsVolume
            return [ vim.host.UnresolvedVmfsVolume() ]

         def resolveMultipleUnresolvedVmfsVolumes(resolutionSpec=[ vim.host.UnresolvedVmfsResolutionSpec() ]): # vim.host.StorageSystem.resolveMultipleUnresolvedVmfsVolumes
            # throws vim.fault.HostConfigFault
            return [ vim.host.UnresolvedVmfsResolutionResult() ]

         def resolveMultipleUnresolvedVmfsVolumesEx(resolutionSpec=[ vim.host.UnresolvedVmfsResolutionSpec() ]): # vim.host.StorageSystem.resolveMultipleUnresolvedVmfsVolumesEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def unmountForceMountedVmfsVolume(vmfsUuid=""): # vim.host.StorageSystem.unmountForceMountedVmfsVolume
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def rescanHba(hbaDevice=""): # vim.host.StorageSystem.rescanHba
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def rescanAllHba(): # vim.host.StorageSystem.rescanAllHba
            # throws vim.fault.HostConfigFault
            return None

         def updateSoftwareInternetScsiEnabled(enabled=False): # vim.host.StorageSystem.updateSoftwareInternetScsiEnabled
            # throws vim.fault.HostConfigFault
            return None

         def updateInternetScsiDiscoveryProperties(iScsiHbaDevice="", discoveryProperties=vim.host.InternetScsiHba.DiscoveryProperties()): # vim.host.StorageSystem.updateInternetScsiDiscoveryProperties
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAuthenticationProperties(iScsiHbaDevice="", authenticationProperties=vim.host.InternetScsiHba.AuthenticationProperties(), targetSet=vim.host.InternetScsiHba.TargetSet() or None): # vim.host.StorageSystem.updateInternetScsiAuthenticationProperties
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiDigestProperties(iScsiHbaDevice="", targetSet=vim.host.InternetScsiHba.TargetSet() or None, digestProperties=vim.host.InternetScsiHba.DigestProperties()): # vim.host.StorageSystem.updateInternetScsiDigestProperties
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAdvancedOptions(iScsiHbaDevice="", targetSet=vim.host.InternetScsiHba.TargetSet() or None, options=[ vim.host.InternetScsiHba.ParamValue() ]): # vim.host.StorageSystem.updateInternetScsiAdvancedOptions
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiIPProperties(iScsiHbaDevice="", ipProperties=vim.host.InternetScsiHba.IPProperties()): # vim.host.StorageSystem.updateInternetScsiIPProperties
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiName(iScsiHbaDevice="", iScsiName=""): # vim.host.StorageSystem.updateInternetScsiName
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAlias(iScsiHbaDevice="", iScsiAlias=""): # vim.host.StorageSystem.updateInternetScsiAlias
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addInternetScsiSendTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.SendTarget() ]): # vim.host.StorageSystem.addInternetScsiSendTargets
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeInternetScsiSendTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.SendTarget() ]): # vim.host.StorageSystem.removeInternetScsiSendTargets
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addInternetScsiStaticTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.StaticTarget() ]): # vim.host.StorageSystem.addInternetScsiStaticTargets
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeInternetScsiStaticTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.StaticTarget() ]): # vim.host.StorageSystem.removeInternetScsiStaticTargets
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def enableMultipathPath(pathName=""): # vim.host.StorageSystem.enableMultipathPath
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableMultipathPath(pathName=""): # vim.host.StorageSystem.disableMultipathPath
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def setMultipathLunPolicy(lunId="", policy=vim.host.MultipathInfo.LogicalUnitPolicy()): # vim.host.StorageSystem.setMultipathLunPolicy
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateHppMultipathLunPolicy(lunId="", policy=vim.host.MultipathInfo.HppLogicalUnitPolicy()): # vim.host.StorageSystem.updateHppMultipathLunPolicy
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryPathSelectionPolicyOptions(): # vim.host.StorageSystem.queryPathSelectionPolicyOptions
            # throws vim.fault.HostConfigFault
            return [ vim.host.PathSelectionPolicyOption() ]

         def queryStorageArrayTypePolicyOptions(): # vim.host.StorageSystem.queryStorageArrayTypePolicyOptions
            # throws vim.fault.HostConfigFault
            return [ vim.host.StorageArrayTypePolicyOption() ]

         def updateScsiLunDisplayName(lunUuid="", displayName=""): # vim.host.StorageSystem.updateScsiLunDisplayName
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidName, vim.fault.DuplicateName
            return None

         def detachScsiLun(lunUuid=""): # vim.host.StorageSystem.detachScsiLun
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState, vim.fault.ResourceInUse
            return None

         def detachScsiLunEx(lunUuid=[ "" ]): # vim.host.StorageSystem.detachScsiLunEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def deleteScsiLunState(lunCanonicalName=""): # vim.host.StorageSystem.deleteScsiLunState
            # throws vim.fault.HostConfigFault
            return None

         def attachScsiLun(lunUuid=""): # vim.host.StorageSystem.attachScsiLun
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def attachScsiLunEx(lunUuid=[ "" ]): # vim.host.StorageSystem.attachScsiLunEx
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def refresh(): # vim.host.StorageSystem.refresh
            return None

         def discoverFcoeHbas(fcoeSpec=vim.host.FcoeConfig.FcoeSpecification()): # vim.host.StorageSystem.discoverFcoeHbas
            # throws vim.fault.FcoeFaultPnicHasNoPortSet, vim.fault.HostConfigFault, vim.fault.NotFound
            return None

         def markForRemoval(hbaName="", remove=False): # vim.host.StorageSystem.markForRemoval
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def formatVffs(createSpec=vim.host.VffsVolume.Specification()): # vim.host.StorageSystem.formatVffs
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return vim.host.VffsVolume()

         def extendVffs(vffsPath="", devicePath="", spec=vim.host.DiskPartitionInfo.Specification() or None): # vim.host.StorageSystem.extendVffs
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def destroyVffs(vffsPath=""): # vim.host.StorageSystem.destroyVffs
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def mountVffsVolume(vffsUuid=""): # vim.host.StorageSystem.mountVffsVolume
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVffsVolume(vffsUuid=""): # vim.host.StorageSystem.unmountVffsVolume
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def deleteVffsVolumeState(vffsUuid=""): # vim.host.StorageSystem.deleteVffsVolumeState
            # throws vim.fault.HostConfigFault
            return None

         def rescanVffs(): # vim.host.StorageSystem.rescanVffs
            # throws vim.fault.HostConfigFault
            return None

         def queryAvailableSsds(vffsPath="" or None): # vim.host.StorageSystem.queryAvailableSsds
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.ScsiDisk() ]

         def setNFSUser(user="", password=""): # vim.host.StorageSystem.setNFSUser
            # throws vim.fault.HostConfigFault
            return None

         def changeNFSUserPassword(password=""): # vim.host.StorageSystem.changeNFSUserPassword
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryNFSUser(): # vim.host.StorageSystem.queryNFSUser
            # throws vim.fault.HostConfigFault
            return vim.host.NasVolume.UserInfo()

         def clearNFSUser(): # vim.host.StorageSystem.clearNFSUser
            # throws vim.fault.HostConfigFault
            return None

         def turnDiskLocatorLedOn(scsiDiskUuids=[ "" ]): # vim.host.StorageSystem.turnDiskLocatorLedOn
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def turnDiskLocatorLedOff(scsiDiskUuids=[ "" ]): # vim.host.StorageSystem.turnDiskLocatorLedOff
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def markAsSsd(scsiDiskUuid=""): # vim.host.StorageSystem.markAsSsd
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsNonSsd(scsiDiskUuid=""): # vim.host.StorageSystem.markAsNonSsd
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsLocal(scsiDiskUuid=""): # vim.host.StorageSystem.markAsLocal
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsNonLocal(scsiDiskUuid=""): # vim.host.StorageSystem.markAsNonLocal
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def updateVmfsUnmapPriority(vmfsUuid="", unmapPriority=""): # vim.host.StorageSystem.updateVmfsUnmapPriority
            return None

         def updateVmfsUnmapBandwidth(vmfsUuid="", unmapBandwidthSpec=vim.host.VmfsVolume.UnmapBandwidthSpec()): # vim.host.StorageSystem.updateVmfsUnmapBandwidth
            return None

         def queryVmfsConfigOption(): # vim.host.StorageSystem.queryVmfsConfigOption
            return [ vim.host.VmfsVolume.ConfigOption() ]

         def markPerenniallyReserved(lunUuid="", state=False): # vim.host.StorageSystem.markPerenniallyReserved
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def markPerenniallyReservedEx(lunUuid=[ "" ] or None, state=False): # vim.host.StorageSystem.markPerenniallyReservedEx
            return vim.Task()

         def createNvmeOverRdmaAdapter(rdmaDeviceName=""): # vim.host.StorageSystem.createNvmeOverRdmaAdapter
            # throws vim.fault.ResourceInUse, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeNvmeOverRdmaAdapter(hbaDeviceName=""): # vim.host.StorageSystem.removeNvmeOverRdmaAdapter
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def discoverNvmeControllers(discoverSpec=vim.host.NvmeDiscoverSpec()): # vim.host.StorageSystem.discoverNvmeControllers
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.NvmeDiscoveryLog()

         def connectNvmeController(connectSpec=vim.host.NvmeConnectSpec()): # vim.host.StorageSystem.connectNvmeController
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disconnectNvmeController(disconnectSpec=vim.host.NvmeDisconnectSpec()): # vim.host.StorageSystem.disconnectNvmeController
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         class VmfsVolumeResult(vmodl.DynamicData): # vim.host.StorageSystem.VmfsVolumeResult
            key = ""
            fault = vmodl.MethodFault()

         class ScsiLunResult(vmodl.DynamicData): # vim.host.StorageSystem.ScsiLunResult
            key = ""
            fault = vmodl.MethodFault()

         class DiskLocatorLedResult(vmodl.DynamicData): # vim.host.StorageSystem.DiskLocatorLedResult
            key = ""
            fault = vmodl.MethodFault()

      class VMotionManager(object): # (unknown name)

         class SrcInstantCloneResult(vmodl.DynamicData): # vim.host.VMotionManager.SrcInstantCloneResult
            startTime = 0
            quiesceTime = 0
            quiesceDoneTime = 0
            resumeDoneTime = 0
            endTime = 0

         class DstInstantCloneResult(vmodl.DynamicData): # vim.host.VMotionManager.DstInstantCloneResult
            dstVmId = 0
            startTime = 0
            cptLoadTime = 0
            cptLoadDoneTime = 0
            replicateMemDoneTime = 0
            endTime = 0
            cptXferTime = 0
            cptCacheUsed = 0
            devCptStreamSize = 0
            devCptStreamTime = 0

      class VmfsDatastoreCreateSpec(vim.host.VmfsDatastoreSpec): # vim.host.VmfsDatastoreCreateSpec
         partition = vim.host.DiskPartitionInfo.Specification()
         vmfs = vim.host.VmfsVolume.Specification()
         extent = [ vim.host.ScsiDisk.Partition() ]

      class VmfsDatastoreInfo(vim.Datastore.Info): # vim.host.VmfsDatastoreInfo
         maxPhysicalRDMFileSize = 0
         maxVirtualRDMFileSize = 0
         vmfs = vim.host.VmfsVolume()

      class VvolDatastoreInfo(vim.Datastore.Info): # vim.host.VvolDatastoreInfo
         vvolDS = vim.host.VvolVolume()

   class net(object): # (unknown name)

      class DhcpConfigInfo(vmodl.DynamicData): # vim.net.DhcpConfigInfo
         ipv6 = vim.net.DhcpConfigInfo.DhcpOptions()
         ipv4 = vim.net.DhcpConfigInfo.DhcpOptions()

         class DhcpOptions(vmodl.DynamicData): # vim.net.DhcpConfigInfo.DhcpOptions
            enable = False
            config = [ vim.KeyValue() ]

      class DhcpConfigSpec(vmodl.DynamicData): # vim.net.DhcpConfigSpec
         ipv6 = vim.net.DhcpConfigSpec.DhcpOptionsSpec()
         ipv4 = vim.net.DhcpConfigSpec.DhcpOptionsSpec()

         class DhcpOptionsSpec(vmodl.DynamicData): # vim.net.DhcpConfigSpec.DhcpOptionsSpec
            enable = False
            config = [ vim.KeyValue() ]
            operation = ""

      class DnsConfigInfo(vmodl.DynamicData): # vim.net.DnsConfigInfo
         dhcp = False
         hostName = ""
         domainName = ""
         ipAddress = [ "" ]
         searchDomain = [ "" ]

      class DnsConfigSpec(vmodl.DynamicData): # vim.net.DnsConfigSpec
         dhcp = False
         hostName = ""
         domainName = ""
         ipAddress = [ "" ]
         searchDomain = [ "" ]

      class IpConfigInfo(vmodl.DynamicData): # vim.net.IpConfigInfo
         ipAddress = [ vim.net.IpConfigInfo.IpAddress() ]
         dhcp = vim.net.DhcpConfigInfo()
         autoConfigurationEnabled = False

         class IpAddressOrigin(Enum): # vim.net.IpConfigInfo.IpAddressOrigin
            other = 0
            manual = 1
            dhcp = 2
            linklayer = 3
            random = 4

         class IpAddressStatus(Enum): # vim.net.IpConfigInfo.IpAddressStatus
            preferred = 0
            deprecated = 1
            invalid = 2
            inaccessible = 3
            unknown = 4
            tentative = 5
            duplicate = 6

         class IpAddress(vmodl.DynamicData): # vim.net.IpConfigInfo.IpAddress
            ipAddress = ""
            prefixLength = 0
            origin = ""
            state = ""
            lifetime = vmodl.DateTime()

      class IpConfigSpec(vmodl.DynamicData): # vim.net.IpConfigSpec
         ipAddress = [ vim.net.IpConfigSpec.IpAddressSpec() ]
         dhcp = vim.net.DhcpConfigSpec()
         autoConfigurationEnabled = False

         class IpAddressSpec(vmodl.DynamicData): # vim.net.IpConfigSpec.IpAddressSpec
            ipAddress = ""
            prefixLength = 0
            operation = ""

      class IpRouteConfigInfo(vmodl.DynamicData): # vim.net.IpRouteConfigInfo
         ipRoute = [ vim.net.IpRouteConfigInfo.IpRoute() ]

         class Gateway(vmodl.DynamicData): # vim.net.IpRouteConfigInfo.Gateway
            ipAddress = ""
            device = ""

         class IpRoute(vmodl.DynamicData): # vim.net.IpRouteConfigInfo.IpRoute
            network = ""
            prefixLength = 0
            gateway = vim.net.IpRouteConfigInfo.Gateway()

      class IpRouteConfigSpec(vmodl.DynamicData): # vim.net.IpRouteConfigSpec
         ipRoute = [ vim.net.IpRouteConfigSpec.IpRouteSpec() ]

         class GatewaySpec(vmodl.DynamicData): # vim.net.IpRouteConfigSpec.GatewaySpec
            ipAddress = ""
            device = ""

         class IpRouteSpec(vmodl.DynamicData): # vim.net.IpRouteConfigSpec.IpRouteSpec
            network = ""
            prefixLength = 0
            gateway = vim.net.IpRouteConfigSpec.GatewaySpec()
            operation = ""

      class IpStackInfo(vmodl.DynamicData): # vim.net.IpStackInfo
         neighbor = [ vim.net.IpStackInfo.NetToMedia() ]
         defaultRouter = [ vim.net.IpStackInfo.DefaultRouter() ]

         class EntryType(Enum): # vim.net.IpStackInfo.EntryType
            other = 0
            invalid = 1
            dynamic = 2
            manual = 3

         class Preference(Enum): # vim.net.IpStackInfo.Preference
            reserved = 0
            low = 1
            medium = 2
            high = 3

         class NetToMedia(vmodl.DynamicData): # vim.net.IpStackInfo.NetToMedia
            ipAddress = ""
            physicalAddress = ""
            device = ""
            type = ""

         class DefaultRouter(vmodl.DynamicData): # vim.net.IpStackInfo.DefaultRouter
            ipAddress = ""
            device = ""
            lifetime = vmodl.DateTime()
            preference = ""

      class NetBIOSConfigInfo(vmodl.DynamicData): # vim.net.NetBIOSConfigInfo
         mode = ""

         class Mode(Enum): # vim.net.NetBIOSConfigInfo.Mode
            unknown = 0
            enabled = 1
            disabled = 2
            enabledViaDHCP = 3

      class WinNetBIOSConfigInfo(vim.net.NetBIOSConfigInfo): # vim.net.WinNetBIOSConfigInfo
         primaryWINS = ""
         secondaryWINS = ""

   class option(object): # (unknown name)

      class ArrayUpdateSpec(vmodl.DynamicData): # vim.option.ArrayUpdateSpec
         operation = vim.option.ArrayUpdateSpec.Operation()
         removeKey = {}

         class Operation(Enum): # vim.option.ArrayUpdateSpec.Operation
            add = 0
            remove = 1
            edit = 2

      class OptionDef(vim.ElementDescription): # vim.option.OptionDef
         optionType = vim.option.OptionType()

      class OptionManager(vmodl.ManagedObject): # vim.option.OptionManager
         supportedOption = [ vim.option.OptionDef() ]
         setting = [ vim.option.OptionValue() ]

         def queryView(name="" or None): # vim.option.OptionManager.queryView
            # throws vim.fault.InvalidName
            return [ vim.option.OptionValue() ]

         def updateValues(changedValue=[ vim.option.OptionValue() ]): # vim.option.OptionManager.updateValues
            # throws vim.fault.InvalidName
            return None

      class OptionType(vmodl.DynamicData): # vim.option.OptionType
         valueIsReadonly = False

      class OptionValue(vmodl.DynamicData): # vim.option.OptionValue
         key = ""
         value = {}

      class StringOption(vim.option.OptionType): # vim.option.StringOption
         defaultValue = ""
         validCharacters = ""

      class BoolOption(vim.option.OptionType): # vim.option.BoolOption
         supported = False
         defaultValue = False

      class ChoiceOption(vim.option.OptionType): # vim.option.ChoiceOption
         choiceInfo = [ vim.ElementDescription() ]
         defaultIndex = 0

      class FloatOption(vim.option.OptionType): # vim.option.FloatOption
         min = 0.0
         max = 0.0
         defaultValue = 0.0

      class IntOption(vim.option.OptionType): # vim.option.IntOption
         min = 0
         max = 0
         defaultValue = 0

      class LongOption(vim.option.OptionType): # vim.option.LongOption
         min = 0
         max = 0
         defaultValue = 0

   class profile(object): # (unknown name)

      class ApplyProfile(vmodl.DynamicData): # vim.profile.ApplyProfile
         enabled = False
         policy = [ vim.profile.Policy() ]
         profileTypeName = ""
         profileVersion = ""
         property = [ vim.profile.ApplyProfileProperty() ]
         favorite = False
         toBeMerged = False
         toReplaceWith = False
         toBeDeleted = False
         copyEnableStatus = False
         hidden = False

      class ApplyProfileElement(vim.profile.ApplyProfile): # vim.profile.ApplyProfileElement
         key = ""

      class ApplyProfileProperty(vmodl.DynamicData): # vim.profile.ApplyProfileProperty
         propertyName = ""
         array = False
         profile = [ vim.profile.ApplyProfile() ]

      class ComplianceLocator(vmodl.DynamicData): # vim.profile.ComplianceLocator
         expressionName = ""
         applyPath = vim.profile.ProfilePropertyPath()

      class ComplianceManager(vmodl.ManagedObject): # vim.profile.ComplianceManager

         def checkCompliance(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None): # vim.profile.ComplianceManager.checkCompliance
            return vim.Task()

         def queryComplianceStatus(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None): # vim.profile.ComplianceManager.queryComplianceStatus
            return [ vim.profile.ComplianceResult() ]

         def clearComplianceStatus(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None): # vim.profile.ComplianceManager.clearComplianceStatus
            return None

         def queryExpressionMetadata(expressionName=[ "" ] or None, profile=vim.profile.Profile() or None): # vim.profile.ComplianceManager.queryExpressionMetadata
            return [ vim.profile.ExpressionMetadata() ]

      class ComplianceProfile(vmodl.DynamicData): # vim.profile.ComplianceProfile
         expression = [ vim.profile.Expression() ]
         rootExpression = ""

      class ComplianceResult(vmodl.DynamicData): # vim.profile.ComplianceResult
         profile = vim.profile.Profile()
         complianceStatus = ""
         entity = vim.ManagedEntity()
         checkTime = vmodl.DateTime()
         failure = [ vim.profile.ComplianceResult.ComplianceFailure() ]

         class Status(Enum): # vim.profile.ComplianceResult.Status
            compliant = 0
            nonCompliant = 1
            unknown = 2
            running = 3

         class ComplianceFailure(vmodl.DynamicData): # vim.profile.ComplianceResult.ComplianceFailure
            failureType = ""
            message = vmodl.LocalizableMessage()
            expressionName = ""
            failureValues = [ vim.profile.ComplianceResult.ComplianceFailure.ComplianceFailureValues() ]

            class ComplianceFailureValues(vmodl.DynamicData): # vim.profile.ComplianceResult.ComplianceFailure.ComplianceFailureValues
               comparisonIdentifier = ""
               profileInstance = ""
               hostValue = {}
               profileValue = {}

      class DeferredPolicyOptionParameter(vmodl.DynamicData): # vim.profile.DeferredPolicyOptionParameter
         inputPath = vim.profile.ProfilePropertyPath()
         parameter = [ vmodl.KeyAnyValue() ]

      class Expression(vmodl.DynamicData): # vim.profile.Expression
         id = ""
         displayName = ""
         negated = False

      class ExpressionMetadata(vmodl.DynamicData): # vim.profile.ExpressionMetadata
         expressionId = vim.ExtendedElementDescription()
         parameter = [ vim.profile.ParameterMetadata() ]

      class NumericComparator(Enum): # vim.profile.NumericComparator
         lessThan = 0
         lessThanEqual = 1
         equal = 2
         notEqual = 3
         greaterThanEqual = 4
         greaterThan = 5

      class ParameterMetadata(vmodl.DynamicData): # vim.profile.ParameterMetadata
         id = vim.ExtendedElementDescription()
         type = vmodl.TypeName()
         optional = False
         defaultValue = {}
         hidden = False
         securitySensitive = False
         readOnly = False
         parameterRelations = [ vim.profile.ParameterMetadata.ParameterRelationMetadata() ]

         class RelationType(Enum): # vim.profile.ParameterMetadata.RelationType
            dynamic_relation = 0
            extensible_relation = 1
            localizable_relation = 2
            static_relation = 3
            validation_relation = 4

         class ParameterRelationMetadata(vmodl.DynamicData): # vim.profile.ParameterMetadata.ParameterRelationMetadata
            relationTypes = [ "" ]
            values = [ {} ]
            path = vim.profile.ProfilePropertyPath()
            minCount = 0
            maxCount = 0

      class Policy(vmodl.DynamicData): # vim.profile.Policy
         id = ""
         policyOption = vim.profile.PolicyOption()

      class PolicyMetadata(vmodl.DynamicData): # vim.profile.PolicyMetadata
         id = vim.ExtendedElementDescription()
         possibleOption = [ vim.profile.PolicyOptionMetadata() ]

      class PolicyOption(vmodl.DynamicData): # vim.profile.PolicyOption
         id = ""
         parameter = [ vmodl.KeyAnyValue() ]

      class PolicyOptionMetadata(vmodl.DynamicData): # vim.profile.PolicyOptionMetadata
         id = vim.ExtendedElementDescription()
         parameter = [ vim.profile.ParameterMetadata() ]

      class Profile(vmodl.ManagedObject): # vim.profile.Profile
         config = vim.profile.Profile.ConfigInfo()
         description = vim.profile.Profile.Description()
         name = ""
         createdTime = vmodl.DateTime()
         modifiedTime = vmodl.DateTime()
         entity = [ vim.ManagedEntity() ]
         complianceStatus = ""

         def retrieveDescription(): # vim.profile.Profile.retrieveDescription
            return vim.profile.Profile.Description()

         def destroy(): # vim.profile.Profile.destroy
            return None

         def associateEntities(entity=[ vim.ManagedEntity() ]): # vim.profile.Profile.associateEntities
            return None

         def dissociateEntities(entity=[ vim.ManagedEntity() ] or None): # vim.profile.Profile.dissociateEntities
            return None

         def checkCompliance(entity=[ vim.ManagedEntity() ] or None): # vim.profile.Profile.checkCompliance
            return vim.Task()

         def exportProfile(): # vim.profile.Profile.exportProfile
            return ""

         class CreateSpec(vmodl.DynamicData): # vim.profile.Profile.CreateSpec
            name = ""
            annotation = ""
            enabled = False

         class SerializedCreateSpec(vim.profile.Profile.CreateSpec): # vim.profile.Profile.SerializedCreateSpec
            profileConfigString = ""

         class ConfigInfo(vmodl.DynamicData): # vim.profile.Profile.ConfigInfo
            name = ""
            annotation = ""
            enabled = False

         class Description(vmodl.DynamicData): # vim.profile.Profile.Description
            section = [ vim.profile.Profile.Description.Section() ]

            class Section(vmodl.DynamicData): # vim.profile.Profile.Description.Section
               description = vim.ExtendedElementDescription()
               message = [ vmodl.LocalizableMessage() ]

      class ProfileManager(vmodl.ManagedObject): # vim.profile.ProfileManager
         profile = [ vim.profile.Profile() ]

         def createProfile(createSpec=vim.profile.Profile.CreateSpec()): # vim.profile.ProfileManager.createProfile
            # throws vim.fault.DuplicateName
            return vim.profile.Profile()

         def queryPolicyMetadata(policyName=[ "" ] or None, profile=vim.profile.Profile() or None): # vim.profile.ProfileManager.queryPolicyMetadata
            return [ vim.profile.PolicyMetadata() ]

         def findAssociatedProfile(entity=vim.ManagedEntity()): # vim.profile.ProfileManager.findAssociatedProfile
            return [ vim.profile.Profile() ]

      class ProfileMetadata(vmodl.DynamicData): # vim.profile.ProfileMetadata
         key = vmodl.TypeName()
         profileTypeName = ""
         description = vim.ExtendedDescription()
         sortSpec = [ vim.profile.ProfileMetadata.ProfileSortSpec() ]
         profileCategory = ""
         profileComponent = ""
         operationMessages = [ vim.profile.ProfileMetadata.ProfileOperationMessage() ]

         class ProfileSortSpec(vmodl.DynamicData): # vim.profile.ProfileMetadata.ProfileSortSpec
            policyId = ""
            parameter = ""

         class ProfileOperationMessage(vmodl.DynamicData): # vim.profile.ProfileMetadata.ProfileOperationMessage
            operationName = ""
            message = vmodl.LocalizableMessage()

      class ProfilePropertyPath(vmodl.DynamicData): # vim.profile.ProfilePropertyPath
         profilePath = vmodl.PropertyPath()
         policyId = ""
         parameterId = ""
         policyOptionId = ""

      class ProfileStructure(vmodl.DynamicData): # vim.profile.ProfileStructure
         profileTypeName = ""
         child = [ vim.profile.ProfileStructureProperty() ]

      class ProfileStructureProperty(vmodl.DynamicData): # vim.profile.ProfileStructureProperty
         propertyName = ""
         array = False
         element = vim.profile.ProfileStructure()

      class SimpleExpression(vim.profile.Expression): # vim.profile.SimpleExpression
         expressionType = ""
         parameter = [ vmodl.KeyAnyValue() ]

      class UserInputRequiredParameterMetadata(vim.profile.PolicyOptionMetadata): # vim.profile.UserInputRequiredParameterMetadata
         userInputParameter = [ vim.profile.ParameterMetadata() ]

      class cluster(object): # (unknown name)

         class ClusterProfile(vim.profile.Profile): # vim.profile.cluster.ClusterProfile

            def update(config=vim.profile.cluster.ClusterProfile.ConfigSpec()): # vim.profile.cluster.ClusterProfile.update
               # throws vim.fault.DuplicateName
               return None

            class ConfigInfo(vim.profile.Profile.ConfigInfo): # vim.profile.cluster.ClusterProfile.ConfigInfo
               complyProfile = vim.profile.ComplianceProfile()

            class CreateSpec(vim.profile.Profile.CreateSpec): # vim.profile.cluster.ClusterProfile.CreateSpec
               pass

            class ConfigSpec(vim.profile.cluster.ClusterProfile.CreateSpec): # vim.profile.cluster.ClusterProfile.ConfigSpec
               pass

            class CompleteConfigSpec(vim.profile.cluster.ClusterProfile.ConfigSpec): # vim.profile.cluster.ClusterProfile.CompleteConfigSpec
               complyProfile = vim.profile.ComplianceProfile()

            class ServiceType(Enum): # vim.profile.cluster.ClusterProfile.ServiceType
               DRS = 0
               HA = 1
               DPM = 2
               FT = 3

            class ConfigServiceCreateSpec(vim.profile.cluster.ClusterProfile.ConfigSpec): # vim.profile.cluster.ClusterProfile.ConfigServiceCreateSpec
               serviceType = [ "" ]

         class ProfileManager(vim.profile.ProfileManager): # vim.profile.cluster.ProfileManager
            pass

      class host(object): # (unknown name)

         class ActiveDirectoryProfile(vim.profile.ApplyProfile): # vim.profile.host.ActiveDirectoryProfile
            pass

         class AnswerFile(vmodl.DynamicData): # vim.profile.host.AnswerFile
            userInput = [ vim.profile.DeferredPolicyOptionParameter() ]
            createdTime = vmodl.DateTime()
            modifiedTime = vmodl.DateTime()

         class AnswerFileStatusResult(vmodl.DynamicData): # vim.profile.host.AnswerFileStatusResult
            checkedTime = vmodl.DateTime()
            host = vim.HostSystem()
            status = ""
            error = [ vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError() ]

            class AnswerFileStatusError(vmodl.DynamicData): # vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError
               userInputPath = vim.profile.ProfilePropertyPath()
               errMsg = vmodl.LocalizableMessage()

         class AuthenticationProfile(vim.profile.ApplyProfile): # vim.profile.host.AuthenticationProfile
            activeDirectory = vim.profile.host.ActiveDirectoryProfile()

         class DateTimeProfile(vim.profile.ApplyProfile): # vim.profile.host.DateTimeProfile
            pass

         class DvsProfile(vim.profile.ApplyProfile): # vim.profile.host.DvsProfile
            key = ""
            name = ""
            uplink = [ vim.profile.host.PnicUplinkProfile() ]

         class DvsVNicProfile(vim.profile.ApplyProfile): # vim.profile.host.DvsVNicProfile
            key = ""
            ipConfig = vim.profile.host.IpAddressProfile()

         class ExecuteResult(vmodl.DynamicData): # vim.profile.host.ExecuteResult
            status = ""
            configSpec = vim.host.ConfigSpec()
            inapplicablePath = [ vmodl.PropertyPath() ]
            requireInput = [ vim.profile.DeferredPolicyOptionParameter() ]
            error = [ vim.profile.host.ExecuteResult.ExecuteError() ]

            class Status(Enum): # vim.profile.host.ExecuteResult.Status
               success = 0
               needInput = 1
               error = 2

            class ExecuteError(vmodl.DynamicData): # vim.profile.host.ExecuteResult.ExecuteError
               path = vim.profile.ProfilePropertyPath()
               message = vmodl.LocalizableMessage()

         class FirewallProfile(vim.profile.ApplyProfile): # vim.profile.host.FirewallProfile
            ruleset = [ vim.profile.host.FirewallProfile.RulesetProfile() ]

            class RulesetProfile(vim.profile.ApplyProfile): # vim.profile.host.FirewallProfile.RulesetProfile
               key = ""

         class HostApplyProfile(vim.profile.ApplyProfile): # vim.profile.host.HostApplyProfile
            memory = vim.profile.host.HostMemoryProfile()
            storage = vim.profile.host.StorageProfile()
            network = vim.profile.host.NetworkProfile()
            datetime = vim.profile.host.DateTimeProfile()
            firewall = vim.profile.host.FirewallProfile()
            security = vim.profile.host.SecurityProfile()
            service = [ vim.profile.host.ServiceProfile() ]
            option = [ vim.profile.host.OptionProfile() ]
            userAccount = [ vim.profile.host.UserProfile() ]
            usergroupAccount = [ vim.profile.host.UserGroupProfile() ]
            authentication = vim.profile.host.AuthenticationProfile()

         class HostMemoryProfile(vim.profile.ApplyProfile): # vim.profile.host.HostMemoryProfile
            pass

         class HostSpecification(vmodl.DynamicData): # vim.profile.host.HostSpecification
            createdTime = vmodl.DateTime()
            lastModified = vmodl.DateTime()
            host = vim.HostSystem()
            subSpecs = [ vim.profile.host.HostSubSpecification() ]
            changeID = ""

         class HostSpecificationManager(vmodl.ManagedObject): # vim.profile.host.HostSpecificationManager

            def updateHostSpecification(host=vim.HostSystem(), hostSpec=vim.profile.host.HostSpecification()): # vim.profile.host.HostSpecificationManager.updateHostSpecification
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def updateHostSubSpecification(host=vim.HostSystem(), hostSubSpec=vim.profile.host.HostSubSpecification()): # vim.profile.host.HostSpecificationManager.updateHostSubSpecification
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def retrieveHostSpecification(host=vim.HostSystem(), fromHost=False): # vim.profile.host.HostSpecificationManager.retrieveHostSpecification
               # throws vim.fault.HostSpecificationOperationFailed
               return vim.profile.host.HostSpecification()

            def deleteHostSubSpecification(host=vim.HostSystem(), subSpecName=""): # vim.profile.host.HostSpecificationManager.deleteHostSubSpecification
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def deleteHostSpecification(host=vim.HostSystem()): # vim.profile.host.HostSpecificationManager.deleteHostSpecification
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def getUpdatedHosts(startChangeID="" or None, endChangeID="" or None): # vim.profile.host.HostSpecificationManager.getUpdatedHosts
               return [ vim.HostSystem() ]

         class HostSubSpecification(vmodl.DynamicData): # vim.profile.host.HostSubSpecification
            name = ""
            createdTime = vmodl.DateTime()
            data = [ 0x00 ]
            binaryData = vmodl.Binary()

         class IpAddressProfile(vim.profile.ApplyProfile): # vim.profile.host.IpAddressProfile
            pass

         class IpRouteProfile(vim.profile.ApplyProfile): # vim.profile.host.IpRouteProfile
            staticRoute = [ vim.profile.host.StaticRouteProfile() ]

         class NasStorageProfile(vim.profile.ApplyProfile): # vim.profile.host.NasStorageProfile
            key = ""

         class NetworkPolicyProfile(vim.profile.ApplyProfile): # vim.profile.host.NetworkPolicyProfile
            pass

         class NetworkProfile(vim.profile.ApplyProfile): # vim.profile.host.NetworkProfile
            vswitch = [ vim.profile.host.VirtualSwitchProfile() ]
            vmPortGroup = [ vim.profile.host.VmPortGroupProfile() ]
            hostPortGroup = [ vim.profile.host.HostPortGroupProfile() ]
            serviceConsolePortGroup = [ vim.profile.host.ServiceConsolePortGroupProfile() ]
            dnsConfig = vim.profile.host.NetworkProfile.DnsConfigProfile()
            ipRouteConfig = vim.profile.host.IpRouteProfile()
            consoleIpRouteConfig = vim.profile.host.IpRouteProfile()
            pnic = [ vim.profile.host.PhysicalNicProfile() ]
            dvswitch = [ vim.profile.host.DvsProfile() ]
            dvsServiceConsoleNic = [ vim.profile.host.DvsServiceConsoleVNicProfile() ]
            dvsHostNic = [ vim.profile.host.DvsHostVNicProfile() ]
            nsxHostNic = [ vim.profile.host.NsxHostVNicProfile() ]
            netStackInstance = [ vim.profile.host.NetStackInstanceProfile() ]
            opaqueSwitch = vim.profile.host.OpaqueSwitchProfile()

            class DnsConfigProfile(vim.profile.ApplyProfile): # vim.profile.host.NetworkProfile.DnsConfigProfile
               pass

         class NsxHostVNicProfile(vim.profile.ApplyProfile): # vim.profile.host.NsxHostVNicProfile
            key = ""
            ipConfig = vim.profile.host.IpAddressProfile()

         class OpaqueSwitchProfile(vim.profile.ApplyProfile): # vim.profile.host.OpaqueSwitchProfile
            pass

         class OptionProfile(vim.profile.ApplyProfile): # vim.profile.host.OptionProfile
            key = ""

         class PermissionProfile(vim.profile.ApplyProfile): # vim.profile.host.PermissionProfile
            key = ""

         class PhysicalNicProfile(vim.profile.ApplyProfile): # vim.profile.host.PhysicalNicProfile
            key = ""

         class PnicUplinkProfile(vim.profile.ApplyProfile): # vim.profile.host.PnicUplinkProfile
            key = ""

         class PortGroupProfile(vim.profile.ApplyProfile): # vim.profile.host.PortGroupProfile
            key = ""
            name = ""
            vlan = vim.profile.host.PortGroupProfile.VlanProfile()
            vswitch = vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile()
            networkPolicy = vim.profile.host.NetworkPolicyProfile()

            class VlanProfile(vim.profile.ApplyProfile): # vim.profile.host.PortGroupProfile.VlanProfile
               pass

            class VirtualSwitchSelectionProfile(vim.profile.ApplyProfile): # vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile
               pass

         class SecurityProfile(vim.profile.ApplyProfile): # vim.profile.host.SecurityProfile
            permission = [ vim.profile.host.PermissionProfile() ]

         class ServiceConsolePortGroupProfile(vim.profile.host.PortGroupProfile): # vim.profile.host.ServiceConsolePortGroupProfile
            ipConfig = vim.profile.host.IpAddressProfile()

         class ServiceProfile(vim.profile.ApplyProfile): # vim.profile.host.ServiceProfile
            key = ""

         class StaticRouteProfile(vim.profile.ApplyProfile): # vim.profile.host.StaticRouteProfile
            key = ""

         class StorageProfile(vim.profile.ApplyProfile): # vim.profile.host.StorageProfile
            nasStorage = [ vim.profile.host.NasStorageProfile() ]

         class UserGroupProfile(vim.profile.ApplyProfile): # vim.profile.host.UserGroupProfile
            key = ""

         class UserProfile(vim.profile.ApplyProfile): # vim.profile.host.UserProfile
            key = ""

         class VirtualSwitchProfile(vim.profile.ApplyProfile): # vim.profile.host.VirtualSwitchProfile
            key = ""
            name = ""
            link = vim.profile.host.VirtualSwitchProfile.LinkProfile()
            numPorts = vim.profile.host.VirtualSwitchProfile.NumPortsProfile()
            networkPolicy = vim.profile.host.NetworkPolicyProfile()

            class LinkProfile(vim.profile.ApplyProfile): # vim.profile.host.VirtualSwitchProfile.LinkProfile
               pass

            class NumPortsProfile(vim.profile.ApplyProfile): # vim.profile.host.VirtualSwitchProfile.NumPortsProfile
               pass

         class VmPortGroupProfile(vim.profile.host.PortGroupProfile): # vim.profile.host.VmPortGroupProfile
            pass

         class profileEngine(object): # (unknown name)

            class AnswerFileValidationInfo(object): # (unknown name)

               class Status(Enum): # vim.profile.host.profileEngine.AnswerFileValidationInfo.Status
                  success = 0
                  failed = 1
                  failed_defaults = 2

         class DvsHostVNicProfile(vim.profile.host.DvsVNicProfile): # vim.profile.host.DvsHostVNicProfile
            pass

         class DvsServiceConsoleVNicProfile(vim.profile.host.DvsVNicProfile): # vim.profile.host.DvsServiceConsoleVNicProfile
            pass

         class HostPortGroupProfile(vim.profile.host.PortGroupProfile): # vim.profile.host.HostPortGroupProfile
            ipConfig = vim.profile.host.IpAddressProfile()

         class HostProfile(vim.profile.Profile): # vim.profile.host.HostProfile
            validationState = ""
            validationStateUpdateTime = vmodl.DateTime()
            validationFailureInfo = vim.profile.host.HostProfile.ValidationFailureInfo()
            referenceHost = vim.HostSystem()

            def ResetValidationState(): # vim.profile.host.HostProfile.ResetValidationState
               return None

            def updateReferenceHost(host=vim.HostSystem() or None): # vim.profile.host.HostProfile.updateReferenceHost
               return None

            def update(config=vim.profile.host.HostProfile.ConfigSpec()): # vim.profile.host.HostProfile.update
               # throws vim.fault.DuplicateName, vim.fault.ProfileUpdateFailed
               return None

            def execute(host=vim.HostSystem(), deferredParam=[ vim.profile.DeferredPolicyOptionParameter() ] or None): # vim.profile.host.HostProfile.execute
               return vim.profile.host.ExecuteResult()

            class ConfigInfo(vim.profile.Profile.ConfigInfo): # vim.profile.host.HostProfile.ConfigInfo
               applyProfile = vim.profile.host.HostApplyProfile()
               defaultComplyProfile = vim.profile.ComplianceProfile()
               defaultComplyLocator = [ vim.profile.ComplianceLocator() ]
               customComplyProfile = vim.profile.ComplianceProfile()
               disabledExpressionList = [ "" ]
               description = vim.profile.Profile.Description()

            class ConfigSpec(vim.profile.Profile.CreateSpec): # vim.profile.host.HostProfile.ConfigSpec
               pass

            class SerializedHostProfileSpec(vim.profile.Profile.SerializedCreateSpec): # vim.profile.host.HostProfile.SerializedHostProfileSpec
               validatorHost = vim.HostSystem()
               validating = False

            class CompleteConfigSpec(vim.profile.host.HostProfile.ConfigSpec): # vim.profile.host.HostProfile.CompleteConfigSpec
               applyProfile = vim.profile.host.HostApplyProfile()
               customComplyProfile = vim.profile.ComplianceProfile()
               disabledExpressionListChanged = False
               disabledExpressionList = [ "" ]
               validatorHost = vim.HostSystem()
               validating = False
               hostConfig = vim.profile.host.HostProfile.ConfigInfo()

            class HostBasedConfigSpec(vim.profile.host.HostProfile.ConfigSpec): # vim.profile.host.HostProfile.HostBasedConfigSpec
               host = vim.HostSystem()
               useHostProfileEngine = False

            class ValidationState(Enum): # vim.profile.host.HostProfile.ValidationState
               Ready = 0
               Running = 1
               Failed = 2

            class ValidationFailureInfo(vmodl.DynamicData): # vim.profile.host.HostProfile.ValidationFailureInfo
               name = ""
               annotation = ""
               updateType = ""
               host = vim.HostSystem()
               applyProfile = vim.profile.host.HostApplyProfile()
               failures = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]
               faults = [ vmodl.MethodFault() ]

               class UpdateType(Enum): # vim.profile.host.HostProfile.ValidationFailureInfo.UpdateType
                  HostBased = 0
                  Import = 1
                  Edit = 2
                  Compose = 3

         class NetStackInstanceProfile(vim.profile.ApplyProfile): # vim.profile.host.NetStackInstanceProfile
            key = ""
            dnsConfig = vim.profile.host.NetworkProfile.DnsConfigProfile()
            ipRouteConfig = vim.profile.host.IpRouteProfile()

         class ProfileManager(vim.profile.ProfileManager): # vim.profile.host.ProfileManager

            def applyHostConfiguration(host=vim.HostSystem(), configSpec=vim.host.ConfigSpec(), userInput=[ vim.profile.DeferredPolicyOptionParameter() ] or None): # vim.profile.host.ProfileManager.applyHostConfiguration
               # throws vim.fault.InvalidState, vim.fault.HostConfigFailed
               return vim.Task()

            def generateConfigTaskList(configSpec=vim.host.ConfigSpec(), host=vim.HostSystem()): # vim.profile.host.ProfileManager.generateConfigTaskList
               return vim.profile.host.ProfileManager.ConfigTaskList()

            def generateTaskList(configSpec=vim.host.ConfigSpec(), host=vim.HostSystem()): # vim.profile.host.ProfileManager.generateTaskList
               return vim.Task()

            def queryProfileMetadata(profileName=[ vmodl.TypeName() ] or None, profile=vim.profile.Profile() or None): # vim.profile.host.ProfileManager.queryProfileMetadata
               return [ vim.profile.ProfileMetadata() ]

            def queryProfileStructure(profile=vim.profile.Profile() or None): # vim.profile.host.ProfileManager.queryProfileStructure
               return vim.profile.ProfileStructure()

            def createDefaultProfile(profileType=vmodl.TypeName(), profileTypeName="" or None, profile=vim.profile.Profile() or None): # vim.profile.host.ProfileManager.createDefaultProfile
               return vim.profile.ApplyProfile()

            def updateAnswerFile(host=vim.HostSystem(), configSpec=vim.profile.host.ProfileManager.AnswerFileCreateSpec()): # vim.profile.host.ProfileManager.updateAnswerFile
               # throws vim.fault.AnswerFileUpdateFailed
               return vim.Task()

            def retrieveAnswerFile(host=vim.HostSystem()): # vim.profile.host.ProfileManager.retrieveAnswerFile
               return vim.profile.host.AnswerFile()

            def retrieveAnswerFileForProfile(host=vim.HostSystem(), applyProfile=vim.profile.host.HostApplyProfile()): # vim.profile.host.ProfileManager.retrieveAnswerFileForProfile
               return vim.profile.host.AnswerFile()

            def exportAnswerFile(host=vim.HostSystem()): # vim.profile.host.ProfileManager.exportAnswerFile
               return vim.Task()

            def checkAnswerFileStatus(host=[ vim.HostSystem() ]): # vim.profile.host.ProfileManager.checkAnswerFileStatus
               return vim.Task()

            def queryAnswerFileStatus(host=[ vim.HostSystem() ]): # vim.profile.host.ProfileManager.queryAnswerFileStatus
               return [ vim.profile.host.AnswerFileStatusResult() ]

            def updateHostCustomizations(hostToConfigSpecMap=[ vim.profile.host.ProfileManager.HostToConfigSpecMap() ] or None): # vim.profile.host.ProfileManager.updateHostCustomizations
               return vim.Task()

            def retrieveHostCustomizations(hosts=[ vim.HostSystem() ] or None): # vim.profile.host.ProfileManager.retrieveHostCustomizations
               return [ vim.profile.host.ProfileManager.StructuredCustomizations() ]

            def retrieveHostCustomizationsForProfile(hosts=[ vim.HostSystem() ] or None, applyProfile=vim.profile.host.HostApplyProfile()): # vim.profile.host.ProfileManager.retrieveHostCustomizationsForProfile
               return [ vim.profile.host.ProfileManager.StructuredCustomizations() ]

            def generateHostConfigTaskSpec(hostsInfo=[ vim.profile.host.ProfileManager.StructuredCustomizations() ] or None): # vim.profile.host.ProfileManager.generateHostConfigTaskSpec
               return vim.Task()

            def applyEntitiesConfiguration(applyConfigSpecs=[ vim.profile.host.ProfileManager.ApplyHostConfigSpec() ] or None): # vim.profile.host.ProfileManager.applyEntitiesConfiguration
               return vim.Task()

            def validateComposition(source=vim.profile.Profile(), targets=[ vim.profile.Profile() ] or None, toBeMerged=vim.profile.host.HostApplyProfile() or None, toReplaceWith=vim.profile.host.HostApplyProfile() or None, toBeDeleted=vim.profile.host.HostApplyProfile() or None, enableStatusToBeCopied=vim.profile.host.HostApplyProfile() or None, errorOnly=False or None): # vim.profile.host.ProfileManager.validateComposition
               return vim.Task()

            def compositeProfile(source=vim.profile.Profile(), targets=[ vim.profile.Profile() ] or None, toBeMerged=vim.profile.host.HostApplyProfile() or None, toBeReplacedWith=vim.profile.host.HostApplyProfile() or None, toBeDeleted=vim.profile.host.HostApplyProfile() or None, enableStatusToBeCopied=vim.profile.host.HostApplyProfile() or None): # vim.profile.host.ProfileManager.compositeProfile
               return vim.Task()

            class TaskListRequirement(Enum): # vim.profile.host.ProfileManager.TaskListRequirement
               maintenanceModeRequired = 0
               rebootRequired = 1

            class ConfigTaskList(vmodl.DynamicData): # vim.profile.host.ProfileManager.ConfigTaskList
               configSpec = vim.host.ConfigSpec()
               taskDescription = [ vmodl.LocalizableMessage() ]
               taskListRequirement = [ "" ]

            class AnswerFileCreateSpec(vmodl.DynamicData): # vim.profile.host.ProfileManager.AnswerFileCreateSpec
               validating = False

            class AnswerFileOptionsCreateSpec(vim.profile.host.ProfileManager.AnswerFileCreateSpec): # vim.profile.host.ProfileManager.AnswerFileOptionsCreateSpec
               userInput = [ vim.profile.DeferredPolicyOptionParameter() ]

            class AnswerFileSerializedCreateSpec(vim.profile.host.ProfileManager.AnswerFileCreateSpec): # vim.profile.host.ProfileManager.AnswerFileSerializedCreateSpec
               answerFileConfigString = ""

            class AnswerFileStatus(Enum): # vim.profile.host.ProfileManager.AnswerFileStatus
               valid = 0
               invalid = 1
               unknown = 2

            class EntityCustomizations(vmodl.DynamicData): # vim.profile.host.ProfileManager.EntityCustomizations
               pass

            class StructuredCustomizations(vim.profile.host.ProfileManager.EntityCustomizations): # vim.profile.host.ProfileManager.StructuredCustomizations
               entity = vim.ManagedEntity()
               customizations = vim.profile.host.AnswerFile()

            class HostToConfigSpecMap(vmodl.DynamicData): # vim.profile.host.ProfileManager.HostToConfigSpecMap
               host = vim.HostSystem()
               configSpec = vim.profile.host.ProfileManager.AnswerFileCreateSpec()

            class ApplyHostConfigSpec(vim.profile.host.ExecuteResult): # vim.profile.host.ProfileManager.ApplyHostConfigSpec
               host = vim.HostSystem()
               taskListRequirement = [ "" ]
               taskDescription = [ vmodl.LocalizableMessage() ]
               rebootStateless = False
               rebootHost = False
               faultData = vmodl.MethodFault()

            class ApplyHostConfigResult(vmodl.DynamicData): # vim.profile.host.ProfileManager.ApplyHostConfigResult
               startTime = vmodl.DateTime()
               completeTime = vmodl.DateTime()
               host = vim.HostSystem()
               status = ""
               errors = [ vmodl.MethodFault() ]

               class Status(Enum): # vim.profile.host.ProfileManager.ApplyHostConfigResult.Status
                  success = 0
                  failed = 1
                  reboot_failed = 2
                  stateless_reboot_failed = 3
                  check_compliance_failed = 4
                  state_not_satisfied = 5
                  exit_maintenancemode_failed = 6
                  canceled = 7

            class CompositionValidationResult(vmodl.DynamicData): # vim.profile.host.ProfileManager.CompositionValidationResult
               results = [ vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement() ]
               errors = [ vmodl.LocalizableMessage() ]

               class ResultElement(vmodl.DynamicData): # vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement
                  target = vim.profile.Profile()
                  status = ""
                  errors = [ vmodl.LocalizableMessage() ]
                  sourceDiffForToBeMerged = vim.profile.host.HostApplyProfile()
                  targetDiffForToBeMerged = vim.profile.host.HostApplyProfile()
                  toBeAdded = vim.profile.host.HostApplyProfile()
                  toBeDeleted = vim.profile.host.HostApplyProfile()
                  toBeDisabled = vim.profile.host.HostApplyProfile()
                  toBeEnabled = vim.profile.host.HostApplyProfile()
                  toBeReenableCC = vim.profile.host.HostApplyProfile()

                  class Status(Enum): # vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement.Status
                     success = 0
                     error = 1

            class CompositionResult(vmodl.DynamicData): # vim.profile.host.ProfileManager.CompositionResult
               errors = [ vmodl.LocalizableMessage() ]
               results = [ vim.profile.host.ProfileManager.CompositionResult.ResultElement() ]

               class ResultElement(vmodl.DynamicData): # vim.profile.host.ProfileManager.CompositionResult.ResultElement
                  target = vim.profile.Profile()
                  status = ""
                  errors = [ vmodl.LocalizableMessage() ]

                  class Status(Enum): # vim.profile.host.ProfileManager.CompositionResult.ResultElement.Status
                     success = 0
                     error = 1

      class CompositeExpression(vim.profile.Expression): # vim.profile.CompositeExpression
         operator = ""
         expressionName = [ "" ]

      class CompositePolicyOption(vim.profile.PolicyOption): # vim.profile.CompositePolicyOption
         option = [ vim.profile.PolicyOption() ]

      class CompositePolicyOptionMetadata(vim.profile.PolicyOptionMetadata): # vim.profile.CompositePolicyOptionMetadata
         option = [ "" ]

   class scheduler(object): # (unknown name)

      class ScheduledTask(vim.ExtensibleManagedObject): # vim.scheduler.ScheduledTask
         info = vim.scheduler.ScheduledTaskInfo()

         def remove(): # vim.scheduler.ScheduledTask.remove
            # throws vim.fault.InvalidState
            return None

         def reconfigure(spec=vim.scheduler.ScheduledTaskSpec()): # vim.scheduler.ScheduledTask.reconfigure
            # throws vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.DuplicateName
            return None

         def run(): # vim.scheduler.ScheduledTask.run
            # throws vim.fault.InvalidState
            return None

      class ScheduledTaskDescription(vmodl.DynamicData): # vim.scheduler.ScheduledTaskDescription
         action = [ vim.TypeDescription() ]
         schedulerInfo = [ vim.scheduler.ScheduledTaskDescription.SchedulerDetail() ]
         state = [ vim.ElementDescription() ]
         dayOfWeek = [ vim.ElementDescription() ]
         weekOfMonth = [ vim.ElementDescription() ]

         class SchedulerDetail(vim.TypeDescription): # vim.scheduler.ScheduledTaskDescription.SchedulerDetail
            frequency = ""

      class ScheduledTaskManager(vmodl.ManagedObject): # vim.scheduler.ScheduledTaskManager
         scheduledTask = [ vim.scheduler.ScheduledTask() ]
         description = vim.scheduler.ScheduledTaskDescription()

         def create(entity=vim.ManagedEntity(), spec=vim.scheduler.ScheduledTaskSpec()): # vim.scheduler.ScheduledTaskManager.create
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.scheduler.ScheduledTask()

         def retrieveEntityScheduledTask(entity=vim.ManagedEntity() or None): # vim.scheduler.ScheduledTaskManager.retrieveEntityScheduledTask
            return [ vim.scheduler.ScheduledTask() ]

         def createObjectScheduledTask(obj=vmodl.ManagedObject(), spec=vim.scheduler.ScheduledTaskSpec()): # vim.scheduler.ScheduledTaskManager.createObjectScheduledTask
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.scheduler.ScheduledTask()

         def retrieveObjectScheduledTask(obj=vmodl.ManagedObject() or None): # vim.scheduler.ScheduledTaskManager.retrieveObjectScheduledTask
            return [ vim.scheduler.ScheduledTask() ]

      class ScheduledTaskSpec(vmodl.DynamicData): # vim.scheduler.ScheduledTaskSpec
         name = ""
         description = ""
         enabled = False
         scheduler = vim.scheduler.TaskScheduler()
         action = vim.action.Action()
         notification = ""

      class TaskScheduler(vmodl.DynamicData): # vim.scheduler.TaskScheduler
         activeTime = vmodl.DateTime()
         expireTime = vmodl.DateTime()

      class AfterStartupTaskScheduler(vim.scheduler.TaskScheduler): # vim.scheduler.AfterStartupTaskScheduler
         minute = 0

      class OnceTaskScheduler(vim.scheduler.TaskScheduler): # vim.scheduler.OnceTaskScheduler
         runAt = vmodl.DateTime()

      class RecurrentTaskScheduler(vim.scheduler.TaskScheduler): # vim.scheduler.RecurrentTaskScheduler
         interval = 0

      class ScheduledTaskInfo(vim.scheduler.ScheduledTaskSpec): # vim.scheduler.ScheduledTaskInfo
         scheduledTask = vim.scheduler.ScheduledTask()
         entity = vim.ManagedEntity()
         lastModifiedTime = vmodl.DateTime()
         lastModifiedUser = ""
         nextRunTime = vmodl.DateTime()
         prevRunTime = vmodl.DateTime()
         state = vim.TaskInfo.State()
         error = vmodl.MethodFault()
         result = {}
         progress = 0
         activeTask = vim.Task()
         taskObject = vmodl.ManagedObject()

      class HourlyTaskScheduler(vim.scheduler.RecurrentTaskScheduler): # vim.scheduler.HourlyTaskScheduler
         minute = 0

      class DailyTaskScheduler(vim.scheduler.HourlyTaskScheduler): # vim.scheduler.DailyTaskScheduler
         hour = 0

      class MonthlyTaskScheduler(vim.scheduler.DailyTaskScheduler): # vim.scheduler.MonthlyTaskScheduler
         pass

      class WeeklyTaskScheduler(vim.scheduler.DailyTaskScheduler): # vim.scheduler.WeeklyTaskScheduler
         sunday = False
         monday = False
         tuesday = False
         wednesday = False
         thursday = False
         friday = False
         saturday = False

      class MonthlyByDayTaskScheduler(vim.scheduler.MonthlyTaskScheduler): # vim.scheduler.MonthlyByDayTaskScheduler
         day = 0

      class MonthlyByWeekdayTaskScheduler(vim.scheduler.MonthlyTaskScheduler): # vim.scheduler.MonthlyByWeekdayTaskScheduler
         offset = vim.scheduler.MonthlyByWeekdayTaskScheduler.WeekOfMonth()
         weekday = vim.scheduler.MonthlyByWeekdayTaskScheduler.DayOfWeek()

         class DayOfWeek(Enum): # vim.scheduler.MonthlyByWeekdayTaskScheduler.DayOfWeek
            sunday = 0
            monday = 1
            tuesday = 2
            wednesday = 3
            thursday = 4
            friday = 5
            saturday = 6

         class WeekOfMonth(Enum): # vim.scheduler.MonthlyByWeekdayTaskScheduler.WeekOfMonth
            first = 0
            second = 1
            third = 2
            fourth = 3
            last = 4

   class storageDrs(object): # (unknown name)

      class ApplyRecommendationResult(vmodl.DynamicData): # vim.storageDrs.ApplyRecommendationResult
         vm = vim.VirtualMachine()

      class AutomationConfig(vmodl.DynamicData): # vim.storageDrs.AutomationConfig
         spaceLoadBalanceAutomationMode = ""
         ioLoadBalanceAutomationMode = ""
         ruleEnforcementAutomationMode = ""
         policyEnforcementAutomationMode = ""
         vmEvacuationAutomationMode = ""

      class ConfigInfo(vmodl.DynamicData): # vim.storageDrs.ConfigInfo
         podConfig = vim.storageDrs.PodConfigInfo()
         vmConfig = [ vim.storageDrs.VmConfigInfo() ]

      class ConfigSpec(vmodl.DynamicData): # vim.storageDrs.ConfigSpec
         podConfigSpec = vim.storageDrs.PodConfigSpec()
         vmConfigSpec = [ vim.storageDrs.VmConfigSpec() ]

      class HbrDiskMigrationAction(vim.cluster.Action): # vim.storageDrs.HbrDiskMigrationAction
         collectionId = ""
         collectionName = ""
         diskIds = [ "" ]
         source = vim.Datastore()
         destination = vim.Datastore()
         sizeTransferred = 0
         spaceUtilSrcBefore = 0.0
         spaceUtilDstBefore = 0.0
         spaceUtilSrcAfter = 0.0
         spaceUtilDstAfter = 0.0
         ioLatencySrcBefore = 0.0
         ioLatencyDstBefore = 0.0

      class IoLoadBalanceConfig(vmodl.DynamicData): # vim.storageDrs.IoLoadBalanceConfig
         reservablePercentThreshold = 0
         reservableIopsThreshold = 0
         reservableThresholdMode = ""
         ioLatencyThreshold = 0
         ioLoadImbalanceThreshold = 0

      class OptionSpec(vim.option.ArrayUpdateSpec): # vim.storageDrs.OptionSpec
         option = vim.option.OptionValue()

      class PlacementAffinityRule(vmodl.DynamicData): # vim.storageDrs.PlacementAffinityRule
         ruleType = ""
         ruleScope = ""
         vms = [ vim.VirtualMachine() ]
         keys = [ "" ]

         class RuleType(Enum): # vim.storageDrs.PlacementAffinityRule.RuleType
            affinity = 0
            antiAffinity = 1
            softAffinity = 2
            softAntiAffinity = 3

         class RuleScope(Enum): # vim.storageDrs.PlacementAffinityRule.RuleScope
            cluster = 0
            host = 1
            storagePod = 2
            datastore = 3

      class PlacementRankResult(vmodl.DynamicData): # vim.storageDrs.PlacementRankResult
         key = ""
         candidate = vim.ClusterComputeResource()
         reservedSpaceMB = 0
         usedSpaceMB = 0
         totalSpaceMB = 0
         utilization = 0.0
         faults = [ vmodl.MethodFault() ]

      class PlacementRankSpec(vmodl.DynamicData): # vim.storageDrs.PlacementRankSpec
         specs = [ vim.cluster.PlacementSpec() ]
         clusters = [ vim.ClusterComputeResource() ]
         rules = [ vim.storageDrs.PlacementAffinityRule() ]
         placementRankByVm = [ vim.storageDrs.PlacementRankVmSpec() ]

      class PlacementRankVmSpec(vmodl.DynamicData): # vim.storageDrs.PlacementRankVmSpec
         vmPlacementSpec = vim.cluster.PlacementSpec()
         vmClusters = [ vim.ClusterComputeResource() ]

      class PodConfigInfo(vmodl.DynamicData): # vim.storageDrs.PodConfigInfo
         enabled = False
         ioLoadBalanceEnabled = False
         defaultVmBehavior = ""
         loadBalanceInterval = 0
         defaultIntraVmAffinity = False
         spaceLoadBalanceConfig = vim.storageDrs.SpaceLoadBalanceConfig()
         ioLoadBalanceConfig = vim.storageDrs.IoLoadBalanceConfig()
         automationOverrides = vim.storageDrs.AutomationConfig()
         rule = [ vim.cluster.RuleInfo() ]
         option = [ vim.option.OptionValue() ]

         class Behavior(Enum): # vim.storageDrs.PodConfigInfo.Behavior
            manual = 0
            automated = 1

      class PodConfigSpec(vmodl.DynamicData): # vim.storageDrs.PodConfigSpec
         enabled = False
         ioLoadBalanceEnabled = False
         defaultVmBehavior = ""
         loadBalanceInterval = 0
         defaultIntraVmAffinity = False
         spaceLoadBalanceConfig = vim.storageDrs.SpaceLoadBalanceConfig()
         ioLoadBalanceConfig = vim.storageDrs.IoLoadBalanceConfig()
         automationOverrides = vim.storageDrs.AutomationConfig()
         rule = [ vim.cluster.RuleSpec() ]
         option = [ vim.storageDrs.OptionSpec() ]

      class SpaceLoadBalanceConfig(vmodl.DynamicData): # vim.storageDrs.SpaceLoadBalanceConfig
         spaceThresholdMode = ""
         spaceUtilizationThreshold = 0
         freeSpaceThresholdGB = 0
         minSpaceUtilizationDifference = 0

         class SpaceThresholdMode(Enum): # vim.storageDrs.SpaceLoadBalanceConfig.SpaceThresholdMode
            utilization = 0
            freeSpace = 1

      class StorageMigrationAction(vim.cluster.Action): # vim.storageDrs.StorageMigrationAction
         vm = vim.VirtualMachine()
         relocateSpec = vim.vm.RelocateSpec()
         source = vim.Datastore()
         destination = vim.Datastore()
         sizeTransferred = 0
         spaceUtilSrcBefore = 0.0
         spaceUtilDstBefore = 0.0
         spaceUtilSrcAfter = 0.0
         spaceUtilDstAfter = 0.0
         ioLatencySrcBefore = 0.0
         ioLatencyDstBefore = 0.0

      class StoragePlacementAction(vim.cluster.Action): # vim.storageDrs.StoragePlacementAction
         vm = vim.VirtualMachine()
         relocateSpec = vim.vm.RelocateSpec()
         destination = vim.Datastore()
         spaceUtilBefore = 0.0
         spaceDemandBefore = 0.0
         spaceUtilAfter = 0.0
         spaceDemandAfter = 0.0
         ioLatencyBefore = 0.0

      class StoragePlacementResult(vmodl.DynamicData): # vim.storageDrs.StoragePlacementResult
         recommendations = [ vim.cluster.Recommendation() ]
         drsFault = vim.cluster.DrsFaults()
         task = vim.Task()

      class VmConfigInfo(vmodl.DynamicData): # vim.storageDrs.VmConfigInfo
         vm = vim.VirtualMachine()
         enabled = False
         behavior = ""
         intraVmAffinity = False
         intraVmAntiAffinity = vim.storageDrs.VirtualDiskAntiAffinityRuleSpec()
         virtualDiskRules = [ vim.storageDrs.VirtualDiskRuleSpec() ]

      class VmConfigSpec(vim.option.ArrayUpdateSpec): # vim.storageDrs.VmConfigSpec
         info = vim.storageDrs.VmConfigInfo()

      class PodSelectionSpec(vmodl.DynamicData): # vim.storageDrs.PodSelectionSpec
         initialVmConfig = [ vim.storageDrs.PodSelectionSpec.VmPodConfig() ]
         storagePod = vim.StoragePod()

         class VmPodConfig(vmodl.DynamicData): # vim.storageDrs.PodSelectionSpec.VmPodConfig
            storagePod = vim.StoragePod()
            disk = [ vim.storageDrs.PodSelectionSpec.DiskLocator() ]
            vmConfig = vim.storageDrs.VmConfigInfo()
            interVmRule = [ vim.cluster.RuleInfo() ]

         class DiskLocator(vmodl.DynamicData): # vim.storageDrs.PodSelectionSpec.DiskLocator
            diskId = 0
            diskMoveType = ""
            diskBackingInfo = vim.vm.device.VirtualDevice.BackingInfo()
            profile = [ vim.vm.ProfileSpec() ]

      class StoragePlacementSpec(vmodl.DynamicData): # vim.storageDrs.StoragePlacementSpec
         type = ""
         priority = vim.VirtualMachine.MovePriority()
         vm = vim.VirtualMachine()
         podSelectionSpec = vim.storageDrs.PodSelectionSpec()
         cloneSpec = vim.vm.CloneSpec()
         cloneName = ""
         configSpec = vim.vm.ConfigSpec()
         relocateSpec = vim.vm.RelocateSpec()
         resourcePool = vim.ResourcePool()
         host = vim.HostSystem()
         folder = vim.Folder()
         disallowPrerequisiteMoves = False
         resourceLeaseDurationSec = 0

         class PlacementType(Enum): # vim.storageDrs.StoragePlacementSpec.PlacementType
            create = 0
            reconfigure = 1
            relocate = 2
            clone = 3

      class VirtualDiskAntiAffinityRuleSpec(vim.cluster.RuleInfo): # vim.storageDrs.VirtualDiskAntiAffinityRuleSpec
         diskId = [ 0 ]

      class VirtualDiskRuleSpec(vim.cluster.RuleInfo): # vim.storageDrs.VirtualDiskRuleSpec
         diskRuleType = ""
         diskId = [ 0 ]

         class RuleType(Enum): # vim.storageDrs.VirtualDiskRuleSpec.RuleType
            affinity = 0
            antiAffinity = 1
            disabled = 2

   class tenant(object): # (unknown name)

      class TenantManager(vmodl.ManagedObject): # vim.tenant.TenantManager

         def markServiceProviderEntities(entity=[ vim.ManagedEntity() ] or None): # vim.tenant.TenantManager.markServiceProviderEntities
            # throws vmodl.fault.ManagedObjectNotFound, vim.fault.AuthMinimumAdminPermission
            return None

         def unmarkServiceProviderEntities(entity=[ vim.ManagedEntity() ] or None): # vim.tenant.TenantManager.unmarkServiceProviderEntities
            # throws vmodl.fault.ManagedObjectNotFound
            return None

         def retrieveServiceProviderEntities(): # vim.tenant.TenantManager.retrieveServiceProviderEntities
            return [ vim.ManagedEntity() ]

   class vApp(object): # (unknown name)

      class CloneSpec(vmodl.DynamicData): # vim.vApp.CloneSpec
         location = vim.Datastore()
         host = vim.HostSystem()
         resourceSpec = vim.ResourceConfigSpec()
         vmFolder = vim.Folder()
         networkMapping = [ vim.vApp.CloneSpec.NetworkMappingPair() ]
         property = [ vim.KeyValue() ]
         resourceMapping = [ vim.vApp.CloneSpec.ResourceMap() ]
         provisioning = ""

         class NetworkMappingPair(vmodl.DynamicData): # vim.vApp.CloneSpec.NetworkMappingPair
            source = vim.Network()
            destination = vim.Network()

         class ResourceMap(vmodl.DynamicData): # vim.vApp.CloneSpec.ResourceMap
            source = vim.ManagedEntity()
            parent = vim.ResourcePool()
            resourceSpec = vim.ResourceConfigSpec()
            location = vim.Datastore()

         class ProvisioningType(Enum): # vim.vApp.CloneSpec.ProvisioningType
            sameAsSource = 0
            thin = 1
            thick = 2

      class EntityConfigInfo(vmodl.DynamicData): # vim.vApp.EntityConfigInfo
         key = vim.ManagedEntity()
         tag = ""
         startOrder = 0
         startDelay = 0
         waitingForGuest = False
         startAction = ""
         stopDelay = 0
         stopAction = ""
         destroyWithParent = False

         class Action(Enum): # vim.vApp.EntityConfigInfo.Action
            none = 0
            powerOn = 1
            powerOff = 2
            guestShutdown = 3
            suspend = 4

      class IPAssignmentInfo(vmodl.DynamicData): # vim.vApp.IPAssignmentInfo
         supportedAllocationScheme = [ "" ]
         ipAllocationPolicy = ""
         supportedIpProtocol = [ "" ]
         ipProtocol = ""

         class IpAllocationPolicy(Enum): # vim.vApp.IPAssignmentInfo.IpAllocationPolicy
            dhcpPolicy = 0
            transientPolicy = 1
            fixedPolicy = 2
            fixedAllocatedPolicy = 3

         class AllocationSchemes(Enum): # vim.vApp.IPAssignmentInfo.AllocationSchemes
            dhcp = 0
            ovfenv = 1

         class Protocols(Enum): # vim.vApp.IPAssignmentInfo.Protocols
            IPv4 = 0
            IPv6 = 1

      class IpPool(vmodl.DynamicData): # vim.vApp.IpPool
         id = 0
         name = ""
         ipv4Config = vim.vApp.IpPool.IpPoolConfigInfo()
         ipv6Config = vim.vApp.IpPool.IpPoolConfigInfo()
         dnsDomain = ""
         dnsSearchPath = ""
         hostPrefix = ""
         httpProxy = ""
         networkAssociation = [ vim.vApp.IpPool.Association() ]
         availableIpv4Addresses = 0
         availableIpv6Addresses = 0
         allocatedIpv4Addresses = 0
         allocatedIpv6Addresses = 0

         class IpPoolConfigInfo(vmodl.DynamicData): # vim.vApp.IpPool.IpPoolConfigInfo
            subnetAddress = ""
            netmask = ""
            gateway = ""
            range = ""
            dns = [ "" ]
            dhcpServerAvailable = False
            ipPoolEnabled = False

         class Association(vmodl.DynamicData): # vim.vApp.IpPool.Association
            network = vim.Network()
            networkName = ""

      class OvfSectionInfo(vmodl.DynamicData): # vim.vApp.OvfSectionInfo
         key = 0
         namespace = ""
         type = ""
         atEnvelopeLevel = False
         contents = ""

      class OvfSectionSpec(vim.option.ArrayUpdateSpec): # vim.vApp.OvfSectionSpec
         info = vim.vApp.OvfSectionInfo()

      class ProductInfo(vmodl.DynamicData): # vim.vApp.ProductInfo
         key = 0
         classId = ""
         instanceId = ""
         name = ""
         vendor = ""
         version = ""
         fullVersion = ""
         vendorUrl = ""
         productUrl = ""
         appUrl = ""

      class ProductSpec(vim.option.ArrayUpdateSpec): # vim.vApp.ProductSpec
         info = vim.vApp.ProductInfo()

      class PropertyInfo(vmodl.DynamicData): # vim.vApp.PropertyInfo
         key = 0
         classId = ""
         instanceId = ""
         id = ""
         category = ""
         label = ""
         type = ""
         typeReference = ""
         userConfigurable = False
         defaultValue = ""
         value = ""
         description = ""

      class PropertySpec(vim.option.ArrayUpdateSpec): # vim.vApp.PropertySpec
         info = vim.vApp.PropertyInfo()

      class VmConfigInfo(vmodl.DynamicData): # vim.vApp.VmConfigInfo
         product = [ vim.vApp.ProductInfo() ]
         property = [ vim.vApp.PropertyInfo() ]
         ipAssignment = vim.vApp.IPAssignmentInfo()
         eula = [ "" ]
         ovfSection = [ vim.vApp.OvfSectionInfo() ]
         ovfEnvironmentTransport = [ "" ]
         installBootRequired = False
         installBootStopDelay = 0

      class VmConfigSpec(vmodl.DynamicData): # vim.vApp.VmConfigSpec
         product = [ vim.vApp.ProductSpec() ]
         property = [ vim.vApp.PropertySpec() ]
         ipAssignment = vim.vApp.IPAssignmentInfo()
         eula = [ "" ]
         ovfSection = [ vim.vApp.OvfSectionSpec() ]
         ovfEnvironmentTransport = [ "" ]
         installBootRequired = False
         installBootStopDelay = 0

      class VAppConfigInfo(vim.vApp.VmConfigInfo): # vim.vApp.VAppConfigInfo
         entityConfig = [ vim.vApp.EntityConfigInfo() ]
         annotation = ""
         instanceUuid = ""
         managedBy = vim.ext.ManagedByInfo()

      class VAppConfigSpec(vim.vApp.VmConfigSpec): # vim.vApp.VAppConfigSpec
         entityConfig = [ vim.vApp.EntityConfigInfo() ]
         annotation = ""
         instanceUuid = ""
         managedBy = vim.ext.ManagedByInfo()

      class VAppImportSpec(vim.ImportSpec): # vim.vApp.VAppImportSpec
         name = ""
         vAppConfigSpec = vim.vApp.VAppConfigSpec()
         resourcePoolSpec = vim.ResourceConfigSpec()
         child = [ vim.ImportSpec() ]

   class vcha(object): # (unknown name)

      class FailoverClusterConfigurator(vmodl.ManagedObject): # vim.vcha.FailoverClusterConfigurator
         disabledConfigureMethod = [ vmodl.MethodName() ]

         def prepare(networkSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterNetworkSpec()): # vim.vcha.FailoverClusterConfigurator.prepare
            return vim.Task()

         def deploy(deploymentSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterDeploymentSpec()): # vim.vcha.FailoverClusterConfigurator.deploy
            return vim.Task()

         def configure(configSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterConfigSpec()): # vim.vcha.FailoverClusterConfigurator.configure
            return vim.Task()

         def createPassiveNode(passiveDeploymentSpec=vim.vcha.FailoverClusterConfigurator.PassiveNodeDeploymentSpec(), sourceVcSpec=vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()): # vim.vcha.FailoverClusterConfigurator.createPassiveNode
            return vim.Task()

         def createWitnessNode(witnessDeploymentSpec=vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec(), sourceVcSpec=vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()): # vim.vcha.FailoverClusterConfigurator.createWitnessNode
            return vim.Task()

         def getConfig(): # vim.vcha.FailoverClusterConfigurator.getConfig
            return vim.vcha.FailoverClusterConfigurator.VchaClusterConfigInfo()

         def destroy(): # vim.vcha.FailoverClusterConfigurator.destroy
            return vim.Task()

         class ClusterNetworkConfigSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.ClusterNetworkConfigSpec
            networkPortGroup = vim.Network()
            ipSettings = vim.vm.customization.IPSettings()

         class SourceNodeSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.SourceNodeSpec
            managementVc = vim.ServiceLocator()
            activeVc = vim.VirtualMachine()

         class NodeNetworkSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.NodeNetworkSpec
            ipSettings = vim.vm.customization.IPSettings()

         class PassiveNodeNetworkSpec(vim.vcha.FailoverClusterConfigurator.NodeNetworkSpec): # vim.vcha.FailoverClusterConfigurator.PassiveNodeNetworkSpec
            failoverIpSettings = vim.vm.customization.IPSettings()

         class VchaClusterNetworkSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.VchaClusterNetworkSpec
            witnessNetworkSpec = vim.vcha.FailoverClusterConfigurator.NodeNetworkSpec()
            passiveNetworkSpec = vim.vcha.FailoverClusterConfigurator.PassiveNodeNetworkSpec()

         class NodeDeploymentSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec
            esxHost = vim.HostSystem()
            datastore = vim.Datastore()
            publicNetworkPortGroup = vim.Network()
            clusterNetworkPortGroup = vim.Network()
            folder = vim.Folder()
            resourcePool = vim.ResourcePool()
            managementVc = vim.ServiceLocator()
            nodeName = ""
            ipSettings = vim.vm.customization.IPSettings()

         class PassiveNodeDeploymentSpec(vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec): # vim.vcha.FailoverClusterConfigurator.PassiveNodeDeploymentSpec
            failoverIpSettings = vim.vm.customization.IPSettings()

         class VchaClusterConfigSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.VchaClusterConfigSpec
            passiveIp = ""
            witnessIp = ""

         class VchaClusterDeploymentSpec(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.VchaClusterDeploymentSpec
            passiveDeploymentSpec = vim.vcha.FailoverClusterConfigurator.PassiveNodeDeploymentSpec()
            witnessDeploymentSpec = vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec()
            activeVcSpec = vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()
            activeVcNetworkConfig = vim.vcha.FailoverClusterConfigurator.ClusterNetworkConfigSpec()

         class FailoverNodeInfo(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.FailoverNodeInfo
            clusterIpSettings = vim.vm.customization.IPSettings()
            failoverIp = vim.vm.customization.IPSettings()
            biosUuid = ""

         class WitnessNodeInfo(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.WitnessNodeInfo
            ipSettings = vim.vm.customization.IPSettings()
            biosUuid = ""

         class VchaState(Enum): # vim.vcha.FailoverClusterConfigurator.VchaState
            configured = 0
            notConfigured = 1
            invalid = 2
            prepared = 3

         class VchaClusterConfigInfo(vmodl.DynamicData): # vim.vcha.FailoverClusterConfigurator.VchaClusterConfigInfo
            failoverNodeInfo1 = vim.vcha.FailoverClusterConfigurator.FailoverNodeInfo()
            failoverNodeInfo2 = vim.vcha.FailoverClusterConfigurator.FailoverNodeInfo()
            witnessNodeInfo = vim.vcha.FailoverClusterConfigurator.WitnessNodeInfo()
            state = ""

      class FailoverClusterManager(vmodl.ManagedObject): # vim.vcha.FailoverClusterManager
         disabledClusterMethod = [ vmodl.MethodName() ]

         def setClusterMode(mode=""): # vim.vcha.FailoverClusterManager.setClusterMode
            return vim.Task()

         def getClusterMode(): # vim.vcha.FailoverClusterManager.getClusterMode
            return ""

         def getClusterHealth(): # vim.vcha.FailoverClusterManager.getClusterHealth
            return vim.vcha.FailoverClusterManager.VchaClusterHealth()

         def initiateFailover(planned=False): # vim.vcha.FailoverClusterManager.initiateFailover
            return vim.Task()

         class VchaNodeRole(Enum): # vim.vcha.FailoverClusterManager.VchaNodeRole
            active = 0
            passive = 1
            witness = 2

         class VchaClusterMode(Enum): # vim.vcha.FailoverClusterManager.VchaClusterMode
            enabled = 0
            disabled = 1
            maintenance = 2

         class VchaClusterState(Enum): # vim.vcha.FailoverClusterManager.VchaClusterState
            healthy = 0
            degraded = 1
            isolated = 2

         class VchaNodeState(Enum): # vim.vcha.FailoverClusterManager.VchaNodeState
            up = 0
            down = 1

         class VchaNodeRuntimeInfo(vmodl.DynamicData): # vim.vcha.FailoverClusterManager.VchaNodeRuntimeInfo
            nodeState = ""
            nodeRole = ""
            nodeIp = ""

         class VchaClusterRuntimeInfo(vmodl.DynamicData): # vim.vcha.FailoverClusterManager.VchaClusterRuntimeInfo
            clusterState = ""
            nodeInfo = [ vim.vcha.FailoverClusterManager.VchaNodeRuntimeInfo() ]
            clusterMode = ""

         class VchaClusterHealth(vmodl.DynamicData): # vim.vcha.FailoverClusterManager.VchaClusterHealth
            runtimeInfo = vim.vcha.FailoverClusterManager.VchaClusterRuntimeInfo()
            healthMessages = [ vmodl.LocalizableMessage() ]
            additionalInformation = [ vmodl.LocalizableMessage() ]

   class view(object): # (unknown name)

      class View(vmodl.ManagedObject): # vim.view.View

         def destroy(): # vim.view.View.destroy
            return None

      class ViewManager(vmodl.ManagedObject): # vim.view.ViewManager
         viewList = [ vim.view.View() ]

         def createInventoryView(): # vim.view.ViewManager.createInventoryView
            return vim.view.InventoryView()

         def createContainerView(container=vim.ManagedEntity(), type=[ vmodl.TypeName() ] or None, recursive=False): # vim.view.ViewManager.createContainerView
            return vim.view.ContainerView()

         def createListView(obj=[ vmodl.ManagedObject() ] or None): # vim.view.ViewManager.createListView
            return vim.view.ListView()

         def createListViewFromView(view=vim.view.View()): # vim.view.ViewManager.createListViewFromView
            return vim.view.ListView()

      class ManagedObjectView(vim.view.View): # vim.view.ManagedObjectView
         view = [ vmodl.ManagedObject() ]

      class ContainerView(vim.view.ManagedObjectView): # vim.view.ContainerView
         container = vim.ManagedEntity()
         type = [ vmodl.TypeName() ]
         recursive = False

      class InventoryView(vim.view.ManagedObjectView): # vim.view.InventoryView

         def openFolder(entity=[ vim.ManagedEntity() ]): # vim.view.InventoryView.openFolder
            return [ vim.ManagedEntity() ]

         def closeFolder(entity=[ vim.ManagedEntity() ]): # vim.view.InventoryView.closeFolder
            return [ vim.ManagedEntity() ]

      class ListView(vim.view.ManagedObjectView): # vim.view.ListView

         def modify(add=[ vmodl.ManagedObject() ] or None, remove=[ vmodl.ManagedObject() ] or None): # vim.view.ListView.modify
            return [ vmodl.ManagedObject() ]

         def reset(obj=[ vmodl.ManagedObject() ] or None): # vim.view.ListView.reset
            return [ vmodl.ManagedObject() ]

         def resetFromView(view=vim.view.View()): # vim.view.ListView.resetFromView
            return None

   class vm(object): # (unknown name)

      class AffinityInfo(vmodl.DynamicData): # vim.vm.AffinityInfo
         affinitySet = [ 0 ]

      class BootOptions(vmodl.DynamicData): # vim.vm.BootOptions
         bootDelay = 0
         enterBIOSSetup = False
         efiSecureBootEnabled = False
         bootRetryEnabled = False
         bootRetryDelay = 0
         bootOrder = [ vim.vm.BootOptions.BootableDevice() ]
         networkBootProtocol = ""

         class NetworkBootProtocolType(Enum): # vim.vm.BootOptions.NetworkBootProtocolType
            ipv4 = 0
            ipv6 = 1

         class BootableDevice(vmodl.DynamicData): # vim.vm.BootOptions.BootableDevice
            pass

         class BootableDiskDevice(vim.vm.BootOptions.BootableDevice): # vim.vm.BootOptions.BootableDiskDevice
            deviceKey = 0

         class BootableEthernetDevice(vim.vm.BootOptions.BootableDevice): # vim.vm.BootOptions.BootableEthernetDevice
            deviceKey = 0

         class BootableFloppyDevice(vim.vm.BootOptions.BootableDevice): # vim.vm.BootOptions.BootableFloppyDevice
            pass

         class BootableCdromDevice(vim.vm.BootOptions.BootableDevice): # vim.vm.BootOptions.BootableCdromDevice
            pass

      class Capability(vmodl.DynamicData): # vim.vm.Capability
         snapshotOperationsSupported = False
         multipleSnapshotsSupported = False
         snapshotConfigSupported = False
         poweredOffSnapshotsSupported = False
         memorySnapshotsSupported = False
         revertToSnapshotSupported = False
         quiescedSnapshotsSupported = False
         disableSnapshotsSupported = False
         lockSnapshotsSupported = False
         consolePreferencesSupported = False
         cpuFeatureMaskSupported = False
         s1AcpiManagementSupported = False
         settingScreenResolutionSupported = False
         toolsAutoUpdateSupported = False
         vmNpivWwnSupported = False
         npivWwnOnNonRdmVmSupported = False
         vmNpivWwnDisableSupported = False
         vmNpivWwnUpdateSupported = False
         swapPlacementSupported = False
         toolsSyncTimeSupported = False
         virtualMmuUsageSupported = False
         diskSharesSupported = False
         bootOptionsSupported = False
         bootRetryOptionsSupported = False
         settingVideoRamSizeSupported = False
         settingDisplayTopologySupported = False
         recordReplaySupported = False
         changeTrackingSupported = False
         multipleCoresPerSocketSupported = False
         hostBasedReplicationSupported = False
         guestAutoLockSupported = False
         memoryReservationLockSupported = False
         featureRequirementSupported = False
         poweredOnMonitorTypeChangeSupported = False
         seSparseDiskSupported = False
         nestedHVSupported = False
         vPMCSupported = False
         secureBootSupported = False
         perVmEvcSupported = False
         virtualMmuUsageIgnored = False
         virtualExecUsageIgnored = False
         diskOnlySnapshotOnSuspendedVMSupported = False

      class CloneSpec(vmodl.DynamicData): # vim.vm.CloneSpec
         location = vim.vm.RelocateSpec()
         template = False
         config = vim.vm.ConfigSpec()
         customization = vim.vm.customization.Specification()
         powerOn = False
         snapshot = vim.vm.Snapshot()
         memory = False

      class ConfigInfo(vmodl.DynamicData): # vim.vm.ConfigInfo
         changeVersion = ""
         modified = vmodl.DateTime()
         name = ""
         guestFullName = ""
         version = ""
         uuid = ""
         createDate = vmodl.DateTime()
         instanceUuid = ""
         npivNodeWorldWideName = [ 0 ]
         npivPortWorldWideName = [ 0 ]
         npivWorldWideNameType = ""
         npivDesiredNodeWwns = 0
         npivDesiredPortWwns = 0
         npivTemporaryDisabled = False
         npivOnNonRdmDisks = False
         locationId = ""
         template = False
         guestId = ""
         alternateGuestName = ""
         annotation = ""
         files = vim.vm.FileInfo()
         tools = vim.vm.ToolsConfigInfo()
         flags = vim.vm.FlagInfo()
         consolePreferences = vim.vm.ConsolePreferences()
         defaultPowerOps = vim.vm.DefaultPowerOpInfo()
         hardware = vim.vm.VirtualHardware()
         vcpuConfig = [ vim.vm.VcpuConfig() ]
         cpuAllocation = vim.ResourceAllocationInfo()
         memoryAllocation = vim.ResourceAllocationInfo()
         latencySensitivity = vim.LatencySensitivity()
         memoryHotAddEnabled = False
         cpuHotAddEnabled = False
         cpuHotRemoveEnabled = False
         hotPlugMemoryLimit = 0
         hotPlugMemoryIncrementSize = 0
         cpuAffinity = vim.vm.AffinityInfo()
         memoryAffinity = vim.vm.AffinityInfo()
         networkShaper = vim.vm.NetworkShaperInfo()
         extraConfig = [ vim.option.OptionValue() ]
         cpuFeatureMask = [ vim.host.CpuIdInfo() ]
         datastoreUrl = [ vim.vm.ConfigInfo.DatastoreUrlPair() ]
         swapPlacement = ""
         bootOptions = vim.vm.BootOptions()
         ftInfo = vim.vm.FaultToleranceConfigInfo()
         repConfig = vim.vm.ReplicationConfigSpec()
         vAppConfig = vim.vApp.VmConfigInfo()
         vAssertsEnabled = False
         changeTrackingEnabled = False
         firmware = ""
         maxMksConnections = 0
         guestAutoLockEnabled = False
         managedBy = vim.ext.ManagedByInfo()
         memoryReservationLockedToMax = False
         initialOverhead = vim.vm.ConfigInfo.OverheadInfo()
         nestedHVEnabled = False
         vPMCEnabled = False
         scheduledHardwareUpgradeInfo = vim.vm.ScheduledHardwareUpgradeInfo()
         forkConfigInfo = vim.vm.ForkConfigInfo()
         vFlashCacheReservation = 0
         vmxConfigChecksum = vmodl.Binary()
         messageBusTunnelEnabled = False
         vmStorageObjectId = ""
         swapStorageObjectId = ""
         keyId = vim.encryption.CryptoKeyId()
         guestIntegrityInfo = vim.vm.GuestIntegrityInfo()
         migrateEncryption = ""
         sgxInfo = vim.vm.SgxInfo()
         contentLibItemInfo = vim.vm.ContentLibraryItemInfo()
         guestMonitoringModeInfo = vim.vm.GuestMonitoringModeInfo()

         class NpivWwnType(Enum): # vim.vm.ConfigInfo.NpivWwnType
            vc = 0
            host = 1
            external = 2

         class SwapPlacementType(Enum): # vim.vm.ConfigInfo.SwapPlacementType
            inherit = 0
            vmDirectory = 1
            hostLocal = 2

         class DatastoreUrlPair(vmodl.DynamicData): # vim.vm.ConfigInfo.DatastoreUrlPair
            name = ""
            url = ""

         class OverheadInfo(vmodl.DynamicData): # vim.vm.ConfigInfo.OverheadInfo
            initialMemoryReservation = 0
            initialSwapReservation = 0

      class ConfigOption(vmodl.DynamicData): # vim.vm.ConfigOption
         version = ""
         description = ""
         guestOSDescriptor = [ vim.vm.GuestOsDescriptor() ]
         guestOSDefaultIndex = 0
         hardwareOptions = vim.vm.VirtualHardwareOption()
         capabilities = vim.vm.Capability()
         datastore = vim.vm.DatastoreOption()
         defaultDevice = [ vim.vm.device.VirtualDevice() ]
         supportedMonitorType = [ "" ]
         supportedOvfEnvironmentTransport = [ "" ]
         supportedOvfInstallTransport = [ "" ]
         propertyRelations = [ vim.vm.PropertyRelation() ]

      class ConfigOptionDescriptor(vmodl.DynamicData): # vim.vm.ConfigOptionDescriptor
         key = ""
         description = ""
         host = [ vim.HostSystem() ]
         createSupported = False
         defaultConfigOption = False
         runSupported = False
         upgradeSupported = False

      class ConfigSpec(vmodl.DynamicData): # vim.vm.ConfigSpec
         changeVersion = ""
         name = ""
         version = ""
         createDate = vmodl.DateTime()
         uuid = ""
         instanceUuid = ""
         npivNodeWorldWideName = [ 0 ]
         npivPortWorldWideName = [ 0 ]
         npivWorldWideNameType = ""
         npivDesiredNodeWwns = 0
         npivDesiredPortWwns = 0
         npivTemporaryDisabled = False
         npivOnNonRdmDisks = False
         npivWorldWideNameOp = ""
         locationId = ""
         guestId = ""
         alternateGuestName = ""
         annotation = ""
         files = vim.vm.FileInfo()
         tools = vim.vm.ToolsConfigInfo()
         flags = vim.vm.FlagInfo()
         consolePreferences = vim.vm.ConsolePreferences()
         powerOpInfo = vim.vm.DefaultPowerOpInfo()
         numCPUs = 0
         vcpuConfig = [ vim.vm.VcpuConfig() ]
         numCoresPerSocket = 0
         memoryMB = 0
         memoryHotAddEnabled = False
         cpuHotAddEnabled = False
         cpuHotRemoveEnabled = False
         virtualICH7MPresent = False
         virtualSMCPresent = False
         deviceChange = [ vim.vm.device.VirtualDeviceSpec() ]
         cpuAllocation = vim.ResourceAllocationInfo()
         memoryAllocation = vim.ResourceAllocationInfo()
         latencySensitivity = vim.LatencySensitivity()
         cpuAffinity = vim.vm.AffinityInfo()
         memoryAffinity = vim.vm.AffinityInfo()
         networkShaper = vim.vm.NetworkShaperInfo()
         cpuFeatureMask = [ vim.vm.ConfigSpec.CpuIdInfoSpec() ]
         extraConfig = [ vim.option.OptionValue() ]
         swapPlacement = ""
         bootOptions = vim.vm.BootOptions()
         vAppConfig = vim.vApp.VmConfigSpec()
         ftInfo = vim.vm.FaultToleranceConfigInfo()
         repConfig = vim.vm.ReplicationConfigSpec()
         vAppConfigRemoved = False
         vAssertsEnabled = False
         changeTrackingEnabled = False
         firmware = ""
         maxMksConnections = 0
         guestAutoLockEnabled = False
         managedBy = vim.ext.ManagedByInfo()
         memoryReservationLockedToMax = False
         nestedHVEnabled = False
         vPMCEnabled = False
         scheduledHardwareUpgradeInfo = vim.vm.ScheduledHardwareUpgradeInfo()
         vmProfile = [ vim.vm.ProfileSpec() ]
         messageBusTunnelEnabled = False
         crypto = vim.encryption.CryptoSpec()
         migrateEncryption = ""
         sgxInfo = vim.vm.SgxInfo()
         guestMonitoringModeInfo = vim.vm.GuestMonitoringModeInfo()

         class NpivWwnOp(Enum): # vim.vm.ConfigSpec.NpivWwnOp
            generate = 0
            set = 1
            remove = 2
            extend = 3

         class EncryptedVMotionModes(Enum): # vim.vm.ConfigSpec.EncryptedVMotionModes
            disabled = 0
            opportunistic = 1
            required = 2

         class CpuIdInfoSpec(vim.option.ArrayUpdateSpec): # vim.vm.ConfigSpec.CpuIdInfoSpec
            info = vim.host.CpuIdInfo()

      class ConsolePreferences(vmodl.DynamicData): # vim.vm.ConsolePreferences
         powerOnWhenOpened = False
         enterFullScreenOnPowerOn = False
         closeOnPowerOffOrSuspend = False

      class ContentLibraryItemInfo(vmodl.DynamicData): # vim.vm.ContentLibraryItemInfo
         contentLibraryItemUuid = ""
         contentLibraryItemVersion = ""

      class DatastoreOption(vmodl.DynamicData): # vim.vm.DatastoreOption
         unsupportedVolumes = [ vim.vm.DatastoreOption.FileSystemVolumeOption() ]

         class FileSystemVolumeOption(vmodl.DynamicData): # vim.vm.DatastoreOption.FileSystemVolumeOption
            fileSystemType = vmodl.TypeName()
            majorVersion = 0

      class DefaultPowerOpInfo(vmodl.DynamicData): # vim.vm.DefaultPowerOpInfo
         powerOffType = ""
         suspendType = ""
         resetType = ""
         defaultPowerOffType = ""
         defaultSuspendType = ""
         defaultResetType = ""
         standbyAction = ""

         class PowerOpType(Enum): # vim.vm.DefaultPowerOpInfo.PowerOpType
            soft = 0
            hard = 1
            preset = 2

         class StandbyActionType(Enum): # vim.vm.DefaultPowerOpInfo.StandbyActionType
            checkpoint = 0
            powerOnSuspend = 1

      class DeviceRuntimeInfo(vmodl.DynamicData): # vim.vm.DeviceRuntimeInfo
         runtimeState = vim.vm.DeviceRuntimeInfo.DeviceRuntimeState()
         key = 0

         class DeviceRuntimeState(vmodl.DynamicData): # vim.vm.DeviceRuntimeInfo.DeviceRuntimeState
            pass

         class VirtualEthernetCardRuntimeState(vim.vm.DeviceRuntimeInfo.DeviceRuntimeState): # vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState
            vmDirectPathGen2Active = False
            vmDirectPathGen2InactiveReasonVm = [ "" ]
            vmDirectPathGen2InactiveReasonOther = [ "" ]
            vmDirectPathGen2InactiveReasonExtended = ""
            reservationStatus = ""
            attachmentStatus = ""
            featureRequirement = [ vim.vm.FeatureRequirement() ]

            class VmDirectPathGen2InactiveReasonVm(Enum): # vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonVm
               vmNptIncompatibleGuest = 0
               vmNptIncompatibleGuestDriver = 1
               vmNptIncompatibleAdapterType = 2
               vmNptDisabledOrDisconnectedAdapter = 3
               vmNptIncompatibleAdapterFeatures = 4
               vmNptIncompatibleBackingType = 5
               vmNptInsufficientMemoryReservation = 6
               vmNptFaultToleranceOrRecordReplayConfigured = 7
               vmNptConflictingIOChainConfigured = 8
               vmNptMonitorBlocks = 9
               vmNptConflictingOperationInProgress = 10
               vmNptRuntimeError = 11
               vmNptOutOfIntrVector = 12
               vmNptVMCIActive = 13

            class VmDirectPathGen2InactiveReasonOther(Enum): # vim.vm.DeviceRuntimeInfo.VirtualEthernetCardRuntimeState.VmDirectPathGen2InactiveReasonOther
               vmNptIncompatibleHost = 0
               vmNptIncompatibleNetwork = 1

      class FaultToleranceConfigInfo(vmodl.DynamicData): # vim.vm.FaultToleranceConfigInfo
         role = 0
         instanceUuids = [ "" ]
         configPaths = [ "" ]
         orphaned = False

      class FaultToleranceConfigSpec(vmodl.DynamicData): # vim.vm.FaultToleranceConfigSpec
         metaDataPath = vim.vm.FaultToleranceMetaSpec()
         secondaryVmSpec = vim.vm.FaultToleranceVMConfigSpec()

      class FaultToleranceMetaSpec(vmodl.DynamicData): # vim.vm.FaultToleranceMetaSpec
         metaDataDatastore = vim.Datastore()

      class FaultTolerancePrimaryConfigInfo(vim.vm.FaultToleranceConfigInfo): # vim.vm.FaultTolerancePrimaryConfigInfo
         secondaries = [ vim.VirtualMachine() ]

      class FaultToleranceSecondaryConfigInfo(vim.vm.FaultToleranceConfigInfo): # vim.vm.FaultToleranceSecondaryConfigInfo
         primaryVM = vim.VirtualMachine()

      class FaultToleranceSecondaryOpResult(vmodl.DynamicData): # vim.vm.FaultToleranceSecondaryOpResult
         vm = vim.VirtualMachine()
         powerOnAttempted = False
         powerOnResult = vim.cluster.PowerOnVmResult()

      class FaultToleranceVMConfigSpec(vmodl.DynamicData): # vim.vm.FaultToleranceVMConfigSpec
         vmConfig = vim.Datastore()
         disks = [ vim.vm.FaultToleranceVMConfigSpec.FaultToleranceDiskSpec() ]

         class FaultToleranceDiskSpec(vmodl.DynamicData): # vim.vm.FaultToleranceVMConfigSpec.FaultToleranceDiskSpec
            disk = vim.vm.device.VirtualDevice()
            datastore = vim.Datastore()

      class FeatureRequirement(vmodl.DynamicData): # vim.vm.FeatureRequirement
         key = ""
         featureName = ""
         value = ""

      class FileInfo(vmodl.DynamicData): # vim.vm.FileInfo
         vmPathName = ""
         snapshotDirectory = ""
         suspendDirectory = ""
         logDirectory = ""
         ftMetadataDirectory = ""

      class FileLayout(vmodl.DynamicData): # vim.vm.FileLayout
         configFile = [ "" ]
         logFile = [ "" ]
         disk = [ vim.vm.FileLayout.DiskLayout() ]
         snapshot = [ vim.vm.FileLayout.SnapshotLayout() ]
         swapFile = ""

         class DiskLayout(vmodl.DynamicData): # vim.vm.FileLayout.DiskLayout
            key = 0
            diskFile = [ "" ]

         class SnapshotLayout(vmodl.DynamicData): # vim.vm.FileLayout.SnapshotLayout
            key = vim.vm.Snapshot()
            snapshotFile = [ "" ]

      class FileLayoutEx(vmodl.DynamicData): # vim.vm.FileLayoutEx
         file = [ vim.vm.FileLayoutEx.FileInfo() ]
         disk = [ vim.vm.FileLayoutEx.DiskLayout() ]
         snapshot = [ vim.vm.FileLayoutEx.SnapshotLayout() ]
         timestamp = vmodl.DateTime()

         class FileType(Enum): # vim.vm.FileLayoutEx.FileType
            config = 0
            extendedConfig = 1
            diskDescriptor = 2
            diskExtent = 3
            digestDescriptor = 4
            digestExtent = 5
            diskReplicationState = 6
            log = 7
            stat = 8
            namespaceData = 9
            nvram = 10
            snapshotData = 11
            snapshotMemory = 12
            snapshotList = 13
            snapshotManifestList = 14
            suspend = 15
            suspendMemory = 16
            swap = 17
            uwswap = 18
            core = 19
            screenshot = 20
            ftMetadata = 21
            guestCustomization = 22

         class FileInfo(vmodl.DynamicData): # vim.vm.FileLayoutEx.FileInfo
            key = 0
            name = ""
            type = ""
            size = 0
            uniqueSize = 0
            backingObjectId = ""
            accessible = False

         class DiskUnit(vmodl.DynamicData): # vim.vm.FileLayoutEx.DiskUnit
            fileKey = [ 0 ]

         class DiskLayout(vmodl.DynamicData): # vim.vm.FileLayoutEx.DiskLayout
            key = 0
            chain = [ vim.vm.FileLayoutEx.DiskUnit() ]

         class SnapshotLayout(vmodl.DynamicData): # vim.vm.FileLayoutEx.SnapshotLayout
            key = vim.vm.Snapshot()
            dataKey = 0
            memoryKey = 0
            disk = [ vim.vm.FileLayoutEx.DiskLayout() ]

      class FlagInfo(vmodl.DynamicData): # vim.vm.FlagInfo
         disableAcceleration = False
         enableLogging = False
         useToe = False
         runWithDebugInfo = False
         monitorType = ""
         htSharing = ""
         snapshotDisabled = False
         snapshotLocked = False
         diskUuidEnabled = False
         virtualMmuUsage = ""
         virtualExecUsage = ""
         snapshotPowerOffBehavior = ""
         recordReplayEnabled = False
         faultToleranceType = ""
         cbrcCacheEnabled = False
         vvtdEnabled = False
         vbsEnabled = False

         class HtSharing(Enum): # vim.vm.FlagInfo.HtSharing
            any = 0
            none = 1
            internal = 2

         class PowerOffBehavior(Enum): # vim.vm.FlagInfo.PowerOffBehavior
            powerOff = 0
            revert = 1
            prompt = 2
            take = 3

         class MonitorType(Enum): # vim.vm.FlagInfo.MonitorType
            release = 0
            debug = 1
            stats = 2

         class VirtualMmuUsage(Enum): # vim.vm.FlagInfo.VirtualMmuUsage
            automatic = 0
            on = 1
            off = 2

         class VirtualExecUsage(Enum): # vim.vm.FlagInfo.VirtualExecUsage
            hvAuto = 0
            hvOn = 1
            hvOff = 2

      class ForkConfigInfo(vmodl.DynamicData): # vim.vm.ForkConfigInfo
         parentEnabled = False
         childForkGroupId = ""
         parentForkGroupId = ""
         childType = ""

         class ChildType(Enum): # vim.vm.ForkConfigInfo.ChildType
            none = 0
            persistent = 1
            nonpersistent = 2

      class GuestCustomizationManager(vmodl.ManagedObject): # vim.vm.GuestCustomizationManager

         def customize(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), spec=vim.vm.customization.Specification(), configParams=[ vim.option.OptionValue() ] or None): # vim.vm.GuestCustomizationManager.customize
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

         def startNetwork(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()): # vim.vm.GuestCustomizationManager.startNetwork
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

         def abortCustomization(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()): # vim.vm.GuestCustomizationManager.abortCustomization
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

      class GuestInfo(vmodl.DynamicData): # vim.vm.GuestInfo
         toolsStatus = vim.vm.GuestInfo.ToolsStatus()
         toolsVersionStatus = ""
         toolsVersionStatus2 = ""
         toolsRunningStatus = ""
         toolsVersion = ""
         toolsInstallType = ""
         guestId = ""
         guestFamily = ""
         guestFullName = ""
         hostName = ""
         ipAddress = ""
         net = [ vim.vm.GuestInfo.NicInfo() ]
         ipStack = [ vim.vm.GuestInfo.StackInfo() ]
         disk = [ vim.vm.GuestInfo.DiskInfo() ]
         screen = vim.vm.GuestInfo.ScreenInfo()
         guestState = ""
         appHeartbeatStatus = ""
         guestKernelCrashed = False
         appState = ""
         guestOperationsReady = False
         interactiveGuestOperationsReady = False
         guestStateChangeSupported = False
         generationInfo = [ vim.vm.GuestInfo.NamespaceGenerationInfo() ]
         hwVersion = ""

         class ToolsStatus(Enum): # vim.vm.GuestInfo.ToolsStatus
            toolsNotInstalled = 0
            toolsNotRunning = 1
            toolsOld = 2
            toolsOk = 3

         class ToolsVersionStatus(Enum): # vim.vm.GuestInfo.ToolsVersionStatus
            guestToolsNotInstalled = 0
            guestToolsNeedUpgrade = 1
            guestToolsCurrent = 2
            guestToolsUnmanaged = 3
            guestToolsTooOld = 4
            guestToolsSupportedOld = 5
            guestToolsSupportedNew = 6
            guestToolsTooNew = 7
            guestToolsBlacklisted = 8

         class ToolsRunningStatus(Enum): # vim.vm.GuestInfo.ToolsRunningStatus
            guestToolsNotRunning = 0
            guestToolsRunning = 1
            guestToolsExecutingScripts = 2

         class ToolsInstallType(Enum): # vim.vm.GuestInfo.ToolsInstallType
            guestToolsTypeUnknown = 0
            guestToolsTypeMSI = 1
            guestToolsTypeTar = 2
            guestToolsTypeOSP = 3
            guestToolsTypeOpenVMTools = 4

         class VirtualDiskMapping(vmodl.DynamicData): # vim.vm.GuestInfo.VirtualDiskMapping
            key = 0

         class DiskInfo(vmodl.DynamicData): # vim.vm.GuestInfo.DiskInfo
            diskPath = ""
            capacity = 0
            freeSpace = 0
            filesystemType = ""
            mappings = [ vim.vm.GuestInfo.VirtualDiskMapping() ]

         class NicInfo(vmodl.DynamicData): # vim.vm.GuestInfo.NicInfo
            network = ""
            ipAddress = [ "" ]
            macAddress = ""
            connected = False
            deviceConfigId = 0
            dnsConfig = vim.net.DnsConfigInfo()
            ipConfig = vim.net.IpConfigInfo()
            netBIOSConfig = vim.net.NetBIOSConfigInfo()

         class StackInfo(vmodl.DynamicData): # vim.vm.GuestInfo.StackInfo
            dnsConfig = vim.net.DnsConfigInfo()
            ipRouteConfig = vim.net.IpRouteConfigInfo()
            ipStackConfig = [ vim.KeyValue() ]
            dhcpConfig = vim.net.DhcpConfigInfo()

         class ScreenInfo(vmodl.DynamicData): # vim.vm.GuestInfo.ScreenInfo
            width = 0
            height = 0

         class GuestState(Enum): # vim.vm.GuestInfo.GuestState
            running = 0
            shuttingDown = 1
            resetting = 2
            standby = 3
            notRunning = 4
            unknown = 5

         class AppStateType(Enum): # vim.vm.GuestInfo.AppStateType
            none = 0
            appStateOk = 1
            appStateNeedReset = 2

         class NamespaceGenerationInfo(vmodl.DynamicData): # vim.vm.GuestInfo.NamespaceGenerationInfo
            key = ""
            generationNo = 0

      class GuestIntegrityInfo(vmodl.DynamicData): # vim.vm.GuestIntegrityInfo
         enabled = False

      class GuestMonitoringModeInfo(vmodl.DynamicData): # vim.vm.GuestMonitoringModeInfo
         gmmFile = ""
         gmmAppliance = ""

      class GuestOsDescriptor(vmodl.DynamicData): # vim.vm.GuestOsDescriptor
         id = ""
         family = ""
         fullName = ""
         supportedMaxCPUs = 0
         numSupportedPhysicalSockets = 0
         numSupportedCoresPerSocket = 0
         supportedMinMemMB = 0
         supportedMaxMemMB = 0
         recommendedMemMB = 0
         recommendedColorDepth = 0
         supportedDiskControllerList = [ vmodl.TypeName() ]
         recommendedSCSIController = vmodl.TypeName()
         recommendedDiskController = vmodl.TypeName()
         supportedNumDisks = 0
         recommendedDiskSizeMB = 0
         recommendedCdromController = vmodl.TypeName()
         supportedEthernetCard = [ vmodl.TypeName() ]
         recommendedEthernetCard = vmodl.TypeName()
         supportsSlaveDisk = False
         cpuFeatureMask = [ vim.host.CpuIdInfo() ]
         smcRequired = False
         supportsWakeOnLan = False
         supportsVMI = False
         supportsMemoryHotAdd = False
         supportsCpuHotAdd = False
         supportsCpuHotRemove = False
         supportedFirmware = [ "" ]
         recommendedFirmware = ""
         supportedUSBControllerList = [ vmodl.TypeName() ]
         recommendedUSBController = vmodl.TypeName()
         supports3D = False
         recommended3D = False
         smcRecommended = False
         ich7mRecommended = False
         usbRecommended = False
         supportLevel = ""
         supportedForCreate = False
         vRAMSizeInKB = vim.option.IntOption()
         numSupportedFloppyDevices = 0
         wakeOnLanEthernetCard = [ vmodl.TypeName() ]
         supportsPvscsiControllerForBoot = False
         diskUuidEnabled = False
         supportsHotPlugPCI = False
         supportsSecureBoot = False
         defaultSecureBoot = False
         persistentMemorySupported = False
         supportedMinPersistentMemoryMB = 0
         supportedMaxPersistentMemoryMB = 0
         recommendedPersistentMemoryMB = 0
         persistentMemoryHotAddSupported = False
         persistentMemoryHotRemoveSupported = False
         persistentMemoryColdGrowthSupported = False
         persistentMemoryColdGrowthGranularityMB = 0
         persistentMemoryHotGrowthSupported = False
         persistentMemoryHotGrowthGranularityMB = 0
         numRecommendedPhysicalSockets = 0
         numRecommendedCoresPerSocket = 0
         vvtdSupported = vim.option.BoolOption()
         vbsSupported = vim.option.BoolOption()
         vsgxSupported = vim.option.BoolOption()
         supportsTPM20 = False
         vwdtSupported = False

         class GuestOsFamily(Enum): # vim.vm.GuestOsDescriptor.GuestOsFamily
            windowsGuest = 0
            linuxGuest = 1
            netwareGuest = 2
            solarisGuest = 3
            darwinGuestFamily = 4
            otherGuestFamily = 5

         class GuestOsIdentifier(Enum): # vim.vm.GuestOsDescriptor.GuestOsIdentifier
            dosGuest = 0
            win31Guest = 1
            win95Guest = 2
            win98Guest = 3
            winMeGuest = 4
            winNTGuest = 5
            win2000ProGuest = 6
            win2000ServGuest = 7
            win2000AdvServGuest = 8
            winXPHomeGuest = 9
            winXPProGuest = 10
            winXPPro64Guest = 11
            winNetWebGuest = 12
            winNetStandardGuest = 13
            winNetEnterpriseGuest = 14
            winNetDatacenterGuest = 15
            winNetBusinessGuest = 16
            winNetStandard64Guest = 17
            winNetEnterprise64Guest = 18
            winLonghornGuest = 19
            winLonghorn64Guest = 20
            winNetDatacenter64Guest = 21
            winVistaGuest = 22
            winVista64Guest = 23
            windows7Guest = 24
            windows7_64Guest = 25
            windows7Server64Guest = 26
            windows8Guest = 27
            windows8_64Guest = 28
            windows8Server64Guest = 29
            windows9Guest = 30
            windows9_64Guest = 31
            windows9Server64Guest = 32
            windowsHyperVGuest = 33
            windows2019srv_64Guest = 34
            freebsdGuest = 35
            freebsd64Guest = 36
            freebsd11Guest = 37
            freebsd11_64Guest = 38
            freebsd12Guest = 39
            freebsd12_64Guest = 40
            redhatGuest = 41
            rhel2Guest = 42
            rhel3Guest = 43
            rhel3_64Guest = 44
            rhel4Guest = 45
            rhel4_64Guest = 46
            rhel5Guest = 47
            rhel5_64Guest = 48
            rhel6Guest = 49
            rhel6_64Guest = 50
            rhel7Guest = 51
            rhel7_64Guest = 52
            rhel8_64Guest = 53
            centosGuest = 54
            centos64Guest = 55
            centos6Guest = 56
            centos6_64Guest = 57
            centos7Guest = 58
            centos7_64Guest = 59
            centos8_64Guest = 60
            oracleLinuxGuest = 61
            oracleLinux64Guest = 62
            oracleLinux6Guest = 63
            oracleLinux6_64Guest = 64
            oracleLinux7Guest = 65
            oracleLinux7_64Guest = 66
            oracleLinux8_64Guest = 67
            suseGuest = 68
            suse64Guest = 69
            slesGuest = 70
            sles64Guest = 71
            sles10Guest = 72
            sles10_64Guest = 73
            sles11Guest = 74
            sles11_64Guest = 75
            sles12Guest = 76
            sles12_64Guest = 77
            sles15_64Guest = 78
            nld9Guest = 79
            oesGuest = 80
            sjdsGuest = 81
            mandrakeGuest = 82
            mandrivaGuest = 83
            mandriva64Guest = 84
            turboLinuxGuest = 85
            turboLinux64Guest = 86
            ubuntuGuest = 87
            ubuntu64Guest = 88
            debian4Guest = 89
            debian4_64Guest = 90
            debian5Guest = 91
            debian5_64Guest = 92
            debian6Guest = 93
            debian6_64Guest = 94
            debian7Guest = 95
            debian7_64Guest = 96
            debian8Guest = 97
            debian8_64Guest = 98
            debian9Guest = 99
            debian9_64Guest = 100
            debian10Guest = 101
            debian10_64Guest = 102
            debian11Guest = 103
            debian11_64Guest = 104
            asianux3Guest = 105
            asianux3_64Guest = 106
            asianux4Guest = 107
            asianux4_64Guest = 108
            asianux5_64Guest = 109
            asianux7_64Guest = 110
            asianux8_64Guest = 111
            opensuseGuest = 112
            opensuse64Guest = 113
            fedoraGuest = 114
            fedora64Guest = 115
            coreos64Guest = 116
            vmwarePhoton64Guest = 117
            other24xLinuxGuest = 118
            other26xLinuxGuest = 119
            otherLinuxGuest = 120
            other3xLinuxGuest = 121
            other4xLinuxGuest = 122
            genericLinuxGuest = 123
            other24xLinux64Guest = 124
            other26xLinux64Guest = 125
            other3xLinux64Guest = 126
            other4xLinux64Guest = 127
            otherLinux64Guest = 128
            solaris6Guest = 129
            solaris7Guest = 130
            solaris8Guest = 131
            solaris9Guest = 132
            solaris10Guest = 133
            solaris10_64Guest = 134
            solaris11_64Guest = 135
            os2Guest = 136
            eComStationGuest = 137
            eComStation2Guest = 138
            netware4Guest = 139
            netware5Guest = 140
            netware6Guest = 141
            openServer5Guest = 142
            openServer6Guest = 143
            unixWare7Guest = 144
            darwinGuest = 145
            darwin64Guest = 146
            darwin10Guest = 147
            darwin10_64Guest = 148
            darwin11Guest = 149
            darwin11_64Guest = 150
            darwin12_64Guest = 151
            darwin13_64Guest = 152
            darwin14_64Guest = 153
            darwin15_64Guest = 154
            darwin16_64Guest = 155
            darwin17_64Guest = 156
            darwin18_64Guest = 157
            darwin19_64Guest = 158
            vmkernelGuest = 159
            vmkernel5Guest = 160
            vmkernel6Guest = 161
            vmkernel65Guest = 162
            vmkernel7Guest = 163
            amazonlinux2_64Guest = 164
            crxPod1Guest = 165
            otherGuest = 166
            otherGuest64 = 167

         class FirmwareType(Enum): # vim.vm.GuestOsDescriptor.FirmwareType
            bios = 0
            efi = 1
            csm = 2

         class SupportLevel(Enum): # vim.vm.GuestOsDescriptor.SupportLevel
            experimental = 0
            legacy = 1
            terminated = 2
            supported = 3
            unsupported = 4
            deprecated = 5
            techPreview = 6

      class GuestQuiesceSpec(vmodl.DynamicData): # vim.vm.GuestQuiesceSpec
         timeout = 0

      class InstantCloneSpec(vmodl.DynamicData): # vim.vm.InstantCloneSpec
         name = ""
         location = vim.vm.RelocateSpec()
         config = [ vim.option.OptionValue() ]
         biosUuid = ""

      class LegacyNetworkSwitchInfo(vmodl.DynamicData): # vim.vm.LegacyNetworkSwitchInfo
         name = ""

      class Message(vmodl.DynamicData): # vim.vm.Message
         id = ""
         argument = [ {} ]
         text = ""

      class MetadataManager(object): # (unknown name)

         class VmMetadataOwner(vmodl.DynamicData): # vim.vm.MetadataManager.VmMetadataOwner
            name = ""

            class Owner(Enum): # vim.vm.MetadataManager.VmMetadataOwner.Owner
               ComVmwareVsphereHA = 0

         class VmMetadataOp(Enum): # vim.vm.MetadataManager.VmMetadataOp
            Update = 0
            Remove = 1

         class VmMetadata(vmodl.DynamicData): # vim.vm.MetadataManager.VmMetadata
            vmId = ""
            metadata = ""

         class VmMetadataInput(vmodl.DynamicData): # vim.vm.MetadataManager.VmMetadataInput
            operation = ""
            vmMetadata = vim.vm.MetadataManager.VmMetadata()

         class VmMetadataResult(vmodl.DynamicData): # vim.vm.MetadataManager.VmMetadataResult
            vmMetadata = vim.vm.MetadataManager.VmMetadata()
            error = vmodl.MethodFault()

      class NetworkShaperInfo(vmodl.DynamicData): # vim.vm.NetworkShaperInfo
         enabled = False
         peakBps = 0
         averageBps = 0
         burstSize = 0

      class ProfileDetails(vmodl.DynamicData): # vim.vm.ProfileDetails
         profile = [ vim.vm.ProfileSpec() ]
         diskProfileDetails = [ vim.vm.ProfileDetails.DiskProfileDetails() ]

         class DiskProfileDetails(vmodl.DynamicData): # vim.vm.ProfileDetails.DiskProfileDetails
            diskId = 0
            profile = [ vim.vm.ProfileSpec() ]

      class ProfileRawData(vmodl.DynamicData): # vim.vm.ProfileRawData
         extensionKey = ""
         objectData = ""

      class ProfileSpec(vmodl.DynamicData): # vim.vm.ProfileSpec
         pass

      class PropertyRelation(vmodl.DynamicData): # vim.vm.PropertyRelation
         key = vmodl.DynamicProperty()
         relations = [ vmodl.DynamicProperty() ]

      class QuestionInfo(vmodl.DynamicData): # vim.vm.QuestionInfo
         id = ""
         text = ""
         choice = vim.option.ChoiceOption()
         message = [ vim.vm.Message() ]

      class ReplicationConfigSpec(vmodl.DynamicData): # vim.vm.ReplicationConfigSpec
         generation = 0
         vmReplicationId = ""
         destination = ""
         port = 0
         rpo = 0
         quiesceGuestEnabled = False
         paused = False
         oppUpdatesEnabled = False
         netCompressionEnabled = False
         netEncryptionEnabled = False
         encryptionDestination = ""
         encryptionPort = 0
         remoteCertificateThumbprint = ""
         disk = [ vim.vm.ReplicationConfigSpec.DiskSettings() ]

         class DiskSettings(vmodl.DynamicData): # vim.vm.ReplicationConfigSpec.DiskSettings
            key = 0
            diskReplicationId = ""

      class ScheduledHardwareUpgradeInfo(vmodl.DynamicData): # vim.vm.ScheduledHardwareUpgradeInfo
         upgradePolicy = ""
         versionKey = ""
         scheduledHardwareUpgradeStatus = ""
         fault = vmodl.MethodFault()

         class HardwareUpgradePolicy(Enum): # vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradePolicy
            never = 0
            onSoftPowerOff = 1
            always = 2

         class HardwareUpgradeStatus(Enum): # vim.vm.ScheduledHardwareUpgradeInfo.HardwareUpgradeStatus
            none = 0
            pending = 1
            success = 2
            failed = 3

      class SgxInfo(vmodl.DynamicData): # vim.vm.SgxInfo
         epcSize = 0
         flcMode = ""
         lePubKeyHash = ""

         class FlcModes(Enum): # vim.vm.SgxInfo.FlcModes
            locked = 0
            unlocked = 1

      class Snapshot(vim.ExtensibleManagedObject): # vim.vm.Snapshot
         config = vim.vm.ConfigInfo()
         childSnapshot = [ vim.vm.Snapshot() ]
         vm = vim.VirtualMachine()

         def revert(host=vim.HostSystem() or None, suppressPowerOn=False or None): # vim.vm.Snapshot.revert
            # throws vim.fault.TaskInProgress, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
            return vim.Task()

         def remove(removeChildren=False, consolidate=False or None): # vim.vm.Snapshot.remove
            # throws vim.fault.TaskInProgress
            return vim.Task()

         def rename(name="" or None, description="" or None): # vim.vm.Snapshot.rename
            # throws vim.fault.InvalidName, vim.fault.TaskInProgress, vim.fault.InvalidState
            return None

         def exportSnapshot(): # vim.vm.Snapshot.exportSnapshot
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
            return vim.HttpNfcLease()

      class SnapshotInfo(vmodl.DynamicData): # vim.vm.SnapshotInfo
         currentSnapshot = vim.vm.Snapshot()
         rootSnapshotList = [ vim.vm.SnapshotTree() ]

      class SriovDevicePoolInfo(vmodl.DynamicData): # vim.vm.SriovDevicePoolInfo
         key = ""

      class SriovNetworkDevicePoolInfo(vim.vm.SriovDevicePoolInfo): # vim.vm.SriovNetworkDevicePoolInfo
         switchKey = ""
         switchUuid = ""

      class StorageInfo(vmodl.DynamicData): # vim.vm.StorageInfo
         perDatastoreUsage = [ vim.vm.StorageInfo.UsageOnDatastore() ]
         timestamp = vmodl.DateTime()

         class UsageOnDatastore(vmodl.DynamicData): # vim.vm.StorageInfo.UsageOnDatastore
            datastore = vim.Datastore()
            committed = 0
            uncommitted = 0
            unshared = 0

      class TargetInfo(vmodl.DynamicData): # vim.vm.TargetInfo
         name = ""
         configurationTag = [ "" ]

         class ConfigurationTag(Enum): # vim.vm.TargetInfo.ConfigurationTag
            compliant = 0
            clusterWide = 1

      class ToolsConfigInfo(vmodl.DynamicData): # vim.vm.ToolsConfigInfo
         toolsVersion = 0
         toolsInstallType = ""
         afterPowerOn = False
         afterResume = False
         beforeGuestStandby = False
         beforeGuestShutdown = False
         beforeGuestReboot = False
         toolsUpgradePolicy = ""
         pendingCustomization = ""
         customizationKeyId = vim.encryption.CryptoKeyId()
         syncTimeWithHost = False
         lastInstallInfo = vim.vm.ToolsConfigInfo.ToolsLastInstallInfo()

         class UpgradePolicy(Enum): # vim.vm.ToolsConfigInfo.UpgradePolicy
            manual = 0
            upgradeAtPowerCycle = 1

         class ToolsLastInstallInfo(vmodl.DynamicData): # vim.vm.ToolsConfigInfo.ToolsLastInstallInfo
            counter = 0
            fault = vmodl.MethodFault()

      class UsbInfo(vim.vm.TargetInfo): # vim.vm.UsbInfo
         description = ""
         vendor = 0
         product = 0
         physicalPath = ""
         family = [ "" ]
         speed = [ "" ]
         summary = vim.vm.Summary()

         class Speed(Enum): # vim.vm.UsbInfo.Speed
            low = 0
            full = 1
            high = 2
            superSpeed = 3
            superSpeedPlus = 4
            unknownSpeed = 5

         class Family(Enum): # vim.vm.UsbInfo.Family
            audio = 0
            hid = 1
            hid_bootable = 2
            physical = 3
            communication = 4
            imaging = 5
            printer = 6
            storage = 7
            hub = 8
            smart_card = 9
            security = 10
            video = 11
            wireless = 12
            bluetooth = 13
            wusb = 14
            pda = 15
            vendor_specific = 16
            other = 17
            unknownFamily = 18

      class UsbScanCodeSpec(vmodl.DynamicData): # vim.vm.UsbScanCodeSpec
         keyEvents = [ vim.vm.UsbScanCodeSpec.KeyEvent() ]

         class ModifierType(vmodl.DynamicData): # vim.vm.UsbScanCodeSpec.ModifierType
            leftControl = False
            leftShift = False
            leftAlt = False
            leftGui = False
            rightControl = False
            rightShift = False
            rightAlt = False
            rightGui = False

         class KeyEvent(vmodl.DynamicData): # vim.vm.UsbScanCodeSpec.KeyEvent
            usbHidCode = 0
            modifiers = vim.vm.UsbScanCodeSpec.ModifierType()

      class VcpuConfig(vmodl.DynamicData): # vim.vm.VcpuConfig
         latencySensitivity = vim.LatencySensitivity()

      class VirtualHardware(vmodl.DynamicData): # vim.vm.VirtualHardware
         numCPU = 0
         numCoresPerSocket = 0
         memoryMB = 0
         virtualICH7MPresent = False
         virtualSMCPresent = False
         device = [ vim.vm.device.VirtualDevice() ]

      class VirtualHardwareOption(vmodl.DynamicData): # vim.vm.VirtualHardwareOption
         hwVersion = 0
         virtualDeviceOption = [ vim.vm.device.VirtualDeviceOption() ]
         deviceListReadonly = False
         numCPU = [ 0 ]
         numCoresPerSocket = vim.option.IntOption()
         numCpuReadonly = False
         memoryMB = vim.option.LongOption()
         numPCIControllers = vim.option.IntOption()
         numIDEControllers = vim.option.IntOption()
         numUSBControllers = vim.option.IntOption()
         numUSBXHCIControllers = vim.option.IntOption()
         numSIOControllers = vim.option.IntOption()
         numPS2Controllers = vim.option.IntOption()
         licensingLimit = [ vmodl.PropertyPath() ]
         numSupportedWwnPorts = vim.option.IntOption()
         numSupportedWwnNodes = vim.option.IntOption()
         resourceConfigOption = vim.ResourceConfigOption()
         numNVDIMMControllers = vim.option.IntOption()
         numTPMDevices = vim.option.IntOption()
         numWDTDevices = vim.option.IntOption()
         numPrecisionClockDevices = vim.option.IntOption()
         epcMemoryMB = vim.option.LongOption()

      class WindowsQuiesceSpec(vim.vm.GuestQuiesceSpec): # vim.vm.WindowsQuiesceSpec
         vssBackupType = 0
         vssBootableSystemState = False
         vssPartialFileSupport = False
         vssBackupContext = ""

         class VssBackupContext(Enum): # vim.vm.WindowsQuiesceSpec.VssBackupContext
            ctx_auto = 0
            ctx_backup = 1
            ctx_file_share_backup = 2

      class check(object): # (unknown name)

         class CompatibilityChecker(vmodl.ManagedObject): # vim.vm.check.CompatibilityChecker

            def checkCompatibility(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None): # vim.vm.check.CompatibilityChecker.checkCompatibility
               # throws vim.fault.InvalidState, vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

            def checkVmConfig(spec=vim.vm.ConfigSpec(), vm=vim.VirtualMachine() or None, host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None): # vim.vm.check.CompatibilityChecker.checkVmConfig
               # throws vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

            def checkPowerOn(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None): # vim.vm.check.CompatibilityChecker.checkPowerOn
               # throws vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

         class Result(vmodl.DynamicData): # vim.vm.check.Result
            vm = vim.VirtualMachine()
            host = vim.HostSystem()
            warning = [ vmodl.MethodFault() ]
            error = [ vmodl.MethodFault() ]

         class TestType(Enum): # vim.vm.check.TestType
            sourceTests = 0
            hostTests = 1
            resourcePoolTests = 2
            datastoreTests = 3
            networkTests = 4

         class ProvisioningChecker(vmodl.ManagedObject): # vim.vm.check.ProvisioningChecker

            def queryVMotionCompatibilityEx(vm=[ vim.VirtualMachine() ], host=[ vim.HostSystem() ]): # vim.vm.check.ProvisioningChecker.queryVMotionCompatibilityEx
               return vim.Task()

            def checkMigrate(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, state=vim.VirtualMachine.PowerState() or None, testType=[ "" ] or None): # vim.vm.check.ProvisioningChecker.checkMigrate
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkRelocate(vm=vim.VirtualMachine(), spec=vim.vm.RelocateSpec(), testType=[ "" ] or None): # vim.vm.check.ProvisioningChecker.checkRelocate
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkClone(vm=vim.VirtualMachine(), folder=vim.Folder(), name="", spec=vim.vm.CloneSpec(), testType=[ "" ] or None): # vim.vm.check.ProvisioningChecker.checkClone
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkInstantClone(vm=vim.VirtualMachine(), spec=vim.vm.InstantCloneSpec(), testType=[ "" ] or None): # vim.vm.check.ProvisioningChecker.checkInstantClone
               # throws vim.fault.InvalidState
               return vim.Task()

      class customization(object): # (unknown name)

         class AdapterMapping(vmodl.DynamicData): # vim.vm.customization.AdapterMapping
            macAddress = ""
            adapter = vim.vm.customization.IPSettings()

         class GlobalIPSettings(vmodl.DynamicData): # vim.vm.customization.GlobalIPSettings
            dnsSuffixList = [ "" ]
            dnsServerList = [ "" ]

         class GuiRunOnce(vmodl.DynamicData): # vim.vm.customization.GuiRunOnce
            commandList = [ "" ]

         class GuiUnattended(vmodl.DynamicData): # vim.vm.customization.GuiUnattended
            password = vim.vm.customization.Password()
            timeZone = 0
            autoLogon = False
            autoLogonCount = 0

         class IPSettings(vmodl.DynamicData): # vim.vm.customization.IPSettings
            ip = vim.vm.customization.IpGenerator()
            subnetMask = ""
            gateway = [ "" ]
            ipV6Spec = vim.vm.customization.IPSettings.IpV6AddressSpec()
            dnsServerList = [ "" ]
            dnsDomain = ""
            primaryWINS = ""
            secondaryWINS = ""
            netBIOS = vim.vm.customization.IPSettings.NetBIOSMode()

            class IpV6AddressSpec(vmodl.DynamicData): # vim.vm.customization.IPSettings.IpV6AddressSpec
               ip = [ vim.vm.customization.IpV6Generator() ]
               gateway = [ "" ]

            class NetBIOSMode(Enum): # vim.vm.customization.IPSettings.NetBIOSMode
               enableNetBIOSViaDhcp = 0
               enableNetBIOS = 1
               disableNetBIOS = 2

         class Identification(vmodl.DynamicData): # vim.vm.customization.Identification
            joinWorkgroup = ""
            joinDomain = ""
            domainAdmin = ""
            domainAdminPassword = vim.vm.customization.Password()

         class IdentitySettings(vmodl.DynamicData): # vim.vm.customization.IdentitySettings
            pass

         class IpGenerator(vmodl.DynamicData): # vim.vm.customization.IpGenerator
            pass

         class IpV6Generator(vmodl.DynamicData): # vim.vm.customization.IpV6Generator
            pass

         class LicenseFilePrintData(vmodl.DynamicData): # vim.vm.customization.LicenseFilePrintData
            autoMode = vim.vm.customization.LicenseFilePrintData.AutoMode()
            autoUsers = 0

            class AutoMode(Enum): # vim.vm.customization.LicenseFilePrintData.AutoMode
               perServer = 0
               perSeat = 1

         class LinuxPrep(vim.vm.customization.IdentitySettings): # vim.vm.customization.LinuxPrep
            hostName = vim.vm.customization.NameGenerator()
            domain = ""
            timeZone = ""
            hwClockUTC = False
            scriptText = ""

         class NameGenerator(vmodl.DynamicData): # vim.vm.customization.NameGenerator
            pass

         class Options(vmodl.DynamicData): # vim.vm.customization.Options
            pass

         class Password(vmodl.DynamicData): # vim.vm.customization.Password
            value = ""
            plainText = False

         class PrefixNameGenerator(vim.vm.customization.NameGenerator): # vim.vm.customization.PrefixNameGenerator
            base = ""

         class Specification(vmodl.DynamicData): # vim.vm.customization.Specification
            options = vim.vm.customization.Options()
            identity = vim.vm.customization.IdentitySettings()
            globalIPSettings = vim.vm.customization.GlobalIPSettings()
            nicSettingMap = [ vim.vm.customization.AdapterMapping() ]
            encryptionKey = [ 0x00 ]

         class StatelessIpV6Generator(vim.vm.customization.IpV6Generator): # vim.vm.customization.StatelessIpV6Generator
            pass

         class Sysprep(vim.vm.customization.IdentitySettings): # vim.vm.customization.Sysprep
            guiUnattended = vim.vm.customization.GuiUnattended()
            userData = vim.vm.customization.UserData()
            guiRunOnce = vim.vm.customization.GuiRunOnce()
            identification = vim.vm.customization.Identification()
            licenseFilePrintData = vim.vm.customization.LicenseFilePrintData()

         class SysprepText(vim.vm.customization.IdentitySettings): # vim.vm.customization.SysprepText
            value = ""

         class UnknownIpGenerator(vim.vm.customization.IpGenerator): # vim.vm.customization.UnknownIpGenerator
            pass

         class UnknownIpV6Generator(vim.vm.customization.IpV6Generator): # vim.vm.customization.UnknownIpV6Generator
            pass

         class UnknownNameGenerator(vim.vm.customization.NameGenerator): # vim.vm.customization.UnknownNameGenerator
            pass

         class UserData(vmodl.DynamicData): # vim.vm.customization.UserData
            fullName = ""
            orgName = ""
            computerName = vim.vm.customization.NameGenerator()
            productId = ""

         class VirtualMachineNameGenerator(vim.vm.customization.NameGenerator): # vim.vm.customization.VirtualMachineNameGenerator
            pass

         class WinOptions(vim.vm.customization.Options): # vim.vm.customization.WinOptions
            changeSID = False
            deleteAccounts = False
            reboot = vim.vm.customization.WinOptions.SysprepRebootOption()

            class SysprepRebootOption(Enum): # vim.vm.customization.WinOptions.SysprepRebootOption
               reboot = 0
               noreboot = 1
               shutdown = 2

         class AutoIpV6Generator(vim.vm.customization.IpV6Generator): # vim.vm.customization.AutoIpV6Generator
            pass

         class CustomIpGenerator(vim.vm.customization.IpGenerator): # vim.vm.customization.CustomIpGenerator
            argument = ""

         class CustomIpV6Generator(vim.vm.customization.IpV6Generator): # vim.vm.customization.CustomIpV6Generator
            argument = ""

         class CustomNameGenerator(vim.vm.customization.NameGenerator): # vim.vm.customization.CustomNameGenerator
            argument = ""

         class DhcpIpGenerator(vim.vm.customization.IpGenerator): # vim.vm.customization.DhcpIpGenerator
            pass

         class DhcpIpV6Generator(vim.vm.customization.IpV6Generator): # vim.vm.customization.DhcpIpV6Generator
            pass

         class FixedIp(vim.vm.customization.IpGenerator): # vim.vm.customization.FixedIp
            ipAddress = ""

         class FixedIpV6(vim.vm.customization.IpV6Generator): # vim.vm.customization.FixedIpV6
            ipAddress = ""
            subnetMask = 0

         class FixedName(vim.vm.customization.NameGenerator): # vim.vm.customization.FixedName
            name = ""

         class LinuxOptions(vim.vm.customization.Options): # vim.vm.customization.LinuxOptions
            pass

      class device(object): # (unknown name)

         class HostDiskMappingInfo(vmodl.DynamicData): # vim.vm.device.HostDiskMappingInfo
            physicalPartition = vim.vm.device.HostDiskMappingInfo.PartitionInfo()
            name = ""
            exclusive = False

            class PartitionInfo(vmodl.DynamicData): # vim.vm.device.HostDiskMappingInfo.PartitionInfo
               name = ""
               fileSystem = ""
               capacityInKb = 0

         class HostDiskMappingOption(vmodl.DynamicData): # vim.vm.device.HostDiskMappingOption
            physicalPartition = [ vim.vm.device.HostDiskMappingOption.PartitionOption() ]
            name = ""

            class PartitionOption(vmodl.DynamicData): # vim.vm.device.HostDiskMappingOption.PartitionOption
               name = ""
               fileSystem = ""
               capacityInKb = 0

         class VirtualDevice(vmodl.DynamicData): # vim.vm.device.VirtualDevice
            key = 0
            deviceInfo = vim.Description()
            backing = vim.vm.device.VirtualDevice.BackingInfo()
            connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            slotInfo = vim.vm.device.VirtualDevice.BusSlotInfo()
            controllerKey = 0
            unitNumber = 0

            class BackingInfo(vmodl.DynamicData): # vim.vm.device.VirtualDevice.BackingInfo
               pass

            class FileBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualDevice.FileBackingInfo
               fileName = ""
               datastore = vim.Datastore()
               backingObjectId = ""

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualDevice.DeviceBackingInfo
               deviceName = ""
               useAutoDetect = False

            class RemoteDeviceBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo
               deviceName = ""
               useAutoDetect = False

            class PipeBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualDevice.PipeBackingInfo
               pipeName = ""

            class URIBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualDevice.URIBackingInfo
               serviceURI = ""
               direction = ""
               proxyURI = ""

            class ConnectInfo(vmodl.DynamicData): # vim.vm.device.VirtualDevice.ConnectInfo
               migrateConnect = ""
               startConnected = False
               allowGuestControl = False
               connected = False
               status = ""

               class Status(Enum): # vim.vm.device.VirtualDevice.ConnectInfo.Status
                  ok = 0
                  recoverableError = 1
                  unrecoverableError = 2
                  untried = 3

               class MigrateConnectOp(Enum): # vim.vm.device.VirtualDevice.ConnectInfo.MigrateConnectOp
                  connect = 0
                  disconnect = 1
                  unset = 2

            class BusSlotInfo(vmodl.DynamicData): # vim.vm.device.VirtualDevice.BusSlotInfo
               pass

            class PciBusSlotInfo(vim.vm.device.VirtualDevice.BusSlotInfo): # vim.vm.device.VirtualDevice.PciBusSlotInfo
               pciSlotNumber = 0

         class VirtualDeviceOption(vmodl.DynamicData): # vim.vm.device.VirtualDeviceOption
            type = vmodl.TypeName()
            connectOption = vim.vm.device.VirtualDeviceOption.ConnectOption()
            busSlotOption = vim.vm.device.VirtualDeviceOption.BusSlotOption()
            controllerType = vmodl.TypeName()
            autoAssignController = vim.option.BoolOption()
            backingOption = [ vim.vm.device.VirtualDeviceOption.BackingOption() ]
            defaultBackingOptionIndex = 0
            licensingLimit = [ vmodl.PropertyPath() ]
            deprecated = False
            plugAndPlay = False
            hotRemoveSupported = False

            class BackingOption(vmodl.DynamicData): # vim.vm.device.VirtualDeviceOption.BackingOption
               type = vmodl.TypeName()

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualDeviceOption.FileBackingOption
               fileNameExtensions = vim.option.ChoiceOption()

               class FileExtension(Enum): # vim.vm.device.VirtualDeviceOption.FileBackingOption.FileExtension
                  iso = 0
                  flp = 1
                  vmdk = 2
                  dsk = 3
                  rdm = 4

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualDeviceOption.DeviceBackingOption
               autoDetectAvailable = vim.option.BoolOption()

            class RemoteDeviceBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption
               autoDetectAvailable = vim.option.BoolOption()

            class PipeBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualDeviceOption.PipeBackingOption
               pass

            class URIBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualDeviceOption.URIBackingOption
               directions = vim.option.ChoiceOption()

               class Direction(Enum): # vim.vm.device.VirtualDeviceOption.URIBackingOption.Direction
                  server = 0
                  client = 1

            class ConnectOption(vmodl.DynamicData): # vim.vm.device.VirtualDeviceOption.ConnectOption
               startConnected = vim.option.BoolOption()
               allowGuestControl = vim.option.BoolOption()

            class BusSlotOption(vmodl.DynamicData): # vim.vm.device.VirtualDeviceOption.BusSlotOption
               type = vmodl.TypeName()

         class VirtualDeviceSpec(vmodl.DynamicData): # vim.vm.device.VirtualDeviceSpec
            operation = vim.vm.device.VirtualDeviceSpec.Operation()
            fileOperation = vim.vm.device.VirtualDeviceSpec.FileOperation()
            device = vim.vm.device.VirtualDevice()
            profile = [ vim.vm.ProfileSpec() ]
            backing = vim.vm.device.VirtualDeviceSpec.BackingSpec()

            class Operation(Enum): # vim.vm.device.VirtualDeviceSpec.Operation
               add = 0
               remove = 1
               edit = 2

            class FileOperation(Enum): # vim.vm.device.VirtualDeviceSpec.FileOperation
               create = 0
               destroy = 1
               replace = 2

            class BackingSpec(vmodl.DynamicData): # vim.vm.device.VirtualDeviceSpec.BackingSpec
               parent = vim.vm.device.VirtualDeviceSpec.BackingSpec()
               crypto = vim.encryption.CryptoSpec()

         class VirtualDisk(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualDisk
            capacityInKB = 0
            capacityInBytes = 0
            shares = vim.SharesInfo()
            storageIOAllocation = vim.StorageResourceManager.IOAllocationInfo()
            diskObjectId = ""
            vFlashCacheConfigInfo = vim.vm.device.VirtualDisk.VFlashCacheConfigInfo()
            iofilter = [ "" ]
            vDiskId = vim.vslm.ID()
            nativeUnmanagedLinkedClone = False

            class DeltaDiskFormat(Enum): # vim.vm.device.VirtualDisk.DeltaDiskFormat
               redoLogFormat = 0
               nativeFormat = 1
               seSparseFormat = 2

            class DeltaDiskFormatVariant(Enum): # vim.vm.device.VirtualDisk.DeltaDiskFormatVariant
               vmfsSparseVariant = 0
               vsanSparseVariant = 1

            class Sharing(Enum): # vim.vm.device.VirtualDisk.Sharing
               sharingNone = 0
               sharingMultiWriter = 1

            class SparseVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.SparseVer1BackingInfo
               diskMode = ""
               split = False
               writeThrough = False
               spaceUsedInKB = 0
               contentId = ""
               parent = vim.vm.device.VirtualDisk.SparseVer1BackingInfo()

            class SparseVer2BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.SparseVer2BackingInfo
               diskMode = ""
               split = False
               writeThrough = False
               spaceUsedInKB = 0
               uuid = ""
               contentId = ""
               changeId = ""
               parent = vim.vm.device.VirtualDisk.SparseVer2BackingInfo()
               keyId = vim.encryption.CryptoKeyId()

            class FlatVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.FlatVer1BackingInfo
               diskMode = ""
               split = False
               writeThrough = False
               contentId = ""
               parent = vim.vm.device.VirtualDisk.FlatVer1BackingInfo()

            class FlatVer2BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.FlatVer2BackingInfo
               diskMode = ""
               split = False
               writeThrough = False
               thinProvisioned = False
               eagerlyScrub = False
               uuid = ""
               contentId = ""
               changeId = ""
               parent = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
               deltaDiskFormat = ""
               digestEnabled = False
               deltaGrainSize = 0
               deltaDiskFormatVariant = ""
               sharing = ""
               keyId = vim.encryption.CryptoKeyId()

            class SeSparseBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.SeSparseBackingInfo
               diskMode = ""
               writeThrough = False
               uuid = ""
               contentId = ""
               changeId = ""
               parent = vim.vm.device.VirtualDisk.SeSparseBackingInfo()
               deltaDiskFormat = ""
               digestEnabled = False
               grainSize = 0
               keyId = vim.encryption.CryptoKeyId()

            class RawDiskVer2BackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo
               descriptorFileName = ""
               uuid = ""
               changeId = ""
               sharing = ""

            class PartitionedRawDiskVer2BackingInfo(vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo): # vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo
               partition = [ 0 ]

            class RawDiskMappingVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo
               lunUuid = ""
               deviceName = ""
               compatibilityMode = ""
               diskMode = ""
               uuid = ""
               contentId = ""
               changeId = ""
               parent = vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo()
               deltaDiskFormat = ""
               deltaGrainSize = 0
               sharing = ""

            class LocalPMemBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualDisk.LocalPMemBackingInfo
               diskMode = ""
               uuid = ""
               volumeUUID = ""
               contentId = ""

            class VFlashCacheConfigInfo(vmodl.DynamicData): # vim.vm.device.VirtualDisk.VFlashCacheConfigInfo
               vFlashModule = ""
               reservationInMB = 0
               cacheConsistencyType = ""
               cacheMode = ""
               blockSizeInKB = 0

               class CacheConsistencyType(Enum): # vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheConsistencyType
                  strong = 0
                  weak = 1

               class CacheMode(Enum): # vim.vm.device.VirtualDisk.VFlashCacheConfigInfo.CacheMode
                  write_thru = 0
                  write_back = 1

         class VirtualDiskId(vmodl.DynamicData): # vim.vm.device.VirtualDiskId
            vm = vim.VirtualMachine()
            diskId = 0

         class VirtualDiskOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualDiskOption
            capacityInKB = vim.option.LongOption()
            ioAllocationOption = vim.StorageResourceManager.IOAllocationOption()
            vFlashCacheConfigOption = vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption()

            class DiskMode(Enum): # vim.vm.device.VirtualDiskOption.DiskMode
               persistent = 0
               nonpersistent = 1
               undoable = 2
               independent_persistent = 3
               independent_nonpersistent = 4
               append = 5

            class CompatibilityMode(Enum): # vim.vm.device.VirtualDiskOption.CompatibilityMode
               virtualMode = 0
               physicalMode = 1

            class SparseVer1BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.SparseVer1BackingOption
               diskModes = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False

            class SparseVer2BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.SparseVer2BackingOption
               diskMode = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False
               hotGrowable = False
               uuid = False

            class FlatVer1BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.FlatVer1BackingOption
               diskMode = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False

            class DeltaDiskFormatsSupported(vmodl.DynamicData): # vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported
               datastoreType = vmodl.TypeName()
               deltaDiskFormat = vim.option.ChoiceOption()

            class FlatVer2BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.FlatVer2BackingOption
               diskMode = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False
               hotGrowable = False
               uuid = False
               thinProvisioned = vim.option.BoolOption()
               eagerlyScrub = vim.option.BoolOption()
               deltaDiskFormat = vim.option.ChoiceOption()
               deltaDiskFormatsSupported = [ vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported() ]

            class SeSparseBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.SeSparseBackingOption
               diskMode = vim.option.ChoiceOption()
               writeThrough = vim.option.BoolOption()
               growable = False
               hotGrowable = False
               uuid = False
               deltaDiskFormatsSupported = [ vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported() ]

            class RawDiskVer2BackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualDiskOption.RawDiskVer2BackingOption
               descriptorFileNameExtensions = vim.option.ChoiceOption()
               uuid = False

            class PartitionedRawDiskVer2BackingOption(vim.vm.device.VirtualDiskOption.RawDiskVer2BackingOption): # vim.vm.device.VirtualDiskOption.PartitionedRawDiskVer2BackingOption
               pass

            class RawDiskMappingVer1BackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualDiskOption.RawDiskMappingVer1BackingOption
               descriptorFileNameExtensions = vim.option.ChoiceOption()
               compatibilityMode = vim.option.ChoiceOption()
               diskMode = vim.option.ChoiceOption()
               uuid = False

            class LocalPMemBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualDiskOption.LocalPMemBackingOption
               diskMode = vim.option.ChoiceOption()
               growable = False
               hotGrowable = False
               uuid = False

            class VFlashCacheConfigOption(vmodl.DynamicData): # vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption
               cacheConsistencyType = vim.option.ChoiceOption()
               cacheMode = vim.option.ChoiceOption()
               reservationInMB = vim.option.LongOption()
               blockSizeInKB = vim.option.LongOption()

         class VirtualDiskSpec(vim.vm.device.VirtualDeviceSpec): # vim.vm.device.VirtualDiskSpec
            diskMoveType = ""
            migrateCache = False

         class VirtualEthernetCard(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualEthernetCard
            addressType = ""
            macAddress = ""
            wakeOnLanEnabled = False
            resourceAllocation = vim.vm.device.VirtualEthernetCard.ResourceAllocation()
            externalId = ""
            uptCompatibilityEnabled = False

            class NetworkBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualEthernetCard.NetworkBackingInfo
               network = vim.Network()
               inPassthroughMode = False

            class LegacyNetworkBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualEthernetCard.LegacyNetworkBackingInfo
               pass

            class DistributedVirtualPortBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo
               port = vim.dvs.PortConnection()

            class OpaqueNetworkBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualEthernetCard.OpaqueNetworkBackingInfo
               opaqueNetworkId = ""
               opaqueNetworkType = ""

            class ResourceAllocation(vmodl.DynamicData): # vim.vm.device.VirtualEthernetCard.ResourceAllocation
               reservation = 0
               share = vim.SharesInfo()
               limit = 0

         class VirtualEthernetCardOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualEthernetCardOption
            supportedOUI = vim.option.ChoiceOption()
            macType = vim.option.ChoiceOption()
            wakeOnLanEnabled = vim.option.BoolOption()
            vmDirectPathGen2Supported = False
            uptCompatibilityEnabled = vim.option.BoolOption()

            class NetworkBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualEthernetCardOption.NetworkBackingOption
               pass

            class OpaqueNetworkBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualEthernetCardOption.OpaqueNetworkBackingOption
               pass

            class LegacyNetworkBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualEthernetCardOption.LegacyNetworkBackingOption

               class LegacyNetworkDeviceName(Enum): # vim.vm.device.VirtualEthernetCardOption.LegacyNetworkBackingOption.LegacyNetworkDeviceName
                  bridged = 0
                  nat = 1
                  hostonly = 2

            class DistributedVirtualPortBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualEthernetCardOption.DistributedVirtualPortBackingOption
               pass

            class MacTypes(Enum): # vim.vm.device.VirtualEthernetCardOption.MacTypes
               manual = 0
               generated = 1
               assigned = 2

         class VirtualFloppy(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualFloppy

            class ImageBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualFloppy.ImageBackingInfo
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualFloppy.DeviceBackingInfo
               pass

            class RemoteDeviceBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo): # vim.vm.device.VirtualFloppy.RemoteDeviceBackingInfo
               pass

         class VirtualFloppyOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualFloppyOption

            class ImageBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualFloppyOption.ImageBackingOption
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualFloppyOption.DeviceBackingOption
               pass

            class RemoteDeviceBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption): # vim.vm.device.VirtualFloppyOption.RemoteDeviceBackingOption
               pass

         class VirtualKeyboard(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualKeyboard
            pass

         class VirtualKeyboardOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualKeyboardOption
            pass

         class VirtualNVDIMM(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualNVDIMM
            capacityInMB = 0

            class BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualNVDIMM.BackingInfo
               parent = vim.vm.device.VirtualNVDIMM.BackingInfo()
               changeId = ""

         class VirtualNVDIMMOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualNVDIMMOption
            capacityInMB = vim.option.LongOption()
            growable = False
            hotGrowable = False
            granularityInMB = 0

         class VirtualPCIPassthrough(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualPCIPassthrough

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo
               id = ""
               deviceId = ""
               systemId = ""
               vendorId = 0

            class AllowedDevice(vmodl.DynamicData): # vim.vm.device.VirtualPCIPassthrough.AllowedDevice
               vendorId = 0
               deviceId = 0
               subVendorId = 0
               subDeviceId = 0
               revisionId = 0

            class DynamicBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualPCIPassthrough.DynamicBackingInfo
               allowedDevice = [ vim.vm.device.VirtualPCIPassthrough.AllowedDevice() ]
               customLabel = ""
               assignedId = ""

            class PluginBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualPCIPassthrough.PluginBackingInfo
               pass

            class VmiopBackingInfo(vim.vm.device.VirtualPCIPassthrough.PluginBackingInfo): # vim.vm.device.VirtualPCIPassthrough.VmiopBackingInfo
               vgpu = ""

         class VirtualPCIPassthroughOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualPCIPassthroughOption

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualPCIPassthroughOption.DeviceBackingOption
               pass

            class PluginBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualPCIPassthroughOption.PluginBackingOption
               pass

            class VmiopBackingOption(vim.vm.device.VirtualPCIPassthroughOption.PluginBackingOption): # vim.vm.device.VirtualPCIPassthroughOption.VmiopBackingOption
               vgpu = vim.option.StringOption()
               maxInstances = 0

            class DynamicBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualPCIPassthroughOption.DynamicBackingOption
               pass

         class VirtualPCNet32(vim.vm.device.VirtualEthernetCard): # vim.vm.device.VirtualPCNet32
            pass

         class VirtualPCNet32Option(vim.vm.device.VirtualEthernetCardOption): # vim.vm.device.VirtualPCNet32Option
            supportsMorphing = False

         class VirtualParallelPort(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualParallelPort

            class FileBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualParallelPort.FileBackingInfo
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualParallelPort.DeviceBackingInfo
               pass

         class VirtualParallelPortOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualParallelPortOption

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualParallelPortOption.FileBackingOption
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualParallelPortOption.DeviceBackingOption
               pass

         class VirtualPointingDevice(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualPointingDevice

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualPointingDevice.DeviceBackingInfo
               hostPointingDevice = ""

         class VirtualPointingDeviceOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualPointingDeviceOption

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualPointingDeviceOption.DeviceBackingOption
               hostPointingDevice = vim.option.ChoiceOption()

               class HostPointingDeviceChoice(Enum): # vim.vm.device.VirtualPointingDeviceOption.DeviceBackingOption.HostPointingDeviceChoice
                  autodetect = 0
                  intellimouseExplorer = 1
                  intellimousePs2 = 2
                  logitechMouseman = 3
                  microsoft_serial = 4
                  mouseSystems = 5
                  mousemanSerial = 6
                  ps2 = 7

         class VirtualPrecisionClock(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualPrecisionClock

            class SystemClockBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualPrecisionClock.SystemClockBackingInfo
               protocol = ""

         class VirtualPrecisionClockOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualPrecisionClockOption

            class SystemClockBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualPrecisionClockOption.SystemClockBackingOption
               protocol = vim.option.ChoiceOption()

         class VirtualSCSIPassthrough(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualSCSIPassthrough

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualSCSIPassthrough.DeviceBackingInfo
               pass

         class VirtualSCSIPassthroughOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualSCSIPassthroughOption

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualSCSIPassthroughOption.DeviceBackingOption
               pass

         class VirtualSerialPort(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualSerialPort
            yieldOnPoll = False

            class FileBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualSerialPort.FileBackingInfo
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualSerialPort.DeviceBackingInfo
               pass

            class PipeBackingInfo(vim.vm.device.VirtualDevice.PipeBackingInfo): # vim.vm.device.VirtualSerialPort.PipeBackingInfo
               endpoint = ""
               noRxLoss = False

            class URIBackingInfo(vim.vm.device.VirtualDevice.URIBackingInfo): # vim.vm.device.VirtualSerialPort.URIBackingInfo
               pass

            class ThinPrintBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualSerialPort.ThinPrintBackingInfo
               pass

         class VirtualSerialPortOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualSerialPortOption
            yieldOnPoll = vim.option.BoolOption()

            class EndPoint(Enum): # vim.vm.device.VirtualSerialPortOption.EndPoint
               client = 0
               server = 1

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualSerialPortOption.FileBackingOption
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualSerialPortOption.DeviceBackingOption
               pass

            class PipeBackingOption(vim.vm.device.VirtualDeviceOption.PipeBackingOption): # vim.vm.device.VirtualSerialPortOption.PipeBackingOption
               endpoint = vim.option.ChoiceOption()
               noRxLoss = vim.option.BoolOption()

            class URIBackingOption(vim.vm.device.VirtualDeviceOption.URIBackingOption): # vim.vm.device.VirtualSerialPortOption.URIBackingOption
               pass

            class ThinPrintBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualSerialPortOption.ThinPrintBackingOption
               pass

         class VirtualSoundCard(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualSoundCard

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualSoundCard.DeviceBackingInfo
               pass

         class VirtualSoundCardOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualSoundCardOption

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualSoundCardOption.DeviceBackingOption
               pass

         class VirtualSriovEthernetCard(vim.vm.device.VirtualEthernetCard): # vim.vm.device.VirtualSriovEthernetCard
            allowGuestOSMtuChange = False
            sriovBacking = vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo()

            class SriovBackingInfo(vim.vm.device.VirtualDevice.BackingInfo): # vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo
               physicalFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
               virtualFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
               virtualFunctionIndex = 0

         class VirtualSriovEthernetCardOption(vim.vm.device.VirtualEthernetCardOption): # vim.vm.device.VirtualSriovEthernetCardOption

            class SriovBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption): # vim.vm.device.VirtualSriovEthernetCardOption.SriovBackingOption
               pass

         class VirtualTPM(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualTPM
            endorsementKeyCertificateSigningRequest = [ vmodl.Binary() ]
            endorsementKeyCertificate = [ vmodl.Binary() ]

         class VirtualTPMOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualTPMOption
            supportedFirmware = [ "" ]

         class VirtualUSB(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualUSB
            connected = False
            vendor = 0
            product = 0
            family = [ "" ]
            speed = [ "" ]

            class USBBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualUSB.USBBackingInfo
               pass

            class RemoteHostBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualUSB.RemoteHostBackingInfo
               hostname = ""

            class RemoteClientBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo): # vim.vm.device.VirtualUSB.RemoteClientBackingInfo
               hostname = ""

         class VirtualUSBOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualUSBOption

            class USBBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualUSBOption.USBBackingOption
               pass

            class RemoteHostBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualUSBOption.RemoteHostBackingOption
               pass

            class RemoteClientBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption): # vim.vm.device.VirtualUSBOption.RemoteClientBackingOption
               pass

         class VirtualVMCIDevice(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualVMCIDevice
            id = 0
            allowUnrestrictedCommunication = False
            filterEnable = False
            filterInfo = vim.vm.device.VirtualVMCIDevice.FilterInfo()

            class Action(Enum): # vim.vm.device.VirtualVMCIDevice.Action
               allow = 0
               deny = 1

            class Protocol(Enum): # vim.vm.device.VirtualVMCIDevice.Protocol
               hypervisor = 0
               doorbell = 1
               queuepair = 2
               datagram = 3
               stream = 4
               anyProtocol = 5

            class Direction(Enum): # vim.vm.device.VirtualVMCIDevice.Direction
               guest = 0
               host = 1
               anyDirection = 2

            class FilterSpec(vmodl.DynamicData): # vim.vm.device.VirtualVMCIDevice.FilterSpec
               rank = 0
               action = ""
               protocol = ""
               direction = ""
               lowerDstPortBoundary = 0
               upperDstPortBoundary = 0

            class FilterInfo(vmodl.DynamicData): # vim.vm.device.VirtualVMCIDevice.FilterInfo
               filters = [ vim.vm.device.VirtualVMCIDevice.FilterSpec() ]

         class VirtualVMCIDeviceOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualVMCIDeviceOption
            allowUnrestrictedCommunication = vim.option.BoolOption()
            filterSpecOption = vim.vm.device.VirtualVMCIDeviceOption.FilterSpecOption()
            filterSupported = vim.option.BoolOption()

            class FilterSpecOption(vmodl.DynamicData): # vim.vm.device.VirtualVMCIDeviceOption.FilterSpecOption
               action = vim.option.ChoiceOption()
               protocol = vim.option.ChoiceOption()
               direction = vim.option.ChoiceOption()
               lowerDstPortBoundary = vim.option.LongOption()
               upperDstPortBoundary = vim.option.LongOption()

         class VirtualVMIROM(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualVMIROM
            pass

         class VirtualVMIROMOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualVMIROMOption
            pass

         class VirtualVideoCard(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualVideoCard
            videoRamSizeInKB = 0
            numDisplays = 0
            useAutoDetect = False
            enable3DSupport = False
            use3dRenderer = ""
            graphicsMemorySizeInKB = 0

            class Use3dRenderer(Enum): # vim.vm.device.VirtualVideoCard.Use3dRenderer
               automatic = 0
               software = 1
               hardware = 2

         class VirtualVideoCardOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualVideoCardOption
            videoRamSizeInKB = vim.option.LongOption()
            numDisplays = vim.option.IntOption()
            useAutoDetect = vim.option.BoolOption()
            support3D = vim.option.BoolOption()
            use3dRendererSupported = vim.option.BoolOption()
            graphicsMemorySizeInKB = vim.option.LongOption()
            graphicsMemorySizeSupported = vim.option.BoolOption()

         class VirtualVmxnet(vim.vm.device.VirtualEthernetCard): # vim.vm.device.VirtualVmxnet
            pass

         class VirtualVmxnet2(vim.vm.device.VirtualVmxnet): # vim.vm.device.VirtualVmxnet2
            pass

         class VirtualVmxnet3(vim.vm.device.VirtualVmxnet): # vim.vm.device.VirtualVmxnet3
            pass

         class VirtualVmxnet3Vrdma(vim.vm.device.VirtualVmxnet3): # vim.vm.device.VirtualVmxnet3Vrdma
            deviceProtocol = ""

         class VirtualVmxnetOption(vim.vm.device.VirtualEthernetCardOption): # vim.vm.device.VirtualVmxnetOption
            pass

         class VirtualWDT(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualWDT
            runOnBoot = False
            running = False

         class VirtualWDTOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualWDTOption
            runOnBoot = vim.option.BoolOption()

         class VirtualCdrom(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualCdrom

            class IsoBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo): # vim.vm.device.VirtualCdrom.IsoBackingInfo
               pass

            class PassthroughBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualCdrom.PassthroughBackingInfo
               exclusive = False

            class RemotePassthroughBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo): # vim.vm.device.VirtualCdrom.RemotePassthroughBackingInfo
               exclusive = False

            class AtapiBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo): # vim.vm.device.VirtualCdrom.AtapiBackingInfo
               pass

            class RemoteAtapiBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo): # vim.vm.device.VirtualCdrom.RemoteAtapiBackingInfo
               pass

         class VirtualCdromOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualCdromOption

            class IsoBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption): # vim.vm.device.VirtualCdromOption.IsoBackingOption
               pass

            class PassthroughBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualCdromOption.PassthroughBackingOption
               exclusive = vim.option.BoolOption()

            class RemotePassthroughBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption): # vim.vm.device.VirtualCdromOption.RemotePassthroughBackingOption
               exclusive = vim.option.BoolOption()

            class AtapiBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualCdromOption.AtapiBackingOption
               pass

            class RemoteAtapiBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption): # vim.vm.device.VirtualCdromOption.RemoteAtapiBackingOption
               pass

         class VirtualController(vim.vm.device.VirtualDevice): # vim.vm.device.VirtualController
            busNumber = 0
            device = [ 0 ]

         class VirtualControllerOption(vim.vm.device.VirtualDeviceOption): # vim.vm.device.VirtualControllerOption
            devices = vim.option.IntOption()
            supportedDevice = [ vmodl.TypeName() ]

         class VirtualE1000(vim.vm.device.VirtualEthernetCard): # vim.vm.device.VirtualE1000
            pass

         class VirtualE1000Option(vim.vm.device.VirtualEthernetCardOption): # vim.vm.device.VirtualE1000Option
            pass

         class VirtualE1000e(vim.vm.device.VirtualEthernetCard): # vim.vm.device.VirtualE1000e
            pass

         class VirtualE1000eOption(vim.vm.device.VirtualEthernetCardOption): # vim.vm.device.VirtualE1000eOption
            pass

         class VirtualEnsoniq1371(vim.vm.device.VirtualSoundCard): # vim.vm.device.VirtualEnsoniq1371
            pass

         class VirtualEnsoniq1371Option(vim.vm.device.VirtualSoundCardOption): # vim.vm.device.VirtualEnsoniq1371Option
            pass

         class VirtualHdAudioCard(vim.vm.device.VirtualSoundCard): # vim.vm.device.VirtualHdAudioCard
            pass

         class VirtualHdAudioCardOption(vim.vm.device.VirtualSoundCardOption): # vim.vm.device.VirtualHdAudioCardOption
            pass

         class VirtualIDEController(vim.vm.device.VirtualController): # vim.vm.device.VirtualIDEController
            pass

         class VirtualIDEControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualIDEControllerOption
            numIDEDisks = vim.option.IntOption()
            numIDECdroms = vim.option.IntOption()

         class VirtualNVDIMMController(vim.vm.device.VirtualController): # vim.vm.device.VirtualNVDIMMController
            pass

         class VirtualNVDIMMControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualNVDIMMControllerOption
            numNVDIMMControllers = vim.option.IntOption()

         class VirtualNVMEController(vim.vm.device.VirtualController): # vim.vm.device.VirtualNVMEController
            pass

         class VirtualNVMEControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualNVMEControllerOption
            numNVMEDisks = vim.option.IntOption()

         class VirtualPCIController(vim.vm.device.VirtualController): # vim.vm.device.VirtualPCIController
            pass

         class VirtualPCIControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualPCIControllerOption
            numSCSIControllers = vim.option.IntOption()
            numEthernetCards = vim.option.IntOption()
            numVideoCards = vim.option.IntOption()
            numSoundCards = vim.option.IntOption()
            numVmiRoms = vim.option.IntOption()
            numVmciDevices = vim.option.IntOption()
            numPCIPassthroughDevices = vim.option.IntOption()
            numSasSCSIControllers = vim.option.IntOption()
            numVmxnet3EthernetCards = vim.option.IntOption()
            numParaVirtualSCSIControllers = vim.option.IntOption()
            numSATAControllers = vim.option.IntOption()
            numNVMEControllers = vim.option.IntOption()
            numVmxnet3VrdmaEthernetCards = vim.option.IntOption()

         class VirtualPS2Controller(vim.vm.device.VirtualController): # vim.vm.device.VirtualPS2Controller
            pass

         class VirtualPS2ControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualPS2ControllerOption
            numKeyboards = vim.option.IntOption()
            numPointingDevices = vim.option.IntOption()

         class VirtualSATAController(vim.vm.device.VirtualController): # vim.vm.device.VirtualSATAController
            pass

         class VirtualSATAControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualSATAControllerOption
            numSATADisks = vim.option.IntOption()
            numSATACdroms = vim.option.IntOption()

         class VirtualSCSIController(vim.vm.device.VirtualController): # vim.vm.device.VirtualSCSIController
            hotAddRemove = False
            sharedBus = vim.vm.device.VirtualSCSIController.Sharing()
            scsiCtlrUnitNumber = 0

            class Sharing(Enum): # vim.vm.device.VirtualSCSIController.Sharing
               noSharing = 0
               virtualSharing = 1
               physicalSharing = 2

         class VirtualSCSIControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualSCSIControllerOption
            numSCSIDisks = vim.option.IntOption()
            numSCSICdroms = vim.option.IntOption()
            numSCSIPassthrough = vim.option.IntOption()
            sharing = [ vim.vm.device.VirtualSCSIController.Sharing() ]
            defaultSharedIndex = 0
            hotAddRemove = vim.option.BoolOption()
            scsiCtlrUnitNumber = 0

         class VirtualSIOController(vim.vm.device.VirtualController): # vim.vm.device.VirtualSIOController
            pass

         class VirtualSIOControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualSIOControllerOption
            numFloppyDrives = vim.option.IntOption()
            numSerialPorts = vim.option.IntOption()
            numParallelPorts = vim.option.IntOption()

         class VirtualSoundBlaster16(vim.vm.device.VirtualSoundCard): # vim.vm.device.VirtualSoundBlaster16
            pass

         class VirtualSoundBlaster16Option(vim.vm.device.VirtualSoundCardOption): # vim.vm.device.VirtualSoundBlaster16Option
            pass

         class VirtualUSBController(vim.vm.device.VirtualController): # vim.vm.device.VirtualUSBController
            autoConnectDevices = False
            ehciEnabled = False

            class PciBusSlotInfo(vim.vm.device.VirtualDevice.PciBusSlotInfo): # vim.vm.device.VirtualUSBController.PciBusSlotInfo
               ehciPciSlotNumber = 0

         class VirtualUSBControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualUSBControllerOption
            autoConnectDevices = vim.option.BoolOption()
            ehciSupported = vim.option.BoolOption()
            supportedSpeeds = [ "" ]

         class VirtualUSBXHCIController(vim.vm.device.VirtualController): # vim.vm.device.VirtualUSBXHCIController
            autoConnectDevices = False

         class VirtualUSBXHCIControllerOption(vim.vm.device.VirtualControllerOption): # vim.vm.device.VirtualUSBXHCIControllerOption
            autoConnectDevices = vim.option.BoolOption()
            supportedSpeeds = [ "" ]

         class VirtualVmxnet2Option(vim.vm.device.VirtualVmxnetOption): # vim.vm.device.VirtualVmxnet2Option
            pass

         class VirtualVmxnet3Option(vim.vm.device.VirtualVmxnetOption): # vim.vm.device.VirtualVmxnet3Option
            pass

         class VirtualVmxnet3VrdmaOption(vim.vm.device.VirtualVmxnet3Option): # vim.vm.device.VirtualVmxnet3VrdmaOption
            deviceProtocol = vim.option.ChoiceOption()

            class DeviceProtocols(Enum): # vim.vm.device.VirtualVmxnet3VrdmaOption.DeviceProtocols
               rocev1 = 0
               rocev2 = 1

         class ParaVirtualSCSIController(vim.vm.device.VirtualSCSIController): # vim.vm.device.ParaVirtualSCSIController
            pass

         class ParaVirtualSCSIControllerOption(vim.vm.device.VirtualSCSIControllerOption): # vim.vm.device.ParaVirtualSCSIControllerOption
            pass

         class VirtualAHCIController(vim.vm.device.VirtualSATAController): # vim.vm.device.VirtualAHCIController
            pass

         class VirtualAHCIControllerOption(vim.vm.device.VirtualSATAControllerOption): # vim.vm.device.VirtualAHCIControllerOption
            pass

         class VirtualBusLogicController(vim.vm.device.VirtualSCSIController): # vim.vm.device.VirtualBusLogicController
            pass

         class VirtualBusLogicControllerOption(vim.vm.device.VirtualSCSIControllerOption): # vim.vm.device.VirtualBusLogicControllerOption
            pass

         class VirtualLsiLogicController(vim.vm.device.VirtualSCSIController): # vim.vm.device.VirtualLsiLogicController
            pass

         class VirtualLsiLogicControllerOption(vim.vm.device.VirtualSCSIControllerOption): # vim.vm.device.VirtualLsiLogicControllerOption
            pass

         class VirtualLsiLogicSASController(vim.vm.device.VirtualSCSIController): # vim.vm.device.VirtualLsiLogicSASController
            pass

         class VirtualLsiLogicSASControllerOption(vim.vm.device.VirtualSCSIControllerOption): # vim.vm.device.VirtualLsiLogicSASControllerOption
            pass

      class guest(object): # (unknown name)

         class AliasManager(vmodl.ManagedObject): # vim.vm.guest.AliasManager

            def addAlias(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", mapCert=False, base64Cert="", aliasInfo=vim.vm.guest.AliasManager.GuestAuthAliasInfo()): # vim.vm.guest.AliasManager.addAlias
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def removeAlias(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", base64Cert="", subject=vim.vm.guest.AliasManager.GuestAuthSubject()): # vim.vm.guest.AliasManager.removeAlias
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def removeAliasByCert(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", base64Cert=""): # vim.vm.guest.AliasManager.removeAliasByCert
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listAliases(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username=""): # vim.vm.guest.AliasManager.listAliases
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.AliasManager.GuestAliases() ]

            def listMappedAliases(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()): # vim.vm.guest.AliasManager.listMappedAliases
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.AliasManager.GuestMappedAliases() ]

            class GuestAuthSubject(vmodl.DynamicData): # vim.vm.guest.AliasManager.GuestAuthSubject
               pass

            class GuestAuthAnySubject(vim.vm.guest.AliasManager.GuestAuthSubject): # vim.vm.guest.AliasManager.GuestAuthAnySubject
               pass

            class GuestAuthNamedSubject(vim.vm.guest.AliasManager.GuestAuthSubject): # vim.vm.guest.AliasManager.GuestAuthNamedSubject
               name = ""

            class GuestAuthAliasInfo(vmodl.DynamicData): # vim.vm.guest.AliasManager.GuestAuthAliasInfo
               subject = vim.vm.guest.AliasManager.GuestAuthSubject()
               comment = ""

            class GuestAliases(vmodl.DynamicData): # vim.vm.guest.AliasManager.GuestAliases
               base64Cert = ""
               aliases = [ vim.vm.guest.AliasManager.GuestAuthAliasInfo() ]

            class GuestMappedAliases(vmodl.DynamicData): # vim.vm.guest.AliasManager.GuestMappedAliases
               base64Cert = ""
               username = ""
               subjects = [ vim.vm.guest.AliasManager.GuestAuthSubject() ]

         class AuthManager(vmodl.ManagedObject): # vim.vm.guest.AuthManager

            def validateCredentials(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()): # vim.vm.guest.AuthManager.validateCredentials
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def acquireCredentials(vm=vim.VirtualMachine(), requestedAuth=vim.vm.guest.GuestAuthentication(), sessionID=0 or None): # vim.vm.guest.AuthManager.acquireCredentials
               # throws vim.fault.GuestOperationsFault, vim.fault.TaskInProgress, vim.fault.InvalidState
               return vim.vm.guest.GuestAuthentication()

            def releaseCredentials(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()): # vim.vm.guest.AuthManager.releaseCredentials
               # throws vim.fault.GuestOperationsFault, vim.fault.TaskInProgress, vim.fault.InvalidState
               return None

         class FileManager(vmodl.ManagedObject): # vim.vm.guest.FileManager

            def makeDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), directoryPath="", createParentDirectories=False): # vim.vm.guest.FileManager.makeDirectory
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def deleteFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), filePath=""): # vim.vm.guest.FileManager.deleteFile
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def deleteDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), directoryPath="", recursive=False): # vim.vm.guest.FileManager.deleteDirectory
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def moveDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), srcDirectoryPath="", dstDirectoryPath=""): # vim.vm.guest.FileManager.moveDirectory
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def moveFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), srcFilePath="", dstFilePath="", overwrite=False): # vim.vm.guest.FileManager.moveFile
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def createTemporaryFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), prefix="", suffix="", directoryPath="" or None): # vim.vm.guest.FileManager.createTemporaryFile
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            def createTemporaryDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), prefix="", suffix="", directoryPath="" or None): # vim.vm.guest.FileManager.createTemporaryDirectory
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            def listFiles(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), filePath="", index=0 or None, maxResults=0 or None, matchPattern="" or None): # vim.vm.guest.FileManager.listFiles
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return vim.vm.guest.FileManager.ListFileInfo()

            def changeFileAttributes(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath="", fileAttributes=vim.vm.guest.FileManager.FileAttributes()): # vim.vm.guest.FileManager.changeFileAttributes
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def initiateFileTransferFromGuest(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath=""): # vim.vm.guest.FileManager.initiateFileTransferFromGuest
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return vim.vm.guest.FileManager.FileTransferInformation()

            def initiateFileTransferToGuest(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath="", fileAttributes=vim.vm.guest.FileManager.FileAttributes(), fileSize=0, overwrite=False): # vim.vm.guest.FileManager.initiateFileTransferToGuest
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            class FileAttributes(vmodl.DynamicData): # vim.vm.guest.FileManager.FileAttributes
               modificationTime = vmodl.DateTime()
               accessTime = vmodl.DateTime()
               symlinkTarget = ""

            class PosixFileAttributes(vim.vm.guest.FileManager.FileAttributes): # vim.vm.guest.FileManager.PosixFileAttributes
               ownerId = 0
               groupId = 0
               permissions = 0

            class WindowsFileAttributes(vim.vm.guest.FileManager.FileAttributes): # vim.vm.guest.FileManager.WindowsFileAttributes
               hidden = False
               readOnly = False
               createTime = vmodl.DateTime()

            class FileInfo(vmodl.DynamicData): # vim.vm.guest.FileManager.FileInfo
               path = ""
               type = ""
               size = 0
               attributes = vim.vm.guest.FileManager.FileAttributes()

               class FileType(Enum): # vim.vm.guest.FileManager.FileInfo.FileType
                  file = 0
                  directory = 1
                  symlink = 2

            class ListFileInfo(vmodl.DynamicData): # vim.vm.guest.FileManager.ListFileInfo
               files = [ vim.vm.guest.FileManager.FileInfo() ]
               remaining = 0

            class FileTransferInformation(vmodl.DynamicData): # vim.vm.guest.FileManager.FileTransferInformation
               attributes = vim.vm.guest.FileManager.FileAttributes()
               size = 0
               url = ""

         class GuestAuthentication(vmodl.DynamicData): # vim.vm.guest.GuestAuthentication
            interactiveSession = False

         class GuestOperationsManager(vmodl.ManagedObject): # vim.vm.guest.GuestOperationsManager
            authManager = vim.vm.guest.AuthManager()
            fileManager = vim.vm.guest.FileManager()
            processManager = vim.vm.guest.ProcessManager()
            guestWindowsRegistryManager = vim.vm.guest.WindowsRegistryManager()
            aliasManager = vim.vm.guest.AliasManager()

         class NamePasswordAuthentication(vim.vm.guest.GuestAuthentication): # vim.vm.guest.NamePasswordAuthentication
            username = ""
            password = ""

         class ProcessManager(vmodl.ManagedObject): # vim.vm.guest.ProcessManager

            def startProgram(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), spec=vim.vm.guest.ProcessManager.ProgramSpec()): # vim.vm.guest.ProcessManager.startProgram
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return 0

            def listProcesses(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), pids=[ 0 ] or None): # vim.vm.guest.ProcessManager.listProcesses
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.ProcessManager.ProcessInfo() ]

            def terminateProcess(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), pid=0): # vim.vm.guest.ProcessManager.terminateProcess
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def readEnvironmentVariable(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), names=[ "" ] or None): # vim.vm.guest.ProcessManager.readEnvironmentVariable
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ "" ]

            class ProgramSpec(vmodl.DynamicData): # vim.vm.guest.ProcessManager.ProgramSpec
               programPath = ""
               arguments = ""
               workingDirectory = ""
               envVariables = [ "" ]

            class WindowsProgramSpec(vim.vm.guest.ProcessManager.ProgramSpec): # vim.vm.guest.ProcessManager.WindowsProgramSpec
               startMinimized = False

            class ProcessInfo(vmodl.DynamicData): # vim.vm.guest.ProcessManager.ProcessInfo
               name = ""
               pid = 0
               owner = ""
               cmdLine = ""
               startTime = vmodl.DateTime()
               endTime = vmodl.DateTime()
               exitCode = 0

         class SAMLTokenAuthentication(vim.vm.guest.GuestAuthentication): # vim.vm.guest.SAMLTokenAuthentication
            token = ""
            username = ""

         class SSPIAuthentication(vim.vm.guest.GuestAuthentication): # vim.vm.guest.SSPIAuthentication
            sspiToken = ""

         class TicketedSessionAuthentication(vim.vm.guest.GuestAuthentication): # vim.vm.guest.TicketedSessionAuthentication
            ticket = ""

         class WindowsRegistryManager(vmodl.ManagedObject): # vim.vm.guest.WindowsRegistryManager

            def createRegistryKey(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), isVolatile=False, classType="" or None): # vim.vm.guest.WindowsRegistryManager.createRegistryKey
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listRegistryKeys(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), recursive=False, matchPattern="" or None): # vim.vm.guest.WindowsRegistryManager.listRegistryKeys
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.WindowsRegistryManager.RegistryKeyRecord() ]

            def deleteRegistryKey(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), recursive=False): # vim.vm.guest.WindowsRegistryManager.deleteRegistryKey
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def setRegistryValue(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), value=vim.vm.guest.WindowsRegistryManager.RegistryValue()): # vim.vm.guest.WindowsRegistryManager.setRegistryValue
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listRegistryValues(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), expandStrings=False, matchPattern="" or None): # vim.vm.guest.WindowsRegistryManager.listRegistryValues
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.WindowsRegistryManager.RegistryValue() ]

            def deleteRegistryValue(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), valueName=vim.vm.guest.WindowsRegistryManager.RegistryValueName()): # vim.vm.guest.WindowsRegistryManager.deleteRegistryValue
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            class RegistryKeyName(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryKeyName
               registryPath = ""
               wowBitness = ""

               class RegistryKeyWowBitness(Enum): # vim.vm.guest.WindowsRegistryManager.RegistryKeyName.RegistryKeyWowBitness
                  WOWNative = 0
                  WOW32 = 1
                  WOW64 = 2

            class RegistryKey(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryKey
               keyName = vim.vm.guest.WindowsRegistryManager.RegistryKeyName()
               classType = ""
               lastWritten = vmodl.DateTime()

            class RegistryKeyRecord(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryKeyRecord
               key = vim.vm.guest.WindowsRegistryManager.RegistryKey()
               fault = vmodl.MethodFault()

            class RegistryValueName(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryValueName
               keyName = vim.vm.guest.WindowsRegistryManager.RegistryKeyName()
               name = ""

            class RegistryValueData(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryValueData
               pass

            class RegistryValueDword(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueDword
               value = 0

            class RegistryValueQword(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueQword
               value = 0

            class RegistryValueString(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueString
               value = ""

            class RegistryValueExpandString(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueExpandString
               value = ""

            class RegistryValueMultiString(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueMultiString
               value = [ "" ]

            class RegistryValueBinary(vim.vm.guest.WindowsRegistryManager.RegistryValueData): # vim.vm.guest.WindowsRegistryManager.RegistryValueBinary
               value = vmodl.Binary()

            class RegistryValue(vmodl.DynamicData): # vim.vm.guest.WindowsRegistryManager.RegistryValue
               name = vim.vm.guest.WindowsRegistryManager.RegistryValueName()
               data = vim.vm.guest.WindowsRegistryManager.RegistryValueData()

      class replication(object): # (unknown name)

         class DeviceGroupId(vmodl.DynamicData): # vim.vm.replication.DeviceGroupId
            id = ""

         class FaultDomainId(vmodl.DynamicData): # vim.vm.replication.FaultDomainId
            id = ""

         class ReplicationGroupId(vmodl.DynamicData): # vim.vm.replication.ReplicationGroupId
            faultDomainId = vim.vm.replication.FaultDomainId()
            deviceGroupId = vim.vm.replication.DeviceGroupId()

         class ReplicationSpec(vmodl.DynamicData): # vim.vm.replication.ReplicationSpec
            replicationGroupId = vim.vm.replication.ReplicationGroupId()

      class CdromInfo(vim.vm.TargetInfo): # vim.vm.CdromInfo
         description = ""

      class ConfigTarget(vmodl.DynamicData): # vim.vm.ConfigTarget
         numCpus = 0
         numCpuCores = 0
         numNumaNodes = 0
         maxCpusPerHost = 0
         smcPresent = False
         datastore = [ vim.vm.DatastoreInfo() ]
         network = [ vim.vm.NetworkInfo() ]
         opaqueNetwork = [ vim.vm.OpaqueNetworkInfo() ]
         distributedVirtualPortgroup = [ vim.dvs.DistributedVirtualPortgroupInfo() ]
         distributedVirtualSwitch = [ vim.dvs.DistributedVirtualSwitchInfo() ]
         cdRom = [ vim.vm.CdromInfo() ]
         serial = [ vim.vm.SerialInfo() ]
         parallel = [ vim.vm.ParallelInfo() ]
         sound = [ vim.vm.SoundInfo() ]
         usb = [ vim.vm.UsbInfo() ]
         floppy = [ vim.vm.FloppyInfo() ]
         legacyNetworkInfo = [ vim.vm.LegacyNetworkSwitchInfo() ]
         scsiPassthrough = [ vim.vm.ScsiPassthroughInfo() ]
         scsiDisk = [ vim.vm.ScsiDiskDeviceInfo() ]
         ideDisk = [ vim.vm.IdeDiskDeviceInfo() ]
         maxMemMBOptimalPerf = 0
         supportedMaxMemMB = 0
         resourcePool = vim.ResourcePool.RuntimeInfo()
         autoVmotion = False
         pciPassthrough = [ vim.vm.PciPassthroughInfo() ]
         sriov = [ vim.vm.SriovInfo() ]
         vFlashModule = [ vim.vm.VFlashModuleInfo() ]
         sharedGpuPassthroughTypes = [ vim.vm.PciSharedGpuPassthroughInfo() ]
         availablePersistentMemoryReservationMB = 0
         dynamicPassthrough = [ vim.vm.DynamicPassthroughInfo() ]
         sgxTargetInfo = vim.vm.SgxTargetInfo()
         precisionClockInfo = [ vim.vm.PrecisionClockInfo() ]

      class DefaultProfileSpec(vim.vm.ProfileSpec): # vim.vm.DefaultProfileSpec
         pass

      class DefinedProfileSpec(vim.vm.ProfileSpec): # vim.vm.DefinedProfileSpec
         profileId = ""
         replicationSpec = vim.vm.replication.ReplicationSpec()
         profileData = vim.vm.ProfileRawData()
         profileParams = [ vim.KeyValue() ]

      class DiskDeviceInfo(vim.vm.TargetInfo): # vim.vm.DiskDeviceInfo
         capacity = 0
         vm = [ vim.VirtualMachine() ]

      class DynamicPassthroughInfo(vim.vm.TargetInfo): # vim.vm.DynamicPassthroughInfo
         vendorName = ""
         deviceName = ""
         customLabel = ""
         vendorId = 0
         deviceId = 0

      class EmptyProfileSpec(vim.vm.ProfileSpec): # vim.vm.EmptyProfileSpec
         pass

      class FloppyInfo(vim.vm.TargetInfo): # vim.vm.FloppyInfo
         pass

      class IdeDiskDeviceInfo(vim.vm.DiskDeviceInfo): # vim.vm.IdeDiskDeviceInfo
         partitionTable = [ vim.vm.IdeDiskDeviceInfo.PartitionInfo() ]

         class PartitionInfo(vmodl.DynamicData): # vim.vm.IdeDiskDeviceInfo.PartitionInfo
            id = 0
            capacity = 0

      class NetworkInfo(vim.vm.TargetInfo): # vim.vm.NetworkInfo
         network = vim.Network.Summary()
         vswitch = ""

      class OpaqueNetworkInfo(vim.vm.TargetInfo): # vim.vm.OpaqueNetworkInfo
         network = vim.OpaqueNetwork.Summary()
         networkReservationSupported = False

      class ParallelInfo(vim.vm.TargetInfo): # vim.vm.ParallelInfo
         pass

      class PciPassthroughInfo(vim.vm.TargetInfo): # vim.vm.PciPassthroughInfo
         pciDevice = vim.host.PciDevice()
         systemId = ""

      class PciSharedGpuPassthroughInfo(vim.vm.TargetInfo): # vim.vm.PciSharedGpuPassthroughInfo
         vgpu = ""

      class PrecisionClockInfo(vim.vm.TargetInfo): # vim.vm.PrecisionClockInfo
         systemClockProtocol = ""

      class RelocateSpec(vmodl.DynamicData): # vim.vm.RelocateSpec
         service = vim.ServiceLocator()
         folder = vim.Folder()
         datastore = vim.Datastore()
         diskMoveType = ""
         pool = vim.ResourcePool()
         host = vim.HostSystem()
         disk = [ vim.vm.RelocateSpec.DiskLocator() ]
         transform = vim.vm.RelocateSpec.Transformation()
         deviceChange = [ vim.vm.device.VirtualDeviceSpec() ]
         profile = [ vim.vm.ProfileSpec() ]
         cryptoSpec = vim.encryption.CryptoSpec()

         class Transformation(Enum): # vim.vm.RelocateSpec.Transformation
            flat = 0
            sparse = 1

         class DiskLocator(vmodl.DynamicData): # vim.vm.RelocateSpec.DiskLocator
            diskId = 0
            datastore = vim.Datastore()
            diskMoveType = ""
            diskBackingInfo = vim.vm.device.VirtualDevice.BackingInfo()
            profile = [ vim.vm.ProfileSpec() ]
            backing = vim.vm.RelocateSpec.DiskLocator.BackingSpec()

            class BackingSpec(vmodl.DynamicData): # vim.vm.RelocateSpec.DiskLocator.BackingSpec
               parent = vim.vm.RelocateSpec.DiskLocator.BackingSpec()
               crypto = vim.encryption.CryptoSpec()

         class DiskMoveOptions(Enum): # vim.vm.RelocateSpec.DiskMoveOptions
            moveAllDiskBackingsAndAllowSharing = 0
            moveAllDiskBackingsAndDisallowSharing = 1
            moveChildMostDiskBacking = 2
            createNewChildDiskBacking = 3
            moveAllDiskBackingsAndConsolidate = 4

      class RuntimeInfo(vmodl.DynamicData): # vim.vm.RuntimeInfo
         device = [ vim.vm.DeviceRuntimeInfo() ]
         host = vim.HostSystem()
         connectionState = vim.VirtualMachine.ConnectionState()
         powerState = vim.VirtualMachine.PowerState()
         faultToleranceState = vim.VirtualMachine.FaultToleranceState()
         dasVmProtection = vim.vm.RuntimeInfo.DasProtectionState()
         toolsInstallerMounted = False
         suspendTime = vmodl.DateTime()
         bootTime = vmodl.DateTime()
         suspendInterval = 0
         question = vim.vm.QuestionInfo()
         memoryOverhead = 0
         maxCpuUsage = 0
         maxMemoryUsage = 0
         numMksConnections = 0
         recordReplayState = vim.VirtualMachine.RecordReplayState()
         cleanPowerOff = False
         needSecondaryReason = ""
         onlineStandby = False
         minRequiredEVCModeKey = ""
         consolidationNeeded = False
         offlineFeatureRequirement = [ vim.vm.FeatureRequirement() ]
         featureRequirement = [ vim.vm.FeatureRequirement() ]
         featureMask = [ vim.host.FeatureMask() ]
         vFlashCacheAllocation = 0
         paused = False
         snapshotInBackground = False
         quiescedForkParent = False
         instantCloneFrozen = False
         cryptoState = ""

         class DasProtectionState(vmodl.DynamicData): # vim.vm.RuntimeInfo.DasProtectionState
            dasProtected = False

      class ScsiDiskDeviceInfo(vim.vm.DiskDeviceInfo): # vim.vm.ScsiDiskDeviceInfo
         disk = vim.host.ScsiDisk()
         transportHint = ""
         lunNumber = 0

      class ScsiPassthroughInfo(vim.vm.TargetInfo): # vim.vm.ScsiPassthroughInfo
         scsiClass = ""
         vendor = ""
         physicalUnitNumber = 0

         class ScsiClass(Enum): # vim.vm.ScsiPassthroughInfo.ScsiClass
            disk = 0
            tape = 1
            printer = 2
            processor = 3
            worm = 4
            cdrom = 5
            scanner = 6
            optical = 7
            media = 8
            com = 9
            raid = 10
            unknown = 11

      class SerialInfo(vim.vm.TargetInfo): # vim.vm.SerialInfo
         pass

      class SgxTargetInfo(vim.vm.TargetInfo): # vim.vm.SgxTargetInfo
         maxEpcSize = 0
         flcModes = [ "" ]
         lePubKeyHashes = [ "" ]

      class SnapshotTree(vmodl.DynamicData): # vim.vm.SnapshotTree
         snapshot = vim.vm.Snapshot()
         vm = vim.VirtualMachine()
         name = ""
         description = ""
         id = 0
         createTime = vmodl.DateTime()
         state = vim.VirtualMachine.PowerState()
         quiesced = False
         backupManifest = ""
         childSnapshotList = [ vim.vm.SnapshotTree() ]
         replaySupported = False

      class SoundInfo(vim.vm.TargetInfo): # vim.vm.SoundInfo
         pass

      class SriovInfo(vim.vm.PciPassthroughInfo): # vim.vm.SriovInfo
         virtualFunction = False
         pnic = ""
         devicePool = vim.vm.SriovDevicePoolInfo()

      class Summary(vmodl.DynamicData): # vim.vm.Summary
         vm = vim.VirtualMachine()
         runtime = vim.vm.RuntimeInfo()
         guest = vim.vm.Summary.GuestSummary()
         config = vim.vm.Summary.ConfigSummary()
         storage = vim.vm.Summary.StorageSummary()
         quickStats = vim.vm.Summary.QuickStats()
         overallStatus = vim.ManagedEntity.Status()
         customValue = [ vim.CustomFieldsManager.Value() ]

         class ConfigSummary(vmodl.DynamicData): # vim.vm.Summary.ConfigSummary
            name = ""
            template = False
            vmPathName = ""
            memorySizeMB = 0
            cpuReservation = 0
            memoryReservation = 0
            numCpu = 0
            numEthernetCards = 0
            numVirtualDisks = 0
            uuid = ""
            instanceUuid = ""
            guestId = ""
            guestFullName = ""
            annotation = ""
            product = vim.vApp.ProductInfo()
            installBootRequired = False
            ftInfo = vim.vm.FaultToleranceConfigInfo()
            managedBy = vim.ext.ManagedByInfo()
            tpmPresent = False
            numVmiopBackings = 0
            hwVersion = ""

         class QuickStats(vmodl.DynamicData): # vim.vm.Summary.QuickStats
            overallCpuUsage = 0
            overallCpuDemand = 0
            overallCpuReadiness = 0
            guestMemoryUsage = 0
            hostMemoryUsage = 0
            guestHeartbeatStatus = vim.ManagedEntity.Status()
            distributedCpuEntitlement = 0
            distributedMemoryEntitlement = 0
            staticCpuEntitlement = 0
            staticMemoryEntitlement = 0
            grantedMemory = 0
            privateMemory = 0
            sharedMemory = 0
            swappedMemory = 0
            balloonedMemory = 0
            consumedOverheadMemory = 0
            ftLogBandwidth = 0
            ftSecondaryLatency = 0
            ftLatencyStatus = vim.ManagedEntity.Status()
            compressedMemory = 0
            uptimeSeconds = 0
            ssdSwappedMemory = 0

         class GuestSummary(vmodl.DynamicData): # vim.vm.Summary.GuestSummary
            guestId = ""
            guestFullName = ""
            toolsStatus = vim.vm.GuestInfo.ToolsStatus()
            toolsVersionStatus = ""
            toolsVersionStatus2 = ""
            toolsRunningStatus = ""
            hostName = ""
            ipAddress = ""
            hwVersion = ""

         class StorageSummary(vmodl.DynamicData): # vim.vm.Summary.StorageSummary
            committed = 0
            uncommitted = 0
            unshared = 0
            timestamp = vmodl.DateTime()

      class VFlashModuleInfo(vim.vm.TargetInfo): # vim.vm.VFlashModuleInfo
         vFlashModule = vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption()

      class VmImportSpec(vim.ImportSpec): # vim.vm.VmImportSpec
         configSpec = vim.vm.ConfigSpec()
         resPoolEntity = vim.ResourcePool()

      class DatastoreInfo(vim.vm.TargetInfo): # vim.vm.DatastoreInfo
         datastore = vim.Datastore.Summary()
         capability = vim.Datastore.Capability()
         maxFileSize = 0
         maxVirtualDiskCapacity = 0
         maxPhysicalRDMFileSize = 0
         maxVirtualRDMFileSize = 0
         mode = ""
         vStorageSupport = ""

   class vsan(object): # (unknown name)

      class cluster(object): # (unknown name)

         class ConfigInfo(vmodl.DynamicData): # vim.vsan.cluster.ConfigInfo
            enabled = False
            defaultConfig = vim.vsan.cluster.ConfigInfo.HostDefaultInfo()

            class HostDefaultInfo(vmodl.DynamicData): # vim.vsan.cluster.ConfigInfo.HostDefaultInfo
               uuid = ""
               autoClaimStorage = False
               checksumEnabled = False

      class host(object): # (unknown name)

         class ClusterStatus(vmodl.DynamicData): # vim.vsan.host.ClusterStatus
            uuid = ""
            nodeUuid = ""
            health = ""
            nodeState = vim.vsan.host.ClusterStatus.State()
            memberUuid = [ "" ]

            class State(vmodl.DynamicData): # vim.vsan.host.ClusterStatus.State
               state = ""
               completion = vim.vsan.host.ClusterStatus.State.CompletionEstimate()

               class CompletionEstimate(vmodl.DynamicData): # vim.vsan.host.ClusterStatus.State.CompletionEstimate
                  completeTime = vmodl.DateTime()
                  percentComplete = 0

         class ConfigInfo(vmodl.DynamicData): # vim.vsan.host.ConfigInfo
            enabled = False
            hostSystem = vim.HostSystem()
            clusterInfo = vim.vsan.host.ConfigInfo.ClusterInfo()
            storageInfo = vim.vsan.host.ConfigInfo.StorageInfo()
            networkInfo = vim.vsan.host.ConfigInfo.NetworkInfo()
            faultDomainInfo = vim.vsan.host.ConfigInfo.FaultDomainInfo()

            class StorageInfo(vmodl.DynamicData): # vim.vsan.host.ConfigInfo.StorageInfo
               autoClaimStorage = False
               diskMapping = [ vim.vsan.host.DiskMapping() ]
               diskMapInfo = [ vim.vsan.host.DiskMapInfo() ]
               checksumEnabled = False

            class ClusterInfo(vmodl.DynamicData): # vim.vsan.host.ConfigInfo.ClusterInfo
               uuid = ""
               nodeUuid = ""

            class NetworkInfo(vmodl.DynamicData): # vim.vsan.host.ConfigInfo.NetworkInfo
               port = [ vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig() ]

               class PortConfig(vmodl.DynamicData): # vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig
                  ipConfig = vim.vsan.host.IpConfig()
                  device = ""

            class FaultDomainInfo(vmodl.DynamicData): # vim.vsan.host.ConfigInfo.FaultDomainInfo
               name = ""

         class DecommissionMode(vmodl.DynamicData): # vim.vsan.host.DecommissionMode
            objectAction = ""

            class ObjectAction(Enum): # vim.vsan.host.DecommissionMode.ObjectAction
               noAction = 0
               ensureObjectAccessibility = 1
               evacuateAllData = 2

         class DiskMapInfo(vmodl.DynamicData): # vim.vsan.host.DiskMapInfo
            mapping = vim.vsan.host.DiskMapping()
            mounted = False

         class DiskMapResult(vmodl.DynamicData): # vim.vsan.host.DiskMapResult
            mapping = vim.vsan.host.DiskMapping()
            diskResult = [ vim.vsan.host.DiskResult() ]
            error = vmodl.MethodFault()

         class DiskMapping(vmodl.DynamicData): # vim.vsan.host.DiskMapping
            ssd = vim.host.ScsiDisk()
            nonSsd = [ vim.host.ScsiDisk() ]

         class DiskResult(vmodl.DynamicData): # vim.vsan.host.DiskResult
            disk = vim.host.ScsiDisk()
            state = ""
            vsanUuid = ""
            error = vmodl.MethodFault()
            degraded = False

            class State(Enum): # vim.vsan.host.DiskResult.State
               inUse = 0
               eligible = 1
               ineligible = 2

         class HealthState(Enum): # vim.vsan.host.HealthState
            unknown = 0
            healthy = 1
            unhealthy = 2

         class IpConfig(vmodl.DynamicData): # vim.vsan.host.IpConfig
            upstreamIpAddress = ""
            downstreamIpAddress = ""

         class MembershipInfo(vmodl.DynamicData): # vim.vsan.host.MembershipInfo
            nodeUuid = ""
            hostname = ""

         class NodeState(Enum): # vim.vsan.host.NodeState
            error = 0
            disabled = 1
            agent = 2
            master = 3
            backup = 4
            starting = 5
            stopping = 6
            enteringMaintenanceMode = 7
            exitingMaintenanceMode = 8
            decommissioning = 9

         class VsanDiskInfo(vmodl.DynamicData): # vim.vsan.host.VsanDiskInfo
            vsanUuid = ""
            formatVersion = 0

         class VsanRuntimeInfo(vmodl.DynamicData): # vim.vsan.host.VsanRuntimeInfo
            membershipList = [ vim.vsan.host.MembershipInfo() ]
            diskIssues = [ vim.vsan.host.VsanRuntimeInfo.DiskIssue() ]
            accessGenNo = 0

            class DiskIssueType(Enum): # vim.vsan.host.VsanRuntimeInfo.DiskIssueType
               nonExist = 0
               stampMismatch = 1
               unknown = 2

            class DiskIssue(vmodl.DynamicData): # vim.vsan.host.VsanRuntimeInfo.DiskIssue
               diskId = ""
               issue = ""

   class vslm(object): # (unknown name)

      class BaseConfigInfo(vmodl.DynamicData): # vim.vslm.BaseConfigInfo
         id = vim.vslm.ID()
         name = ""
         createTime = vmodl.DateTime()
         keepAfterDeleteVm = False
         relocationDisabled = False
         nativeSnapshotSupported = False
         changedBlockTrackingEnabled = False
         backing = vim.vslm.BaseConfigInfo.BackingInfo()
         iofilter = [ "" ]

         class BackingInfo(vmodl.DynamicData): # vim.vslm.BaseConfigInfo.BackingInfo
            datastore = vim.Datastore()

         class FileBackingInfo(vim.vslm.BaseConfigInfo.BackingInfo): # vim.vslm.BaseConfigInfo.FileBackingInfo
            filePath = ""
            backingObjectId = ""
            parent = vim.vslm.BaseConfigInfo.FileBackingInfo()
            deltaSizeInMB = 0
            keyId = vim.encryption.CryptoKeyId()

         class DiskFileBackingInfo(vim.vslm.BaseConfigInfo.FileBackingInfo): # vim.vslm.BaseConfigInfo.DiskFileBackingInfo
            provisioningType = ""

            class ProvisioningType(Enum): # vim.vslm.BaseConfigInfo.DiskFileBackingInfo.ProvisioningType
               thin = 0
               eagerZeroedThick = 1
               lazyZeroedThick = 2

         class RawDiskMappingBackingInfo(vim.vslm.BaseConfigInfo.FileBackingInfo): # vim.vslm.BaseConfigInfo.RawDiskMappingBackingInfo
            lunUuid = ""
            compatibilityMode = ""

      class CreateSpec(vmodl.DynamicData): # vim.vslm.CreateSpec
         name = ""
         keepAfterDeleteVm = False
         backingSpec = vim.vslm.CreateSpec.BackingSpec()
         capacityInMB = 0
         profile = [ vim.vm.ProfileSpec() ]
         crypto = vim.encryption.CryptoSpec()
         metadata = [ vim.KeyValue() ]

         class BackingSpec(vmodl.DynamicData): # vim.vslm.CreateSpec.BackingSpec
            datastore = vim.Datastore()
            path = ""

         class DiskFileBackingSpec(vim.vslm.CreateSpec.BackingSpec): # vim.vslm.CreateSpec.DiskFileBackingSpec
            provisioningType = ""

         class RawDiskMappingBackingSpec(vim.vslm.CreateSpec.BackingSpec): # vim.vslm.CreateSpec.RawDiskMappingBackingSpec
            lunUuid = ""
            compatibilityMode = ""

      class DiskCryptoSpec(vmodl.DynamicData): # vim.vslm.DiskCryptoSpec
         parent = vim.vslm.DiskCryptoSpec()
         crypto = vim.encryption.CryptoSpec()

      class ID(vmodl.DynamicData): # vim.vslm.ID
         id = ""

      class InfrastructureObjectPolicy(vmodl.DynamicData): # vim.vslm.InfrastructureObjectPolicy
         name = ""
         backingObjectId = ""
         profileId = ""
         error = vmodl.MethodFault()

      class InfrastructureObjectPolicySpec(vmodl.DynamicData): # vim.vslm.InfrastructureObjectPolicySpec
         datastore = vim.Datastore()
         profile = [ vim.vm.ProfileSpec() ]

      class MigrateSpec(vmodl.DynamicData): # vim.vslm.MigrateSpec
         backingSpec = vim.vslm.CreateSpec.BackingSpec()
         profile = [ vim.vm.ProfileSpec() ]
         consolidate = False
         disksCrypto = vim.vslm.DiskCryptoSpec()

      class RelocateSpec(vim.vslm.MigrateSpec): # vim.vslm.RelocateSpec
         pass

      class StateInfo(vmodl.DynamicData): # vim.vslm.StateInfo
         tentative = False

      class TagEntry(vmodl.DynamicData): # vim.vslm.TagEntry
         tagName = ""
         parentCategoryName = ""

      class VStorageObject(vmodl.DynamicData): # vim.vslm.VStorageObject
         config = vim.vslm.VStorageObject.ConfigInfo()

         class ConsumptionType(Enum): # vim.vslm.VStorageObject.ConsumptionType
            disk = 0

         class ConfigInfo(vim.vslm.BaseConfigInfo): # vim.vslm.VStorageObject.ConfigInfo
            capacityInMB = 0
            consumptionType = [ "" ]
            consumerId = [ vim.vslm.ID() ]

      class VStorageObjectControlFlag(Enum): # vim.vslm.VStorageObjectControlFlag
         keepAfterDeleteVm = 0
         disableRelocation = 1
         enableChangedBlockTracking = 2

      class VStorageObjectManagerBase(vmodl.ManagedObject): # vim.vslm.VStorageObjectManagerBase
         pass

      class VStorageObjectSnapshotDetails(vmodl.DynamicData): # vim.vslm.VStorageObjectSnapshotDetails
         path = ""
         changedBlockTrackingId = ""

      class VStorageObjectSnapshotInfo(vmodl.DynamicData): # vim.vslm.VStorageObjectSnapshotInfo
         snapshots = [ vim.vslm.VStorageObjectSnapshotInfo.VStorageObjectSnapshot() ]

         class VStorageObjectSnapshot(vmodl.DynamicData): # vim.vslm.VStorageObjectSnapshotInfo.VStorageObjectSnapshot
            id = vim.vslm.ID()
            backingObjectId = ""
            createTime = vmodl.DateTime()
            description = ""

      class vcenter(object): # (unknown name)

         class RetrieveVStorageObjSpec(vmodl.DynamicData): # vim.vslm.vcenter.RetrieveVStorageObjSpec
            id = vim.vslm.ID()
            datastore = vim.Datastore()

         class VStorageObjectAssociations(vmodl.DynamicData): # vim.vslm.vcenter.VStorageObjectAssociations
            id = vim.vslm.ID()
            vmDiskAssociations = [ vim.vslm.vcenter.VStorageObjectAssociations.VmDiskAssociations() ]
            fault = vmodl.MethodFault()

            class VmDiskAssociations(vmodl.DynamicData): # vim.vslm.vcenter.VStorageObjectAssociations.VmDiskAssociations
               vmId = ""
               diskKey = 0

         class VStorageObjectManager(vim.vslm.VStorageObjectManagerBase): # vim.vslm.vcenter.VStorageObjectManager

            def createDisk(spec=vim.vslm.CreateSpec()): # vim.vslm.vcenter.VStorageObjectManager.createDisk
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore
               return vim.Task()

            def registerDisk(path="", name="" or None): # vim.vslm.vcenter.VStorageObjectManager.registerDisk
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.AlreadyExists
               return vim.vslm.VStorageObject()

            def extendDisk(id=vim.vslm.ID(), datastore=vim.Datastore(), newCapacityInMB=0): # vim.vslm.vcenter.VStorageObjectManager.extendDisk
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def inflateDisk(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.inflateDisk
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def renameVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), name=""): # vim.vslm.vcenter.VStorageObjectManager.renameVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def updateVStorageObjectPolicy(id=vim.vslm.ID(), datastore=vim.Datastore(), profile=[ vim.vm.ProfileSpec() ] or None): # vim.vslm.vcenter.VStorageObjectManager.updateVStorageObjectPolicy
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def updateVStorageObjectCrypto(id=vim.vslm.ID(), datastore=vim.Datastore(), profile=[ vim.vm.ProfileSpec() ] or None, disksCrypto=vim.vslm.DiskCryptoSpec() or None): # vim.vslm.vcenter.VStorageObjectManager.updateVStorageObjectCrypto
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def updateVStorageInfrastructureObjectPolicy(spec=vim.vslm.InfrastructureObjectPolicySpec()): # vim.vslm.vcenter.VStorageObjectManager.updateVStorageInfrastructureObjectPolicy
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageInfrastructureObjectPolicy(datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.retrieveVStorageInfrastructureObjectPolicy
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState
               return [ vim.vslm.InfrastructureObjectPolicy() ]

            def deleteVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.deleteVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.retrieveVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.VStorageObject()

            def retrieveVStorageObjectState(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.retrieveVStorageObjectState
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.StateInfo()

            def retrieveVStorageObjectAssociations(ids=[ vim.vslm.vcenter.RetrieveVStorageObjSpec() ] or None): # vim.vslm.vcenter.VStorageObjectManager.retrieveVStorageObjectAssociations
               return [ vim.vslm.vcenter.VStorageObjectAssociations() ]

            def listVStorageObject(datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.listVStorageObject
               # throws vim.fault.InvalidDatastore
               return [ vim.vslm.ID() ]

            def cloneVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.CloneSpec()): # vim.vslm.vcenter.VStorageObjectManager.cloneVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def relocateVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.RelocateSpec()): # vim.vslm.vcenter.VStorageObjectManager.relocateVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def setVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None): # vim.vslm.vcenter.VStorageObjectManager.setVStorageObjectControlFlags
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def clearVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None): # vim.vslm.vcenter.VStorageObjectManager.clearVStorageObjectControlFlags
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def attachTagToVStorageObject(id=vim.vslm.ID(), category="", tag=""): # vim.vslm.vcenter.VStorageObjectManager.attachTagToVStorageObject
               # throws vim.fault.NotFound
               return None

            def detachTagFromVStorageObject(id=vim.vslm.ID(), category="", tag=""): # vim.vslm.vcenter.VStorageObjectManager.detachTagFromVStorageObject
               # throws vim.fault.NotFound
               return None

            def listVStorageObjectsAttachedToTag(category="", tag=""): # vim.vslm.vcenter.VStorageObjectManager.listVStorageObjectsAttachedToTag
               # throws vim.fault.NotFound
               return [ vim.vslm.ID() ]

            def listTagsAttachedToVStorageObject(id=vim.vslm.ID()): # vim.vslm.vcenter.VStorageObjectManager.listTagsAttachedToVStorageObject
               # throws vim.fault.NotFound
               return [ vim.vslm.TagEntry() ]

            def reconcileDatastoreInventory(datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.reconcileDatastoreInventory
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def scheduleReconcileDatastoreInventory(datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.scheduleReconcileDatastoreInventory
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def createSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), description=""): # vim.vslm.vcenter.VStorageObjectManager.createSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def deleteSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()): # vim.vslm.vcenter.VStorageObjectManager.deleteSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotInfo(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.vcenter.VStorageObjectManager.retrieveSnapshotInfo
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotInfo()

            def createDiskFromSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), name="", profile=[ vim.vm.ProfileSpec() ] or None, crypto=vim.encryption.CryptoSpec() or None, path="" or None): # vim.vslm.vcenter.VStorageObjectManager.createDiskFromSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def RevertVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()): # vim.vslm.vcenter.VStorageObjectManager.RevertVStorageObject
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotDetails(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()): # vim.vslm.vcenter.VStorageObjectManager.retrieveSnapshotDetails
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotDetails()

            def queryChangedDiskAreas(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), startOffset=0, changeId=""): # vim.vslm.vcenter.VStorageObjectManager.queryChangedDiskAreas
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState, vmodl.fault.InvalidArgument
               return vim.VirtualMachine.DiskChangeInfo()

      class CloneSpec(vim.vslm.MigrateSpec): # vim.vslm.CloneSpec
         name = ""
         keepAfterDeleteVm = False
         metadata = [ vim.KeyValue() ]

      class host(object): # (unknown name)

         class VStorageObjectManager(vim.vslm.VStorageObjectManagerBase): # vim.vslm.host.VStorageObjectManager

            def createDisk(spec=vim.vslm.CreateSpec()): # vim.vslm.host.VStorageObjectManager.createDisk
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore
               return vim.Task()

            def registerDisk(path="", name="" or None): # vim.vslm.host.VStorageObjectManager.registerDisk
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.AlreadyExists
               return vim.vslm.VStorageObject()

            def extendDisk(id=vim.vslm.ID(), datastore=vim.Datastore(), newCapacityInMB=0): # vim.vslm.host.VStorageObjectManager.extendDisk
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def inflateDisk(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.inflateDisk
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def renameVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), name=""): # vim.vslm.host.VStorageObjectManager.renameVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def retrieveVStorageInfrastructureObjectPolicy(datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.retrieveVStorageInfrastructureObjectPolicy
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState
               return [ vim.vslm.InfrastructureObjectPolicy() ]

            def deleteVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.deleteVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.retrieveVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.VStorageObject()

            def retrieveVStorageObjectState(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.retrieveVStorageObjectState
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.StateInfo()

            def listVStorageObject(datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.listVStorageObject
               # throws vim.fault.InvalidDatastore
               return [ vim.vslm.ID() ]

            def cloneVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.CloneSpec()): # vim.vslm.host.VStorageObjectManager.cloneVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def relocateVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.RelocateSpec()): # vim.vslm.host.VStorageObjectManager.relocateVStorageObject
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def setVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None): # vim.vslm.host.VStorageObjectManager.setVStorageObjectControlFlags
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def clearVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None): # vim.vslm.host.VStorageObjectManager.clearVStorageObjectControlFlags
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def reconcileDatastoreInventory(datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.reconcileDatastoreInventory
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def scheduleReconcileDatastoreInventory(datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.scheduleReconcileDatastoreInventory
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def createSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), description=""): # vim.vslm.host.VStorageObjectManager.createSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def deleteSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()): # vim.vslm.host.VStorageObjectManager.deleteSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotInfo(id=vim.vslm.ID(), datastore=vim.Datastore()): # vim.vslm.host.VStorageObjectManager.retrieveSnapshotInfo
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotInfo()

            def createDiskFromSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), name="", profile=[ vim.vm.ProfileSpec() ] or None, crypto=vim.encryption.CryptoSpec() or None, path="" or None): # vim.vslm.host.VStorageObjectManager.createDiskFromSnapshot
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def RevertVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()): # vim.vslm.host.VStorageObjectManager.RevertVStorageObject
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def updateVStorageObjectMetadata(id=vim.vslm.ID(), datastore=vim.Datastore(), metadata=[ vim.KeyValue() ] or None, deleteKeys=[ "" ] or None): # vim.vslm.host.VStorageObjectManager.updateVStorageObjectMetadata
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def retrieveVStorageObjectMetadata(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID() or None, prefix="" or None): # vim.vslm.host.VStorageObjectManager.retrieveVStorageObjectMetadata
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return [ vim.KeyValue() ]

            def retrieveVStorageObjectMetadataValue(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID() or None, key=""): # vim.vslm.host.VStorageObjectManager.retrieveVStorageObjectMetadataValue
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.KeyNotFound
               return ""

   class AuthorizationManager(vmodl.ManagedObject): # vim.AuthorizationManager
      privilegeList = [ vim.AuthorizationManager.Privilege() ]
      roleList = [ vim.AuthorizationManager.Role() ]
      description = vim.AuthorizationDescription()

      def addRole(name="", privIds=[ "" ] or None): # vim.AuthorizationManager.addRole
         # throws vim.fault.AlreadyExists, vim.fault.InvalidName
         return 0

      def removeRole(roleId=0, failIfUsed=False): # vim.AuthorizationManager.removeRole
         # throws vim.fault.NotFound, vim.fault.RemoveFailed
         return None

      def updateRole(roleId=0, newName="", privIds=[ "" ] or None): # vim.AuthorizationManager.updateRole
         # throws vim.fault.NotFound, vim.fault.InvalidName, vim.fault.AlreadyExists
         return None

      def mergePermissions(srcRoleId=0, dstRoleId=0): # vim.AuthorizationManager.mergePermissions
         # throws vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def retrieveRolePermissions(roleId=0): # vim.AuthorizationManager.retrieveRolePermissions
         # throws vim.fault.NotFound
         return [ vim.AuthorizationManager.Permission() ]

      def retrieveEntityPermissions(entity=vim.ManagedEntity(), inherited=False): # vim.AuthorizationManager.retrieveEntityPermissions
         return [ vim.AuthorizationManager.Permission() ]

      def retrieveAllPermissions(): # vim.AuthorizationManager.retrieveAllPermissions
         return [ vim.AuthorizationManager.Permission() ]

      def setEntityPermissions(entity=vim.ManagedEntity(), permission=[ vim.AuthorizationManager.Permission() ] or None): # vim.AuthorizationManager.setEntityPermissions
         # throws vim.fault.UserNotFound, vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def resetEntityPermissions(entity=vim.ManagedEntity(), permission=[ vim.AuthorizationManager.Permission() ] or None): # vim.AuthorizationManager.resetEntityPermissions
         # throws vim.fault.UserNotFound, vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def removeEntityPermission(entity=vim.ManagedEntity(), user="", isGroup=False): # vim.AuthorizationManager.removeEntityPermission
         # throws vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def hasPrivilegeOnEntity(entity=vim.ManagedEntity(), sessionId="", privId=[ "" ] or None): # vim.AuthorizationManager.hasPrivilegeOnEntity
         return [ False ]

      def hasPrivilegeOnEntities(entity=[ vim.ManagedEntity() ], sessionId="", privId=[ "" ] or None): # vim.AuthorizationManager.hasPrivilegeOnEntities
         return [ vim.AuthorizationManager.EntityPrivilege() ]

      def hasUserPrivilegeOnEntities(entities=[ vmodl.ManagedObject() ], userName="", privId=[ "" ] or None): # vim.AuthorizationManager.hasUserPrivilegeOnEntities
         return [ vim.AuthorizationManager.EntityPrivilege() ]

      def fetchUserPrivilegeOnEntities(entities=[ vim.ManagedEntity() ], userName=""): # vim.AuthorizationManager.fetchUserPrivilegeOnEntities
         return [ vim.AuthorizationManager.UserPrivilegeResult() ]

      class Permission(vmodl.DynamicData): # vim.AuthorizationManager.Permission
         entity = vim.ManagedEntity()
         principal = ""
         group = False
         roleId = 0
         propagate = False

      class Role(vmodl.DynamicData): # vim.AuthorizationManager.Role
         roleId = 0
         system = False
         name = ""
         info = vim.Description()
         privilege = [ "" ]

      class Privilege(vmodl.DynamicData): # vim.AuthorizationManager.Privilege
         privId = ""
         onParent = False
         name = ""
         privGroupName = ""

      class PrivilegeAvailability(vmodl.DynamicData): # vim.AuthorizationManager.PrivilegeAvailability
         privId = ""
         isGranted = False

      class EntityPrivilege(vmodl.DynamicData): # vim.AuthorizationManager.EntityPrivilege
         entity = vim.ManagedEntity()
         privAvailability = [ vim.AuthorizationManager.PrivilegeAvailability() ]

      class UserPrivilegeResult(vmodl.DynamicData): # vim.AuthorizationManager.UserPrivilegeResult
         entity = vim.ManagedEntity()
         privileges = [ "" ]

   class BoolPolicy(vim.InheritablePolicy): # vim.BoolPolicy
      value = False

   class EVCMode(vim.ElementDescription): # vim.EVCMode
      guaranteedCPUFeatures = [ vim.host.CpuIdInfo() ]
      featureCapability = [ vim.host.FeatureCapability() ]
      featureMask = [ vim.host.FeatureMask() ]
      featureRequirement = [ vim.vm.FeatureRequirement() ]
      vendor = ""
      track = [ "" ]
      vendorTier = 0

   class ImportSpec(vmodl.DynamicData): # vim.ImportSpec
      entityConfig = vim.vApp.EntityConfigInfo()
      instantiationOst = vim.OvfConsumer.OstNode()

   class IntExpression(vim.NegatableExpression): # vim.IntExpression
      value = 0

   class IpAddress(vim.NegatableExpression): # vim.IpAddress
      pass

   class IpRange(vim.IpAddress): # vim.IpRange
      addressPrefix = ""
      prefixLength = 0

   class LicenseAssignmentManager(vmodl.ManagedObject): # vim.LicenseAssignmentManager

      def updateAssignedLicense(entity="", licenseKey="", entityDisplayName="" or None): # vim.LicenseAssignmentManager.updateAssignedLicense
         # throws vim.fault.LicenseEntityNotFound
         return vim.LicenseManager.LicenseInfo()

      def removeAssignedLicense(entityId=""): # vim.LicenseAssignmentManager.removeAssignedLicense
         # throws vim.fault.LicenseEntityNotFound
         return None

      def queryAssignedLicenses(entityId="" or None): # vim.LicenseAssignmentManager.queryAssignedLicenses
         return [ vim.LicenseAssignmentManager.LicenseAssignment() ]

      class LicenseAssignment(vmodl.DynamicData): # vim.LicenseAssignmentManager.LicenseAssignment
         entityId = ""
         scope = ""
         entityDisplayName = ""
         assignedLicense = vim.LicenseManager.LicenseInfo()
         properties = [ vmodl.KeyAnyValue() ]

   class MacAddress(vim.NegatableExpression): # vim.MacAddress
      pass

   class MacRange(vim.MacAddress): # vim.MacRange
      address = ""
      mask = ""

   class ManagedEntity(vim.ExtensibleManagedObject): # vim.ManagedEntity
      parent = vim.ManagedEntity()
      customValue = [ vim.CustomFieldsManager.Value() ]
      overallStatus = vim.ManagedEntity.Status()
      configStatus = vim.ManagedEntity.Status()
      configIssue = [ vim.event.Event() ]
      effectiveRole = [ 0 ]
      permission = [ vim.AuthorizationManager.Permission() ]
      name = ""
      disabledMethod = [ vmodl.MethodName() ]
      recentTask = [ vim.Task() ]
      declaredAlarmState = [ vim.alarm.AlarmState() ]
      triggeredAlarmState = [ vim.alarm.AlarmState() ]
      alarmActionsEnabled = False
      tag = [ vim.Tag() ]

      def reload(): # vim.ManagedEntity.reload
         return None

      def rename(newName=""): # vim.ManagedEntity.rename
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def destroy(): # vim.ManagedEntity.destroy
         # throws vim.fault.VimFault
         return vim.Task()

      class Status(Enum): # vim.ManagedEntity.Status
         gray = 0
         green = 1
         yellow = 2
         red = 3

   class Network(vim.ManagedEntity): # vim.Network
      summary = vim.Network.Summary()
      host = [ vim.HostSystem() ]
      vm = [ vim.VirtualMachine() ]

      def destroyNetwork(): # vim.Network.destroyNetwork
         # throws vim.fault.ResourceInUse
         return None

      class Summary(vmodl.DynamicData): # vim.Network.Summary
         network = vim.Network()
         name = ""
         accessible = False
         ipPoolName = ""
         ipPoolId = 0

   class OpaqueNetwork(vim.Network): # vim.OpaqueNetwork
      capability = vim.OpaqueNetwork.Capability()
      extraConfig = [ vim.option.OptionValue() ]

      class Summary(vim.Network.Summary): # vim.OpaqueNetwork.Summary
         opaqueNetworkId = ""
         opaqueNetworkType = ""

      class Capability(vmodl.DynamicData): # vim.OpaqueNetwork.Capability
         networkReservationSupported = False

   class PosixUserSearchResult(vim.UserSearchResult): # vim.PosixUserSearchResult
      id = 0
      shellAccess = False

   class ResourcePool(vim.ManagedEntity): # vim.ResourcePool
      summary = vim.ResourcePool.Summary()
      runtime = vim.ResourcePool.RuntimeInfo()
      owner = vim.ComputeResource()
      resourcePool = [ vim.ResourcePool() ]
      vm = [ vim.VirtualMachine() ]
      config = vim.ResourceConfigSpec()
      namespace = ""
      childConfiguration = [ vim.ResourceConfigSpec() ]

      def updateConfig(name="" or None, config=vim.ResourceConfigSpec() or None): # vim.ResourcePool.updateConfig
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault, vim.fault.ConcurrentAccess
         return None

      def moveInto(list=[ vim.ManagedEntity() ]): # vim.ResourcePool.moveInto
         # throws vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault
         return None

      def updateChildResourceConfiguration(spec=[ vim.ResourceConfigSpec() ]): # vim.ResourcePool.updateChildResourceConfiguration
         # throws vim.fault.InvalidState, vim.fault.InsufficientResourcesFault
         return None

      def createResourcePool(name="", spec=vim.ResourceConfigSpec()): # vim.ResourcePool.createResourcePool
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault
         return vim.ResourcePool()

      def destroyChildren(): # vim.ResourcePool.destroyChildren
         return None

      def createVApp(name="", resSpec=vim.ResourceConfigSpec(), configSpec=vim.vApp.VAppConfigSpec(), vmFolder=vim.Folder() or None): # vim.ResourcePool.createVApp
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.VirtualApp()

      def createVm(config=vim.vm.ConfigSpec(), host=vim.HostSystem() or None): # vim.ResourcePool.createVm
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def registerVm(path="", name="" or None, host=vim.HostSystem() or None): # vim.ResourcePool.registerVm
         # throws vim.fault.OutOfBounds, vim.fault.AlreadyExists, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.VmConfigFault, vim.fault.InsufficientResourcesFault, vim.fault.FileFault
         return vim.Task()

      def importVApp(spec=vim.ImportSpec(), folder=vim.Folder() or None, host=vim.HostSystem() or None): # vim.ResourcePool.importVApp
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault
         return vim.HttpNfcLease()

      def queryResourceConfigOption(): # vim.ResourcePool.queryResourceConfigOption
         return vim.ResourceConfigOption()

      def refreshRuntime(): # vim.ResourcePool.refreshRuntime
         return None

      class ResourceUsage(vmodl.DynamicData): # vim.ResourcePool.ResourceUsage
         reservationUsed = 0
         reservationUsedForVm = 0
         unreservedForPool = 0
         unreservedForVm = 0
         overallUsage = 0
         maxUsage = 0

      class RuntimeInfo(vmodl.DynamicData): # vim.ResourcePool.RuntimeInfo
         memory = vim.ResourcePool.ResourceUsage()
         cpu = vim.ResourcePool.ResourceUsage()
         overallStatus = vim.ManagedEntity.Status()
         sharesScalable = ""

      class Summary(vmodl.DynamicData): # vim.ResourcePool.Summary
         name = ""
         config = vim.ResourceConfigSpec()
         runtime = vim.ResourcePool.RuntimeInfo()
         quickStats = vim.ResourcePool.Summary.QuickStats()
         configuredMemoryMB = 0

         class QuickStats(vmodl.DynamicData): # vim.ResourcePool.Summary.QuickStats
            overallCpuUsage = 0
            overallCpuDemand = 0
            guestMemoryUsage = 0
            hostMemoryUsage = 0
            distributedCpuEntitlement = 0
            distributedMemoryEntitlement = 0
            staticCpuEntitlement = 0
            staticMemoryEntitlement = 0
            privateMemory = 0
            sharedMemory = 0
            swappedMemory = 0
            balloonedMemory = 0
            overheadMemory = 0
            consumedOverheadMemory = 0
            compressedMemory = 0

   class SingleIp(vim.IpAddress): # vim.SingleIp
      address = ""

   class SingleMac(vim.MacAddress): # vim.SingleMac
      address = ""

   class Task(vim.ExtensibleManagedObject): # vim.Task
      info = vim.TaskInfo()

      def cancel(): # vim.Task.cancel
         # throws vim.fault.InvalidState
         return None

      def UpdateProgress(percentDone=0): # vim.Task.UpdateProgress
         # throws vim.fault.InvalidState, vim.fault.OutOfBounds
         return None

      def setState(state=vim.TaskInfo.State(), result={} or None, fault=vmodl.MethodFault() or None): # vim.Task.setState
         # throws vim.fault.InvalidState
         return None

      def UpdateDescription(description=vmodl.LocalizableMessage()): # vim.Task.UpdateDescription
         return None

   class TaskFilterSpec(vmodl.DynamicData): # vim.TaskFilterSpec
      entity = vim.TaskFilterSpec.ByEntity()
      time = vim.TaskFilterSpec.ByTime()
      userName = vim.TaskFilterSpec.ByUsername()
      activationId = [ "" ]
      state = [ vim.TaskInfo.State() ]
      alarm = vim.alarm.Alarm()
      scheduledTask = vim.scheduler.ScheduledTask()
      eventChainId = [ 0 ]
      tag = [ "" ]
      parentTaskKey = [ "" ]
      rootTaskKey = [ "" ]

      class RecursionOption(Enum): # vim.TaskFilterSpec.RecursionOption
         self = 0
         children = 1
         all = 2

      class TimeOption(Enum): # vim.TaskFilterSpec.TimeOption
         queuedTime = 0
         startedTime = 1
         completedTime = 2

      class ByEntity(vmodl.DynamicData): # vim.TaskFilterSpec.ByEntity
         entity = vim.ManagedEntity()
         recursion = vim.TaskFilterSpec.RecursionOption()

      class ByTime(vmodl.DynamicData): # vim.TaskFilterSpec.ByTime
         timeType = vim.TaskFilterSpec.TimeOption()
         beginTime = vmodl.DateTime()
         endTime = vmodl.DateTime()

      class ByUsername(vmodl.DynamicData): # vim.TaskFilterSpec.ByUsername
         systemUser = False
         userList = [ "" ]

   class VirtualApp(vim.ResourcePool): # vim.VirtualApp
      parentFolder = vim.Folder()
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      vAppConfig = vim.vApp.VAppConfigInfo()
      parentVApp = vim.ManagedEntity()
      childLink = [ vim.VirtualApp.LinkInfo() ]

      def updateVAppConfig(spec=vim.vApp.VAppConfigSpec()): # vim.VirtualApp.updateVAppConfig
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.InvalidDatastore
         return None

      def updateLinkedChildren(addChangeSet=[ vim.VirtualApp.LinkInfo() ] or None, removeSet=[ vim.ManagedEntity() ] or None): # vim.VirtualApp.updateLinkedChildren
         # throws vim.fault.ConcurrentAccess
         return None

      def clone(name="", target=vim.ResourcePool(), spec=vim.vApp.CloneSpec()): # vim.VirtualApp.clone
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.MigrationFault, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def exportVApp(): # vim.VirtualApp.exportVApp
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
         return vim.HttpNfcLease()

      def powerOn(): # vim.VirtualApp.powerOn
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmConfigFault, vim.fault.VAppConfigFault, vim.fault.FileFault
         return vim.Task()

      def powerOff(force=False): # vim.VirtualApp.powerOff
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.VAppConfigFault
         return vim.Task()

      def suspend(): # vim.VirtualApp.suspend
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.VAppConfigFault
         return vim.Task()

      def unregister(): # vim.VirtualApp.unregister
         # throws vim.fault.ConcurrentAccess, vim.fault.InvalidState
         return vim.Task()

      class VAppState(Enum): # vim.VirtualApp.VAppState
         started = 0
         stopped = 1
         starting = 2
         stopping = 3

      class Summary(vim.ResourcePool.Summary): # vim.VirtualApp.Summary
         product = vim.vApp.ProductInfo()
         vAppState = vim.VirtualApp.VAppState()
         suspended = False
         installBootRequired = False
         instanceUuid = ""

      class LinkInfo(vmodl.DynamicData): # vim.VirtualApp.LinkInfo
         key = vim.ManagedEntity()
         destroyWithParent = False

   class VirtualDiskManager(vmodl.ManagedObject): # vim.VirtualDiskManager

      def createVirtualDisk(name="", datacenter=vim.Datacenter() or None, spec=vim.VirtualDiskManager.VirtualDiskSpec()): # vim.VirtualDiskManager.createVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def deleteVirtualDisk(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.deleteVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def moveVirtualDisk(sourceName="", sourceDatacenter=vim.Datacenter() or None, destName="", destDatacenter=vim.Datacenter() or None, force=False or None, profile=[ vim.vm.ProfileSpec() ] or None): # vim.VirtualDiskManager.moveVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def copyVirtualDisk(sourceName="", sourceDatacenter=vim.Datacenter() or None, destName="", destDatacenter=vim.Datacenter() or None, destSpec=vim.VirtualDiskManager.VirtualDiskSpec() or None, force=False or None): # vim.VirtualDiskManager.copyVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDiskFormat, vim.fault.InvalidDatastore
         return vim.Task()

      def extendVirtualDisk(name="", datacenter=vim.Datacenter() or None, newCapacityKb=0, eagerZero=False or None): # vim.VirtualDiskManager.extendVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def queryVirtualDiskFragmentation(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.queryVirtualDiskFragmentation
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return 0

      def defragmentVirtualDisk(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.defragmentVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def shrinkVirtualDisk(name="", datacenter=vim.Datacenter() or None, copy=False or None): # vim.VirtualDiskManager.shrinkVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def inflateVirtualDisk(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.inflateVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def eagerZeroVirtualDisk(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.eagerZeroVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def zeroFillVirtualDisk(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.zeroFillVirtualDisk
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def setVirtualDiskUuid(name="", datacenter=vim.Datacenter() or None, uuid=""): # vim.VirtualDiskManager.setVirtualDiskUuid
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return None

      def queryVirtualDiskUuid(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.queryVirtualDiskUuid
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return ""

      def queryVirtualDiskGeometry(name="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.queryVirtualDiskGeometry
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.host.DiskDimensions.Chs()

      def importUnmanagedSnapshot(vdisk="", datacenter=vim.Datacenter() or None, vvolId=""): # vim.VirtualDiskManager.importUnmanagedSnapshot
         # throws vim.fault.NotFound, vim.fault.InvalidDatastore
         return None

      def releaseManagedSnapshot(vdisk="", datacenter=vim.Datacenter() or None): # vim.VirtualDiskManager.releaseManagedSnapshot
         # throws vim.fault.InvalidDatastore, vim.fault.FileNotFound
         return None

      class VirtualDiskType(Enum): # vim.VirtualDiskManager.VirtualDiskType
         preallocated = 0
         thin = 1
         seSparse = 2
         rdm = 3
         rdmp = 4
         raw = 5
         delta = 6
         sparse2Gb = 7
         thick2Gb = 8
         eagerZeroedThick = 9
         sparseMonolithic = 10
         flatMonolithic = 11
         thick = 12

      class VirtualDiskAdapterType(Enum): # vim.VirtualDiskManager.VirtualDiskAdapterType
         ide = 0
         busLogic = 1
         lsiLogic = 2

      class VirtualDiskSpec(vmodl.DynamicData): # vim.VirtualDiskManager.VirtualDiskSpec
         diskType = ""
         adapterType = ""

      class FileBackedVirtualDiskSpec(vim.VirtualDiskManager.VirtualDiskSpec): # vim.VirtualDiskManager.FileBackedVirtualDiskSpec
         capacityKb = 0
         profile = [ vim.vm.ProfileSpec() ]
         crypto = vim.encryption.CryptoSpec()

      class SeSparseVirtualDiskSpec(vim.VirtualDiskManager.FileBackedVirtualDiskSpec): # vim.VirtualDiskManager.SeSparseVirtualDiskSpec
         grainSizeKb = 0

      class DeviceBackedVirtualDiskSpec(vim.VirtualDiskManager.VirtualDiskSpec): # vim.VirtualDiskManager.DeviceBackedVirtualDiskSpec
         device = ""

   class VirtualMachine(vim.ManagedEntity): # vim.VirtualMachine
      capability = vim.vm.Capability()
      config = vim.vm.ConfigInfo()
      layout = vim.vm.FileLayout()
      layoutEx = vim.vm.FileLayoutEx()
      storage = vim.vm.StorageInfo()
      environmentBrowser = vim.EnvironmentBrowser()
      resourcePool = vim.ResourcePool()
      parentVApp = vim.ManagedEntity()
      resourceConfig = vim.ResourceConfigSpec()
      runtime = vim.vm.RuntimeInfo()
      guest = vim.vm.GuestInfo()
      summary = vim.vm.Summary()
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      snapshot = vim.vm.SnapshotInfo()
      rootSnapshot = [ vim.vm.Snapshot() ]
      guestHeartbeatStatus = vim.ManagedEntity.Status()

      def refreshStorageInfo(): # vim.VirtualMachine.refreshStorageInfo
         return None

      def createSnapshot(name="", description="" or None, memory=False, quiesce=False): # vim.VirtualMachine.createSnapshot
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.InvalidState
         return vim.Task()

      def createSnapshotEx(name="", description="" or None, memory=False, quiesceSpec=vim.vm.GuestQuiesceSpec() or None): # vim.VirtualMachine.createSnapshotEx
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.InvalidState
         return vim.Task()

      def revertToCurrentSnapshot(host=vim.HostSystem() or None, suppressPowerOn=False or None): # vim.VirtualMachine.revertToCurrentSnapshot
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.NotFound
         return vim.Task()

      def removeAllSnapshots(consolidate=False or None): # vim.VirtualMachine.removeAllSnapshots
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.SnapshotFault
         return vim.Task()

      def consolidateDisks(): # vim.VirtualMachine.consolidateDisks
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def estimateStorageRequirementForConsolidate(): # vim.VirtualMachine.estimateStorageRequirementForConsolidate
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def reconfigure(spec=vim.vm.ConfigSpec()): # vim.VirtualMachine.reconfigure
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.InvalidDatastore
         return vim.Task()

      def upgradeVirtualHardware(version="" or None): # vim.VirtualMachine.upgradeVirtualHardware
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.AlreadyUpgraded, vim.fault.NoDiskFound
         return vim.Task()

      def extractOvfEnvironment(): # vim.VirtualMachine.extractOvfEnvironment
         # throws vim.fault.InvalidState
         return ""

      def powerOn(host=vim.HostSystem() or None): # vim.VirtualMachine.powerOn
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmConfigFault, vim.fault.FileFault
         return vim.Task()

      def powerOff(): # vim.VirtualMachine.powerOff
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def suspend(): # vim.VirtualMachine.suspend
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def reset(): # vim.VirtualMachine.reset
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def shutdownGuest(): # vim.VirtualMachine.shutdownGuest
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def rebootGuest(): # vim.VirtualMachine.rebootGuest
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def standbyGuest(): # vim.VirtualMachine.standbyGuest
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def answer(questionId="", answerChoice=""): # vim.VirtualMachine.answer
         # throws vim.fault.ConcurrentAccess
         return None

      def customize(spec=vim.vm.customization.Specification()): # vim.VirtualMachine.customize
         # throws vim.fault.CustomizationFault
         return vim.Task()

      def checkCustomizationSpec(spec=vim.vm.customization.Specification()): # vim.VirtualMachine.checkCustomizationSpec
         # throws vim.fault.CustomizationFault
         return None

      def migrate(pool=vim.ResourcePool() or None, host=vim.HostSystem() or None, priority=vim.VirtualMachine.MovePriority(), state=vim.VirtualMachine.PowerState() or None): # vim.VirtualMachine.migrate
         # throws vim.fault.MigrationFault, vim.fault.FileFault, vim.fault.Timedout, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.Task()

      def relocate(spec=vim.vm.RelocateSpec(), priority=vim.VirtualMachine.MovePriority() or None): # vim.VirtualMachine.relocate
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.MigrationFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.Timedout, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def clone(folder=vim.Folder(), name="", spec=vim.vm.CloneSpec()): # vim.VirtualMachine.clone
         # throws vim.fault.CustomizationFault, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.MigrationFault, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def instantClone(spec=vim.vm.InstantCloneSpec()): # vim.VirtualMachine.instantClone
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault, vim.fault.DisallowedMigrationDeviceAttached, vim.fault.FileFault
         return vim.Task()

      def exportVm(): # vim.VirtualMachine.exportVm
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
         return vim.HttpNfcLease()

      def markAsTemplate(): # vim.VirtualMachine.markAsTemplate
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.FileFault
         return None

      def markAsVirtualMachine(pool=vim.ResourcePool(), host=vim.HostSystem() or None): # vim.VirtualMachine.markAsVirtualMachine
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.VmConfigFault, vim.fault.FileFault
         return None

      def unregister(): # vim.VirtualMachine.unregister
         # throws vim.fault.TaskInProgress, vim.fault.InvalidPowerState
         return None

      def resetGuestInformation(): # vim.VirtualMachine.resetGuestInformation
         # throws vim.fault.InvalidState
         return None

      def mountToolsInstaller(): # vim.VirtualMachine.mountToolsInstaller
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.VmToolsUpgradeFault
         return None

      def unmountToolsInstaller(): # vim.VirtualMachine.unmountToolsInstaller
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return None

      def upgradeTools(installerOptions="" or None): # vim.VirtualMachine.upgradeTools
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.VmToolsUpgradeFault, vim.fault.ToolsUnavailable, vim.fault.VmConfigFault
         return vim.Task()

      def acquireMksTicket(): # vim.VirtualMachine.acquireMksTicket
         return vim.VirtualMachine.MksTicket()

      def acquireTicket(ticketType=""): # vim.VirtualMachine.acquireTicket
         # throws vim.fault.InvalidState
         return vim.VirtualMachine.Ticket()

      def setScreenResolution(width=0, height=0): # vim.VirtualMachine.setScreenResolution
         # throws vim.fault.InvalidState, vim.fault.ToolsUnavailable
         return None

      def defragmentAllDisks(): # vim.VirtualMachine.defragmentAllDisks
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault
         return None

      def createSecondary(host=vim.HostSystem() or None): # vim.VirtualMachine.createSecondary
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmFaultToleranceIssue, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def createSecondaryEx(host=vim.HostSystem() or None, spec=vim.vm.FaultToleranceConfigSpec() or None): # vim.VirtualMachine.createSecondaryEx
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmFaultToleranceIssue, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def turnOffFaultTolerance(): # vim.VirtualMachine.turnOffFaultTolerance
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def makePrimary(vm=vim.VirtualMachine()): # vim.VirtualMachine.makePrimary
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def terminateFaultTolerantVM(vm=vim.VirtualMachine() or None): # vim.VirtualMachine.terminateFaultTolerantVM
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def disableSecondary(vm=vim.VirtualMachine()): # vim.VirtualMachine.disableSecondary
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def enableSecondary(vm=vim.VirtualMachine(), host=vim.HostSystem() or None): # vim.VirtualMachine.enableSecondary
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.Task()

      def setDisplayTopology(displays=[ vim.VirtualMachine.DisplayTopology() ]): # vim.VirtualMachine.setDisplayTopology
         # throws vim.fault.InvalidState, vim.fault.ToolsUnavailable
         return None

      def startRecording(name="", description="" or None): # vim.VirtualMachine.startRecording
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.RecordReplayDisabled, vim.fault.HostIncompatibleForRecordReplay, vim.fault.InvalidName
         return vim.Task()

      def stopRecording(): # vim.VirtualMachine.stopRecording
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault
         return vim.Task()

      def startReplaying(replaySnapshot=vim.vm.Snapshot()): # vim.VirtualMachine.startReplaying
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault, vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.RecordReplayDisabled, vim.fault.HostIncompatibleForRecordReplay
         return vim.Task()

      def stopReplaying(): # vim.VirtualMachine.stopReplaying
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault
         return vim.Task()

      def promoteDisks(unlink=False, disks=[ vim.vm.device.VirtualDisk() ] or None): # vim.VirtualMachine.promoteDisks
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress
         return vim.Task()

      def createScreenshot(): # vim.VirtualMachine.createScreenshot
         # throws vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def putUsbScanCodes(spec=vim.vm.UsbScanCodeSpec()): # vim.VirtualMachine.putUsbScanCodes
         return 0

      def queryChangedDiskAreas(snapshot=vim.vm.Snapshot() or None, deviceKey=0, startOffset=0, changeId=""): # vim.VirtualMachine.queryChangedDiskAreas
         # throws vim.fault.FileFault, vim.fault.NotFound
         return vim.VirtualMachine.DiskChangeInfo()

      def queryUnownedFiles(): # vim.VirtualMachine.queryUnownedFiles
         return [ "" ]

      def reloadFromPath(configurationPath=""): # vim.VirtualMachine.reloadFromPath
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.AlreadyExists
         return vim.Task()

      def queryFaultToleranceCompatibility(): # vim.VirtualMachine.queryFaultToleranceCompatibility
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return [ vmodl.MethodFault() ]

      def queryFaultToleranceCompatibilityEx(forLegacyFt=False or None): # vim.VirtualMachine.queryFaultToleranceCompatibilityEx
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return [ vmodl.MethodFault() ]

      def terminate(): # vim.VirtualMachine.terminate
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress
         return None

      def sendNMI(): # vim.VirtualMachine.sendNMI
         # throws vim.fault.InvalidState
         return None

      def attachDisk(diskId=vim.vslm.ID(), datastore=vim.Datastore(), controllerKey=0 or None, unitNumber=0 or None): # vim.VirtualMachine.attachDisk
         # throws vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.InvalidController, vim.fault.MissingController, vim.fault.DeviceUnsupportedForVmVersion
         return vim.Task()

      def detachDisk(diskId=vim.vslm.ID()): # vim.VirtualMachine.detachDisk
         # throws vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def applyEvcMode(mask=[ vim.host.FeatureMask() ] or None, completeMasks=False or None): # vim.VirtualMachine.applyEvcMode
         # throws vim.fault.InvalidState
         return vim.Task()

      def cryptoUnlock(): # vim.VirtualMachine.cryptoUnlock
         # throws vim.fault.InvalidState, vmodl.fault.NotSupported
         return vim.Task()

      class StorageRequirement(vmodl.DynamicData): # vim.VirtualMachine.StorageRequirement
         datastore = vim.Datastore()
         freeSpaceRequiredInKb = 0

      class PowerState(Enum): # vim.VirtualMachine.PowerState
         poweredOff = 0
         poweredOn = 1
         suspended = 2

      class AppHeartbeatStatusType(Enum): # vim.VirtualMachine.AppHeartbeatStatusType
         appStatusGray = 0
         appStatusGreen = 1
         appStatusRed = 2

      class ConnectionState(Enum): # vim.VirtualMachine.ConnectionState
         connected = 0
         disconnected = 1
         orphaned = 2
         inaccessible = 3
         invalid = 4

      class CryptoState(Enum): # vim.VirtualMachine.CryptoState
         unlocked = 0
         locked = 1

      class MovePriority(Enum): # vim.VirtualMachine.MovePriority
         lowPriority = 0
         highPriority = 1
         defaultPriority = 2

      class Ticket(vmodl.DynamicData): # vim.VirtualMachine.Ticket
         ticket = ""
         cfgFile = ""
         host = ""
         port = 0
         sslThumbprint = ""
         url = ""

      class MksTicket(vmodl.DynamicData): # vim.VirtualMachine.MksTicket
         ticket = ""
         cfgFile = ""
         host = ""
         port = 0
         sslThumbprint = ""

      class FaultToleranceState(Enum): # vim.VirtualMachine.FaultToleranceState
         notConfigured = 0
         disabled = 1
         enabled = 2
         needSecondary = 3
         starting = 4
         running = 5

      class RecordReplayState(Enum): # vim.VirtualMachine.RecordReplayState
         recording = 0
         replaying = 1
         inactive = 2

      class NeedSecondaryReason(Enum): # vim.VirtualMachine.NeedSecondaryReason
         initializing = 0
         divergence = 1
         lostConnection = 2
         partialHardwareFailure = 3
         userAction = 4
         checkpointError = 5
         other = 6

      class FaultToleranceType(Enum): # vim.VirtualMachine.FaultToleranceType
         unset = 0
         recordReplay = 1
         checkpointing = 2

      class TicketType(Enum): # vim.VirtualMachine.TicketType
         mks = 0
         device = 1
         guestControl = 2
         dnd = 3
         webmks = 4
         guestIntegrity = 5
         webRemoteDevice = 6

      class DisplayTopology(vmodl.DynamicData): # vim.VirtualMachine.DisplayTopology
         x = 0
         y = 0
         width = 0
         height = 0

      class DiskChangeInfo(vmodl.DynamicData): # vim.VirtualMachine.DiskChangeInfo
         startOffset = 0
         length = 0
         changedArea = [ vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent() ]

         class DiskChangeExtent(vmodl.DynamicData): # vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent
            start = 0
            length = 0

      class WipeResult(vmodl.DynamicData): # vim.VirtualMachine.WipeResult
         diskId = 0
         shrinkableDiskSpace = 0

   class ComputeResource(vim.ManagedEntity): # vim.ComputeResource
      resourcePool = vim.ResourcePool()
      host = [ vim.HostSystem() ]
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      summary = vim.ComputeResource.Summary()
      environmentBrowser = vim.EnvironmentBrowser()
      configurationEx = vim.ComputeResource.ConfigInfo()
      lifecycleManaged = False

      def reconfigureEx(spec=vim.ComputeResource.ConfigSpec(), modify=False): # vim.ComputeResource.reconfigureEx
         return vim.Task()

      class Summary(vmodl.DynamicData): # vim.ComputeResource.Summary
         totalCpu = 0
         totalMemory = 0
         numCpuCores = 0
         numCpuThreads = 0
         effectiveCpu = 0
         effectiveMemory = 0
         numHosts = 0
         numEffectiveHosts = 0
         overallStatus = vim.ManagedEntity.Status()

      class ConfigInfo(vmodl.DynamicData): # vim.ComputeResource.ConfigInfo
         vmSwapPlacement = ""
         spbmEnabled = False
         defaultHardwareVersionKey = ""

      class HostSPBMLicenseInfo(vmodl.DynamicData): # vim.ComputeResource.HostSPBMLicenseInfo
         host = vim.HostSystem()
         licenseState = vim.ComputeResource.HostSPBMLicenseInfo.HostSPBMLicenseState()

         class HostSPBMLicenseState(Enum): # vim.ComputeResource.HostSPBMLicenseInfo.HostSPBMLicenseState
            licensed = 0
            unlicensed = 1
            unknown = 2

      class ConfigSpec(vmodl.DynamicData): # vim.ComputeResource.ConfigSpec
         vmSwapPlacement = ""
         spbmEnabled = False
         defaultHardwareVersionKey = ""
         desiredSoftwareSpec = vim.DesiredSoftwareSpec()

   class Datastore(vim.ManagedEntity): # vim.Datastore
      info = vim.Datastore.Info()
      summary = vim.Datastore.Summary()
      host = [ vim.Datastore.HostMount() ]
      vm = [ vim.VirtualMachine() ]
      browser = vim.host.DatastoreBrowser()
      capability = vim.Datastore.Capability()
      iormConfiguration = vim.StorageResourceManager.IORMConfigInfo()

      def refresh(): # vim.Datastore.refresh
         # throws vim.fault.NotFound, vim.fault.HostConfigFault
         return None

      def refreshStorageInfo(): # vim.Datastore.refreshStorageInfo
         return None

      def updateVirtualMachineFiles(mountPathDatastoreMapping=[ vim.Datastore.MountPathDatastorePair() ]): # vim.Datastore.updateVirtualMachineFiles
         # throws vim.fault.ResourceInUse, vim.fault.PlatformConfigFault, vim.fault.TaskInProgress, vim.fault.InvalidDatastore
         return vim.Task()

      def renameDatastore(newName=""): # vim.Datastore.renameDatastore
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return None

      def destroyDatastore(): # vim.Datastore.destroyDatastore
         # throws vim.fault.ResourceInUse
         return None

      def enterMaintenanceMode(): # vim.Datastore.enterMaintenanceMode
         # throws vim.fault.InvalidState
         return vim.storageDrs.StoragePlacementResult()

      def exitMaintenanceMode(): # vim.Datastore.exitMaintenanceMode
         # throws vim.fault.InvalidState
         return vim.Task()

      def updateVVolVirtualMachineFiles(failoverPair=[ vim.Datastore.VVolContainerFailoverPair() ] or None): # vim.Datastore.updateVVolVirtualMachineFiles
         # throws vmodl.fault.NotSupported, vim.fault.PlatformConfigFault, vim.fault.TaskInProgress, vim.fault.InvalidDatastore
         return vim.Task()

      class Accessible(Enum): # vim.Datastore.Accessible
         True = 0
         False = 1

      class Summary(vmodl.DynamicData): # vim.Datastore.Summary
         datastore = vim.Datastore()
         name = ""
         url = ""
         capacity = 0
         freeSpace = 0
         uncommitted = 0
         accessible = False
         multipleHostAccess = False
         type = ""
         maintenanceMode = ""

         class MaintenanceModeState(Enum): # vim.Datastore.Summary.MaintenanceModeState
            normal = 0
            enteringMaintenance = 1
            inMaintenance = 2

      class Info(vmodl.DynamicData): # vim.Datastore.Info
         name = ""
         url = ""
         freeSpace = 0
         maxFileSize = 0
         maxVirtualDiskCapacity = 0
         maxMemoryFileSize = 0
         timestamp = vmodl.DateTime()
         containerId = ""
         aliasOf = ""

      class Capability(vmodl.DynamicData): # vim.Datastore.Capability
         directoryHierarchySupported = False
         rawDiskMappingsSupported = False
         perFileThinProvisioningSupported = False
         storageIORMSupported = False
         nativeSnapshotSupported = False
         topLevelDirectoryCreateSupported = False
         seSparseSupported = False
         vmfsSparseSupported = False
         vsanSparseSupported = False
         upitSupported = False
         vmdkExpandSupported = False
         clusteredVmdkSupported = False

      class HostMount(vmodl.DynamicData): # vim.Datastore.HostMount
         key = vim.HostSystem()
         mountInfo = vim.host.MountInfo()

      class MountPathDatastorePair(vmodl.DynamicData): # vim.Datastore.MountPathDatastorePair
         oldMountPath = ""
         datastore = vim.Datastore()

      class VVolContainerFailoverPair(vmodl.DynamicData): # vim.Datastore.VVolContainerFailoverPair
         srcContainer = ""
         tgtContainer = ""
         vvolMapping = [ vim.KeyValue() ]

   class DistributedVirtualSwitch(vim.ManagedEntity): # vim.DistributedVirtualSwitch
      uuid = ""
      capability = vim.DistributedVirtualSwitch.Capability()
      summary = vim.DistributedVirtualSwitch.Summary()
      config = vim.DistributedVirtualSwitch.ConfigInfo()
      networkResourcePool = [ vim.dvs.NetworkResourcePool() ]
      portgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
      runtime = vim.DistributedVirtualSwitch.RuntimeInfo()

      def fetchPortKeys(criteria=vim.dvs.PortCriteria() or None): # vim.DistributedVirtualSwitch.fetchPortKeys
         return [ "" ]

      def fetchPorts(criteria=vim.dvs.PortCriteria() or None): # vim.DistributedVirtualSwitch.fetchPorts
         return [ vim.dvs.DistributedVirtualPort() ]

      def queryUsedVlanId(): # vim.DistributedVirtualSwitch.queryUsedVlanId
         return [ 0 ]

      def reconfigure(spec=vim.DistributedVirtualSwitch.ConfigSpec()): # vim.DistributedVirtualSwitch.reconfigure
         # throws vim.fault.DvsFault, vim.fault.ConcurrentAccess, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.NotFound, vim.fault.AlreadyExists, vim.fault.LimitExceeded, vim.fault.ResourceInUse, vim.fault.ResourceNotAvailable, vim.fault.DvsNotAuthorized
         return vim.Task()

      def performProductSpecOperation(operation="", productSpec=vim.dvs.ProductSpec() or None): # vim.DistributedVirtualSwitch.performProductSpecOperation
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.DvsFault
         return vim.Task()

      def merge(dvs=vim.DistributedVirtualSwitch()): # vim.DistributedVirtualSwitch.merge
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.InvalidHostState
         return vim.Task()

      def addPortgroups(spec=[ vim.dvs.DistributedVirtualPortgroup.ConfigSpec() ]): # vim.DistributedVirtualSwitch.addPortgroups
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def movePort(portKey=[ "" ], destinationPortgroupKey="" or None): # vim.DistributedVirtualSwitch.movePort
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ConcurrentAccess
         return vim.Task()

      def updateCapability(capability=vim.DistributedVirtualSwitch.Capability()): # vim.DistributedVirtualSwitch.updateCapability
         # throws vim.fault.DvsFault
         return None

      def reconfigurePort(port=[ vim.dvs.DistributedVirtualPort.ConfigSpec() ]): # vim.DistributedVirtualSwitch.reconfigurePort
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.ConcurrentAccess
         return vim.Task()

      def refreshPortState(portKeys=[ "" ] or None): # vim.DistributedVirtualSwitch.refreshPortState
         # throws vim.fault.DvsFault, vim.fault.NotFound
         return None

      def rectifyHost(hosts=[ vim.HostSystem() ] or None): # vim.DistributedVirtualSwitch.rectifyHost
         # throws vim.fault.DvsFault, vim.fault.NotFound
         return vim.Task()

      def updateNetworkResourcePool(configSpec=[ vim.dvs.NetworkResourcePool.ConfigSpec() ]): # vim.DistributedVirtualSwitch.updateNetworkResourcePool
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ConcurrentAccess
         return None

      def addNetworkResourcePool(configSpec=[ vim.dvs.NetworkResourcePool.ConfigSpec() ]): # vim.DistributedVirtualSwitch.addNetworkResourcePool
         # throws vim.fault.DvsFault, vim.fault.InvalidName
         return None

      def removeNetworkResourcePool(key=[ "" ]): # vim.DistributedVirtualSwitch.removeNetworkResourcePool
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ResourceInUse
         return None

      def reconfigureVmVnicNetworkResourcePool(configSpec=[ vim.dvs.VmVnicNetworkResourcePool.ConfigSpec() ]): # vim.DistributedVirtualSwitch.reconfigureVmVnicNetworkResourcePool
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ConcurrentAccess, vim.fault.ConflictingConfiguration, vim.fault.ResourceInUse
         return vim.Task()

      def enableNetworkResourceManagement(enable=False): # vim.DistributedVirtualSwitch.enableNetworkResourceManagement
         # throws vim.fault.DvsFault
         return None

      def rollback(entityBackup=vim.dvs.EntityBackup.Config() or None): # vim.DistributedVirtualSwitch.rollback
         # throws vim.fault.DvsFault, vim.fault.RollbackFailure
         return vim.Task()

      def addPortgroup(spec=vim.dvs.DistributedVirtualPortgroup.ConfigSpec()): # vim.DistributedVirtualSwitch.addPortgroup
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def updateHealthCheckConfig(healthCheckConfig=[ vim.DistributedVirtualSwitch.HealthCheckConfig() ]): # vim.DistributedVirtualSwitch.updateHealthCheckConfig
         # throws vim.fault.DvsFault
         return vim.Task()

      def lookupPortgroup(portgroupKey=""): # vim.DistributedVirtualSwitch.lookupPortgroup
         # throws vim.fault.NotFound
         return vim.dvs.DistributedVirtualPortgroup()

      class ProductSpecOperationType(Enum): # vim.DistributedVirtualSwitch.ProductSpecOperationType
         preInstall = 0
         upgrade = 1
         notifyAvailableUpgrade = 2
         proceedWithUpgrade = 3
         updateBundleInfo = 4

      class ContactInfo(vmodl.DynamicData): # vim.DistributedVirtualSwitch.ContactInfo
         name = ""
         contact = ""

      class NicTeamingPolicyMode(Enum): # vim.DistributedVirtualSwitch.NicTeamingPolicyMode
         loadbalance_ip = 0
         loadbalance_srcmac = 1
         loadbalance_srcid = 2
         failover_explicit = 3
         loadbalance_loadbased = 4

      class NetworkResourceManagementCapability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.NetworkResourceManagementCapability
         networkResourceManagementSupported = False
         networkResourcePoolHighShareValue = 0
         qosSupported = False
         userDefinedNetworkResourcePoolsSupported = False
         networkResourceControlVersion3Supported = False
         userDefinedInfraTrafficPoolSupported = False

      class RollbackCapability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.RollbackCapability
         rollbackSupported = False

      class BackupRestoreCapability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.BackupRestoreCapability
         backupRestoreSupported = False

      class FeatureCapability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.FeatureCapability
         networkResourceManagementSupported = False
         vmDirectPathGen2Supported = False
         nicTeamingPolicy = [ "" ]
         networkResourcePoolHighShareValue = 0
         networkResourceManagementCapability = vim.DistributedVirtualSwitch.NetworkResourceManagementCapability()
         healthCheckCapability = vim.DistributedVirtualSwitch.HealthCheckFeatureCapability()
         rollbackCapability = vim.DistributedVirtualSwitch.RollbackCapability()
         backupRestoreCapability = vim.DistributedVirtualSwitch.BackupRestoreCapability()
         networkFilterSupported = False
         macLearningSupported = False

      class HealthCheckFeatureCapability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.HealthCheckFeatureCapability
         pass

      class Capability(vmodl.DynamicData): # vim.DistributedVirtualSwitch.Capability
         dvsOperationSupported = False
         dvPortGroupOperationSupported = False
         dvPortOperationSupported = False
         compatibleHostComponentProductInfo = [ vim.dvs.HostProductSpec() ]
         featuresSupported = vim.DistributedVirtualSwitch.FeatureCapability()

      class Summary(vmodl.DynamicData): # vim.DistributedVirtualSwitch.Summary
         name = ""
         uuid = ""
         numPorts = 0
         productInfo = vim.dvs.ProductSpec()
         hostMember = [ vim.HostSystem() ]
         vm = [ vim.VirtualMachine() ]
         host = [ vim.HostSystem() ]
         portgroupName = [ "" ]
         description = ""
         contact = vim.DistributedVirtualSwitch.ContactInfo()
         numHosts = 0

      class SwitchPolicy(vmodl.DynamicData): # vim.DistributedVirtualSwitch.SwitchPolicy
         autoPreInstallAllowed = False
         autoUpgradeAllowed = False
         partialUpgradeAllowed = False

      class UplinkPortPolicy(vmodl.DynamicData): # vim.DistributedVirtualSwitch.UplinkPortPolicy
         pass

      class NameArrayUplinkPortPolicy(vim.DistributedVirtualSwitch.UplinkPortPolicy): # vim.DistributedVirtualSwitch.NameArrayUplinkPortPolicy
         uplinkPortName = [ "" ]

      class ConfigSpec(vmodl.DynamicData): # vim.DistributedVirtualSwitch.ConfigSpec
         configVersion = ""
         name = ""
         numStandalonePorts = 0
         maxPorts = 0
         uplinkPortPolicy = vim.DistributedVirtualSwitch.UplinkPortPolicy()
         uplinkPortgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
         defaultPortConfig = vim.dvs.DistributedVirtualPort.Setting()
         host = [ vim.dvs.HostMember.ConfigSpec() ]
         extensionKey = ""
         description = ""
         policy = vim.DistributedVirtualSwitch.SwitchPolicy()
         vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
         contact = vim.DistributedVirtualSwitch.ContactInfo()
         switchIpAddress = ""
         defaultProxySwitchMaxNumPorts = 0
         infrastructureTrafficResourceConfig = [ vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource() ]
         netResourcePoolTrafficResourceConfig = [ vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource() ]
         networkResourceControlVersion = ""

      class CreateSpec(vmodl.DynamicData): # vim.DistributedVirtualSwitch.CreateSpec
         configSpec = vim.DistributedVirtualSwitch.ConfigSpec()
         productInfo = vim.dvs.ProductSpec()
         capability = vim.DistributedVirtualSwitch.Capability()

      class ConfigInfo(vmodl.DynamicData): # vim.DistributedVirtualSwitch.ConfigInfo
         uuid = ""
         name = ""
         numStandalonePorts = 0
         numPorts = 0
         maxPorts = 0
         uplinkPortPolicy = vim.DistributedVirtualSwitch.UplinkPortPolicy()
         uplinkPortgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
         defaultPortConfig = vim.dvs.DistributedVirtualPort.Setting()
         host = [ vim.dvs.HostMember() ]
         productInfo = vim.dvs.ProductSpec()
         targetInfo = vim.dvs.ProductSpec()
         extensionKey = ""
         vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
         policy = vim.DistributedVirtualSwitch.SwitchPolicy()
         description = ""
         configVersion = ""
         contact = vim.DistributedVirtualSwitch.ContactInfo()
         switchIpAddress = ""
         createTime = vmodl.DateTime()
         networkResourceManagementEnabled = False
         defaultProxySwitchMaxNumPorts = 0
         healthCheckConfig = [ vim.DistributedVirtualSwitch.HealthCheckConfig() ]
         infrastructureTrafficResourceConfig = [ vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource() ]
         netResourcePoolTrafficResourceConfig = [ vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource() ]
         networkResourceControlVersion = ""
         vmVnicNetworkResourcePool = [ vim.dvs.VmVnicNetworkResourcePool() ]
         pnicCapacityRatioForReservation = 0

      class NetworkResourceControlVersion(Enum): # vim.DistributedVirtualSwitch.NetworkResourceControlVersion
         version2 = 0
         version3 = 1

      class HostInfrastructureTrafficClass(Enum): # vim.DistributedVirtualSwitch.HostInfrastructureTrafficClass
         management = 0
         faultTolerance = 1
         vmotion = 2
         virtualMachine = 3
         iSCSI = 4
         nfs = 5
         hbr = 6
         vsan = 7
         vdp = 8

      class HostInfrastructureTrafficResource(vmodl.DynamicData): # vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource
         key = ""
         description = ""
         allocationInfo = vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource.ResourceAllocation()

         class ResourceAllocation(vmodl.DynamicData): # vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource.ResourceAllocation
            limit = 0
            shares = vim.SharesInfo()
            reservation = 0

      class HealthCheckConfig(vmodl.DynamicData): # vim.DistributedVirtualSwitch.HealthCheckConfig
         enable = False
         interval = 0

      class ResourceRuntimeInfo(vmodl.DynamicData): # vim.DistributedVirtualSwitch.ResourceRuntimeInfo
         capacity = 0
         usage = 0
         available = 0
         allocatedResource = [ vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource() ]
         vmVnicNetworkResourcePoolRuntime = [ vim.dvs.VmVnicNetworkResourcePool.RuntimeInfo() ]

      class RuntimeInfo(vmodl.DynamicData): # vim.DistributedVirtualSwitch.RuntimeInfo
         hostMemberRuntime = [ vim.dvs.HostMember.RuntimeInfo() ]
         resourceRuntimeInfo = vim.DistributedVirtualSwitch.ResourceRuntimeInfo()

   class Folder(vim.ManagedEntity): # vim.Folder
      childType = [ vmodl.TypeName() ]
      childEntity = [ vim.ManagedEntity() ]
      namespace = ""

      def createFolder(name=""): # vim.Folder.createFolder
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Folder()

      def moveInto(list=[ vim.ManagedEntity() ]): # vim.Folder.moveInto
         # throws vim.fault.DuplicateName, vim.fault.InvalidFolder, vim.fault.InvalidState
         return vim.Task()

      def createVm(config=vim.vm.ConfigSpec(), pool=vim.ResourcePool(), host=vim.HostSystem() or None): # vim.Folder.createVm
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault, vim.fault.AlreadyExists, vim.fault.InvalidState
         return vim.Task()

      def registerVm(path="", name="" or None, asTemplate=False, pool=vim.ResourcePool() or None, host=vim.HostSystem() or None): # vim.Folder.registerVm
         # throws vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.AlreadyExists, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.VmConfigFault, vim.fault.InsufficientResourcesFault, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def createCluster(name="", spec=vim.cluster.ConfigSpec()): # vim.Folder.createCluster
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.ClusterComputeResource()

      def createClusterEx(name="", spec=vim.cluster.ConfigSpecEx()): # vim.Folder.createClusterEx
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.ClusterComputeResource()

      def addStandaloneHost(spec=vim.host.ConnectSpec(), compResSpec=vim.ComputeResource.ConfigSpec() or None, addConnected=False, license="" or None): # vim.Folder.addStandaloneHost
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault, vim.fault.DuplicateName
         return vim.Task()

      def createDatacenter(name=""): # vim.Folder.createDatacenter
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Datacenter()

      def unregisterAndDestroy(): # vim.Folder.unregisterAndDestroy
         # throws vim.fault.ConcurrentAccess, vim.fault.InvalidState
         return vim.Task()

      def createDistributedVirtualSwitch(spec=vim.DistributedVirtualSwitch.CreateSpec()): # vim.Folder.createDistributedVirtualSwitch
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.NotFound, vim.fault.DvsNotAuthorized
         return vim.Task()

      def createStoragePod(name=""): # vim.Folder.createStoragePod
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.StoragePod()

      def batchAddStandaloneHosts(newHosts=[ vim.Folder.NewHostSpec() ] or None, compResSpec=vim.ComputeResource.ConfigSpec() or None, addConnected=False): # vim.Folder.batchAddStandaloneHosts
         return vim.Task()

      def batchAddHostsToCluster(cluster=vim.ClusterComputeResource(), newHosts=[ vim.Folder.NewHostSpec() ] or None, existingHosts=[ vim.HostSystem() ] or None, compResSpec=vim.ComputeResource.ConfigSpec() or None, desiredState="" or None): # vim.Folder.batchAddHostsToCluster
         return vim.Task()

      class DesiredHostState(Enum): # vim.Folder.DesiredHostState
         maintenance = 0
         non_maintenance = 1

      class NewHostSpec(vmodl.DynamicData): # vim.Folder.NewHostSpec
         hostCnxSpec = vim.host.ConnectSpec()
         esxLicense = ""

      class FailedHostResult(vmodl.DynamicData): # vim.Folder.FailedHostResult
         hostName = ""
         host = vim.HostSystem()
         context = vmodl.LocalizableMessage()
         fault = vmodl.MethodFault()

      class BatchAddStandaloneHostsResult(vmodl.DynamicData): # vim.Folder.BatchAddStandaloneHostsResult
         addedHosts = [ vim.HostSystem() ]
         hostsFailedInventoryAdd = [ vim.Folder.FailedHostResult() ]

      class BatchAddHostsToClusterResult(vmodl.DynamicData): # vim.Folder.BatchAddHostsToClusterResult
         hostsAddedToCluster = [ vim.HostSystem() ]
         hostsFailedInventoryAdd = [ vim.Folder.FailedHostResult() ]
         hostsFailedMoveToCluster = [ vim.Folder.FailedHostResult() ]

   class HealthUpdate(vmodl.DynamicData): # vim.HealthUpdate
      entity = vim.ManagedEntity()
      healthUpdateInfoId = ""
      id = ""
      status = vim.ManagedEntity.Status()
      remediation = ""

   class HostSystem(vim.ManagedEntity): # vim.HostSystem
      runtime = vim.host.RuntimeInfo()
      summary = vim.host.Summary()
      hardware = vim.host.HardwareInfo()
      capability = vim.host.Capability()
      licensableResource = vim.LicenseManager.LicensableResourceInfo()
      remediationState = vim.HostSystem.RemediationState()
      precheckRemediationResult = vim.profile.host.ProfileManager.ApplyHostConfigSpec()
      remediationResult = vim.profile.host.ProfileManager.ApplyHostConfigResult()
      complianceCheckState = vim.HostSystem.ComplianceCheckState()
      complianceCheckResult = vim.profile.ComplianceResult()
      configManager = vim.host.ConfigManager()
      config = vim.host.ConfigInfo()
      vm = [ vim.VirtualMachine() ]
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      datastoreBrowser = vim.host.DatastoreBrowser()
      systemResources = vim.host.SystemResourceInfo()
      answerFileValidationState = vim.profile.host.AnswerFileStatusResult()
      answerFileValidationResult = vim.profile.host.AnswerFileStatusResult()

      def queryTpmAttestationReport(): # vim.HostSystem.queryTpmAttestationReport
         return vim.host.TpmAttestationReport()

      def queryConnectionInfo(): # vim.HostSystem.queryConnectionInfo
         return vim.host.ConnectInfo()

      def updateSystemResources(resourceInfo=vim.host.SystemResourceInfo()): # vim.HostSystem.updateSystemResources
         return None

      def updateSystemSwapConfiguration(sysSwapConfig=vim.host.SystemSwapConfiguration()): # vim.HostSystem.updateSystemSwapConfiguration
         return None

      def reconnect(cnxSpec=vim.host.ConnectSpec() or None, reconnectSpec=vim.HostSystem.ReconnectSpec() or None): # vim.HostSystem.reconnect
         # throws vim.fault.InvalidLogin, vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.HostConnectFault
         return vim.Task()

      def disconnect(): # vim.HostSystem.disconnect
         return vim.Task()

      def enterMaintenanceMode(timeout=0, evacuatePoweredOffVms=False or None, maintenanceSpec=vim.host.MaintenanceSpec() or None): # vim.HostSystem.enterMaintenanceMode
         # throws vim.fault.InvalidState, vim.fault.Timedout
         return vim.Task()

      def exitMaintenanceMode(timeout=0): # vim.HostSystem.exitMaintenanceMode
         # throws vim.fault.InvalidState, vim.fault.Timedout
         return vim.Task()

      def reboot(force=False): # vim.HostSystem.reboot
         # throws vim.fault.InvalidState
         return vim.Task()

      def shutdown(force=False): # vim.HostSystem.shutdown
         # throws vim.fault.InvalidState
         return vim.Task()

      def enterStandbyMode(timeoutSec=0, evacuatePoweredOffVms=False or None): # vim.HostSystem.enterStandbyMode
         # throws vim.fault.HostPowerOpFailed, vim.fault.InvalidState, vmodl.fault.NotSupported, vim.fault.Timedout, vmodl.fault.RequestCanceled
         return vim.Task()

      def exitStandbyMode(timeoutSec=0): # vim.HostSystem.exitStandbyMode
         # throws vim.fault.HostPowerOpFailed, vim.fault.InvalidState, vmodl.fault.NotSupported, vim.fault.Timedout
         return vim.Task()

      def queryOverhead(memorySize=0, videoRamSize=0 or None, numVcpus=0): # vim.HostSystem.queryOverhead
         return 0

      def queryOverheadEx(vmConfigInfo=vim.vm.ConfigInfo()): # vim.HostSystem.queryOverheadEx
         return 0

      def reconfigureDAS(): # vim.HostSystem.reconfigureDAS
         # throws vim.fault.DasConfigFault
         return vim.Task()

      def updateFlags(flagInfo=vim.host.FlagInfo()): # vim.HostSystem.updateFlags
         return None

      def enterLockdownMode(): # vim.HostSystem.enterLockdownMode
         # throws vim.fault.HostConfigFault
         return None

      def exitLockdownMode(): # vim.HostSystem.exitLockdownMode
         # throws vim.fault.HostConfigFault
         return None

      def acquireCimServicesTicket(): # vim.HostSystem.acquireCimServicesTicket
         return vim.HostServiceTicket()

      def updateIpmi(ipmiInfo=vim.host.IpmiInfo()): # vim.HostSystem.updateIpmi
         # throws vim.fault.InvalidIpmiLoginInfo, vim.fault.InvalidIpmiMacAddress
         return None

      def retrieveHardwareUptime(): # vim.HostSystem.retrieveHardwareUptime
         return 0

      def prepareCrypto(): # vim.HostSystem.prepareCrypto
         # throws vim.fault.InvalidState
         return None

      def enableCrypto(keyPlain=vim.encryption.CryptoKeyPlain()): # vim.HostSystem.enableCrypto
         # throws vim.fault.InvalidState
         return None

      def configureCryptoKey(keyId=vim.encryption.CryptoKeyId() or None): # vim.HostSystem.configureCryptoKey
         return None

      def queryProductLockerLocation(): # vim.HostSystem.queryProductLockerLocation
         # throws vim.fault.HostConfigFault
         return ""

      def updateProductLockerLocation(path=""): # vim.HostSystem.updateProductLockerLocation
         # throws vmodl.fault.InvalidArgument, vim.fault.FileNotFound, vim.fault.TaskInProgress, vim.fault.HostConfigFault
         return vim.Task()

      def retrieveFreeEpcMemory(): # vim.HostSystem.retrieveFreeEpcMemory
         return 0

      class ConnectionState(Enum): # vim.HostSystem.ConnectionState
         connected = 0
         notResponding = 1
         disconnected = 2

      class PowerState(Enum): # vim.HostSystem.PowerState
         poweredOn = 0
         poweredOff = 1
         standBy = 2
         unknown = 3

      class StandbyMode(Enum): # vim.HostSystem.StandbyMode
         entering = 0
         exiting = 1
         in = 2
         none = 3

      class CryptoState(Enum): # vim.HostSystem.CryptoState
         incapable = 0
         prepared = 1
         safe = 2
         pendingIncapable = 3

      class RemediationState(vmodl.DynamicData): # vim.HostSystem.RemediationState
         state = ""
         operationTime = vmodl.DateTime()

         class State(Enum): # vim.HostSystem.RemediationState.State
            remediationReady = 0
            precheckRemediationRunning = 1
            precheckRemediationComplete = 2
            precheckRemediationFailed = 3
            remediationRunning = 4
            remediationFailed = 5

      class ComplianceCheckState(vmodl.DynamicData): # vim.HostSystem.ComplianceCheckState
         state = ""
         checkTime = vmodl.DateTime()

      class ReconnectSpec(vmodl.DynamicData): # vim.HostSystem.ReconnectSpec
         syncState = False

   class ServiceInstance(vmodl.ManagedObject): # vim.ServiceInstance
      serverClock = vmodl.DateTime()
      capability = vim.Capability()
      content = vim.ServiceInstanceContent()

      def currentTime(): # vim.ServiceInstance.currentTime
         return vmodl.DateTime()

      def retrieveContent(): # vim.ServiceInstance.retrieveContent
         return vim.ServiceInstanceContent()

      def validateMigration(vm=[ vim.VirtualMachine() ], state=vim.VirtualMachine.PowerState() or None, testType=[ "" ] or None, pool=vim.ResourcePool() or None, host=vim.HostSystem() or None): # vim.ServiceInstance.validateMigration
         # throws vim.fault.InvalidState
         return [ vim.event.Event() ]

      def queryVMotionCompatibility(vm=vim.VirtualMachine(), host=[ vim.HostSystem() ], compatibility=[ "" ] or None): # vim.ServiceInstance.queryVMotionCompatibility
         return [ vim.ServiceInstance.HostVMotionCompatibility() ]

      def retrieveProductComponents(): # vim.ServiceInstance.retrieveProductComponents
         return [ vim.ServiceInstance.ProductComponentInfo() ]

      class ValidateMigrationTestType(Enum): # vim.ServiceInstance.ValidateMigrationTestType
         sourceTests = 0
         compatibilityTests = 1
         diskAccessibilityTests = 2
         resourceTests = 3

      class VMotionCompatibilityType(Enum): # vim.ServiceInstance.VMotionCompatibilityType
         cpu = 0
         software = 1

      class HostVMotionCompatibility(vmodl.DynamicData): # vim.ServiceInstance.HostVMotionCompatibility
         host = vim.HostSystem()
         compatibility = [ "" ]

      class ProductComponentInfo(vmodl.DynamicData): # vim.ServiceInstance.ProductComponentInfo
         id = ""
         name = ""
         version = ""
         release = 0

   class StoragePod(vim.Folder): # vim.StoragePod
      summary = vim.StoragePod.Summary()
      podStorageDrsEntry = vim.StorageResourceManager.PodStorageDrsEntry()

      class Summary(vmodl.DynamicData): # vim.StoragePod.Summary
         name = ""
         capacity = 0
         freeSpace = 0

   class VasaVvolManager(object): # (unknown name)

      class VasaProviderContainerSpec(vmodl.DynamicData): # vim.VasaVvolManager.VasaProviderContainerSpec
         vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
         scId = ""
         deleted = False

   class ClusterComputeResource(vim.ComputeResource): # vim.ClusterComputeResource
      configuration = vim.cluster.ConfigInfo()
      recommendation = [ vim.cluster.Recommendation() ]
      drsRecommendation = [ vim.cluster.DrsRecommendation() ]
      hciConfig = vim.ClusterComputeResource.HCIConfigInfo()
      migrationHistory = [ vim.cluster.DrsMigration() ]
      actionHistory = [ vim.cluster.ActionHistory() ]
      drsFault = [ vim.cluster.DrsFaults() ]

      def configureHCI(clusterSpec=vim.ClusterComputeResource.HCIConfigSpec(), hostInputs=[ vim.ClusterComputeResource.HostConfigurationInput() ] or None): # vim.ClusterComputeResource.configureHCI
         return vim.Task()

      def extendHCI(hostInputs=[ vim.ClusterComputeResource.HostConfigurationInput() ] or None, vSanConfigSpec=vim.SDDCBase() or None): # vim.ClusterComputeResource.extendHCI
         return vim.Task()

      def AbandonHciWorkflow(): # vim.ClusterComputeResource.AbandonHciWorkflow
         # throws vim.fault.InvalidState
         return None

      def validateHCIConfiguration(hciConfigSpec=vim.ClusterComputeResource.HCIConfigSpec() or None, hosts=[ vim.HostSystem() ] or None): # vim.ClusterComputeResource.validateHCIConfiguration
         # throws vim.fault.InvalidState
         return [ vim.ClusterComputeResource.ValidationResultBase() ]

      def reconfigure(spec=vim.cluster.ConfigSpec(), modify=False): # vim.ClusterComputeResource.reconfigure
         return vim.Task()

      def applyRecommendation(key=""): # vim.ClusterComputeResource.applyRecommendation
         return None

      def cancelRecommendation(key=""): # vim.ClusterComputeResource.cancelRecommendation
         return None

      def recommendHostsForVm(vm=vim.VirtualMachine(), pool=vim.ResourcePool() or None): # vim.ClusterComputeResource.recommendHostsForVm
         return [ vim.cluster.HostRecommendation() ]

      def addHost(spec=vim.host.ConnectSpec(), asConnected=False, resourcePool=vim.ResourcePool() or None, license="" or None): # vim.ClusterComputeResource.addHost
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault, vim.fault.DuplicateName
         return vim.Task()

      def moveInto(host=[ vim.HostSystem() ]): # vim.ClusterComputeResource.moveInto
         # throws vim.fault.DuplicateName, vim.fault.TooManyHosts, vim.fault.InvalidState
         return vim.Task()

      def moveHostInto(host=vim.HostSystem(), resourcePool=vim.ResourcePool() or None): # vim.ClusterComputeResource.moveHostInto
         # throws vim.fault.TooManyHosts, vim.fault.InvalidState
         return vim.Task()

      def refreshRecommendation(): # vim.ClusterComputeResource.refreshRecommendation
         return None

      def evcManager(): # vim.ClusterComputeResource.evcManager
         return vim.cluster.EVCManager()

      def retrieveDasAdvancedRuntimeInfo(): # vim.ClusterComputeResource.retrieveDasAdvancedRuntimeInfo
         return vim.cluster.DasAdvancedRuntimeInfo()

      def enterMaintenanceMode(host=[ vim.HostSystem() ], option=[ vim.option.OptionValue() ] or None): # vim.ClusterComputeResource.enterMaintenanceMode
         return vim.cluster.EnterMaintenanceResult()

      def placeVm(placementSpec=vim.cluster.PlacementSpec()): # vim.ClusterComputeResource.placeVm
         # throws vim.fault.InvalidState
         return vim.cluster.PlacementResult()

      def findRulesForVm(vm=vim.VirtualMachine()): # vim.ClusterComputeResource.findRulesForVm
         return [ vim.cluster.RuleInfo() ]

      def stampAllRulesWithUuid(): # vim.ClusterComputeResource.stampAllRulesWithUuid
         return vim.Task()

      def getResourceUsage(): # vim.ClusterComputeResource.getResourceUsage
         return vim.cluster.ResourceUsageSummary()

      def setCryptoMode(cryptoMode=""): # vim.ClusterComputeResource.setCryptoMode
         # throws vmodl.fault.InvalidRequest, vmodl.fault.InvalidArgument
         return None

      class Summary(vim.ComputeResource.Summary): # vim.ClusterComputeResource.Summary
         currentFailoverLevel = 0
         admissionControlInfo = vim.cluster.DasAdmissionControlInfo()
         numVmotions = 0
         targetBalance = 0
         currentBalance = 0
         drsScore = 0
         numVmsPerDrsScoreBucket = [ 0 ]
         usageSummary = vim.cluster.UsageSummary()
         currentEVCModeKey = ""
         dasData = vim.cluster.DasData()

      class DVSSetting(vmodl.DynamicData): # vim.ClusterComputeResource.DVSSetting
         dvSwitch = vim.DistributedVirtualSwitch()
         pnicDevices = [ "" ]
         dvPortgroupSetting = [ vim.ClusterComputeResource.DVSSetting.DVPortgroupToServiceMapping() ]

         class DVPortgroupToServiceMapping(vmodl.DynamicData): # vim.ClusterComputeResource.DVSSetting.DVPortgroupToServiceMapping
            dvPortgroup = vim.dvs.DistributedVirtualPortgroup()
            service = ""

      class HCIWorkflowState(Enum): # vim.ClusterComputeResource.HCIWorkflowState
         in_progress = 0
         done = 1
         invalid = 2

      class HostConfigurationProfile(vmodl.DynamicData): # vim.ClusterComputeResource.HostConfigurationProfile
         dateTimeConfig = vim.host.DateTimeConfig()
         lockdownMode = vim.host.HostAccessManager.LockdownMode()

      class HCIConfigInfo(vmodl.DynamicData): # vim.ClusterComputeResource.HCIConfigInfo
         workflowState = ""
         dvsSetting = [ vim.ClusterComputeResource.DVSSetting() ]
         configuredHosts = [ vim.HostSystem() ]
         hostConfigProfile = vim.ClusterComputeResource.HostConfigurationProfile()

      class ClusterConfigResult(vmodl.DynamicData): # vim.ClusterComputeResource.ClusterConfigResult
         failedHosts = [ vim.Folder.FailedHostResult() ]
         configuredHosts = [ vim.HostSystem() ]

      class DvsProfile(vmodl.DynamicData): # vim.ClusterComputeResource.DvsProfile
         dvsName = ""
         dvSwitch = vim.DistributedVirtualSwitch()
         pnicDevices = [ "" ]
         dvPortgroupMapping = [ vim.ClusterComputeResource.DvsProfile.DVPortgroupSpecToServiceMapping() ]

         class DVPortgroupSpecToServiceMapping(vmodl.DynamicData): # vim.ClusterComputeResource.DvsProfile.DVPortgroupSpecToServiceMapping
            dvPortgroupSpec = vim.dvs.DistributedVirtualPortgroup.ConfigSpec()
            dvPortgroup = vim.dvs.DistributedVirtualPortgroup()
            service = ""

      class VCProfile(vmodl.DynamicData): # vim.ClusterComputeResource.VCProfile
         clusterSpec = vim.cluster.ConfigSpecEx()
         evcModeKey = ""

      class HCIConfigSpec(vmodl.DynamicData): # vim.ClusterComputeResource.HCIConfigSpec
         dvsProf = [ vim.ClusterComputeResource.DvsProfile() ]
         hostConfigProfile = vim.ClusterComputeResource.HostConfigurationProfile()
         vSanConfigSpec = vim.SDDCBase()
         vcProf = vim.ClusterComputeResource.VCProfile()

      class HostVmkNicInfo(vmodl.DynamicData): # vim.ClusterComputeResource.HostVmkNicInfo
         nicSpec = vim.host.VirtualNic.Specification()
         service = ""

      class HostConfigurationInput(vmodl.DynamicData): # vim.ClusterComputeResource.HostConfigurationInput
         host = vim.HostSystem()
         hostVmkNics = [ vim.ClusterComputeResource.HostVmkNicInfo() ]
         allowedInNonMaintenanceMode = False

      class ValidationResultBase(vmodl.DynamicData): # vim.ClusterComputeResource.ValidationResultBase
         info = [ vmodl.LocalizableMessage() ]

      class HostConfigurationValidation(vim.ClusterComputeResource.ValidationResultBase): # vim.ClusterComputeResource.HostConfigurationValidation
         host = vim.HostSystem()
         isDvsSettingValid = False
         isVmknicSettingValid = False
         isNtpSettingValid = False
         isLockdownModeValid = False

      class DVSConfigurationValidation(vim.ClusterComputeResource.ValidationResultBase): # vim.ClusterComputeResource.DVSConfigurationValidation
         isDvsValid = False
         isDvpgValid = False

   class Datacenter(vim.ManagedEntity): # vim.Datacenter
      vmFolder = vim.Folder()
      hostFolder = vim.Folder()
      datastoreFolder = vim.Folder()
      networkFolder = vim.Folder()
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      configuration = vim.Datacenter.ConfigInfo()

      def batchQueryConnectInfo(hostSpecs=[ vim.host.ConnectSpec() ] or None): # vim.Datacenter.batchQueryConnectInfo
         return [ vim.Datacenter.BasicConnectInfo() ]

      def queryConnectionInfo(hostname="", port=0, username="", password="", sslThumbprint="" or None): # vim.Datacenter.queryConnectionInfo
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
         return vim.host.ConnectInfo()

      def queryConnectionInfoViaSpec(spec=vim.host.ConnectSpec()): # vim.Datacenter.queryConnectionInfoViaSpec
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
         return vim.host.ConnectInfo()

      def powerOnVm(vm=[ vim.VirtualMachine() ], option=[ vim.option.OptionValue() ] or None): # vim.Datacenter.powerOnVm
         return vim.Task()

      def queryConfigOptionDescriptor(): # vim.Datacenter.queryConfigOptionDescriptor
         return [ vim.vm.ConfigOptionDescriptor() ]

      def reconfigure(spec=vim.Datacenter.ConfigSpec(), modify=False): # vim.Datacenter.reconfigure
         return vim.Task()

      class BasicConnectInfo(vmodl.DynamicData): # vim.Datacenter.BasicConnectInfo
         hostname = ""
         error = vmodl.MethodFault()
         serverIp = ""
         numVm = 0
         numPoweredOnVm = 0
         hostProductInfo = vim.AboutInfo()
         hardwareVendor = ""
         hardwareModel = ""

      class ConfigInfo(vmodl.DynamicData): # vim.Datacenter.ConfigInfo
         defaultHardwareVersionKey = ""

      class ConfigSpec(vmodl.DynamicData): # vim.Datacenter.ConfigSpec
         defaultHardwareVersionKey = ""
