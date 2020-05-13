from enum import Enum

class vim(object):

   class AboutInfo(vmodl.DynamicData):
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

   class AuthorizationDescription(vmodl.DynamicData):
      privilege = [ vim.ElementDescription() ]
      privilegeGroup = [ vim.ElementDescription() ]

   class BatchResult(vmodl.DynamicData):
      result = ""
      hostKey = ""
      ds = vim.Datastore()
      fault = vmodl.MethodFault()

      class Result(Enum):
         success = 0
         fail = 1

   class Capability(vmodl.DynamicData):
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

   class CertificateManager(vmodl.ManagedObject):

      def refreshCACertificatesAndCRLs(host=[ vim.HostSystem() ]):
         return vim.Task()

      def refreshCertificates(host=[ vim.HostSystem() ]):
         return vim.Task()

      def revokeCertificates(host=[ vim.HostSystem() ]):
         return vim.Task()

   class ConfigSpecOperation(Enum):
      add = 0
      edit = 1
      remove = 2

   class CustomFieldsManager(vmodl.ManagedObject):
      field = [ vim.CustomFieldsManager.FieldDef() ]

      def addFieldDefinition(name="", moType=vmodl.TypeName() or None, fieldDefPolicy=vim.PrivilegePolicyDef() or None, fieldPolicy=vim.PrivilegePolicyDef() or None):
         # throws vim.fault.DuplicateName, vim.fault.InvalidPrivilege
         return vim.CustomFieldsManager.FieldDef()

      def removeFieldDefinition(key=0):
         return None

      def renameFieldDefinition(key=0, name=""):
         # throws vim.fault.DuplicateName
         return None

      def setField(entity=vim.ManagedEntity(), key=0, value=""):
         return None

      class FieldDef(vmodl.DynamicData):
         key = 0
         name = ""
         type = vmodl.TypeName()
         managedObjectType = vmodl.TypeName()
         fieldDefPrivileges = vim.PrivilegePolicyDef()
         fieldInstancePrivileges = vim.PrivilegePolicyDef()

      class Value(vmodl.DynamicData):
         key = 0

      class StringValue(vim.CustomFieldsManager.Value):
         value = ""

   class CustomizationSpecInfo(vmodl.DynamicData):
      name = ""
      description = ""
      type = ""
      changeVersion = ""
      lastUpdateTime = vmodl.DateTime()

   class CustomizationSpecItem(vmodl.DynamicData):
      info = vim.CustomizationSpecInfo()
      spec = vim.vm.customization.Specification()

   class CustomizationSpecManager(vmodl.ManagedObject):
      info = [ vim.CustomizationSpecInfo() ]
      encryptionKey = [ 0x00 ]

      def exists(name=""):
         return False

      def get(name=""):
         # throws vim.fault.NotFound
         return vim.CustomizationSpecItem()

      def create(item=vim.CustomizationSpecItem()):
         # throws vim.fault.CustomizationFault, vim.fault.AlreadyExists
         return None

      def overwrite(item=vim.CustomizationSpecItem()):
         # throws vim.fault.CustomizationFault, vim.fault.NotFound, vim.fault.ConcurrentAccess
         return None

      def delete(name=""):
         # throws vim.fault.NotFound
         return None

      def duplicate(name="", newName=""):
         # throws vim.fault.NotFound, vim.fault.AlreadyExists
         return None

      def rename(name="", newName=""):
         # throws vim.fault.NotFound, vim.fault.AlreadyExists
         return None

      def specItemToXml(item=vim.CustomizationSpecItem()):
         return ""

      def xmlToSpecItem(specItemXml=""):
         # throws vim.fault.CustomizationFault
         return vim.CustomizationSpecItem()

      def checkResources(guestOs=""):
         # throws vim.fault.CustomizationFault
         return None

   class DatastoreNamespaceManager(vmodl.ManagedObject):

      def CreateDirectory(datastore=vim.Datastore(), displayName="" or None, policy="" or None):
         # throws vim.fault.CannotCreateFile, vim.fault.FileAlreadyExists, vim.fault.InvalidDatastore
         return ""

      def DeleteDirectory(datacenter=vim.Datacenter() or None, datastorePath=""):
         # throws vim.fault.FileFault, vim.fault.FileNotFound, vim.fault.InvalidDatastore, vim.fault.InvalidDatastorePath
         return None

      def ConvertNamespacePathToUuidPath(datacenter=vim.Datacenter() or None, namespaceUrl=""):
         # throws vim.fault.InvalidDatastore, vim.fault.InvalidDatastorePath
         return ""

   class Description(vmodl.DynamicData):
      label = ""
      summary = ""

   class DesiredSoftwareSpec(vmodl.DynamicData):
      baseImageSpec = vim.DesiredSoftwareSpec.BaseImageSpec()
      vendorAddOnSpec = vim.DesiredSoftwareSpec.VendorAddOnSpec()

      class BaseImageSpec(vmodl.DynamicData):
         version = ""

      class VendorAddOnSpec(vmodl.DynamicData):
         name = ""
         version = ""

   class DiagnosticManager(vmodl.ManagedObject):

      def queryDescriptions(host=vim.HostSystem() or None):
         return [ vim.DiagnosticManager.LogDescriptor() ]

      def browse(host=vim.HostSystem() or None, key="", start=0 or None, lines=0 or None):
         # throws vim.fault.CannotAccessFile
         return vim.DiagnosticManager.LogHeader()

      def generateLogBundles(includeDefault=False, host=[ vim.HostSystem() ] or None):
         # throws vim.fault.LogBundlingFailed, vim.fault.TaskInProgress
         return vim.Task()

      class LogDescriptor(vmodl.DynamicData):
         key = ""
         fileName = ""
         creator = ""
         format = ""
         mimeType = ""
         info = vim.Description()

         class Creator(Enum):
            vpxd = 0
            vpxa = 1
            hostd = 2
            serverd = 3
            install = 4
            vpxClient = 5
            recordLog = 6

         class Format(Enum):
            plain = 0

      class LogHeader(vmodl.DynamicData):
         lineStart = 0
         lineEnd = 0
         lineText = [ "" ]

      class BundleInfo(vmodl.DynamicData):
         system = vim.HostSystem()
         url = ""

   class DrsStatsManager(object):

      class InjectorWorkload(object):

         class CorrelationState(Enum):
            Correlated = 0
            Uncorrelated = 1

   class ElementDescription(vim.Description):
      key = ""

   class EnumDescription(vmodl.DynamicData):
      key = vmodl.TypeName()
      tags = [ vim.ElementDescription() ]

   class EnvironmentBrowser(vmodl.ManagedObject):
      datastoreBrowser = vim.host.DatastoreBrowser()

      def queryConfigOptionDescriptor():
         return [ vim.vm.ConfigOptionDescriptor() ]

      def queryConfigOption(key="" or None, host=vim.HostSystem() or None):
         return vim.vm.ConfigOption()

      def queryConfigOptionEx(spec=vim.EnvironmentBrowser.ConfigOptionQuerySpec() or None):
         return vim.vm.ConfigOption()

      def queryConfigTarget(host=vim.HostSystem() or None):
         return vim.vm.ConfigTarget()

      def queryTargetCapabilities(host=vim.HostSystem() or None):
         return vim.host.Capability()

      class ConfigOptionQuerySpec(vmodl.DynamicData):
         key = ""
         host = vim.HostSystem()
         guestId = [ "" ]

   class ExtendedDescription(vim.Description):
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ExtendedElementDescription(vim.ElementDescription):
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ExtensibleManagedObject(vmodl.ManagedObject):
      value = [ vim.CustomFieldsManager.Value() ]
      availableField = [ vim.CustomFieldsManager.FieldDef() ]

      def setCustomValue(key="", value=""):
         return None

   class Extension(vmodl.DynamicData):
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

      class ServerInfo(vmodl.DynamicData):
         url = ""
         description = vim.Description()
         company = ""
         type = ""
         adminEmail = [ "" ]
         serverThumbprint = ""

      class ClientInfo(vmodl.DynamicData):
         version = ""
         description = vim.Description()
         company = ""
         type = ""
         url = ""

      class TaskTypeInfo(vmodl.DynamicData):
         taskID = ""

      class EventTypeInfo(vmodl.DynamicData):
         eventID = ""
         eventTypeSchema = ""

      class FaultTypeInfo(vmodl.DynamicData):
         faultID = ""

      class PrivilegeInfo(vmodl.DynamicData):
         privID = ""
         privGroupName = ""

      class ResourceInfo(vmodl.DynamicData):
         locale = ""
         module = ""
         data = [ vim.KeyValue() ]

      class HealthInfo(vmodl.DynamicData):
         url = ""

      class OvfConsumerInfo(vmodl.DynamicData):
         callbackUrl = ""
         sectionType = [ "" ]

   class ExtensionManager(vmodl.ManagedObject):
      extensionList = [ vim.Extension() ]

      def unregisterExtension(extensionKey=""):
         # throws vim.fault.NotFound
         return None

      def findExtension(extensionKey=""):
         return vim.Extension()

      def registerExtension(extension=vim.Extension()):
         return None

      def updateExtension(extension=vim.Extension()):
         # throws vim.fault.NotFound
         return None

      def getPublicKey():
         return ""

      def setPublicKey(extensionKey="", publicKey=""):
         return None

      def setCertificate(extensionKey="", certificatePem="" or None):
         # throws vim.fault.NotFound, vim.fault.NoClientCertificate
         return None

      def queryManagedBy(extensionKey=""):
         return [ vim.ManagedEntity() ]

      def queryExtensionIpAllocationUsage(extensionKeys=[ "" ] or None):
         return [ vim.ExtensionManager.IpAllocationUsage() ]

      class IpAllocationUsage(vmodl.DynamicData):
         extensionKey = ""
         numAddresses = 0

   class FaultsByHost(vmodl.DynamicData):
      host = vim.HostSystem()
      faults = [ vmodl.MethodFault() ]

   class FaultsByVM(vmodl.DynamicData):
      vm = vim.VirtualMachine()
      faults = [ vmodl.MethodFault() ]

   class FileManager(vmodl.ManagedObject):

      def moveFile(sourceName="", sourceDatacenter=vim.Datacenter() or None, destinationName="", destinationDatacenter=vim.Datacenter() or None, force=False or None):
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def copyFile(sourceName="", sourceDatacenter=vim.Datacenter() or None, destinationName="", destinationDatacenter=vim.Datacenter() or None, force=False or None):
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def deleteFile(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return vim.Task()

      def makeDirectory(name="", datacenter=vim.Datacenter() or None, createParentDirectories=False or None):
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault
         return None

      def changeOwner(name="", datacenter=vim.Datacenter() or None, owner=""):
         # throws vim.fault.InvalidDatastore, vim.fault.FileFault, vim.fault.UserNotFound
         return None

   class HbrManager(object):

      class ReplicationVmInfo(vmodl.DynamicData):
         state = ""
         progressInfo = vim.HbrManager.ReplicationVmInfo.ProgressInfo()
         imageId = ""
         lastError = vmodl.MethodFault()

         class State(Enum):
            none = 0
            paused = 1
            syncing = 2
            idle = 3
            active = 4
            error = 5

         class ProgressInfo(vmodl.DynamicData):
            progress = 0
            bytesTransferred = 0
            bytesToTransfer = 0
            checksumTotalBytes = 0
            checksumComparedBytes = 0

      class VmReplicationCapability(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         supportedQuiesceMode = ""
         compressionSupported = False
         maxSupportedSourceDiskCapacity = 0
         minRpo = 0
         fault = vmodl.MethodFault()

         class QuiesceMode(Enum):
            application = 0
            filesystem = 1
            none = 2

   class HealthUpdateInfo(vmodl.DynamicData):
      id = ""
      componentType = ""
      description = ""

      class ComponentType(Enum):
         Memory = 0
         Power = 1
         Fan = 2
         Network = 3
         Storage = 4

   class HealthUpdateManager(vmodl.ManagedObject):

      def registerProvider(name="", healthUpdateInfo=[ vim.HealthUpdateInfo() ] or None):
         return ""

      def unregisterProvider(providerId=""):
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return None

      def queryProviderList():
         return [ "" ]

      def hasProvider(id=""):
         return False

      def queryProviderName(id=""):
         # throws vim.fault.NotFound
         return ""

      def queryHealthUpdateInfos(providerId=""):
         # throws vim.fault.NotFound
         return [ vim.HealthUpdateInfo() ]

      def addMonitoredEntities(providerId="", entities=[ vim.ManagedEntity() ] or None):
         # throws vim.fault.NotFound
         return None

      def removeMonitoredEntities(providerId="", entities=[ vim.ManagedEntity() ] or None):
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return None

      def queryMonitoredEntities(providerId=""):
         # throws vim.fault.NotFound
         return [ vim.ManagedEntity() ]

      def hasMonitoredEntity(providerId="", entity=vim.ManagedEntity()):
         # throws vim.fault.NotFound
         return False

      def queryUnmonitoredHosts(providerId="", cluster=vim.ClusterComputeResource()):
         # throws vim.fault.NotFound
         return [ vim.HostSystem() ]

      def postHealthUpdates(providerId="", updates=[ vim.HealthUpdate() ] or None):
         # throws vim.fault.NotFound
         return None

      def queryHealthUpdates(providerId=""):
         # throws vim.fault.NotFound
         return [ vim.HealthUpdate() ]

      def addFilter(providerId="", filterName="", infoIds=[ "" ] or None):
         # throws vim.fault.NotFound
         return ""

      def queryFilterList(providerId=""):
         # throws vim.fault.NotFound
         return [ "" ]

      def queryFilterName(filterId=""):
         # throws vim.fault.NotFound
         return ""

      def queryFilterInfoIds(filterId=""):
         # throws vim.fault.NotFound
         return [ "" ]

      def queryFilterEntities(filterId=""):
         # throws vim.fault.NotFound
         return [ vim.ManagedEntity() ]

      def addFilterEntities(filterId="", entities=[ vim.ManagedEntity() ] or None):
         # throws vim.fault.NotFound
         return None

      def removeFilterEntities(filterId="", entities=[ vim.ManagedEntity() ] or None):
         # throws vim.fault.NotFound
         return None

      def removeFilter(filterId=""):
         # throws vim.fault.NotFound
         return None

   class HistoricalInterval(vmodl.DynamicData):
      key = 0
      samplingPeriod = 0
      name = ""
      length = 0
      level = 0
      enabled = False

   class HistoryCollector(vmodl.ManagedObject):
      filter = anyType()

      def setLatestPageSize(maxCount=0):
         return None

      def rewind():
         return None

      def reset():
         return None

      def remove():
         return None

   class HostServiceTicket(vmodl.DynamicData):
      host = ""
      port = 0
      sslThumbprint = ""
      service = ""
      serviceVersion = ""
      sessionId = ""

   class HttpNfcLease(vmodl.ManagedObject):
      initializeProgress = 0
      transferProgress = 0
      mode = ""
      capabilities = vim.HttpNfcLease.Capabilities()
      info = vim.HttpNfcLease.Info()
      state = vim.HttpNfcLease.State()
      error = vmodl.MethodFault()

      def getManifest():
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return [ vim.HttpNfcLease.ManifestEntry() ]

      def setManifestChecksumType(deviceUrlsToChecksumTypes=[ vim.KeyValue() ] or None):
         # throws vim.fault.InvalidState
         return None

      def complete():
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return None

      def abort(fault=vmodl.MethodFault() or None):
         # throws vim.fault.Timedout, vim.fault.InvalidState
         return None

      def progress(percent=0):
         # throws vim.fault.Timedout
         return None

      def pullFromUrls(files=[ vim.HttpNfcLease.SourceFile() ] or None):
         # throws vim.fault.InvalidState, vim.fault.HttpFault, vim.fault.SSLVerifyFault
         return vim.Task()

      class State(Enum):
         initializing = 0
         ready = 1
         done = 2
         error = 3

      class Mode(Enum):
         pushOrGet = 0
         pull = 1

      class DatastoreLeaseInfo(vmodl.DynamicData):
         datastoreKey = ""
         hosts = [ vim.HttpNfcLease.HostInfo() ]

      class HostInfo(vmodl.DynamicData):
         url = ""
         sslThumbprint = ""

      class Info(vmodl.DynamicData):
         lease = vim.HttpNfcLease()
         entity = vim.ManagedEntity()
         deviceUrl = [ vim.HttpNfcLease.DeviceUrl() ]
         totalDiskCapacityInKB = 0
         leaseTimeout = 0
         hostMap = [ vim.HttpNfcLease.DatastoreLeaseInfo() ]

      class DeviceUrl(vmodl.DynamicData):
         key = ""
         importKey = ""
         url = ""
         sslThumbprint = ""
         disk = False
         targetId = ""
         datastoreKey = ""
         fileSize = 0

      class ManifestEntry(vmodl.DynamicData):
         key = ""
         sha1 = ""
         checksum = ""
         checksumType = ""
         size = 0
         disk = False
         capacity = 0
         populatedSize = 0

         class ChecksumType(Enum):
            sha1 = 0
            sha256 = 1

      class SourceFile(vmodl.DynamicData):
         targetDeviceId = ""
         url = ""
         memberName = ""
         create = False
         sslThumbprint = ""
         httpHeaders = [ vim.KeyValue() ]
         size = 0

      class Capabilities(vmodl.DynamicData):
         pullModeSupported = False
         corsSupported = False

   class InheritablePolicy(vmodl.DynamicData):
      inherited = False

   class IntPolicy(vim.InheritablePolicy):
      value = 0

   class IoFilterManager(vmodl.ManagedObject):

      def installIoFilter(vibUrl="", compRes=vim.ComputeResource()):
         # throws vim.fault.AlreadyExists
         return vim.Task()

      def uninstallIoFilter(filterId="", compRes=vim.ComputeResource()):
         # throws vim.fault.NotFound, vim.fault.FilterInUse, vim.fault.InvalidState
         return vim.Task()

      def upgradeIoFilter(filterId="", compRes=vim.ComputeResource(), vibUrl=""):
         # throws vim.fault.NotFound, vim.fault.InvalidState
         return vim.Task()

      def queryIssue(filterId="", compRes=vim.ComputeResource()):
         # throws vim.fault.NotFound
         return vim.IoFilterManager.QueryIssueResult()

      def queryIoFilterInfo(compRes=vim.ComputeResource()):
         return [ vim.IoFilterManager.ClusterIoFilterInfo() ]

      def resolveInstallationErrorsOnHost(filterId="", host=vim.HostSystem()):
         # throws vim.fault.NotFound
         return vim.Task()

      def resolveInstallationErrorsOnCluster(filterId="", cluster=vim.ClusterComputeResource()):
         # throws vim.fault.NotFound
         return vim.Task()

      def queryDisksUsingFilter(filterId="", compRes=vim.ComputeResource()):
         # throws vim.fault.NotFound
         return [ vim.vm.device.VirtualDiskId() ]

      class IoFilterInfo(vmodl.DynamicData):
         id = ""
         name = ""
         vendor = ""
         version = ""
         type = ""
         summary = ""
         releaseDate = ""

      class HostIoFilterInfo(vim.IoFilterManager.IoFilterInfo):
         available = False

      class OperationType(Enum):
         install = 0
         uninstall = 1
         upgrade = 2

      class ClusterIoFilterInfo(vim.IoFilterManager.IoFilterInfo):
         opType = ""
         vibUrl = ""

      class IoFilterType(Enum):
         cache = 0
         replication = 1
         encryption = 2
         compression = 3
         inspection = 4
         datastoreIoControl = 5
         dataProvider = 6

      class QueryIssueResult(vmodl.DynamicData):
         opType = ""
         hostIssue = [ vim.IoFilterManager.QueryIssueResult.HostIssue() ]

         class HostIssue(vmodl.DynamicData):
            host = vim.HostSystem()
            issue = [ vmodl.MethodFault() ]

   class IpPoolManager(vmodl.ManagedObject):

      def queryIpPools(dc=vim.Datacenter()):
         return [ vim.vApp.IpPool() ]

      def createIpPool(dc=vim.Datacenter(), pool=vim.vApp.IpPool()):
         return 0

      def updateIpPool(dc=vim.Datacenter(), pool=vim.vApp.IpPool()):
         return None

      def destroyIpPool(dc=vim.Datacenter(), id=0, force=False):
         # throws vim.fault.InvalidState
         return None

      def allocateIpv4Address(dc=vim.Datacenter(), poolId=0, allocationId=""):
         return ""

      def allocateIpv6Address(dc=vim.Datacenter(), poolId=0, allocationId=""):
         return ""

      def releaseIpAllocation(dc=vim.Datacenter(), poolId=0, allocationId=""):
         return None

      def queryIPAllocations(dc=vim.Datacenter(), poolId=0, extensionKey=""):
         return [ vim.IpPoolManager.IpAllocation() ]

      class IpAllocation(vmodl.DynamicData):
         ipAddress = ""
         allocationId = ""

   class KeyValue(vmodl.DynamicData):
      key = ""
      value = ""

   class LatencySensitivity(vmodl.DynamicData):
      level = vim.LatencySensitivity.SensitivityLevel()
      sensitivity = 0

      class SensitivityLevel(Enum):
         low = 0
         normal = 1
         medium = 2
         high = 3
         custom = 4

   class LicenseManager(vmodl.ManagedObject):
      source = vim.LicenseManager.LicenseSource()
      sourceAvailable = False
      diagnostics = vim.LicenseManager.DiagnosticInfo()
      featureInfo = [ vim.LicenseManager.FeatureInfo() ]
      licensedEdition = ""
      licenses = [ vim.LicenseManager.LicenseInfo() ]
      licenseAssignmentManager = vim.LicenseAssignmentManager()
      evaluation = vim.LicenseManager.EvaluationInfo()

      def querySupportedFeatures(host=vim.HostSystem() or None):
         return [ vim.LicenseManager.FeatureInfo() ]

      def querySourceAvailability(host=vim.HostSystem() or None):
         return [ vim.LicenseManager.AvailabilityInfo() ]

      def queryUsage(host=vim.HostSystem() or None):
         return vim.LicenseManager.LicenseUsageInfo()

      def setEdition(host=vim.HostSystem() or None, featureKey="" or None):
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return None

      def checkFeature(host=vim.HostSystem() or None, featureKey=""):
         # throws vim.fault.InvalidState
         return False

      def enable(host=vim.HostSystem() or None, featureKey=""):
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return False

      def disable(host=vim.HostSystem() or None, featureKey=""):
         # throws vim.fault.InvalidState, vim.fault.LicenseServerUnavailable
         return False

      def configureSource(host=vim.HostSystem() or None, licenseSource=vim.LicenseManager.LicenseSource()):
         # throws vim.fault.CannotAccessLocalSource, vim.fault.InvalidLicense, vim.fault.LicenseServerUnavailable
         return None

      def updateLicense(licenseKey="", labels=[ vim.KeyValue() ] or None):
         return vim.LicenseManager.LicenseInfo()

      def addLicense(licenseKey="", labels=[ vim.KeyValue() ] or None):
         return vim.LicenseManager.LicenseInfo()

      def removeLicense(licenseKey=""):
         return None

      def decodeLicense(licenseKey=""):
         return vim.LicenseManager.LicenseInfo()

      def updateLabel(licenseKey="", labelKey="", labelValue=""):
         return None

      def removeLabel(licenseKey="", labelKey=""):
         return None

      class LicenseState(Enum):
         initializing = 0
         normal = 1
         marginal = 2
         fault = 3

      class LicenseKey(Enum):
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

      class LicenseSource(vmodl.DynamicData):
         pass

      class LicenseServer(vim.LicenseManager.LicenseSource):
         licenseServer = ""

      class LocalLicense(vim.LicenseManager.LicenseSource):
         licenseKeys = ""

      class EvaluationLicense(vim.LicenseManager.LicenseSource):
         remainingHours = 0

      class FeatureInfo(vmodl.DynamicData):
         key = ""
         featureName = ""
         featureDescription = ""
         state = vim.LicenseManager.FeatureInfo.State()
         costUnit = ""
         sourceRestriction = ""
         dependentKey = [ "" ]
         edition = False
         expiresOn = vmodl.DateTime()

         class CostUnit(Enum):
            host = 0
            cpuCore = 1
            cpuPackage = 2
            server = 3
            vm = 4

         class State(Enum):
            enabled = 0
            disabled = 1
            optional = 2

         class SourceRestriction(Enum):
            unrestricted = 0
            served = 1
            file = 2

      class ReservationInfo(vmodl.DynamicData):
         key = ""
         state = vim.LicenseManager.ReservationInfo.State()
         required = 0

         class State(Enum):
            notUsed = 0
            noLicense = 1
            unlicensedUse = 2
            licensed = 3

      class AvailabilityInfo(vmodl.DynamicData):
         feature = vim.LicenseManager.FeatureInfo()
         total = 0
         available = 0

      class DiagnosticInfo(vmodl.DynamicData):
         sourceLastChanged = vmodl.DateTime()
         sourceLost = ""
         sourceLatency = 0.0
         licenseRequests = ""
         licenseRequestFailures = ""
         licenseFeatureUnknowns = ""
         opState = vim.LicenseManager.LicenseState()
         lastStatusUpdate = vmodl.DateTime()
         opFailureMessage = ""

      class LicenseUsageInfo(vmodl.DynamicData):
         source = vim.LicenseManager.LicenseSource()
         sourceAvailable = False
         reservationInfo = [ vim.LicenseManager.ReservationInfo() ]
         featureInfo = [ vim.LicenseManager.FeatureInfo() ]

      class EvaluationInfo(vmodl.DynamicData):
         properties = [ vmodl.KeyAnyValue() ]

      class LicensableResourceInfo(vmodl.DynamicData):
         resource = [ vmodl.KeyAnyValue() ]

         class ResourceKey(Enum):
            numCpuPackages = 0
            numCpuCores = 1
            memorySize = 2
            memoryForVms = 3
            numVmsStarted = 4
            numVmsStarting = 5

      class LicenseInfo(vmodl.DynamicData):
         licenseKey = ""
         editionKey = ""
         name = ""
         total = 0
         used = 0
         costUnit = ""
         properties = [ vmodl.KeyAnyValue() ]
         labels = [ vim.KeyValue() ]

   class LocalizationManager(vmodl.ManagedObject):
      catalog = [ vim.LocalizationManager.MessageCatalog() ]

      class MessageCatalog(vmodl.DynamicData):
         moduleName = ""
         catalogName = ""
         locale = ""
         catalogUri = ""
         lastModified = vmodl.DateTime()
         md5sum = ""
         version = ""

   class LongPolicy(vim.InheritablePolicy):
      value = 0

   class MethodDescription(vim.Description):
      key = vmodl.MethodName()

   class NegatableExpression(vmodl.DynamicData):
      negate = False

   class NumericRange(vmodl.DynamicData):
      start = 0
      end = 0

   class OverheadMemoryManager(vmodl.ManagedObject):

      def lookupVmOverheadMemory(vm=vim.VirtualMachine(), host=vim.HostSystem()):
         # throws vim.fault.NotFound, vmodl.fault.InvalidArgument, vmodl.fault.ManagedObjectNotFound, vmodl.fault.InvalidType
         return 0

   class OvfConsumer(object):

      class OvfSection(vmodl.DynamicData):
         lineNumber = 0
         xml = ""

      class OstNodeType(Enum):
         envelope = 0
         virtualSystem = 1
         virtualSystemCollection = 2

      class OstNode(vmodl.DynamicData):
         id = ""
         type = ""
         section = [ vim.OvfConsumer.OvfSection() ]
         child = [ vim.OvfConsumer.OstNode() ]
         entity = vim.ManagedEntity()

   class OvfManager(vmodl.ManagedObject):
      ovfImportOption = [ vim.OvfManager.OvfOptionInfo() ]
      ovfExportOption = [ vim.OvfManager.OvfOptionInfo() ]

      def validateHost(ovfDescriptor="", host=vim.HostSystem(), vhp=vim.OvfManager.ValidateHostParams()):
         # throws vim.fault.TaskInProgress, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.ValidateHostResult()

      def parseDescriptor(ovfDescriptor="", pdp=vim.OvfManager.ParseDescriptorParams()):
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.ParseDescriptorResult()

      def createImportSpec(ovfDescriptor="", resourcePool=vim.ResourcePool(), datastore=vim.Datastore(), cisp=vim.OvfManager.CreateImportSpecParams()):
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.InvalidDatastore
         return vim.OvfManager.CreateImportSpecResult()

      def createDescriptor(obj=vim.ManagedEntity(), cdp=vim.OvfManager.CreateDescriptorParams()):
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidState
         return vim.OvfManager.CreateDescriptorResult()

      class OvfOptionInfo(vmodl.DynamicData):
         option = ""
         description = vmodl.LocalizableMessage()

      class DeploymentOption(vmodl.DynamicData):
         key = ""
         label = ""
         description = ""

      class CommonParams(vmodl.DynamicData):
         locale = ""
         deploymentOption = ""
         msgBundle = [ vim.KeyValue() ]
         importOption = [ "" ]

      class ValidateHostParams(vim.OvfManager.CommonParams):
         pass

      class ValidateHostResult(vmodl.DynamicData):
         downloadSize = 0
         flatDeploymentSize = 0
         sparseDeploymentSize = 0
         error = [ vmodl.MethodFault() ]
         warning = [ vmodl.MethodFault() ]
         supportedDiskProvisioning = [ "" ]

      class ParseDescriptorParams(vim.OvfManager.CommonParams):
         pass

      class ParseDescriptorResult(vmodl.DynamicData):
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

      class NetworkInfo(vmodl.DynamicData):
         name = ""
         description = ""

      class CreateImportSpecParams(vim.OvfManager.CommonParams):
         entityName = ""
         hostSystem = vim.HostSystem()
         networkMapping = [ vim.OvfManager.NetworkMapping() ]
         ipAllocationPolicy = ""
         ipProtocol = ""
         propertyMapping = [ vim.KeyValue() ]
         resourceMapping = [ vim.OvfManager.ResourceMap() ]
         diskProvisioning = ""
         instantiationOst = vim.OvfConsumer.OstNode()

         class DiskProvisioningType(Enum):
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

      class ResourceMap(vmodl.DynamicData):
         source = ""
         parent = vim.ResourcePool()
         resourceSpec = vim.ResourceConfigSpec()
         datastore = vim.Datastore()

      class NetworkMapping(vmodl.DynamicData):
         name = ""
         network = vim.Network()

      class CreateImportSpecResult(vmodl.DynamicData):
         importSpec = vim.ImportSpec()
         fileItem = [ vim.OvfManager.FileItem() ]
         warning = [ vmodl.MethodFault() ]
         error = [ vmodl.MethodFault() ]

      class FileItem(vmodl.DynamicData):
         deviceId = ""
         path = ""
         compressionMethod = ""
         chunkSize = 0
         size = 0
         cimType = 0
         create = False

      class CreateDescriptorParams(vmodl.DynamicData):
         ovfFiles = [ vim.OvfManager.OvfFile() ]
         name = ""
         description = ""
         includeImageFiles = False
         exportOption = [ "" ]
         snapshot = vim.vm.Snapshot()

      class CreateDescriptorResult(vmodl.DynamicData):
         ovfDescriptor = ""
         error = [ vmodl.MethodFault() ]
         warning = [ vmodl.MethodFault() ]
         includeImageFiles = False

      class OvfFile(vmodl.DynamicData):
         deviceId = ""
         path = ""
         compressionMethod = ""
         chunkSize = 0
         size = 0
         capacity = 0
         populatedSize = 0

   class PasswordField(vmodl.DynamicData):
      value = ""

   class PerformanceDescription(vmodl.DynamicData):
      counterType = [ vim.ElementDescription() ]
      statsType = [ vim.ElementDescription() ]

   class PerformanceManager(vmodl.ManagedObject):
      description = vim.PerformanceDescription()
      historicalInterval = [ vim.HistoricalInterval() ]
      perfCounter = [ vim.PerformanceManager.CounterInfo() ]

      def queryProviderSummary(entity=vmodl.ManagedObject()):
         return vim.PerformanceManager.ProviderSummary()

      def queryAvailableMetric(entity=vmodl.ManagedObject(), beginTime=vmodl.DateTime() or None, endTime=vmodl.DateTime() or None, intervalId=0 or None):
         return [ vim.PerformanceManager.MetricId() ]

      def queryCounter(counterId=[ 0 ]):
         return [ vim.PerformanceManager.CounterInfo() ]

      def queryCounterByLevel(level=0):
         return [ vim.PerformanceManager.CounterInfo() ]

      def queryStats(querySpec=[ vim.PerformanceManager.QuerySpec() ]):
         return [ vim.PerformanceManager.EntityMetricBase() ]

      def queryCompositeStats(querySpec=vim.PerformanceManager.QuerySpec()):
         return vim.PerformanceManager.CompositeEntityMetric()

      def createHistoricalInterval(intervalId=vim.HistoricalInterval()):
         return None

      def removeHistoricalInterval(samplePeriod=0):
         return None

      def updateHistoricalInterval(interval=vim.HistoricalInterval()):
         return None

      def updateCounterLevelMapping(counterLevelMap=[ vim.PerformanceManager.CounterLevelMapping() ]):
         return None

      def resetCounterLevelMapping(counters=[ 0 ]):
         return None

      class Format(Enum):
         normal = 0
         csv = 1

      class ProviderSummary(vmodl.DynamicData):
         entity = vmodl.ManagedObject()
         currentSupported = False
         summarySupported = False
         refreshRate = 0

      class CounterInfo(vmodl.DynamicData):
         key = 0
         nameInfo = vim.ElementDescription()
         groupInfo = vim.ElementDescription()
         unitInfo = vim.ElementDescription()
         rollupType = vim.PerformanceManager.CounterInfo.RollupType()
         statsType = vim.PerformanceManager.CounterInfo.StatsType()
         level = 0
         perDeviceLevel = 0
         associatedCounterId = [ 0 ]

         class RollupType(Enum):
            average = 0
            maximum = 1
            minimum = 2
            latest = 3
            summation = 4
            none = 5

         class StatsType(Enum):
            absolute = 0
            delta = 1
            rate = 2

         class Unit(Enum):
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

      class MetricId(vmodl.DynamicData):
         counterId = 0
         instance = ""

      class QuerySpec(vmodl.DynamicData):
         entity = vmodl.ManagedObject()
         startTime = vmodl.DateTime()
         endTime = vmodl.DateTime()
         maxSample = 0
         metricId = [ vim.PerformanceManager.MetricId() ]
         intervalId = 0
         format = ""

      class SampleInfo(vmodl.DynamicData):
         timestamp = vmodl.DateTime()
         interval = 0

      class MetricSeries(vmodl.DynamicData):
         id = vim.PerformanceManager.MetricId()

      class IntSeries(vim.PerformanceManager.MetricSeries):
         value = [ 0 ]

      class MetricSeriesCSV(vim.PerformanceManager.MetricSeries):
         value = ""

      class EntityMetricBase(vmodl.DynamicData):
         entity = vmodl.ManagedObject()

      class EntityMetric(vim.PerformanceManager.EntityMetricBase):
         sampleInfo = [ vim.PerformanceManager.SampleInfo() ]
         value = [ vim.PerformanceManager.MetricSeries() ]

      class EntityMetricCSV(vim.PerformanceManager.EntityMetricBase):
         sampleInfoCSV = ""
         value = [ vim.PerformanceManager.MetricSeriesCSV() ]

      class CompositeEntityMetric(vmodl.DynamicData):
         entity = vim.PerformanceManager.EntityMetricBase()
         childEntity = [ vim.PerformanceManager.EntityMetricBase() ]

      class CounterLevelMapping(vmodl.DynamicData):
         counterId = 0
         aggregateLevel = 0
         perDeviceLevel = 0

   class PrivilegePolicyDef(vmodl.DynamicData):
      createPrivilege = ""
      readPrivilege = ""
      updatePrivilege = ""
      deletePrivilege = ""

   class ResourceAllocationInfo(vmodl.DynamicData):
      reservation = 0
      expandableReservation = False
      limit = 0
      shares = vim.SharesInfo()
      overheadLimit = 0

   class ResourceAllocationOption(vmodl.DynamicData):
      sharesOption = vim.SharesOption()

   class ResourceConfigOption(vmodl.DynamicData):
      cpuAllocationOption = vim.ResourceAllocationOption()
      memoryAllocationOption = vim.ResourceAllocationOption()

   class ResourceConfigSpec(vmodl.DynamicData):
      entity = vim.ManagedEntity()
      changeVersion = ""
      lastModified = vmodl.DateTime()
      cpuAllocation = vim.ResourceAllocationInfo()
      memoryAllocation = vim.ResourceAllocationInfo()
      scaleDescendantsShares = ""

      class ScaleSharesBehavior(Enum):
         disabled = 0
         scaleCpuAndMemoryShares = 1

   class ResourcePlanningManager(vmodl.ManagedObject):

      def estimateDatabaseSize(dbSizeParam=vim.ResourcePlanningManager.DatabaseSizeParam()):
         return vim.ResourcePlanningManager.DatabaseSizeEstimate()

      class DatabaseSizeParam(vmodl.DynamicData):
         inventoryDesc = vim.ResourcePlanningManager.InventoryDescription()
         perfStatsDesc = vim.ResourcePlanningManager.PerfStatsDescription()

      class InventoryDescription(vmodl.DynamicData):
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

      class PerfStatsDescription(vmodl.DynamicData):
         intervals = [ vim.HistoricalInterval() ]

      class DatabaseSizeEstimate(vmodl.DynamicData):
         size = 0

   class SDDCBase(vmodl.DynamicData):
      pass

   class SearchIndex(vmodl.ManagedObject):

      def findByUuid(datacenter=vim.Datacenter() or None, uuid="", vmSearch=False, instanceUuid=False or None):
         return vim.ManagedEntity()

      def findByDatastorePath(datacenter=vim.Datacenter(), path=""):
         # throws vim.fault.InvalidDatastore
         return vim.VirtualMachine()

      def findByDnsName(datacenter=vim.Datacenter() or None, dnsName="", vmSearch=False):
         return vim.ManagedEntity()

      def findByIp(datacenter=vim.Datacenter() or None, ip="", vmSearch=False):
         return vim.ManagedEntity()

      def findByInventoryPath(inventoryPath=""):
         return vim.ManagedEntity()

      def findChild(entity=vim.ManagedEntity(), name=""):
         return vim.ManagedEntity()

      def findAllByUuid(datacenter=vim.Datacenter() or None, uuid="", vmSearch=False, instanceUuid=False or None):
         return [ vim.ManagedEntity() ]

      def findAllByDnsName(datacenter=vim.Datacenter() or None, dnsName="", vmSearch=False):
         return [ vim.ManagedEntity() ]

      def findAllByIp(datacenter=vim.Datacenter() or None, ip="", vmSearch=False):
         return [ vim.ManagedEntity() ]

   class SelectionSet(vmodl.DynamicData):
      pass

   class ServiceInstanceContent(vmodl.DynamicData):
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

   class ServiceLocator(vmodl.DynamicData):
      instanceUuid = ""
      url = ""
      credential = vim.ServiceLocator.Credential()
      sslThumbprint = ""

      class Credential(vmodl.DynamicData):
         pass

      class NamePassword(vim.ServiceLocator.Credential):
         username = ""
         password = ""

      class SAMLCredential(vim.ServiceLocator.Credential):
         token = ""

   class ServiceManager(vmodl.ManagedObject):
      service = [ vim.ServiceManager.ServiceInfo() ]

      def queryServiceList(serviceName="" or None, location=[ "" ] or None):
         return [ vim.ServiceManager.ServiceInfo() ]

      class ServiceInfo(vmodl.DynamicData):
         serviceName = ""
         location = [ "" ]
         service = vmodl.ManagedObject()
         description = ""

   class SessionManager(vmodl.ManagedObject):
      sessionList = [ vim.UserSession() ]
      currentSession = vim.UserSession()
      message = ""
      messageLocaleList = [ "" ]
      supportedLocaleList = [ "" ]
      defaultLocale = ""

      def updateMessage(message=""):
         return None

      def loginByToken(locale="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def login(userName="", password="", locale="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def loginBySSPI(base64Token="", locale="" or None):
         # throws vim.fault.SSPIChallenge, vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def logout():
         return None

      def acquireLocalTicket(userName=""):
         # throws vim.fault.InvalidLogin
         return vim.SessionManager.LocalTicket()

      def acquireGenericServiceTicket(spec=vim.SessionManager.ServiceRequestSpec()):
         return vim.SessionManager.GenericServiceTicket()

      def terminate(sessionId=[ "" ]):
         # throws vim.fault.NotFound
         return None

      def setLocale(locale=""):
         # throws vim.fault.InvalidLocale
         return None

      def loginExtensionBySubjectName(extensionKey="", locale="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale, vim.fault.NotFound, vim.fault.NoClientCertificate, vim.fault.NoSubjectName
         return vim.UserSession()

      def loginExtensionByCertificate(extensionKey="", locale="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale, vim.fault.NoClientCertificate
         return vim.UserSession()

      def impersonateUser(userName="", locale="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidLocale
         return vim.UserSession()

      def sessionIsActive(sessionID="", userName=""):
         return False

      def acquireCloneTicket():
         return ""

      def cloneSession(cloneTicket=""):
         # throws vim.fault.InvalidLogin
         return vim.UserSession()

      class LocalTicket(vmodl.DynamicData):
         userName = ""
         passwordFilePath = ""

      class GenericServiceTicket(vmodl.DynamicData):
         id = ""
         hostName = ""
         sslThumbprint = ""

      class ServiceRequestSpec(vmodl.DynamicData):
         pass

      class VmomiServiceRequestSpec(vim.SessionManager.ServiceRequestSpec):
         method = vmodl.MethodName()

      class HttpServiceRequestSpec(vim.SessionManager.ServiceRequestSpec):
         method = ""
         url = ""

         class Method(Enum):
            httpOptions = 0
            httpGet = 1
            httpHead = 2
            httpPost = 3
            httpPut = 4
            httpDelete = 5
            httpTrace = 6
            httpConnect = 7

   class SharesInfo(vmodl.DynamicData):
      shares = 0
      level = vim.SharesInfo.Level()

      class Level(Enum):
         low = 0
         normal = 1
         high = 2
         custom = 3

   class SharesOption(vmodl.DynamicData):
      sharesOption = vim.option.IntOption()
      defaultLevel = vim.SharesInfo.Level()

   class SimpleCommand(vmodl.ManagedObject):
      encodingType = vim.SimpleCommand.Encoding()
      entity = vim.ServiceManager.ServiceInfo()

      def Execute(arguments=[ "" ] or None):
         return ""

      class Encoding(Enum):
         CSV = 0
         HEX = 1
         STRING = 2

   class SiteInfo(vmodl.DynamicData):
      pass

   class SiteInfoManager(vmodl.ManagedObject):

      def GetSiteInfo():
         return vim.SiteInfo()

   class StorageQueryManager(vmodl.ManagedObject):

      def queryHostsWithAttachedLun(lunUuid=""):
         return [ vim.HostSystem() ]

   class StorageResourceManager(vmodl.ManagedObject):

      def ConfigureDatastoreIORM(datastore=vim.Datastore(), spec=vim.StorageResourceManager.IORMConfigSpec()):
         # throws vim.fault.IORMNotSupportedHostOnDatastore, vim.fault.InaccessibleDatastore
         return vim.Task()

      def QueryIORMConfigOption(host=vim.HostSystem()):
         return vim.StorageResourceManager.IORMConfigOption()

      def queryDatastorePerformanceSummary(datastore=vim.Datastore()):
         # throws vim.fault.NotFound
         return [ vim.StorageResourceManager.StoragePerformanceSummary() ]

      def applyRecommendationToPod(pod=vim.StoragePod(), key=""):
         return vim.Task()

      def applyRecommendation(key=[ "" ]):
         return vim.Task()

      def cancelRecommendation(key=[ "" ]):
         return None

      def refreshRecommendation(pod=vim.StoragePod()):
         return None

      def refreshRecommendationsForPod(pod=vim.StoragePod()):
         # throws vmodl.fault.InvalidArgument
         return vim.Task()

      def configureStorageDrsForPod(pod=vim.StoragePod(), spec=vim.storageDrs.ConfigSpec(), modify=False):
         return vim.Task()

      def validateStoragePodConfig(pod=vim.StoragePod(), spec=vim.storageDrs.ConfigSpec()):
         return vmodl.MethodFault()

      def recommendDatastores(storageSpec=vim.storageDrs.StoragePlacementSpec()):
         return vim.storageDrs.StoragePlacementResult()

      class IOAllocationInfo(vmodl.DynamicData):
         limit = 0
         shares = vim.SharesInfo()
         reservation = 0

      class IOAllocationOption(vmodl.DynamicData):
         limitOption = vim.option.LongOption()
         sharesOption = vim.SharesOption()

      class CongestionThresholdMode(Enum):
         automatic = 0
         manual = 1

      class IORMConfigInfo(vmodl.DynamicData):
         enabled = False
         congestionThresholdMode = ""
         congestionThreshold = 0
         percentOfPeakThroughput = 0
         statsCollectionEnabled = False
         reservationEnabled = False
         statsAggregationDisabled = False
         reservableIopsThreshold = 0

      class IORMConfigSpec(vmodl.DynamicData):
         enabled = False
         congestionThresholdMode = ""
         congestionThreshold = 0
         percentOfPeakThroughput = 0
         statsCollectionEnabled = False
         reservationEnabled = False
         statsAggregationDisabled = False
         reservableIopsThreshold = 0

      class IORMConfigOption(vmodl.DynamicData):
         enabledOption = vim.option.BoolOption()
         congestionThresholdOption = vim.option.IntOption()
         statsCollectionEnabledOption = vim.option.BoolOption()
         reservationEnabledOption = vim.option.BoolOption()

      class StoragePerformanceSummary(vmodl.DynamicData):
         interval = 0
         percentile = [ 0 ]
         datastoreReadLatency = [ 0.0 ]
         datastoreWriteLatency = [ 0.0 ]
         datastoreVmLatency = [ 0.0 ]
         datastoreReadIops = [ 0.0 ]
         datastoreWriteIops = [ 0.0 ]
         siocActivityDuration = 0

      class PodStorageDrsEntry(vmodl.DynamicData):
         storageDrsConfig = vim.storageDrs.ConfigInfo()
         recommendation = [ vim.cluster.Recommendation() ]
         drsFault = [ vim.cluster.DrsFaults() ]
         actionHistory = [ vim.cluster.ActionHistory() ]

      class StorageProfileStatistics(vmodl.DynamicData):
         profileId = ""
         totalSpaceMB = 0
         usedSpaceMB = 0

   class StringExpression(vim.NegatableExpression):
      value = ""

   class StringPolicy(vim.InheritablePolicy):
      value = ""

   class Tag(vmodl.DynamicData):
      key = ""

   class TaskDescription(vmodl.DynamicData):
      methodInfo = [ vim.ElementDescription() ]
      state = [ vim.ElementDescription() ]
      reason = [ vim.TypeDescription() ]

   class TaskHistoryCollector(vim.HistoryCollector):
      latestPage = [ vim.TaskInfo() ]

      def readNext(maxCount=0):
         return [ vim.TaskInfo() ]

      def readPrev(maxCount=0):
         return [ vim.TaskInfo() ]

   class TaskInfo(vmodl.DynamicData):
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
      result = anyType()
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

      class State(Enum):
         queued = 0
         running = 1
         success = 2
         error = 3

   class TaskManager(vmodl.ManagedObject):
      recentTask = [ vim.Task() ]
      description = vim.TaskDescription()
      maxCollector = 0

      def createCollector(filter=vim.TaskFilterSpec()):
         # throws vim.fault.InvalidState
         return vim.TaskHistoryCollector()

      def createTask(obj=vmodl.ManagedObject(), taskTypeId="", initiatedBy="" or None, cancelable=False, parentTaskKey="" or None, activationId="" or None):
         return vim.TaskInfo()

   class TaskReason(vmodl.DynamicData):
      pass

   class TaskReasonAlarm(vim.TaskReason):
      alarmName = ""
      alarm = vim.alarm.Alarm()
      entityName = ""
      entity = vim.ManagedEntity()

   class TaskReasonSchedule(vim.TaskReason):
      name = ""
      scheduledTask = vim.scheduler.ScheduledTask()

   class TaskReasonSystem(vim.TaskReason):
      pass

   class TaskReasonUser(vim.TaskReason):
      userName = ""

   class TypeDescription(vim.Description):
      key = vmodl.TypeName()

   class UpdateVirtualMachineFilesResult(vmodl.DynamicData):
      failedVmFile = [ vim.UpdateVirtualMachineFilesResult.FailedVmFileInfo() ]

      class FailedVmFileInfo(vmodl.DynamicData):
         vmFile = ""
         fault = vmodl.MethodFault()

   class UserDirectory(vmodl.ManagedObject):
      domainList = [ "" ]

      def retrieveUserGroups(domain="" or None, searchStr="", belongsToGroup="" or None, belongsToUser="" or None, exactMatch=False, findUsers=False, findGroups=False):
         # throws vim.fault.NotFound
         return [ vim.UserSearchResult() ]

   class UserSearchResult(vmodl.DynamicData):
      principal = ""
      fullName = ""
      group = False

   class UserSession(vmodl.DynamicData):
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

   class VVolVmConfigFileUpdateResult(vmodl.DynamicData):
      succeededVmConfigFile = [ vim.KeyValue() ]
      failedVmConfigFile = [ vim.VVolVmConfigFileUpdateResult.FailedVmConfigFileInfo() ]

      class FailedVmConfigFileInfo(vmodl.DynamicData):
         targetConfigVVolId = ""
         dsPath = ""
         fault = vmodl.MethodFault()

   class VasaStorageArray(vmodl.DynamicData):
      name = ""
      uuid = ""
      vendorId = ""
      modelId = ""

   class VimVasaProvider(vmodl.DynamicData):
      uid = ""
      url = ""
      name = ""
      selfSignedCertificate = ""

      class StatePerArray(vmodl.DynamicData):
         priority = 0
         arrayId = ""
         active = False

   class VimVasaProviderInfo(vmodl.DynamicData):
      provider = vim.VimVasaProvider()
      arrayState = [ vim.VimVasaProvider.StatePerArray() ]

   class VirtualizationManager(vmodl.ManagedObject):
      pass

   class VsanUpgradeSystem(vmodl.ManagedObject):

      def performUpgradePreflightCheck(cluster=vim.ClusterComputeResource(), downgradeFormat=False or None):
         # throws vim.fault.VsanFault
         return vim.VsanUpgradeSystem.PreflightCheckResult()

      def queryUpgradeStatus(cluster=vim.ClusterComputeResource()):
         # throws vim.fault.VsanFault
         return vim.VsanUpgradeSystem.UpgradeStatus()

      def performUpgrade(cluster=vim.ClusterComputeResource(), performObjectUpgrade=False or None, downgradeFormat=False or None, allowReducedRedundancy=False or None, excludeHosts=[ vim.HostSystem() ] or None):
         # throws vim.fault.VsanFault
         return vim.Task()

      class PreflightCheckIssue(vmodl.DynamicData):
         msg = ""

      class HostsDisconnectedIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         hosts = [ vim.HostSystem() ]

      class MissingHostsInClusterIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         hosts = [ vim.HostSystem() ]

      class RogueHostsInClusterIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         uuids = [ "" ]

      class WrongEsxVersionIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         hosts = [ vim.HostSystem() ]

      class AutoClaimEnabledOnHostsIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         hosts = [ vim.HostSystem() ]

      class APIBrokenIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         hosts = [ vim.HostSystem() ]

      class V2ObjectsPresentDuringDowngradeIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         uuids = [ "" ]

      class NotEnoughFreeCapacityIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         reducedRedundancyUpgradePossible = False

      class NetworkPartitionInfo(vmodl.DynamicData):
         hosts = [ vim.HostSystem() ]

      class NetworkPartitionIssue(vim.VsanUpgradeSystem.PreflightCheckIssue):
         partitions = [ vim.VsanUpgradeSystem.NetworkPartitionInfo() ]

      class PreflightCheckResult(vmodl.DynamicData):
         issues = [ vim.VsanUpgradeSystem.PreflightCheckIssue() ]
         diskMappingToRestore = vim.vsan.host.DiskMapping()

      class UpgradeHistoryItem(vmodl.DynamicData):
         timestamp = vmodl.DateTime()
         host = vim.HostSystem()
         message = ""
         task = vim.Task()

      class UpgradeHistoryDiskGroupOpType(Enum):
         add = 0
         remove = 1

      class UpgradeHistoryDiskGroupOp(vim.VsanUpgradeSystem.UpgradeHistoryItem):
         operation = ""
         diskMapping = vim.vsan.host.DiskMapping()

      class UpgradeHistoryPreflightFail(vim.VsanUpgradeSystem.UpgradeHistoryItem):
         preflightResult = vim.VsanUpgradeSystem.PreflightCheckResult()

      class UpgradeStatus(vmodl.DynamicData):
         inProgress = False
         history = [ vim.VsanUpgradeSystem.UpgradeHistoryItem() ]
         aborted = False
         completed = False
         progress = 0

   class action(object):

      class Action(vmodl.DynamicData):

         class ActionParameter(Enum):
            targetName = 0
            alarmName = 1
            oldStatus = 2
            newStatus = 3
            triggeringSummary = 4
            declaringSummary = 5
            eventDescription = 6
            target = 7
            alarm = 8

      class CreateTaskAction(vim.action.Action):
         taskTypeId = ""
         cancelable = False

      class MethodAction(vim.action.Action):
         name = vmodl.MethodName()
         argument = [ vim.action.MethodActionArgument() ]

      class MethodActionArgument(vmodl.DynamicData):
         value = anyType()

      class RunScriptAction(vim.action.Action):
         script = ""

      class SendEmailAction(vim.action.Action):
         toList = ""
         ccList = ""
         subject = ""
         body = ""

      class SendSNMPAction(vim.action.Action):
         pass

   class alarm(object):

      class Alarm(vim.ExtensibleManagedObject):
         info = vim.alarm.AlarmInfo()

         def remove():
            return None

         def reconfigure(spec=vim.alarm.AlarmSpec()):
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return None

      class AlarmAction(vmodl.DynamicData):
         pass

      class AlarmDescription(vmodl.DynamicData):
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

      class AlarmExpression(vmodl.DynamicData):
         pass

      class AlarmSetting(vmodl.DynamicData):
         toleranceRange = 0
         reportingFrequency = 0

      class AlarmSpec(vmodl.DynamicData):
         name = ""
         systemName = ""
         description = ""
         enabled = False
         expression = vim.alarm.AlarmExpression()
         action = vim.alarm.AlarmAction()
         actionFrequency = 0
         setting = vim.alarm.AlarmSetting()

      class AndAlarmExpression(vim.alarm.AlarmExpression):
         expression = [ vim.alarm.AlarmExpression() ]

      class GroupAlarmAction(vim.alarm.AlarmAction):
         action = [ vim.alarm.AlarmAction() ]

      class MetricAlarmExpression(vim.alarm.AlarmExpression):
         operator = vim.alarm.MetricAlarmExpression.MetricOperator()
         type = vmodl.TypeName()
         metric = vim.PerformanceManager.MetricId()
         yellow = 0
         yellowInterval = 0
         red = 0
         redInterval = 0

         class MetricOperator(Enum):
            isAbove = 0
            isBelow = 1

      class OrAlarmExpression(vim.alarm.AlarmExpression):
         expression = [ vim.alarm.AlarmExpression() ]

      class StateAlarmExpression(vim.alarm.AlarmExpression):
         operator = vim.alarm.StateAlarmExpression.StateOperator()
         type = vmodl.TypeName()
         statePath = vmodl.PropertyPath()
         yellow = ""
         red = ""

         class StateOperator(Enum):
            isEqual = 0
            isUnequal = 1

      class AlarmFilterSpec(vmodl.DynamicData):
         status = [ vim.ManagedEntity.Status() ]
         typeEntity = ""
         typeTrigger = ""

         class AlarmTypeByEntity(Enum):
            entityTypeAll = 0
            entityTypeHost = 1
            entityTypeVm = 2

         class AlarmTypeByTrigger(Enum):
            triggerTypeAll = 0
            triggerTypeEvent = 1
            triggerTypeMetric = 2

      class AlarmInfo(vim.alarm.AlarmSpec):
         key = ""
         alarm = vim.alarm.Alarm()
         entity = vim.ManagedEntity()
         lastModifiedTime = vmodl.DateTime()
         lastModifiedUser = ""
         creationEventId = 0

      class AlarmManager(vmodl.ManagedObject):
         defaultExpression = [ vim.alarm.AlarmExpression() ]
         description = vim.alarm.AlarmDescription()

         def create(entity=vim.ManagedEntity(), spec=vim.alarm.AlarmSpec()):
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.alarm.Alarm()

         def getAlarm(entity=vim.ManagedEntity() or None):
            return [ vim.alarm.Alarm() ]

         def getAlarmActionsEnabled(entity=vim.ManagedEntity()):
            return False

         def setAlarmActionsEnabled(entity=vim.ManagedEntity(), enabled=False):
            return None

         def getAlarmState(entity=vim.ManagedEntity()):
            return [ vim.alarm.AlarmState() ]

         def acknowledgeAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()):
            return None

         def clearTriggeredAlarms(filter=vim.alarm.AlarmFilterSpec()):
            return None

         def disableAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()):
            return None

         def enableAlarm(alarm=vim.alarm.Alarm(), entity=vim.ManagedEntity()):
            return None

      class AlarmState(vmodl.DynamicData):
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

      class AlarmTriggeringAction(vim.alarm.AlarmAction):
         action = vim.action.Action()
         transitionSpecs = [ vim.alarm.AlarmTriggeringAction.TransitionSpec() ]
         green2yellow = False
         yellow2red = False
         red2yellow = False
         yellow2green = False

         class TransitionSpec(vmodl.DynamicData):
            startState = vim.ManagedEntity.Status()
            finalState = vim.ManagedEntity.Status()
            repeats = False

      class EventAlarmExpression(vim.alarm.AlarmExpression):
         comparisons = [ vim.alarm.EventAlarmExpression.Comparison() ]
         eventType = vmodl.TypeName()
         eventTypeId = ""
         objectType = vmodl.TypeName()
         status = vim.ManagedEntity.Status()

         class ComparisonOperator(Enum):
            equals = 0
            notEqualTo = 1
            startsWith = 2
            doesNotStartWith = 3
            endsWith = 4
            doesNotEndWith = 5

         class Comparison(vmodl.DynamicData):
            attributeName = ""
            operator = ""
            value = ""

   class cluster(object):

      class Action(vmodl.DynamicData):
         type = ""
         target = vmodl.ManagedObject()

         class ActionType(Enum):
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

      class ActionHistory(vmodl.DynamicData):
         action = vim.cluster.Action()
         time = vmodl.DateTime()

      class AttemptedVmInfo(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         task = vim.Task()

      class ConfigInfo(vmodl.DynamicData):
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfig = [ vim.cluster.DasVmConfigInfo() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfig = [ vim.cluster.DrsVmConfigInfo() ]
         rule = [ vim.cluster.RuleInfo() ]

      class ConfigSpec(vmodl.DynamicData):
         dasConfig = vim.cluster.DasConfigInfo()
         dasVmConfigSpec = [ vim.cluster.DasVmConfigSpec() ]
         drsConfig = vim.cluster.DrsConfigInfo()
         drsVmConfigSpec = [ vim.cluster.DrsVmConfigSpec() ]
         rulesSpec = [ vim.cluster.RuleSpec() ]

      class CryptoConfigInfo(vmodl.DynamicData):
         cryptoMode = ""

         class CryptoMode(Enum):
            onDemand = 0
            forceEnable = 1

      class DasAamNodeState(vmodl.DynamicData):
         host = vim.HostSystem()
         name = ""
         configState = ""
         runtimeState = ""

         class DasState(Enum):
            uninitialized = 0
            initialized = 1
            configuring = 2
            unconfiguring = 3
            running = 4
            error = 5
            agentShutdown = 6
            nodeFailed = 7

      class DasAdmissionControlInfo(vmodl.DynamicData):
         pass

      class DasAdmissionControlPolicy(vmodl.DynamicData):
         resourceReductionToToleratePercent = 0

      class DasAdvancedRuntimeInfo(vmodl.DynamicData):
         dasHostInfo = vim.cluster.DasHostInfo()
         vmcpSupported = vim.cluster.DasAdvancedRuntimeInfo.VmcpCapabilityInfo()
         heartbeatDatastoreInfo = [ vim.cluster.DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo() ]

         class VmcpCapabilityInfo(vmodl.DynamicData):
            storageAPDSupported = False
            storagePDLSupported = False

         class HeartbeatDatastoreInfo(vmodl.DynamicData):
            datastore = vim.Datastore()
            hosts = [ vim.HostSystem() ]

      class DasConfigInfo(vmodl.DynamicData):
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

         class ServiceState(Enum):
            disabled = 0
            enabled = 1

         class VmMonitoringState(Enum):
            vmMonitoringDisabled = 0
            vmMonitoringOnly = 1
            vmAndAppMonitoring = 2

         class HBDatastoreCandidate(Enum):
            userSelectedDs = 0
            allFeasibleDs = 1
            allFeasibleDsWithUserPreference = 2

      class DasData(vmodl.DynamicData):
         pass

      class DasDataSummary(vim.cluster.DasData):
         hostListVersion = 0
         clusterConfigVersion = 0
         compatListVersion = 0

      class DasFailoverLevelAdvancedRuntimeInfo(vim.cluster.DasAdvancedRuntimeInfo):
         slotInfo = vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.SlotInfo()
         totalSlots = 0
         usedSlots = 0
         unreservedSlots = 0
         totalVms = 0
         totalHosts = 0
         totalGoodHosts = 0
         hostSlots = [ vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.HostSlots() ]
         vmsRequiringMultipleSlots = [ vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.VmSlots() ]

         class SlotInfo(vmodl.DynamicData):
            numVcpus = 0
            cpuMHz = 0
            memoryMB = 0

         class HostSlots(vmodl.DynamicData):
            host = vim.HostSystem()
            slots = 0

         class VmSlots(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            slots = 0

      class DasFdmAvailabilityState(Enum):
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

      class DasFdmHostState(vmodl.DynamicData):
         state = ""
         stateReporter = vim.HostSystem()

      class DasHostInfo(vmodl.DynamicData):
         pass

      class DasHostRecommendation(vmodl.DynamicData):
         host = vim.HostSystem()
         drsRating = 0

      class DasVmConfigInfo(vmodl.DynamicData):
         key = vim.VirtualMachine()
         restartPriority = vim.cluster.DasVmConfigInfo.Priority()
         powerOffOnIsolation = False
         dasSettings = vim.cluster.DasVmSettings()

         class Priority(Enum):
            disabled = 0
            low = 1
            medium = 2
            high = 3

      class DasVmSettings(vmodl.DynamicData):
         restartPriority = ""
         restartPriorityTimeout = 0
         isolationResponse = ""
         vmToolsMonitoringSettings = vim.cluster.VmToolsMonitoringSettings()
         vmComponentProtectionSettings = vim.cluster.VmComponentProtectionSettings()

         class RestartPriority(Enum):
            disabled = 0
            lowest = 1
            low = 2
            medium = 3
            high = 4
            highest = 5
            clusterRestartPriority = 6

         class IsolationResponse(Enum):
            none = 0
            powerOff = 1
            shutdown = 2
            clusterIsolationResponse = 3

      class DpmConfigInfo(vmodl.DynamicData):
         enabled = False
         defaultDpmBehavior = vim.cluster.DpmConfigInfo.DpmBehavior()
         hostPowerActionRate = 0
         option = [ vim.option.OptionValue() ]

         class DpmBehavior(Enum):
            manual = 0
            automated = 1

      class DpmHostConfigInfo(vmodl.DynamicData):
         key = vim.HostSystem()
         enabled = False
         behavior = vim.cluster.DpmConfigInfo.DpmBehavior()

      class DrsConfigInfo(vmodl.DynamicData):
         enabled = False
         enableVmBehaviorOverrides = False
         defaultVmBehavior = vim.cluster.DrsConfigInfo.DrsBehavior()
         vmotionRate = 0
         scaleDescendantsShares = ""
         option = [ vim.option.OptionValue() ]

         class DrsBehavior(Enum):
            manual = 0
            partiallyAutomated = 1
            fullyAutomated = 2

      class DrsFaults(vmodl.DynamicData):
         reason = ""
         faultsByVm = [ vim.cluster.DrsFaults.FaultsByVm() ]

         class FaultsByVm(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            fault = [ vmodl.MethodFault() ]

         class FaultsByVirtualDisk(vim.cluster.DrsFaults.FaultsByVm):
            disk = vim.vm.device.VirtualDiskId()

      class DrsMigration(vmodl.DynamicData):
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

      class DrsRecommendation(vmodl.DynamicData):
         key = ""
         rating = 0
         reason = ""
         reasonText = ""
         migrationList = [ vim.cluster.DrsMigration() ]

         class ReasonCode(Enum):
            fairnessCpuAvg = 0
            fairnessMemAvg = 1
            jointAffin = 2
            antiAffin = 3
            hostMaint = 4

      class DrsVmConfigInfo(vmodl.DynamicData):
         key = vim.VirtualMachine()
         enabled = False
         behavior = vim.cluster.DrsConfigInfo.DrsBehavior()

      class EVCManager(vim.ExtensibleManagedObject):
         managedCluster = vim.ClusterComputeResource()
         evcState = vim.cluster.EVCManager.EVCState()

         def configureEvc(evcModeKey=""):
            # throws vim.fault.EVCConfigFault
            return vim.Task()

         def disableEvc():
            return vim.Task()

         def checkConfigureEvc(evcModeKey=""):
            return vim.Task()

         def checkAddHostEvc(cnxSpec=vim.host.ConnectSpec()):
            # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
            return vim.Task()

         class EVCState(vmodl.DynamicData):
            supportedEVCMode = [ vim.EVCMode() ]
            currentEVCModeKey = ""
            guaranteedCPUFeatures = [ vim.host.CpuIdInfo() ]
            featureCapability = [ vim.host.FeatureCapability() ]
            featureMask = [ vim.host.FeatureMask() ]
            featureRequirement = [ vim.vm.FeatureRequirement() ]

         class CheckResult(vmodl.DynamicData):
            evcModeKey = ""
            error = vmodl.MethodFault()
            host = [ vim.HostSystem() ]

      class EnterMaintenanceResult(vmodl.DynamicData):
         recommendations = [ vim.cluster.Recommendation() ]
         fault = vim.cluster.DrsFaults()

      class FailoverHostAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy):
         failoverHosts = [ vim.HostSystem() ]
         failoverLevel = 0

      class FailoverLevelAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo):
         currentFailoverLevel = 0

      class FailoverLevelAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy):
         failoverLevel = 0
         slotPolicy = vim.cluster.SlotPolicy()

      class FailoverResourcesAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo):
         currentCpuFailoverResourcesPercent = 0
         currentMemoryFailoverResourcesPercent = 0

      class FailoverResourcesAdmissionControlPolicy(vim.cluster.DasAdmissionControlPolicy):
         cpuFailoverResourcesPercent = 0
         memoryFailoverResourcesPercent = 0
         failoverLevel = 0
         autoComputePercentages = False

      class GroupInfo(vmodl.DynamicData):
         name = ""
         userCreated = False
         uniqueID = ""

      class HostGroup(vim.cluster.GroupInfo):
         host = [ vim.HostSystem() ]

      class HostInfraUpdateHaModeAction(vim.cluster.Action):
         operationType = ""

         class OperationType(Enum):
            enterQuarantine = 0
            exitQuarantine = 1
            enterMaintenance = 2

      class HostPowerAction(vim.cluster.Action):
         operationType = vim.cluster.HostPowerAction.OperationType()
         powerConsumptionWatt = 0
         cpuCapacityMHz = 0
         memCapacityMB = 0

         class OperationType(Enum):
            powerOn = 0
            powerOff = 1

      class HostRecommendation(vmodl.DynamicData):
         host = vim.HostSystem()
         rating = 0

      class InfraUpdateHaConfigInfo(vmodl.DynamicData):
         enabled = False
         behavior = ""
         moderateRemediation = ""
         severeRemediation = ""
         providers = [ "" ]

         class BehaviorType(Enum):
            Manual = 0
            Automated = 1

         class RemediationType(Enum):
            QuarantineMode = 0
            MaintenanceMode = 1

      class InitialPlacementAction(vim.cluster.Action):
         targetHost = vim.HostSystem()
         pool = vim.ResourcePool()

      class MigrationAction(vim.cluster.Action):
         drsMigration = vim.cluster.DrsMigration()

      class NotAttemptedVmInfo(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         fault = vmodl.MethodFault()

      class OrchestrationInfo(vmodl.DynamicData):
         defaultVmReadiness = vim.cluster.VmReadiness()

      class PlacementAction(vim.cluster.Action):
         vm = vim.VirtualMachine()
         targetHost = vim.HostSystem()
         relocateSpec = vim.vm.RelocateSpec()

      class PlacementResult(vmodl.DynamicData):
         recommendations = [ vim.cluster.Recommendation() ]
         drsFault = vim.cluster.DrsFaults()

      class PowerOnVmOption(Enum):
         OverrideAutomationLevel = 0
         ReserveResources = 1

      class PowerOnVmResult(vmodl.DynamicData):
         attempted = [ vim.cluster.AttemptedVmInfo() ]
         notAttempted = [ vim.cluster.NotAttemptedVmInfo() ]
         recommendations = [ vim.cluster.Recommendation() ]

      class ProactiveDrsConfigInfo(vmodl.DynamicData):
         enabled = False

      class Recommendation(vmodl.DynamicData):
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

         class RecommendationType(Enum):
            V1 = 0

         class ReasonCode(Enum):
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

      class ResourceUsageSummary(vmodl.DynamicData):
         cpuUsedMHz = 0
         cpuCapacityMHz = 0
         memUsedMB = 0
         memCapacityMB = 0
         pMemAvailableMB = 0
         pMemCapacityMB = 0
         storageUsedMB = 0
         storageCapacityMB = 0

      class SlotPolicy(vmodl.DynamicData):
         pass

      class UsageSummary(vmodl.DynamicData):
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

      class VmComponentProtectionSettings(vmodl.DynamicData):
         vmStorageProtectionForAPD = ""
         enableAPDTimeoutForHosts = False
         vmTerminateDelayForAPDSec = 0
         vmReactionOnAPDCleared = ""
         vmStorageProtectionForPDL = ""

         class StorageVmReaction(Enum):
            disabled = 0
            warning = 1
            restartConservative = 2
            restartAggressive = 3
            clusterDefault = 4

         class VmReactionOnAPDCleared(Enum):
            none = 0
            reset = 1
            useClusterDefault = 2

      class VmGroup(vim.cluster.GroupInfo):
         vm = [ vim.VirtualMachine() ]

      class VmOrchestrationInfo(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         vmReadiness = vim.cluster.VmReadiness()

      class VmReadiness(vmodl.DynamicData):
         readyCondition = ""
         postReadyDelay = 0

         class ReadyCondition(Enum):
            none = 0
            poweredOn = 1
            guestHbStatusGreen = 2
            appHbStatusGreen = 3
            useClusterDefault = 4

      class VmToolsMonitoringSettings(vmodl.DynamicData):
         enabled = False
         vmMonitoring = ""
         clusterSettings = False
         failureInterval = 0
         minUpTime = 0
         maxFailures = 0
         maxFailureWindow = 0

      class DasAamHostInfo(vim.cluster.DasHostInfo):
         hostDasState = [ vim.cluster.DasAamNodeState() ]
         primaryHosts = [ "" ]

      class DasVmConfigSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.DasVmConfigInfo()

      class DpmHostConfigSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.DpmHostConfigInfo()

      class DrsVmConfigSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.DrsVmConfigInfo()

      class FailoverHostAdmissionControlInfo(vim.cluster.DasAdmissionControlInfo):
         hostStatus = [ vim.cluster.FailoverHostAdmissionControlInfo.HostStatus() ]

         class HostStatus(vmodl.DynamicData):
            host = vim.HostSystem()
            status = vim.ManagedEntity.Status()

      class FixedSizeSlotPolicy(vim.cluster.SlotPolicy):
         cpu = 0
         memory = 0

      class GroupSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.GroupInfo()

      class PlacementSpec(vmodl.DynamicData):
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

         class PlacementType(Enum):
            create = 0
            reconfigure = 1
            relocate = 2
            clone = 3

      class RuleInfo(vmodl.DynamicData):
         key = 0
         status = vim.ManagedEntity.Status()
         enabled = False
         name = ""
         mandatory = False
         userCreated = False
         inCompliance = False
         ruleUuid = ""

      class RuleSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.RuleInfo()

      class VmHostRuleInfo(vim.cluster.RuleInfo):
         vmGroupName = ""
         affineHostGroupName = ""
         antiAffineHostGroupName = ""

      class VmOrchestrationSpec(vim.option.ArrayUpdateSpec):
         info = vim.cluster.VmOrchestrationInfo()

      class AffinityRuleSpec(vim.cluster.RuleInfo):
         vm = [ vim.VirtualMachine() ]

      class AntiAffinityRuleSpec(vim.cluster.RuleInfo):
         vm = [ vim.VirtualMachine() ]

      class ConfigInfoEx(vim.ComputeResource.ConfigInfo):
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

      class ConfigSpecEx(vim.ComputeResource.ConfigSpec):
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

      class DependencyRuleInfo(vim.cluster.RuleInfo):
         vmGroup = ""
         dependsOnVmGroup = ""

   class dvs(object):

      class DistributedVirtualPort(vmodl.DynamicData):
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

         class ConfigSpec(vmodl.DynamicData):
            operation = ""
            key = ""
            name = ""
            scope = [ vim.ManagedEntity() ]
            description = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            configVersion = ""

         class ConfigInfo(vmodl.DynamicData):
            name = ""
            scope = [ vim.ManagedEntity() ]
            description = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            configVersion = ""

         class TrafficShapingPolicy(vim.InheritablePolicy):
            enabled = vim.BoolPolicy()
            averageBandwidth = vim.LongPolicy()
            peakBandwidth = vim.LongPolicy()
            burstSize = vim.LongPolicy()

         class HostLocalPortInfo(vmodl.DynamicData):
            switchUuid = ""
            portKey = ""
            setting = vim.dvs.DistributedVirtualPort.Setting()
            vnic = ""

         class VendorSpecificConfig(vim.InheritablePolicy):
            keyValue = [ vim.dvs.KeyedOpaqueBlob() ]

         class FilterParameter(vmodl.DynamicData):
            parameters = [ "" ]

         class FilterOnFailure(Enum):
            failOpen = 0
            failClosed = 1

         class FilterConfig(vim.InheritablePolicy):
            key = ""
            agentName = ""
            slotNumber = ""
            parameters = vim.dvs.DistributedVirtualPort.FilterParameter()
            onFailure = ""

         class TrafficFilterConfig(vim.dvs.DistributedVirtualPort.FilterConfig):
            trafficRuleset = vim.dvs.TrafficRuleset()

         class FilterConfigSpec(vim.dvs.DistributedVirtualPort.FilterConfig):
            operation = ""

         class TrafficFilterConfigSpec(vim.dvs.DistributedVirtualPort.TrafficFilterConfig):
            operation = ""

         class FilterPolicy(vim.InheritablePolicy):
            filterConfig = [ vim.dvs.DistributedVirtualPort.FilterConfig() ]

         class Setting(vmodl.DynamicData):
            blocked = vim.BoolPolicy()
            vmDirectPathGen2Allowed = vim.BoolPolicy()
            inShapingPolicy = vim.dvs.DistributedVirtualPort.TrafficShapingPolicy()
            outShapingPolicy = vim.dvs.DistributedVirtualPort.TrafficShapingPolicy()
            vendorSpecificConfig = vim.dvs.DistributedVirtualPort.VendorSpecificConfig()
            networkResourcePoolKey = vim.StringPolicy()
            filterPolicy = vim.dvs.DistributedVirtualPort.FilterPolicy()

         class RuntimeInfo(vmodl.DynamicData):
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

            class VmDirectPathGen2InactiveReasonNetwork(Enum):
               portNptIncompatibleDvs = 0
               portNptNoCompatibleNics = 1
               portNptNoVirtualFunctionsAvailable = 2
               portNptDisabledForPort = 3

            class VmDirectPathGen2InactiveReasonOther(Enum):
               portNptIncompatibleHost = 0
               portNptIncompatibleConnectee = 1

         class State(vmodl.DynamicData):
            runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
            stats = vim.dvs.PortStatistics()
            vendorSpecificState = [ vim.dvs.KeyedOpaqueBlob() ]

      class DistributedVirtualPortgroupInfo(vmodl.DynamicData):
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

      class DistributedVirtualPortgroupSelection(vim.SelectionSet):
         dvsUuid = ""
         portgroupKey = [ "" ]

      class DistributedVirtualSwitchInfo(vmodl.DynamicData):
         switchName = ""
         switchUuid = ""
         distributedVirtualSwitch = vim.DistributedVirtualSwitch()
         networkReservationSupported = False

      class DistributedVirtualSwitchSelection(vim.SelectionSet):
         dvsUuid = ""

      class EntityBackup(vmodl.DynamicData):

         class Config(vmodl.DynamicData):
            entityType = ""
            configBlob = vmodl.Binary()
            key = ""
            name = ""
            container = vim.ManagedEntity()
            configVersion = ""

         class EntityType(Enum):
            distributedVirtualSwitch = 0
            distributedVirtualPortgroup = 1

         class ImportType(Enum):
            createEntityWithNewIdentifier = 0
            createEntityWithOriginalIdentifier = 1
            applyToEntitySpecified = 2

      class HostMember(vmodl.DynamicData):
         runtimeState = vim.dvs.HostMember.RuntimeState()
         config = vim.dvs.HostMember.ConfigInfo()
         productInfo = vim.dvs.ProductSpec()
         uplinkPortKey = [ "" ]
         status = ""
         statusDetail = ""

         class HostComponentState(Enum):
            up = 0
            pending = 1
            outOfSync = 2
            warning = 3
            disconnected = 4
            down = 5

         class ConfigSpec(vmodl.DynamicData):
            operation = ""
            host = vim.HostSystem()
            backing = vim.dvs.HostMember.Backing()
            maxProxySwitchPorts = 0
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]

         class PnicSpec(vmodl.DynamicData):
            pnicDevice = ""
            uplinkPortKey = ""
            uplinkPortgroupKey = ""
            connectionCookie = 0

         class Backing(vmodl.DynamicData):
            pass

         class PnicBacking(vim.dvs.HostMember.Backing):
            pnicSpec = [ vim.dvs.HostMember.PnicSpec() ]

         class RuntimeState(vmodl.DynamicData):
            currentMaxProxySwitchPorts = 0

         class TransportZoneType(Enum):
            vlan = 0
            overlay = 1

         class TransportZoneInfo(vmodl.DynamicData):
            uuid = ""
            type = ""

         class ConfigInfo(vmodl.DynamicData):
            host = vim.HostSystem()
            maxProxySwitchPorts = 0
            vendorSpecificConfig = [ vim.dvs.KeyedOpaqueBlob() ]
            backing = vim.dvs.HostMember.Backing()
            nsxSwitch = False
            ensEnabled = False
            ensInterruptEnabled = False
            transportZones = [ vim.dvs.HostMember.TransportZoneInfo() ]
            nsxtUsedUplinkNames = [ "" ]

         class RuntimeInfo(vmodl.DynamicData):
            host = vim.HostSystem()
            status = ""
            statusDetail = ""
            nsxtStatus = ""
            nsxtStatusDetail = ""
            healthCheckResult = [ vim.dvs.HostMember.HealthCheckResult() ]

         class HealthCheckResult(vmodl.DynamicData):
            summary = ""

         class UplinkHealthCheckResult(vim.dvs.HostMember.HealthCheckResult):
            uplinkPortKey = ""

      class HostProductSpec(vmodl.DynamicData):
         productLineId = ""
         version = ""

      class KeyedOpaqueBlob(vmodl.DynamicData):
         key = ""
         opaqueData = ""

      class NetworkResourcePool(vmodl.DynamicData):
         key = ""
         name = ""
         description = ""
         configVersion = ""
         allocationInfo = vim.dvs.NetworkResourcePool.AllocationInfo()

         class AllocationInfo(vmodl.DynamicData):
            limit = 0
            shares = vim.SharesInfo()
            priorityTag = 0

         class ConfigSpec(vmodl.DynamicData):
            key = ""
            configVersion = ""
            allocationInfo = vim.dvs.NetworkResourcePool.AllocationInfo()
            name = ""
            description = ""

      class PortConnectee(vmodl.DynamicData):
         connectedEntity = vim.ManagedEntity()
         nicKey = ""
         type = ""
         addressHint = ""

         class ConnecteeType(Enum):
            pnic = 0
            vmVnic = 1
            hostConsoleVnic = 2
            hostVmkVnic = 3

      class PortConnection(vmodl.DynamicData):
         switchUuid = ""
         portgroupKey = ""
         portKey = ""
         connectionCookie = 0

      class PortCriteria(vmodl.DynamicData):
         connected = False
         active = False
         uplinkPort = False
         nsxPort = False
         scope = vim.ManagedEntity()
         portgroupKey = [ "" ]
         inside = False
         portKey = [ "" ]
         host = [ vim.HostSystem() ]

      class PortStatistics(vmodl.DynamicData):
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

      class ProductSpec(vmodl.DynamicData):
         name = ""
         vendor = ""
         version = ""
         build = ""
         forwardingClass = ""
         bundleId = ""
         bundleUrl = ""

      class TrafficRule(vmodl.DynamicData):
         key = ""
         description = ""
         sequence = 0
         qualifier = [ vim.dvs.TrafficRule.Qualifier() ]
         action = vim.dvs.TrafficRule.Action()
         direction = ""

         class Qualifier(vmodl.DynamicData):
            key = ""

         class Action(vmodl.DynamicData):
            pass

         class RuleDirectionType(Enum):
            incomingPackets = 0
            outgoingPackets = 1
            both = 2

         class IpQualifier(vim.dvs.TrafficRule.Qualifier):
            sourceAddress = vim.IpAddress()
            destinationAddress = vim.IpAddress()
            protocol = vim.IntExpression()
            sourceIpPort = vim.dvs.TrafficRule.IpPort()
            destinationIpPort = vim.dvs.TrafficRule.IpPort()
            tcpFlags = vim.IntExpression()

         class IpPort(vim.NegatableExpression):
            pass

         class SingleIpPort(vim.dvs.TrafficRule.IpPort):
            portNumber = 0

         class IpPortRange(vim.dvs.TrafficRule.IpPort):
            startPortNumber = 0
            endPortNumber = 0

         class MacQualifier(vim.dvs.TrafficRule.Qualifier):
            sourceAddress = vim.MacAddress()
            destinationAddress = vim.MacAddress()
            protocol = vim.IntExpression()
            vlanId = vim.IntExpression()

         class SystemTrafficQualifier(vim.dvs.TrafficRule.Qualifier):
            typeOfSystemTraffic = vim.StringExpression()

         class DropAction(vim.dvs.TrafficRule.Action):
            pass

         class AcceptAction(vim.dvs.TrafficRule.Action):
            pass

         class UpdateTagAction(vim.dvs.TrafficRule.Action):
            qosTag = 0
            dscpTag = 0

         class RateLimitAction(vim.dvs.TrafficRule.Action):
            packetsPerSecond = 0

         class LogAction(vim.dvs.TrafficRule.Action):
            pass

         class GreAction(vim.dvs.TrafficRule.Action):
            encapsulationIp = vim.SingleIp()

         class MacRewriteAction(vim.dvs.TrafficRule.Action):
            rewriteMac = ""

         class PuntAction(vim.dvs.TrafficRule.Action):
            pass

         class CopyAction(vim.dvs.TrafficRule.Action):
            pass

      class TrafficRuleset(vmodl.DynamicData):
         key = ""
         enabled = False
         precedence = 0
         rules = [ vim.dvs.TrafficRule() ]

      class VmVnicNetworkResourcePool(vmodl.DynamicData):
         key = ""
         name = ""
         description = ""
         configVersion = ""
         allocationInfo = vim.dvs.VmVnicNetworkResourcePool.ResourceAllocation()

         class ResourceAllocation(vmodl.DynamicData):
            reservationQuota = 0

         class ConfigSpec(vmodl.DynamicData):
            operation = ""
            key = ""
            configVersion = ""
            allocationInfo = vim.dvs.VmVnicNetworkResourcePool.ResourceAllocation()
            name = ""
            description = ""

         class VnicAllocatedResource(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            vnicKey = ""
            reservation = 0

         class RuntimeInfo(vmodl.DynamicData):
            key = ""
            name = ""
            capacity = 0
            usage = 0
            available = 0
            status = ""
            allocatedResource = [ vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource() ]

      class DistributedVirtualPortgroup(vim.Network):
         key = ""
         config = vim.dvs.DistributedVirtualPortgroup.ConfigInfo()
         portKeys = [ "" ]

         def reconfigure(spec=vim.dvs.DistributedVirtualPortgroup.ConfigSpec()):
            # throws vim.fault.DvsFault, vim.fault.ConcurrentAccess, vim.fault.DuplicateName, vim.fault.InvalidName
            return vim.Task()

         def rollback(entityBackup=vim.dvs.EntityBackup.Config() or None):
            # throws vim.fault.DvsFault, vim.fault.RollbackFailure
            return vim.Task()

         class PortgroupType(Enum):
            earlyBinding = 0
            lateBinding = 1
            ephemeral = 2

         class BackingType(Enum):
            standard = 0
            nsx = 1

         class PortgroupPolicy(vmodl.DynamicData):
            blockOverrideAllowed = False
            shapingOverrideAllowed = False
            vendorConfigOverrideAllowed = False
            livePortMovingAllowed = False
            portConfigResetAtDisconnect = False
            networkResourcePoolOverrideAllowed = False
            trafficFilterOverrideAllowed = False

         class MetaTagName(Enum):
            dvsName = 0
            portgroupName = 1
            portIndex = 2

         class ConfigSpec(vmodl.DynamicData):
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

         class ConfigInfo(vmodl.DynamicData):
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

         class Problem(vmodl.DynamicData):
            logicalSwitchUuid = ""
            fault = vmodl.MethodFault()

         class NsxPortgroupOperationResult(vmodl.DynamicData):
            portgroups = [ vim.dvs.DistributedVirtualPortgroup() ]
            problems = [ vim.dvs.DistributedVirtualPortgroup.Problem() ]

      class DistributedVirtualSwitchManager(vmodl.ManagedObject):

         def querySupportedSwitchSpec(recommended=False or None):
            return [ vim.dvs.ProductSpec() ]

         def queryCompatibleHostForNewDvs(container=vim.ManagedEntity(), recursive=False, switchProductSpec=vim.dvs.ProductSpec() or None):
            return [ vim.HostSystem() ]

         def queryCompatibleHostForExistingDvs(container=vim.ManagedEntity(), recursive=False, dvs=vim.DistributedVirtualSwitch()):
            return [ vim.HostSystem() ]

         def queryCompatibleHostSpec(switchProductSpec=vim.dvs.ProductSpec() or None):
            return [ vim.dvs.HostProductSpec() ]

         def queryFeatureCapability(switchProductSpec=vim.dvs.ProductSpec() or None):
            return vim.DistributedVirtualSwitch.FeatureCapability()

         def querySwitchByUuid(uuid=""):
            # throws vim.fault.NotFound
            return vim.DistributedVirtualSwitch()

         def queryDvsConfigTarget(host=vim.HostSystem() or None, dvs=vim.DistributedVirtualSwitch() or None):
            return vim.dvs.DistributedVirtualSwitchManager.DvsConfigTarget()

         def checkCompatibility(hostContainer=vim.dvs.DistributedVirtualSwitchManager.HostContainer(), dvsProductSpec=vim.dvs.DistributedVirtualSwitchManager.DvsProductSpec() or None, hostFilterSpec=[ vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec() ] or None):
            return [ vim.dvs.DistributedVirtualSwitchManager.CompatibilityResult() ]

         def rectifyHost(hosts=[ vim.HostSystem() ]):
            # throws vim.fault.DvsFault
            return vim.Task()

         def exportEntity(selectionSet=[ vim.SelectionSet() ]):
            # throws vim.fault.NotFound, vim.fault.BackupBlobWriteFailure
            return vim.Task()

         def importEntity(entityBackup=[ vim.dvs.EntityBackup.Config() ], importType=""):
            # throws vim.fault.DvsFault, vim.fault.NotFound
            return vim.Task()

         def lookupPortgroup(switchUuid="", portgroupKey=""):
            # throws vim.fault.NotFound
            return vim.dvs.DistributedVirtualPortgroup()

         class DvsConfigTarget(vmodl.DynamicData):
            distributedVirtualPortgroup = [ vim.dvs.DistributedVirtualPortgroupInfo() ]
            distributedVirtualSwitch = [ vim.dvs.DistributedVirtualSwitchInfo() ]

         class CompatibilityResult(vmodl.DynamicData):
            host = vim.HostSystem()
            error = [ vmodl.MethodFault() ]

         class HostContainer(vmodl.DynamicData):
            container = vim.ManagedEntity()
            recursive = False

         class HostDvsFilterSpec(vmodl.DynamicData):
            inclusive = False

         class HostArrayFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec):
            host = [ vim.HostSystem() ]

         class HostContainerFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec):
            hostContainer = vim.dvs.DistributedVirtualSwitchManager.HostContainer()

         class HostDvsMembershipFilter(vim.dvs.DistributedVirtualSwitchManager.HostDvsFilterSpec):
            distributedVirtualSwitch = vim.DistributedVirtualSwitch()

         class DvsProductSpec(vmodl.DynamicData):
            newSwitchProductSpec = vim.dvs.ProductSpec()
            distributedVirtualSwitch = vim.DistributedVirtualSwitch()

         class ImportResult(vmodl.DynamicData):
            distributedVirtualSwitch = [ vim.DistributedVirtualSwitch() ]
            distributedVirtualPortgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
            importFault = [ vim.fault.ImportOperationBulkFault.FaultOnImport() ]

      class VmwareDistributedVirtualSwitch(vim.DistributedVirtualSwitch):

         def updateLacpGroupConfig(lacpGroupSpec=[ vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec() ]):
            # throws vim.fault.DvsFault
            return vim.Task()

         class FeatureCapability(vim.DistributedVirtualSwitch.FeatureCapability):
            vspanSupported = False
            lldpSupported = False
            ipfixSupported = False
            ipfixCapability = vim.dvs.VmwareDistributedVirtualSwitch.IpfixFeatureCapability()
            multicastSnoopingSupported = False
            vspanCapability = vim.dvs.VmwareDistributedVirtualSwitch.VspanFeatureCapability()
            lacpCapability = vim.dvs.VmwareDistributedVirtualSwitch.LacpFeatureCapability()
            nsxSupported = False

         class IpfixFeatureCapability(vmodl.DynamicData):
            ipfixSupported = False
            ipv6ForIpfixSupported = False
            observationDomainIdSupported = False

         class LacpFeatureCapability(vmodl.DynamicData):
            lacpSupported = False
            multiLacpGroupSupported = False

         class VmwareHealthCheckFeatureCapability(vim.DistributedVirtualSwitch.HealthCheckFeatureCapability):
            vlanMtuSupported = False
            teamingSupported = False

         class VspanFeatureCapability(vmodl.DynamicData):
            mixedDestSupported = False
            dvportSupported = False
            remoteSourceSupported = False
            remoteDestSupported = False
            encapRemoteSourceSupported = False
            erspanProtocolSupported = False
            mirrorNetstackSupported = False

         class VspanPorts(vmodl.DynamicData):
            portKey = [ "" ]
            uplinkPortName = [ "" ]
            wildcardPortConnecteeType = [ "" ]
            vlans = [ 0 ]
            ipAddress = [ "" ]

         class VspanSession(vmodl.DynamicData):
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

         class IpfixConfig(vmodl.DynamicData):
            collectorIpAddress = ""
            collectorPort = 0
            observationDomainId = 0
            activeFlowTimeout = 0
            idleFlowTimeout = 0
            samplingRate = 0
            internalFlowsOnly = False

         class ConfigInfo(vim.DistributedVirtualSwitch.ConfigInfo):
            vspanSession = [ vim.dvs.VmwareDistributedVirtualSwitch.VspanSession() ]
            pvlanConfig = [ vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry() ]
            maxMtu = 0
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()
            ipfixConfig = vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig()
            lacpGroupConfig = [ vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig() ]
            lacpApiVersion = ""
            multicastFilteringMode = ""

         class ConfigSpec(vim.DistributedVirtualSwitch.ConfigSpec):
            pvlanConfigSpec = [ vim.dvs.VmwareDistributedVirtualSwitch.PvlanConfigSpec() ]
            vspanConfigSpec = [ vim.dvs.VmwareDistributedVirtualSwitch.VspanConfigSpec() ]
            maxMtu = 0
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()
            ipfixConfig = vim.dvs.VmwareDistributedVirtualSwitch.IpfixConfig()
            lacpApiVersion = ""
            multicastFilteringMode = ""

         class UplinkPortOrderPolicy(vim.InheritablePolicy):
            activeUplinkPort = [ "" ]
            standbyUplinkPort = [ "" ]

         class FailureCriteria(vim.InheritablePolicy):
            checkSpeed = vim.StringPolicy()
            speed = vim.IntPolicy()
            checkDuplex = vim.BoolPolicy()
            fullDuplex = vim.BoolPolicy()
            checkErrorPercent = vim.BoolPolicy()
            percentage = vim.IntPolicy()
            checkBeacon = vim.BoolPolicy()

         class UplinkPortTeamingPolicy(vim.InheritablePolicy):
            policy = vim.StringPolicy()
            reversePolicy = vim.BoolPolicy()
            notifySwitches = vim.BoolPolicy()
            rollingOrder = vim.BoolPolicy()
            failureCriteria = vim.dvs.VmwareDistributedVirtualSwitch.FailureCriteria()
            uplinkPortOrder = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy()

         class VlanSpec(vim.InheritablePolicy):
            pass

         class PvlanSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec):
            pvlanId = 0

         class VlanIdSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec):
            vlanId = 0

         class TrunkVlanSpec(vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec):
            vlanId = [ vim.NumericRange() ]

         class SecurityPolicy(vim.InheritablePolicy):
            allowPromiscuous = vim.BoolPolicy()
            macChanges = vim.BoolPolicy()
            forgedTransmits = vim.BoolPolicy()

         class MacLimitPolicyType(Enum):
            allow = 0
            drop = 1

         class MacLearningPolicy(vim.InheritablePolicy):
            enabled = False
            allowUnicastFlooding = False
            limit = 0
            limitPolicy = ""

         class MacManagementPolicy(vim.InheritablePolicy):
            allowPromiscuous = False
            macChanges = False
            forgedTransmits = False
            macLearningPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacLearningPolicy()

         class VmwarePortConfigPolicy(vim.dvs.DistributedVirtualPort.Setting):
            vlan = vim.dvs.VmwareDistributedVirtualSwitch.VlanSpec()
            qosTag = vim.IntPolicy()
            uplinkTeamingPolicy = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy()
            securityPolicy = vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy()
            ipfixEnabled = vim.BoolPolicy()
            txUplink = vim.BoolPolicy()
            lacpPolicy = vim.dvs.VmwareDistributedVirtualSwitch.UplinkLacpPolicy()
            macManagementPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacManagementPolicy()
            VNI = vim.IntPolicy()

         class VMwarePortgroupPolicy(vim.dvs.DistributedVirtualPortgroup.PortgroupPolicy):
            vlanOverrideAllowed = False
            uplinkTeamingOverrideAllowed = False
            securityPolicyOverrideAllowed = False
            ipfixOverrideAllowed = False
            macManagementOverrideAllowed = False

         class PvlanPortType(Enum):
            promiscuous = 0
            isolated = 1
            community = 2

         class PvlanConfigSpec(vmodl.DynamicData):
            pvlanEntry = vim.dvs.VmwareDistributedVirtualSwitch.PvlanMapEntry()
            operation = ""

         class PvlanMapEntry(vmodl.DynamicData):
            primaryVlanId = 0
            secondaryVlanId = 0
            pvlanType = ""

         class VspanConfigSpec(vmodl.DynamicData):
            vspanSession = vim.dvs.VmwareDistributedVirtualSwitch.VspanSession()
            operation = ""

         class VspanSessionEncapType(Enum):
            gre = 0
            erspan2 = 1
            erspan3 = 2

         class VspanSessionType(Enum):
            mixedDestMirror = 0
            dvPortMirror = 1
            remoteMirrorSource = 2
            remoteMirrorDest = 3
            encapsulatedRemoteMirrorSource = 4

         class VmwareHealthCheckConfig(vim.DistributedVirtualSwitch.HealthCheckConfig):
            pass

         class VlanMtuHealthCheckConfig(vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig):
            pass

         class TeamingHealthCheckConfig(vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig):
            pass

         class VlanHealthCheckResult(vim.dvs.HostMember.UplinkHealthCheckResult):
            trunkedVlan = [ vim.NumericRange() ]
            untrunkedVlan = [ vim.NumericRange() ]

         class MtuHealthCheckResult(vim.dvs.HostMember.UplinkHealthCheckResult):
            mtuMismatch = False
            vlanSupportSwitchMtu = [ vim.NumericRange() ]
            vlanNotSupportSwitchMtu = [ vim.NumericRange() ]

         class TeamingMatchStatus(Enum):
            iphashMatch = 0
            nonIphashMatch = 1
            iphashMismatch = 2
            nonIphashMismatch = 3

         class TeamingHealthCheckResult(vim.dvs.HostMember.HealthCheckResult):
            teamingStatus = ""

         class UplinkLacpPolicy(vim.InheritablePolicy):
            enable = vim.BoolPolicy()
            mode = vim.StringPolicy()

         class LacpGroupConfig(vmodl.DynamicData):
            key = ""
            name = ""
            mode = ""
            uplinkNum = 0
            loadbalanceAlgorithm = ""
            vlan = vim.dvs.VmwareDistributedVirtualSwitch.LagVlanConfig()
            ipfix = vim.dvs.VmwareDistributedVirtualSwitch.LagIpfixConfig()
            uplinkName = [ "" ]
            uplinkPortKey = [ "" ]

         class LagVlanConfig(vmodl.DynamicData):
            vlanId = [ vim.NumericRange() ]

         class LagIpfixConfig(vmodl.DynamicData):
            ipfixEnabled = False

         class UplinkLacpMode(Enum):
            active = 0
            passive = 1

         class LacpGroupSpec(vmodl.DynamicData):
            lacpGroupConfig = vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupConfig()
            operation = ""

         class LacpLoadBalanceAlgorithm(Enum):
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

         class LacpApiVersion(Enum):
            singleLag = 0
            multipleLag = 1

         class MulticastFilteringMode(Enum):
            legacyFiltering = 0
            snooping = 1

   class encryption(object):

      class CryptoKeyId(vmodl.DynamicData):
         keyId = ""
         providerId = vim.encryption.KeyProviderId()

      class CryptoKeyPlain(vmodl.DynamicData):
         keyId = vim.encryption.CryptoKeyId()
         algorithm = ""
         keyData = ""

      class CryptoKeyResult(vmodl.DynamicData):
         keyId = vim.encryption.CryptoKeyId()
         success = False
         reason = ""

      class CryptoManager(vmodl.ManagedObject):
         enabled = False

         def addKey(key=vim.encryption.CryptoKeyPlain()):
            # throws vim.fault.AlreadyExists, vim.fault.InvalidState
            return None

         def addKeys(keys=[ vim.encryption.CryptoKeyPlain() ] or None):
            # throws vim.fault.InvalidState
            return [ vim.encryption.CryptoKeyResult() ]

         def removeKey(key=vim.encryption.CryptoKeyId(), force=False):
            # throws vim.fault.ResourceInUse
            return None

         def removeKeys(keys=[ vim.encryption.CryptoKeyId() ] or None, force=False):
            return [ vim.encryption.CryptoKeyResult() ]

         def listKeys(limit=0 or None):
            return [ vim.encryption.CryptoKeyId() ]

      class CryptoManagerHost(vim.encryption.CryptoManager):

         def prepare():
            # throws vim.fault.InvalidState
            return None

         def enable(initialKey=vim.encryption.CryptoKeyPlain()):
            # throws vim.fault.InvalidState, vim.fault.AlreadyExists
            return None

         def changeKey(newKey=vim.encryption.CryptoKeyPlain()):
            # throws vim.fault.InvalidState
            return vim.Task()

         def disable():
            # throws vim.fault.InvalidState
            return None

      class CryptoManagerHostKMS(vim.encryption.CryptoManagerHost):
         pass

      class CryptoSpec(vmodl.DynamicData):
         pass

      class CryptoSpecDecrypt(vim.encryption.CryptoSpec):
         pass

      class CryptoSpecDeepRecrypt(vim.encryption.CryptoSpec):
         newKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecEncrypt(vim.encryption.CryptoSpec):
         cryptoKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecNoOp(vim.encryption.CryptoSpec):
         pass

      class CryptoSpecRegister(vim.encryption.CryptoSpecNoOp):
         cryptoKeyId = vim.encryption.CryptoKeyId()

      class CryptoSpecShallowRecrypt(vim.encryption.CryptoSpec):
         newKeyId = vim.encryption.CryptoKeyId()

      class KeyProviderId(vmodl.DynamicData):
         id = ""

      class KmipClusterInfo(vmodl.DynamicData):
         clusterId = vim.encryption.KeyProviderId()
         servers = [ vim.encryption.KmipServerInfo() ]
         useAsDefault = False
         managementType = ""
         useAsEntityDefault = [ vim.ManagedEntity() ]

         class KmsManagementType(Enum):
            unknown = 0
            vCenter = 1
            trustAuthority = 2

      class KmipServerInfo(vmodl.DynamicData):
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

      class KmipServerSpec(vmodl.DynamicData):
         clusterId = vim.encryption.KeyProviderId()
         info = vim.encryption.KmipServerInfo()
         password = ""

      class CryptoManagerKmip(vim.encryption.CryptoManager):
         kmipServers = [ vim.encryption.KmipClusterInfo() ]

         def registerKmipServer(server=vim.encryption.KmipServerSpec()):
            return None

         def markDefault(clusterId=vim.encryption.KeyProviderId()):
            return None

         def updateKmipServer(server=vim.encryption.KmipServerSpec()):
            return None

         def removeKmipServer(clusterId=vim.encryption.KeyProviderId(), serverName=""):
            return None

         def listKmipServers(limit=0 or None):
            return [ vim.encryption.KmipClusterInfo() ]

         def retrieveKmipServersStatus(clusters=[ vim.encryption.KmipClusterInfo() ] or None):
            return vim.Task()

         def generateKey(keyProvider=vim.encryption.KeyProviderId() or None):
            return vim.encryption.CryptoKeyResult()

         def retrieveKmipServerCert(keyProvider=vim.encryption.KeyProviderId(), server=vim.encryption.KmipServerInfo()):
            return vim.encryption.CryptoManagerKmip.ServerCertInfo()

         def uploadKmipServerCert(cluster=vim.encryption.KeyProviderId(), certificate=""):
            return None

         def generateSelfSignedClientCert(cluster=vim.encryption.KeyProviderId()):
            return ""

         def generateClientCsr(cluster=vim.encryption.KeyProviderId()):
            return ""

         def retrieveSelfSignedClientCert(cluster=vim.encryption.KeyProviderId()):
            return ""

         def retrieveClientCsr(cluster=vim.encryption.KeyProviderId()):
            return ""

         def retrieveClientCert(cluster=vim.encryption.KeyProviderId()):
            return ""

         def updateSelfSignedClientCert(cluster=vim.encryption.KeyProviderId(), certificate=""):
            return None

         def updateKmsSignedCsrClientCert(cluster=vim.encryption.KeyProviderId(), certificate=""):
            return None

         def uploadClientCert(cluster=vim.encryption.KeyProviderId(), certificate="", privateKey=""):
            return None

         def IsKmsClusterActive(cluster=vim.encryption.KeyProviderId() or None):
            # throws vmodl.fault.InvalidArgument
            return False

         def setDefaultKmsCluster(entity=vim.ManagedEntity() or None, clusterId=vim.encryption.KeyProviderId() or None):
            return None

         def getDefaultKmsCluster(entity=vim.ManagedEntity() or None, defaultsToParent=False or None):
            return vim.encryption.KeyProviderId()

         def queryCryptoKeyStatus(keyIds=[ vim.encryption.CryptoKeyId() ] or None, checkKeyBitMap=0):
            return [ vim.encryption.CryptoManagerKmip.CryptoKeyStatus() ]

         def registerKmsCluster(clusterId=vim.encryption.KeyProviderId(), managementType="" or None):
            return None

         def unregisterKmsCluster(clusterId=vim.encryption.KeyProviderId()):
            return None

         def listKmsClusters(includeKmsServers=False or None, managementTypeFilter=0 or None, statusFilter=0 or None):
            return [ vim.encryption.KmipClusterInfo() ]

         class CertificateInfo(vmodl.DynamicData):
            subject = ""
            issuer = ""
            serialNumber = ""
            notBefore = vmodl.DateTime()
            notAfter = vmodl.DateTime()
            fingerprint = ""
            checkTime = vmodl.DateTime()
            secondsSinceValid = 0
            secondsBeforeExpire = 0

         class ServerStatus(vmodl.DynamicData):
            name = ""
            status = vim.ManagedEntity.Status()
            connectionStatus = ""
            certInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()
            clientTrustServer = False
            serverTrustClient = False

         class ClusterStatus(vmodl.DynamicData):
            clusterId = vim.encryption.KeyProviderId()
            overallStatus = vim.ManagedEntity.Status()
            managementType = ""
            servers = [ vim.encryption.CryptoManagerKmip.ServerStatus() ]
            clientCertInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()

         class ServerCertInfo(vmodl.DynamicData):
            certificate = ""
            certInfo = vim.encryption.CryptoManagerKmip.CertificateInfo()
            clientTrustServer = False

         class CryptoKeyStatus(vmodl.DynamicData):
            keyId = vim.encryption.CryptoKeyId()
            keyAvailable = False
            reason = ""
            encryptedVMs = [ vim.VirtualMachine() ]
            affectedHosts = [ vim.HostSystem() ]
            referencedByTags = [ "" ]

            class KeyUnavailableReason(Enum):
               KeyStateMissingInCache = 0
               KeyStateClusterInvalid = 1
               KeyStateClusterUnreachable = 2
               KeyStateMissingInKMS = 3
               KeyStateNotActiveOrEnabled = 4
               KeyStateManagedByTrustAuthority = 5

      class KmipServerStatus(vmodl.DynamicData):
         clusterId = vim.encryption.KeyProviderId()
         name = ""
         status = vim.ManagedEntity.Status()
         description = ""

   class event(object):

      class ChangesInfoEventArgument(vmodl.DynamicData):
         modified = ""
         added = ""
         deleted = ""

      class DvsOutOfSyncHostArgument(vmodl.DynamicData):
         outOfSyncHost = vim.event.HostEventArgument()
         configParamters = [ "" ]

      class Event(vmodl.DynamicData):
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

         class EventSeverity(Enum):
            error = 0
            warning = 1
            info = 2
            user = 3

      class EventArgument(vmodl.DynamicData):
         pass

      class EventDescription(vmodl.DynamicData):
         category = [ vim.ElementDescription() ]
         eventInfo = [ vim.event.EventDescription.EventDetail() ]
         enumeratedTypes = [ vim.EnumDescription() ]

         class EventCategory(Enum):
            info = 0
            warning = 1
            error = 2
            user = 3

         class EventArgDesc(vmodl.DynamicData):
            name = ""
            type = ""
            description = vim.ElementDescription()

         class EventDetail(vmodl.DynamicData):
            key = vmodl.TypeName()
            description = ""
            category = ""
            formatOnDatacenter = ""
            formatOnComputeResource = ""
            formatOnHost = ""
            formatOnVm = ""
            fullFormat = ""
            longDescription = ""

      class EventEx(vim.event.Event):
         eventTypeId = ""
         severity = ""
         message = ""
         arguments = [ vmodl.KeyAnyValue() ]
         objectId = ""
         objectType = vmodl.TypeName()
         objectName = ""
         fault = vmodl.MethodFault()

      class EventFilterSpec(vmodl.DynamicData):
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

         class RecursionOption(Enum):
            self = 0
            children = 1
            all = 2

         class ByEntity(vmodl.DynamicData):
            entity = vim.ManagedEntity()
            recursion = vim.event.EventFilterSpec.RecursionOption()

         class ByTime(vmodl.DynamicData):
            beginTime = vmodl.DateTime()
            endTime = vmodl.DateTime()

         class ByUsername(vmodl.DynamicData):
            systemUser = False
            userList = [ "" ]

      class EventHistoryCollector(vim.HistoryCollector):
         latestPage = [ vim.event.Event() ]

         def readNext(maxCount=0):
            return [ vim.event.Event() ]

         def readPrev(maxCount=0):
            return [ vim.event.Event() ]

      class EventManager(vmodl.ManagedObject):
         description = vim.event.EventDescription()
         latestEvent = vim.event.Event()
         maxCollector = 0

         def retrieveArgumentDescription(eventTypeId=""):
            return [ vim.event.EventDescription.EventArgDesc() ]

         def createCollector(filter=vim.event.EventFilterSpec()):
            # throws vim.fault.InvalidState
            return vim.event.EventHistoryCollector()

         def logUserEvent(entity=vim.ManagedEntity(), msg=""):
            return None

         def QueryEvent(filter=vim.event.EventFilterSpec()):
            return [ vim.event.Event() ]

         def postEvent(eventToPost=vim.event.Event(), taskInfo=vim.TaskInfo() or None):
            # throws vim.fault.InvalidEvent
            return None

      class GeneralEvent(vim.event.Event):
         message = ""

      class GeneralHostErrorEvent(vim.event.GeneralEvent):
         pass

      class GeneralHostInfoEvent(vim.event.GeneralEvent):
         pass

      class GeneralHostWarningEvent(vim.event.GeneralEvent):
         pass

      class GeneralUserEvent(vim.event.GeneralEvent):
         entity = vim.event.ManagedEntityEventArgument()

      class GeneralVmErrorEvent(vim.event.GeneralEvent):
         pass

      class GeneralVmInfoEvent(vim.event.GeneralEvent):
         pass

      class GeneralVmWarningEvent(vim.event.GeneralEvent):
         pass

      class HealthStatusChangedEvent(vim.event.Event):
         componentId = ""
         oldStatus = ""
         newStatus = ""
         componentName = ""
         serviceId = ""

      class HostEvent(vim.event.Event):
         pass

      class HostGetShortNameFailedEvent(vim.event.HostEvent):
         pass

      class HostInAuditModeEvent(vim.event.HostEvent):
         pass

      class HostInventoryUnreadableEvent(vim.event.Event):
         pass

      class HostIpChangedEvent(vim.event.HostEvent):
         oldIP = ""
         newIP = ""

      class HostIpInconsistentEvent(vim.event.HostEvent):
         ipAddress = ""
         ipAddress2 = ""

      class HostIpToShortNameFailedEvent(vim.event.HostEvent):
         pass

      class HostNonCompliantEvent(vim.event.HostEvent):
         pass

      class HostProfileAppliedEvent(vim.event.HostEvent):
         profile = vim.event.ProfileEventArgument()

      class HostReconnectionFailedEvent(vim.event.HostEvent):
         pass

      class HostRemovedEvent(vim.event.HostEvent):
         pass

      class HostShortNameToIpFailedEvent(vim.event.HostEvent):
         shortName = ""

      class HostShutdownEvent(vim.event.HostEvent):
         reason = ""

      class HostSpecificationChangedEvent(vim.event.HostEvent):
         pass

      class HostSpecificationRequireEvent(vim.event.HostEvent):
         pass

      class HostSpecificationUpdateEvent(vim.event.HostEvent):
         hostSpec = vim.profile.host.HostSpecification()

      class HostSubSpecificationDeleteEvent(vim.event.HostEvent):
         subSpecName = ""

      class HostSubSpecificationUpdateEvent(vim.event.HostEvent):
         hostSubSpec = vim.profile.host.HostSubSpecification()

      class HostSyncFailedEvent(vim.event.HostEvent):
         reason = vmodl.MethodFault()

      class HostUpgradeFailedEvent(vim.event.HostEvent):
         pass

      class HostUserWorldSwapNotEnabledEvent(vim.event.HostEvent):
         pass

      class HostVnicConnectedToCustomizedDVPortEvent(vim.event.HostEvent):
         vnic = vim.event.VnicPortArgument()
         prevPortKey = ""

      class HostWwnChangedEvent(vim.event.HostEvent):
         oldNodeWwns = [ 0 ]
         oldPortWwns = [ 0 ]
         newNodeWwns = [ 0 ]
         newPortWwns = [ 0 ]

      class HostWwnConflictEvent(vim.event.HostEvent):
         conflictedVms = [ vim.event.VmEventArgument() ]
         conflictedHosts = [ vim.event.HostEventArgument() ]
         wwn = 0

      class LicenseEvent(vim.event.Event):
         pass

      class LicenseExpiredEvent(vim.event.Event):
         feature = vim.LicenseManager.FeatureInfo()

      class LicenseNonComplianceEvent(vim.event.LicenseEvent):
         url = ""

      class LicenseRestrictedEvent(vim.event.LicenseEvent):
         pass

      class LicenseServerAvailableEvent(vim.event.LicenseEvent):
         licenseServer = ""

      class LicenseServerUnavailableEvent(vim.event.LicenseEvent):
         licenseServer = ""

      class LocalDatastoreCreatedEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class LocalTSMEnabledEvent(vim.event.HostEvent):
         pass

      class LockerMisconfiguredEvent(vim.event.Event):
         datastore = vim.event.DatastoreEventArgument()

      class LockerReconfiguredEvent(vim.event.Event):
         oldDatastore = vim.event.DatastoreEventArgument()
         newDatastore = vim.event.DatastoreEventArgument()

      class NASDatastoreCreatedEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class NetworkRollbackEvent(vim.event.Event):
         methodName = ""
         transactionId = ""

      class NoDatastoresConfiguredEvent(vim.event.HostEvent):
         pass

      class NoLicenseEvent(vim.event.LicenseEvent):
         feature = vim.LicenseManager.FeatureInfo()

      class ProfileEvent(vim.event.Event):
         profile = vim.event.ProfileEventArgument()

      class ProfileEventArgument(vim.event.EventArgument):
         profile = vim.profile.Profile()
         name = ""

      class ProfileReferenceHostChangedEvent(vim.event.ProfileEvent):
         referenceHost = vim.HostSystem()
         referenceHostName = ""
         prevReferenceHostName = ""

      class ProfileRemovedEvent(vim.event.ProfileEvent):
         pass

      class RemoteTSMEnabledEvent(vim.event.HostEvent):
         pass

      class ResourcePoolEvent(vim.event.Event):
         resourcePool = vim.event.ResourcePoolEventArgument()

      class ResourcePoolMovedEvent(vim.event.ResourcePoolEvent):
         oldParent = vim.event.ResourcePoolEventArgument()
         newParent = vim.event.ResourcePoolEventArgument()

      class ResourcePoolReconfiguredEvent(vim.event.ResourcePoolEvent):
         configChanges = vim.event.ChangesInfoEventArgument()

      class ResourceViolatedEvent(vim.event.ResourcePoolEvent):
         pass

      class RoleEventArgument(vim.event.EventArgument):
         roleId = 0
         name = ""

      class ScheduledTaskEvent(vim.event.Event):
         scheduledTask = vim.event.ScheduledTaskEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class ScheduledTaskFailedEvent(vim.event.ScheduledTaskEvent):
         reason = vmodl.MethodFault()

      class ScheduledTaskReconfiguredEvent(vim.event.ScheduledTaskEvent):
         configChanges = vim.event.ChangesInfoEventArgument()

      class ScheduledTaskRemovedEvent(vim.event.ScheduledTaskEvent):
         pass

      class ScheduledTaskStartedEvent(vim.event.ScheduledTaskEvent):
         pass

      class ServerLicenseExpiredEvent(vim.event.LicenseEvent):
         product = ""

      class SessionEvent(vim.event.Event):
         pass

      class SessionTerminatedEvent(vim.event.SessionEvent):
         sessionId = ""
         terminatedUsername = ""

      class TaskEvent(vim.event.Event):
         info = vim.TaskInfo()

      class TaskTimeoutEvent(vim.event.TaskEvent):
         pass

      class TemplateUpgradeEvent(vim.event.Event):
         legacyTemplate = ""

      class TemplateUpgradeFailedEvent(vim.event.TemplateUpgradeEvent):
         reason = vmodl.MethodFault()

      class TemplateUpgradedEvent(vim.event.TemplateUpgradeEvent):
         pass

      class TimedOutHostOperationEvent(vim.event.HostEvent):
         pass

      class UnlicensedVirtualMachinesEvent(vim.event.LicenseEvent):
         unlicensed = 0
         available = 0

      class UnlicensedVirtualMachinesFoundEvent(vim.event.LicenseEvent):
         available = 0

      class UpdatedAgentBeingRestartedEvent(vim.event.HostEvent):
         pass

      class UpgradeEvent(vim.event.Event):
         message = ""

      class UserAssignedToGroup(vim.event.HostEvent):
         userLogin = ""
         group = ""

      class UserLoginSessionEvent(vim.event.SessionEvent):
         ipAddress = ""
         userAgent = ""
         locale = ""
         sessionId = ""

      class UserLogoutSessionEvent(vim.event.SessionEvent):
         ipAddress = ""
         userAgent = ""
         callCount = 0
         sessionId = ""
         loginTime = vmodl.DateTime()

      class UserPasswordChanged(vim.event.HostEvent):
         userLogin = ""

      class UserUnassignedFromGroup(vim.event.HostEvent):
         userLogin = ""
         group = ""

      class UserUpgradeEvent(vim.event.UpgradeEvent):
         pass

      class VMFSDatastoreCreatedEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()
         datastoreUrl = ""

      class VMFSDatastoreExpandedEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()

      class VMFSDatastoreExtendedEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()

      class VMotionLicenseExpiredEvent(vim.event.LicenseEvent):
         pass

      class VcAgentUninstallFailedEvent(vim.event.HostEvent):
         reason = ""

      class VcAgentUninstalledEvent(vim.event.HostEvent):
         pass

      class VcAgentUpgradeFailedEvent(vim.event.HostEvent):
         reason = ""

      class VcAgentUpgradedEvent(vim.event.HostEvent):
         pass

      class VimAccountPasswordChangedEvent(vim.event.HostEvent):
         pass

      class VmEvent(vim.event.Event):
         template = False

      class VmFailedMigrateEvent(vim.event.VmEvent):
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmFailedRelayoutEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedRelayoutOnVmfs2DatastoreEvent(vim.event.VmEvent):
         pass

      class VmFailedStartingSecondaryEvent(vim.event.VmEvent):
         reason = ""

         class FailureReason(Enum):
            incompatibleHost = 0
            loginFailed = 1
            registerVmFailed = 2
            migrateFailed = 3

      class VmFailedToPowerOffEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToPowerOnEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToRebootGuestEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToResetEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToShutdownGuestEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToStandbyGuestEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedToSuspendEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFailedUpdatingSecondaryConfig(vim.event.VmEvent):
         pass

      class VmFailoverFailed(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmFaultToleranceTurnedOffEvent(vim.event.VmEvent):
         pass

      class VmFaultToleranceVmTerminatedEvent(vim.event.VmEvent):
         reason = ""

      class VmGuestOSCrashedEvent(vim.event.VmEvent):
         pass

      class VmGuestRebootEvent(vim.event.VmEvent):
         pass

      class VmGuestShutdownEvent(vim.event.VmEvent):
         pass

      class VmGuestStandbyEvent(vim.event.VmEvent):
         pass

      class VmInstanceUuidAssignedEvent(vim.event.VmEvent):
         instanceUuid = ""

      class VmInstanceUuidChangedEvent(vim.event.VmEvent):
         oldInstanceUuid = ""
         newInstanceUuid = ""

      class VmInstanceUuidConflictEvent(vim.event.VmEvent):
         conflictedVm = vim.event.VmEventArgument()
         instanceUuid = ""

      class VmMacAssignedEvent(vim.event.VmEvent):
         adapter = ""
         mac = ""

      class VmMacChangedEvent(vim.event.VmEvent):
         adapter = ""
         oldMac = ""
         newMac = ""

      class VmMacConflictEvent(vim.event.VmEvent):
         conflictedVm = vim.event.VmEventArgument()
         mac = ""

      class VmMaxFTRestartCountReached(vim.event.VmEvent):
         pass

      class VmMaxRestartCountReached(vim.event.VmEvent):
         pass

      class VmMessageErrorEvent(vim.event.VmEvent):
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMessageEvent(vim.event.VmEvent):
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMessageWarningEvent(vim.event.VmEvent):
         message = ""
         messageInfo = [ vim.vm.Message() ]

      class VmMigratedEvent(vim.event.VmEvent):
         sourceHost = vim.event.HostEventArgument()
         sourceDatacenter = vim.event.DatacenterEventArgument()
         sourceDatastore = vim.event.DatastoreEventArgument()

      class VmNoCompatibleHostForSecondaryEvent(vim.event.VmEvent):
         pass

      class VmNoNetworkAccessEvent(vim.event.VmEvent):
         destHost = vim.event.HostEventArgument()

      class VmOrphanedEvent(vim.event.VmEvent):
         pass

      class VmPoweredOffEvent(vim.event.VmEvent):
         pass

      class VmPoweredOnEvent(vim.event.VmEvent):
         pass

      class VmPoweringOnWithCustomizedDVPortEvent(vim.event.VmEvent):
         vnic = [ vim.event.VnicPortArgument() ]

      class VmPrimaryFailoverEvent(vim.event.VmEvent):
         reason = ""

      class VmReconfiguredEvent(vim.event.VmEvent):
         configSpec = vim.vm.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class VmRegisteredEvent(vim.event.VmEvent):
         pass

      class VmRelayoutSuccessfulEvent(vim.event.VmEvent):
         pass

      class VmRelayoutUpToDateEvent(vim.event.VmEvent):
         pass

      class VmReloadFromPathEvent(vim.event.VmEvent):
         configPath = ""

      class VmReloadFromPathFailedEvent(vim.event.VmEvent):
         configPath = ""

      class VmRelocateSpecEvent(vim.event.VmEvent):
         pass

      class VmRelocatedEvent(vim.event.VmRelocateSpecEvent):
         sourceHost = vim.event.HostEventArgument()
         sourceDatacenter = vim.event.DatacenterEventArgument()
         sourceDatastore = vim.event.DatastoreEventArgument()

      class VmRemoteConsoleConnectedEvent(vim.event.VmEvent):
         pass

      class VmRemoteConsoleDisconnectedEvent(vim.event.VmEvent):
         pass

      class VmRemovedEvent(vim.event.VmEvent):
         pass

      class VmRenamedEvent(vim.event.VmEvent):
         oldName = ""
         newName = ""

      class VmRequirementsExceedCurrentEVCModeEvent(vim.event.VmEvent):
         pass

      class VmResettingEvent(vim.event.VmEvent):
         pass

      class VmResourcePoolMovedEvent(vim.event.VmEvent):
         oldParent = vim.event.ResourcePoolEventArgument()
         newParent = vim.event.ResourcePoolEventArgument()

      class VmResourceReallocatedEvent(vim.event.VmEvent):
         configChanges = vim.event.ChangesInfoEventArgument()

      class VmRestartedOnAlternateHostEvent(vim.event.VmPoweredOnEvent):
         sourceHost = vim.event.HostEventArgument()

      class VmResumingEvent(vim.event.VmEvent):
         pass

      class VmSecondaryAddedEvent(vim.event.VmEvent):
         pass

      class VmSecondaryDisabledBySystemEvent(vim.event.VmEvent):
         reason = vmodl.MethodFault()

      class VmSecondaryDisabledEvent(vim.event.VmEvent):
         pass

      class VmSecondaryEnabledEvent(vim.event.VmEvent):
         pass

      class VmSecondaryStartedEvent(vim.event.VmEvent):
         pass

      class VmShutdownOnIsolationEvent(vim.event.VmPoweredOffEvent):
         isolatedHost = vim.event.HostEventArgument()
         shutdownResult = ""

         class Operation(Enum):
            shutdown = 0
            poweredOff = 1

      class VmStartRecordingEvent(vim.event.VmEvent):
         pass

      class VmStartReplayingEvent(vim.event.VmEvent):
         pass

      class VmStartingEvent(vim.event.VmEvent):
         pass

      class VmStartingSecondaryEvent(vim.event.VmEvent):
         pass

      class VmStaticMacConflictEvent(vim.event.VmEvent):
         conflictedVm = vim.event.VmEventArgument()
         mac = ""

      class VmStoppingEvent(vim.event.VmEvent):
         pass

      class VmSuspendedEvent(vim.event.VmEvent):
         pass

      class VmSuspendingEvent(vim.event.VmEvent):
         pass

      class VmTimedoutStartingSecondaryEvent(vim.event.VmEvent):
         timeout = 0

      class VmUnsupportedStartingEvent(vim.event.VmStartingEvent):
         guestId = ""

      class VmUpgradeCompleteEvent(vim.event.VmEvent):
         version = ""

      class VmUpgradeFailedEvent(vim.event.VmEvent):
         pass

      class VmUpgradingEvent(vim.event.VmEvent):
         version = ""

      class VmUuidAssignedEvent(vim.event.VmEvent):
         uuid = ""

      class VmUuidChangedEvent(vim.event.VmEvent):
         oldUuid = ""
         newUuid = ""

      class VmUuidConflictEvent(vim.event.VmEvent):
         conflictedVm = vim.event.VmEventArgument()
         uuid = ""

      class VmWwnAssignedEvent(vim.event.VmEvent):
         nodeWwns = [ 0 ]
         portWwns = [ 0 ]

      class VmWwnChangedEvent(vim.event.VmEvent):
         oldNodeWwns = [ 0 ]
         oldPortWwns = [ 0 ]
         newNodeWwns = [ 0 ]
         newPortWwns = [ 0 ]

      class VmWwnConflictEvent(vim.event.VmEvent):
         conflictedVms = [ vim.event.VmEventArgument() ]
         conflictedHosts = [ vim.event.HostEventArgument() ]
         wwn = 0

      class VnicPortArgument(vmodl.DynamicData):
         vnic = ""
         port = vim.dvs.PortConnection()

      class WarningUpgradeEvent(vim.event.UpgradeEvent):
         pass

      class iScsiBootFailureEvent(vim.event.HostEvent):
         pass

      class AccountCreatedEvent(vim.event.HostEvent):
         spec = vim.host.LocalAccountManager.AccountSpecification()
         group = False

      class AccountRemovedEvent(vim.event.HostEvent):
         account = ""
         group = False

      class AccountUpdatedEvent(vim.event.HostEvent):
         spec = vim.host.LocalAccountManager.AccountSpecification()
         group = False
         prevDescription = ""

      class AdminPasswordNotChangedEvent(vim.event.HostEvent):
         pass

      class AlarmEvent(vim.event.Event):
         alarm = vim.event.AlarmEventArgument()

      class AlarmReconfiguredEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         configChanges = vim.event.ChangesInfoEventArgument()

      class AlarmRemovedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmScriptCompleteEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         script = ""

      class AlarmScriptFailedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         script = ""
         reason = vmodl.MethodFault()

      class AlarmSnmpCompletedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmSnmpFailedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         reason = vmodl.MethodFault()

      class AlarmStatusChangedEvent(vim.event.AlarmEvent):
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()
         from = ""
         to = ""

      class AllVirtualMachinesLicensedEvent(vim.event.LicenseEvent):
         pass

      class AlreadyAuthenticatedSessionEvent(vim.event.SessionEvent):
         pass

      class AuthorizationEvent(vim.event.Event):
         pass

      class BadUsernameSessionEvent(vim.event.SessionEvent):
         ipAddress = ""

      class CanceledHostOperationEvent(vim.event.HostEvent):
         pass

      class ClusterEvent(vim.event.Event):
         pass

      class ClusterOvercommittedEvent(vim.event.ClusterEvent):
         pass

      class ClusterReconfiguredEvent(vim.event.ClusterEvent):
         configChanges = vim.event.ChangesInfoEventArgument()

      class ClusterStatusChangedEvent(vim.event.ClusterEvent):
         oldStatus = ""
         newStatus = ""

      class CustomFieldEvent(vim.event.Event):
         pass

      class CustomFieldValueChangedEvent(vim.event.CustomFieldEvent):
         entity = vim.event.ManagedEntityEventArgument()
         fieldKey = 0
         name = ""
         value = ""
         prevState = ""

      class CustomizationEvent(vim.event.VmEvent):
         logLocation = ""

      class CustomizationFailed(vim.event.CustomizationEvent):
         reason = ""

         class ReasonCode(Enum):
            userDefinedScriptDisabled = 0

      class CustomizationLinuxIdentityFailed(vim.event.CustomizationFailed):
         pass

      class CustomizationNetworkSetupFailed(vim.event.CustomizationFailed):
         pass

      class CustomizationStartedEvent(vim.event.CustomizationEvent):
         pass

      class CustomizationSucceeded(vim.event.CustomizationEvent):
         pass

      class CustomizationSysprepFailed(vim.event.CustomizationFailed):
         sysprepVersion = ""
         systemVersion = ""

      class CustomizationUnknownFailure(vim.event.CustomizationFailed):
         pass

      class DVPortgroupEvent(vim.event.Event):
         pass

      class DVPortgroupReconfiguredEvent(vim.event.DVPortgroupEvent):
         configSpec = vim.dvs.DistributedVirtualPortgroup.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class DVPortgroupRenamedEvent(vim.event.DVPortgroupEvent):
         oldName = ""
         newName = ""

      class DasAdmissionControlDisabledEvent(vim.event.ClusterEvent):
         pass

      class DasAdmissionControlEnabledEvent(vim.event.ClusterEvent):
         pass

      class DasAgentFoundEvent(vim.event.ClusterEvent):
         pass

      class DasAgentUnavailableEvent(vim.event.ClusterEvent):
         pass

      class DasClusterIsolatedEvent(vim.event.ClusterEvent):
         pass

      class DasDisabledEvent(vim.event.ClusterEvent):
         pass

      class DasEnabledEvent(vim.event.ClusterEvent):
         pass

      class DasHostFailedEvent(vim.event.ClusterEvent):
         failedHost = vim.event.HostEventArgument()

      class DasHostIsolatedEvent(vim.event.ClusterEvent):
         isolatedHost = vim.event.HostEventArgument()

      class DatacenterEvent(vim.event.Event):
         pass

      class DatacenterRenamedEvent(vim.event.DatacenterEvent):
         oldName = ""
         newName = ""

      class DatastoreDiscoveredEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreEvent(vim.event.Event):
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreFileEvent(vim.event.DatastoreEvent):
         targetFile = ""
         sourceOfOperation = ""
         succeeded = False

      class DatastoreFileMovedEvent(vim.event.DatastoreFileEvent):
         sourceDatastore = vim.event.DatastoreEventArgument()
         sourceFile = ""

      class DatastoreIORMReconfiguredEvent(vim.event.DatastoreEvent):
         pass

      class DatastorePrincipalConfigured(vim.event.HostEvent):
         datastorePrincipal = ""

      class DatastoreRemovedOnHostEvent(vim.event.HostEvent):
         datastore = vim.event.DatastoreEventArgument()

      class DatastoreRenamedEvent(vim.event.DatastoreEvent):
         oldName = ""
         newName = ""

      class DatastoreRenamedOnHostEvent(vim.event.HostEvent):
         oldName = ""
         newName = ""

      class DrsDisabledEvent(vim.event.ClusterEvent):
         pass

      class DrsEnabledEvent(vim.event.ClusterEvent):
         behavior = ""

      class DrsInvocationFailedEvent(vim.event.ClusterEvent):
         pass

      class DrsRecoveredFromFailureEvent(vim.event.ClusterEvent):
         pass

      class DrsResourceConfigureFailedEvent(vim.event.HostEvent):
         reason = vmodl.MethodFault()

      class DrsResourceConfigureSyncedEvent(vim.event.HostEvent):
         pass

      class DrsRuleComplianceEvent(vim.event.VmEvent):
         pass

      class DrsRuleViolationEvent(vim.event.VmEvent):
         pass

      class DrsSoftRuleViolationEvent(vim.event.VmEvent):
         pass

      class DrsVmMigratedEvent(vim.event.VmMigratedEvent):
         pass

      class DrsVmPoweredOnEvent(vim.event.VmPoweredOnEvent):
         pass

      class DuplicateIpDetectedEvent(vim.event.HostEvent):
         duplicateIP = ""
         macAddress = ""

      class DvpgImportEvent(vim.event.DVPortgroupEvent):
         importType = ""

      class DvpgRestoreEvent(vim.event.DVPortgroupEvent):
         pass

      class DvsEvent(vim.event.Event):

         class PortBlockState(Enum):
            unset = 0
            blocked = 1
            unblocked = 2
            unknown = 3

      class DvsHealthStatusChangeEvent(vim.event.HostEvent):
         switchUuid = ""
         healthResult = vim.dvs.HostMember.HealthCheckResult()

      class DvsHostBackInSyncEvent(vim.event.DvsEvent):
         hostBackInSync = vim.event.HostEventArgument()

      class DvsHostJoinedEvent(vim.event.DvsEvent):
         hostJoined = vim.event.HostEventArgument()

      class DvsHostLeftEvent(vim.event.DvsEvent):
         hostLeft = vim.event.HostEventArgument()

      class DvsHostStatusUpdated(vim.event.DvsEvent):
         hostMember = vim.event.HostEventArgument()
         oldStatus = ""
         newStatus = ""
         oldStatusDetail = ""
         newStatusDetail = ""

      class DvsHostWentOutOfSyncEvent(vim.event.DvsEvent):
         hostOutOfSync = vim.event.DvsOutOfSyncHostArgument()

      class DvsImportEvent(vim.event.DvsEvent):
         importType = ""

      class DvsMergedEvent(vim.event.DvsEvent):
         sourceDvs = vim.event.DvsEventArgument()
         destinationDvs = vim.event.DvsEventArgument()

      class DvsPortBlockedEvent(vim.event.DvsEvent):
         portKey = ""
         statusDetail = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
         prevBlockState = ""

      class DvsPortConnectedEvent(vim.event.DvsEvent):
         portKey = ""
         connectee = vim.dvs.PortConnectee()

      class DvsPortCreatedEvent(vim.event.DvsEvent):
         portKey = [ "" ]

      class DvsPortDeletedEvent(vim.event.DvsEvent):
         portKey = [ "" ]

      class DvsPortDisconnectedEvent(vim.event.DvsEvent):
         portKey = ""
         connectee = vim.dvs.PortConnectee()

      class DvsPortEnteredPassthruEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortExitedPassthruEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortJoinPortgroupEvent(vim.event.DvsEvent):
         portKey = ""
         portgroupKey = ""
         portgroupName = ""

      class DvsPortLeavePortgroupEvent(vim.event.DvsEvent):
         portKey = ""
         portgroupKey = ""
         portgroupName = ""

      class DvsPortLinkDownEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortLinkUpEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortReconfiguredEvent(vim.event.DvsEvent):
         portKey = [ "" ]
         configChanges = [ vim.event.ChangesInfoEventArgument() ]

      class DvsPortRuntimeChangeEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()

      class DvsPortUnblockedEvent(vim.event.DvsEvent):
         portKey = ""
         runtimeInfo = vim.dvs.DistributedVirtualPort.RuntimeInfo()
         prevBlockState = ""

      class DvsPortVendorSpecificStateChangeEvent(vim.event.DvsEvent):
         portKey = ""

      class DvsRenamedEvent(vim.event.DvsEvent):
         oldName = ""
         newName = ""

      class DvsRestoreEvent(vim.event.DvsEvent):
         pass

      class DvsUpgradeAvailableEvent(vim.event.DvsEvent):
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradeInProgressEvent(vim.event.DvsEvent):
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradeRejectedEvent(vim.event.DvsEvent):
         productInfo = vim.dvs.ProductSpec()

      class DvsUpgradedEvent(vim.event.DvsEvent):
         productInfo = vim.dvs.ProductSpec()

      class EnteredMaintenanceModeEvent(vim.event.HostEvent):
         pass

      class EnteredStandbyModeEvent(vim.event.HostEvent):
         pass

      class EnteringMaintenanceModeEvent(vim.event.HostEvent):
         pass

      class EnteringStandbyModeEvent(vim.event.HostEvent):
         pass

      class EntityEventArgument(vim.event.EventArgument):
         name = ""

      class ErrorUpgradeEvent(vim.event.UpgradeEvent):
         pass

      class ExitMaintenanceModeEvent(vim.event.HostEvent):
         pass

      class ExitStandbyModeFailedEvent(vim.event.HostEvent):
         pass

      class ExitedStandbyModeEvent(vim.event.HostEvent):
         pass

      class ExitingStandbyModeEvent(vim.event.HostEvent):
         pass

      class ExtendedEvent(vim.event.GeneralEvent):
         eventTypeId = ""
         managedObject = vmodl.ManagedObject()
         data = [ vim.event.ExtendedEvent.Pair() ]

         class Pair(vmodl.DynamicData):
            key = ""
            value = ""

      class FailoverLevelRestored(vim.event.ClusterEvent):
         pass

      class FolderEventArgument(vim.event.EntityEventArgument):
         folder = vim.Folder()

      class GhostDvsProxySwitchDetectedEvent(vim.event.HostEvent):
         switchUuid = [ "" ]

      class GhostDvsProxySwitchRemovedEvent(vim.event.HostEvent):
         switchUuid = [ "" ]

      class GlobalMessageChangedEvent(vim.event.SessionEvent):
         message = ""
         prevMessage = ""

      class HostAddFailedEvent(vim.event.HostEvent):
         hostname = ""

      class HostAddedEvent(vim.event.HostEvent):
         pass

      class HostAdminDisableEvent(vim.event.HostEvent):
         pass

      class HostAdminEnableEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedAccountFailedEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedAlreadyManagedEvent(vim.event.HostEvent):
         serverName = ""

      class HostCnxFailedBadCcagentEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedBadUsernameEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedBadVersionEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedCcagentUpgradeEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedNetworkErrorEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedNoAccessEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedNoConnectionEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedNoLicenseEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedNotFoundEvent(vim.event.HostEvent):
         pass

      class HostCnxFailedTimeoutEvent(vim.event.HostEvent):
         pass

      class HostComplianceCheckedEvent(vim.event.HostEvent):
         profile = vim.event.ProfileEventArgument()

      class HostCompliantEvent(vim.event.HostEvent):
         pass

      class HostConfigAppliedEvent(vim.event.HostEvent):
         pass

      class HostConnectedEvent(vim.event.HostEvent):
         pass

      class HostConnectionLostEvent(vim.event.HostEvent):
         pass

      class HostDasDisabledEvent(vim.event.HostEvent):
         pass

      class HostDasDisablingEvent(vim.event.HostEvent):
         pass

      class HostDasEnabledEvent(vim.event.HostEvent):
         pass

      class HostDasEnablingEvent(vim.event.HostEvent):
         pass

      class HostDasErrorEvent(vim.event.HostEvent):
         message = ""
         reason = ""

         class HostDasErrorReason(Enum):
            configFailed = 0
            timeout = 1
            communicationInitFailed = 2
            healthCheckScriptFailed = 3
            agentFailed = 4
            agentShutdown = 5
            isolationAddressUnpingable = 6
            other = 7

      class HostDasEvent(vim.event.HostEvent):
         pass

      class HostDasOkEvent(vim.event.HostEvent):
         pass

      class HostDisconnectedEvent(vim.event.HostEvent):
         reason = ""

         class ReasonCode(Enum):
            sslThumbprintVerifyFailed = 0
            licenseExpired = 1
            agentUpgrade = 2
            userRequest = 3
            insufficientLicenses = 4
            agentOutOfDate = 5
            passwordDecryptFailure = 6
            unknown = 7
            vcVRAMCapacityExceeded = 8

      class HostEnableAdminFailedEvent(vim.event.HostEvent):
         permissions = [ vim.AuthorizationManager.Permission() ]

      class HostEventArgument(vim.event.EntityEventArgument):
         host = vim.HostSystem()

      class HostExtraNetworksEvent(vim.event.HostDasEvent):
         ips = ""

      class HostInventoryFullEvent(vim.event.LicenseEvent):
         capacity = 0

      class HostIsolationIpPingFailedEvent(vim.event.HostDasEvent):
         isolationIp = ""

      class HostLicenseExpiredEvent(vim.event.LicenseEvent):
         pass

      class HostLocalPortCreatedEvent(vim.event.DvsEvent):
         hostLocalPort = vim.dvs.DistributedVirtualPort.HostLocalPortInfo()

      class HostMissingNetworksEvent(vim.event.HostDasEvent):
         ips = ""

      class HostMonitoringStateChangedEvent(vim.event.ClusterEvent):
         state = ""
         prevState = ""

      class HostNoAvailableNetworksEvent(vim.event.HostDasEvent):
         ips = ""

      class HostNoHAEnabledPortGroupsEvent(vim.event.HostDasEvent):
         pass

      class HostNoRedundantManagementNetworkEvent(vim.event.HostDasEvent):
         pass

      class HostNotInClusterEvent(vim.event.HostDasEvent):
         pass

      class HostOvercommittedEvent(vim.event.ClusterOvercommittedEvent):
         pass

      class HostPrimaryAgentNotShortNameEvent(vim.event.HostDasEvent):
         primaryAgent = ""

      class HostShortNameInconsistentEvent(vim.event.HostDasEvent):
         shortName = ""
         shortName2 = ""

      class HostStatusChangedEvent(vim.event.ClusterStatusChangedEvent):
         pass

      class IncorrectHostInformationEvent(vim.event.LicenseEvent):
         pass

      class InfoUpgradeEvent(vim.event.UpgradeEvent):
         pass

      class InsufficientFailoverResourcesEvent(vim.event.ClusterEvent):
         pass

      class InvalidEditionEvent(vim.event.LicenseEvent):
         feature = ""

      class ManagedEntityEventArgument(vim.event.EntityEventArgument):
         entity = vim.ManagedEntity()

      class MigrationEvent(vim.event.VmEvent):
         fault = vmodl.MethodFault()

      class MigrationHostErrorEvent(vim.event.MigrationEvent):
         dstHost = vim.event.HostEventArgument()

      class MigrationHostWarningEvent(vim.event.MigrationEvent):
         dstHost = vim.event.HostEventArgument()

      class MigrationResourceErrorEvent(vim.event.MigrationEvent):
         dstPool = vim.event.ResourcePoolEventArgument()
         dstHost = vim.event.HostEventArgument()

      class MigrationResourceWarningEvent(vim.event.MigrationEvent):
         dstPool = vim.event.ResourcePoolEventArgument()
         dstHost = vim.event.HostEventArgument()

      class MigrationWarningEvent(vim.event.MigrationEvent):
         pass

      class MtuMatchEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class MtuMismatchEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class NetworkEventArgument(vim.event.EntityEventArgument):
         network = vim.Network()

      class NoAccessUserEvent(vim.event.SessionEvent):
         ipAddress = ""

      class NoMaintenanceModeDrsRecommendationForVM(vim.event.VmEvent):
         pass

      class NonVIWorkloadDetectedOnDatastoreEvent(vim.event.DatastoreEvent):
         pass

      class NotEnoughResourcesToStartVmEvent(vim.event.VmEvent):
         reason = ""

      class OutOfSyncDvsHost(vim.event.DvsEvent):
         hostOutOfSync = [ vim.event.DvsOutOfSyncHostArgument() ]

      class PermissionEvent(vim.event.AuthorizationEvent):
         entity = vim.event.ManagedEntityEventArgument()
         principal = ""
         group = False

      class PermissionRemovedEvent(vim.event.PermissionEvent):
         pass

      class PermissionUpdatedEvent(vim.event.PermissionEvent):
         role = vim.event.RoleEventArgument()
         propagate = False
         prevRole = vim.event.RoleEventArgument()
         prevPropagate = False

      class ProfileAssociatedEvent(vim.event.ProfileEvent):
         pass

      class ProfileChangedEvent(vim.event.ProfileEvent):
         pass

      class ProfileCreatedEvent(vim.event.ProfileEvent):
         pass

      class ProfileDissociatedEvent(vim.event.ProfileEvent):
         pass

      class RecoveryEvent(vim.event.DvsEvent):
         hostName = ""
         portKey = ""
         dvsUuid = ""
         vnic = ""

      class ResourcePoolCreatedEvent(vim.event.ResourcePoolEvent):
         parent = vim.event.ResourcePoolEventArgument()

      class ResourcePoolDestroyedEvent(vim.event.ResourcePoolEvent):
         pass

      class ResourcePoolEventArgument(vim.event.EntityEventArgument):
         resourcePool = vim.ResourcePool()

      class RoleEvent(vim.event.AuthorizationEvent):
         role = vim.event.RoleEventArgument()

      class RoleRemovedEvent(vim.event.RoleEvent):
         pass

      class RoleUpdatedEvent(vim.event.RoleEvent):
         privilegeList = [ "" ]
         prevRoleName = ""
         privilegesAdded = [ "" ]
         privilegesRemoved = [ "" ]

      class RollbackEvent(vim.event.DvsEvent):
         hostName = ""
         methodName = ""

      class ScheduledTaskCompletedEvent(vim.event.ScheduledTaskEvent):
         pass

      class ScheduledTaskCreatedEvent(vim.event.ScheduledTaskEvent):
         pass

      class ScheduledTaskEmailCompletedEvent(vim.event.ScheduledTaskEvent):
         to = ""

      class ScheduledTaskEmailFailedEvent(vim.event.ScheduledTaskEvent):
         to = ""
         reason = vmodl.MethodFault()

      class ScheduledTaskEventArgument(vim.event.EntityEventArgument):
         scheduledTask = vim.scheduler.ScheduledTask()

      class ServerStartedSessionEvent(vim.event.SessionEvent):
         pass

      class TeamingMatchEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class TeamingMisMatchEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class TemplateBeingUpgradedEvent(vim.event.TemplateUpgradeEvent):
         pass

      class UplinkPortMtuNotSupportEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class UplinkPortMtuSupportEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class UplinkPortVlanTrunkedEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class UplinkPortVlanUntrunkedEvent(vim.event.DvsHealthStatusChangeEvent):
         pass

      class VmAcquiredMksTicketEvent(vim.event.VmEvent):
         pass

      class VmAcquiredTicketEvent(vim.event.VmEvent):
         ticketType = ""

      class VmAutoRenameEvent(vim.event.VmEvent):
         oldName = ""
         newName = ""

      class VmBeingCreatedEvent(vim.event.VmEvent):
         configSpec = vim.vm.ConfigSpec()

      class VmBeingDeployedEvent(vim.event.VmEvent):
         srcTemplate = vim.event.VmEventArgument()

      class VmBeingHotMigratedEvent(vim.event.VmEvent):
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmBeingMigratedEvent(vim.event.VmEvent):
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmBeingRelocatedEvent(vim.event.VmRelocateSpecEvent):
         destHost = vim.event.HostEventArgument()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmCloneEvent(vim.event.VmEvent):
         pass

      class VmCloneFailedEvent(vim.event.VmCloneEvent):
         destFolder = vim.event.FolderEventArgument()
         destName = ""
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()

      class VmClonedEvent(vim.event.VmCloneEvent):
         sourceVm = vim.event.VmEventArgument()

      class VmConfigMissingEvent(vim.event.VmEvent):
         pass

      class VmConnectedEvent(vim.event.VmEvent):
         pass

      class VmCreatedEvent(vim.event.VmEvent):
         pass

      class VmDasBeingResetEvent(vim.event.VmEvent):
         reason = ""

         class ReasonCode(Enum):
            vmtoolsHeartbeatFailure = 0
            appHeartbeatFailure = 1
            appImmediateResetRequest = 2
            vmcpResetApdCleared = 3
            guestOsCrashFailure = 4

      class VmDasBeingResetWithScreenshotEvent(vim.event.VmDasBeingResetEvent):
         screenshotFilePath = ""

      class VmDasResetFailedEvent(vim.event.VmEvent):
         pass

      class VmDasUpdateErrorEvent(vim.event.VmEvent):
         pass

      class VmDasUpdateOkEvent(vim.event.VmEvent):
         pass

      class VmDateRolledBackEvent(vim.event.VmEvent):
         pass

      class VmDeployFailedEvent(vim.event.VmEvent):
         destDatastore = vim.event.EntityEventArgument()
         reason = vmodl.MethodFault()

      class VmDeployedEvent(vim.event.VmEvent):
         srcTemplate = vim.event.VmEventArgument()

      class VmDisconnectedEvent(vim.event.VmEvent):
         pass

      class VmDiscoveredEvent(vim.event.VmEvent):
         pass

      class VmDiskFailedEvent(vim.event.VmEvent):
         disk = ""
         reason = vmodl.MethodFault()

      class VmEmigratingEvent(vim.event.VmEvent):
         pass

      class VmEndRecordingEvent(vim.event.VmEvent):
         pass

      class VmEndReplayingEvent(vim.event.VmEvent):
         pass

      class VmEventArgument(vim.event.EntityEventArgument):
         vm = vim.VirtualMachine()

      class VmFaultToleranceStateChangedEvent(vim.event.VmEvent):
         oldState = vim.VirtualMachine.FaultToleranceState()
         newState = vim.VirtualMachine.FaultToleranceState()

      class VmHealthMonitoringStateChangedEvent(vim.event.ClusterEvent):
         state = ""
         prevState = ""

      class VmPowerOffOnIsolationEvent(vim.event.VmPoweredOffEvent):
         isolatedHost = vim.event.HostEventArgument()

      class VmRelocateFailedEvent(vim.event.VmRelocateSpecEvent):
         destHost = vim.event.HostEventArgument()
         reason = vmodl.MethodFault()
         destDatacenter = vim.event.DatacenterEventArgument()
         destDatastore = vim.event.DatastoreEventArgument()

      class VmVnicPoolReservationViolationClearEvent(vim.event.DvsEvent):
         vmVnicResourcePoolKey = ""
         vmVnicResourcePoolName = ""

      class VmVnicPoolReservationViolationRaiseEvent(vim.event.DvsEvent):
         vmVnicResourcePoolKey = ""
         vmVnicResourcePoolName = ""

      class AlarmAcknowledgedEvent(vim.event.AlarmEvent):
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmActionTriggeredEvent(vim.event.AlarmEvent):
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmClearedEvent(vim.event.AlarmEvent):
         source = vim.event.ManagedEntityEventArgument()
         entity = vim.event.ManagedEntityEventArgument()
         from = ""

      class AlarmCreatedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()

      class AlarmEmailCompletedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         to = ""

      class AlarmEmailFailedEvent(vim.event.AlarmEvent):
         entity = vim.event.ManagedEntityEventArgument()
         to = ""
         reason = vmodl.MethodFault()

      class AlarmEventArgument(vim.event.EntityEventArgument):
         alarm = vim.alarm.Alarm()

      class ClusterComplianceCheckedEvent(vim.event.ClusterEvent):
         profile = vim.event.ProfileEventArgument()

      class ClusterCreatedEvent(vim.event.ClusterEvent):
         parent = vim.event.FolderEventArgument()

      class ClusterDestroyedEvent(vim.event.ClusterEvent):
         pass

      class ComputeResourceEventArgument(vim.event.EntityEventArgument):
         computeResource = vim.ComputeResource()

      class CustomFieldDefEvent(vim.event.CustomFieldEvent):
         fieldKey = 0
         name = ""

      class CustomFieldDefRemovedEvent(vim.event.CustomFieldDefEvent):
         pass

      class CustomFieldDefRenamedEvent(vim.event.CustomFieldDefEvent):
         newName = ""

      class DVPortgroupCreatedEvent(vim.event.DVPortgroupEvent):
         pass

      class DVPortgroupDestroyedEvent(vim.event.DVPortgroupEvent):
         pass

      class DatacenterCreatedEvent(vim.event.DatacenterEvent):
         parent = vim.event.FolderEventArgument()

      class DatacenterEventArgument(vim.event.EntityEventArgument):
         datacenter = vim.Datacenter()

      class DatastoreCapacityIncreasedEvent(vim.event.DatastoreEvent):
         oldCapacity = 0
         newCapacity = 0

      class DatastoreDestroyedEvent(vim.event.DatastoreEvent):
         pass

      class DatastoreDuplicatedEvent(vim.event.DatastoreEvent):
         pass

      class DatastoreEventArgument(vim.event.EntityEventArgument):
         datastore = vim.Datastore()

      class DatastoreFileCopiedEvent(vim.event.DatastoreFileEvent):
         sourceDatastore = vim.event.DatastoreEventArgument()
         sourceFile = ""

      class DatastoreFileDeletedEvent(vim.event.DatastoreFileEvent):
         pass

      class DrsEnteredStandbyModeEvent(vim.event.EnteredStandbyModeEvent):
         pass

      class DrsEnteringStandbyModeEvent(vim.event.EnteringStandbyModeEvent):
         pass

      class DrsExitStandbyModeFailedEvent(vim.event.ExitStandbyModeFailedEvent):
         pass

      class DrsExitedStandbyModeEvent(vim.event.ExitedStandbyModeEvent):
         pass

      class DrsExitingStandbyModeEvent(vim.event.ExitingStandbyModeEvent):
         pass

      class DvsCreatedEvent(vim.event.DvsEvent):
         parent = vim.event.FolderEventArgument()

      class DvsDestroyedEvent(vim.event.DvsEvent):
         pass

      class DvsEventArgument(vim.event.EntityEventArgument):
         dvs = vim.DistributedVirtualSwitch()

      class DvsReconfiguredEvent(vim.event.DvsEvent):
         configSpec = vim.DistributedVirtualSwitch.ConfigSpec()
         configChanges = vim.event.ChangesInfoEventArgument()

      class MigrationErrorEvent(vim.event.MigrationEvent):
         pass

      class PermissionAddedEvent(vim.event.PermissionEvent):
         role = vim.event.RoleEventArgument()
         propagate = False

      class RoleAddedEvent(vim.event.RoleEvent):
         privilegeList = [ "" ]

      class VmBeingClonedEvent(vim.event.VmCloneEvent):
         destFolder = vim.event.FolderEventArgument()
         destName = ""
         destHost = vim.event.HostEventArgument()

      class VmBeingClonedNoFolderEvent(vim.event.VmCloneEvent):
         destName = ""
         destHost = vim.event.HostEventArgument()

      class CustomFieldDefAddedEvent(vim.event.CustomFieldDefEvent):
         pass

   class ext(object):

      class ExtendedProductInfo(vmodl.DynamicData):
         companyUrl = ""
         productUrl = ""
         managementUrl = ""
         self = vim.ManagedEntity()

      class ManagedByInfo(vmodl.DynamicData):
         extensionKey = ""
         type = ""

      class ManagedEntityInfo(vmodl.DynamicData):
         type = ""
         smallIconUrl = ""
         iconUrl = ""
         description = ""

      class SolutionManagerInfo(vmodl.DynamicData):
         tab = [ vim.ext.SolutionManagerInfo.TabInfo() ]
         smallIconUrl = ""

         class TabInfo(vmodl.DynamicData):
            label = ""
            url = ""

   class fault(object):

      class CannotDisableDrsOnClustersWithVApps(vmodl.RuntimeFault):
         pass

      class ConflictingDatastoreFound(vmodl.RuntimeFault):
         name = ""
         url = ""

      class DatabaseError(vmodl.RuntimeFault):
         pass

      class DisallowedChangeByService(vmodl.RuntimeFault):
         serviceName = ""
         disallowedChange = ""

         class DisallowedChange(Enum):
            hotExtendDisk = 0

      class DisallowedOperationOnFailoverHost(vmodl.RuntimeFault):
         host = vim.HostSystem()
         hostname = ""

      class ExpiredFeatureLicense(vmodl.fault.NotEnoughLicenses):
         feature = ""
         count = 0
         expirationDate = vmodl.DateTime()

      class FailToLockFaultToleranceVMs(vmodl.RuntimeFault):
         vmName = ""
         vm = vim.VirtualMachine()
         alreadyLockedVm = vim.VirtualMachine()

      class HostAccessRestrictedToManagementServer(vmodl.fault.NotSupported):
         managementServer = ""

      class HostInventoryFull(vmodl.fault.NotEnoughLicenses):
         capacity = 0

      class InUseFeatureManipulationDisallowed(vmodl.fault.NotEnoughLicenses):
         pass

      class IncompatibleSetting(vmodl.fault.InvalidArgument):
         conflictingProperty = vmodl.PropertyPath()

      class IncorrectHostInformation(vmodl.fault.NotEnoughLicenses):
         pass

      class InvalidDasConfigArgument(vmodl.fault.InvalidArgument):
         entry = ""
         clusterName = ""

         class EntryForInvalidArgument(Enum):
            admissionControl = 0
            userHeartbeatDs = 1
            vmConfig = 2

      class InvalidDasRestartPriorityForFtVm(vmodl.fault.InvalidArgument):
         vm = vim.VirtualMachine()
         vmName = ""

      class InvalidDrsBehaviorForFtVm(vmodl.fault.InvalidArgument):
         vm = vim.VirtualMachine()
         vmName = ""

      class InvalidEditionLicense(vmodl.fault.NotEnoughLicenses):
         feature = ""

      class InvalidIndexArgument(vmodl.fault.InvalidArgument):
         key = ""

      class InvalidProfileReferenceHost(vmodl.RuntimeFault):
         reason = ""
         host = vim.HostSystem()
         profile = vim.profile.Profile()
         profileName = ""

         class Reason(Enum):
            incompatibleVersion = 0
            missingReferenceHost = 1

      class InventoryHasStandardAloneHosts(vmodl.fault.NotEnoughLicenses):
         hosts = [ "" ]

      class LicenseAssignmentFailed(vmodl.RuntimeFault):
         reason = ""

         class Reason(Enum):
            keyEntityMismatch = 0
            downgradeDisallowed = 1
            inventoryNotManageableByVirtualCenter = 2
            hostsUnmanageableByVirtualCenterWithoutLicenseServer = 3

      class LicenseDowngradeDisallowed(vmodl.fault.NotEnoughLicenses):
         edition = ""
         entityId = ""
         features = [ vmodl.KeyAnyValue() ]

      class LicenseExpired(vmodl.fault.NotEnoughLicenses):
         licenseKey = ""

      class LicenseKeyEntityMismatch(vmodl.fault.NotEnoughLicenses):
         pass

      class LicenseRestricted(vmodl.fault.NotEnoughLicenses):
         pass

      class LicenseSourceUnavailable(vmodl.fault.NotEnoughLicenses):
         licenseSource = vim.LicenseManager.LicenseSource()

      class MethodAlreadyDisabledFault(vmodl.RuntimeFault):
         sourceId = ""

      class MethodDisabled(vmodl.RuntimeFault):
         source = ""

      class NoLicenseServerConfigured(vmodl.fault.NotEnoughLicenses):
         pass

      class NoPermission(vmodl.fault.SecurityError):
         object = vmodl.ManagedObject()
         privilegeId = ""

      class NotAuthenticated(vim.fault.NoPermission):
         pass

      class OperationDisallowedOnHost(vmodl.RuntimeFault):
         pass

      class RestrictedByAdministrator(vmodl.RuntimeFault):
         details = ""

      class RestrictedVersion(vmodl.fault.SecurityError):
         pass

      class SolutionUserRequired(vmodl.fault.SecurityError):
         pass

      class ThirdPartyLicenseAssignmentFailed(vmodl.RuntimeFault):
         host = vim.HostSystem()
         module = ""
         reason = ""

         class Reason(Enum):
            licenseAssignmentFailed = 0
            moduleNotInstalled = 1

      class VAppOperationInProgress(vmodl.RuntimeFault):
         pass

      class VimFault(vmodl.MethodFault):
         pass

      class VmConfigFault(vim.fault.VimFault):
         pass

      class VmConfigIncompatibleForFaultTolerance(vim.fault.VmConfigFault):
         fault = vmodl.MethodFault()

      class VmConfigIncompatibleForRecordReplay(vim.fault.VmConfigFault):
         fault = vmodl.MethodFault()

      class VmFaultToleranceIssue(vim.fault.VimFault):
         pass

      class VmFaultToleranceOpIssuesList(vim.fault.VmFaultToleranceIssue):
         errors = [ vmodl.MethodFault() ]
         warnings = [ vmodl.MethodFault() ]

      class VmHostAffinityRuleViolation(vim.fault.VmConfigFault):
         vmName = ""
         hostName = ""

      class VmLimitLicense(vmodl.fault.NotEnoughLicenses):
         limit = 0

      class VmMetadataManagerFault(vim.fault.VimFault):
         pass

      class VmMonitorIncompatibleForFaultTolerance(vim.fault.VimFault):
         pass

      class VmToolsUpgradeFault(vim.fault.VimFault):
         pass

      class VmValidateMaxDevice(vim.fault.VimFault):
         device = ""
         max = 0
         count = 0

      class VramLimitLicense(vmodl.fault.NotEnoughLicenses):
         limit = 0

      class VsanFault(vim.fault.VimFault):
         pass

      class WipeDiskFault(vim.fault.VimFault):
         pass

      class ActiveDirectoryFault(vim.fault.VimFault):
         errorCode = 0

      class AlreadyExists(vim.fault.VimFault):
         name = ""

      class AlreadyUpgraded(vim.fault.VimFault):
         pass

      class AnswerFileUpdateFailed(vim.fault.VimFault):
         failure = [ vim.fault.AnswerFileUpdateFailed.UpdateFailure() ]

         class UpdateFailure(vmodl.DynamicData):
            userInputPath = vim.profile.ProfilePropertyPath()
            errMsg = vmodl.LocalizableMessage()

      class AuthMinimumAdminPermission(vim.fault.VimFault):
         pass

      class CannotAccessLocalSource(vim.fault.VimFault):
         pass

      class CannotAccessVmComponent(vim.fault.VmConfigFault):
         pass

      class CannotAccessVmConfig(vim.fault.CannotAccessVmComponent):
         reason = vmodl.MethodFault()

      class CannotAccessVmDevice(vim.fault.CannotAccessVmComponent):
         device = ""
         backing = ""
         connected = False

      class CannotAccessVmDisk(vim.fault.CannotAccessVmDevice):
         fault = vmodl.MethodFault()

      class CannotChangeDrsBehaviorForFtSecondary(vim.fault.VmFaultToleranceIssue):
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotChangeHaSettingsForFtSecondary(vim.fault.VmFaultToleranceIssue):
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotChangeVsanClusterUuid(vim.fault.VsanFault):
         pass

      class CannotChangeVsanNodeUuid(vim.fault.VsanFault):
         pass

      class CannotComputeFTCompatibleHosts(vim.fault.VmFaultToleranceIssue):
         vm = vim.VirtualMachine()
         vmName = ""

      class CannotDisableSnapshot(vim.fault.VmConfigFault):
         pass

      class CannotDisconnectHostWithFaultToleranceVm(vim.fault.VimFault):
         hostName = ""

      class CannotEnableVmcpForCluster(vim.fault.VimFault):
         host = vim.HostSystem()
         hostName = ""
         reason = ""

         class Reason(Enum):
            APDTimeoutDisabled = 0

      class CannotMoveFaultToleranceVm(vim.fault.VimFault):
         moveType = ""
         vmName = ""

         class MoveType(Enum):
            resourcePool = 0
            cluster = 1

      class CannotMoveHostWithFaultToleranceVm(vim.fault.VimFault):
         pass

      class CannotMoveVsanEnabledHost(vim.fault.VsanFault):
         pass

      class CannotPlaceWithoutPrerequisiteMoves(vim.fault.VimFault):
         pass

      class CannotReconfigureVsanWhenHaEnabled(vim.fault.VsanFault):
         pass

      class CannotUseNetwork(vim.fault.VmConfigFault):
         device = ""
         backing = ""
         connected = False
         reason = ""
         network = vim.Network()

         class Reason(Enum):
            NetworkReservationNotSupported = 0
            MismatchedNetworkPolicies = 1
            MismatchedDvsVersionOrVendor = 2
            VMotionToUnsupportedNetworkType = 3
            NetworkUnderMaintenance = 4
            MismatchedEnsMode = 5

      class ConcurrentAccess(vim.fault.VimFault):
         pass

      class CpuHotPlugNotSupported(vim.fault.VmConfigFault):
         pass

      class CustomizationFault(vim.fault.VimFault):
         pass

      class CustomizationPending(vim.fault.CustomizationFault):
         pass

      class DasConfigFault(vim.fault.VimFault):
         reason = ""
         output = ""
         event = [ vim.event.Event() ]

         class DasConfigFaultReason(Enum):
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

      class DeltaDiskFormatNotSupported(vim.fault.VmConfigFault):
         datastore = [ vim.Datastore() ]
         deltaDiskFormat = ""

      class DestinationVsanDisabled(vim.fault.CannotMoveVsanEnabledHost):
         destinationCluster = ""

      class DomainNotFound(vim.fault.ActiveDirectoryFault):
         domainName = ""

      class DrsDisabledOnVm(vim.fault.VimFault):
         pass

      class DuplicateName(vim.fault.VimFault):
         name = ""
         object = vmodl.ManagedObject()

      class DuplicateVsanNetworkInterface(vim.fault.VsanFault):
         device = ""

      class DvsFault(vim.fault.VimFault):
         pass

      class DvsNotAuthorized(vim.fault.DvsFault):
         sessionExtensionKey = ""
         dvsExtensionKey = ""

      class DvsOperationBulkFault(vim.fault.DvsFault):
         hostFault = [ vim.fault.DvsOperationBulkFault.FaultOnHost() ]

         class FaultOnHost(vmodl.DynamicData):
            host = vim.HostSystem()
            fault = vmodl.MethodFault()

      class DvsScopeViolated(vim.fault.DvsFault):
         scope = [ vim.ManagedEntity() ]
         entity = vim.ManagedEntity()

      class EVCConfigFault(vim.fault.VimFault):
         faults = [ vmodl.MethodFault() ]

      class EVCModeIllegalByVendor(vim.fault.EVCConfigFault):
         clusterCPUVendor = ""
         modeCPUVendor = ""

      class EVCModeUnsupportedByHosts(vim.fault.EVCConfigFault):
         evcMode = ""
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EVCUnsupportedByHostHardware(vim.fault.EVCConfigFault):
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EVCUnsupportedByHostSoftware(vim.fault.EVCConfigFault):
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class EightHostLimitViolated(vim.fault.VmConfigFault):
         pass

      class ExpiredAddonLicense(vim.fault.ExpiredFeatureLicense):
         pass

      class ExpiredEditionLicense(vim.fault.ExpiredFeatureLicense):
         pass

      class ExtendedFault(vim.fault.VimFault):
         faultTypeId = ""
         data = [ vim.KeyValue() ]

      class FaultToleranceCannotEditMem(vim.fault.VmConfigFault):
         vmName = ""
         vm = vim.VirtualMachine()

      class FaultToleranceNotLicensed(vim.fault.VmFaultToleranceIssue):
         hostName = ""

      class FaultTolerancePrimaryPowerOnNotAttempted(vim.fault.VmFaultToleranceIssue):
         secondaryVm = vim.VirtualMachine()
         primaryVm = vim.VirtualMachine()

      class FaultToleranceVmNotDasProtected(vim.fault.VimFault):
         vm = vim.VirtualMachine()
         vmName = ""

      class FcoeFault(vim.fault.VimFault):
         pass

      class FcoeFaultPnicHasNoPortSet(vim.fault.FcoeFault):
         nicDevice = ""

      class FileFault(vim.fault.VimFault):
         file = ""

      class FileLocked(vim.fault.FileFault):
         pass

      class FileNameTooLong(vim.fault.FileFault):
         pass

      class FileNotFound(vim.fault.FileFault):
         pass

      class FileNotWritable(vim.fault.FileFault):
         pass

      class FileTooLarge(vim.fault.FileFault):
         datastore = ""
         fileSize = 0
         maxFileSize = 0

      class FtIssuesOnHost(vim.fault.VmFaultToleranceIssue):
         host = vim.HostSystem()
         hostName = ""
         errors = [ vmodl.MethodFault() ]

         class HostSelectionType(Enum):
            user = 0
            vc = 1
            drs = 2

      class GenericDrsFault(vim.fault.VimFault):
         hostFaults = [ vmodl.MethodFault() ]

      class GenericVmConfigFault(vim.fault.VmConfigFault):
         reason = ""

      class GuestOperationsFault(vim.fault.VimFault):
         pass

      class GuestOperationsUnavailable(vim.fault.GuestOperationsFault):
         pass

      class GuestPermissionDenied(vim.fault.GuestOperationsFault):
         pass

      class GuestProcessNotFound(vim.fault.GuestOperationsFault):
         pid = 0

      class GuestRegistryFault(vim.fault.GuestOperationsFault):
         windowsSystemErrorCode = 0

      class GuestRegistryKeyFault(vim.fault.GuestRegistryFault):
         keyName = ""

      class GuestRegistryKeyHasSubkeys(vim.fault.GuestRegistryKeyFault):
         pass

      class GuestRegistryKeyInvalid(vim.fault.GuestRegistryKeyFault):
         pass

      class GuestRegistryKeyParentVolatile(vim.fault.GuestRegistryKeyFault):
         pass

      class GuestRegistryValueFault(vim.fault.GuestRegistryFault):
         keyName = ""
         valueName = ""

      class GuestRegistryValueNotFound(vim.fault.GuestRegistryValueFault):
         pass

      class HeterogenousHostsBlockingEVC(vim.fault.EVCConfigFault):
         pass

      class HostConfigFault(vim.fault.VimFault):
         pass

      class HostConnectFault(vim.fault.VimFault):
         pass

      class HostHasComponentFailure(vim.fault.VimFault):
         hostName = ""
         componentType = ""
         componentName = ""

         class HostComponentType(Enum):
            Datastore = 0

      class HostInDomain(vim.fault.HostConfigFault):
         pass

      class HostIncompatibleForFaultTolerance(vim.fault.VmFaultToleranceIssue):
         hostName = ""
         reason = ""

         class Reason(Enum):
            product = 0
            processor = 1

      class HostIncompatibleForRecordReplay(vim.fault.VimFault):
         hostName = ""
         reason = ""

         class Reason(Enum):
            product = 0
            processor = 1

      class HostPowerOpFailed(vim.fault.VimFault):
         pass

      class HostSpecificationOperationFailed(vim.fault.VimFault):
         host = vim.HostSystem()

      class HttpFault(vim.fault.VimFault):
         statusCode = 0
         statusMessage = ""

      class IORMNotSupportedHostOnDatastore(vim.fault.VimFault):
         datastore = vim.Datastore()
         datastoreName = ""
         host = [ vim.HostSystem() ]

      class ImportHostAddFailure(vim.fault.DvsFault):
         hostIp = [ "" ]

      class ImportOperationBulkFault(vim.fault.DvsFault):
         importFaults = [ vim.fault.ImportOperationBulkFault.FaultOnImport() ]

         class FaultOnImport(vmodl.DynamicData):
            entityType = ""
            key = ""
            fault = vmodl.MethodFault()

      class InaccessibleVFlashSource(vim.fault.VimFault):
         hostName = ""

      class IncompatibleHostForFtSecondary(vim.fault.VmFaultToleranceIssue):
         host = vim.HostSystem()
         error = [ vmodl.MethodFault() ]

      class IncorrectFileType(vim.fault.FileFault):
         pass

      class InsufficientResourcesFault(vim.fault.VimFault):
         pass

      class InsufficientStandbyResource(vim.fault.InsufficientResourcesFault):
         pass

      class InsufficientStorageIops(vim.fault.VimFault):
         unreservedIops = 0
         requestedIops = 0
         datastoreName = ""

      class InsufficientStorageSpace(vim.fault.InsufficientResourcesFault):
         pass

      class InsufficientVFlashResourcesFault(vim.fault.InsufficientResourcesFault):
         freeSpaceInMB = 0
         freeSpace = 0
         requestedSpaceInMB = 0
         requestedSpace = 0

      class InvalidAffinitySettingFault(vim.fault.VimFault):
         pass

      class InvalidBmcRole(vim.fault.VimFault):
         pass

      class InvalidCAMServer(vim.fault.ActiveDirectoryFault):
         camServer = ""

      class InvalidDatastore(vim.fault.VimFault):
         datastore = vim.Datastore()
         name = ""

      class InvalidDatastorePath(vim.fault.InvalidDatastore):
         datastorePath = ""

      class InvalidEvent(vim.fault.VimFault):
         pass

      class InvalidFolder(vim.fault.VimFault):
         target = vim.ManagedEntity()

      class InvalidFormat(vim.fault.VmConfigFault):
         pass

      class InvalidGuestLogin(vim.fault.GuestOperationsFault):
         pass

      class InvalidHostName(vim.fault.HostConfigFault):
         pass

      class InvalidIpfixConfig(vim.fault.DvsFault):
         property = vmodl.PropertyPath()

      class InvalidIpmiLoginInfo(vim.fault.VimFault):
         pass

      class InvalidIpmiMacAddress(vim.fault.VimFault):
         userProvidedMacAddress = ""
         observedMacAddress = ""

      class InvalidLicense(vim.fault.VimFault):
         licenseContent = ""

      class InvalidLocale(vim.fault.VimFault):
         pass

      class InvalidLogin(vim.fault.VimFault):
         pass

      class InvalidName(vim.fault.VimFault):
         name = ""
         entity = vim.ManagedEntity()

      class InvalidOperationOnSecondaryVm(vim.fault.VmFaultToleranceIssue):
         instanceUuid = ""

      class InvalidPrivilege(vim.fault.VimFault):
         privilege = ""

      class InvalidResourcePoolStructureFault(vim.fault.InsufficientResourcesFault):
         pass

      class InvalidSnapshotFormat(vim.fault.InvalidFormat):
         pass

      class InvalidState(vim.fault.VimFault):
         pass

      class InvalidVmConfig(vim.fault.VmConfigFault):
         property = vmodl.PropertyPath()

      class InvalidVmState(vim.fault.InvalidState):
         vm = vim.VirtualMachine()

      class IpHostnameGeneratorError(vim.fault.CustomizationFault):
         pass

      class IscsiFault(vim.fault.VimFault):
         pass

      class IscsiFaultInvalidVnic(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultPnicInUse(vim.fault.IscsiFault):
         pnicDevice = ""

      class IscsiFaultVnicAlreadyBound(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicHasActivePaths(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicHasMultipleUplinks(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicHasNoUplinks(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicHasWrongUplink(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicInUse(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicIsLastPath(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicNotBound(vim.fault.IscsiFault):
         vnicDevice = ""

      class IscsiFaultVnicNotFound(vim.fault.IscsiFault):
         vnicDevice = ""

      class KeyNotFound(vim.fault.VimFault):
         key = ""

      class LargeRDMNotSupportedOnDatastore(vim.fault.VmConfigFault):
         device = ""
         datastore = vim.Datastore()
         datastoreName = ""

      class LicenseEntityNotFound(vim.fault.VimFault):
         entityId = ""

      class LicenseServerUnavailable(vim.fault.VimFault):
         licenseServer = ""

      class LimitExceeded(vim.fault.VimFault):
         property = vmodl.PropertyPath()
         limit = 0

      class LinuxVolumeNotClean(vim.fault.CustomizationFault):
         pass

      class LogBundlingFailed(vim.fault.VimFault):
         pass

      class MemoryHotPlugNotSupported(vim.fault.VmConfigFault):
         pass

      class MigrationFault(vim.fault.VimFault):
         pass

      class MigrationFeatureNotSupported(vim.fault.MigrationFault):
         atSourceHost = False
         failedHostName = ""
         failedHost = vim.HostSystem()

      class MigrationNotReady(vim.fault.MigrationFault):
         reason = ""

      class MismatchedBundle(vim.fault.VimFault):
         bundleUuid = ""
         hostUuid = ""
         bundleBuildNumber = 0
         hostBuildNumber = 0

      class MismatchedNetworkPolicies(vim.fault.MigrationFault):
         device = ""
         backing = ""
         connected = False

      class MismatchedVMotionNetworkNames(vim.fault.MigrationFault):
         sourceNetwork = ""
         destNetwork = ""

      class MissingBmcSupport(vim.fault.VimFault):
         pass

      class MissingLinuxCustResources(vim.fault.CustomizationFault):
         pass

      class MissingWindowsCustResources(vim.fault.CustomizationFault):
         pass

      class MksConnectionLimitReached(vim.fault.InvalidState):
         connectionLimit = 0

      class MountError(vim.fault.CustomizationFault):
         vm = vim.VirtualMachine()
         diskIndex = 0

      class MultipleCertificatesVerifyFault(vim.fault.HostConnectFault):
         thumbprintData = [ vim.fault.MultipleCertificatesVerifyFault.ThumbprintData() ]

         class ThumbprintData(vmodl.DynamicData):
            port = 0
            thumbprint = ""

      class NamespaceFull(vim.fault.VimFault):
         name = ""
         currentMaxSize = 0
         requiredSize = 0

      class NamespaceLimitReached(vim.fault.VimFault):
         limit = 0

      class NamespaceWriteProtected(vim.fault.VimFault):
         name = ""

      class NasConfigFault(vim.fault.HostConfigFault):
         name = ""

      class NasConnectionLimitReached(vim.fault.NasConfigFault):
         remoteHost = ""
         remotePath = ""

      class NasSessionCredentialConflict(vim.fault.NasConfigFault):
         remoteHost = ""
         remotePath = ""
         userName = ""

      class NasVolumeNotMounted(vim.fault.NasConfigFault):
         remoteHost = ""
         remotePath = ""

      class NetworkCopyFault(vim.fault.FileFault):
         pass

      class NetworkDisruptedAndConfigRolledBack(vim.fault.VimFault):
         host = ""

      class NetworkInaccessible(vim.fault.NasConfigFault):
         pass

      class NetworksMayNotBeTheSame(vim.fault.MigrationFault):
         name = ""

      class NicSettingMismatch(vim.fault.CustomizationFault):
         numberOfNicsInSpec = 0
         numberOfNicsInVM = 0

      class NoActiveHostInCluster(vim.fault.InvalidState):
         computeResource = vim.ComputeResource()

      class NoClientCertificate(vim.fault.VimFault):
         pass

      class NoCompatibleDatastore(vim.fault.VimFault):
         pass

      class NoCompatibleHardAffinityHost(vim.fault.VmConfigFault):
         vmName = ""

      class NoCompatibleHost(vim.fault.VimFault):
         host = [ vim.HostSystem() ]
         error = [ vmodl.MethodFault() ]

      class NoCompatibleHostWithAccessToDevice(vim.fault.NoCompatibleHost):
         pass

      class NoCompatibleSoftAffinityHost(vim.fault.VmConfigFault):
         vmName = ""

      class NoConnectedDatastore(vim.fault.VimFault):
         pass

      class NoDiskFound(vim.fault.VimFault):
         pass

      class NoDiskSpace(vim.fault.FileFault):
         datastore = ""

      class NoDisksToCustomize(vim.fault.CustomizationFault):
         pass

      class NoGateway(vim.fault.HostConfigFault):
         pass

      class NoGuestHeartbeat(vim.fault.MigrationFault):
         pass

      class NoHost(vim.fault.HostConnectFault):
         name = ""

      class NoHostSuitableForFtSecondary(vim.fault.VmFaultToleranceIssue):
         vm = vim.VirtualMachine()
         vmName = ""

      class NoPeerHostFound(vim.fault.HostPowerOpFailed):
         pass

      class NoPermissionOnAD(vim.fault.ActiveDirectoryFault):
         pass

      class NoPermissionOnHost(vim.fault.HostConnectFault):
         pass

      class NoPermissionOnNasVolume(vim.fault.NasConfigFault):
         userName = ""

      class NoSubjectName(vim.fault.VimFault):
         pass

      class NoVirtualNic(vim.fault.HostConfigFault):
         pass

      class NonADUserRequired(vim.fault.ActiveDirectoryFault):
         pass

      class NonHomeRDMVMotionNotSupported(vim.fault.MigrationFeatureNotSupported):
         device = ""

      class NotADirectory(vim.fault.FileFault):
         pass

      class NotAFile(vim.fault.FileFault):
         pass

      class NotFound(vim.fault.VimFault):
         pass

      class NotSupportedDeviceForFT(vim.fault.VmFaultToleranceIssue):
         host = vim.HostSystem()
         hostName = ""
         vm = vim.VirtualMachine()
         vmName = ""
         deviceType = ""
         deviceLabel = ""

         class DeviceType(Enum):
            virtualVmxnet3 = 0
            paraVirtualSCSIController = 1

      class NotSupportedHost(vim.fault.HostConnectFault):
         productName = ""
         productVersion = ""

      class NotSupportedHostForChecksum(vim.fault.VimFault):
         pass

      class NotSupportedHostForVFlash(vim.fault.NotSupportedHost):
         hostName = ""

      class NotSupportedHostForVmcp(vim.fault.NotSupportedHost):
         hostName = ""

      class NotSupportedHostForVmemFile(vim.fault.NotSupportedHost):
         hostName = ""

      class NotSupportedHostForVsan(vim.fault.NotSupportedHost):
         hostName = ""

      class NotSupportedHostInCluster(vim.fault.NotSupportedHost):
         pass

      class NotSupportedHostInDvs(vim.fault.NotSupportedHost):
         switchProductSpec = vim.dvs.ProductSpec()

      class NotSupportedHostInHACluster(vim.fault.NotSupportedHost):
         hostName = ""
         build = ""

      class NumVirtualCpusExceedsLimit(vim.fault.InsufficientResourcesFault):
         maxSupportedVcpus = 0

      class NumVirtualCpusIncompatible(vim.fault.VmConfigFault):
         reason = ""
         numCpu = 0

         class Reason(Enum):
            recordReplay = 0
            faultTolerance = 1

      class OperationDisabledByGuest(vim.fault.GuestOperationsFault):
         pass

      class OperationNotSupportedByGuest(vim.fault.GuestOperationsFault):
         pass

      class OutOfBounds(vim.fault.VimFault):
         argumentName = vmodl.PropertyPath()

      class OvfConsumerPowerOnFault(vim.fault.InvalidState):
         extensionKey = ""
         extensionName = ""
         description = ""

      class OvfConsumerValidationFault(vim.fault.VmConfigFault):
         extensionKey = ""
         extensionName = ""
         message = ""

      class OvfFault(vim.fault.VimFault):
         pass

      class OvfImport(vim.fault.OvfFault):
         pass

      class OvfImportFailed(vim.fault.OvfImport):
         pass

      class OvfInvalidPackage(vim.fault.OvfFault):
         lineNumber = 0

      class OvfMappedOsId(vim.fault.OvfImport):
         ovfId = 0
         ovfDescription = ""
         targetDescription = ""

      class OvfMissingHardware(vim.fault.OvfImport):
         name = ""
         resourceType = 0

      class OvfNetworkMappingNotSupported(vim.fault.OvfImport):
         pass

      class OvfProperty(vim.fault.OvfInvalidPackage):
         type = ""
         value = ""

      class OvfPropertyNetwork(vim.fault.OvfProperty):
         pass

      class OvfPropertyQualifier(vim.fault.OvfProperty):
         qualifier = ""

      class OvfPropertyQualifierDuplicate(vim.fault.OvfProperty):
         qualifier = ""

      class OvfPropertyQualifierIgnored(vim.fault.OvfProperty):
         qualifier = ""

      class OvfPropertyType(vim.fault.OvfProperty):
         pass

      class OvfPropertyValue(vim.fault.OvfProperty):
         pass

      class OvfSystemFault(vim.fault.OvfFault):
         pass

      class OvfToXmlUnsupportedElement(vim.fault.OvfSystemFault):
         name = ""

      class OvfUnknownDevice(vim.fault.OvfSystemFault):
         device = vim.vm.device.VirtualDevice()
         vmName = ""

      class OvfUnknownEntity(vim.fault.OvfSystemFault):
         lineNumber = 0

      class OvfUnsupportedDeviceBackingInfo(vim.fault.OvfSystemFault):
         elementName = ""
         instanceId = ""
         deviceName = ""
         backingName = ""

      class OvfUnsupportedDeviceBackingOption(vim.fault.OvfSystemFault):
         elementName = ""
         instanceId = ""
         deviceName = ""
         backingName = ""

      class OvfUnsupportedDiskProvisioning(vim.fault.OvfImport):
         diskProvisioning = ""
         supportedDiskProvisioning = ""

      class OvfUnsupportedPackage(vim.fault.OvfFault):
         lineNumber = 0

      class OvfUnsupportedSubType(vim.fault.OvfUnsupportedPackage):
         elementName = ""
         instanceId = ""
         deviceType = 0
         deviceSubType = ""

      class OvfUnsupportedType(vim.fault.OvfUnsupportedPackage):
         name = ""
         instanceId = ""
         deviceType = 0

      class OvfWrongNamespace(vim.fault.OvfInvalidPackage):
         namespaceName = ""

      class OvfXmlFormat(vim.fault.OvfInvalidPackage):
         description = ""

      class PasswordExpired(vim.fault.InvalidLogin):
         pass

      class PatchBinariesNotFound(vim.fault.VimFault):
         patchID = ""
         binary = [ "" ]

      class PatchMetadataInvalid(vim.fault.VimFault):
         patchID = ""
         metaData = [ "" ]

      class PatchMetadataNotFound(vim.fault.PatchMetadataInvalid):
         pass

      class PatchNotApplicable(vim.fault.VimFault):
         patchID = ""

      class PatchSuperseded(vim.fault.PatchNotApplicable):
         supersede = [ "" ]

      class PlatformConfigFault(vim.fault.HostConfigFault):
         text = ""

      class PowerOnFtSecondaryFailed(vim.fault.VmFaultToleranceIssue):
         vm = vim.VirtualMachine()
         vmName = ""
         hostSelectionBy = vim.fault.FtIssuesOnHost.HostSelectionType()
         hostErrors = [ vmodl.MethodFault() ]
         rootCause = vmodl.MethodFault()

      class ProfileUpdateFailed(vim.fault.VimFault):
         failure = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]
         warnings = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]

         class UpdateFailure(vmodl.DynamicData):
            profilePath = vim.profile.ProfilePropertyPath()
            errMsg = vmodl.LocalizableMessage()

      class QuarantineModeFault(vim.fault.VmConfigFault):
         vmName = ""
         faultType = ""

         class FaultType(Enum):
            NoCompatibleNonQuarantinedHost = 0
            CorrectionDisallowed = 1
            CorrectionImpact = 2

      class QuestionPending(vim.fault.InvalidState):
         text = ""

      class RDMConversionNotSupported(vim.fault.MigrationFault):
         device = ""

      class RDMNotPreserved(vim.fault.MigrationFault):
         device = ""

      class RDMNotSupportedOnDatastore(vim.fault.VmConfigFault):
         device = ""
         datastore = vim.Datastore()
         datastoreName = ""

      class RDMPointsToInaccessibleDisk(vim.fault.CannotAccessVmDisk):
         pass

      class ReadHostResourcePoolTreeFailed(vim.fault.HostConnectFault):
         pass

      class ReadOnlyDisksWithLegacyDestination(vim.fault.MigrationFault):
         roDiskCount = 0
         timeoutDanger = False

      class RebootRequired(vim.fault.VimFault):
         patch = ""

      class RecordReplayDisabled(vim.fault.VimFault):
         pass

      class RemoveFailed(vim.fault.VimFault):
         pass

      class ReplicationFault(vim.fault.VimFault):
         pass

      class ReplicationIncompatibleWithFT(vim.fault.ReplicationFault):
         pass

      class ReplicationInvalidOptions(vim.fault.ReplicationFault):
         options = ""
         entity = vim.ManagedEntity()

      class ReplicationNotSupportedOnHost(vim.fault.ReplicationFault):
         pass

      class ReplicationVmFault(vim.fault.ReplicationFault):
         reason = ""
         state = ""
         instanceId = ""
         vm = vim.VirtualMachine()

         class ReasonForFault(Enum):
            notConfigured = 0
            poweredOff = 1
            suspended = 2
            poweredOn = 3
            offlineReplicating = 4
            invalidState = 5
            invalidInstanceId = 6
            closeDiskError = 7
            groupExist = 8

      class ReplicationVmInProgressFault(vim.fault.ReplicationVmFault):
         requestedActivity = ""
         inProgressActivity = ""

         class Activity(Enum):
            fullSync = 0
            delta = 1

      class ResourceInUse(vim.fault.VimFault):
         type = vmodl.TypeName()
         name = ""

      class ResourceNotAvailable(vim.fault.VimFault):
         containerType = vmodl.TypeName()
         containerName = ""
         type = vmodl.TypeName()

      class RollbackFailure(vim.fault.DvsFault):
         entityName = ""
         entityType = ""

      class RuleViolation(vim.fault.VmConfigFault):
         host = vim.HostSystem()
         rule = vim.cluster.RuleInfo()

      class SSLDisabledFault(vim.fault.HostConnectFault):
         pass

      class SSLVerifyFault(vim.fault.HostConnectFault):
         selfSigned = False
         thumbprint = ""

      class SSPIChallenge(vim.fault.VimFault):
         base64Token = ""

      class SecondaryVmAlreadyDisabled(vim.fault.VmFaultToleranceIssue):
         instanceUuid = ""

      class SecondaryVmAlreadyEnabled(vim.fault.VmFaultToleranceIssue):
         instanceUuid = ""

      class SecondaryVmAlreadyRegistered(vim.fault.VmFaultToleranceIssue):
         instanceUuid = ""

      class SecondaryVmNotRegistered(vim.fault.VmFaultToleranceIssue):
         instanceUuid = ""

      class ShrinkDiskFault(vim.fault.VimFault):
         diskId = 0

      class SnapshotCopyNotSupported(vim.fault.MigrationFault):
         pass

      class SnapshotFault(vim.fault.VimFault):
         pass

      class SnapshotIncompatibleDeviceInVm(vim.fault.SnapshotFault):
         fault = vmodl.MethodFault()

      class SnapshotLocked(vim.fault.SnapshotFault):
         pass

      class SnapshotMoveFromNonHomeNotSupported(vim.fault.SnapshotCopyNotSupported):
         pass

      class SnapshotMoveNotSupported(vim.fault.SnapshotCopyNotSupported):
         pass

      class SnapshotMoveToNonHomeNotSupported(vim.fault.SnapshotCopyNotSupported):
         pass

      class SnapshotNoChange(vim.fault.SnapshotFault):
         pass

      class SnapshotRevertIssue(vim.fault.MigrationFault):
         snapshotName = ""
         event = [ vim.event.Event() ]
         errors = False

      class SoftRuleVioCorrectionDisallowed(vim.fault.VmConfigFault):
         vmName = ""

      class SoftRuleVioCorrectionImpact(vim.fault.VmConfigFault):
         vmName = ""

      class SsdDiskNotAvailable(vim.fault.VimFault):
         devicePath = ""

      class StorageDrsCannotMoveDiskInMultiWriterMode(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveFTVm(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveIndependentDisk(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveManuallyPlacedSwapFile(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveManuallyPlacedVm(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveSharedDisk(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveTemplate(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveVmInUserFolder(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveVmWithMountedCDROM(vim.fault.VimFault):
         pass

      class StorageDrsCannotMoveVmWithNoFilesInLayout(vim.fault.VimFault):
         pass

      class StorageDrsDatacentersCannotShareDatastore(vim.fault.VimFault):
         pass

      class StorageDrsDisabledOnVm(vim.fault.VimFault):
         pass

      class StorageDrsHbrDiskNotMovable(vim.fault.VimFault):
         nonMovableDiskIds = ""

      class StorageDrsHmsMoveInProgress(vim.fault.VimFault):
         pass

      class StorageDrsHmsUnreachable(vim.fault.VimFault):
         pass

      class StorageDrsIolbDisabledInternally(vim.fault.VimFault):
         pass

      class StorageDrsRelocateDisabled(vim.fault.VimFault):
         pass

      class StorageDrsStaleHmsCollection(vim.fault.VimFault):
         pass

      class StorageDrsUnableToMoveFiles(vim.fault.VimFault):
         pass

      class StorageVMotionNotSupported(vim.fault.MigrationFeatureNotSupported):
         pass

      class SuspendedRelocateNotSupported(vim.fault.MigrationFault):
         pass

      class SwapDatastoreUnset(vim.fault.VimFault):
         pass

      class SwapPlacementOverrideNotSupported(vim.fault.InvalidVmConfig):
         pass

      class SwitchIpUnset(vim.fault.DvsFault):
         pass

      class SwitchNotInUpgradeMode(vim.fault.DvsFault):
         pass

      class TaskInProgress(vim.fault.VimFault):
         task = vim.Task()

      class Timedout(vim.fault.VimFault):
         pass

      class TooManyConcurrentNativeClones(vim.fault.FileFault):
         pass

      class TooManyConsecutiveOverrides(vim.fault.VimFault):
         pass

      class TooManyDevices(vim.fault.InvalidVmConfig):
         pass

      class TooManyDisksOnLegacyHost(vim.fault.MigrationFault):
         diskCount = 0
         timeoutDanger = False

      class TooManyGuestLogons(vim.fault.GuestOperationsFault):
         pass

      class TooManyHosts(vim.fault.HostConnectFault):
         pass

      class TooManyNativeCloneLevels(vim.fault.FileFault):
         pass

      class TooManyNativeClonesOnFile(vim.fault.FileFault):
         pass

      class TooManySnapshotLevels(vim.fault.SnapshotFault):
         pass

      class ToolsAlreadyUpgraded(vim.fault.VmToolsUpgradeFault):
         pass

      class ToolsAutoUpgradeNotSupported(vim.fault.VmToolsUpgradeFault):
         pass

      class ToolsImageCopyFailed(vim.fault.VmToolsUpgradeFault):
         pass

      class ToolsImageNotAvailable(vim.fault.VmToolsUpgradeFault):
         pass

      class ToolsImageSignatureCheckFailed(vim.fault.VmToolsUpgradeFault):
         pass

      class ToolsInstallationInProgress(vim.fault.MigrationFault):
         pass

      class ToolsUnavailable(vim.fault.VimFault):
         pass

      class ToolsUpgradeCancelled(vim.fault.VmToolsUpgradeFault):
         pass

      class UncommittedUndoableDisk(vim.fault.MigrationFault):
         pass

      class UncustomizableGuest(vim.fault.CustomizationFault):
         uncustomizableGuestOS = ""

      class UnexpectedCustomizationFault(vim.fault.CustomizationFault):
         pass

      class UnrecognizedHost(vim.fault.VimFault):
         hostName = ""

      class UnsharedSwapVMotionNotSupported(vim.fault.MigrationFeatureNotSupported):
         pass

      class UnsupportedDatastore(vim.fault.VmConfigFault):
         datastore = vim.Datastore()

      class UnsupportedGuest(vim.fault.InvalidVmConfig):
         unsupportedGuestOS = ""

      class UnsupportedVimApiVersion(vim.fault.VimFault):
         version = ""

      class UnsupportedVmxLocation(vim.fault.VmConfigFault):
         pass

      class UserNotFound(vim.fault.VimFault):
         principal = ""
         unresolved = False

      class VAppConfigFault(vim.fault.VimFault):
         pass

      class VAppNotRunning(vim.fault.VmConfigFault):
         pass

      class VAppPropertyFault(vim.fault.VmConfigFault):
         id = ""
         category = ""
         label = ""
         type = ""
         value = ""

      class VAppTaskInProgress(vim.fault.TaskInProgress):
         pass

      class VFlashCacheHotConfigNotSupported(vim.fault.VmConfigFault):
         pass

      class VFlashModuleNotSupported(vim.fault.VmConfigFault):
         vmName = ""
         moduleName = ""
         reason = ""
         hostName = ""

         class Reason(Enum):
            CacheModeNotSupported = 0
            CacheConsistencyTypeNotSupported = 1
            CacheBlockSizeNotSupported = 2
            CacheReservationNotSupported = 3
            DiskSizeNotSupported = 4

      class VFlashModuleVersionIncompatible(vim.fault.VimFault):
         moduleName = ""
         vmRequestModuleVersion = ""
         hostMinSupportedVerson = ""
         hostModuleVersion = ""

      class VMotionAcrossNetworkNotSupported(vim.fault.MigrationFeatureNotSupported):
         pass

      class VMotionInterfaceIssue(vim.fault.MigrationFault):
         atSourceHost = False
         failedHost = ""
         failedHostEntity = vim.HostSystem()

      class VMotionLinkCapacityLow(vim.fault.VMotionInterfaceIssue):
         network = ""

      class VMotionLinkDown(vim.fault.VMotionInterfaceIssue):
         network = ""

      class VMotionNotConfigured(vim.fault.VMotionInterfaceIssue):
         pass

      class VMotionNotLicensed(vim.fault.VMotionInterfaceIssue):
         pass

      class VMotionNotSupported(vim.fault.VMotionInterfaceIssue):
         pass

      class VMotionProtocolIncompatible(vim.fault.MigrationFault):
         pass

      class VirtualHardwareCompatibilityIssue(vim.fault.VmConfigFault):
         pass

      class VirtualHardwareVersionNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         hostName = ""
         host = vim.HostSystem()

      class VmAlreadyExistsInDatacenter(vim.fault.InvalidFolder):
         host = vim.HostSystem()
         hostname = ""
         vm = [ vim.VirtualMachine() ]

      class VmFaultToleranceConfigIssue(vim.fault.VmFaultToleranceIssue):
         reason = ""
         entityName = ""
         entity = vim.ManagedEntity()

         class ReasonForIssue(Enum):
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

      class VmFaultToleranceConfigIssueWrapper(vim.fault.VmFaultToleranceIssue):
         entityName = ""
         entity = vim.ManagedEntity()
         error = vmodl.MethodFault()

      class VmFaultToleranceInvalidFileBacking(vim.fault.VmFaultToleranceIssue):
         backingType = ""
         backingFilename = ""

         class DeviceType(Enum):
            virtualFloppy = 0
            virtualCdrom = 1
            virtualSerialPort = 2
            virtualParallelPort = 3
            virtualDisk = 4

      class VmFaultToleranceTooManyFtVcpusOnHost(vim.fault.InsufficientResourcesFault):
         hostName = ""
         maxNumFtVcpus = 0

      class VmFaultToleranceTooManyVMsOnHost(vim.fault.InsufficientResourcesFault):
         hostName = ""
         maxNumFtVms = 0

      class VmPowerOnDisabled(vim.fault.InvalidState):
         pass

      class VmSmpFaultToleranceTooManyVMsOnHost(vim.fault.InsufficientResourcesFault):
         hostName = ""
         maxNumSmpFtVms = 0

      class VmWwnConflict(vim.fault.InvalidVmConfig):
         vm = vim.VirtualMachine()
         host = vim.HostSystem()
         name = ""
         wwn = 0

      class VmfsMountFault(vim.fault.HostConfigFault):
         uuid = ""

      class VmotionInterfaceNotEnabled(vim.fault.HostPowerOpFailed):
         pass

      class VolumeEditorError(vim.fault.CustomizationFault):
         pass

      class VsanClusterUuidMismatch(vim.fault.CannotMoveVsanEnabledHost):
         hostClusterUuid = ""
         destinationClusterUuid = ""

      class VsanDiskFault(vim.fault.VsanFault):
         device = ""

      class VsanIncompatibleDiskMapping(vim.fault.VsanDiskFault):
         pass

      class VspanDestPortConflict(vim.fault.DvsFault):
         vspanSessionKey1 = ""
         vspanSessionKey2 = ""
         portKey = ""

      class VspanPortConflict(vim.fault.DvsFault):
         vspanSessionKey1 = ""
         vspanSessionKey2 = ""
         portKey = ""

      class VspanPortMoveFault(vim.fault.DvsFault):
         srcPortgroupName = ""
         destPortgroupName = ""
         portKey = ""

      class VspanPortPromiscChangeFault(vim.fault.DvsFault):
         portKey = ""

      class VspanPortgroupPromiscChangeFault(vim.fault.DvsFault):
         portgroupName = ""

      class VspanPortgroupTypeChangeFault(vim.fault.DvsFault):
         portgroupName = ""

      class VspanPromiscuousPortNotSupported(vim.fault.DvsFault):
         vspanSessionKey = ""
         portKey = ""

      class VspanSameSessionPortConflict(vim.fault.DvsFault):
         vspanSessionKey = ""
         portKey = ""

      class WakeOnLanNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         pass

      class WakeOnLanNotSupportedByVmotionNIC(vim.fault.HostPowerOpFailed):
         pass

      class WillLoseHAProtection(vim.fault.MigrationFault):
         resolution = ""

         class Resolution(Enum):
            svmotion = 0
            relocate = 1

      class WillModifyConfigCpuRequirements(vim.fault.MigrationFault):
         pass

      class WillResetSnapshotDirectory(vim.fault.MigrationFault):
         pass

      class ActiveVMsBlockingEVC(vim.fault.EVCConfigFault):
         evcMode = ""
         host = [ vim.HostSystem() ]
         hostName = [ "" ]

      class AdminDisabled(vim.fault.HostConfigFault):
         pass

      class AdminNotDisabled(vim.fault.HostConfigFault):
         pass

      class AffinityConfigured(vim.fault.MigrationFault):
         configuredAffinity = [ "" ]

         class Affinity(Enum):
            memory = 0
            cpu = 1

      class AgentInstallFailed(vim.fault.HostConnectFault):
         reason = ""
         statusCode = 0
         installerOutput = ""

         class Reason(Enum):
            NotEnoughSpaceOnDevice = 0
            PrepareToUpgradeFailed = 1
            AgentNotRunning = 2
            AgentNotReachable = 3
            InstallTimedout = 4
            SignatureVerificationFailed = 5
            AgentUploadFailed = 6
            AgentUploadTimedout = 7
            UnknownInstallerError = 8

      class AlreadyBeingManaged(vim.fault.HostConnectFault):
         ipAddress = ""

      class AlreadyConnected(vim.fault.HostConnectFault):
         name = ""

      class ApplicationQuiesceFault(vim.fault.SnapshotFault):
         pass

      class BackupBlobReadFailure(vim.fault.DvsFault):
         entityName = ""
         entityType = ""
         fault = vmodl.MethodFault()

      class BackupBlobWriteFailure(vim.fault.DvsFault):
         entityName = ""
         entityType = ""
         fault = vmodl.MethodFault()

      class BlockedByFirewall(vim.fault.HostConfigFault):
         pass

      class CAMServerRefusedConnection(vim.fault.InvalidCAMServer):
         pass

      class CannotAccessFile(vim.fault.FileFault):
         pass

      class CannotAccessNetwork(vim.fault.CannotAccessVmDevice):
         network = vim.Network()

      class CannotAddHostWithFTVmAsStandalone(vim.fault.HostConnectFault):
         pass

      class CannotAddHostWithFTVmToDifferentCluster(vim.fault.HostConnectFault):
         pass

      class CannotAddHostWithFTVmToNonHACluster(vim.fault.HostConnectFault):
         pass

      class CannotCreateFile(vim.fault.FileFault):
         pass

      class CannotDecryptPasswords(vim.fault.CustomizationFault):
         pass

      class CannotDeleteFile(vim.fault.FileFault):
         pass

      class CannotModifyConfigCpuRequirements(vim.fault.MigrationFault):
         pass

      class CannotMoveVmWithDeltaDisk(vim.fault.MigrationFault):
         device = ""

      class CannotMoveVmWithNativeDeltaDisk(vim.fault.MigrationFault):
         pass

      class CannotPowerOffVmInCluster(vim.fault.InvalidState):
         operation = ""
         vm = vim.VirtualMachine()
         vmName = ""

         class Operation(Enum):
            suspend = 0
            powerOff = 1
            guestShutdown = 2
            guestSuspend = 3

      class ClockSkew(vim.fault.HostConfigFault):
         pass

      class CloneFromSnapshotNotSupported(vim.fault.MigrationFault):
         pass

      class CollectorAddressUnset(vim.fault.DvsFault):
         pass

      class ConflictingConfiguration(vim.fault.DvsFault):
         configInConflict = [ vim.fault.ConflictingConfiguration.Config() ]

         class Config(vmodl.DynamicData):
            entity = vim.ManagedEntity()
            propertyPath = ""

      class CpuIncompatible(vim.fault.VirtualHardwareCompatibilityIssue):
         level = 0
         registerName = ""
         registerBits = ""
         desiredBits = ""
         host = vim.HostSystem()

      class CpuIncompatible1ECX(vim.fault.CpuIncompatible):
         sse3 = False
         pclmulqdq = False
         ssse3 = False
         sse41 = False
         sse42 = False
         aes = False
         other = False
         otherOnly = False

      class CpuIncompatible81EDX(vim.fault.CpuIncompatible):
         nx = False
         ffxsr = False
         rdtscp = False
         lm = False
         other = False
         otherOnly = False

      class DatacenterMismatch(vim.fault.MigrationFault):
         invalidArgument = [ vim.fault.DatacenterMismatch.Argument() ]
         expectedDatacenter = vim.Datacenter()

         class Argument(vmodl.DynamicData):
            entity = vim.ManagedEntity()
            inputDatacenter = vim.Datacenter()

      class DatastoreNotWritableOnHost(vim.fault.InvalidDatastore):
         host = vim.HostSystem()

      class DestinationSwitchFull(vim.fault.CannotAccessNetwork):
         pass

      class DeviceNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         device = ""
         reason = ""

         class Reason(Enum):
            host = 0
            guest = 1
            ft = 2

      class DigestNotSupported(vim.fault.DeviceNotSupported):
         pass

      class DirectoryNotEmpty(vim.fault.FileFault):
         pass

      class DisableAdminNotSupported(vim.fault.HostConfigFault):
         pass

      class DisallowedMigrationDeviceAttached(vim.fault.MigrationFault):
         fault = vmodl.MethodFault()

      class DisconnectedHostsBlockingEVC(vim.fault.EVCConfigFault):
         pass

      class DiskHasPartitions(vim.fault.VsanDiskFault):
         pass

      class DiskIsLastRemainingNonSSD(vim.fault.VsanDiskFault):
         pass

      class DiskIsNonLocal(vim.fault.VsanDiskFault):
         pass

      class DiskIsUSB(vim.fault.VsanDiskFault):
         pass

      class DiskMoveTypeNotSupported(vim.fault.MigrationFault):
         pass

      class DiskNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         disk = 0

      class DiskTooSmall(vim.fault.VsanDiskFault):
         pass

      class DrsVmotionIncompatibleFault(vim.fault.VirtualHardwareCompatibilityIssue):
         host = vim.HostSystem()

      class DuplicateDisks(vim.fault.VsanDiskFault):
         pass

      class DvsApplyOperationFault(vim.fault.DvsFault):
         objectFault = [ vim.fault.DvsApplyOperationFault.FaultOnObject() ]

         class FaultOnObject(vmodl.DynamicData):
            objectId = ""
            type = vmodl.TypeName()
            fault = vmodl.MethodFault()

      class EVCAdmissionFailed(vim.fault.NotSupportedHostInCluster):
         faults = [ vmodl.MethodFault() ]

      class EVCAdmissionFailedCPUFeaturesForMode(vim.fault.EVCAdmissionFailed):
         currentEVCModeKey = ""

      class EVCAdmissionFailedCPUModel(vim.fault.EVCAdmissionFailed):
         pass

      class EVCAdmissionFailedCPUModelForMode(vim.fault.EVCAdmissionFailed):
         currentEVCModeKey = ""

      class EVCAdmissionFailedCPUVendor(vim.fault.EVCAdmissionFailed):
         clusterCPUVendor = ""
         hostCPUVendor = ""

      class EVCAdmissionFailedCPUVendorUnknown(vim.fault.EVCAdmissionFailed):
         pass

      class EVCAdmissionFailedHostDisconnected(vim.fault.EVCAdmissionFailed):
         pass

      class EVCAdmissionFailedHostSoftware(vim.fault.EVCAdmissionFailed):
         pass

      class EVCAdmissionFailedHostSoftwareForMode(vim.fault.EVCAdmissionFailed):
         pass

      class EVCAdmissionFailedVmActive(vim.fault.EVCAdmissionFailed):
         pass

      class EncryptionKeyRequired(vim.fault.InvalidState):
         requiredKey = [ vim.encryption.CryptoKeyId() ]

      class FailToEnableSPBM(vmodl.fault.NotEnoughLicenses):
         cs = vim.ComputeResource()
         csName = ""
         hostLicenseStates = [ vim.ComputeResource.HostSPBMLicenseInfo() ]

      class FaultToleranceAntiAffinityViolated(vim.fault.MigrationFault):
         hostName = ""
         host = vim.HostSystem()

      class FaultToleranceCpuIncompatible(vim.fault.CpuIncompatible):
         model = False
         family = False
         stepping = False

      class FaultToleranceNeedsThickDisk(vim.fault.MigrationFault):
         vmName = ""

      class FaultToleranceNotSameBuild(vim.fault.MigrationFault):
         build = ""

      class FeatureRequirementsNotMet(vim.fault.VirtualHardwareCompatibilityIssue):
         featureRequirement = [ vim.vm.FeatureRequirement() ]
         vm = vim.VirtualMachine()
         host = vim.HostSystem()

      class FileAlreadyExists(vim.fault.FileFault):
         pass

      class FileBackedPortNotSupported(vim.fault.DeviceNotSupported):
         pass

      class FilesystemQuiesceFault(vim.fault.SnapshotFault):
         pass

      class FilterInUse(vim.fault.ResourceInUse):
         disk = [ vim.vm.device.VirtualDiskId() ]

      class FullStorageVMotionNotSupported(vim.fault.MigrationFeatureNotSupported):
         pass

      class GatewayConnectFault(vim.fault.HostConnectFault):
         gatewayType = ""
         gatewayId = ""
         gatewayInfo = ""
         details = vmodl.LocalizableMessage()

      class GatewayNotFound(vim.fault.GatewayConnectFault):
         pass

      class GatewayNotReachable(vim.fault.GatewayConnectFault):
         pass

      class GatewayOperationRefused(vim.fault.GatewayConnectFault):
         pass

      class GatewayToHostConnectFault(vim.fault.GatewayConnectFault):
         hostname = ""
         port = 0

      class GatewayToHostTrustVerifyFault(vim.fault.GatewayToHostConnectFault):
         verificationToken = ""
         propertiesToVerify = [ vim.KeyValue() ]

      class GuestAuthenticationChallenge(vim.fault.GuestOperationsFault):
         serverChallenge = vim.vm.guest.GuestAuthentication()
         sessionID = 0

      class GuestComponentsOutOfDate(vim.fault.GuestOperationsFault):
         pass

      class GuestMultipleMappings(vim.fault.GuestOperationsFault):
         pass

      class GuestRegistryKeyAlreadyExists(vim.fault.GuestRegistryKeyFault):
         pass

      class HAErrorsAtDest(vim.fault.MigrationFault):
         pass

      class HostConfigFailed(vim.fault.HostConfigFault):
         failure = [ vmodl.MethodFault() ]

      class HotSnapshotMoveNotSupported(vim.fault.SnapshotCopyNotSupported):
         pass

      class IDEDiskNotSupported(vim.fault.DiskNotSupported):
         pass

      class InaccessibleDatastore(vim.fault.InvalidDatastore):
         detail = ""

      class InaccessibleFTMetadataDatastore(vim.fault.InaccessibleDatastore):
         pass

      class IncompatibleDefaultDevice(vim.fault.MigrationFault):
         device = ""

      class IncompatibleHostForVmReplication(vim.fault.ReplicationFault):
         vmName = ""
         hostName = ""
         reason = ""

         class IncompatibleReason(Enum):
            rpo = 0
            netCompression = 1

      class IndependentDiskVMotionNotSupported(vim.fault.MigrationFeatureNotSupported):
         pass

      class InsufficientAgentVmsDeployed(vim.fault.InsufficientResourcesFault):
         hostName = ""
         requiredNumAgentVms = 0
         currentNumAgentVms = 0

      class InsufficientCpuResourcesFault(vim.fault.InsufficientResourcesFault):
         unreserved = 0
         requested = 0

      class InsufficientDisks(vim.fault.VsanDiskFault):
         pass

      class InsufficientFailoverResourcesFault(vim.fault.InsufficientResourcesFault):
         pass

      class InsufficientGraphicsResourcesFault(vim.fault.InsufficientResourcesFault):
         pass

      class InsufficientHostCapacityFault(vim.fault.InsufficientResourcesFault):
         host = vim.HostSystem()

      class InsufficientHostCpuCapacityFault(vim.fault.InsufficientHostCapacityFault):
         unreserved = 0
         requested = 0

      class InsufficientHostMemoryCapacityFault(vim.fault.InsufficientHostCapacityFault):
         unreserved = 0
         requested = 0

      class InsufficientMemoryResourcesFault(vim.fault.InsufficientResourcesFault):
         unreserved = 0
         requested = 0

      class InsufficientNetworkCapacity(vim.fault.InsufficientResourcesFault):
         pass

      class InsufficientNetworkResourcePoolCapacity(vim.fault.InsufficientResourcesFault):
         dvsName = ""
         dvsUuid = ""
         resourcePoolKey = ""
         available = 0
         requested = 0
         device = [ "" ]

      class InsufficientPerCpuCapacity(vim.fault.InsufficientHostCapacityFault):
         pass

      class InsufficientStandbyCpuResource(vim.fault.InsufficientStandbyResource):
         available = 0
         requested = 0

      class InsufficientStandbyMemoryResource(vim.fault.InsufficientStandbyResource):
         available = 0
         requested = 0

      class InvalidBundle(vim.fault.PlatformConfigFault):
         pass

      class InvalidCAMCertificate(vim.fault.InvalidCAMServer):
         pass

      class InvalidClientCertificate(vim.fault.InvalidLogin):
         pass

      class InvalidDatastoreState(vim.fault.InvalidState):
         datastoreName = ""

      class InvalidDeviceSpec(vim.fault.InvalidVmConfig):
         deviceIndex = 0

      class InvalidDiskFormat(vim.fault.InvalidFormat):
         pass

      class InvalidHostState(vim.fault.InvalidState):
         host = vim.HostSystem()

      class InvalidNasCredentials(vim.fault.NasConfigFault):
         userName = ""

      class InvalidNetworkInType(vim.fault.VAppPropertyFault):
         pass

      class InvalidNetworkResource(vim.fault.NasConfigFault):
         remoteHost = ""
         remotePath = ""

      class InvalidPowerState(vim.fault.InvalidState):
         requestedState = vim.VirtualMachine.PowerState()
         existingState = vim.VirtualMachine.PowerState()

      class InvalidPropertyType(vim.fault.VAppPropertyFault):
         pass

      class InvalidPropertyValue(vim.fault.VAppPropertyFault):
         pass

      class LargeRDMConversionNotSupported(vim.fault.MigrationFault):
         device = ""

      class LegacyNetworkInterfaceInUse(vim.fault.CannotAccessNetwork):
         pass

      class MaintenanceModeFileMove(vim.fault.MigrationFault):
         pass

      class MemoryFileFormatNotSupportedByDatastore(vim.fault.UnsupportedDatastore):
         datastoreName = ""
         type = ""

      class MemorySizeNotRecommended(vim.fault.VirtualHardwareCompatibilityIssue):
         memorySizeMB = 0
         minMemorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySizeNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         memorySizeMB = 0
         minMemorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySizeNotSupportedByDatastore(vim.fault.VirtualHardwareCompatibilityIssue):
         datastore = vim.Datastore()
         memorySizeMB = 0
         maxMemorySizeMB = 0

      class MemorySnapshotOnIndependentDisk(vim.fault.SnapshotFault):
         pass

      class MigrationDisabled(vim.fault.MigrationFault):
         pass

      class MissingController(vim.fault.InvalidDeviceSpec):
         pass

      class MissingIpPool(vim.fault.VAppPropertyFault):
         pass

      class MissingNetworkIpConfig(vim.fault.VAppPropertyFault):
         pass

      class MissingPowerOffConfiguration(vim.fault.VAppConfigFault):
         pass

      class MissingPowerOnConfiguration(vim.fault.VAppConfigFault):
         pass

      class MultiWriterNotSupported(vim.fault.DeviceNotSupported):
         pass

      class MultipleSnapshotsNotSupported(vim.fault.SnapshotFault):
         pass

      class NoAvailableIp(vim.fault.VAppPropertyFault):
         network = vim.Network()

      class NoVcManagedIpConfigured(vim.fault.VAppPropertyFault):
         pass

      class NoVmInVApp(vim.fault.VAppConfigFault):
         pass

      class NonPersistentDisksNotSupported(vim.fault.DeviceNotSupported):
         pass

      class NonVmwareOuiMacNotSupportedHost(vim.fault.NotSupportedHost):
         hostName = ""

      class NotEnoughCpus(vim.fault.VirtualHardwareCompatibilityIssue):
         numCpuDest = 0
         numCpuVm = 0

      class NotEnoughLogicalCpus(vim.fault.NotEnoughCpus):
         host = vim.HostSystem()

      class NotUserConfigurableProperty(vim.fault.VAppPropertyFault):
         pass

      class NumVirtualCoresPerSocketNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         maxSupportedCoresPerSocketDest = 0
         numCoresPerSocketVm = 0

      class NumVirtualCpusNotSupported(vim.fault.VirtualHardwareCompatibilityIssue):
         maxSupportedVcpusDest = 0
         numCpuVm = 0

      class OvfAttribute(vim.fault.OvfInvalidPackage):
         elementName = ""
         attributeName = ""

      class OvfConstraint(vim.fault.OvfInvalidPackage):
         name = ""

      class OvfConsumerCallbackFault(vim.fault.OvfFault):
         extensionKey = ""
         extensionName = ""

      class OvfConsumerCommunicationError(vim.fault.OvfConsumerCallbackFault):
         description = ""

      class OvfConsumerFault(vim.fault.OvfConsumerCallbackFault):
         errorKey = ""
         message = ""
         params = [ vim.KeyValue() ]

      class OvfConsumerInvalidSection(vim.fault.OvfConsumerCallbackFault):
         lineNumber = 0
         description = ""

      class OvfConsumerUndeclaredSection(vim.fault.OvfConsumerCallbackFault):
         qualifiedSectionType = ""

      class OvfConsumerUndefinedPrefix(vim.fault.OvfConsumerCallbackFault):
         prefix = ""

      class OvfCpuCompatibility(vim.fault.OvfImport):
         registerName = ""
         level = 0
         registerValue = ""
         desiredRegisterValue = ""

      class OvfCpuCompatibilityCheckNotSupported(vim.fault.OvfImport):
         pass

      class OvfDiskMappingNotFound(vim.fault.OvfSystemFault):
         diskName = ""
         vmName = ""

      class OvfDiskOrderConstraint(vim.fault.OvfConstraint):
         pass

      class OvfElement(vim.fault.OvfInvalidPackage):
         name = ""

      class OvfElementInvalidValue(vim.fault.OvfElement):
         value = ""

      class OvfExport(vim.fault.OvfFault):
         pass

      class OvfExportFailed(vim.fault.OvfExport):
         pass

      class OvfHardwareCheck(vim.fault.OvfImport):
         pass

      class OvfHardwareExport(vim.fault.OvfExport):
         device = vim.vm.device.VirtualDevice()
         vmPath = ""

      class OvfHostResourceConstraint(vim.fault.OvfConstraint):
         value = ""

      class OvfHostValueNotParsed(vim.fault.OvfSystemFault):
         property = ""
         value = ""

      class OvfInternalError(vim.fault.OvfSystemFault):
         pass

      class OvfInvalidValue(vim.fault.OvfAttribute):
         value = ""

      class OvfInvalidValueConfiguration(vim.fault.OvfInvalidValue):
         pass

      class OvfInvalidValueEmpty(vim.fault.OvfInvalidValue):
         pass

      class OvfInvalidValueFormatMalformed(vim.fault.OvfInvalidValue):
         pass

      class OvfInvalidValueReference(vim.fault.OvfInvalidValue):
         pass

      class OvfInvalidVmName(vim.fault.OvfUnsupportedPackage):
         name = ""

      class OvfMissingAttribute(vim.fault.OvfAttribute):
         pass

      class OvfMissingElement(vim.fault.OvfElement):
         pass

      class OvfMissingElementNormalBoundary(vim.fault.OvfMissingElement):
         boundary = ""

      class OvfNoHostNic(vim.fault.OvfUnsupportedPackage):
         pass

      class OvfNoSupportedHardwareFamily(vim.fault.OvfUnsupportedPackage):
         version = ""

      class OvfPropertyExport(vim.fault.OvfExport):
         type = ""
         value = ""

      class OvfPropertyNetworkExport(vim.fault.OvfExport):
         network = ""

      class OvfUnableToExportDisk(vim.fault.OvfHardwareExport):
         diskName = ""

      class OvfUnexpectedElement(vim.fault.OvfElement):
         pass

      class OvfUnknownDeviceBacking(vim.fault.OvfHardwareExport):
         backing = vim.vm.device.VirtualDevice.BackingInfo()

      class OvfUnsupportedAttribute(vim.fault.OvfUnsupportedPackage):
         elementName = ""
         attributeName = ""

      class OvfUnsupportedAttributeValue(vim.fault.OvfUnsupportedAttribute):
         value = ""

      class OvfUnsupportedDeviceExport(vim.fault.OvfHardwareExport):
         pass

      class OvfUnsupportedElement(vim.fault.OvfUnsupportedPackage):
         name = ""

      class OvfUnsupportedElementValue(vim.fault.OvfUnsupportedElement):
         value = ""

      class OvfUnsupportedSection(vim.fault.OvfUnsupportedElement):
         info = ""

      class OvfWrongElement(vim.fault.OvfElement):
         pass

      class PatchAlreadyInstalled(vim.fault.PatchNotApplicable):
         pass

      class PatchInstallFailed(vim.fault.PlatformConfigFault):
         rolledBack = False

      class PatchIntegrityError(vim.fault.PlatformConfigFault):
         pass

      class PatchMetadataCorrupted(vim.fault.PatchMetadataInvalid):
         pass

      class PatchMissingDependencies(vim.fault.PatchNotApplicable):
         prerequisitePatch = [ "" ]
         prerequisiteLib = [ "" ]

      class PowerOnFtSecondaryTimedout(vim.fault.Timedout):
         vm = vim.VirtualMachine()
         vmName = ""
         timeout = 0

      class QuiesceDatastoreIOForHAFailed(vim.fault.ResourceInUse):
         host = vim.HostSystem()
         hostName = ""
         ds = vim.Datastore()
         dsName = ""

      class RDMNotSupported(vim.fault.DeviceNotSupported):
         pass

      class RawDiskNotSupported(vim.fault.DeviceNotSupported):
         pass

      class RemoteDeviceNotSupported(vim.fault.DeviceNotSupported):
         pass

      class ReplicationConfigFault(vim.fault.ReplicationFault):
         pass

      class ReplicationDiskConfigFault(vim.fault.ReplicationConfigFault):
         reason = ""
         vmRef = vim.VirtualMachine()
         key = 0

         class ReasonForFault(Enum):
            diskNotFound = 0
            diskTypeNotSupported = 1
            invalidDiskKey = 2
            invalidDiskReplicationId = 3
            duplicateDiskReplicationId = 4
            invalidPersistentFilePath = 5
            reconfigureDiskReplicationIdNotAllowed = 6

      class ReplicationVmConfigFault(vim.fault.ReplicationConfigFault):
         reason = ""
         vmRef = vim.VirtualMachine()

         class ReasonForFault(Enum):
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

      class SharedBusControllerNotSupported(vim.fault.DeviceNotSupported):
         pass

      class SnapshotCloneNotSupported(vim.fault.SnapshotCopyNotSupported):
         pass

      class SnapshotDisabled(vim.fault.SnapshotFault):
         pass

      class StorageVmotionIncompatible(vim.fault.VirtualHardwareCompatibilityIssue):
         datastore = vim.Datastore()

      class SwapDatastoreNotWritableOnHost(vim.fault.DatastoreNotWritableOnHost):
         pass

      class UnSupportedDatastoreForVFlash(vim.fault.UnsupportedDatastore):
         datastoreName = ""
         type = ""

      class UnconfiguredPropertyValue(vim.fault.InvalidPropertyValue):
         pass

      class VMINotSupported(vim.fault.DeviceNotSupported):
         pass

      class VMOnConflictDVPort(vim.fault.CannotAccessNetwork):
         pass

      class VMOnVirtualIntranet(vim.fault.CannotAccessNetwork):
         pass

      class VirtualDiskModeNotSupported(vim.fault.DeviceNotSupported):
         mode = ""

      class VirtualEthernetCardNotSupported(vim.fault.DeviceNotSupported):
         pass

      class VmfsAlreadyMounted(vim.fault.VmfsMountFault):
         pass

      class VmfsAmbiguousMount(vim.fault.VmfsMountFault):
         pass

      class ConnectedIso(vim.fault.OvfExport):
         cdrom = vim.vm.device.VirtualCdrom()
         filename = ""

      class CpuCompatibilityUnknown(vim.fault.CpuIncompatible):
         pass

      class DeviceBackingNotSupported(vim.fault.DeviceNotSupported):
         backing = ""

      class DeviceControllerNotSupported(vim.fault.DeviceNotSupported):
         controller = ""

      class DeviceHotPlugNotSupported(vim.fault.InvalidDeviceSpec):
         pass

      class DeviceNotFound(vim.fault.InvalidDeviceSpec):
         pass

      class DeviceUnsupportedForVmPlatform(vim.fault.InvalidDeviceSpec):
         pass

      class DeviceUnsupportedForVmVersion(vim.fault.InvalidDeviceSpec):
         currentVersion = ""
         expectedVersion = ""

      class DisallowedDiskModeChange(vim.fault.InvalidDeviceSpec):
         pass

      class GatewayHostNotReachable(vim.fault.GatewayToHostConnectFault):
         pass

      class GatewayToHostAuthFault(vim.fault.GatewayToHostConnectFault):
         invalidProperties = [ "" ]
         missingProperties = [ "" ]

      class InvalidController(vim.fault.InvalidDeviceSpec):
         controllerKey = 0

      class InvalidDeviceBacking(vim.fault.InvalidDeviceSpec):
         pass

      class InvalidDeviceOperation(vim.fault.InvalidDeviceSpec):
         badOp = vim.vm.device.VirtualDeviceSpec.Operation()
         badFileOp = vim.vm.device.VirtualDeviceSpec.FileOperation()

      class InvalidHostConnectionState(vim.fault.InvalidHostState):
         pass

      class OvfConnectedDevice(vim.fault.OvfHardwareExport):
         pass

      class OvfConnectedDeviceFloppy(vim.fault.OvfConnectedDevice):
         filename = ""

      class OvfConnectedDeviceIso(vim.fault.OvfConnectedDevice):
         filename = ""

      class OvfDuplicateElement(vim.fault.OvfElement):
         pass

      class OvfDuplicatedElementBoundary(vim.fault.OvfElement):
         boundary = ""

      class OvfDuplicatedPropertyIdExport(vim.fault.OvfExport):
         fqid = ""

      class OvfDuplicatedPropertyIdImport(vim.fault.OvfExport):
         pass

      class OvfNoSpaceOnController(vim.fault.OvfUnsupportedElement):
         parent = ""

      class PhysCompatRDMNotSupported(vim.fault.RDMNotSupported):
         pass

      class UnusedVirtualDiskBlocksNotScrubbed(vim.fault.DeviceBackingNotSupported):
         pass

      class VirtualDiskBlocksNotFullyProvisioned(vim.fault.DeviceBackingNotSupported):
         pass

      class DVPortNotSupported(vim.fault.DeviceBackingNotSupported):
         pass

   class host(object):

      class ActiveDirectorySpec(vmodl.DynamicData):
         changeOperation = ""
         spec = vim.host.ActiveDirectorySpec.Specification()

         class Specification(vmodl.DynamicData):
            domainName = ""
            userName = ""
            password = ""
            camServer = ""
            thumbprint = ""
            smartCardAuthenticationEnabled = False
            smartCardTrustAnchors = [ "" ]

      class AssignableHardwareBinding(vmodl.DynamicData):
         instanceId = ""
         vm = vim.VirtualMachine()

      class AssignableHardwareConfig(vmodl.DynamicData):
         attributeOverride = [ vim.host.AssignableHardwareConfig.AttributeOverride() ]

         class AttributeOverride(vmodl.DynamicData):
            instanceId = ""
            name = ""
            value = anyType()

      class AssignableHardwareManager(vmodl.ManagedObject):
         binding = [ vim.host.AssignableHardwareBinding() ]
         config = vim.host.AssignableHardwareConfig()

         def downloadDescriptionTree():
            return vmodl.Binary()

         def retrieveDynamicPassthroughInfo():
            return [ vim.vm.DynamicPassthroughInfo() ]

         def updateConfig(config=vim.host.AssignableHardwareConfig()):
            # throws vim.fault.HostConfigFault
            return None

      class AuthenticationManager(vmodl.ManagedObject):
         info = vim.host.AuthenticationManagerInfo()
         supportedStore = [ vim.host.AuthenticationStore() ]

      class AuthenticationManagerInfo(vmodl.DynamicData):
         authConfig = [ vim.host.AuthenticationStoreInfo() ]

      class AuthenticationStore(vmodl.ManagedObject):
         info = vim.host.AuthenticationStoreInfo()

      class AuthenticationStoreInfo(vmodl.DynamicData):
         enabled = False

      class AutoStartManager(vmodl.ManagedObject):
         config = vim.host.AutoStartManager.Config()

         def reconfigure(spec=vim.host.AutoStartManager.Config()):
            return None

         def autoPowerOn():
            return None

         def autoPowerOff():
            return None

         class Action(Enum):
            none = 0
            systemDefault = 1
            powerOn = 2
            powerOff = 3
            guestShutdown = 4
            suspend = 5

         class SystemDefaults(vmodl.DynamicData):
            enabled = False
            startDelay = 0
            stopDelay = 0
            waitForHeartbeat = False
            stopAction = ""

         class AutoPowerInfo(vmodl.DynamicData):
            key = vim.VirtualMachine()
            startOrder = 0
            startDelay = 0
            waitForHeartbeat = vim.host.AutoStartManager.AutoPowerInfo.WaitHeartbeatSetting()
            startAction = ""
            stopDelay = 0
            stopAction = ""

            class WaitHeartbeatSetting(Enum):
               yes = 0
               no = 1
               systemDefault = 2

         class Config(vmodl.DynamicData):
            defaults = vim.host.AutoStartManager.SystemDefaults()
            powerInfo = [ vim.host.AutoStartManager.AutoPowerInfo() ]

      class BIOSInfo(vmodl.DynamicData):
         biosVersion = ""
         releaseDate = vmodl.DateTime()
         vendor = ""
         majorRelease = 0
         minorRelease = 0
         firmwareMajorRelease = 0
         firmwareMinorRelease = 0

      class BootDeviceSystem(vmodl.ManagedObject):

         def queryBootDevices():
            return vim.host.BootDeviceInfo()

         def updateBootDevice(key=""):
            return None

         class BootDevice(vmodl.DynamicData):
            key = ""
            description = ""

      class CacheConfigurationManager(vmodl.ManagedObject):
         cacheConfigurationInfo = [ vim.host.CacheConfigurationManager.CacheConfigurationInfo() ]

         def configureCache(spec=vim.host.CacheConfigurationManager.CacheConfigurationSpec()):
            return vim.Task()

         class CacheConfigurationSpec(vmodl.DynamicData):
            datastore = vim.Datastore()
            swapSize = 0

         class CacheConfigurationInfo(vmodl.DynamicData):
            key = vim.Datastore()
            swapSize = 0

      class Capability(vmodl.DynamicData):
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

         class ReplayUnsupportedReason(Enum):
            incompatibleProduct = 0
            incompatibleCpu = 1
            hvDisabled = 2
            cpuidLimitSet = 3
            oldBIOS = 4
            unknown = 5

         class FtUnsupportedReason(Enum):
            vMotionNotLicensed = 0
            missingVMotionNic = 1
            missingFTLoggingNic = 2
            ftNotLicensed = 3
            haAgentIssue = 4
            unsupportedProduct = 5
            cpuHvUnsupported = 6
            cpuHwmmuUnsupported = 7
            cpuHvDisabled = 8

         class VmDirectPathGen2UnsupportedReason(Enum):
            hostNptIncompatibleProduct = 0
            hostNptIncompatibleHardware = 1
            hostNptDisabled = 2

         class UnmapMethodSupported(Enum):
            priority = 0
            fixed = 1
            dynamic = 2

      class CertificateManager(vmodl.ManagedObject):
         certificateInfo = vim.host.CertificateManager.CertificateInfo()

         def generateCertificateSigningRequest(useIpAddressAsCommonName=False):
            # throws vim.fault.HostConfigFault
            return ""

         def generateCertificateSigningRequestByDn(distinguishedName=""):
            # throws vim.fault.HostConfigFault
            return ""

         def installServerCertificate(cert=""):
            # throws vim.fault.HostConfigFault
            return None

         def replaceCACertificatesAndCRLs(caCert=[ "" ], caCrl=[ "" ] or None):
            # throws vim.fault.HostConfigFault
            return None

         def listCACertificates():
            # throws vim.fault.HostConfigFault
            return [ "" ]

         def listCACertificateRevocationLists():
            # throws vim.fault.HostConfigFault
            return [ "" ]

         class CertificateInfo(vmodl.DynamicData):
            issuer = ""
            notBefore = vmodl.DateTime()
            notAfter = vmodl.DateTime()
            subject = ""
            status = ""

            class CertificateStatus(Enum):
               unknown = 0
               expired = 1
               expiring = 2
               expiringShortly = 3
               expirationImminent = 4
               good = 5
               revoked = 6

      class ConfigChange(vmodl.DynamicData):

         class Mode(Enum):
            modify = 0
            replace = 1

         class Operation(Enum):
            add = 0
            remove = 1
            edit = 2
            ignore = 3

      class ConfigManager(vmodl.DynamicData):
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

      class CpuIdInfo(vmodl.DynamicData):
         level = 0
         vendor = ""
         eax = ""
         ebx = ""
         ecx = ""
         edx = ""

      class CpuInfo(vmodl.DynamicData):
         numCpuPackages = 0
         numCpuCores = 0
         numCpuThreads = 0
         hz = 0

      class CpuPackage(vmodl.DynamicData):
         index = 0
         vendor = ""
         hz = 0
         busHz = 0
         description = ""
         threadId = [ 0 ]
         cpuFeature = [ vim.host.CpuIdInfo() ]

         class Vendor(Enum):
            unknown = 0
            intel = 1
            amd = 2
            hygon = 3
            arm = 4

      class CpuPowerManagementInfo(vmodl.DynamicData):
         currentPolicy = ""
         hardwareSupport = ""

         class PolicyType(Enum):
            off = 0
            staticPolicy = 1
            dynamicPolicy = 2

      class CpuSchedulerSystem(vim.ExtensibleManagedObject):
         hyperthreadInfo = vim.host.CpuSchedulerSystem.HyperThreadScheduleInfo()

         def enableHyperThreading():
            return None

         def disableHyperThreading():
            return None

         class HyperThreadScheduleInfo(vmodl.DynamicData):
            available = False
            active = False
            config = False

      class DatastoreBrowser(vmodl.ManagedObject):
         datastore = [ vim.Datastore() ]
         supportedType = [ vim.host.DatastoreBrowser.Query() ]

         def search(datastorePath="", searchSpec=vim.host.DatastoreBrowser.SearchSpec() or None):
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return vim.Task()

         def searchSubFolders(datastorePath="", searchSpec=vim.host.DatastoreBrowser.SearchSpec() or None):
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return vim.Task()

         def deleteFile(datastorePath=""):
            # throws vim.fault.InvalidDatastore, vim.fault.FileFault
            return None

         class FileInfo(vmodl.DynamicData):
            path = ""
            friendlyName = ""
            fileSize = 0
            modification = vmodl.DateTime()
            owner = ""

            class Details(vmodl.DynamicData):
               fileType = False
               fileSize = False
               modification = False
               fileOwner = False

         class Query(vmodl.DynamicData):
            pass

         class VmConfigQuery(vim.host.DatastoreBrowser.Query):
            filter = vim.host.DatastoreBrowser.VmConfigQuery.Filter()
            details = vim.host.DatastoreBrowser.VmConfigQuery.Details()

            class Filter(vmodl.DynamicData):
               matchConfigVersion = [ 0 ]
               encrypted = False

            class Details(vmodl.DynamicData):
               configVersion = False
               encryption = False

         class TemplateVmConfigQuery(vim.host.DatastoreBrowser.VmConfigQuery):
            pass

         class VmDiskQuery(vim.host.DatastoreBrowser.Query):
            filter = vim.host.DatastoreBrowser.VmDiskQuery.Filter()
            details = vim.host.DatastoreBrowser.VmDiskQuery.Details()

            class Filter(vmodl.DynamicData):
               diskType = [ vmodl.TypeName() ]
               matchHardwareVersion = [ 0 ]
               controllerType = [ vmodl.TypeName() ]
               thin = False
               encrypted = False

            class Details(vmodl.DynamicData):
               diskType = False
               capacityKb = False
               hardwareVersion = False
               controllerType = False
               diskExtents = False
               thin = False
               encryption = False

         class FolderQuery(vim.host.DatastoreBrowser.Query):
            pass

         class VmSnapshotQuery(vim.host.DatastoreBrowser.Query):
            pass

         class IsoImageQuery(vim.host.DatastoreBrowser.Query):
            pass

         class FloppyImageQuery(vim.host.DatastoreBrowser.Query):
            pass

         class VmNvramQuery(vim.host.DatastoreBrowser.Query):
            pass

         class VmLogQuery(vim.host.DatastoreBrowser.Query):
            pass

         class VmConfigInfo(vim.host.DatastoreBrowser.FileInfo):
            configVersion = 0
            encryption = vim.host.DatastoreBrowser.VmConfigInfo.VmConfigEncryptionInfo()

            class VmConfigEncryptionInfo(vmodl.DynamicData):
               keyId = vim.encryption.CryptoKeyId()

         class TemplateVmConfigInfo(vim.host.DatastoreBrowser.VmConfigInfo):
            pass

         class VmDiskInfo(vim.host.DatastoreBrowser.FileInfo):
            diskType = vmodl.TypeName()
            capacityKb = 0
            hardwareVersion = 0
            controllerType = vmodl.TypeName()
            diskExtents = [ "" ]
            thin = False
            encryption = vim.host.DatastoreBrowser.VmDiskInfo.VmDiskEncryptionInfo()

            class VmDiskEncryptionInfo(vmodl.DynamicData):
               keyId = vim.encryption.CryptoKeyId()

         class FolderInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class VmSnapshotInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class IsoImageInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class FloppyImageInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class VmNvramInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class VmLogInfo(vim.host.DatastoreBrowser.FileInfo):
            pass

         class SearchSpec(vmodl.DynamicData):
            query = [ vim.host.DatastoreBrowser.Query() ]
            details = vim.host.DatastoreBrowser.FileInfo.Details()
            searchCaseInsensitive = False
            matchPattern = [ "" ]
            sortFoldersFirst = False

         class SearchResults(vmodl.DynamicData):
            datastore = vim.Datastore()
            folderPath = ""
            file = [ vim.host.DatastoreBrowser.FileInfo() ]

      class DateTimeConfig(vmodl.DynamicData):
         timeZone = ""
         ntpConfig = vim.host.NtpConfig()

      class DateTimeSystem(vmodl.ManagedObject):
         dateTimeInfo = vim.host.DateTimeInfo()

         def updateConfig(config=vim.host.DateTimeConfig()):
            # throws vim.fault.HostConfigFault
            return None

         def queryAvailableTimeZones():
            return [ vim.host.DateTimeSystem.TimeZone() ]

         def queryDateTime():
            return vmodl.DateTime()

         def updateDateTime(dateTime=vmodl.DateTime()):
            # throws vim.fault.HostConfigFault
            return None

         def refresh():
            return None

         class TimeZone(vmodl.DynamicData):
            key = ""
            name = ""
            description = ""
            gmtOffset = 0

      class DeploymentInfo(vmodl.DynamicData):
         bootedFromStatelessCache = False

      class Device(vmodl.DynamicData):
         deviceName = ""
         deviceType = ""

      class DhcpService(vmodl.DynamicData):
         key = ""
         spec = vim.host.DhcpService.Specification()

         class Specification(vmodl.DynamicData):
            virtualSwitch = ""
            defaultLeaseDuration = 0
            leaseBeginIp = ""
            leaseEndIp = ""
            maxLeaseDuration = 0
            unlimitedLease = False
            ipSubnetAddr = ""
            ipSubnetMask = ""

         class Config(vmodl.DynamicData):
            changeOperation = ""
            key = ""
            spec = vim.host.DhcpService.Specification()

      class DigestInfo(vmodl.DynamicData):
         digestMethod = ""
         digestValue = [ 0x00 ]
         objectName = ""

         class DigestMethodType(Enum):
            SHA1 = 0
            MD5 = 1
            SHA256 = 2
            SHA384 = 3
            SHA512 = 4
            SM3_256 = 5

      class DirectoryStore(vim.host.AuthenticationStore):
         pass

      class DirectoryStoreInfo(vim.host.AuthenticationStoreInfo):
         pass

      class DiskConfigurationResult(vmodl.DynamicData):
         devicePath = ""
         success = False
         fault = vmodl.MethodFault()

      class DiskDimensions(vmodl.DynamicData):

         class Chs(vmodl.DynamicData):
            cylinder = 0
            head = 0
            sector = 0

         class Lba(vmodl.DynamicData):
            blockSize = 0
            block = 0

      class DiskPartitionInfo(vmodl.DynamicData):
         deviceName = ""
         spec = vim.host.DiskPartitionInfo.Specification()
         layout = vim.host.DiskPartitionInfo.Layout()

         class PartitionFormat(Enum):
            gpt = 0
            mbr = 1
            unknown = 2

         class Type(Enum):
            none = 0
            vmfs = 1
            linuxNative = 2
            linuxSwap = 3
            extended = 4
            ntfs = 5
            vmkDiagnostic = 6
            vffs = 7

         class Partition(vmodl.DynamicData):
            partition = 0
            startSector = 0
            endSector = 0
            type = ""
            guid = ""
            logical = False
            attributes = 0x00
            partitionAlignment = 0

         class BlockRange(vmodl.DynamicData):
            partition = 0
            type = ""
            start = vim.host.DiskDimensions.Lba()
            end = vim.host.DiskDimensions.Lba()

         class Specification(vmodl.DynamicData):
            partitionFormat = ""
            chs = vim.host.DiskDimensions.Chs()
            totalSectors = 0
            partition = [ vim.host.DiskPartitionInfo.Partition() ]

         class Layout(vmodl.DynamicData):
            total = vim.host.DiskDimensions.Lba()
            partition = [ vim.host.DiskPartitionInfo.BlockRange() ]

      class DnsConfig(vmodl.DynamicData):
         dhcp = False
         virtualNicDevice = ""
         ipv6VirtualNicDevice = ""
         hostName = ""
         domainName = ""
         address = [ "" ]
         searchDomain = [ "" ]

      class DnsConfigSpec(vim.host.DnsConfig):
         virtualNicConnection = vim.host.VirtualNicConnection()
         virtualNicConnectionV6 = vim.host.VirtualNicConnection()

      class EnterMaintenanceResult(vmodl.DynamicData):
         vmFaults = [ vim.FaultsByVM() ]
         hostFaults = [ vim.FaultsByHost() ]

      class EsxAgentHostManager(vmodl.ManagedObject):
         configInfo = vim.host.EsxAgentHostManager.ConfigInfo()

         def updateConfig(configInfo=vim.host.EsxAgentHostManager.ConfigInfo()):
            # throws vim.fault.HostConfigFault
            return None

         class ConfigInfo(vmodl.DynamicData):
            agentVmDatastore = vim.Datastore()
            agentVmNetwork = vim.Network()

      class FaultToleranceManager(object):

         class ComponentHealthInfo(vmodl.DynamicData):
            isStorageHealthy = False
            isNetworkHealthy = False

      class FcoeConfig(vmodl.DynamicData):
         priorityClass = 0
         sourceMac = ""
         vlanRange = [ vim.host.FcoeConfig.VlanRange() ]
         capabilities = vim.host.FcoeConfig.FcoeCapabilities()
         fcoeActive = False

         class VlanRange(vmodl.DynamicData):
            vlanLow = 0
            vlanHigh = 0

         class FcoeCapabilities(vmodl.DynamicData):
            priorityClass = False
            sourceMacAddress = False
            vlanRange = False

         class FcoeSpecification(vmodl.DynamicData):
            underlyingPnic = ""
            priorityClass = 0
            sourceMac = ""
            vlanRange = [ vim.host.FcoeConfig.VlanRange() ]

      class FeatureCapability(vmodl.DynamicData):
         key = ""
         featureName = ""
         value = ""

      class FeatureMask(vmodl.DynamicData):
         key = ""
         featureName = ""
         value = ""

      class FeatureVersionInfo(vmodl.DynamicData):
         key = ""
         value = ""

         class FeatureVersionKey(Enum):
            faultTolerance = 0

      class FileAccess(vmodl.DynamicData):
         who = ""
         what = ""

         class Modes(vmodl.DynamicData):
            browse = ""
            read = ""
            modify = ""
            use = ""
            admin = ""
            full = ""

      class FileSystemMountInfo(vmodl.DynamicData):
         mountInfo = vim.host.MountInfo()
         volume = vim.host.FileSystemVolume()
         vStorageSupport = ""

         class VStorageSupportStatus(Enum):
            vStorageSupported = 0
            vStorageUnsupported = 1
            vStorageUnknown = 2

      class FileSystemVolume(vmodl.DynamicData):
         type = ""
         name = ""
         capacity = 0

         class FileSystemType(Enum):
            VMFS = 0
            NFS = 1
            NFS41 = 2
            CIFS = 3
            vsan = 4
            VFFS = 5
            VVOL = 6
            PMEM = 7
            OTHER = 8

      class FileSystemVolumeInfo(vmodl.DynamicData):
         volumeTypeList = [ "" ]
         mountInfo = [ vim.host.FileSystemMountInfo() ]

      class FirewallInfo(vmodl.DynamicData):
         defaultPolicy = vim.host.FirewallInfo.DefaultPolicy()
         ruleset = [ vim.host.Ruleset() ]

         class DefaultPolicy(vmodl.DynamicData):
            incomingBlocked = False
            outgoingBlocked = False

      class FirmwareSystem(vmodl.ManagedObject):

         def resetToFactoryDefaults():
            # throws vim.fault.InvalidState
            return None

         def backupConfiguration():
            return ""

         def queryConfigUploadURL():
            return ""

         def restoreConfiguration(force=False):
            # throws vim.fault.InvalidState, vim.fault.FileFault, vim.fault.MismatchedBundle, vim.fault.InvalidBundle
            return None

      class FlagInfo(vmodl.DynamicData):
         backgroundSnapshotsEnabled = False

      class ForceMountedInfo(vmodl.DynamicData):
         persist = False
         mounted = False

      class GatewaySpec(vmodl.DynamicData):
         gatewayType = ""
         gatewayId = ""
         trustVerificationToken = ""
         hostAuthParams = [ vim.KeyValue() ]

      class GraphicsConfig(vmodl.DynamicData):
         hostDefaultGraphicsType = ""
         sharedPassthruAssignmentPolicy = ""
         deviceType = [ vim.host.GraphicsConfig.DeviceType() ]

         class GraphicsType(Enum):
            shared = 0
            sharedDirect = 1

         class SharedPassthruAssignmentPolicy(Enum):
            performance = 0
            consolidation = 1

         class DeviceType(vmodl.DynamicData):
            deviceId = ""
            graphicsType = ""

      class GraphicsInfo(vmodl.DynamicData):
         deviceName = ""
         vendorName = ""
         pciId = ""
         graphicsType = ""
         memorySizeInKB = 0
         vm = [ vim.VirtualMachine() ]

         class GraphicsType(Enum):
            basic = 0
            shared = 1
            direct = 2
            sharedDirect = 3

      class GraphicsManager(vim.ExtensibleManagedObject):
         graphicsInfo = [ vim.host.GraphicsInfo() ]
         graphicsConfig = vim.host.GraphicsConfig()
         sharedPassthruGpuTypes = [ "" ]
         sharedGpuCapabilities = [ vim.host.SharedGpuCapabilities() ]

         def refresh():
            return None

         def isSharedGraphicsActive():
            return False

         def updateGraphicsConfig(config=vim.host.GraphicsConfig()):
            return None

      class HardwareInfo(vmodl.DynamicData):
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

      class HardwareStatusInfo(vmodl.DynamicData):
         memoryStatusInfo = [ vim.host.HardwareStatusInfo.HardwareElementInfo() ]
         cpuStatusInfo = [ vim.host.HardwareStatusInfo.HardwareElementInfo() ]
         storageStatusInfo = [ vim.host.HardwareStatusInfo.StorageStatusInfo() ]

         class Status(Enum):
            Unknown = 0
            Green = 1
            Yellow = 2
            Red = 3

         class HardwareElementInfo(vmodl.DynamicData):
            name = ""
            status = vim.ElementDescription()

         class StorageStatusInfo(vim.host.HardwareStatusInfo.HardwareElementInfo):
            operationalInfo = [ vim.host.HardwareStatusInfo.StorageStatusInfo.OperationalInfo() ]

            class OperationalInfo(vmodl.DynamicData):
               property = ""
               value = ""

      class HealthStatusSystem(vmodl.ManagedObject):
         runtime = vim.host.HealthStatusSystem.Runtime()

         def refresh():
            return None

         def resetSystemHealthInfo():
            return None

         def clearSystemEventLog():
            return None

         def FetchSystemEventLog():
            return [ vim.host.SystemEventInfo() ]

         class Runtime(vmodl.DynamicData):
            systemHealthInfo = vim.host.SystemHealthInfo()
            hardwareStatusInfo = vim.host.HardwareStatusInfo()

      class HostAccessManager(vmodl.ManagedObject):
         lockdownMode = vim.host.HostAccessManager.LockdownMode()

         def retrieveAccessEntries():
            return [ vim.host.HostAccessManager.AccessEntry() ]

         def changeAccessMode(principal="", isGroup=False, accessMode=vim.host.HostAccessManager.AccessMode()):
            # throws vim.fault.AuthMinimumAdminPermission, vim.fault.UserNotFound
            return None

         def querySystemUsers():
            return [ "" ]

         def updateSystemUsers(users=[ "" ] or None):
            # throws vim.fault.UserNotFound
            return None

         def queryLockdownExceptions():
            return [ "" ]

         def updateLockdownExceptions(users=[ "" ] or None):
            # throws vim.fault.AuthMinimumAdminPermission, vim.fault.UserNotFound
            return None

         def changeLockdownMode(mode=vim.host.HostAccessManager.LockdownMode()):
            # throws vim.fault.AuthMinimumAdminPermission
            return None

         class AccessMode(Enum):
            accessNone = 0
            accessAdmin = 1
            accessNoAccess = 2
            accessReadOnly = 3
            accessOther = 4

         class AccessEntry(vmodl.DynamicData):
            principal = ""
            group = False
            accessMode = vim.host.HostAccessManager.AccessMode()

         class LockdownMode(Enum):
            lockdownDisabled = 0
            lockdownNormal = 1
            lockdownStrict = 2

      class HostBusAdapter(vmodl.DynamicData):
         key = ""
         device = ""
         bus = 0
         status = ""
         model = ""
         driver = ""
         pci = ""
         storageProtocol = ""

      class HostProxySwitch(vmodl.DynamicData):
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

         class Specification(vmodl.DynamicData):
            backing = vim.dvs.HostMember.Backing()

         class Config(vmodl.DynamicData):
            changeOperation = ""
            uuid = ""
            spec = vim.host.HostProxySwitch.Specification()

         class HostLagConfig(vmodl.DynamicData):
            lagKey = ""
            lagName = ""
            uplinkPort = [ vim.KeyValue() ]

      class ImageConfigManager(vmodl.ManagedObject):

         def queryHostAcceptanceLevel():
            # throws vim.fault.HostConfigFault
            return ""

         def queryHostImageProfile():
            return vim.host.ImageConfigManager.ImageProfileSummary()

         def updateAcceptanceLevel(newAcceptanceLevel=""):
            # throws vim.fault.HostConfigFault
            return None

         def fetchSoftwarePackages():
            return [ vim.host.SoftwarePackage() ]

         def installDate():
            return vmodl.DateTime()

         class AcceptanceLevel(Enum):
            vmware_certified = 0
            vmware_accepted = 1
            partner = 2
            community = 3

         class ImageProfileSummary(vmodl.DynamicData):
            name = ""
            vendor = ""

      class IpConfig(vmodl.DynamicData):
         dhcp = False
         ipAddress = ""
         subnetMask = ""
         ipV6Config = vim.host.IpConfig.IpV6AddressConfiguration()

         class IpV6AddressConfigType(Enum):
            other = 0
            manual = 1
            dhcp = 2
            linklayer = 3
            random = 4

         class IpV6AddressStatus(Enum):
            preferred = 0
            deprecated = 1
            invalid = 2
            inaccessible = 3
            unknown = 4
            tentative = 5
            duplicate = 6

         class IpV6Address(vmodl.DynamicData):
            ipAddress = ""
            prefixLength = 0
            origin = ""
            dadState = ""
            lifetime = vmodl.DateTime()
            operation = ""

         class IpV6AddressConfiguration(vmodl.DynamicData):
            ipV6Address = [ vim.host.IpConfig.IpV6Address() ]
            autoConfigurationEnabled = False
            dhcpV6Enabled = False

      class IpRouteConfig(vmodl.DynamicData):
         defaultGateway = ""
         gatewayDevice = ""
         ipV6DefaultGateway = ""
         ipV6GatewayDevice = ""

      class IpRouteConfigSpec(vim.host.IpRouteConfig):
         gatewayDeviceConnection = vim.host.VirtualNicConnection()
         ipV6GatewayDeviceConnection = vim.host.VirtualNicConnection()

      class IpRouteEntry(vmodl.DynamicData):
         network = ""
         prefixLength = 0
         gateway = ""
         deviceName = ""

      class IpRouteOp(vmodl.DynamicData):
         changeOperation = ""
         route = vim.host.IpRouteEntry()

      class IpRouteTableConfig(vmodl.DynamicData):
         ipRoute = [ vim.host.IpRouteOp() ]
         ipv6Route = [ vim.host.IpRouteOp() ]

      class IpRouteTableInfo(vmodl.DynamicData):
         ipRoute = [ vim.host.IpRouteEntry() ]
         ipv6Route = [ vim.host.IpRouteEntry() ]

      class IpmiInfo(vmodl.DynamicData):
         bmcIpAddress = ""
         bmcMacAddress = ""
         login = ""
         password = ""

      class IscsiManager(vmodl.ManagedObject):

         def queryVnicStatus(vnicDevice=""):
            # throws vim.fault.IscsiFault
            return vim.host.IscsiManager.IscsiStatus()

         def queryPnicStatus(pnicDevice=""):
            # throws vim.fault.IscsiFault
            return vim.host.IscsiManager.IscsiStatus()

         def queryBoundVnics(iScsiHbaName=""):
            # throws vim.fault.IscsiFault, vim.fault.NotFound
            return [ vim.host.IscsiManager.IscsiPortInfo() ]

         def queryCandidateNics(iScsiHbaName=""):
            # throws vim.fault.IscsiFault, vim.fault.NotFound
            return [ vim.host.IscsiManager.IscsiPortInfo() ]

         def bindVnic(iScsiHbaName="", vnicDevice=""):
            # throws vim.fault.IscsiFaultVnicAlreadyBound, vim.fault.IscsiFaultVnicHasNoUplinks, vim.fault.IscsiFaultVnicHasMultipleUplinks, vim.fault.IscsiFaultVnicHasWrongUplink, vim.fault.IscsiFaultVnicNotFound, vim.fault.IscsiFaultInvalidVnic, vim.fault.PlatformConfigFault, vim.fault.IscsiFault, vim.fault.NotFound
            return None

         def unbindVnic(iScsiHbaName="", vnicDevice="", force=False):
            # throws vim.fault.IscsiFaultVnicNotBound, vim.fault.IscsiFaultVnicHasActivePaths, vim.fault.IscsiFaultVnicIsLastPath, vim.fault.PlatformConfigFault, vim.fault.IscsiFault, vim.fault.NotFound
            return None

         def queryMigrationDependencies(pnicDevice=[ "" ]):
            return vim.host.IscsiManager.IscsiMigrationDependency()

         class IscsiStatus(vmodl.DynamicData):
            reason = [ vmodl.MethodFault() ]

         class IscsiPortInfo(vmodl.DynamicData):
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

            class PathStatus(Enum):
               notUsed = 0
               active = 1
               standBy = 2
               lastActive = 3

         class IscsiDependencyEntity(vmodl.DynamicData):
            pnicDevice = ""
            vnicDevice = ""
            vmhbaName = ""

         class IscsiMigrationDependency(vmodl.DynamicData):
            migrationAllowed = False
            disallowReason = vim.host.IscsiManager.IscsiStatus()
            dependency = [ vim.host.IscsiManager.IscsiDependencyEntity() ]

      class KernelModuleSystem(vmodl.ManagedObject):

         def queryModules():
            return [ vim.host.KernelModuleSystem.ModuleInfo() ]

         def updateModuleOptionString(name="", options=""):
            # throws vim.fault.NotFound
            return None

         def queryConfiguredModuleOptionString(name=""):
            # throws vim.fault.NotFound
            return ""

         class ModuleInfo(vmodl.DynamicData):
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

            class SectionInfo(vmodl.DynamicData):
               address = 0
               length = 0

      class LicenseSpec(vmodl.DynamicData):
         source = vim.LicenseManager.LicenseSource()
         editionKey = ""
         disabledFeatureKey = [ "" ]
         enabledFeatureKey = [ "" ]

      class LinkDiscoveryProtocolConfig(vmodl.DynamicData):
         protocol = ""
         operation = ""

         class ProtocolType(Enum):
            cdp = 0
            lldp = 1

         class OperationType(Enum):
            none = 0
            listen = 1
            advertise = 2
            both = 3

      class LocalAccountManager(vmodl.ManagedObject):

         def createUser(user=vim.host.LocalAccountManager.AccountSpecification()):
            # throws vim.fault.AlreadyExists
            return None

         def updateUser(user=vim.host.LocalAccountManager.AccountSpecification()):
            # throws vim.fault.UserNotFound, vim.fault.AlreadyExists
            return None

         def createGroup(group=vim.host.LocalAccountManager.AccountSpecification()):
            # throws vim.fault.AlreadyExists
            return None

         def removeUser(userName=""):
            # throws vim.fault.UserNotFound
            return None

         def removeGroup(groupName=""):
            # throws vim.fault.UserNotFound
            return None

         def assignUserToGroup(user="", group=""):
            # throws vim.fault.UserNotFound, vim.fault.AlreadyExists
            return None

         def unassignUserFromGroup(user="", group=""):
            # throws vim.fault.UserNotFound
            return None

         def changePassword(user="", oldPassword="", newPassword=""):
            # throws vim.fault.InvalidLogin
            return None

         class AccountSpecification(vmodl.DynamicData):
            id = ""
            password = ""
            description = ""

         class PosixAccountSpecification(vim.host.LocalAccountManager.AccountSpecification):
            posixId = 0
            shellAccess = False

      class LocalAuthentication(vim.host.AuthenticationStore):
         pass

      class LocalAuthenticationInfo(vim.host.AuthenticationStoreInfo):
         pass

      class LocalFileSystemVolume(vim.host.FileSystemVolume):
         device = ""

         class Specification(vmodl.DynamicData):
            device = ""
            localPath = ""

      class LowLevelProvisioningManager(object):

         class VmRecoveryInfo(vmodl.DynamicData):
            version = ""
            biosUUID = ""
            instanceUUID = ""
            ftInfo = vim.vm.FaultToleranceConfigInfo()

         class VmMigrationStatus(vmodl.DynamicData):
            migrationId = 0
            type = ""
            source = False
            consideredSuccessful = False

         class ReloadTarget(Enum):
            currentConfig = 0
            snapshotConfig = 1

         class DiskLayoutSpec(vmodl.DynamicData):
            controllerType = vmodl.TypeName()
            busNumber = 0
            unitNumber = 0
            srcFilename = ""
            dstFilename = ""

         class SnapshotLayoutSpec(vmodl.DynamicData):
            id = 0
            srcFilename = ""
            dstFilename = ""
            disk = [ vim.host.LowLevelProvisioningManager.DiskLayoutSpec() ]

         class FileType(Enum):
            File = 0
            VirtualDisk = 1
            Directory = 2

         class FileReserveSpec(vmodl.DynamicData):
            baseName = ""
            parentDir = ""
            fileType = ""
            storageProfile = ""

         class FileReserveResult(vmodl.DynamicData):
            baseName = ""
            parentDir = ""
            reservedName = ""

         class FileDeleteSpec(vmodl.DynamicData):
            fileName = ""
            fileType = ""

         class FileDeleteResult(vmodl.DynamicData):
            fileName = ""
            fault = vmodl.MethodFault()

      class MaintenanceSpec(vmodl.DynamicData):
         vsanMode = vim.vsan.host.DecommissionMode()
         purpose = ""

         class Purpose(Enum):
            hostUpgrade = 0

      class MemoryManagerSystem(vim.ExtensibleManagedObject):
         consoleReservationInfo = vim.host.MemoryManagerSystem.ServiceConsoleReservationInfo()
         virtualMachineReservationInfo = vim.host.MemoryManagerSystem.VirtualMachineReservationInfo()

         def reconfigureServiceConsoleReservation(cfgBytes=0):
            return None

         def reconfigureVirtualMachineReservation(spec=vim.host.MemoryManagerSystem.VirtualMachineReservationSpec()):
            return None

         class ServiceConsoleReservationInfo(vmodl.DynamicData):
            serviceConsoleReservedCfg = 0
            serviceConsoleReserved = 0
            unreserved = 0

         class VirtualMachineReservationInfo(vmodl.DynamicData):
            virtualMachineMin = 0
            virtualMachineMax = 0
            virtualMachineReserved = 0
            allocationPolicy = ""

            class AllocationPolicy(Enum):
               swapNone = 0
               swapSome = 1
               swapMost = 2

         class VirtualMachineReservationSpec(vmodl.DynamicData):
            virtualMachineReserved = 0
            allocationPolicy = ""

      class MemorySpec(vmodl.DynamicData):
         serviceConsoleReservation = 0

      class MessageBusProxy(vmodl.ManagedObject):
         pass

      class MountInfo(vmodl.DynamicData):
         path = ""
         accessMode = ""
         mounted = False
         accessible = False
         inaccessibleReason = ""

         class AccessMode(Enum):
            readWrite = 0
            readOnly = 1

         class InaccessibleReason(Enum):
            AllPathsDown_Start = 0
            AllPathsDown_Timeout = 1
            PermanentDeviceLoss = 2

      class MultipathInfo(vmodl.DynamicData):
         lun = [ vim.host.MultipathInfo.LogicalUnit() ]

         class PathState(Enum):
            standby = 0
            active = 1
            disabled = 2
            dead = 3
            unknown = 4

         class LogicalUnitPolicy(vmodl.DynamicData):
            policy = ""

         class HppLogicalUnitPolicy(vim.host.MultipathInfo.LogicalUnitPolicy):
            bytes = 0
            iops = 0
            path = ""
            latencyEvalTime = 0
            samplingIosPerPath = 0

         class LogicalUnitStorageArrayTypePolicy(vmodl.DynamicData):
            policy = ""

         class FixedLogicalUnitPolicy(vim.host.MultipathInfo.LogicalUnitPolicy):
            prefer = ""

         class LogicalUnit(vmodl.DynamicData):
            key = ""
            id = ""
            lun = vim.host.ScsiLun()
            path = [ vim.host.MultipathInfo.Path() ]
            policy = vim.host.MultipathInfo.LogicalUnitPolicy()
            storageArrayTypePolicy = vim.host.MultipathInfo.LogicalUnitStorageArrayTypePolicy()

         class Path(vmodl.DynamicData):
            key = ""
            name = ""
            pathState = ""
            state = ""
            isWorkingPath = False
            adapter = vim.host.HostBusAdapter()
            lun = vim.host.MultipathInfo.LogicalUnit()
            transport = vim.host.TargetTransport()

      class MultipathStateInfo(vmodl.DynamicData):
         path = [ vim.host.MultipathStateInfo.Path() ]

         class Path(vmodl.DynamicData):
            name = ""
            pathState = ""

      class NasVolume(vim.host.FileSystemVolume):
         remoteHost = ""
         remotePath = ""
         userName = ""
         remoteHostNames = [ "" ]
         securityType = ""
         protocolEndpoint = False

         class UserInfo(vmodl.DynamicData):
            user = ""

         class SecurityType(Enum):
            AUTH_SYS = 0
            SEC_KRB5 = 1
            SEC_KRB5I = 2

         class Specification(vmodl.DynamicData):
            remoteHost = ""
            remotePath = ""
            localPath = ""
            accessMode = ""
            type = ""
            userName = ""
            password = ""
            remoteHostNames = [ "" ]
            securityType = ""

         class Config(vmodl.DynamicData):
            changeOperation = ""
            spec = vim.host.NasVolume.Specification()

      class NatService(vmodl.DynamicData):
         key = ""
         spec = vim.host.NatService.Specification()

         class PortForwardSpecification(vmodl.DynamicData):
            type = ""
            name = ""
            hostPort = 0
            guestPort = 0
            guestIpAddress = ""

         class NameServiceSpec(vmodl.DynamicData):
            dnsAutoDetect = False
            dnsPolicy = ""
            dnsRetries = 0
            dnsTimeout = 0
            dnsNameServer = [ "" ]
            nbdsTimeout = 0
            nbnsRetries = 0
            nbnsTimeout = 0

         class Specification(vmodl.DynamicData):
            virtualSwitch = ""
            activeFtp = False
            allowAnyOui = False
            configPort = False
            ipGatewayAddress = ""
            udpTimeout = 0
            portForward = [ vim.host.NatService.PortForwardSpecification() ]
            nameService = vim.host.NatService.NameServiceSpec()

         class Config(vmodl.DynamicData):
            changeOperation = ""
            key = ""
            spec = vim.host.NatService.Specification()

      class NetCapabilities(vmodl.DynamicData):
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

      class NetOffloadCapabilities(vmodl.DynamicData):
         csumOffload = False
         tcpSegmentation = False
         zeroCopyXmit = False

      class NetStackInstance(vmodl.DynamicData):
         key = ""
         name = ""
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         requestedMaxNumberOfConnections = 0
         congestionControlAlgorithm = ""
         ipV6Enabled = False
         routeTableConfig = vim.host.IpRouteTableConfig()

         class SystemStackKey(Enum):
            defaultTcpipStack = 0
            vmotion = 1
            vSphereProvisioning = 2

         class CongestionControlAlgorithmType(Enum):
            newreno = 0
            cubic = 1

      class NetworkInfo(vmodl.DynamicData):
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

      class NetworkPolicy(vmodl.DynamicData):
         security = vim.host.NetworkPolicy.SecurityPolicy()
         nicTeaming = vim.host.NetworkPolicy.NicTeamingPolicy()
         offloadPolicy = vim.host.NetOffloadCapabilities()
         shapingPolicy = vim.host.NetworkPolicy.TrafficShapingPolicy()

         class SecurityPolicy(vmodl.DynamicData):
            allowPromiscuous = False
            macChanges = False
            forgedTransmits = False

         class TrafficShapingPolicy(vmodl.DynamicData):
            enabled = False
            averageBandwidth = 0
            peakBandwidth = 0
            burstSize = 0

         class NicFailureCriteria(vmodl.DynamicData):
            checkSpeed = ""
            speed = 0
            checkDuplex = False
            fullDuplex = False
            checkErrorPercent = False
            percentage = 0
            checkBeacon = False

         class NicOrderPolicy(vmodl.DynamicData):
            activeNic = [ "" ]
            standbyNic = [ "" ]

         class NicTeamingPolicy(vmodl.DynamicData):
            policy = ""
            reversePolicy = False
            notifySwitches = False
            rollingOrder = False
            failureCriteria = vim.host.NetworkPolicy.NicFailureCriteria()
            nicOrder = vim.host.NetworkPolicy.NicOrderPolicy()

      class NtpConfig(vmodl.DynamicData):
         server = [ "" ]
         configFile = [ "" ]

      class NumaInfo(vmodl.DynamicData):
         type = ""
         numNodes = 0
         numaNode = [ vim.host.NumaNode() ]

      class NumaNode(vmodl.DynamicData):
         typeId = 0x00
         cpuID = [ 0 ]
         memoryRangeBegin = 0
         memoryRangeLength = 0
         pciId = [ "" ]

      class NumericSensorInfo(vmodl.DynamicData):
         name = ""
         healthState = vim.ElementDescription()
         currentReading = 0
         unitModifier = 0
         baseUnits = ""
         rateUnits = ""
         sensorType = ""
         id = ""
         timeStamp = ""

         class HealthState(Enum):
            unknown = 0
            green = 1
            yellow = 2
            red = 3

         class SensorType(Enum):
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

      class NvdimmSystem(vmodl.ManagedObject):
         nvdimmSystemInfo = vim.host.NvdimmSystem.NvdimmSystemInfo()

         def createNamespace(createSpec=vim.host.NvdimmSystem.NamespaceCreateSpec()):
            # throws vim.fault.InvalidHostState, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Task()

         def createPMemNamespace(createSpec=vim.host.NvdimmSystem.PMemNamespaceCreateSpec()):
            # throws vim.fault.InvalidHostState, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Task()

         def deleteNamespace(deleteSpec=vim.host.NvdimmSystem.NamespaceDeleteSpec()):
            # throws vim.fault.NotFound, vim.fault.InvalidHostState, vim.fault.HostConfigFault
            return vim.Task()

         def deleteBlockNamespaces():
            # throws vim.fault.NotFound, vim.fault.InvalidHostState, vim.fault.HostConfigFault
            return vim.Task()

         class RangeType(Enum):
            volatileRange = 0
            persistentRange = 1
            controlRange = 2
            blockRange = 3
            volatileVirtualDiskRange = 4
            volatileVirtualCDRange = 5
            persistentVirtualDiskRange = 6
            persistentVirtualCDRange = 7

         class NamespaceType(Enum):
            blockNamespace = 0
            persistentNamespace = 1

         class HealthInfo(vmodl.DynamicData):
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

            class StateFlag(Enum):
               normal = 0
               error = 1

         class RegionInfo(vmodl.DynamicData):
            regionId = 0
            setId = 0
            rangeType = ""
            startAddr = 0
            size = 0
            offset = 0

         class Summary(vmodl.DynamicData):
            numDimms = 0
            healthStatus = ""
            totalCapacity = 0
            persistentCapacity = 0
            blockCapacity = 0
            availableCapacity = 0
            numInterleavesets = 0
            numNamespaces = 0

         class DimmInfo(vmodl.DynamicData):
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

         class InterleaveSetInfo(vmodl.DynamicData):
            setId = 0
            rangeType = ""
            baseAddress = 0
            size = 0
            availableSize = 0
            deviceList = [ 0 ]
            state = ""

            class InterleaveSetState(Enum):
               invalid = 0
               active = 1

         class Guid(vmodl.DynamicData):
            uuid = ""

         class NamespaceInfo(vmodl.DynamicData):
            uuid = ""
            friendlyName = ""
            blockSize = 0
            blockCount = 0
            type = ""
            namespaceHealthStatus = ""
            locationID = 0
            state = ""

            class NamespaceHealthStatus(Enum):
               normal = 0
               missing = 1
               labelMissing = 2
               interleaveBroken = 3
               labelInconsistent = 4
               bttCorrupt = 5
               badBlockSize = 6

            class NamespaceState(Enum):
               invalid = 0
               notInUse = 1
               inUse = 2

         class NamespaceDetails(vmodl.DynamicData):
            uuid = ""
            friendlyName = ""
            size = 0
            type = ""
            namespaceHealthStatus = ""
            interleavesetID = 0
            state = ""

            class NamespaceHealthStatus(Enum):
               normal = 0
               missing = 1
               labelMissing = 2
               interleaveBroken = 3
               labelInconsistent = 4

            class NamespaceState(Enum):
               invalid = 0
               notInUse = 1
               inUse = 2

         class NamespaceCreateSpec(vmodl.DynamicData):
            friendlyName = ""
            blockSize = 0
            blockCount = 0
            type = ""
            locationID = 0

         class PMemNamespaceCreateSpec(vmodl.DynamicData):
            friendlyName = ""
            size = 0
            interleavesetID = 0

         class NamespaceDeleteSpec(vmodl.DynamicData):
            uuid = ""

         class NvdimmSystemInfo(vmodl.DynamicData):
            summary = vim.host.NvdimmSystem.Summary()
            dimms = [ 0 ]
            dimmInfo = [ vim.host.NvdimmSystem.DimmInfo() ]
            interleaveSet = [ 0 ]
            iSetInfo = [ vim.host.NvdimmSystem.InterleaveSetInfo() ]
            namespace = [ vim.host.NvdimmSystem.Guid() ]
            nsInfo = [ vim.host.NvdimmSystem.NamespaceInfo() ]
            nsDetails = [ vim.host.NvdimmSystem.NamespaceDetails() ]

      class NvmeController(vmodl.DynamicData):
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

      class NvmeDisconnectSpec(vmodl.DynamicData):
         hbaName = ""
         subnqn = ""
         controllerNumber = 0

      class NvmeDiscoveryLog(vmodl.DynamicData):
         entry = [ vim.host.NvmeDiscoveryLog.Entry() ]
         complete = False

         class SubsystemType(Enum):
            discovery = 0
            nvm = 1

         class TransportRequirements(Enum):
            secureChannelRequired = 0
            secureChannelNotRequired = 1
            requirementsNotSpecified = 2

         class Entry(vmodl.DynamicData):
            subnqn = ""
            subsystemType = ""
            subsystemPortId = 0
            controllerId = 0
            adminQueueMaxSize = 0
            transportParameters = vim.host.NvmeTransportParameters()
            transportRequirements = ""
            connected = False

      class NvmeNamespace(vmodl.DynamicData):
         key = ""
         name = ""
         id = 0
         blockSize = 0
         capacityInBlocks = 0

      class NvmeSpec(vmodl.DynamicData):
         hbaName = ""
         transportParameters = vim.host.NvmeTransportParameters()

      class NvmeTopology(vmodl.DynamicData):
         adapter = [ vim.host.NvmeTopology.Interface() ]

         class Interface(vmodl.DynamicData):
            key = ""
            adapter = vim.host.HostBusAdapter()
            connectedController = [ vim.host.NvmeController() ]

      class NvmeTransportParameters(vmodl.DynamicData):

         class NvmeAddressFamily(Enum):
            ipv4 = 0
            ipv6 = 1
            infiniBand = 2
            fc = 3
            loopback = 4
            unknown = 5

      class NvmeTransportType(Enum):
         pcie = 0
         fibreChannel = 1
         rdma = 2
         loopback = 3
         unsupported = 4

      class OpaqueSwitch(vmodl.DynamicData):
         key = ""
         name = ""
         pnic = [ vim.host.PhysicalNic() ]
         pnicZone = [ vim.host.OpaqueSwitch.PhysicalNicZone() ]
         status = ""
         vtep = [ vim.host.VirtualNic() ]
         extraConfig = [ vim.option.OptionValue() ]
         featureCapability = [ vim.host.FeatureCapability() ]

         class OpaqueSwitchState(Enum):
            up = 0
            warning = 1
            down = 2
            maintenance = 3

         class PhysicalNicZone(vmodl.DynamicData):
            key = ""
            pnicDevice = [ "" ]

      class PMemVolume(vim.host.FileSystemVolume):
         uuid = ""
         version = ""

      class ParallelScsiHba(vim.host.HostBusAdapter):
         pass

      class PatchManager(vmodl.ManagedObject):

         def Check(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Scan(repository=vim.host.PatchManager.Locator(), updateID=[ "" ] or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.PatchMetadataInvalid, vim.fault.PlatformConfigFault
            return vim.Task()

         def ScanV2(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Stage(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, vibUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Install(repository=vim.host.PatchManager.Locator(), updateID="", force=False or None):
            # throws vim.fault.PatchMetadataInvalid, vim.fault.PatchBinariesNotFound, vim.fault.PatchNotApplicable, vim.fault.NoDiskSpace, vim.fault.PatchInstallFailed, vim.fault.RebootRequired, vim.fault.InvalidState, vim.fault.TaskInProgress
            return vim.Task()

         def InstallV2(metaUrls=[ "" ] or None, bundleUrls=[ "" ] or None, vibUrls=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Uninstall(bulletinIds=[ "" ] or None, spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         def Query(spec=vim.host.PatchManager.PatchManagerOperationSpec() or None):
            # throws vmodl.fault.RequestCanceled, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.PlatformConfigFault
            return vim.Task()

         class Result(vmodl.DynamicData):
            version = ""
            status = [ vim.host.PatchManager.Status() ]
            xmlResult = ""

         class Status(vmodl.DynamicData):
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

            class Reason(Enum):
               obsoleted = 0
               missingPatch = 1
               missingLib = 2
               hasDependentPatch = 3
               conflictPatch = 4
               conflictLib = 5

            class Integrity(Enum):
               validated = 0
               keyNotFound = 1
               keyRevoked = 2
               keyExpired = 3
               digestMismatch = 4
               notEnoughSignatures = 5
               validationError = 6

            class InstallState(Enum):
               hostRestarted = 0
               imageActive = 1

            class PrerequisitePatch(vmodl.DynamicData):
               id = ""
               installState = [ "" ]

         class Locator(vmodl.DynamicData):
            url = ""
            proxy = ""

         class PatchManagerOperationSpec(vmodl.DynamicData):
            proxy = ""
            port = 0
            userName = ""
            password = ""
            cmdOption = ""

      class PathSelectionPolicyOption(vmodl.DynamicData):
         policy = vim.ElementDescription()

      class PciDevice(vmodl.DynamicData):
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

      class PciPassthruConfig(vmodl.DynamicData):
         id = ""
         passthruEnabled = False
         applyNow = False

      class PciPassthruInfo(vmodl.DynamicData):
         id = ""
         dependentDevice = ""
         passthruEnabled = False
         passthruCapable = False
         passthruActive = False

      class PciPassthruSystem(vim.ExtensibleManagedObject):
         pciPassthruInfo = [ vim.host.PciPassthruInfo() ]
         sriovDevicePoolInfo = [ vim.host.SriovDevicePoolInfo() ]

         def refresh():
            return None

         def updatePassthruConfig(config=[ vim.host.PciPassthruConfig() ]):
            # throws vim.fault.HostConfigFault
            return None

      class PcieHba(vim.host.HostBusAdapter):
         pass

      class PersistentMemoryInfo(vmodl.DynamicData):
         capacityInMB = 0
         volumeUUID = ""

      class PhysicalNic(vmodl.DynamicData):
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

         class Specification(vmodl.DynamicData):
            ip = vim.host.IpConfig()
            linkSpeed = vim.host.PhysicalNic.LinkSpeedDuplex()
            enableEnhancedNetworkingStack = False
            ensInterruptEnabled = False

         class Config(vmodl.DynamicData):
            device = ""
            spec = vim.host.PhysicalNic.Specification()

         class LinkSpeedDuplex(vmodl.DynamicData):
            speedMb = 0
            duplex = False

         class NetworkHint(vmodl.DynamicData):
            device = ""
            subnet = [ vim.host.PhysicalNic.NetworkHint.IpNetwork() ]
            network = [ vim.host.PhysicalNic.NetworkHint.NamedNetwork() ]
            connectedSwitchPort = vim.host.PhysicalNic.CdpInfo()
            lldpInfo = vim.host.PhysicalNic.LldpInfo()

            class HintElement(vmodl.DynamicData):
               vlanId = 0

            class IpNetwork(vim.host.PhysicalNic.NetworkHint.HintElement):
               ipSubnet = ""

            class NamedNetwork(vim.host.PhysicalNic.NetworkHint.HintElement):
               network = ""

         class CdpDeviceCapability(vmodl.DynamicData):
            router = False
            transparentBridge = False
            sourceRouteBridge = False
            networkSwitch = False
            host = False
            igmpEnabled = False
            repeater = False

         class CdpInfo(vmodl.DynamicData):
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

         class LldpInfo(vmodl.DynamicData):
            chassisId = ""
            portId = ""
            timeToLive = 0
            parameter = [ vmodl.KeyAnyValue() ]

         class VmDirectPathGen2SupportedMode(Enum):
            upt = 0

         class ResourcePoolSchedulerDisallowedReason(Enum):
            userOptOut = 0
            hardwareUnsupported = 1

      class PlugStoreTopology(vmodl.DynamicData):
         adapter = [ vim.host.PlugStoreTopology.Adapter() ]
         path = [ vim.host.PlugStoreTopology.Path() ]
         target = [ vim.host.PlugStoreTopology.Target() ]
         device = [ vim.host.PlugStoreTopology.Device() ]
         plugin = [ vim.host.PlugStoreTopology.Plugin() ]

         class Adapter(vmodl.DynamicData):
            key = ""
            adapter = vim.host.HostBusAdapter()
            path = [ vim.host.PlugStoreTopology.Path() ]

         class Path(vmodl.DynamicData):
            key = ""
            name = ""
            channelNumber = 0
            targetNumber = 0
            lunNumber = 0
            adapter = vim.host.PlugStoreTopology.Adapter()
            target = vim.host.PlugStoreTopology.Target()
            device = vim.host.PlugStoreTopology.Device()

         class Device(vmodl.DynamicData):
            key = ""
            lun = vim.host.ScsiLun()
            path = [ vim.host.PlugStoreTopology.Path() ]

         class Plugin(vmodl.DynamicData):
            key = ""
            name = ""
            device = [ vim.host.PlugStoreTopology.Device() ]
            claimedPath = [ vim.host.PlugStoreTopology.Path() ]

         class Target(vmodl.DynamicData):
            key = ""
            transport = vim.host.TargetTransport()

      class PortGroup(vmodl.DynamicData):
         key = ""
         port = [ vim.host.PortGroup.Port() ]
         vswitch = vim.host.VirtualSwitch()
         computedPolicy = vim.host.NetworkPolicy()
         spec = vim.host.PortGroup.Specification()

         class PortConnecteeType(Enum):
            virtualMachine = 0
            systemManagement = 1
            host = 2
            unknown = 3

         class Specification(vmodl.DynamicData):
            name = ""
            vlanId = 0
            vswitchName = ""
            policy = vim.host.NetworkPolicy()

         class Config(vmodl.DynamicData):
            changeOperation = ""
            spec = vim.host.PortGroup.Specification()

         class Port(vmodl.DynamicData):
            key = ""
            mac = [ "" ]
            type = ""

      class PowerSystem(vmodl.ManagedObject):
         capability = vim.host.PowerSystem.Capability()
         info = vim.host.PowerSystem.Info()

         def configurePolicy(key=0):
            # throws vim.fault.HostConfigFault
            return None

         class PowerPolicy(vmodl.DynamicData):
            key = 0
            name = ""
            shortName = ""
            description = ""

         class Capability(vmodl.DynamicData):
            availablePolicy = [ vim.host.PowerSystem.PowerPolicy() ]

         class Info(vmodl.DynamicData):
            currentPolicy = vim.host.PowerSystem.PowerPolicy()

      class ProtocolEndpoint(vmodl.DynamicData):
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

         class PEType(Enum):
            block = 0
            nas = 1

         class ProtocolEndpointType(Enum):
            scsi = 0
            nfs = 1
            nfs4x = 2

      class RdmaDevice(vmodl.DynamicData):
         key = ""
         device = ""
         driver = ""
         description = ""
         backing = vim.host.RdmaDevice.Backing()
         connectionInfo = vim.host.RdmaDevice.ConnectionInfo()
         capability = vim.host.RdmaDevice.Capability()

         class Backing(vmodl.DynamicData):
            pass

         class PnicBacking(vim.host.RdmaDevice.Backing):
            pairedUplink = vim.host.PhysicalNic()

         class ConnectionState(Enum):
            unknown = 0
            down = 1
            init = 2
            armed = 3
            active = 4
            activeDefer = 5

         class ConnectionInfo(vmodl.DynamicData):
            state = ""
            mtu = 0
            speedInMbps = 0

         class Capability(vmodl.DynamicData):
            roceV1Capable = False
            roceV2Capable = False
            iWarpCapable = False

      class RdmaHba(vim.host.HostBusAdapter):
         associatedRdmaDevice = ""

      class ReliableMemoryInfo(vmodl.DynamicData):
         memorySize = 0

      class ResignatureRescanResult(vmodl.DynamicData):
         rescan = [ vim.host.VmfsRescanResult() ]
         result = vim.Datastore()

      class Ruleset(vmodl.DynamicData):
         key = ""
         label = ""
         required = False
         rule = [ vim.host.Ruleset.Rule() ]
         service = ""
         enabled = False
         allowedHosts = vim.host.Ruleset.IpList()

         class IpNetwork(vmodl.DynamicData):
            network = ""
            prefixLength = 0

         class IpList(vmodl.DynamicData):
            ipAddress = [ "" ]
            ipNetwork = [ vim.host.Ruleset.IpNetwork() ]
            allIp = False

         class RulesetSpec(vmodl.DynamicData):
            allowedHosts = vim.host.Ruleset.IpList()

         class Rule(vmodl.DynamicData):
            port = 0
            endPort = 0
            direction = vim.host.Ruleset.Rule.Direction()
            portType = vim.host.Ruleset.Rule.PortType()
            protocol = ""

            class Direction(Enum):
               inbound = 0
               outbound = 1

            class PortType(Enum):
               src = 0
               dst = 1

            class Protocol(Enum):
               tcp = 0
               udp = 1

      class ScsiLun(vim.host.Device):
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

         class ScsiLunType(Enum):
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

         class Capabilities(vmodl.DynamicData):
            updateDisplayNameSupported = False

         class DurableName(vmodl.DynamicData):
            namespace = ""
            namespaceId = 0x00
            data = [ 0x00 ]

         class State(Enum):
            unknownState = 0
            ok = 1
            error = 2
            off = 3
            quiesced = 4
            degraded = 5
            lostCommunication = 6
            timeout = 7

         class DescriptorQuality(Enum):
            highQuality = 0
            mediumQuality = 1
            lowQuality = 2
            unknownQuality = 3

         class Descriptor(vmodl.DynamicData):
            quality = ""
            id = ""

         class VStorageSupportStatus(Enum):
            vStorageSupported = 0
            vStorageUnsupported = 1
            vStorageUnknown = 2

      class ScsiTopology(vmodl.DynamicData):
         adapter = [ vim.host.ScsiTopology.Interface() ]

         class Interface(vmodl.DynamicData):
            key = ""
            adapter = vim.host.HostBusAdapter()
            target = [ vim.host.ScsiTopology.Target() ]

         class Target(vmodl.DynamicData):
            key = ""
            target = 0
            lun = [ vim.host.ScsiTopology.Lun() ]
            transport = vim.host.TargetTransport()

         class Lun(vmodl.DynamicData):
            key = ""
            lun = 0
            scsiLun = vim.host.ScsiLun()

      class SerialAttachedHba(vim.host.HostBusAdapter):
         nodeWorldWideName = ""

      class Service(vmodl.DynamicData):
         key = ""
         label = ""
         required = False
         uninstallable = False
         running = False
         ruleset = [ "" ]
         policy = ""
         sourcePackage = vim.host.Service.SourcePackage()

         class Policy(Enum):
            on = 0
            automatic = 1
            off = 2

         class SourcePackage(vmodl.DynamicData):
            sourcePackageName = ""
            description = ""

      class ServiceConfig(vmodl.DynamicData):
         serviceId = ""
         startupPolicy = ""

      class ServiceInfo(vmodl.DynamicData):
         service = [ vim.host.Service() ]

      class ServiceSystem(vim.ExtensibleManagedObject):
         serviceInfo = vim.host.ServiceInfo()

         def updatePolicy(id="", policy=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def start(id=""):
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def stop(id=""):
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def restart(id=""):
            # throws vim.fault.InvalidState, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def uninstall(id=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh():
            return None

      class SgxInfo(vmodl.DynamicData):
         sgxState = ""
         totalEpcMemory = 0
         flcMode = ""
         lePubKeyHash = ""

         class SgxStates(Enum):
            notPresent = 0
            disabledBIOS = 1
            disabledCFW101 = 2
            disabledCPUMismatch = 3
            disabledNoFLC = 4
            disabledNUMAUnsup = 5
            disabledMaxEPCRegs = 6
            enabled = 7

         class FlcModes(Enum):
            off = 0
            locked = 1
            unlocked = 2

      class SharedGpuCapabilities(vmodl.DynamicData):
         vgpu = ""
         diskSnapshotSupported = False
         memorySnapshotSupported = False
         suspendSupported = False
         migrateSupported = False

      class SnmpSystem(vmodl.ManagedObject):
         configuration = vim.host.SnmpSystem.SnmpConfigSpec()
         limits = vim.host.SnmpSystem.AgentLimits()

         def reconfigureSnmpAgent(spec=vim.host.SnmpSystem.SnmpConfigSpec()):
            # throws vim.fault.NotFound, vim.fault.InsufficientResourcesFault
            return None

         def sendTestNotification():
            # throws vim.fault.NotFound, vim.fault.InsufficientResourcesFault
            return None

         class SnmpConfigSpec(vmodl.DynamicData):
            enabled = False
            port = 0
            readOnlyCommunities = [ "" ]
            trapTargets = [ vim.host.SnmpSystem.SnmpConfigSpec.Destination() ]
            option = [ vim.KeyValue() ]

            class Destination(vmodl.DynamicData):
               hostName = ""
               port = 0
               community = ""

         class AgentLimits(vmodl.DynamicData):
            maxReadOnlyCommunities = 0
            maxTrapDestinations = 0
            maxCommunityLength = 0
            maxBufferSize = 0
            capability = vim.host.SnmpSystem.AgentLimits.Capability()

            class Capability(Enum):
               COMPLETE = 0
               DIAGNOSTICS = 1
               CONFIGURATION = 2

      class SoftwarePackage(vmodl.DynamicData):
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

         class VibType(Enum):
            bootbank = 0
            tools = 1
            meta = 2

         class Capability(vmodl.DynamicData):
            liveInstallAllowed = False
            liveRemoveAllowed = False
            statelessReady = False
            overlay = False

         class Constraint(Enum):
            equals = 0
            lessThan = 1
            lessThanEqual = 2
            greaterThanEqual = 3
            greaterThan = 4

         class Relation(vmodl.DynamicData):
            constraint = ""
            name = ""
            version = ""

      class SriovConfig(vim.host.PciPassthruConfig):
         sriovEnabled = False
         numVirtualFunction = 0

      class SriovDevicePoolInfo(vmodl.DynamicData):
         key = ""

      class SriovInfo(vim.host.PciPassthruInfo):
         sriovEnabled = False
         sriovCapable = False
         sriovActive = False
         numVirtualFunctionRequested = 0
         numVirtualFunction = 0
         maxVirtualFunctionSupported = 0

      class SriovNetworkDevicePoolInfo(vim.host.SriovDevicePoolInfo):
         switchKey = ""
         switchUuid = ""
         pnic = [ vim.host.PhysicalNic() ]

      class SslThumbprintInfo(vmodl.DynamicData):
         principal = ""
         ownerTag = ""
         sslThumbprints = [ "" ]

      class StorageArrayTypePolicyOption(vmodl.DynamicData):
         policy = vim.ElementDescription()

      class StorageDeviceInfo(vmodl.DynamicData):
         hostBusAdapter = [ vim.host.HostBusAdapter() ]
         scsiLun = [ vim.host.ScsiLun() ]
         scsiTopology = vim.host.ScsiTopology()
         nvmeTopology = vim.host.NvmeTopology()
         multipathInfo = vim.host.MultipathInfo()
         plugStoreTopology = vim.host.PlugStoreTopology()
         softwareInternetScsiEnabled = False

      class StorageProtocol(Enum):
         scsi = 0
         nvme = 1

      class SystemEventInfo(vmodl.DynamicData):
         recordId = 0
         when = ""
         selType = 0
         message = ""
         sensorNumber = 0

      class SystemHealthInfo(vmodl.DynamicData):
         numericSensorInfo = [ vim.host.NumericSensorInfo() ]

      class SystemIdentificationInfo(vmodl.DynamicData):
         identifierValue = ""
         identifierType = vim.ElementDescription()

         class Identifier(Enum):
            AssetTag = 0
            ServiceTag = 1
            OemSpecificString = 2
            EnclosureSerialNumberTag = 3
            SerialNumberTag = 4

      class SystemInfo(vmodl.DynamicData):
         vendor = ""
         model = ""
         uuid = ""
         otherIdentifyingInfo = [ vim.host.SystemIdentificationInfo() ]
         serialNumber = ""

      class SystemResourceInfo(vmodl.DynamicData):
         key = ""
         config = vim.ResourceConfigSpec()
         child = [ vim.host.SystemResourceInfo() ]

      class SystemSwapConfiguration(vmodl.DynamicData):
         option = [ vim.host.SystemSwapConfiguration.SystemSwapOption() ]

         class SystemSwapOption(vmodl.DynamicData):
            key = 0

         class DisabledOption(vim.host.SystemSwapConfiguration.SystemSwapOption):
            pass

         class HostCacheOption(vim.host.SystemSwapConfiguration.SystemSwapOption):
            pass

         class HostLocalSwapOption(vim.host.SystemSwapConfiguration.SystemSwapOption):
            pass

         class DatastoreOption(vim.host.SystemSwapConfiguration.SystemSwapOption):
            datastore = ""

      class TargetTransport(vmodl.DynamicData):
         pass

      class TpmAttestationInfo(vmodl.DynamicData):
         time = vmodl.DateTime()
         status = vim.host.TpmAttestationInfo.AcceptanceStatus()
         message = vmodl.LocalizableMessage()

         class AcceptanceStatus(Enum):
            notAccepted = 0
            accepted = 1

      class TpmAttestationReport(vmodl.DynamicData):
         tpmPcrValues = [ vim.host.TpmDigestInfo() ]
         tpmEvents = [ vim.host.TpmEventLogEntry() ]
         tpmLogReliable = False

      class TpmDigestInfo(vim.host.DigestInfo):
         pcrNumber = 0

      class TpmEventDetails(vmodl.DynamicData):
         dataHash = [ 0x00 ]
         dataHashMethod = ""

      class TpmEventLogEntry(vmodl.DynamicData):
         pcrIndex = 0
         eventDetails = vim.host.TpmEventDetails()

      class TpmOptionEventDetails(vim.host.TpmEventDetails):
         optionsFileName = ""
         bootOptions = [ 0x00 ]

      class TpmSoftwareComponentEventDetails(vim.host.TpmEventDetails):
         componentName = ""
         vibName = ""
         vibVersion = ""
         vibVendor = ""

      class UnresolvedVmfsResignatureSpec(vmodl.DynamicData):
         extentDevicePath = [ "" ]

      class UnresolvedVmfsResolutionResult(vmodl.DynamicData):
         spec = vim.host.UnresolvedVmfsResolutionSpec()
         vmfs = vim.host.VmfsVolume()
         fault = vmodl.MethodFault()

      class UnresolvedVmfsResolutionSpec(vmodl.DynamicData):
         extentDevicePath = [ "" ]
         uuidResolution = ""

         class VmfsUuidResolution(Enum):
            resignature = 0
            forceMount = 1

      class UnresolvedVmfsVolume(vmodl.DynamicData):
         extent = [ vim.host.UnresolvedVmfsExtent() ]
         vmfsLabel = ""
         vmfsUuid = ""
         totalBlocks = 0
         resolveStatus = vim.host.UnresolvedVmfsVolume.ResolveStatus()

         class ResolveStatus(vmodl.DynamicData):
            resolvable = False
            incompleteExtents = False
            multipleCopies = False

      class VFlashResourceConfigurationResult(vmodl.DynamicData):
         devicePath = [ "" ]
         vffs = vim.host.VffsVolume()
         diskConfigurationResult = [ vim.host.DiskConfigurationResult() ]

      class VMotionConfig(vmodl.DynamicData):
         vmotionNicKey = ""
         enabled = False

      class VMotionSystem(vim.ExtensibleManagedObject):
         netConfig = vim.host.VMotionSystem.NetConfig()
         ipConfig = vim.host.IpConfig()

         def updateIpConfig(ipConfig=vim.host.IpConfig()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def selectVnic(device=""):
            # throws vim.fault.HostConfigFault
            return None

         def deselectVnic():
            # throws vim.fault.HostConfigFault
            return None

         class NetConfig(vmodl.DynamicData):
            candidateVnic = [ vim.host.VirtualNic() ]
            selectedVnic = vim.host.VirtualNic()

      class VfatVolume(vim.host.FileSystemVolume):
         pass

      class VirtualNic(vmodl.DynamicData):
         device = ""
         key = ""
         portgroup = ""
         spec = vim.host.VirtualNic.Specification()
         port = vim.host.PortGroup.Port()

         class Specification(vmodl.DynamicData):
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

         class Config(vmodl.DynamicData):
            changeOperation = ""
            device = ""
            portgroup = ""
            spec = vim.host.VirtualNic.Specification()

         class OpaqueNetworkSpec(vmodl.DynamicData):
            opaqueNetworkId = ""
            opaqueNetworkType = ""

         class IpRouteSpec(vmodl.DynamicData):
            ipRouteConfig = vim.host.IpRouteConfig()

      class VirtualNicConnection(vmodl.DynamicData):
         portgroup = ""
         dvPort = vim.dvs.PortConnection()
         opNetwork = vim.host.VirtualNic.OpaqueNetworkSpec()

      class VirtualNicManager(vim.ExtensibleManagedObject):
         info = vim.host.VirtualNicManagerInfo()

         def queryNetConfig(nicType=""):
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return vim.host.VirtualNicManager.NetConfig()

         def selectVnic(nicType="", device=""):
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return None

         def deselectVnic(nicType="", device=""):
            # throws vim.fault.HostConfigFault, vmodl.fault.InvalidArgument
            return None

         class NicType(Enum):
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

         class NicTypeSelection(vmodl.DynamicData):
            vnic = vim.host.VirtualNicConnection()
            nicType = [ "" ]

         class NetConfig(vmodl.DynamicData):
            nicType = ""
            multiSelectAllowed = False
            candidateVnic = [ vim.host.VirtualNic() ]
            selectedVnic = [ vim.host.VirtualNic() ]

      class VirtualNicManagerInfo(vmodl.DynamicData):
         netConfig = [ vim.host.VirtualNicManager.NetConfig() ]

      class VirtualSwitch(vmodl.DynamicData):
         name = ""
         key = ""
         numPorts = 0
         numPortsAvailable = 0
         mtu = 0
         portgroup = [ vim.host.PortGroup() ]
         pnic = [ vim.host.PhysicalNic() ]
         spec = vim.host.VirtualSwitch.Specification()

         class Bridge(vmodl.DynamicData):
            pass

         class AutoBridge(vim.host.VirtualSwitch.Bridge):
            excludedNicDevice = [ "" ]

         class SimpleBridge(vim.host.VirtualSwitch.Bridge):
            nicDevice = ""

         class BondBridge(vim.host.VirtualSwitch.Bridge):
            nicDevice = [ "" ]
            beacon = vim.host.VirtualSwitch.BeaconConfig()
            linkDiscoveryProtocolConfig = vim.host.LinkDiscoveryProtocolConfig()

         class BeaconConfig(vmodl.DynamicData):
            interval = 0

         class Specification(vmodl.DynamicData):
            numPorts = 0
            bridge = vim.host.VirtualSwitch.Bridge()
            policy = vim.host.NetworkPolicy()
            mtu = 0

         class Config(vmodl.DynamicData):
            changeOperation = ""
            name = ""
            spec = vim.host.VirtualSwitch.Specification()

      class VmciAccessManager(object):

         class Mode(Enum):
            grant = 0
            replace = 1
            revoke = 2

         class AccessSpec(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            services = [ "" ]
            mode = ""

      class VmfsDatastoreOption(vmodl.DynamicData):
         info = vim.host.VmfsDatastoreOption.Info()
         spec = vim.host.VmfsDatastoreSpec()

         class Info(vmodl.DynamicData):
            layout = vim.host.DiskPartitionInfo.Layout()
            partitionFormatChange = False

         class SingleExtentInfo(vim.host.VmfsDatastoreOption.Info):
            vmfsExtent = vim.host.DiskPartitionInfo.BlockRange()

         class AllExtentInfo(vim.host.VmfsDatastoreOption.SingleExtentInfo):
            pass

         class MultipleExtentInfo(vim.host.VmfsDatastoreOption.Info):
            vmfsExtent = [ vim.host.DiskPartitionInfo.BlockRange() ]

      class VmfsDatastoreSpec(vmodl.DynamicData):
         diskUuid = ""

      class VmfsRescanResult(vmodl.DynamicData):
         host = vim.HostSystem()
         fault = vmodl.MethodFault()

      class VsanInternalSystem(vmodl.ManagedObject):

         def queryCmmds(queries=[ vim.host.VsanInternalSystem.CmmdsQuery() ]):
            return ""

         def queryPhysicalVsanDisks(props=[ "" ] or None):
            return ""

         def queryVsanObjects(uuids=[ "" ] or None):
            return ""

         def queryObjectsOnPhysicalVsanDisk(disks=[ "" ]):
            return ""

         def abdicateDomOwnership(uuids=[ "" ]):
            return [ "" ]

         def queryVsanStatistics(labels=[ "" ]):
            return ""

         def reconfigureDomObject(uuid="", policy=""):
            return None

         def querySyncingVsanObjects(uuids=[ "" ] or None):
            return ""

         def runVsanPhysicalDiskDiagnostics(disks=[ "" ] or None):
            return [ vim.host.VsanInternalSystem.VsanPhysicalDiskDiagnosticsResult() ]

         def getVsanObjExtAttrs(uuids=[ "" ]):
            # throws vim.fault.VimFault
            return ""

         def reconfigurationSatisfiable(pcbs=[ vim.host.VsanInternalSystem.PolicyChangeBatch() ], ignoreSatisfiability=False or None):
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.PolicySatisfiability() ]

         def canProvisionObjects(npbs=[ vim.host.VsanInternalSystem.NewPolicyBatch() ], ignoreSatisfiability=False or None):
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.PolicySatisfiability() ]

         def deleteVsanObjects(uuids=[ "" ], force=False or None):
            # throws vim.fault.VimFault
            return [ vim.host.VsanInternalSystem.DeleteVsanObjectsResult() ]

         def upgradeVsanObjects(uuids=[ "" ], newVersion=0):
            # throws vim.fault.VsanFault
            return [ vim.host.VsanInternalSystem.VsanObjectOperationResult() ]

         def queryVsanObjectUuidsByFilter(uuids=[ "" ] or None, limit=0 or None, version=0 or None):
            # throws vim.fault.VsanFault
            return [ "" ]

         class CmmdsQuery(vmodl.DynamicData):
            type = ""
            uuid = ""
            owner = ""

         class PolicyCost(vmodl.DynamicData):
            changeDataSize = 0
            currentDataSize = 0
            tempDataSize = 0
            copyDataSize = 0
            changeFlashReadCacheSize = 0
            currentFlashReadCacheSize = 0
            currentDiskSpaceToAddressSpaceRatio = 0.0
            diskSpaceToAddressSpaceRatio = 0.0

         class PolicySatisfiability(vmodl.DynamicData):
            uuid = ""
            isSatisfiable = False
            reason = vmodl.LocalizableMessage()
            cost = vim.host.VsanInternalSystem.PolicyCost()

         class PolicyChangeBatch(vmodl.DynamicData):
            uuid = [ "" ]
            policy = ""

         class NewPolicyBatch(vmodl.DynamicData):
            size = [ 0 ]
            policy = ""

         class VsanPhysicalDiskDiagnosticsResult(vmodl.DynamicData):
            diskUuid = ""
            success = False
            failureReason = ""

         class DeleteVsanObjectsResult(vmodl.DynamicData):
            uuid = ""
            success = False
            failureReason = [ vmodl.LocalizableMessage() ]

         class VsanObjectOperationResult(vmodl.DynamicData):
            uuid = ""
            failureReason = [ vmodl.LocalizableMessage() ]

      class VsanSystem(vmodl.ManagedObject):
         config = vim.vsan.host.ConfigInfo()

         def queryDisksForVsan(canonicalName=[ "" ] or None):
            return [ vim.vsan.host.DiskResult() ]

         def addDisks(disk=[ vim.host.ScsiDisk() ]):
            return vim.Task()

         def initializeDisks(mapping=[ vim.vsan.host.DiskMapping() ]):
            return vim.Task()

         def removeDisk(disk=[ vim.host.ScsiDisk() ], maintenanceSpec=vim.host.MaintenanceSpec() or None, timeout=0 or None):
            return vim.Task()

         def removeDiskMapping(mapping=[ vim.vsan.host.DiskMapping() ], maintenanceSpec=vim.host.MaintenanceSpec() or None, timeout=0 or None):
            return vim.Task()

         def unmountDiskMapping(mapping=[ vim.vsan.host.DiskMapping() ]):
            # throws vim.fault.InvalidState, vim.fault.VsanFault
            return vim.Task()

         def update(config=vim.vsan.host.ConfigInfo()):
            return vim.Task()

         def queryHostStatus():
            return vim.vsan.host.ClusterStatus()

         def evacuateNode(maintenanceSpec=vim.host.MaintenanceSpec(), timeout=0):
            # throws vim.fault.InvalidState, vmodl.fault.RequestCanceled, vim.fault.Timedout, vim.fault.VsanFault
            return vim.Task()

         def recommissionNode():
            # throws vim.fault.InvalidState, vim.fault.VsanFault
            return vim.Task()

      class VvolVolume(vim.host.FileSystemVolume):
         scId = ""
         hostPE = [ vim.host.VvolVolume.HostProtocolEndpoint() ]
         vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
         storageArray = [ vim.VasaStorageArray() ]

         class Specification(vmodl.DynamicData):
            maxSizeInMB = 0
            volumeName = ""
            vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
            storageArray = [ vim.VasaStorageArray() ]
            uuid = ""

         class HostProtocolEndpoint(vmodl.DynamicData):
            key = vim.HostSystem()
            protocolEndpoint = [ vim.host.ProtocolEndpoint() ]

      class ActiveDirectoryAuthentication(vim.host.DirectoryStore):

         def joinDomain(domainName="", userName="", password=""):
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.InvalidLogin, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def joinDomainWithCAM(domainName="", camServer=""):
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def importCertificateForCAM(certPath="", camServer=""):
            # throws vim.fault.FileNotFound, vim.fault.ActiveDirectoryFault
            return vim.Task()

         def leaveCurrentDomain(force=False):
            # throws vim.fault.InvalidState, vim.fault.AuthMinimumAdminPermission, vim.fault.ActiveDirectoryFault, vim.fault.TaskInProgress
            return vim.Task()

         def enableSmartCardAuthentication():
            # throws vim.fault.ActiveDirectoryFault, vim.fault.HostConfigFault
            return None

         def installSmartCardTrustAnchor(cert=""):
            # throws vim.fault.HostConfigFault
            return None

         def replaceSmartCardTrustAnchors(certs=[ "" ] or None):
            return None

         def removeSmartCardTrustAnchor(issuer="", serial=""):
            # throws vim.fault.HostConfigFault
            return None

         def removeSmartCardTrustAnchorByFingerprint(fingerprint="", digest=""):
            # throws vim.fault.HostConfigFault
            return None

         def listSmartCardTrustAnchors():
            # throws vim.fault.HostConfigFault
            return [ "" ]

         def disableSmartCardAuthentication():
            # throws vim.fault.ActiveDirectoryFault, vim.fault.HostConfigFault
            return None

         class CertificateDigest(Enum):
            SHA1 = 0

      class ActiveDirectoryInfo(vim.host.DirectoryStoreInfo):
         joinedDomain = ""
         trustedDomain = [ "" ]
         domainMembershipStatus = ""
         smartCardAuthenticationEnabled = False

         class DomainMembershipStatus(Enum):
            unknown = 0
            ok = 1
            noServers = 2
            clientTrustBroken = 3
            serverTrustBroken = 4
            inconsistentTrust = 5
            otherProblem = 6

      class BlockAdapterTargetTransport(vim.host.TargetTransport):
         pass

      class BlockHba(vim.host.HostBusAdapter):
         pass

      class BootDeviceInfo(vmodl.DynamicData):
         bootDevices = [ vim.host.BootDeviceSystem.BootDevice() ]
         currentBootDeviceKey = ""

      class ConfigSpec(vmodl.DynamicData):
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

      class ConnectSpec(vmodl.DynamicData):
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

      class DatastoreSystem(vmodl.ManagedObject):
         datastore = [ vim.Datastore() ]
         capabilities = vim.host.DatastoreSystem.Capabilities()

         def updateLocalSwapDatastore(datastore=vim.Datastore() or None):
            # throws vim.fault.InaccessibleDatastore, vim.fault.DatastoreNotWritableOnHost
            return None

         def queryAvailableDisksForVmfs(datastore=vim.Datastore() or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.ScsiDisk() ]

         def queryVmfsDatastoreCreateOptions(devicePath="", vmfsMajorVersion=0 or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def createVmfsDatastore(spec=vim.host.VmfsDatastoreCreateSpec()):
            # throws vim.fault.DuplicateName, vim.fault.HostConfigFault
            return vim.Datastore()

         def queryVmfsDatastoreExtendOptions(datastore=vim.Datastore(), devicePath="", suppressExpandCandidates=False or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def queryVmfsDatastoreExpandOptions(datastore=vim.Datastore()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.VmfsDatastoreOption() ]

         def extendVmfsDatastore(datastore=vim.Datastore(), spec=vim.host.VmfsDatastoreExtendSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Datastore()

         def enableClusteredVmdkSupport(datastore=vim.Datastore()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableClusteredVmdkSupport(datastore=vim.Datastore()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def expandVmfsDatastore(datastore=vim.Datastore(), spec=vim.host.VmfsDatastoreExpandSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Datastore()

         def createNasDatastore(spec=vim.host.NasVolume.Specification()):
            # throws vim.fault.DuplicateName, vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.Datastore()

         def createLocalDatastore(name="", path=""):
            # throws vim.fault.DuplicateName, vim.fault.HostConfigFault, vim.fault.FileNotFound, vim.fault.InvalidName
            return vim.Datastore()

         def createVvolDatastore(spec=vim.host.DatastoreSystem.VvolDatastoreSpec()):
            # throws vim.fault.NotFound, vim.fault.DuplicateName, vim.fault.HostConfigFault, vim.fault.InvalidName
            return vim.Datastore()

         def removeDatastore(datastore=vim.Datastore()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def removeDatastoreEx(datastore=[ vim.Datastore() ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def configureDatastorePrincipal(userName="", password="" or None):
            # throws vim.fault.InvalidState, vim.fault.HostConfigFault
            return None

         def queryUnresolvedVmfsVolumes():
            return [ vim.host.UnresolvedVmfsVolume() ]

         def resignatureUnresolvedVmfsVolume(resolutionSpec=vim.host.UnresolvedVmfsResignatureSpec()):
            # throws vim.fault.VmfsAmbiguousMount, vim.fault.HostConfigFault
            return vim.Task()

         class Capabilities(vmodl.DynamicData):
            nfsMountCreationRequired = False
            nfsMountCreationSupported = False
            localDatastoreSupported = False
            vmfsExtentExpansionSupported = False

         class VvolDatastoreSpec(vmodl.DynamicData):
            name = ""
            scId = ""

         class DatastoreResult(vmodl.DynamicData):
            key = vim.Datastore()
            fault = vmodl.MethodFault()

      class DateTimeInfo(vmodl.DynamicData):
         timeZone = vim.host.DateTimeSystem.TimeZone()
         systemClockProtocol = ""
         ntpConfig = vim.host.NtpConfig()

         class Protocol(Enum):
            ntp = 0
            ptp = 1

      class FibreChannelHba(vim.host.HostBusAdapter):
         portWorldWideName = 0
         nodeWorldWideName = 0
         portType = vim.host.FibreChannelHba.PortType()
         speed = 0

         class PortType(Enum):
            fabric = 0
            loop = 1
            pointToPoint = 2
            unknown = 3

      class FibreChannelOverEthernetHba(vim.host.FibreChannelHba):
         underlyingNic = ""
         linkInfo = vim.host.FibreChannelOverEthernetHba.LinkInfo()
         isSoftwareFcoe = False
         markedForRemoval = False

         class LinkInfo(vmodl.DynamicData):
            vnportMac = ""
            fcfMac = ""
            vlanId = 0

      class FibreChannelTargetTransport(vim.host.TargetTransport):
         portWorldWideName = 0
         nodeWorldWideName = 0

      class FirewallConfig(vmodl.DynamicData):
         rule = [ vim.host.FirewallConfig.RuleSetConfig() ]
         defaultBlockingPolicy = vim.host.FirewallInfo.DefaultPolicy()

         class RuleSetConfig(vmodl.DynamicData):
            rulesetId = ""
            enabled = False
            allowedHosts = vim.host.Ruleset.IpList()

      class FirewallSystem(vim.ExtensibleManagedObject):
         firewallInfo = vim.host.FirewallInfo()

         def updateDefaultPolicy(defaultPolicy=vim.host.FirewallInfo.DefaultPolicy()):
            return None

         def enableRuleset(id=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableRuleset(id=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateRuleset(id="", spec=vim.host.Ruleset.RulesetSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh():
            return None

      class InternetScsiHba(vim.host.HostBusAdapter):
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

         class ParamValue(vim.option.OptionValue):
            isInherited = False

         class DiscoveryCapabilities(vmodl.DynamicData):
            iSnsDiscoverySettable = False
            slpDiscoverySettable = False
            staticTargetDiscoverySettable = False
            sendTargetsDiscoverySettable = False

         class DiscoveryProperties(vmodl.DynamicData):
            iSnsDiscoveryEnabled = False
            iSnsDiscoveryMethod = ""
            iSnsHost = ""
            slpDiscoveryEnabled = False
            slpDiscoveryMethod = ""
            slpHost = ""
            staticTargetDiscoveryEnabled = False
            sendTargetsDiscoveryEnabled = False

            class ISnsDiscoveryMethod(Enum):
               isnsStatic = 0
               isnsDhcp = 1
               isnsSlp = 2

            class SlpDiscoveryMethod(Enum):
               slpDhcp = 0
               slpAutoUnicast = 1
               slpAutoMulticast = 2
               slpManual = 3

         class ChapAuthenticationType(Enum):
            chapProhibited = 0
            chapDiscouraged = 1
            chapPreferred = 2
            chapRequired = 3

         class AuthenticationCapabilities(vmodl.DynamicData):
            chapAuthSettable = False
            krb5AuthSettable = False
            srpAuthSettable = False
            spkmAuthSettable = False
            mutualChapSettable = False
            targetChapSettable = False
            targetMutualChapSettable = False

         class AuthenticationProperties(vmodl.DynamicData):
            chapAuthEnabled = False
            chapName = ""
            chapSecret = ""
            chapAuthenticationType = ""
            chapInherited = False
            mutualChapName = ""
            mutualChapSecret = ""
            mutualChapAuthenticationType = ""
            mutualChapInherited = False

         class DigestType(Enum):
            digestProhibited = 0
            digestDiscouraged = 1
            digestPreferred = 2
            digestRequired = 3

         class DigestCapabilities(vmodl.DynamicData):
            headerDigestSettable = False
            dataDigestSettable = False
            targetHeaderDigestSettable = False
            targetDataDigestSettable = False

         class DigestProperties(vmodl.DynamicData):
            headerDigestType = ""
            headerDigestInherited = False
            dataDigestType = ""
            dataDigestInherited = False

         class IPCapabilities(vmodl.DynamicData):
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

         class IscsiIpv6Address(vmodl.DynamicData):
            address = ""
            prefixLength = 0
            origin = ""
            operation = ""

            class AddressConfigurationType(Enum):
               DHCP = 0
               AutoConfigured = 1
               Static = 2
               Other = 3

            class IPv6AddressOperation(Enum):
               add = 0
               remove = 1

         class IPv6Properties(vmodl.DynamicData):
            iscsiIpv6Address = [ vim.host.InternetScsiHba.IscsiIpv6Address() ]
            ipv6DhcpConfigurationEnabled = False
            ipv6LinkLocalAutoConfigurationEnabled = False
            ipv6RouterAdvertisementConfigurationEnabled = False
            ipv6DefaultGateway = ""

         class IPProperties(vmodl.DynamicData):
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

         class SendTarget(vmodl.DynamicData):
            address = ""
            port = 0
            authenticationProperties = vim.host.InternetScsiHba.AuthenticationProperties()
            digestProperties = vim.host.InternetScsiHba.DigestProperties()
            supportedAdvancedOptions = [ vim.option.OptionDef() ]
            advancedOptions = [ vim.host.InternetScsiHba.ParamValue() ]
            parent = ""

         class StaticTarget(vmodl.DynamicData):
            address = ""
            port = 0
            iScsiName = ""
            discoveryMethod = ""
            authenticationProperties = vim.host.InternetScsiHba.AuthenticationProperties()
            digestProperties = vim.host.InternetScsiHba.DigestProperties()
            supportedAdvancedOptions = [ vim.option.OptionDef() ]
            advancedOptions = [ vim.host.InternetScsiHba.ParamValue() ]
            parent = ""

            class TargetDiscoveryMethod(Enum):
               staticMethod = 0
               sendTargetMethod = 1
               slpMethod = 2
               isnsMethod = 3
               unknownMethod = 4

         class TargetSet(vmodl.DynamicData):
            staticTargets = [ vim.host.InternetScsiHba.StaticTarget() ]
            sendTargets = [ vim.host.InternetScsiHba.SendTarget() ]

         class NetworkBindingSupportType(Enum):
            notsupported = 0
            optional = 1
            required = 2

      class InternetScsiTargetTransport(vim.host.TargetTransport):
         iScsiName = ""
         iScsiAlias = ""
         address = [ "" ]

      class NetworkConfig(vmodl.DynamicData):
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

         class Result(vmodl.DynamicData):
            vnicDevice = [ "" ]
            consoleVnicDevice = [ "" ]

         class NetStackSpec(vmodl.DynamicData):
            netStackInstance = vim.host.NetStackInstance()
            operation = ""

      class NetworkSystem(vim.ExtensibleManagedObject):
         capabilities = vim.host.NetCapabilities()
         networkInfo = vim.host.NetworkInfo()
         offloadCapabilities = vim.host.NetOffloadCapabilities()
         networkConfig = vim.host.NetworkConfig()
         dnsConfig = vim.host.DnsConfig()
         ipRouteConfig = vim.host.IpRouteConfig()
         consoleIpRouteConfig = vim.host.IpRouteConfig()

         def updateNetworkConfig(config=vim.host.NetworkConfig(), changeMode=""):
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return vim.host.NetworkConfig.Result()

         def updateDnsConfig(config=vim.host.DnsConfig()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateIpRouteConfig(config=vim.host.IpRouteConfig()):
            # throws vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def updateConsoleIpRouteConfig(config=vim.host.IpRouteConfig()):
            # throws vim.fault.HostConfigFault
            return None

         def updateIpRouteTableConfig(config=vim.host.IpRouteTableConfig()):
            # throws vim.fault.HostConfigFault
            return None

         def addVirtualSwitch(vswitchName="", spec=vim.host.VirtualSwitch.Specification() or None):
            # throws vim.fault.AlreadyExists, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def removeVirtualSwitch(vswitchName=""):
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updateVirtualSwitch(vswitchName="", spec=vim.host.VirtualSwitch.Specification()):
            # throws vim.fault.ResourceInUse, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addPortGroup(portgrp=vim.host.PortGroup.Specification()):
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removePortGroup(pgName=""):
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updatePortGroup(pgName="", portgrp=vim.host.PortGroup.Specification()):
            # throws vim.fault.AlreadyExists, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updatePhysicalNicLinkSpeed(device="", linkSpeed=vim.host.PhysicalNic.LinkSpeedDuplex() or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryNetworkHint(device=[ "" ] or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.PhysicalNic.NetworkHint() ]

         def addVirtualNic(portgroup="", nic=vim.host.VirtualNic.Specification()):
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault, vim.fault.InvalidState
            return ""

         def removeVirtualNic(device=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateVirtualNic(device="", nic=vim.host.VirtualNic.Specification()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def addServiceConsoleVirtualNic(portgroup="", nic=vim.host.VirtualNic.Specification()):
            # throws vim.fault.HostConfigFault
            return ""

         def removeServiceConsoleVirtualNic(device=""):
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def updateServiceConsoleVirtualNic(device="", nic=vim.host.VirtualNic.Specification()):
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def restartServiceConsoleVirtualNic(device=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def refresh():
            return None

      class NvmeConnectSpec(vim.host.NvmeSpec):
         subnqn = ""
         controllerId = 0
         adminQueueSize = 0
         keepAliveTimeout = 0

      class NvmeDiscoverSpec(vim.host.NvmeSpec):
         autoConnect = False

      class NvmeOpaqueTransportParameters(vim.host.NvmeTransportParameters):
         trtype = ""
         traddr = ""
         adrfam = ""
         trsvcid = ""
         tsas = vmodl.Binary()

      class NvmeOverFibreChannelParameters(vim.host.NvmeTransportParameters):
         nodeWorldWideName = 0
         portWorldWideName = 0

      class NvmeOverRdmaParameters(vim.host.NvmeTransportParameters):
         address = ""
         addressFamily = ""
         portNumber = 0

      class OpaqueNetworkInfo(vmodl.DynamicData):
         opaqueNetworkId = ""
         opaqueNetworkName = ""
         opaqueNetworkType = ""
         pnicZone = [ "" ]
         capability = vim.OpaqueNetwork.Capability()
         extraConfig = [ vim.option.OptionValue() ]

      class ParallelScsiTargetTransport(vim.host.TargetTransport):
         pass

      class PcieTargetTransport(vim.host.TargetTransport):
         pass

      class RdmaTargetTransport(vim.host.TargetTransport):
         pass

      class ScsiDisk(vim.host.ScsiLun):
         capacity = vim.host.DiskDimensions.Lba()
         devicePath = ""
         ssd = False
         localDisk = False
         physicalLocation = [ "" ]
         emulatedDIXDIFEnabled = False
         vsanDiskInfo = vim.vsan.host.VsanDiskInfo()
         scsiDiskType = ""

         class Partition(vmodl.DynamicData):
            diskName = ""
            partition = 0

         class ScsiDiskType(Enum):
            native512 = 0
            emulated512 = 1
            native4k = 2
            SoftwareEmulated4k = 3
            unknown = 4

      class SecuritySpec(vmodl.DynamicData):
         adminPassword = ""
         removePermission = [ vim.AuthorizationManager.Permission() ]
         addPermission = [ vim.AuthorizationManager.Permission() ]

      class SerialAttachedTargetTransport(vim.host.TargetTransport):
         pass

      class Summary(vmodl.DynamicData):
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

         class HardwareSummary(vmodl.DynamicData):
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

         class QuickStats(vmodl.DynamicData):
            overallCpuUsage = 0
            overallMemoryUsage = 0
            distributedCpuFairness = 0
            distributedMemoryFairness = 0
            availablePMemCapacity = 0
            uptime = 0

         class ConfigSummary(vmodl.DynamicData):
            name = ""
            port = 0
            sslThumbprint = ""
            product = vim.AboutInfo()
            vmotionEnabled = False
            faultToleranceEnabled = False
            featureVersion = [ vim.host.FeatureVersionInfo() ]
            agentVmDatastore = vim.Datastore()
            agentVmNetwork = vim.Network()

         class GatewaySummary(vmodl.DynamicData):
            gatewayType = ""
            gatewayId = ""

      class TpmBootSecurityOptionEventDetails(vim.host.TpmEventDetails):
         bootSecurityOption = ""

      class TpmCommandEventDetails(vim.host.TpmEventDetails):
         commandLine = ""

      class UnresolvedVmfsExtent(vmodl.DynamicData):
         device = vim.host.ScsiDisk.Partition()
         devicePath = ""
         vmfsUuid = ""
         isHeadExtent = False
         ordinal = 0
         startBlock = 0
         endBlock = 0
         reason = ""

         class UnresolvedReason(Enum):
            diskIdMismatch = 0
            uuidConflict = 1

      class VFlashManager(vmodl.ManagedObject):
         vFlashConfigInfo = vim.host.VFlashManager.VFlashConfigInfo()

         def configureVFlashResourceEx(devicePath=[ "" ] or None):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def configureVFlashResource(spec=vim.host.VFlashManager.VFlashResourceConfigSpec()):
            # throws vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def removeVFlashResource():
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def configureHostVFlashCache(spec=vim.host.VFlashManager.VFlashCacheConfigSpec()):
            # throws vim.fault.HostConfigFault, vim.fault.InaccessibleVFlashSource, vim.fault.ResourceInUse
            return None

         def getVFlashModuleDefaultConfig(vFlashModule=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.vm.device.VirtualDisk.VFlashCacheConfigInfo()

         class VFlashResourceConfigSpec(vmodl.DynamicData):
            vffsUuid = ""

         class VFlashResourceConfigInfo(vmodl.DynamicData):
            vffs = vim.host.VffsVolume()
            capacity = 0

         class VFlashResourceRunTimeInfo(vmodl.DynamicData):
            usage = 0
            capacity = 0
            accessible = False
            capacityForVmCache = 0
            freeForVmCache = 0

         class VFlashCacheConfigSpec(vmodl.DynamicData):
            defaultVFlashModule = ""
            swapCacheReservationInGB = 0

         class VFlashCacheConfigInfo(vmodl.DynamicData):
            vFlashModuleConfigOption = [ vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption() ]
            defaultVFlashModule = ""
            swapCacheReservationInGB = 0

            class VFlashModuleConfigOption(vmodl.DynamicData):
               vFlashModule = ""
               vFlashModuleVersion = ""
               minSupportedModuleVersion = ""
               cacheConsistencyType = vim.option.ChoiceOption()
               cacheMode = vim.option.ChoiceOption()
               blockSizeInKBOption = vim.option.LongOption()
               reservationInMBOption = vim.option.LongOption()
               maxDiskSizeInKB = 0

         class VFlashConfigInfo(vmodl.DynamicData):
            vFlashResourceConfigInfo = vim.host.VFlashManager.VFlashResourceConfigInfo()
            vFlashCacheConfigInfo = vim.host.VFlashManager.VFlashCacheConfigInfo()

      class VMotionInfo(vmodl.DynamicData):
         netConfig = vim.host.VMotionSystem.NetConfig()
         ipConfig = vim.host.IpConfig()

      class VffsVolume(vim.host.FileSystemVolume):
         majorVersion = 0
         version = ""
         uuid = ""
         extent = [ vim.host.ScsiDisk.Partition() ]

         class Specification(vmodl.DynamicData):
            devicePath = ""
            partition = vim.host.DiskPartitionInfo.Specification()
            majorVersion = 0
            volumeName = ""

      class VmfsDatastoreExpandSpec(vim.host.VmfsDatastoreSpec):
         partition = vim.host.DiskPartitionInfo.Specification()
         extent = vim.host.ScsiDisk.Partition()

      class VmfsDatastoreExtendSpec(vim.host.VmfsDatastoreSpec):
         partition = vim.host.DiskPartitionInfo.Specification()
         extent = [ vim.host.ScsiDisk.Partition() ]

      class VmfsVolume(vim.host.FileSystemVolume):
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

         class Specification(vmodl.DynamicData):
            extent = vim.host.ScsiDisk.Partition()
            blockSizeMb = 0
            majorVersion = 0
            volumeName = ""
            blockSize = 0
            unmapGranularity = 0
            unmapPriority = ""
            unmapBandwidthSpec = vim.host.VmfsVolume.UnmapBandwidthSpec()

         class UnmapBandwidthSpec(vmodl.DynamicData):
            policy = ""
            fixedValue = 0
            dynamicMin = 0
            dynamicMax = 0

         class UnmapPriority(Enum):
            none = 0
            low = 1

         class UnmapBandwidthPolicy(Enum):
            fixed = 0
            dynamic = 1

         class ConfigOption(vmodl.DynamicData):
            blockSizeOption = 0
            unmapGranularityOption = [ 0 ]
            unmapBandwidthFixedValue = vim.option.LongOption()
            unmapBandwidthDynamicMin = vim.option.LongOption()
            unmapBandwidthDynamicMax = vim.option.LongOption()
            unmapBandwidthIncrement = 0

      class ConfigInfo(vmodl.DynamicData):
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

      class ConnectInfo(vmodl.DynamicData):
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

         class NetworkInfo(vmodl.DynamicData):
            summary = vim.Network.Summary()

         class NewNetworkInfo(vim.host.ConnectInfo.NetworkInfo):
            pass

         class DatastoreInfo(vmodl.DynamicData):
            summary = vim.Datastore.Summary()

         class DatastoreExistsInfo(vim.host.ConnectInfo.DatastoreInfo):
            newDatastoreName = ""

         class DatastoreNameConflictInfo(vim.host.ConnectInfo.DatastoreInfo):
            newDatastoreName = ""

         class LicenseInfo(vmodl.DynamicData):
            license = vim.LicenseManager.LicenseInfo()
            evaluation = vim.LicenseManager.EvaluationInfo()
            resource = vim.LicenseManager.LicensableResourceInfo()

      class DiagnosticPartition(vmodl.DynamicData):
         storageType = ""
         diagnosticType = ""
         slots = 0
         id = vim.host.ScsiDisk.Partition()

         class StorageType(Enum):
            directAttached = 0
            networkAttached = 1

         class DiagnosticType(Enum):
            singleHost = 0
            multiHost = 1

         class CreateOption(vmodl.DynamicData):
            storageType = ""
            diagnosticType = ""
            disk = vim.host.ScsiDisk()

         class CreateSpec(vmodl.DynamicData):
            storageType = ""
            diagnosticType = ""
            id = vim.host.ScsiDisk.Partition()
            partition = vim.host.DiskPartitionInfo.Specification()
            active = False

         class CreateDescription(vmodl.DynamicData):
            layout = vim.host.DiskPartitionInfo.Layout()
            diskUuid = ""
            spec = vim.host.DiagnosticPartition.CreateSpec()

      class DiagnosticSystem(vmodl.ManagedObject):
         activePartition = vim.host.DiagnosticPartition()

         def queryAvailablePartition():
            # throws vim.fault.HostConfigFault
            return [ vim.host.DiagnosticPartition() ]

         def selectActivePartition(partition=vim.host.ScsiDisk.Partition() or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryPartitionCreateOptions(storageType="", diagnosticType=""):
            # throws vim.fault.HostConfigFault
            return [ vim.host.DiagnosticPartition.CreateOption() ]

         def queryPartitionCreateDesc(diskUuid="", diagnosticType=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiagnosticPartition.CreateDescription()

         def createDiagnosticPartition(spec=vim.host.DiagnosticPartition.CreateSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

      class FibreChannelOverEthernetTargetTransport(vim.host.FibreChannelTargetTransport):
         vnportMac = ""
         fcfMac = ""
         vlanId = 0

      class LocalDatastoreInfo(vim.Datastore.Info):
         path = ""

      class NasDatastoreInfo(vim.Datastore.Info):
         nas = vim.host.NasVolume()

      class PMemDatastoreInfo(vim.Datastore.Info):
         pmem = vim.host.PMemVolume()

      class RuntimeInfo(vmodl.DynamicData):
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

         class NetStackInstanceRuntimeInfo(vmodl.DynamicData):
            netStackInstanceKey = ""
            state = ""
            vmknicKeys = [ "" ]
            maxNumberOfConnections = 0
            currentIpV6Enabled = False

            class State(Enum):
               inactive = 0
               active = 1
               deactivating = 2
               activating = 3

         class PlacedVirtualNicIdentifier(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            vnicKey = ""
            reservation = 0

         class PnicNetworkResourceInfo(vmodl.DynamicData):
            pnicDevice = ""
            availableBandwidthForVMTraffic = 0
            unusedBandwidthForVMTraffic = 0
            placedVirtualNics = [ vim.host.RuntimeInfo.PlacedVirtualNicIdentifier() ]

         class NetworkResourceRuntimeInfo(vmodl.DynamicData):
            pnicResourceInfo = [ vim.host.RuntimeInfo.PnicNetworkResourceInfo() ]

         class NetworkRuntimeInfo(vmodl.DynamicData):
            netStackInstanceRuntimeInfo = [ vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo() ]
            networkResourceRuntime = vim.host.RuntimeInfo.NetworkResourceRuntimeInfo()

      class StorageSystem(vim.ExtensibleManagedObject):
         storageDeviceInfo = vim.host.StorageDeviceInfo()
         fileSystemVolumeInfo = vim.host.FileSystemVolumeInfo()
         systemFile = [ "" ]
         multipathStateInfo = vim.host.MultipathStateInfo()

         def retrieveDiskPartitionInfo(devicePath=[ "" ]):
            return [ vim.host.DiskPartitionInfo() ]

         def computeDiskPartitionInfo(devicePath="", layout=vim.host.DiskPartitionInfo.Layout(), partitionFormat="" or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiskPartitionInfo()

         def computeDiskPartitionInfoForResize(partition=vim.host.ScsiDisk.Partition(), blockRange=vim.host.DiskPartitionInfo.BlockRange(), partitionFormat="" or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.DiskPartitionInfo()

         def updateDiskPartitions(devicePath="", spec=vim.host.DiskPartitionInfo.Specification()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def formatVmfs(createSpec=vim.host.VmfsVolume.Specification()):
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault
            return vim.host.VmfsVolume()

         def mountVmfsVolume(vmfsUuid=""):
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVmfsVolume(vmfsUuid=""):
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVmfsVolumeEx(vmfsUuid=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def mountVmfsVolumeEx(vmfsUuid=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def unmapVmfsVolumeEx(vmfsUuid=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def deleteVmfsVolumeState(vmfsUuid=""):
            # throws vim.fault.HostConfigFault
            return None

         def rescanVmfs():
            # throws vim.fault.HostConfigFault
            return None

         def attachVmfsExtent(vmfsPath="", extent=vim.host.ScsiDisk.Partition()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def expandVmfsExtent(vmfsPath="", extent=vim.host.ScsiDisk.Partition()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def upgradeVmfs(vmfsPath=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def upgradeVmLayout():
            return None

         def queryUnresolvedVmfsVolume():
            return [ vim.host.UnresolvedVmfsVolume() ]

         def resolveMultipleUnresolvedVmfsVolumes(resolutionSpec=[ vim.host.UnresolvedVmfsResolutionSpec() ]):
            # throws vim.fault.HostConfigFault
            return [ vim.host.UnresolvedVmfsResolutionResult() ]

         def resolveMultipleUnresolvedVmfsVolumesEx(resolutionSpec=[ vim.host.UnresolvedVmfsResolutionSpec() ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def unmountForceMountedVmfsVolume(vmfsUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def rescanHba(hbaDevice=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def rescanAllHba():
            # throws vim.fault.HostConfigFault
            return None

         def updateSoftwareInternetScsiEnabled(enabled=False):
            # throws vim.fault.HostConfigFault
            return None

         def updateInternetScsiDiscoveryProperties(iScsiHbaDevice="", discoveryProperties=vim.host.InternetScsiHba.DiscoveryProperties()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAuthenticationProperties(iScsiHbaDevice="", authenticationProperties=vim.host.InternetScsiHba.AuthenticationProperties(), targetSet=vim.host.InternetScsiHba.TargetSet() or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiDigestProperties(iScsiHbaDevice="", targetSet=vim.host.InternetScsiHba.TargetSet() or None, digestProperties=vim.host.InternetScsiHba.DigestProperties()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAdvancedOptions(iScsiHbaDevice="", targetSet=vim.host.InternetScsiHba.TargetSet() or None, options=[ vim.host.InternetScsiHba.ParamValue() ]):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiIPProperties(iScsiHbaDevice="", ipProperties=vim.host.InternetScsiHba.IPProperties()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiName(iScsiHbaDevice="", iScsiName=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateInternetScsiAlias(iScsiHbaDevice="", iScsiAlias=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addInternetScsiSendTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.SendTarget() ]):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeInternetScsiSendTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.SendTarget() ]):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def addInternetScsiStaticTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.StaticTarget() ]):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeInternetScsiStaticTargets(iScsiHbaDevice="", targets=[ vim.host.InternetScsiHba.StaticTarget() ]):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def enableMultipathPath(pathName=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disableMultipathPath(pathName=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def setMultipathLunPolicy(lunId="", policy=vim.host.MultipathInfo.LogicalUnitPolicy()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def updateHppMultipathLunPolicy(lunId="", policy=vim.host.MultipathInfo.HppLogicalUnitPolicy()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryPathSelectionPolicyOptions():
            # throws vim.fault.HostConfigFault
            return [ vim.host.PathSelectionPolicyOption() ]

         def queryStorageArrayTypePolicyOptions():
            # throws vim.fault.HostConfigFault
            return [ vim.host.StorageArrayTypePolicyOption() ]

         def updateScsiLunDisplayName(lunUuid="", displayName=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidName, vim.fault.DuplicateName
            return None

         def detachScsiLun(lunUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState, vim.fault.ResourceInUse
            return None

         def detachScsiLunEx(lunUuid=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def deleteScsiLunState(lunCanonicalName=""):
            # throws vim.fault.HostConfigFault
            return None

         def attachScsiLun(lunUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.InvalidState
            return None

         def attachScsiLunEx(lunUuid=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def refresh():
            return None

         def discoverFcoeHbas(fcoeSpec=vim.host.FcoeConfig.FcoeSpecification()):
            # throws vim.fault.FcoeFaultPnicHasNoPortSet, vim.fault.HostConfigFault, vim.fault.NotFound
            return None

         def markForRemoval(hbaName="", remove=False):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def formatVffs(createSpec=vim.host.VffsVolume.Specification()):
            # throws vim.fault.AlreadyExists, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return vim.host.VffsVolume()

         def extendVffs(vffsPath="", devicePath="", spec=vim.host.DiskPartitionInfo.Specification() or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def destroyVffs(vffsPath=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def mountVffsVolume(vffsUuid=""):
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def unmountVffsVolume(vffsUuid=""):
            # throws vim.fault.NotFound, vim.fault.InvalidState, vim.fault.HostConfigFault, vim.fault.ResourceInUse
            return None

         def deleteVffsVolumeState(vffsUuid=""):
            # throws vim.fault.HostConfigFault
            return None

         def rescanVffs():
            # throws vim.fault.HostConfigFault
            return None

         def queryAvailableSsds(vffsPath="" or None):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return [ vim.host.ScsiDisk() ]

         def setNFSUser(user="", password=""):
            # throws vim.fault.HostConfigFault
            return None

         def changeNFSUserPassword(password=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def queryNFSUser():
            # throws vim.fault.HostConfigFault
            return vim.host.NasVolume.UserInfo()

         def clearNFSUser():
            # throws vim.fault.HostConfigFault
            return None

         def turnDiskLocatorLedOn(scsiDiskUuids=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def turnDiskLocatorLedOff(scsiDiskUuids=[ "" ]):
            # throws vim.fault.HostConfigFault
            return vim.Task()

         def markAsSsd(scsiDiskUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsNonSsd(scsiDiskUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsLocal(scsiDiskUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def markAsNonLocal(scsiDiskUuid=""):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.Task()

         def updateVmfsUnmapPriority(vmfsUuid="", unmapPriority=""):
            return None

         def updateVmfsUnmapBandwidth(vmfsUuid="", unmapBandwidthSpec=vim.host.VmfsVolume.UnmapBandwidthSpec()):
            return None

         def queryVmfsConfigOption():
            return [ vim.host.VmfsVolume.ConfigOption() ]

         def markPerenniallyReserved(lunUuid="", state=False):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def markPerenniallyReservedEx(lunUuid=[ "" ] or None, state=False):
            return vim.Task()

         def createNvmeOverRdmaAdapter(rdmaDeviceName=""):
            # throws vim.fault.ResourceInUse, vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def removeNvmeOverRdmaAdapter(hbaDeviceName=""):
            # throws vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.HostConfigFault
            return None

         def discoverNvmeControllers(discoverSpec=vim.host.NvmeDiscoverSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return vim.host.NvmeDiscoveryLog()

         def connectNvmeController(connectSpec=vim.host.NvmeConnectSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         def disconnectNvmeController(disconnectSpec=vim.host.NvmeDisconnectSpec()):
            # throws vim.fault.NotFound, vim.fault.HostConfigFault
            return None

         class VmfsVolumeResult(vmodl.DynamicData):
            key = ""
            fault = vmodl.MethodFault()

         class ScsiLunResult(vmodl.DynamicData):
            key = ""
            fault = vmodl.MethodFault()

         class DiskLocatorLedResult(vmodl.DynamicData):
            key = ""
            fault = vmodl.MethodFault()

      class VMotionManager(object):

         class SrcInstantCloneResult(vmodl.DynamicData):
            startTime = 0
            quiesceTime = 0
            quiesceDoneTime = 0
            resumeDoneTime = 0
            endTime = 0

         class DstInstantCloneResult(vmodl.DynamicData):
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

      class VmfsDatastoreCreateSpec(vim.host.VmfsDatastoreSpec):
         partition = vim.host.DiskPartitionInfo.Specification()
         vmfs = vim.host.VmfsVolume.Specification()
         extent = [ vim.host.ScsiDisk.Partition() ]

      class VmfsDatastoreInfo(vim.Datastore.Info):
         maxPhysicalRDMFileSize = 0
         maxVirtualRDMFileSize = 0
         vmfs = vim.host.VmfsVolume()

      class VvolDatastoreInfo(vim.Datastore.Info):
         vvolDS = vim.host.VvolVolume()

   class net(object):

      class DhcpConfigInfo(vmodl.DynamicData):
         ipv6 = vim.net.DhcpConfigInfo.DhcpOptions()
         ipv4 = vim.net.DhcpConfigInfo.DhcpOptions()

         class DhcpOptions(vmodl.DynamicData):
            enable = False
            config = [ vim.KeyValue() ]

      class DhcpConfigSpec(vmodl.DynamicData):
         ipv6 = vim.net.DhcpConfigSpec.DhcpOptionsSpec()
         ipv4 = vim.net.DhcpConfigSpec.DhcpOptionsSpec()

         class DhcpOptionsSpec(vmodl.DynamicData):
            enable = False
            config = [ vim.KeyValue() ]
            operation = ""

      class DnsConfigInfo(vmodl.DynamicData):
         dhcp = False
         hostName = ""
         domainName = ""
         ipAddress = [ "" ]
         searchDomain = [ "" ]

      class DnsConfigSpec(vmodl.DynamicData):
         dhcp = False
         hostName = ""
         domainName = ""
         ipAddress = [ "" ]
         searchDomain = [ "" ]

      class IpConfigInfo(vmodl.DynamicData):
         ipAddress = [ vim.net.IpConfigInfo.IpAddress() ]
         dhcp = vim.net.DhcpConfigInfo()
         autoConfigurationEnabled = False

         class IpAddressOrigin(Enum):
            other = 0
            manual = 1
            dhcp = 2
            linklayer = 3
            random = 4

         class IpAddressStatus(Enum):
            preferred = 0
            deprecated = 1
            invalid = 2
            inaccessible = 3
            unknown = 4
            tentative = 5
            duplicate = 6

         class IpAddress(vmodl.DynamicData):
            ipAddress = ""
            prefixLength = 0
            origin = ""
            state = ""
            lifetime = vmodl.DateTime()

      class IpConfigSpec(vmodl.DynamicData):
         ipAddress = [ vim.net.IpConfigSpec.IpAddressSpec() ]
         dhcp = vim.net.DhcpConfigSpec()
         autoConfigurationEnabled = False

         class IpAddressSpec(vmodl.DynamicData):
            ipAddress = ""
            prefixLength = 0
            operation = ""

      class IpRouteConfigInfo(vmodl.DynamicData):
         ipRoute = [ vim.net.IpRouteConfigInfo.IpRoute() ]

         class Gateway(vmodl.DynamicData):
            ipAddress = ""
            device = ""

         class IpRoute(vmodl.DynamicData):
            network = ""
            prefixLength = 0
            gateway = vim.net.IpRouteConfigInfo.Gateway()

      class IpRouteConfigSpec(vmodl.DynamicData):
         ipRoute = [ vim.net.IpRouteConfigSpec.IpRouteSpec() ]

         class GatewaySpec(vmodl.DynamicData):
            ipAddress = ""
            device = ""

         class IpRouteSpec(vmodl.DynamicData):
            network = ""
            prefixLength = 0
            gateway = vim.net.IpRouteConfigSpec.GatewaySpec()
            operation = ""

      class IpStackInfo(vmodl.DynamicData):
         neighbor = [ vim.net.IpStackInfo.NetToMedia() ]
         defaultRouter = [ vim.net.IpStackInfo.DefaultRouter() ]

         class EntryType(Enum):
            other = 0
            invalid = 1
            dynamic = 2
            manual = 3

         class Preference(Enum):
            reserved = 0
            low = 1
            medium = 2
            high = 3

         class NetToMedia(vmodl.DynamicData):
            ipAddress = ""
            physicalAddress = ""
            device = ""
            type = ""

         class DefaultRouter(vmodl.DynamicData):
            ipAddress = ""
            device = ""
            lifetime = vmodl.DateTime()
            preference = ""

      class NetBIOSConfigInfo(vmodl.DynamicData):
         mode = ""

         class Mode(Enum):
            unknown = 0
            enabled = 1
            disabled = 2
            enabledViaDHCP = 3

      class WinNetBIOSConfigInfo(vim.net.NetBIOSConfigInfo):
         primaryWINS = ""
         secondaryWINS = ""

   class option(object):

      class ArrayUpdateSpec(vmodl.DynamicData):
         operation = vim.option.ArrayUpdateSpec.Operation()
         removeKey = anyType()

         class Operation(Enum):
            add = 0
            remove = 1
            edit = 2

      class OptionDef(vim.ElementDescription):
         optionType = vim.option.OptionType()

      class OptionManager(vmodl.ManagedObject):
         supportedOption = [ vim.option.OptionDef() ]
         setting = [ vim.option.OptionValue() ]

         def queryView(name="" or None):
            # throws vim.fault.InvalidName
            return [ vim.option.OptionValue() ]

         def updateValues(changedValue=[ vim.option.OptionValue() ]):
            # throws vim.fault.InvalidName
            return None

      class OptionType(vmodl.DynamicData):
         valueIsReadonly = False

      class OptionValue(vmodl.DynamicData):
         key = ""
         value = anyType()

      class StringOption(vim.option.OptionType):
         defaultValue = ""
         validCharacters = ""

      class BoolOption(vim.option.OptionType):
         supported = False
         defaultValue = False

      class ChoiceOption(vim.option.OptionType):
         choiceInfo = [ vim.ElementDescription() ]
         defaultIndex = 0

      class FloatOption(vim.option.OptionType):
         min = 0.0
         max = 0.0
         defaultValue = 0.0

      class IntOption(vim.option.OptionType):
         min = 0
         max = 0
         defaultValue = 0

      class LongOption(vim.option.OptionType):
         min = 0
         max = 0
         defaultValue = 0

   class profile(object):

      class ApplyProfile(vmodl.DynamicData):
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

      class ApplyProfileElement(vim.profile.ApplyProfile):
         key = ""

      class ApplyProfileProperty(vmodl.DynamicData):
         propertyName = ""
         array = False
         profile = [ vim.profile.ApplyProfile() ]

      class ComplianceLocator(vmodl.DynamicData):
         expressionName = ""
         applyPath = vim.profile.ProfilePropertyPath()

      class ComplianceManager(vmodl.ManagedObject):

         def checkCompliance(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None):
            return vim.Task()

         def queryComplianceStatus(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None):
            return [ vim.profile.ComplianceResult() ]

         def clearComplianceStatus(profile=[ vim.profile.Profile() ] or None, entity=[ vim.ManagedEntity() ] or None):
            return None

         def queryExpressionMetadata(expressionName=[ "" ] or None, profile=vim.profile.Profile() or None):
            return [ vim.profile.ExpressionMetadata() ]

      class ComplianceProfile(vmodl.DynamicData):
         expression = [ vim.profile.Expression() ]
         rootExpression = ""

      class ComplianceResult(vmodl.DynamicData):
         profile = vim.profile.Profile()
         complianceStatus = ""
         entity = vim.ManagedEntity()
         checkTime = vmodl.DateTime()
         failure = [ vim.profile.ComplianceResult.ComplianceFailure() ]

         class Status(Enum):
            compliant = 0
            nonCompliant = 1
            unknown = 2
            running = 3

         class ComplianceFailure(vmodl.DynamicData):
            failureType = ""
            message = vmodl.LocalizableMessage()
            expressionName = ""
            failureValues = [ vim.profile.ComplianceResult.ComplianceFailure.ComplianceFailureValues() ]

            class ComplianceFailureValues(vmodl.DynamicData):
               comparisonIdentifier = ""
               profileInstance = ""
               hostValue = anyType()
               profileValue = anyType()

      class DeferredPolicyOptionParameter(vmodl.DynamicData):
         inputPath = vim.profile.ProfilePropertyPath()
         parameter = [ vmodl.KeyAnyValue() ]

      class Expression(vmodl.DynamicData):
         id = ""
         displayName = ""
         negated = False

      class ExpressionMetadata(vmodl.DynamicData):
         expressionId = vim.ExtendedElementDescription()
         parameter = [ vim.profile.ParameterMetadata() ]

      class NumericComparator(Enum):
         lessThan = 0
         lessThanEqual = 1
         equal = 2
         notEqual = 3
         greaterThanEqual = 4
         greaterThan = 5

      class ParameterMetadata(vmodl.DynamicData):
         id = vim.ExtendedElementDescription()
         type = vmodl.TypeName()
         optional = False
         defaultValue = anyType()
         hidden = False
         securitySensitive = False
         readOnly = False
         parameterRelations = [ vim.profile.ParameterMetadata.ParameterRelationMetadata() ]

         class RelationType(Enum):
            dynamic_relation = 0
            extensible_relation = 1
            localizable_relation = 2
            static_relation = 3
            validation_relation = 4

         class ParameterRelationMetadata(vmodl.DynamicData):
            relationTypes = [ "" ]
            values = [ anyType() ]
            path = vim.profile.ProfilePropertyPath()
            minCount = 0
            maxCount = 0

      class Policy(vmodl.DynamicData):
         id = ""
         policyOption = vim.profile.PolicyOption()

      class PolicyMetadata(vmodl.DynamicData):
         id = vim.ExtendedElementDescription()
         possibleOption = [ vim.profile.PolicyOptionMetadata() ]

      class PolicyOption(vmodl.DynamicData):
         id = ""
         parameter = [ vmodl.KeyAnyValue() ]

      class PolicyOptionMetadata(vmodl.DynamicData):
         id = vim.ExtendedElementDescription()
         parameter = [ vim.profile.ParameterMetadata() ]

      class Profile(vmodl.ManagedObject):
         config = vim.profile.Profile.ConfigInfo()
         description = vim.profile.Profile.Description()
         name = ""
         createdTime = vmodl.DateTime()
         modifiedTime = vmodl.DateTime()
         entity = [ vim.ManagedEntity() ]
         complianceStatus = ""

         def retrieveDescription():
            return vim.profile.Profile.Description()

         def destroy():
            return None

         def associateEntities(entity=[ vim.ManagedEntity() ]):
            return None

         def dissociateEntities(entity=[ vim.ManagedEntity() ] or None):
            return None

         def checkCompliance(entity=[ vim.ManagedEntity() ] or None):
            return vim.Task()

         def exportProfile():
            return ""

         class CreateSpec(vmodl.DynamicData):
            name = ""
            annotation = ""
            enabled = False

         class SerializedCreateSpec(vim.profile.Profile.CreateSpec):
            profileConfigString = ""

         class ConfigInfo(vmodl.DynamicData):
            name = ""
            annotation = ""
            enabled = False

         class Description(vmodl.DynamicData):
            section = [ vim.profile.Profile.Description.Section() ]

            class Section(vmodl.DynamicData):
               description = vim.ExtendedElementDescription()
               message = [ vmodl.LocalizableMessage() ]

      class ProfileManager(vmodl.ManagedObject):
         profile = [ vim.profile.Profile() ]

         def createProfile(createSpec=vim.profile.Profile.CreateSpec()):
            # throws vim.fault.DuplicateName
            return vim.profile.Profile()

         def queryPolicyMetadata(policyName=[ "" ] or None, profile=vim.profile.Profile() or None):
            return [ vim.profile.PolicyMetadata() ]

         def findAssociatedProfile(entity=vim.ManagedEntity()):
            return [ vim.profile.Profile() ]

      class ProfileMetadata(vmodl.DynamicData):
         key = vmodl.TypeName()
         profileTypeName = ""
         description = vim.ExtendedDescription()
         sortSpec = [ vim.profile.ProfileMetadata.ProfileSortSpec() ]
         profileCategory = ""
         profileComponent = ""
         operationMessages = [ vim.profile.ProfileMetadata.ProfileOperationMessage() ]

         class ProfileSortSpec(vmodl.DynamicData):
            policyId = ""
            parameter = ""

         class ProfileOperationMessage(vmodl.DynamicData):
            operationName = ""
            message = vmodl.LocalizableMessage()

      class ProfilePropertyPath(vmodl.DynamicData):
         profilePath = vmodl.PropertyPath()
         policyId = ""
         parameterId = ""
         policyOptionId = ""

      class ProfileStructure(vmodl.DynamicData):
         profileTypeName = ""
         child = [ vim.profile.ProfileStructureProperty() ]

      class ProfileStructureProperty(vmodl.DynamicData):
         propertyName = ""
         array = False
         element = vim.profile.ProfileStructure()

      class SimpleExpression(vim.profile.Expression):
         expressionType = ""
         parameter = [ vmodl.KeyAnyValue() ]

      class UserInputRequiredParameterMetadata(vim.profile.PolicyOptionMetadata):
         userInputParameter = [ vim.profile.ParameterMetadata() ]

      class cluster(object):

         class ClusterProfile(vim.profile.Profile):

            def update(config=vim.profile.cluster.ClusterProfile.ConfigSpec()):
               # throws vim.fault.DuplicateName
               return None

            class ConfigInfo(vim.profile.Profile.ConfigInfo):
               complyProfile = vim.profile.ComplianceProfile()

            class CreateSpec(vim.profile.Profile.CreateSpec):
               pass

            class ConfigSpec(vim.profile.cluster.ClusterProfile.CreateSpec):
               pass

            class CompleteConfigSpec(vim.profile.cluster.ClusterProfile.ConfigSpec):
               complyProfile = vim.profile.ComplianceProfile()

            class ServiceType(Enum):
               DRS = 0
               HA = 1
               DPM = 2
               FT = 3

            class ConfigServiceCreateSpec(vim.profile.cluster.ClusterProfile.ConfigSpec):
               serviceType = [ "" ]

         class ProfileManager(vim.profile.ProfileManager):
            pass

      class host(object):

         class ActiveDirectoryProfile(vim.profile.ApplyProfile):
            pass

         class AnswerFile(vmodl.DynamicData):
            userInput = [ vim.profile.DeferredPolicyOptionParameter() ]
            createdTime = vmodl.DateTime()
            modifiedTime = vmodl.DateTime()

         class AnswerFileStatusResult(vmodl.DynamicData):
            checkedTime = vmodl.DateTime()
            host = vim.HostSystem()
            status = ""
            error = [ vim.profile.host.AnswerFileStatusResult.AnswerFileStatusError() ]

            class AnswerFileStatusError(vmodl.DynamicData):
               userInputPath = vim.profile.ProfilePropertyPath()
               errMsg = vmodl.LocalizableMessage()

         class AuthenticationProfile(vim.profile.ApplyProfile):
            activeDirectory = vim.profile.host.ActiveDirectoryProfile()

         class DateTimeProfile(vim.profile.ApplyProfile):
            pass

         class DvsProfile(vim.profile.ApplyProfile):
            key = ""
            name = ""
            uplink = [ vim.profile.host.PnicUplinkProfile() ]

         class DvsVNicProfile(vim.profile.ApplyProfile):
            key = ""
            ipConfig = vim.profile.host.IpAddressProfile()

         class ExecuteResult(vmodl.DynamicData):
            status = ""
            configSpec = vim.host.ConfigSpec()
            inapplicablePath = [ vmodl.PropertyPath() ]
            requireInput = [ vim.profile.DeferredPolicyOptionParameter() ]
            error = [ vim.profile.host.ExecuteResult.ExecuteError() ]

            class Status(Enum):
               success = 0
               needInput = 1
               error = 2

            class ExecuteError(vmodl.DynamicData):
               path = vim.profile.ProfilePropertyPath()
               message = vmodl.LocalizableMessage()

         class FirewallProfile(vim.profile.ApplyProfile):
            ruleset = [ vim.profile.host.FirewallProfile.RulesetProfile() ]

            class RulesetProfile(vim.profile.ApplyProfile):
               key = ""

         class HostApplyProfile(vim.profile.ApplyProfile):
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

         class HostMemoryProfile(vim.profile.ApplyProfile):
            pass

         class HostSpecification(vmodl.DynamicData):
            createdTime = vmodl.DateTime()
            lastModified = vmodl.DateTime()
            host = vim.HostSystem()
            subSpecs = [ vim.profile.host.HostSubSpecification() ]
            changeID = ""

         class HostSpecificationManager(vmodl.ManagedObject):

            def updateHostSpecification(host=vim.HostSystem(), hostSpec=vim.profile.host.HostSpecification()):
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def updateHostSubSpecification(host=vim.HostSystem(), hostSubSpec=vim.profile.host.HostSubSpecification()):
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def retrieveHostSpecification(host=vim.HostSystem(), fromHost=False):
               # throws vim.fault.HostSpecificationOperationFailed
               return vim.profile.host.HostSpecification()

            def deleteHostSubSpecification(host=vim.HostSystem(), subSpecName=""):
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def deleteHostSpecification(host=vim.HostSystem()):
               # throws vim.fault.HostSpecificationOperationFailed
               return None

            def getUpdatedHosts(startChangeID="" or None, endChangeID="" or None):
               return [ vim.HostSystem() ]

         class HostSubSpecification(vmodl.DynamicData):
            name = ""
            createdTime = vmodl.DateTime()
            data = [ 0x00 ]
            binaryData = vmodl.Binary()

         class IpAddressProfile(vim.profile.ApplyProfile):
            pass

         class IpRouteProfile(vim.profile.ApplyProfile):
            staticRoute = [ vim.profile.host.StaticRouteProfile() ]

         class NasStorageProfile(vim.profile.ApplyProfile):
            key = ""

         class NetworkPolicyProfile(vim.profile.ApplyProfile):
            pass

         class NetworkProfile(vim.profile.ApplyProfile):
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

            class DnsConfigProfile(vim.profile.ApplyProfile):
               pass

         class NsxHostVNicProfile(vim.profile.ApplyProfile):
            key = ""
            ipConfig = vim.profile.host.IpAddressProfile()

         class OpaqueSwitchProfile(vim.profile.ApplyProfile):
            pass

         class OptionProfile(vim.profile.ApplyProfile):
            key = ""

         class PermissionProfile(vim.profile.ApplyProfile):
            key = ""

         class PhysicalNicProfile(vim.profile.ApplyProfile):
            key = ""

         class PnicUplinkProfile(vim.profile.ApplyProfile):
            key = ""

         class PortGroupProfile(vim.profile.ApplyProfile):
            key = ""
            name = ""
            vlan = vim.profile.host.PortGroupProfile.VlanProfile()
            vswitch = vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile()
            networkPolicy = vim.profile.host.NetworkPolicyProfile()

            class VlanProfile(vim.profile.ApplyProfile):
               pass

            class VirtualSwitchSelectionProfile(vim.profile.ApplyProfile):
               pass

         class SecurityProfile(vim.profile.ApplyProfile):
            permission = [ vim.profile.host.PermissionProfile() ]

         class ServiceConsolePortGroupProfile(vim.profile.host.PortGroupProfile):
            ipConfig = vim.profile.host.IpAddressProfile()

         class ServiceProfile(vim.profile.ApplyProfile):
            key = ""

         class StaticRouteProfile(vim.profile.ApplyProfile):
            key = ""

         class StorageProfile(vim.profile.ApplyProfile):
            nasStorage = [ vim.profile.host.NasStorageProfile() ]

         class UserGroupProfile(vim.profile.ApplyProfile):
            key = ""

         class UserProfile(vim.profile.ApplyProfile):
            key = ""

         class VirtualSwitchProfile(vim.profile.ApplyProfile):
            key = ""
            name = ""
            link = vim.profile.host.VirtualSwitchProfile.LinkProfile()
            numPorts = vim.profile.host.VirtualSwitchProfile.NumPortsProfile()
            networkPolicy = vim.profile.host.NetworkPolicyProfile()

            class LinkProfile(vim.profile.ApplyProfile):
               pass

            class NumPortsProfile(vim.profile.ApplyProfile):
               pass

         class VmPortGroupProfile(vim.profile.host.PortGroupProfile):
            pass

         class profileEngine(object):

            class AnswerFileValidationInfo(object):

               class Status(Enum):
                  success = 0
                  failed = 1
                  failed_defaults = 2

         class DvsHostVNicProfile(vim.profile.host.DvsVNicProfile):
            pass

         class DvsServiceConsoleVNicProfile(vim.profile.host.DvsVNicProfile):
            pass

         class HostPortGroupProfile(vim.profile.host.PortGroupProfile):
            ipConfig = vim.profile.host.IpAddressProfile()

         class HostProfile(vim.profile.Profile):
            validationState = ""
            validationStateUpdateTime = vmodl.DateTime()
            validationFailureInfo = vim.profile.host.HostProfile.ValidationFailureInfo()
            referenceHost = vim.HostSystem()

            def ResetValidationState():
               return None

            def updateReferenceHost(host=vim.HostSystem() or None):
               return None

            def update(config=vim.profile.host.HostProfile.ConfigSpec()):
               # throws vim.fault.DuplicateName, vim.fault.ProfileUpdateFailed
               return None

            def execute(host=vim.HostSystem(), deferredParam=[ vim.profile.DeferredPolicyOptionParameter() ] or None):
               return vim.profile.host.ExecuteResult()

            class ConfigInfo(vim.profile.Profile.ConfigInfo):
               applyProfile = vim.profile.host.HostApplyProfile()
               defaultComplyProfile = vim.profile.ComplianceProfile()
               defaultComplyLocator = [ vim.profile.ComplianceLocator() ]
               customComplyProfile = vim.profile.ComplianceProfile()
               disabledExpressionList = [ "" ]
               description = vim.profile.Profile.Description()

            class ConfigSpec(vim.profile.Profile.CreateSpec):
               pass

            class SerializedHostProfileSpec(vim.profile.Profile.SerializedCreateSpec):
               validatorHost = vim.HostSystem()
               validating = False

            class CompleteConfigSpec(vim.profile.host.HostProfile.ConfigSpec):
               applyProfile = vim.profile.host.HostApplyProfile()
               customComplyProfile = vim.profile.ComplianceProfile()
               disabledExpressionListChanged = False
               disabledExpressionList = [ "" ]
               validatorHost = vim.HostSystem()
               validating = False
               hostConfig = vim.profile.host.HostProfile.ConfigInfo()

            class HostBasedConfigSpec(vim.profile.host.HostProfile.ConfigSpec):
               host = vim.HostSystem()
               useHostProfileEngine = False

            class ValidationState(Enum):
               Ready = 0
               Running = 1
               Failed = 2

            class ValidationFailureInfo(vmodl.DynamicData):
               name = ""
               annotation = ""
               updateType = ""
               host = vim.HostSystem()
               applyProfile = vim.profile.host.HostApplyProfile()
               failures = [ vim.fault.ProfileUpdateFailed.UpdateFailure() ]
               faults = [ vmodl.MethodFault() ]

               class UpdateType(Enum):
                  HostBased = 0
                  Import = 1
                  Edit = 2
                  Compose = 3

         class NetStackInstanceProfile(vim.profile.ApplyProfile):
            key = ""
            dnsConfig = vim.profile.host.NetworkProfile.DnsConfigProfile()
            ipRouteConfig = vim.profile.host.IpRouteProfile()

         class ProfileManager(vim.profile.ProfileManager):

            def applyHostConfiguration(host=vim.HostSystem(), configSpec=vim.host.ConfigSpec(), userInput=[ vim.profile.DeferredPolicyOptionParameter() ] or None):
               # throws vim.fault.InvalidState, vim.fault.HostConfigFailed
               return vim.Task()

            def generateConfigTaskList(configSpec=vim.host.ConfigSpec(), host=vim.HostSystem()):
               return vim.profile.host.ProfileManager.ConfigTaskList()

            def generateTaskList(configSpec=vim.host.ConfigSpec(), host=vim.HostSystem()):
               return vim.Task()

            def queryProfileMetadata(profileName=[ vmodl.TypeName() ] or None, profile=vim.profile.Profile() or None):
               return [ vim.profile.ProfileMetadata() ]

            def queryProfileStructure(profile=vim.profile.Profile() or None):
               return vim.profile.ProfileStructure()

            def createDefaultProfile(profileType=vmodl.TypeName(), profileTypeName="" or None, profile=vim.profile.Profile() or None):
               return vim.profile.ApplyProfile()

            def updateAnswerFile(host=vim.HostSystem(), configSpec=vim.profile.host.ProfileManager.AnswerFileCreateSpec()):
               # throws vim.fault.AnswerFileUpdateFailed
               return vim.Task()

            def retrieveAnswerFile(host=vim.HostSystem()):
               return vim.profile.host.AnswerFile()

            def retrieveAnswerFileForProfile(host=vim.HostSystem(), applyProfile=vim.profile.host.HostApplyProfile()):
               return vim.profile.host.AnswerFile()

            def exportAnswerFile(host=vim.HostSystem()):
               return vim.Task()

            def checkAnswerFileStatus(host=[ vim.HostSystem() ]):
               return vim.Task()

            def queryAnswerFileStatus(host=[ vim.HostSystem() ]):
               return [ vim.profile.host.AnswerFileStatusResult() ]

            def updateHostCustomizations(hostToConfigSpecMap=[ vim.profile.host.ProfileManager.HostToConfigSpecMap() ] or None):
               return vim.Task()

            def retrieveHostCustomizations(hosts=[ vim.HostSystem() ] or None):
               return [ vim.profile.host.ProfileManager.StructuredCustomizations() ]

            def retrieveHostCustomizationsForProfile(hosts=[ vim.HostSystem() ] or None, applyProfile=vim.profile.host.HostApplyProfile()):
               return [ vim.profile.host.ProfileManager.StructuredCustomizations() ]

            def generateHostConfigTaskSpec(hostsInfo=[ vim.profile.host.ProfileManager.StructuredCustomizations() ] or None):
               return vim.Task()

            def applyEntitiesConfiguration(applyConfigSpecs=[ vim.profile.host.ProfileManager.ApplyHostConfigSpec() ] or None):
               return vim.Task()

            def validateComposition(source=vim.profile.Profile(), targets=[ vim.profile.Profile() ] or None, toBeMerged=vim.profile.host.HostApplyProfile() or None, toReplaceWith=vim.profile.host.HostApplyProfile() or None, toBeDeleted=vim.profile.host.HostApplyProfile() or None, enableStatusToBeCopied=vim.profile.host.HostApplyProfile() or None, errorOnly=False or None):
               return vim.Task()

            def compositeProfile(source=vim.profile.Profile(), targets=[ vim.profile.Profile() ] or None, toBeMerged=vim.profile.host.HostApplyProfile() or None, toBeReplacedWith=vim.profile.host.HostApplyProfile() or None, toBeDeleted=vim.profile.host.HostApplyProfile() or None, enableStatusToBeCopied=vim.profile.host.HostApplyProfile() or None):
               return vim.Task()

            class TaskListRequirement(Enum):
               maintenanceModeRequired = 0
               rebootRequired = 1

            class ConfigTaskList(vmodl.DynamicData):
               configSpec = vim.host.ConfigSpec()
               taskDescription = [ vmodl.LocalizableMessage() ]
               taskListRequirement = [ "" ]

            class AnswerFileCreateSpec(vmodl.DynamicData):
               validating = False

            class AnswerFileOptionsCreateSpec(vim.profile.host.ProfileManager.AnswerFileCreateSpec):
               userInput = [ vim.profile.DeferredPolicyOptionParameter() ]

            class AnswerFileSerializedCreateSpec(vim.profile.host.ProfileManager.AnswerFileCreateSpec):
               answerFileConfigString = ""

            class AnswerFileStatus(Enum):
               valid = 0
               invalid = 1
               unknown = 2

            class EntityCustomizations(vmodl.DynamicData):
               pass

            class StructuredCustomizations(vim.profile.host.ProfileManager.EntityCustomizations):
               entity = vim.ManagedEntity()
               customizations = vim.profile.host.AnswerFile()

            class HostToConfigSpecMap(vmodl.DynamicData):
               host = vim.HostSystem()
               configSpec = vim.profile.host.ProfileManager.AnswerFileCreateSpec()

            class ApplyHostConfigSpec(vim.profile.host.ExecuteResult):
               host = vim.HostSystem()
               taskListRequirement = [ "" ]
               taskDescription = [ vmodl.LocalizableMessage() ]
               rebootStateless = False
               rebootHost = False
               faultData = vmodl.MethodFault()

            class ApplyHostConfigResult(vmodl.DynamicData):
               startTime = vmodl.DateTime()
               completeTime = vmodl.DateTime()
               host = vim.HostSystem()
               status = ""
               errors = [ vmodl.MethodFault() ]

               class Status(Enum):
                  success = 0
                  failed = 1
                  reboot_failed = 2
                  stateless_reboot_failed = 3
                  check_compliance_failed = 4
                  state_not_satisfied = 5
                  exit_maintenancemode_failed = 6
                  canceled = 7

            class CompositionValidationResult(vmodl.DynamicData):
               results = [ vim.profile.host.ProfileManager.CompositionValidationResult.ResultElement() ]
               errors = [ vmodl.LocalizableMessage() ]

               class ResultElement(vmodl.DynamicData):
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

                  class Status(Enum):
                     success = 0
                     error = 1

            class CompositionResult(vmodl.DynamicData):
               errors = [ vmodl.LocalizableMessage() ]
               results = [ vim.profile.host.ProfileManager.CompositionResult.ResultElement() ]

               class ResultElement(vmodl.DynamicData):
                  target = vim.profile.Profile()
                  status = ""
                  errors = [ vmodl.LocalizableMessage() ]

                  class Status(Enum):
                     success = 0
                     error = 1

      class CompositeExpression(vim.profile.Expression):
         operator = ""
         expressionName = [ "" ]

      class CompositePolicyOption(vim.profile.PolicyOption):
         option = [ vim.profile.PolicyOption() ]

      class CompositePolicyOptionMetadata(vim.profile.PolicyOptionMetadata):
         option = [ "" ]

   class scheduler(object):

      class ScheduledTask(vim.ExtensibleManagedObject):
         info = vim.scheduler.ScheduledTaskInfo()

         def remove():
            # throws vim.fault.InvalidState
            return None

         def reconfigure(spec=vim.scheduler.ScheduledTaskSpec()):
            # throws vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.DuplicateName
            return None

         def run():
            # throws vim.fault.InvalidState
            return None

      class ScheduledTaskDescription(vmodl.DynamicData):
         action = [ vim.TypeDescription() ]
         schedulerInfo = [ vim.scheduler.ScheduledTaskDescription.SchedulerDetail() ]
         state = [ vim.ElementDescription() ]
         dayOfWeek = [ vim.ElementDescription() ]
         weekOfMonth = [ vim.ElementDescription() ]

         class SchedulerDetail(vim.TypeDescription):
            frequency = ""

      class ScheduledTaskManager(vmodl.ManagedObject):
         scheduledTask = [ vim.scheduler.ScheduledTask() ]
         description = vim.scheduler.ScheduledTaskDescription()

         def create(entity=vim.ManagedEntity(), spec=vim.scheduler.ScheduledTaskSpec()):
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.scheduler.ScheduledTask()

         def retrieveEntityScheduledTask(entity=vim.ManagedEntity() or None):
            return [ vim.scheduler.ScheduledTask() ]

         def createObjectScheduledTask(obj=vmodl.ManagedObject(), spec=vim.scheduler.ScheduledTaskSpec()):
            # throws vim.fault.InvalidName, vim.fault.DuplicateName
            return vim.scheduler.ScheduledTask()

         def retrieveObjectScheduledTask(obj=vmodl.ManagedObject() or None):
            return [ vim.scheduler.ScheduledTask() ]

      class ScheduledTaskSpec(vmodl.DynamicData):
         name = ""
         description = ""
         enabled = False
         scheduler = vim.scheduler.TaskScheduler()
         action = vim.action.Action()
         notification = ""

      class TaskScheduler(vmodl.DynamicData):
         activeTime = vmodl.DateTime()
         expireTime = vmodl.DateTime()

      class AfterStartupTaskScheduler(vim.scheduler.TaskScheduler):
         minute = 0

      class OnceTaskScheduler(vim.scheduler.TaskScheduler):
         runAt = vmodl.DateTime()

      class RecurrentTaskScheduler(vim.scheduler.TaskScheduler):
         interval = 0

      class ScheduledTaskInfo(vim.scheduler.ScheduledTaskSpec):
         scheduledTask = vim.scheduler.ScheduledTask()
         entity = vim.ManagedEntity()
         lastModifiedTime = vmodl.DateTime()
         lastModifiedUser = ""
         nextRunTime = vmodl.DateTime()
         prevRunTime = vmodl.DateTime()
         state = vim.TaskInfo.State()
         error = vmodl.MethodFault()
         result = anyType()
         progress = 0
         activeTask = vim.Task()
         taskObject = vmodl.ManagedObject()

      class HourlyTaskScheduler(vim.scheduler.RecurrentTaskScheduler):
         minute = 0

      class DailyTaskScheduler(vim.scheduler.HourlyTaskScheduler):
         hour = 0

      class MonthlyTaskScheduler(vim.scheduler.DailyTaskScheduler):
         pass

      class WeeklyTaskScheduler(vim.scheduler.DailyTaskScheduler):
         sunday = False
         monday = False
         tuesday = False
         wednesday = False
         thursday = False
         friday = False
         saturday = False

      class MonthlyByDayTaskScheduler(vim.scheduler.MonthlyTaskScheduler):
         day = 0

      class MonthlyByWeekdayTaskScheduler(vim.scheduler.MonthlyTaskScheduler):
         offset = vim.scheduler.MonthlyByWeekdayTaskScheduler.WeekOfMonth()
         weekday = vim.scheduler.MonthlyByWeekdayTaskScheduler.DayOfWeek()

         class DayOfWeek(Enum):
            sunday = 0
            monday = 1
            tuesday = 2
            wednesday = 3
            thursday = 4
            friday = 5
            saturday = 6

         class WeekOfMonth(Enum):
            first = 0
            second = 1
            third = 2
            fourth = 3
            last = 4

   class storageDrs(object):

      class ApplyRecommendationResult(vmodl.DynamicData):
         vm = vim.VirtualMachine()

      class AutomationConfig(vmodl.DynamicData):
         spaceLoadBalanceAutomationMode = ""
         ioLoadBalanceAutomationMode = ""
         ruleEnforcementAutomationMode = ""
         policyEnforcementAutomationMode = ""
         vmEvacuationAutomationMode = ""

      class ConfigInfo(vmodl.DynamicData):
         podConfig = vim.storageDrs.PodConfigInfo()
         vmConfig = [ vim.storageDrs.VmConfigInfo() ]

      class ConfigSpec(vmodl.DynamicData):
         podConfigSpec = vim.storageDrs.PodConfigSpec()
         vmConfigSpec = [ vim.storageDrs.VmConfigSpec() ]

      class HbrDiskMigrationAction(vim.cluster.Action):
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

      class IoLoadBalanceConfig(vmodl.DynamicData):
         reservablePercentThreshold = 0
         reservableIopsThreshold = 0
         reservableThresholdMode = ""
         ioLatencyThreshold = 0
         ioLoadImbalanceThreshold = 0

      class OptionSpec(vim.option.ArrayUpdateSpec):
         option = vim.option.OptionValue()

      class PlacementAffinityRule(vmodl.DynamicData):
         ruleType = ""
         ruleScope = ""
         vms = [ vim.VirtualMachine() ]
         keys = [ "" ]

         class RuleType(Enum):
            affinity = 0
            antiAffinity = 1
            softAffinity = 2
            softAntiAffinity = 3

         class RuleScope(Enum):
            cluster = 0
            host = 1
            storagePod = 2
            datastore = 3

      class PlacementRankResult(vmodl.DynamicData):
         key = ""
         candidate = vim.ClusterComputeResource()
         reservedSpaceMB = 0
         usedSpaceMB = 0
         totalSpaceMB = 0
         utilization = 0.0
         faults = [ vmodl.MethodFault() ]

      class PlacementRankSpec(vmodl.DynamicData):
         specs = [ vim.cluster.PlacementSpec() ]
         clusters = [ vim.ClusterComputeResource() ]
         rules = [ vim.storageDrs.PlacementAffinityRule() ]
         placementRankByVm = [ vim.storageDrs.PlacementRankVmSpec() ]

      class PlacementRankVmSpec(vmodl.DynamicData):
         vmPlacementSpec = vim.cluster.PlacementSpec()
         vmClusters = [ vim.ClusterComputeResource() ]

      class PodConfigInfo(vmodl.DynamicData):
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

         class Behavior(Enum):
            manual = 0
            automated = 1

      class PodConfigSpec(vmodl.DynamicData):
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

      class SpaceLoadBalanceConfig(vmodl.DynamicData):
         spaceThresholdMode = ""
         spaceUtilizationThreshold = 0
         freeSpaceThresholdGB = 0
         minSpaceUtilizationDifference = 0

         class SpaceThresholdMode(Enum):
            utilization = 0
            freeSpace = 1

      class StorageMigrationAction(vim.cluster.Action):
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

      class StoragePlacementAction(vim.cluster.Action):
         vm = vim.VirtualMachine()
         relocateSpec = vim.vm.RelocateSpec()
         destination = vim.Datastore()
         spaceUtilBefore = 0.0
         spaceDemandBefore = 0.0
         spaceUtilAfter = 0.0
         spaceDemandAfter = 0.0
         ioLatencyBefore = 0.0

      class StoragePlacementResult(vmodl.DynamicData):
         recommendations = [ vim.cluster.Recommendation() ]
         drsFault = vim.cluster.DrsFaults()
         task = vim.Task()

      class VmConfigInfo(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         enabled = False
         behavior = ""
         intraVmAffinity = False
         intraVmAntiAffinity = vim.storageDrs.VirtualDiskAntiAffinityRuleSpec()
         virtualDiskRules = [ vim.storageDrs.VirtualDiskRuleSpec() ]

      class VmConfigSpec(vim.option.ArrayUpdateSpec):
         info = vim.storageDrs.VmConfigInfo()

      class PodSelectionSpec(vmodl.DynamicData):
         initialVmConfig = [ vim.storageDrs.PodSelectionSpec.VmPodConfig() ]
         storagePod = vim.StoragePod()

         class VmPodConfig(vmodl.DynamicData):
            storagePod = vim.StoragePod()
            disk = [ vim.storageDrs.PodSelectionSpec.DiskLocator() ]
            vmConfig = vim.storageDrs.VmConfigInfo()
            interVmRule = [ vim.cluster.RuleInfo() ]

         class DiskLocator(vmodl.DynamicData):
            diskId = 0
            diskMoveType = ""
            diskBackingInfo = vim.vm.device.VirtualDevice.BackingInfo()
            profile = [ vim.vm.ProfileSpec() ]

      class StoragePlacementSpec(vmodl.DynamicData):
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

         class PlacementType(Enum):
            create = 0
            reconfigure = 1
            relocate = 2
            clone = 3

      class VirtualDiskAntiAffinityRuleSpec(vim.cluster.RuleInfo):
         diskId = [ 0 ]

      class VirtualDiskRuleSpec(vim.cluster.RuleInfo):
         diskRuleType = ""
         diskId = [ 0 ]

         class RuleType(Enum):
            affinity = 0
            antiAffinity = 1
            disabled = 2

   class tenant(object):

      class TenantManager(vmodl.ManagedObject):

         def markServiceProviderEntities(entity=[ vim.ManagedEntity() ] or None):
            # throws vmodl.fault.ManagedObjectNotFound, vim.fault.AuthMinimumAdminPermission
            return None

         def unmarkServiceProviderEntities(entity=[ vim.ManagedEntity() ] or None):
            # throws vmodl.fault.ManagedObjectNotFound
            return None

         def retrieveServiceProviderEntities():
            return [ vim.ManagedEntity() ]

   class vApp(object):

      class CloneSpec(vmodl.DynamicData):
         location = vim.Datastore()
         host = vim.HostSystem()
         resourceSpec = vim.ResourceConfigSpec()
         vmFolder = vim.Folder()
         networkMapping = [ vim.vApp.CloneSpec.NetworkMappingPair() ]
         property = [ vim.KeyValue() ]
         resourceMapping = [ vim.vApp.CloneSpec.ResourceMap() ]
         provisioning = ""

         class NetworkMappingPair(vmodl.DynamicData):
            source = vim.Network()
            destination = vim.Network()

         class ResourceMap(vmodl.DynamicData):
            source = vim.ManagedEntity()
            parent = vim.ResourcePool()
            resourceSpec = vim.ResourceConfigSpec()
            location = vim.Datastore()

         class ProvisioningType(Enum):
            sameAsSource = 0
            thin = 1
            thick = 2

      class EntityConfigInfo(vmodl.DynamicData):
         key = vim.ManagedEntity()
         tag = ""
         startOrder = 0
         startDelay = 0
         waitingForGuest = False
         startAction = ""
         stopDelay = 0
         stopAction = ""
         destroyWithParent = False

         class Action(Enum):
            none = 0
            powerOn = 1
            powerOff = 2
            guestShutdown = 3
            suspend = 4

      class IPAssignmentInfo(vmodl.DynamicData):
         supportedAllocationScheme = [ "" ]
         ipAllocationPolicy = ""
         supportedIpProtocol = [ "" ]
         ipProtocol = ""

         class IpAllocationPolicy(Enum):
            dhcpPolicy = 0
            transientPolicy = 1
            fixedPolicy = 2
            fixedAllocatedPolicy = 3

         class AllocationSchemes(Enum):
            dhcp = 0
            ovfenv = 1

         class Protocols(Enum):
            IPv4 = 0
            IPv6 = 1

      class IpPool(vmodl.DynamicData):
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

         class IpPoolConfigInfo(vmodl.DynamicData):
            subnetAddress = ""
            netmask = ""
            gateway = ""
            range = ""
            dns = [ "" ]
            dhcpServerAvailable = False
            ipPoolEnabled = False

         class Association(vmodl.DynamicData):
            network = vim.Network()
            networkName = ""

      class OvfSectionInfo(vmodl.DynamicData):
         key = 0
         namespace = ""
         type = ""
         atEnvelopeLevel = False
         contents = ""

      class OvfSectionSpec(vim.option.ArrayUpdateSpec):
         info = vim.vApp.OvfSectionInfo()

      class ProductInfo(vmodl.DynamicData):
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

      class ProductSpec(vim.option.ArrayUpdateSpec):
         info = vim.vApp.ProductInfo()

      class PropertyInfo(vmodl.DynamicData):
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

      class PropertySpec(vim.option.ArrayUpdateSpec):
         info = vim.vApp.PropertyInfo()

      class VmConfigInfo(vmodl.DynamicData):
         product = [ vim.vApp.ProductInfo() ]
         property = [ vim.vApp.PropertyInfo() ]
         ipAssignment = vim.vApp.IPAssignmentInfo()
         eula = [ "" ]
         ovfSection = [ vim.vApp.OvfSectionInfo() ]
         ovfEnvironmentTransport = [ "" ]
         installBootRequired = False
         installBootStopDelay = 0

      class VmConfigSpec(vmodl.DynamicData):
         product = [ vim.vApp.ProductSpec() ]
         property = [ vim.vApp.PropertySpec() ]
         ipAssignment = vim.vApp.IPAssignmentInfo()
         eula = [ "" ]
         ovfSection = [ vim.vApp.OvfSectionSpec() ]
         ovfEnvironmentTransport = [ "" ]
         installBootRequired = False
         installBootStopDelay = 0

      class VAppConfigInfo(vim.vApp.VmConfigInfo):
         entityConfig = [ vim.vApp.EntityConfigInfo() ]
         annotation = ""
         instanceUuid = ""
         managedBy = vim.ext.ManagedByInfo()

      class VAppConfigSpec(vim.vApp.VmConfigSpec):
         entityConfig = [ vim.vApp.EntityConfigInfo() ]
         annotation = ""
         instanceUuid = ""
         managedBy = vim.ext.ManagedByInfo()

      class VAppImportSpec(vim.ImportSpec):
         name = ""
         vAppConfigSpec = vim.vApp.VAppConfigSpec()
         resourcePoolSpec = vim.ResourceConfigSpec()
         child = [ vim.ImportSpec() ]

   class vcha(object):

      class FailoverClusterConfigurator(vmodl.ManagedObject):
         disabledConfigureMethod = [ vmodl.MethodName() ]

         def prepare(networkSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterNetworkSpec()):
            return vim.Task()

         def deploy(deploymentSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterDeploymentSpec()):
            return vim.Task()

         def configure(configSpec=vim.vcha.FailoverClusterConfigurator.VchaClusterConfigSpec()):
            return vim.Task()

         def createPassiveNode(passiveDeploymentSpec=vim.vcha.FailoverClusterConfigurator.PassiveNodeDeploymentSpec(), sourceVcSpec=vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()):
            return vim.Task()

         def createWitnessNode(witnessDeploymentSpec=vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec(), sourceVcSpec=vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()):
            return vim.Task()

         def getConfig():
            return vim.vcha.FailoverClusterConfigurator.VchaClusterConfigInfo()

         def destroy():
            return vim.Task()

         class ClusterNetworkConfigSpec(vmodl.DynamicData):
            networkPortGroup = vim.Network()
            ipSettings = vim.vm.customization.IPSettings()

         class SourceNodeSpec(vmodl.DynamicData):
            managementVc = vim.ServiceLocator()
            activeVc = vim.VirtualMachine()

         class NodeNetworkSpec(vmodl.DynamicData):
            ipSettings = vim.vm.customization.IPSettings()

         class PassiveNodeNetworkSpec(vim.vcha.FailoverClusterConfigurator.NodeNetworkSpec):
            failoverIpSettings = vim.vm.customization.IPSettings()

         class VchaClusterNetworkSpec(vmodl.DynamicData):
            witnessNetworkSpec = vim.vcha.FailoverClusterConfigurator.NodeNetworkSpec()
            passiveNetworkSpec = vim.vcha.FailoverClusterConfigurator.PassiveNodeNetworkSpec()

         class NodeDeploymentSpec(vmodl.DynamicData):
            esxHost = vim.HostSystem()
            datastore = vim.Datastore()
            publicNetworkPortGroup = vim.Network()
            clusterNetworkPortGroup = vim.Network()
            folder = vim.Folder()
            resourcePool = vim.ResourcePool()
            managementVc = vim.ServiceLocator()
            nodeName = ""
            ipSettings = vim.vm.customization.IPSettings()

         class PassiveNodeDeploymentSpec(vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec):
            failoverIpSettings = vim.vm.customization.IPSettings()

         class VchaClusterConfigSpec(vmodl.DynamicData):
            passiveIp = ""
            witnessIp = ""

         class VchaClusterDeploymentSpec(vmodl.DynamicData):
            passiveDeploymentSpec = vim.vcha.FailoverClusterConfigurator.PassiveNodeDeploymentSpec()
            witnessDeploymentSpec = vim.vcha.FailoverClusterConfigurator.NodeDeploymentSpec()
            activeVcSpec = vim.vcha.FailoverClusterConfigurator.SourceNodeSpec()
            activeVcNetworkConfig = vim.vcha.FailoverClusterConfigurator.ClusterNetworkConfigSpec()

         class FailoverNodeInfo(vmodl.DynamicData):
            clusterIpSettings = vim.vm.customization.IPSettings()
            failoverIp = vim.vm.customization.IPSettings()
            biosUuid = ""

         class WitnessNodeInfo(vmodl.DynamicData):
            ipSettings = vim.vm.customization.IPSettings()
            biosUuid = ""

         class VchaState(Enum):
            configured = 0
            notConfigured = 1
            invalid = 2
            prepared = 3

         class VchaClusterConfigInfo(vmodl.DynamicData):
            failoverNodeInfo1 = vim.vcha.FailoverClusterConfigurator.FailoverNodeInfo()
            failoverNodeInfo2 = vim.vcha.FailoverClusterConfigurator.FailoverNodeInfo()
            witnessNodeInfo = vim.vcha.FailoverClusterConfigurator.WitnessNodeInfo()
            state = ""

      class FailoverClusterManager(vmodl.ManagedObject):
         disabledClusterMethod = [ vmodl.MethodName() ]

         def setClusterMode(mode=""):
            return vim.Task()

         def getClusterMode():
            return ""

         def getClusterHealth():
            return vim.vcha.FailoverClusterManager.VchaClusterHealth()

         def initiateFailover(planned=False):
            return vim.Task()

         class VchaNodeRole(Enum):
            active = 0
            passive = 1
            witness = 2

         class VchaClusterMode(Enum):
            enabled = 0
            disabled = 1
            maintenance = 2

         class VchaClusterState(Enum):
            healthy = 0
            degraded = 1
            isolated = 2

         class VchaNodeState(Enum):
            up = 0
            down = 1

         class VchaNodeRuntimeInfo(vmodl.DynamicData):
            nodeState = ""
            nodeRole = ""
            nodeIp = ""

         class VchaClusterRuntimeInfo(vmodl.DynamicData):
            clusterState = ""
            nodeInfo = [ vim.vcha.FailoverClusterManager.VchaNodeRuntimeInfo() ]
            clusterMode = ""

         class VchaClusterHealth(vmodl.DynamicData):
            runtimeInfo = vim.vcha.FailoverClusterManager.VchaClusterRuntimeInfo()
            healthMessages = [ vmodl.LocalizableMessage() ]
            additionalInformation = [ vmodl.LocalizableMessage() ]

   class view(object):

      class View(vmodl.ManagedObject):

         def destroy():
            return None

      class ViewManager(vmodl.ManagedObject):
         viewList = [ vim.view.View() ]

         def createInventoryView():
            return vim.view.InventoryView()

         def createContainerView(container=vim.ManagedEntity(), type=[ vmodl.TypeName() ] or None, recursive=False):
            return vim.view.ContainerView()

         def createListView(obj=[ vmodl.ManagedObject() ] or None):
            return vim.view.ListView()

         def createListViewFromView(view=vim.view.View()):
            return vim.view.ListView()

      class ManagedObjectView(vim.view.View):
         view = [ vmodl.ManagedObject() ]

      class ContainerView(vim.view.ManagedObjectView):
         container = vim.ManagedEntity()
         type = [ vmodl.TypeName() ]
         recursive = False

      class InventoryView(vim.view.ManagedObjectView):

         def openFolder(entity=[ vim.ManagedEntity() ]):
            return [ vim.ManagedEntity() ]

         def closeFolder(entity=[ vim.ManagedEntity() ]):
            return [ vim.ManagedEntity() ]

      class ListView(vim.view.ManagedObjectView):

         def modify(add=[ vmodl.ManagedObject() ] or None, remove=[ vmodl.ManagedObject() ] or None):
            return [ vmodl.ManagedObject() ]

         def reset(obj=[ vmodl.ManagedObject() ] or None):
            return [ vmodl.ManagedObject() ]

         def resetFromView(view=vim.view.View()):
            return None

   class vm(object):

      class AffinityInfo(vmodl.DynamicData):
         affinitySet = [ 0 ]

      class BootOptions(vmodl.DynamicData):
         bootDelay = 0
         enterBIOSSetup = False
         efiSecureBootEnabled = False
         bootRetryEnabled = False
         bootRetryDelay = 0
         bootOrder = [ vim.vm.BootOptions.BootableDevice() ]
         networkBootProtocol = ""

         class NetworkBootProtocolType(Enum):
            ipv4 = 0
            ipv6 = 1

         class BootableDevice(vmodl.DynamicData):
            pass

         class BootableDiskDevice(vim.vm.BootOptions.BootableDevice):
            deviceKey = 0

         class BootableEthernetDevice(vim.vm.BootOptions.BootableDevice):
            deviceKey = 0

         class BootableFloppyDevice(vim.vm.BootOptions.BootableDevice):
            pass

         class BootableCdromDevice(vim.vm.BootOptions.BootableDevice):
            pass

      class Capability(vmodl.DynamicData):
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

      class CloneSpec(vmodl.DynamicData):
         location = vim.vm.RelocateSpec()
         template = False
         config = vim.vm.ConfigSpec()
         customization = vim.vm.customization.Specification()
         powerOn = False
         snapshot = vim.vm.Snapshot()
         memory = False

      class ConfigInfo(vmodl.DynamicData):
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

         class NpivWwnType(Enum):
            vc = 0
            host = 1
            external = 2

         class SwapPlacementType(Enum):
            inherit = 0
            vmDirectory = 1
            hostLocal = 2

         class DatastoreUrlPair(vmodl.DynamicData):
            name = ""
            url = ""

         class OverheadInfo(vmodl.DynamicData):
            initialMemoryReservation = 0
            initialSwapReservation = 0

      class ConfigOption(vmodl.DynamicData):
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

      class ConfigOptionDescriptor(vmodl.DynamicData):
         key = ""
         description = ""
         host = [ vim.HostSystem() ]
         createSupported = False
         defaultConfigOption = False
         runSupported = False
         upgradeSupported = False

      class ConfigSpec(vmodl.DynamicData):
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

         class NpivWwnOp(Enum):
            generate = 0
            set = 1
            remove = 2
            extend = 3

         class EncryptedVMotionModes(Enum):
            disabled = 0
            opportunistic = 1
            required = 2

         class CpuIdInfoSpec(vim.option.ArrayUpdateSpec):
            info = vim.host.CpuIdInfo()

      class ConsolePreferences(vmodl.DynamicData):
         powerOnWhenOpened = False
         enterFullScreenOnPowerOn = False
         closeOnPowerOffOrSuspend = False

      class ContentLibraryItemInfo(vmodl.DynamicData):
         contentLibraryItemUuid = ""
         contentLibraryItemVersion = ""

      class DatastoreOption(vmodl.DynamicData):
         unsupportedVolumes = [ vim.vm.DatastoreOption.FileSystemVolumeOption() ]

         class FileSystemVolumeOption(vmodl.DynamicData):
            fileSystemType = vmodl.TypeName()
            majorVersion = 0

      class DefaultPowerOpInfo(vmodl.DynamicData):
         powerOffType = ""
         suspendType = ""
         resetType = ""
         defaultPowerOffType = ""
         defaultSuspendType = ""
         defaultResetType = ""
         standbyAction = ""

         class PowerOpType(Enum):
            soft = 0
            hard = 1
            preset = 2

         class StandbyActionType(Enum):
            checkpoint = 0
            powerOnSuspend = 1

      class DeviceRuntimeInfo(vmodl.DynamicData):
         runtimeState = vim.vm.DeviceRuntimeInfo.DeviceRuntimeState()
         key = 0

         class DeviceRuntimeState(vmodl.DynamicData):
            pass

         class VirtualEthernetCardRuntimeState(vim.vm.DeviceRuntimeInfo.DeviceRuntimeState):
            vmDirectPathGen2Active = False
            vmDirectPathGen2InactiveReasonVm = [ "" ]
            vmDirectPathGen2InactiveReasonOther = [ "" ]
            vmDirectPathGen2InactiveReasonExtended = ""
            reservationStatus = ""
            attachmentStatus = ""
            featureRequirement = [ vim.vm.FeatureRequirement() ]

            class VmDirectPathGen2InactiveReasonVm(Enum):
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

            class VmDirectPathGen2InactiveReasonOther(Enum):
               vmNptIncompatibleHost = 0
               vmNptIncompatibleNetwork = 1

      class FaultToleranceConfigInfo(vmodl.DynamicData):
         role = 0
         instanceUuids = [ "" ]
         configPaths = [ "" ]
         orphaned = False

      class FaultToleranceConfigSpec(vmodl.DynamicData):
         metaDataPath = vim.vm.FaultToleranceMetaSpec()
         secondaryVmSpec = vim.vm.FaultToleranceVMConfigSpec()

      class FaultToleranceMetaSpec(vmodl.DynamicData):
         metaDataDatastore = vim.Datastore()

      class FaultTolerancePrimaryConfigInfo(vim.vm.FaultToleranceConfigInfo):
         secondaries = [ vim.VirtualMachine() ]

      class FaultToleranceSecondaryConfigInfo(vim.vm.FaultToleranceConfigInfo):
         primaryVM = vim.VirtualMachine()

      class FaultToleranceSecondaryOpResult(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         powerOnAttempted = False
         powerOnResult = vim.cluster.PowerOnVmResult()

      class FaultToleranceVMConfigSpec(vmodl.DynamicData):
         vmConfig = vim.Datastore()
         disks = [ vim.vm.FaultToleranceVMConfigSpec.FaultToleranceDiskSpec() ]

         class FaultToleranceDiskSpec(vmodl.DynamicData):
            disk = vim.vm.device.VirtualDevice()
            datastore = vim.Datastore()

      class FeatureRequirement(vmodl.DynamicData):
         key = ""
         featureName = ""
         value = ""

      class FileInfo(vmodl.DynamicData):
         vmPathName = ""
         snapshotDirectory = ""
         suspendDirectory = ""
         logDirectory = ""
         ftMetadataDirectory = ""

      class FileLayout(vmodl.DynamicData):
         configFile = [ "" ]
         logFile = [ "" ]
         disk = [ vim.vm.FileLayout.DiskLayout() ]
         snapshot = [ vim.vm.FileLayout.SnapshotLayout() ]
         swapFile = ""

         class DiskLayout(vmodl.DynamicData):
            key = 0
            diskFile = [ "" ]

         class SnapshotLayout(vmodl.DynamicData):
            key = vim.vm.Snapshot()
            snapshotFile = [ "" ]

      class FileLayoutEx(vmodl.DynamicData):
         file = [ vim.vm.FileLayoutEx.FileInfo() ]
         disk = [ vim.vm.FileLayoutEx.DiskLayout() ]
         snapshot = [ vim.vm.FileLayoutEx.SnapshotLayout() ]
         timestamp = vmodl.DateTime()

         class FileType(Enum):
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

         class FileInfo(vmodl.DynamicData):
            key = 0
            name = ""
            type = ""
            size = 0
            uniqueSize = 0
            backingObjectId = ""
            accessible = False

         class DiskUnit(vmodl.DynamicData):
            fileKey = [ 0 ]

         class DiskLayout(vmodl.DynamicData):
            key = 0
            chain = [ vim.vm.FileLayoutEx.DiskUnit() ]

         class SnapshotLayout(vmodl.DynamicData):
            key = vim.vm.Snapshot()
            dataKey = 0
            memoryKey = 0
            disk = [ vim.vm.FileLayoutEx.DiskLayout() ]

      class FlagInfo(vmodl.DynamicData):
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

         class HtSharing(Enum):
            any = 0
            none = 1
            internal = 2

         class PowerOffBehavior(Enum):
            powerOff = 0
            revert = 1
            prompt = 2
            take = 3

         class MonitorType(Enum):
            release = 0
            debug = 1
            stats = 2

         class VirtualMmuUsage(Enum):
            automatic = 0
            on = 1
            off = 2

         class VirtualExecUsage(Enum):
            hvAuto = 0
            hvOn = 1
            hvOff = 2

      class ForkConfigInfo(vmodl.DynamicData):
         parentEnabled = False
         childForkGroupId = ""
         parentForkGroupId = ""
         childType = ""

         class ChildType(Enum):
            none = 0
            persistent = 1
            nonpersistent = 2

      class GuestCustomizationManager(vmodl.ManagedObject):

         def customize(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), spec=vim.vm.customization.Specification(), configParams=[ vim.option.OptionValue() ] or None):
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

         def startNetwork(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()):
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

         def abortCustomization(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()):
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidGuestLogin, vim.fault.GuestPermissionDenied, vim.fault.CustomizationFault
            return vim.Task()

      class GuestInfo(vmodl.DynamicData):
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

         class ToolsStatus(Enum):
            toolsNotInstalled = 0
            toolsNotRunning = 1
            toolsOld = 2
            toolsOk = 3

         class ToolsVersionStatus(Enum):
            guestToolsNotInstalled = 0
            guestToolsNeedUpgrade = 1
            guestToolsCurrent = 2
            guestToolsUnmanaged = 3
            guestToolsTooOld = 4
            guestToolsSupportedOld = 5
            guestToolsSupportedNew = 6
            guestToolsTooNew = 7
            guestToolsBlacklisted = 8

         class ToolsRunningStatus(Enum):
            guestToolsNotRunning = 0
            guestToolsRunning = 1
            guestToolsExecutingScripts = 2

         class ToolsInstallType(Enum):
            guestToolsTypeUnknown = 0
            guestToolsTypeMSI = 1
            guestToolsTypeTar = 2
            guestToolsTypeOSP = 3
            guestToolsTypeOpenVMTools = 4

         class VirtualDiskMapping(vmodl.DynamicData):
            key = 0

         class DiskInfo(vmodl.DynamicData):
            diskPath = ""
            capacity = 0
            freeSpace = 0
            filesystemType = ""
            mappings = [ vim.vm.GuestInfo.VirtualDiskMapping() ]

         class NicInfo(vmodl.DynamicData):
            network = ""
            ipAddress = [ "" ]
            macAddress = ""
            connected = False
            deviceConfigId = 0
            dnsConfig = vim.net.DnsConfigInfo()
            ipConfig = vim.net.IpConfigInfo()
            netBIOSConfig = vim.net.NetBIOSConfigInfo()

         class StackInfo(vmodl.DynamicData):
            dnsConfig = vim.net.DnsConfigInfo()
            ipRouteConfig = vim.net.IpRouteConfigInfo()
            ipStackConfig = [ vim.KeyValue() ]
            dhcpConfig = vim.net.DhcpConfigInfo()

         class ScreenInfo(vmodl.DynamicData):
            width = 0
            height = 0

         class GuestState(Enum):
            running = 0
            shuttingDown = 1
            resetting = 2
            standby = 3
            notRunning = 4
            unknown = 5

         class AppStateType(Enum):
            none = 0
            appStateOk = 1
            appStateNeedReset = 2

         class NamespaceGenerationInfo(vmodl.DynamicData):
            key = ""
            generationNo = 0

      class GuestIntegrityInfo(vmodl.DynamicData):
         enabled = False

      class GuestMonitoringModeInfo(vmodl.DynamicData):
         gmmFile = ""
         gmmAppliance = ""

      class GuestOsDescriptor(vmodl.DynamicData):
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

         class GuestOsFamily(Enum):
            windowsGuest = 0
            linuxGuest = 1
            netwareGuest = 2
            solarisGuest = 3
            darwinGuestFamily = 4
            otherGuestFamily = 5

         class GuestOsIdentifier(Enum):
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

         class FirmwareType(Enum):
            bios = 0
            efi = 1
            csm = 2

         class SupportLevel(Enum):
            experimental = 0
            legacy = 1
            terminated = 2
            supported = 3
            unsupported = 4
            deprecated = 5
            techPreview = 6

      class GuestQuiesceSpec(vmodl.DynamicData):
         timeout = 0

      class InstantCloneSpec(vmodl.DynamicData):
         name = ""
         location = vim.vm.RelocateSpec()
         config = [ vim.option.OptionValue() ]
         biosUuid = ""

      class LegacyNetworkSwitchInfo(vmodl.DynamicData):
         name = ""

      class Message(vmodl.DynamicData):
         id = ""
         argument = [ anyType() ]
         text = ""

      class MetadataManager(object):

         class VmMetadataOwner(vmodl.DynamicData):
            name = ""

            class Owner(Enum):
               ComVmwareVsphereHA = 0

         class VmMetadataOp(Enum):
            Update = 0
            Remove = 1

         class VmMetadata(vmodl.DynamicData):
            vmId = ""
            metadata = ""

         class VmMetadataInput(vmodl.DynamicData):
            operation = ""
            vmMetadata = vim.vm.MetadataManager.VmMetadata()

         class VmMetadataResult(vmodl.DynamicData):
            vmMetadata = vim.vm.MetadataManager.VmMetadata()
            error = vmodl.MethodFault()

      class NetworkShaperInfo(vmodl.DynamicData):
         enabled = False
         peakBps = 0
         averageBps = 0
         burstSize = 0

      class ProfileDetails(vmodl.DynamicData):
         profile = [ vim.vm.ProfileSpec() ]
         diskProfileDetails = [ vim.vm.ProfileDetails.DiskProfileDetails() ]

         class DiskProfileDetails(vmodl.DynamicData):
            diskId = 0
            profile = [ vim.vm.ProfileSpec() ]

      class ProfileRawData(vmodl.DynamicData):
         extensionKey = ""
         objectData = ""

      class ProfileSpec(vmodl.DynamicData):
         pass

      class PropertyRelation(vmodl.DynamicData):
         key = vmodl.DynamicProperty()
         relations = [ vmodl.DynamicProperty() ]

      class QuestionInfo(vmodl.DynamicData):
         id = ""
         text = ""
         choice = vim.option.ChoiceOption()
         message = [ vim.vm.Message() ]

      class ReplicationConfigSpec(vmodl.DynamicData):
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

         class DiskSettings(vmodl.DynamicData):
            key = 0
            diskReplicationId = ""

      class ScheduledHardwareUpgradeInfo(vmodl.DynamicData):
         upgradePolicy = ""
         versionKey = ""
         scheduledHardwareUpgradeStatus = ""
         fault = vmodl.MethodFault()

         class HardwareUpgradePolicy(Enum):
            never = 0
            onSoftPowerOff = 1
            always = 2

         class HardwareUpgradeStatus(Enum):
            none = 0
            pending = 1
            success = 2
            failed = 3

      class SgxInfo(vmodl.DynamicData):
         epcSize = 0
         flcMode = ""
         lePubKeyHash = ""

         class FlcModes(Enum):
            locked = 0
            unlocked = 1

      class Snapshot(vim.ExtensibleManagedObject):
         config = vim.vm.ConfigInfo()
         childSnapshot = [ vim.vm.Snapshot() ]
         vm = vim.VirtualMachine()

         def revert(host=vim.HostSystem() or None, suppressPowerOn=False or None):
            # throws vim.fault.TaskInProgress, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
            return vim.Task()

         def remove(removeChildren=False, consolidate=False or None):
            # throws vim.fault.TaskInProgress
            return vim.Task()

         def rename(name="" or None, description="" or None):
            # throws vim.fault.InvalidName, vim.fault.TaskInProgress, vim.fault.InvalidState
            return None

         def exportSnapshot():
            # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
            return vim.HttpNfcLease()

      class SnapshotInfo(vmodl.DynamicData):
         currentSnapshot = vim.vm.Snapshot()
         rootSnapshotList = [ vim.vm.SnapshotTree() ]

      class SriovDevicePoolInfo(vmodl.DynamicData):
         key = ""

      class SriovNetworkDevicePoolInfo(vim.vm.SriovDevicePoolInfo):
         switchKey = ""
         switchUuid = ""

      class StorageInfo(vmodl.DynamicData):
         perDatastoreUsage = [ vim.vm.StorageInfo.UsageOnDatastore() ]
         timestamp = vmodl.DateTime()

         class UsageOnDatastore(vmodl.DynamicData):
            datastore = vim.Datastore()
            committed = 0
            uncommitted = 0
            unshared = 0

      class TargetInfo(vmodl.DynamicData):
         name = ""
         configurationTag = [ "" ]

         class ConfigurationTag(Enum):
            compliant = 0
            clusterWide = 1

      class ToolsConfigInfo(vmodl.DynamicData):
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

         class UpgradePolicy(Enum):
            manual = 0
            upgradeAtPowerCycle = 1

         class ToolsLastInstallInfo(vmodl.DynamicData):
            counter = 0
            fault = vmodl.MethodFault()

      class UsbInfo(vim.vm.TargetInfo):
         description = ""
         vendor = 0
         product = 0
         physicalPath = ""
         family = [ "" ]
         speed = [ "" ]
         summary = vim.vm.Summary()

         class Speed(Enum):
            low = 0
            full = 1
            high = 2
            superSpeed = 3
            superSpeedPlus = 4
            unknownSpeed = 5

         class Family(Enum):
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

      class UsbScanCodeSpec(vmodl.DynamicData):
         keyEvents = [ vim.vm.UsbScanCodeSpec.KeyEvent() ]

         class ModifierType(vmodl.DynamicData):
            leftControl = False
            leftShift = False
            leftAlt = False
            leftGui = False
            rightControl = False
            rightShift = False
            rightAlt = False
            rightGui = False

         class KeyEvent(vmodl.DynamicData):
            usbHidCode = 0
            modifiers = vim.vm.UsbScanCodeSpec.ModifierType()

      class VcpuConfig(vmodl.DynamicData):
         latencySensitivity = vim.LatencySensitivity()

      class VirtualHardware(vmodl.DynamicData):
         numCPU = 0
         numCoresPerSocket = 0
         memoryMB = 0
         virtualICH7MPresent = False
         virtualSMCPresent = False
         device = [ vim.vm.device.VirtualDevice() ]

      class VirtualHardwareOption(vmodl.DynamicData):
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

      class WindowsQuiesceSpec(vim.vm.GuestQuiesceSpec):
         vssBackupType = 0
         vssBootableSystemState = False
         vssPartialFileSupport = False
         vssBackupContext = ""

         class VssBackupContext(Enum):
            ctx_auto = 0
            ctx_backup = 1
            ctx_file_share_backup = 2

      class check(object):

         class CompatibilityChecker(vmodl.ManagedObject):

            def checkCompatibility(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None):
               # throws vim.fault.InvalidState, vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

            def checkVmConfig(spec=vim.vm.ConfigSpec(), vm=vim.VirtualMachine() or None, host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None):
               # throws vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

            def checkPowerOn(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, testType=[ "" ] or None):
               # throws vmodl.fault.InvalidArgument, vim.fault.DatacenterMismatch
               return vim.Task()

         class Result(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            host = vim.HostSystem()
            warning = [ vmodl.MethodFault() ]
            error = [ vmodl.MethodFault() ]

         class TestType(Enum):
            sourceTests = 0
            hostTests = 1
            resourcePoolTests = 2
            datastoreTests = 3
            networkTests = 4

         class ProvisioningChecker(vmodl.ManagedObject):

            def queryVMotionCompatibilityEx(vm=[ vim.VirtualMachine() ], host=[ vim.HostSystem() ]):
               return vim.Task()

            def checkMigrate(vm=vim.VirtualMachine(), host=vim.HostSystem() or None, pool=vim.ResourcePool() or None, state=vim.VirtualMachine.PowerState() or None, testType=[ "" ] or None):
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkRelocate(vm=vim.VirtualMachine(), spec=vim.vm.RelocateSpec(), testType=[ "" ] or None):
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkClone(vm=vim.VirtualMachine(), folder=vim.Folder(), name="", spec=vim.vm.CloneSpec(), testType=[ "" ] or None):
               # throws vim.fault.InvalidState
               return vim.Task()

            def checkInstantClone(vm=vim.VirtualMachine(), spec=vim.vm.InstantCloneSpec(), testType=[ "" ] or None):
               # throws vim.fault.InvalidState
               return vim.Task()

      class customization(object):

         class AdapterMapping(vmodl.DynamicData):
            macAddress = ""
            adapter = vim.vm.customization.IPSettings()

         class GlobalIPSettings(vmodl.DynamicData):
            dnsSuffixList = [ "" ]
            dnsServerList = [ "" ]

         class GuiRunOnce(vmodl.DynamicData):
            commandList = [ "" ]

         class GuiUnattended(vmodl.DynamicData):
            password = vim.vm.customization.Password()
            timeZone = 0
            autoLogon = False
            autoLogonCount = 0

         class IPSettings(vmodl.DynamicData):
            ip = vim.vm.customization.IpGenerator()
            subnetMask = ""
            gateway = [ "" ]
            ipV6Spec = vim.vm.customization.IPSettings.IpV6AddressSpec()
            dnsServerList = [ "" ]
            dnsDomain = ""
            primaryWINS = ""
            secondaryWINS = ""
            netBIOS = vim.vm.customization.IPSettings.NetBIOSMode()

            class IpV6AddressSpec(vmodl.DynamicData):
               ip = [ vim.vm.customization.IpV6Generator() ]
               gateway = [ "" ]

            class NetBIOSMode(Enum):
               enableNetBIOSViaDhcp = 0
               enableNetBIOS = 1
               disableNetBIOS = 2

         class Identification(vmodl.DynamicData):
            joinWorkgroup = ""
            joinDomain = ""
            domainAdmin = ""
            domainAdminPassword = vim.vm.customization.Password()

         class IdentitySettings(vmodl.DynamicData):
            pass

         class IpGenerator(vmodl.DynamicData):
            pass

         class IpV6Generator(vmodl.DynamicData):
            pass

         class LicenseFilePrintData(vmodl.DynamicData):
            autoMode = vim.vm.customization.LicenseFilePrintData.AutoMode()
            autoUsers = 0

            class AutoMode(Enum):
               perServer = 0
               perSeat = 1

         class LinuxPrep(vim.vm.customization.IdentitySettings):
            hostName = vim.vm.customization.NameGenerator()
            domain = ""
            timeZone = ""
            hwClockUTC = False
            scriptText = ""

         class NameGenerator(vmodl.DynamicData):
            pass

         class Options(vmodl.DynamicData):
            pass

         class Password(vmodl.DynamicData):
            value = ""
            plainText = False

         class PrefixNameGenerator(vim.vm.customization.NameGenerator):
            base = ""

         class Specification(vmodl.DynamicData):
            options = vim.vm.customization.Options()
            identity = vim.vm.customization.IdentitySettings()
            globalIPSettings = vim.vm.customization.GlobalIPSettings()
            nicSettingMap = [ vim.vm.customization.AdapterMapping() ]
            encryptionKey = [ 0x00 ]

         class StatelessIpV6Generator(vim.vm.customization.IpV6Generator):
            pass

         class Sysprep(vim.vm.customization.IdentitySettings):
            guiUnattended = vim.vm.customization.GuiUnattended()
            userData = vim.vm.customization.UserData()
            guiRunOnce = vim.vm.customization.GuiRunOnce()
            identification = vim.vm.customization.Identification()
            licenseFilePrintData = vim.vm.customization.LicenseFilePrintData()

         class SysprepText(vim.vm.customization.IdentitySettings):
            value = ""

         class UnknownIpGenerator(vim.vm.customization.IpGenerator):
            pass

         class UnknownIpV6Generator(vim.vm.customization.IpV6Generator):
            pass

         class UnknownNameGenerator(vim.vm.customization.NameGenerator):
            pass

         class UserData(vmodl.DynamicData):
            fullName = ""
            orgName = ""
            computerName = vim.vm.customization.NameGenerator()
            productId = ""

         class VirtualMachineNameGenerator(vim.vm.customization.NameGenerator):
            pass

         class WinOptions(vim.vm.customization.Options):
            changeSID = False
            deleteAccounts = False
            reboot = vim.vm.customization.WinOptions.SysprepRebootOption()

            class SysprepRebootOption(Enum):
               reboot = 0
               noreboot = 1
               shutdown = 2

         class AutoIpV6Generator(vim.vm.customization.IpV6Generator):
            pass

         class CustomIpGenerator(vim.vm.customization.IpGenerator):
            argument = ""

         class CustomIpV6Generator(vim.vm.customization.IpV6Generator):
            argument = ""

         class CustomNameGenerator(vim.vm.customization.NameGenerator):
            argument = ""

         class DhcpIpGenerator(vim.vm.customization.IpGenerator):
            pass

         class DhcpIpV6Generator(vim.vm.customization.IpV6Generator):
            pass

         class FixedIp(vim.vm.customization.IpGenerator):
            ipAddress = ""

         class FixedIpV6(vim.vm.customization.IpV6Generator):
            ipAddress = ""
            subnetMask = 0

         class FixedName(vim.vm.customization.NameGenerator):
            name = ""

         class LinuxOptions(vim.vm.customization.Options):
            pass

      class device(object):

         class HostDiskMappingInfo(vmodl.DynamicData):
            physicalPartition = vim.vm.device.HostDiskMappingInfo.PartitionInfo()
            name = ""
            exclusive = False

            class PartitionInfo(vmodl.DynamicData):
               name = ""
               fileSystem = ""
               capacityInKb = 0

         class HostDiskMappingOption(vmodl.DynamicData):
            physicalPartition = [ vim.vm.device.HostDiskMappingOption.PartitionOption() ]
            name = ""

            class PartitionOption(vmodl.DynamicData):
               name = ""
               fileSystem = ""
               capacityInKb = 0

         class VirtualDevice(vmodl.DynamicData):
            key = 0
            deviceInfo = vim.Description()
            backing = vim.vm.device.VirtualDevice.BackingInfo()
            connectable = vim.vm.device.VirtualDevice.ConnectInfo()
            slotInfo = vim.vm.device.VirtualDevice.BusSlotInfo()
            controllerKey = 0
            unitNumber = 0

            class BackingInfo(vmodl.DynamicData):
               pass

            class FileBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               fileName = ""
               datastore = vim.Datastore()
               backingObjectId = ""

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               deviceName = ""
               useAutoDetect = False

            class RemoteDeviceBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               deviceName = ""
               useAutoDetect = False

            class PipeBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               pipeName = ""

            class URIBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               serviceURI = ""
               direction = ""
               proxyURI = ""

            class ConnectInfo(vmodl.DynamicData):
               migrateConnect = ""
               startConnected = False
               allowGuestControl = False
               connected = False
               status = ""

               class Status(Enum):
                  ok = 0
                  recoverableError = 1
                  unrecoverableError = 2
                  untried = 3

               class MigrateConnectOp(Enum):
                  connect = 0
                  disconnect = 1
                  unset = 2

            class BusSlotInfo(vmodl.DynamicData):
               pass

            class PciBusSlotInfo(vim.vm.device.VirtualDevice.BusSlotInfo):
               pciSlotNumber = 0

         class VirtualDeviceOption(vmodl.DynamicData):
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

            class BackingOption(vmodl.DynamicData):
               type = vmodl.TypeName()

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               fileNameExtensions = vim.option.ChoiceOption()

               class FileExtension(Enum):
                  iso = 0
                  flp = 1
                  vmdk = 2
                  dsk = 3
                  rdm = 4

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               autoDetectAvailable = vim.option.BoolOption()

            class RemoteDeviceBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               autoDetectAvailable = vim.option.BoolOption()

            class PipeBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

            class URIBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               directions = vim.option.ChoiceOption()

               class Direction(Enum):
                  server = 0
                  client = 1

            class ConnectOption(vmodl.DynamicData):
               startConnected = vim.option.BoolOption()
               allowGuestControl = vim.option.BoolOption()

            class BusSlotOption(vmodl.DynamicData):
               type = vmodl.TypeName()

         class VirtualDeviceSpec(vmodl.DynamicData):
            operation = vim.vm.device.VirtualDeviceSpec.Operation()
            fileOperation = vim.vm.device.VirtualDeviceSpec.FileOperation()
            device = vim.vm.device.VirtualDevice()
            profile = [ vim.vm.ProfileSpec() ]
            backing = vim.vm.device.VirtualDeviceSpec.BackingSpec()

            class Operation(Enum):
               add = 0
               remove = 1
               edit = 2

            class FileOperation(Enum):
               create = 0
               destroy = 1
               replace = 2

            class BackingSpec(vmodl.DynamicData):
               parent = vim.vm.device.VirtualDeviceSpec.BackingSpec()
               crypto = vim.encryption.CryptoSpec()

         class VirtualDisk(vim.vm.device.VirtualDevice):
            capacityInKB = 0
            capacityInBytes = 0
            shares = vim.SharesInfo()
            storageIOAllocation = vim.StorageResourceManager.IOAllocationInfo()
            diskObjectId = ""
            vFlashCacheConfigInfo = vim.vm.device.VirtualDisk.VFlashCacheConfigInfo()
            iofilter = [ "" ]
            vDiskId = vim.vslm.ID()
            nativeUnmanagedLinkedClone = False

            class DeltaDiskFormat(Enum):
               redoLogFormat = 0
               nativeFormat = 1
               seSparseFormat = 2

            class DeltaDiskFormatVariant(Enum):
               vmfsSparseVariant = 0
               vsanSparseVariant = 1

            class Sharing(Enum):
               sharingNone = 0
               sharingMultiWriter = 1

            class SparseVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               diskMode = ""
               split = False
               writeThrough = False
               spaceUsedInKB = 0
               contentId = ""
               parent = vim.vm.device.VirtualDisk.SparseVer1BackingInfo()

            class SparseVer2BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               diskMode = ""
               split = False
               writeThrough = False
               spaceUsedInKB = 0
               uuid = ""
               contentId = ""
               changeId = ""
               parent = vim.vm.device.VirtualDisk.SparseVer2BackingInfo()
               keyId = vim.encryption.CryptoKeyId()

            class FlatVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               diskMode = ""
               split = False
               writeThrough = False
               contentId = ""
               parent = vim.vm.device.VirtualDisk.FlatVer1BackingInfo()

            class FlatVer2BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
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

            class SeSparseBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
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

            class RawDiskVer2BackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               descriptorFileName = ""
               uuid = ""
               changeId = ""
               sharing = ""

            class PartitionedRawDiskVer2BackingInfo(vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo):
               partition = [ 0 ]

            class RawDiskMappingVer1BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
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

            class LocalPMemBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               diskMode = ""
               uuid = ""
               volumeUUID = ""
               contentId = ""

            class VFlashCacheConfigInfo(vmodl.DynamicData):
               vFlashModule = ""
               reservationInMB = 0
               cacheConsistencyType = ""
               cacheMode = ""
               blockSizeInKB = 0

               class CacheConsistencyType(Enum):
                  strong = 0
                  weak = 1

               class CacheMode(Enum):
                  write_thru = 0
                  write_back = 1

         class VirtualDiskId(vmodl.DynamicData):
            vm = vim.VirtualMachine()
            diskId = 0

         class VirtualDiskOption(vim.vm.device.VirtualDeviceOption):
            capacityInKB = vim.option.LongOption()
            ioAllocationOption = vim.StorageResourceManager.IOAllocationOption()
            vFlashCacheConfigOption = vim.vm.device.VirtualDiskOption.VFlashCacheConfigOption()

            class DiskMode(Enum):
               persistent = 0
               nonpersistent = 1
               undoable = 2
               independent_persistent = 3
               independent_nonpersistent = 4
               append = 5

            class CompatibilityMode(Enum):
               virtualMode = 0
               physicalMode = 1

            class SparseVer1BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               diskModes = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False

            class SparseVer2BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               diskMode = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False
               hotGrowable = False
               uuid = False

            class FlatVer1BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               diskMode = vim.option.ChoiceOption()
               split = vim.option.BoolOption()
               writeThrough = vim.option.BoolOption()
               growable = False

            class DeltaDiskFormatsSupported(vmodl.DynamicData):
               datastoreType = vmodl.TypeName()
               deltaDiskFormat = vim.option.ChoiceOption()

            class FlatVer2BackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
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

            class SeSparseBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               diskMode = vim.option.ChoiceOption()
               writeThrough = vim.option.BoolOption()
               growable = False
               hotGrowable = False
               uuid = False
               deltaDiskFormatsSupported = [ vim.vm.device.VirtualDiskOption.DeltaDiskFormatsSupported() ]

            class RawDiskVer2BackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               descriptorFileNameExtensions = vim.option.ChoiceOption()
               uuid = False

            class PartitionedRawDiskVer2BackingOption(vim.vm.device.VirtualDiskOption.RawDiskVer2BackingOption):
               pass

            class RawDiskMappingVer1BackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               descriptorFileNameExtensions = vim.option.ChoiceOption()
               compatibilityMode = vim.option.ChoiceOption()
               diskMode = vim.option.ChoiceOption()
               uuid = False

            class LocalPMemBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               diskMode = vim.option.ChoiceOption()
               growable = False
               hotGrowable = False
               uuid = False

            class VFlashCacheConfigOption(vmodl.DynamicData):
               cacheConsistencyType = vim.option.ChoiceOption()
               cacheMode = vim.option.ChoiceOption()
               reservationInMB = vim.option.LongOption()
               blockSizeInKB = vim.option.LongOption()

         class VirtualDiskSpec(vim.vm.device.VirtualDeviceSpec):
            diskMoveType = ""
            migrateCache = False

         class VirtualEthernetCard(vim.vm.device.VirtualDevice):
            addressType = ""
            macAddress = ""
            wakeOnLanEnabled = False
            resourceAllocation = vim.vm.device.VirtualEthernetCard.ResourceAllocation()
            externalId = ""
            uptCompatibilityEnabled = False

            class NetworkBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               network = vim.Network()
               inPassthroughMode = False

            class LegacyNetworkBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

            class DistributedVirtualPortBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               port = vim.dvs.PortConnection()

            class OpaqueNetworkBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               opaqueNetworkId = ""
               opaqueNetworkType = ""

            class ResourceAllocation(vmodl.DynamicData):
               reservation = 0
               share = vim.SharesInfo()
               limit = 0

         class VirtualEthernetCardOption(vim.vm.device.VirtualDeviceOption):
            supportedOUI = vim.option.ChoiceOption()
            macType = vim.option.ChoiceOption()
            wakeOnLanEnabled = vim.option.BoolOption()
            vmDirectPathGen2Supported = False
            uptCompatibilityEnabled = vim.option.BoolOption()

            class NetworkBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class OpaqueNetworkBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

            class LegacyNetworkBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):

               class LegacyNetworkDeviceName(Enum):
                  bridged = 0
                  nat = 1
                  hostonly = 2

            class DistributedVirtualPortBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

            class MacTypes(Enum):
               manual = 0
               generated = 1
               assigned = 2

         class VirtualFloppy(vim.vm.device.VirtualDevice):

            class ImageBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

            class RemoteDeviceBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo):
               pass

         class VirtualFloppyOption(vim.vm.device.VirtualDeviceOption):

            class ImageBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class RemoteDeviceBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption):
               pass

         class VirtualKeyboard(vim.vm.device.VirtualDevice):
            pass

         class VirtualKeyboardOption(vim.vm.device.VirtualDeviceOption):
            pass

         class VirtualNVDIMM(vim.vm.device.VirtualDevice):
            capacityInMB = 0

            class BackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               parent = vim.vm.device.VirtualNVDIMM.BackingInfo()
               changeId = ""

         class VirtualNVDIMMOption(vim.vm.device.VirtualDeviceOption):
            capacityInMB = vim.option.LongOption()
            growable = False
            hotGrowable = False
            granularityInMB = 0

         class VirtualPCIPassthrough(vim.vm.device.VirtualDevice):

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               id = ""
               deviceId = ""
               systemId = ""
               vendorId = 0

            class AllowedDevice(vmodl.DynamicData):
               vendorId = 0
               deviceId = 0
               subVendorId = 0
               subDeviceId = 0
               revisionId = 0

            class DynamicBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               allowedDevice = [ vim.vm.device.VirtualPCIPassthrough.AllowedDevice() ]
               customLabel = ""
               assignedId = ""

            class PluginBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               pass

            class VmiopBackingInfo(vim.vm.device.VirtualPCIPassthrough.PluginBackingInfo):
               vgpu = ""

         class VirtualPCIPassthroughOption(vim.vm.device.VirtualDeviceOption):

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class PluginBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

            class VmiopBackingOption(vim.vm.device.VirtualPCIPassthroughOption.PluginBackingOption):
               vgpu = vim.option.StringOption()
               maxInstances = 0

            class DynamicBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

         class VirtualPCNet32(vim.vm.device.VirtualEthernetCard):
            pass

         class VirtualPCNet32Option(vim.vm.device.VirtualEthernetCardOption):
            supportsMorphing = False

         class VirtualParallelPort(vim.vm.device.VirtualDevice):

            class FileBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

         class VirtualParallelPortOption(vim.vm.device.VirtualDeviceOption):

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

         class VirtualPointingDevice(vim.vm.device.VirtualDevice):

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               hostPointingDevice = ""

         class VirtualPointingDeviceOption(vim.vm.device.VirtualDeviceOption):

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               hostPointingDevice = vim.option.ChoiceOption()

               class HostPointingDeviceChoice(Enum):
                  autodetect = 0
                  intellimouseExplorer = 1
                  intellimousePs2 = 2
                  logitechMouseman = 3
                  microsoft_serial = 4
                  mouseSystems = 5
                  mousemanSerial = 6
                  ps2 = 7

         class VirtualPrecisionClock(vim.vm.device.VirtualDevice):

            class SystemClockBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               protocol = ""

         class VirtualPrecisionClockOption(vim.vm.device.VirtualDeviceOption):

            class SystemClockBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               protocol = vim.option.ChoiceOption()

         class VirtualSCSIPassthrough(vim.vm.device.VirtualDevice):

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

         class VirtualSCSIPassthroughOption(vim.vm.device.VirtualDeviceOption):

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

         class VirtualSerialPort(vim.vm.device.VirtualDevice):
            yieldOnPoll = False

            class FileBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               pass

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

            class PipeBackingInfo(vim.vm.device.VirtualDevice.PipeBackingInfo):
               endpoint = ""
               noRxLoss = False

            class URIBackingInfo(vim.vm.device.VirtualDevice.URIBackingInfo):
               pass

            class ThinPrintBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               pass

         class VirtualSerialPortOption(vim.vm.device.VirtualDeviceOption):
            yieldOnPoll = vim.option.BoolOption()

            class EndPoint(Enum):
               client = 0
               server = 1

            class FileBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               pass

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class PipeBackingOption(vim.vm.device.VirtualDeviceOption.PipeBackingOption):
               endpoint = vim.option.ChoiceOption()
               noRxLoss = vim.option.BoolOption()

            class URIBackingOption(vim.vm.device.VirtualDeviceOption.URIBackingOption):
               pass

            class ThinPrintBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

         class VirtualSoundCard(vim.vm.device.VirtualDevice):

            class DeviceBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

         class VirtualSoundCardOption(vim.vm.device.VirtualDeviceOption):

            class DeviceBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

         class VirtualSriovEthernetCard(vim.vm.device.VirtualEthernetCard):
            allowGuestOSMtuChange = False
            sriovBacking = vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo()

            class SriovBackingInfo(vim.vm.device.VirtualDevice.BackingInfo):
               physicalFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
               virtualFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
               virtualFunctionIndex = 0

         class VirtualSriovEthernetCardOption(vim.vm.device.VirtualEthernetCardOption):

            class SriovBackingOption(vim.vm.device.VirtualDeviceOption.BackingOption):
               pass

         class VirtualTPM(vim.vm.device.VirtualDevice):
            endorsementKeyCertificateSigningRequest = [ vmodl.Binary() ]
            endorsementKeyCertificate = [ vmodl.Binary() ]

         class VirtualTPMOption(vim.vm.device.VirtualDeviceOption):
            supportedFirmware = [ "" ]

         class VirtualUSB(vim.vm.device.VirtualDevice):
            connected = False
            vendor = 0
            product = 0
            family = [ "" ]
            speed = [ "" ]

            class USBBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

            class RemoteHostBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               hostname = ""

            class RemoteClientBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo):
               hostname = ""

         class VirtualUSBOption(vim.vm.device.VirtualDeviceOption):

            class USBBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class RemoteHostBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class RemoteClientBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption):
               pass

         class VirtualVMCIDevice(vim.vm.device.VirtualDevice):
            id = 0
            allowUnrestrictedCommunication = False
            filterEnable = False
            filterInfo = vim.vm.device.VirtualVMCIDevice.FilterInfo()

            class Action(Enum):
               allow = 0
               deny = 1

            class Protocol(Enum):
               hypervisor = 0
               doorbell = 1
               queuepair = 2
               datagram = 3
               stream = 4
               anyProtocol = 5

            class Direction(Enum):
               guest = 0
               host = 1
               anyDirection = 2

            class FilterSpec(vmodl.DynamicData):
               rank = 0
               action = ""
               protocol = ""
               direction = ""
               lowerDstPortBoundary = 0
               upperDstPortBoundary = 0

            class FilterInfo(vmodl.DynamicData):
               filters = [ vim.vm.device.VirtualVMCIDevice.FilterSpec() ]

         class VirtualVMCIDeviceOption(vim.vm.device.VirtualDeviceOption):
            allowUnrestrictedCommunication = vim.option.BoolOption()
            filterSpecOption = vim.vm.device.VirtualVMCIDeviceOption.FilterSpecOption()
            filterSupported = vim.option.BoolOption()

            class FilterSpecOption(vmodl.DynamicData):
               action = vim.option.ChoiceOption()
               protocol = vim.option.ChoiceOption()
               direction = vim.option.ChoiceOption()
               lowerDstPortBoundary = vim.option.LongOption()
               upperDstPortBoundary = vim.option.LongOption()

         class VirtualVMIROM(vim.vm.device.VirtualDevice):
            pass

         class VirtualVMIROMOption(vim.vm.device.VirtualDeviceOption):
            pass

         class VirtualVideoCard(vim.vm.device.VirtualDevice):
            videoRamSizeInKB = 0
            numDisplays = 0
            useAutoDetect = False
            enable3DSupport = False
            use3dRenderer = ""
            graphicsMemorySizeInKB = 0

            class Use3dRenderer(Enum):
               automatic = 0
               software = 1
               hardware = 2

         class VirtualVideoCardOption(vim.vm.device.VirtualDeviceOption):
            videoRamSizeInKB = vim.option.LongOption()
            numDisplays = vim.option.IntOption()
            useAutoDetect = vim.option.BoolOption()
            support3D = vim.option.BoolOption()
            use3dRendererSupported = vim.option.BoolOption()
            graphicsMemorySizeInKB = vim.option.LongOption()
            graphicsMemorySizeSupported = vim.option.BoolOption()

         class VirtualVmxnet(vim.vm.device.VirtualEthernetCard):
            pass

         class VirtualVmxnet2(vim.vm.device.VirtualVmxnet):
            pass

         class VirtualVmxnet3(vim.vm.device.VirtualVmxnet):
            pass

         class VirtualVmxnet3Vrdma(vim.vm.device.VirtualVmxnet3):
            deviceProtocol = ""

         class VirtualVmxnetOption(vim.vm.device.VirtualEthernetCardOption):
            pass

         class VirtualWDT(vim.vm.device.VirtualDevice):
            runOnBoot = False
            running = False

         class VirtualWDTOption(vim.vm.device.VirtualDeviceOption):
            runOnBoot = vim.option.BoolOption()

         class VirtualCdrom(vim.vm.device.VirtualDevice):

            class IsoBackingInfo(vim.vm.device.VirtualDevice.FileBackingInfo):
               pass

            class PassthroughBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               exclusive = False

            class RemotePassthroughBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo):
               exclusive = False

            class AtapiBackingInfo(vim.vm.device.VirtualDevice.DeviceBackingInfo):
               pass

            class RemoteAtapiBackingInfo(vim.vm.device.VirtualDevice.RemoteDeviceBackingInfo):
               pass

         class VirtualCdromOption(vim.vm.device.VirtualDeviceOption):

            class IsoBackingOption(vim.vm.device.VirtualDeviceOption.FileBackingOption):
               pass

            class PassthroughBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               exclusive = vim.option.BoolOption()

            class RemotePassthroughBackingOption(vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption):
               exclusive = vim.option.BoolOption()

            class AtapiBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

            class RemoteAtapiBackingOption(vim.vm.device.VirtualDeviceOption.DeviceBackingOption):
               pass

         class VirtualController(vim.vm.device.VirtualDevice):
            busNumber = 0
            device = [ 0 ]

         class VirtualControllerOption(vim.vm.device.VirtualDeviceOption):
            devices = vim.option.IntOption()
            supportedDevice = [ vmodl.TypeName() ]

         class VirtualE1000(vim.vm.device.VirtualEthernetCard):
            pass

         class VirtualE1000Option(vim.vm.device.VirtualEthernetCardOption):
            pass

         class VirtualE1000e(vim.vm.device.VirtualEthernetCard):
            pass

         class VirtualE1000eOption(vim.vm.device.VirtualEthernetCardOption):
            pass

         class VirtualEnsoniq1371(vim.vm.device.VirtualSoundCard):
            pass

         class VirtualEnsoniq1371Option(vim.vm.device.VirtualSoundCardOption):
            pass

         class VirtualHdAudioCard(vim.vm.device.VirtualSoundCard):
            pass

         class VirtualHdAudioCardOption(vim.vm.device.VirtualSoundCardOption):
            pass

         class VirtualIDEController(vim.vm.device.VirtualController):
            pass

         class VirtualIDEControllerOption(vim.vm.device.VirtualControllerOption):
            numIDEDisks = vim.option.IntOption()
            numIDECdroms = vim.option.IntOption()

         class VirtualNVDIMMController(vim.vm.device.VirtualController):
            pass

         class VirtualNVDIMMControllerOption(vim.vm.device.VirtualControllerOption):
            numNVDIMMControllers = vim.option.IntOption()

         class VirtualNVMEController(vim.vm.device.VirtualController):
            pass

         class VirtualNVMEControllerOption(vim.vm.device.VirtualControllerOption):
            numNVMEDisks = vim.option.IntOption()

         class VirtualPCIController(vim.vm.device.VirtualController):
            pass

         class VirtualPCIControllerOption(vim.vm.device.VirtualControllerOption):
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

         class VirtualPS2Controller(vim.vm.device.VirtualController):
            pass

         class VirtualPS2ControllerOption(vim.vm.device.VirtualControllerOption):
            numKeyboards = vim.option.IntOption()
            numPointingDevices = vim.option.IntOption()

         class VirtualSATAController(vim.vm.device.VirtualController):
            pass

         class VirtualSATAControllerOption(vim.vm.device.VirtualControllerOption):
            numSATADisks = vim.option.IntOption()
            numSATACdroms = vim.option.IntOption()

         class VirtualSCSIController(vim.vm.device.VirtualController):
            hotAddRemove = False
            sharedBus = vim.vm.device.VirtualSCSIController.Sharing()
            scsiCtlrUnitNumber = 0

            class Sharing(Enum):
               noSharing = 0
               virtualSharing = 1
               physicalSharing = 2

         class VirtualSCSIControllerOption(vim.vm.device.VirtualControllerOption):
            numSCSIDisks = vim.option.IntOption()
            numSCSICdroms = vim.option.IntOption()
            numSCSIPassthrough = vim.option.IntOption()
            sharing = [ vim.vm.device.VirtualSCSIController.Sharing() ]
            defaultSharedIndex = 0
            hotAddRemove = vim.option.BoolOption()
            scsiCtlrUnitNumber = 0

         class VirtualSIOController(vim.vm.device.VirtualController):
            pass

         class VirtualSIOControllerOption(vim.vm.device.VirtualControllerOption):
            numFloppyDrives = vim.option.IntOption()
            numSerialPorts = vim.option.IntOption()
            numParallelPorts = vim.option.IntOption()

         class VirtualSoundBlaster16(vim.vm.device.VirtualSoundCard):
            pass

         class VirtualSoundBlaster16Option(vim.vm.device.VirtualSoundCardOption):
            pass

         class VirtualUSBController(vim.vm.device.VirtualController):
            autoConnectDevices = False
            ehciEnabled = False

            class PciBusSlotInfo(vim.vm.device.VirtualDevice.PciBusSlotInfo):
               ehciPciSlotNumber = 0

         class VirtualUSBControllerOption(vim.vm.device.VirtualControllerOption):
            autoConnectDevices = vim.option.BoolOption()
            ehciSupported = vim.option.BoolOption()
            supportedSpeeds = [ "" ]

         class VirtualUSBXHCIController(vim.vm.device.VirtualController):
            autoConnectDevices = False

         class VirtualUSBXHCIControllerOption(vim.vm.device.VirtualControllerOption):
            autoConnectDevices = vim.option.BoolOption()
            supportedSpeeds = [ "" ]

         class VirtualVmxnet2Option(vim.vm.device.VirtualVmxnetOption):
            pass

         class VirtualVmxnet3Option(vim.vm.device.VirtualVmxnetOption):
            pass

         class VirtualVmxnet3VrdmaOption(vim.vm.device.VirtualVmxnet3Option):
            deviceProtocol = vim.option.ChoiceOption()

            class DeviceProtocols(Enum):
               rocev1 = 0
               rocev2 = 1

         class ParaVirtualSCSIController(vim.vm.device.VirtualSCSIController):
            pass

         class ParaVirtualSCSIControllerOption(vim.vm.device.VirtualSCSIControllerOption):
            pass

         class VirtualAHCIController(vim.vm.device.VirtualSATAController):
            pass

         class VirtualAHCIControllerOption(vim.vm.device.VirtualSATAControllerOption):
            pass

         class VirtualBusLogicController(vim.vm.device.VirtualSCSIController):
            pass

         class VirtualBusLogicControllerOption(vim.vm.device.VirtualSCSIControllerOption):
            pass

         class VirtualLsiLogicController(vim.vm.device.VirtualSCSIController):
            pass

         class VirtualLsiLogicControllerOption(vim.vm.device.VirtualSCSIControllerOption):
            pass

         class VirtualLsiLogicSASController(vim.vm.device.VirtualSCSIController):
            pass

         class VirtualLsiLogicSASControllerOption(vim.vm.device.VirtualSCSIControllerOption):
            pass

      class guest(object):

         class AliasManager(vmodl.ManagedObject):

            def addAlias(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", mapCert=False, base64Cert="", aliasInfo=vim.vm.guest.AliasManager.GuestAuthAliasInfo()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def removeAlias(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", base64Cert="", subject=vim.vm.guest.AliasManager.GuestAuthSubject()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def removeAliasByCert(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username="", base64Cert=""):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listAliases(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), username=""):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.AliasManager.GuestAliases() ]

            def listMappedAliases(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.AliasManager.GuestMappedAliases() ]

            class GuestAuthSubject(vmodl.DynamicData):
               pass

            class GuestAuthAnySubject(vim.vm.guest.AliasManager.GuestAuthSubject):
               pass

            class GuestAuthNamedSubject(vim.vm.guest.AliasManager.GuestAuthSubject):
               name = ""

            class GuestAuthAliasInfo(vmodl.DynamicData):
               subject = vim.vm.guest.AliasManager.GuestAuthSubject()
               comment = ""

            class GuestAliases(vmodl.DynamicData):
               base64Cert = ""
               aliases = [ vim.vm.guest.AliasManager.GuestAuthAliasInfo() ]

            class GuestMappedAliases(vmodl.DynamicData):
               base64Cert = ""
               username = ""
               subjects = [ vim.vm.guest.AliasManager.GuestAuthSubject() ]

         class AuthManager(vmodl.ManagedObject):

            def validateCredentials(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def acquireCredentials(vm=vim.VirtualMachine(), requestedAuth=vim.vm.guest.GuestAuthentication(), sessionID=0 or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.TaskInProgress, vim.fault.InvalidState
               return vim.vm.guest.GuestAuthentication()

            def releaseCredentials(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication()):
               # throws vim.fault.GuestOperationsFault, vim.fault.TaskInProgress, vim.fault.InvalidState
               return None

         class FileManager(vmodl.ManagedObject):

            def makeDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), directoryPath="", createParentDirectories=False):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def deleteFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), filePath=""):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def deleteDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), directoryPath="", recursive=False):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def moveDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), srcDirectoryPath="", dstDirectoryPath=""):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def moveFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), srcFilePath="", dstFilePath="", overwrite=False):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def createTemporaryFile(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), prefix="", suffix="", directoryPath="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            def createTemporaryDirectory(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), prefix="", suffix="", directoryPath="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            def listFiles(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), filePath="", index=0 or None, maxResults=0 or None, matchPattern="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return vim.vm.guest.FileManager.ListFileInfo()

            def changeFileAttributes(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath="", fileAttributes=vim.vm.guest.FileManager.FileAttributes()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return None

            def initiateFileTransferFromGuest(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath=""):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return vim.vm.guest.FileManager.FileTransferInformation()

            def initiateFileTransferToGuest(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), guestFilePath="", fileAttributes=vim.vm.guest.FileManager.FileAttributes(), fileSize=0, overwrite=False):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return ""

            class FileAttributes(vmodl.DynamicData):
               modificationTime = vmodl.DateTime()
               accessTime = vmodl.DateTime()
               symlinkTarget = ""

            class PosixFileAttributes(vim.vm.guest.FileManager.FileAttributes):
               ownerId = 0
               groupId = 0
               permissions = 0

            class WindowsFileAttributes(vim.vm.guest.FileManager.FileAttributes):
               hidden = False
               readOnly = False
               createTime = vmodl.DateTime()

            class FileInfo(vmodl.DynamicData):
               path = ""
               type = ""
               size = 0
               attributes = vim.vm.guest.FileManager.FileAttributes()

               class FileType(Enum):
                  file = 0
                  directory = 1
                  symlink = 2

            class ListFileInfo(vmodl.DynamicData):
               files = [ vim.vm.guest.FileManager.FileInfo() ]
               remaining = 0

            class FileTransferInformation(vmodl.DynamicData):
               attributes = vim.vm.guest.FileManager.FileAttributes()
               size = 0
               url = ""

         class GuestAuthentication(vmodl.DynamicData):
            interactiveSession = False

         class GuestOperationsManager(vmodl.ManagedObject):
            authManager = vim.vm.guest.AuthManager()
            fileManager = vim.vm.guest.FileManager()
            processManager = vim.vm.guest.ProcessManager()
            guestWindowsRegistryManager = vim.vm.guest.WindowsRegistryManager()
            aliasManager = vim.vm.guest.AliasManager()

         class NamePasswordAuthentication(vim.vm.guest.GuestAuthentication):
            username = ""
            password = ""

         class ProcessManager(vmodl.ManagedObject):

            def startProgram(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), spec=vim.vm.guest.ProcessManager.ProgramSpec()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.FileFault
               return 0

            def listProcesses(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), pids=[ 0 ] or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.ProcessManager.ProcessInfo() ]

            def terminateProcess(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), pid=0):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def readEnvironmentVariable(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), names=[ "" ] or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ "" ]

            class ProgramSpec(vmodl.DynamicData):
               programPath = ""
               arguments = ""
               workingDirectory = ""
               envVariables = [ "" ]

            class WindowsProgramSpec(vim.vm.guest.ProcessManager.ProgramSpec):
               startMinimized = False

            class ProcessInfo(vmodl.DynamicData):
               name = ""
               pid = 0
               owner = ""
               cmdLine = ""
               startTime = vmodl.DateTime()
               endTime = vmodl.DateTime()
               exitCode = 0

         class SAMLTokenAuthentication(vim.vm.guest.GuestAuthentication):
            token = ""
            username = ""

         class SSPIAuthentication(vim.vm.guest.GuestAuthentication):
            sspiToken = ""

         class TicketedSessionAuthentication(vim.vm.guest.GuestAuthentication):
            ticket = ""

         class WindowsRegistryManager(vmodl.ManagedObject):

            def createRegistryKey(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), isVolatile=False, classType="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listRegistryKeys(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), recursive=False, matchPattern="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.WindowsRegistryManager.RegistryKeyRecord() ]

            def deleteRegistryKey(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), recursive=False):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def setRegistryValue(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), value=vim.vm.guest.WindowsRegistryManager.RegistryValue()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            def listRegistryValues(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), keyName=vim.vm.guest.WindowsRegistryManager.RegistryKeyName(), expandStrings=False, matchPattern="" or None):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return [ vim.vm.guest.WindowsRegistryManager.RegistryValue() ]

            def deleteRegistryValue(vm=vim.VirtualMachine(), auth=vim.vm.guest.GuestAuthentication(), valueName=vim.vm.guest.WindowsRegistryManager.RegistryValueName()):
               # throws vim.fault.GuestOperationsFault, vim.fault.InvalidState, vim.fault.TaskInProgress
               return None

            class RegistryKeyName(vmodl.DynamicData):
               registryPath = ""
               wowBitness = ""

               class RegistryKeyWowBitness(Enum):
                  WOWNative = 0
                  WOW32 = 1
                  WOW64 = 2

            class RegistryKey(vmodl.DynamicData):
               keyName = vim.vm.guest.WindowsRegistryManager.RegistryKeyName()
               classType = ""
               lastWritten = vmodl.DateTime()

            class RegistryKeyRecord(vmodl.DynamicData):
               key = vim.vm.guest.WindowsRegistryManager.RegistryKey()
               fault = vmodl.MethodFault()

            class RegistryValueName(vmodl.DynamicData):
               keyName = vim.vm.guest.WindowsRegistryManager.RegistryKeyName()
               name = ""

            class RegistryValueData(vmodl.DynamicData):
               pass

            class RegistryValueDword(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = 0

            class RegistryValueQword(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = 0

            class RegistryValueString(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = ""

            class RegistryValueExpandString(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = ""

            class RegistryValueMultiString(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = [ "" ]

            class RegistryValueBinary(vim.vm.guest.WindowsRegistryManager.RegistryValueData):
               value = vmodl.Binary()

            class RegistryValue(vmodl.DynamicData):
               name = vim.vm.guest.WindowsRegistryManager.RegistryValueName()
               data = vim.vm.guest.WindowsRegistryManager.RegistryValueData()

      class replication(object):

         class DeviceGroupId(vmodl.DynamicData):
            id = ""

         class FaultDomainId(vmodl.DynamicData):
            id = ""

         class ReplicationGroupId(vmodl.DynamicData):
            faultDomainId = vim.vm.replication.FaultDomainId()
            deviceGroupId = vim.vm.replication.DeviceGroupId()

         class ReplicationSpec(vmodl.DynamicData):
            replicationGroupId = vim.vm.replication.ReplicationGroupId()

      class CdromInfo(vim.vm.TargetInfo):
         description = ""

      class ConfigTarget(vmodl.DynamicData):
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

      class DefaultProfileSpec(vim.vm.ProfileSpec):
         pass

      class DefinedProfileSpec(vim.vm.ProfileSpec):
         profileId = ""
         replicationSpec = vim.vm.replication.ReplicationSpec()
         profileData = vim.vm.ProfileRawData()
         profileParams = [ vim.KeyValue() ]

      class DiskDeviceInfo(vim.vm.TargetInfo):
         capacity = 0
         vm = [ vim.VirtualMachine() ]

      class DynamicPassthroughInfo(vim.vm.TargetInfo):
         vendorName = ""
         deviceName = ""
         customLabel = ""
         vendorId = 0
         deviceId = 0

      class EmptyProfileSpec(vim.vm.ProfileSpec):
         pass

      class FloppyInfo(vim.vm.TargetInfo):
         pass

      class IdeDiskDeviceInfo(vim.vm.DiskDeviceInfo):
         partitionTable = [ vim.vm.IdeDiskDeviceInfo.PartitionInfo() ]

         class PartitionInfo(vmodl.DynamicData):
            id = 0
            capacity = 0

      class NetworkInfo(vim.vm.TargetInfo):
         network = vim.Network.Summary()
         vswitch = ""

      class OpaqueNetworkInfo(vim.vm.TargetInfo):
         network = vim.OpaqueNetwork.Summary()
         networkReservationSupported = False

      class ParallelInfo(vim.vm.TargetInfo):
         pass

      class PciPassthroughInfo(vim.vm.TargetInfo):
         pciDevice = vim.host.PciDevice()
         systemId = ""

      class PciSharedGpuPassthroughInfo(vim.vm.TargetInfo):
         vgpu = ""

      class PrecisionClockInfo(vim.vm.TargetInfo):
         systemClockProtocol = ""

      class RelocateSpec(vmodl.DynamicData):
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

         class Transformation(Enum):
            flat = 0
            sparse = 1

         class DiskLocator(vmodl.DynamicData):
            diskId = 0
            datastore = vim.Datastore()
            diskMoveType = ""
            diskBackingInfo = vim.vm.device.VirtualDevice.BackingInfo()
            profile = [ vim.vm.ProfileSpec() ]
            backing = vim.vm.RelocateSpec.DiskLocator.BackingSpec()

            class BackingSpec(vmodl.DynamicData):
               parent = vim.vm.RelocateSpec.DiskLocator.BackingSpec()
               crypto = vim.encryption.CryptoSpec()

         class DiskMoveOptions(Enum):
            moveAllDiskBackingsAndAllowSharing = 0
            moveAllDiskBackingsAndDisallowSharing = 1
            moveChildMostDiskBacking = 2
            createNewChildDiskBacking = 3
            moveAllDiskBackingsAndConsolidate = 4

      class RuntimeInfo(vmodl.DynamicData):
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

         class DasProtectionState(vmodl.DynamicData):
            dasProtected = False

      class ScsiDiskDeviceInfo(vim.vm.DiskDeviceInfo):
         disk = vim.host.ScsiDisk()
         transportHint = ""
         lunNumber = 0

      class ScsiPassthroughInfo(vim.vm.TargetInfo):
         scsiClass = ""
         vendor = ""
         physicalUnitNumber = 0

         class ScsiClass(Enum):
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

      class SerialInfo(vim.vm.TargetInfo):
         pass

      class SgxTargetInfo(vim.vm.TargetInfo):
         maxEpcSize = 0
         flcModes = [ "" ]
         lePubKeyHashes = [ "" ]

      class SnapshotTree(vmodl.DynamicData):
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

      class SoundInfo(vim.vm.TargetInfo):
         pass

      class SriovInfo(vim.vm.PciPassthroughInfo):
         virtualFunction = False
         pnic = ""
         devicePool = vim.vm.SriovDevicePoolInfo()

      class Summary(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         runtime = vim.vm.RuntimeInfo()
         guest = vim.vm.Summary.GuestSummary()
         config = vim.vm.Summary.ConfigSummary()
         storage = vim.vm.Summary.StorageSummary()
         quickStats = vim.vm.Summary.QuickStats()
         overallStatus = vim.ManagedEntity.Status()
         customValue = [ vim.CustomFieldsManager.Value() ]

         class ConfigSummary(vmodl.DynamicData):
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

         class QuickStats(vmodl.DynamicData):
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

         class GuestSummary(vmodl.DynamicData):
            guestId = ""
            guestFullName = ""
            toolsStatus = vim.vm.GuestInfo.ToolsStatus()
            toolsVersionStatus = ""
            toolsVersionStatus2 = ""
            toolsRunningStatus = ""
            hostName = ""
            ipAddress = ""
            hwVersion = ""

         class StorageSummary(vmodl.DynamicData):
            committed = 0
            uncommitted = 0
            unshared = 0
            timestamp = vmodl.DateTime()

      class VFlashModuleInfo(vim.vm.TargetInfo):
         vFlashModule = vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption()

      class VmImportSpec(vim.ImportSpec):
         configSpec = vim.vm.ConfigSpec()
         resPoolEntity = vim.ResourcePool()

      class DatastoreInfo(vim.vm.TargetInfo):
         datastore = vim.Datastore.Summary()
         capability = vim.Datastore.Capability()
         maxFileSize = 0
         maxVirtualDiskCapacity = 0
         maxPhysicalRDMFileSize = 0
         maxVirtualRDMFileSize = 0
         mode = ""
         vStorageSupport = ""

   class vsan(object):

      class cluster(object):

         class ConfigInfo(vmodl.DynamicData):
            enabled = False
            defaultConfig = vim.vsan.cluster.ConfigInfo.HostDefaultInfo()

            class HostDefaultInfo(vmodl.DynamicData):
               uuid = ""
               autoClaimStorage = False
               checksumEnabled = False

      class host(object):

         class ClusterStatus(vmodl.DynamicData):
            uuid = ""
            nodeUuid = ""
            health = ""
            nodeState = vim.vsan.host.ClusterStatus.State()
            memberUuid = [ "" ]

            class State(vmodl.DynamicData):
               state = ""
               completion = vim.vsan.host.ClusterStatus.State.CompletionEstimate()

               class CompletionEstimate(vmodl.DynamicData):
                  completeTime = vmodl.DateTime()
                  percentComplete = 0

         class ConfigInfo(vmodl.DynamicData):
            enabled = False
            hostSystem = vim.HostSystem()
            clusterInfo = vim.vsan.host.ConfigInfo.ClusterInfo()
            storageInfo = vim.vsan.host.ConfigInfo.StorageInfo()
            networkInfo = vim.vsan.host.ConfigInfo.NetworkInfo()
            faultDomainInfo = vim.vsan.host.ConfigInfo.FaultDomainInfo()

            class StorageInfo(vmodl.DynamicData):
               autoClaimStorage = False
               diskMapping = [ vim.vsan.host.DiskMapping() ]
               diskMapInfo = [ vim.vsan.host.DiskMapInfo() ]
               checksumEnabled = False

            class ClusterInfo(vmodl.DynamicData):
               uuid = ""
               nodeUuid = ""

            class NetworkInfo(vmodl.DynamicData):
               port = [ vim.vsan.host.ConfigInfo.NetworkInfo.PortConfig() ]

               class PortConfig(vmodl.DynamicData):
                  ipConfig = vim.vsan.host.IpConfig()
                  device = ""

            class FaultDomainInfo(vmodl.DynamicData):
               name = ""

         class DecommissionMode(vmodl.DynamicData):
            objectAction = ""

            class ObjectAction(Enum):
               noAction = 0
               ensureObjectAccessibility = 1
               evacuateAllData = 2

         class DiskMapInfo(vmodl.DynamicData):
            mapping = vim.vsan.host.DiskMapping()
            mounted = False

         class DiskMapResult(vmodl.DynamicData):
            mapping = vim.vsan.host.DiskMapping()
            diskResult = [ vim.vsan.host.DiskResult() ]
            error = vmodl.MethodFault()

         class DiskMapping(vmodl.DynamicData):
            ssd = vim.host.ScsiDisk()
            nonSsd = [ vim.host.ScsiDisk() ]

         class DiskResult(vmodl.DynamicData):
            disk = vim.host.ScsiDisk()
            state = ""
            vsanUuid = ""
            error = vmodl.MethodFault()
            degraded = False

            class State(Enum):
               inUse = 0
               eligible = 1
               ineligible = 2

         class HealthState(Enum):
            unknown = 0
            healthy = 1
            unhealthy = 2

         class IpConfig(vmodl.DynamicData):
            upstreamIpAddress = ""
            downstreamIpAddress = ""

         class MembershipInfo(vmodl.DynamicData):
            nodeUuid = ""
            hostname = ""

         class NodeState(Enum):
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

         class VsanDiskInfo(vmodl.DynamicData):
            vsanUuid = ""
            formatVersion = 0

         class VsanRuntimeInfo(vmodl.DynamicData):
            membershipList = [ vim.vsan.host.MembershipInfo() ]
            diskIssues = [ vim.vsan.host.VsanRuntimeInfo.DiskIssue() ]
            accessGenNo = 0

            class DiskIssueType(Enum):
               nonExist = 0
               stampMismatch = 1
               unknown = 2

            class DiskIssue(vmodl.DynamicData):
               diskId = ""
               issue = ""

   class vslm(object):

      class BaseConfigInfo(vmodl.DynamicData):
         id = vim.vslm.ID()
         name = ""
         createTime = vmodl.DateTime()
         keepAfterDeleteVm = False
         relocationDisabled = False
         nativeSnapshotSupported = False
         changedBlockTrackingEnabled = False
         backing = vim.vslm.BaseConfigInfo.BackingInfo()
         iofilter = [ "" ]

         class BackingInfo(vmodl.DynamicData):
            datastore = vim.Datastore()

         class FileBackingInfo(vim.vslm.BaseConfigInfo.BackingInfo):
            filePath = ""
            backingObjectId = ""
            parent = vim.vslm.BaseConfigInfo.FileBackingInfo()
            deltaSizeInMB = 0
            keyId = vim.encryption.CryptoKeyId()

         class DiskFileBackingInfo(vim.vslm.BaseConfigInfo.FileBackingInfo):
            provisioningType = ""

            class ProvisioningType(Enum):
               thin = 0
               eagerZeroedThick = 1
               lazyZeroedThick = 2

         class RawDiskMappingBackingInfo(vim.vslm.BaseConfigInfo.FileBackingInfo):
            lunUuid = ""
            compatibilityMode = ""

      class CreateSpec(vmodl.DynamicData):
         name = ""
         keepAfterDeleteVm = False
         backingSpec = vim.vslm.CreateSpec.BackingSpec()
         capacityInMB = 0
         profile = [ vim.vm.ProfileSpec() ]
         crypto = vim.encryption.CryptoSpec()
         metadata = [ vim.KeyValue() ]

         class BackingSpec(vmodl.DynamicData):
            datastore = vim.Datastore()
            path = ""

         class DiskFileBackingSpec(vim.vslm.CreateSpec.BackingSpec):
            provisioningType = ""

         class RawDiskMappingBackingSpec(vim.vslm.CreateSpec.BackingSpec):
            lunUuid = ""
            compatibilityMode = ""

      class DiskCryptoSpec(vmodl.DynamicData):
         parent = vim.vslm.DiskCryptoSpec()
         crypto = vim.encryption.CryptoSpec()

      class ID(vmodl.DynamicData):
         id = ""

      class InfrastructureObjectPolicy(vmodl.DynamicData):
         name = ""
         backingObjectId = ""
         profileId = ""
         error = vmodl.MethodFault()

      class InfrastructureObjectPolicySpec(vmodl.DynamicData):
         datastore = vim.Datastore()
         profile = [ vim.vm.ProfileSpec() ]

      class MigrateSpec(vmodl.DynamicData):
         backingSpec = vim.vslm.CreateSpec.BackingSpec()
         profile = [ vim.vm.ProfileSpec() ]
         consolidate = False
         disksCrypto = vim.vslm.DiskCryptoSpec()

      class RelocateSpec(vim.vslm.MigrateSpec):
         pass

      class StateInfo(vmodl.DynamicData):
         tentative = False

      class TagEntry(vmodl.DynamicData):
         tagName = ""
         parentCategoryName = ""

      class VStorageObject(vmodl.DynamicData):
         config = vim.vslm.VStorageObject.ConfigInfo()

         class ConsumptionType(Enum):
            disk = 0

         class ConfigInfo(vim.vslm.BaseConfigInfo):
            capacityInMB = 0
            consumptionType = [ "" ]
            consumerId = [ vim.vslm.ID() ]

      class VStorageObjectControlFlag(Enum):
         keepAfterDeleteVm = 0
         disableRelocation = 1
         enableChangedBlockTracking = 2

      class VStorageObjectManagerBase(vmodl.ManagedObject):
         pass

      class VStorageObjectSnapshotDetails(vmodl.DynamicData):
         path = ""
         changedBlockTrackingId = ""

      class VStorageObjectSnapshotInfo(vmodl.DynamicData):
         snapshots = [ vim.vslm.VStorageObjectSnapshotInfo.VStorageObjectSnapshot() ]

         class VStorageObjectSnapshot(vmodl.DynamicData):
            id = vim.vslm.ID()
            backingObjectId = ""
            createTime = vmodl.DateTime()
            description = ""

      class vcenter(object):

         class RetrieveVStorageObjSpec(vmodl.DynamicData):
            id = vim.vslm.ID()
            datastore = vim.Datastore()

         class VStorageObjectAssociations(vmodl.DynamicData):
            id = vim.vslm.ID()
            vmDiskAssociations = [ vim.vslm.vcenter.VStorageObjectAssociations.VmDiskAssociations() ]
            fault = vmodl.MethodFault()

            class VmDiskAssociations(vmodl.DynamicData):
               vmId = ""
               diskKey = 0

         class VStorageObjectManager(vim.vslm.VStorageObjectManagerBase):

            def createDisk(spec=vim.vslm.CreateSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore
               return vim.Task()

            def registerDisk(path="", name="" or None):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.AlreadyExists
               return vim.vslm.VStorageObject()

            def extendDisk(id=vim.vslm.ID(), datastore=vim.Datastore(), newCapacityInMB=0):
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def inflateDisk(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def renameVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), name=""):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def updateVStorageObjectPolicy(id=vim.vslm.ID(), datastore=vim.Datastore(), profile=[ vim.vm.ProfileSpec() ] or None):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def updateVStorageObjectCrypto(id=vim.vslm.ID(), datastore=vim.Datastore(), profile=[ vim.vm.ProfileSpec() ] or None, disksCrypto=vim.vslm.DiskCryptoSpec() or None):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def updateVStorageInfrastructureObjectPolicy(spec=vim.vslm.InfrastructureObjectPolicySpec()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageInfrastructureObjectPolicy(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState
               return [ vim.vslm.InfrastructureObjectPolicy() ]

            def deleteVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.VStorageObject()

            def retrieveVStorageObjectState(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.StateInfo()

            def retrieveVStorageObjectAssociations(ids=[ vim.vslm.vcenter.RetrieveVStorageObjSpec() ] or None):
               return [ vim.vslm.vcenter.VStorageObjectAssociations() ]

            def listVStorageObject(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore
               return [ vim.vslm.ID() ]

            def cloneVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.CloneSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def relocateVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.RelocateSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def setVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def clearVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def attachTagToVStorageObject(id=vim.vslm.ID(), category="", tag=""):
               # throws vim.fault.NotFound
               return None

            def detachTagFromVStorageObject(id=vim.vslm.ID(), category="", tag=""):
               # throws vim.fault.NotFound
               return None

            def listVStorageObjectsAttachedToTag(category="", tag=""):
               # throws vim.fault.NotFound
               return [ vim.vslm.ID() ]

            def listTagsAttachedToVStorageObject(id=vim.vslm.ID()):
               # throws vim.fault.NotFound
               return [ vim.vslm.TagEntry() ]

            def reconcileDatastoreInventory(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def scheduleReconcileDatastoreInventory(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def createSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), description=""):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def deleteSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotInfo(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotInfo()

            def createDiskFromSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), name="", profile=[ vim.vm.ProfileSpec() ] or None, crypto=vim.encryption.CryptoSpec() or None, path="" or None):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def RevertVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotDetails(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotDetails()

            def queryChangedDiskAreas(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), startOffset=0, changeId=""):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState, vmodl.fault.InvalidArgument
               return vim.VirtualMachine.DiskChangeInfo()

      class CloneSpec(vim.vslm.MigrateSpec):
         name = ""
         keepAfterDeleteVm = False
         metadata = [ vim.KeyValue() ]

      class host(object):

         class VStorageObjectManager(vim.vslm.VStorageObjectManagerBase):

            def createDisk(spec=vim.vslm.CreateSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore
               return vim.Task()

            def registerDisk(path="", name="" or None):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.AlreadyExists
               return vim.vslm.VStorageObject()

            def extendDisk(id=vim.vslm.ID(), datastore=vim.Datastore(), newCapacityInMB=0):
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def inflateDisk(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.NotFound, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.TaskInProgress
               return vim.Task()

            def renameVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), name=""):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def retrieveVStorageInfrastructureObjectPolicy(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidState
               return [ vim.vslm.InfrastructureObjectPolicy() ]

            def deleteVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.TaskInProgress
               return vim.Task()

            def retrieveVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.VStorageObject()

            def retrieveVStorageObjectState(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.vslm.StateInfo()

            def listVStorageObject(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore
               return [ vim.vslm.ID() ]

            def cloneVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.CloneSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def relocateVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), spec=vim.vslm.RelocateSpec()):
               # throws vim.fault.FileFault, vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def setVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def clearVStorageObjectControlFlags(id=vim.vslm.ID(), datastore=vim.Datastore(), controlFlags=[ "" ] or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return None

            def reconcileDatastoreInventory(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return vim.Task()

            def scheduleReconcileDatastoreInventory(datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound
               return None

            def createSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), description=""):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def deleteSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def retrieveSnapshotInfo(id=vim.vslm.ID(), datastore=vim.Datastore()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.vslm.VStorageObjectSnapshotInfo()

            def createDiskFromSnapshot(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID(), name="", profile=[ vim.vm.ProfileSpec() ] or None, crypto=vim.encryption.CryptoSpec() or None, path="" or None):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def RevertVStorageObject(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID()):
               # throws vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.FileFault, vim.fault.InvalidState
               return vim.Task()

            def updateVStorageObjectMetadata(id=vim.vslm.ID(), datastore=vim.Datastore(), metadata=[ vim.KeyValue() ] or None, deleteKeys=[ "" ] or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return vim.Task()

            def retrieveVStorageObjectMetadata(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID() or None, prefix="" or None):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound
               return [ vim.KeyValue() ]

            def retrieveVStorageObjectMetadataValue(id=vim.vslm.ID(), datastore=vim.Datastore(), snapshotId=vim.vslm.ID() or None, key=""):
               # throws vim.fault.InvalidDatastore, vim.fault.InvalidState, vim.fault.NotFound, vim.fault.KeyNotFound
               return ""

   class AuthorizationManager(vmodl.ManagedObject):
      privilegeList = [ vim.AuthorizationManager.Privilege() ]
      roleList = [ vim.AuthorizationManager.Role() ]
      description = vim.AuthorizationDescription()

      def addRole(name="", privIds=[ "" ] or None):
         # throws vim.fault.AlreadyExists, vim.fault.InvalidName
         return 0

      def removeRole(roleId=0, failIfUsed=False):
         # throws vim.fault.NotFound, vim.fault.RemoveFailed
         return None

      def updateRole(roleId=0, newName="", privIds=[ "" ] or None):
         # throws vim.fault.NotFound, vim.fault.InvalidName, vim.fault.AlreadyExists
         return None

      def mergePermissions(srcRoleId=0, dstRoleId=0):
         # throws vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def retrieveRolePermissions(roleId=0):
         # throws vim.fault.NotFound
         return [ vim.AuthorizationManager.Permission() ]

      def retrieveEntityPermissions(entity=vim.ManagedEntity(), inherited=False):
         return [ vim.AuthorizationManager.Permission() ]

      def retrieveAllPermissions():
         return [ vim.AuthorizationManager.Permission() ]

      def setEntityPermissions(entity=vim.ManagedEntity(), permission=[ vim.AuthorizationManager.Permission() ] or None):
         # throws vim.fault.UserNotFound, vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def resetEntityPermissions(entity=vim.ManagedEntity(), permission=[ vim.AuthorizationManager.Permission() ] or None):
         # throws vim.fault.UserNotFound, vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def removeEntityPermission(entity=vim.ManagedEntity(), user="", isGroup=False):
         # throws vim.fault.NotFound, vim.fault.AuthMinimumAdminPermission
         return None

      def hasPrivilegeOnEntity(entity=vim.ManagedEntity(), sessionId="", privId=[ "" ] or None):
         return [ False ]

      def hasPrivilegeOnEntities(entity=[ vim.ManagedEntity() ], sessionId="", privId=[ "" ] or None):
         return [ vim.AuthorizationManager.EntityPrivilege() ]

      def hasUserPrivilegeOnEntities(entities=[ vmodl.ManagedObject() ], userName="", privId=[ "" ] or None):
         return [ vim.AuthorizationManager.EntityPrivilege() ]

      def fetchUserPrivilegeOnEntities(entities=[ vim.ManagedEntity() ], userName=""):
         return [ vim.AuthorizationManager.UserPrivilegeResult() ]

      class Permission(vmodl.DynamicData):
         entity = vim.ManagedEntity()
         principal = ""
         group = False
         roleId = 0
         propagate = False

      class Role(vmodl.DynamicData):
         roleId = 0
         system = False
         name = ""
         info = vim.Description()
         privilege = [ "" ]

      class Privilege(vmodl.DynamicData):
         privId = ""
         onParent = False
         name = ""
         privGroupName = ""

      class PrivilegeAvailability(vmodl.DynamicData):
         privId = ""
         isGranted = False

      class EntityPrivilege(vmodl.DynamicData):
         entity = vim.ManagedEntity()
         privAvailability = [ vim.AuthorizationManager.PrivilegeAvailability() ]

      class UserPrivilegeResult(vmodl.DynamicData):
         entity = vim.ManagedEntity()
         privileges = [ "" ]

   class BoolPolicy(vim.InheritablePolicy):
      value = False

   class EVCMode(vim.ElementDescription):
      guaranteedCPUFeatures = [ vim.host.CpuIdInfo() ]
      featureCapability = [ vim.host.FeatureCapability() ]
      featureMask = [ vim.host.FeatureMask() ]
      featureRequirement = [ vim.vm.FeatureRequirement() ]
      vendor = ""
      track = [ "" ]
      vendorTier = 0

   class ImportSpec(vmodl.DynamicData):
      entityConfig = vim.vApp.EntityConfigInfo()
      instantiationOst = vim.OvfConsumer.OstNode()

   class IntExpression(vim.NegatableExpression):
      value = 0

   class IpAddress(vim.NegatableExpression):
      pass

   class IpRange(vim.IpAddress):
      addressPrefix = ""
      prefixLength = 0

   class LicenseAssignmentManager(vmodl.ManagedObject):

      def updateAssignedLicense(entity="", licenseKey="", entityDisplayName="" or None):
         # throws vim.fault.LicenseEntityNotFound
         return vim.LicenseManager.LicenseInfo()

      def removeAssignedLicense(entityId=""):
         # throws vim.fault.LicenseEntityNotFound
         return None

      def queryAssignedLicenses(entityId="" or None):
         return [ vim.LicenseAssignmentManager.LicenseAssignment() ]

      class LicenseAssignment(vmodl.DynamicData):
         entityId = ""
         scope = ""
         entityDisplayName = ""
         assignedLicense = vim.LicenseManager.LicenseInfo()
         properties = [ vmodl.KeyAnyValue() ]

   class MacAddress(vim.NegatableExpression):
      pass

   class MacRange(vim.MacAddress):
      address = ""
      mask = ""

   class ManagedEntity(vim.ExtensibleManagedObject):
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

      def reload():
         return None

      def rename(newName=""):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def destroy():
         # throws vim.fault.VimFault
         return vim.Task()

      class Status(Enum):
         gray = 0
         green = 1
         yellow = 2
         red = 3

   class Network(vim.ManagedEntity):
      summary = vim.Network.Summary()
      host = [ vim.HostSystem() ]
      vm = [ vim.VirtualMachine() ]

      def destroyNetwork():
         # throws vim.fault.ResourceInUse
         return None

      class Summary(vmodl.DynamicData):
         network = vim.Network()
         name = ""
         accessible = False
         ipPoolName = ""
         ipPoolId = 0

   class OpaqueNetwork(vim.Network):
      capability = vim.OpaqueNetwork.Capability()
      extraConfig = [ vim.option.OptionValue() ]

      class Summary(vim.Network.Summary):
         opaqueNetworkId = ""
         opaqueNetworkType = ""

      class Capability(vmodl.DynamicData):
         networkReservationSupported = False

   class PosixUserSearchResult(vim.UserSearchResult):
      id = 0
      shellAccess = False

   class ResourcePool(vim.ManagedEntity):
      summary = vim.ResourcePool.Summary()
      runtime = vim.ResourcePool.RuntimeInfo()
      owner = vim.ComputeResource()
      resourcePool = [ vim.ResourcePool() ]
      vm = [ vim.VirtualMachine() ]
      config = vim.ResourceConfigSpec()
      namespace = ""
      childConfiguration = [ vim.ResourceConfigSpec() ]

      def updateConfig(name="" or None, config=vim.ResourceConfigSpec() or None):
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault, vim.fault.ConcurrentAccess
         return None

      def moveInto(list=[ vim.ManagedEntity() ]):
         # throws vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault
         return None

      def updateChildResourceConfiguration(spec=[ vim.ResourceConfigSpec() ]):
         # throws vim.fault.InvalidState, vim.fault.InsufficientResourcesFault
         return None

      def createResourcePool(name="", spec=vim.ResourceConfigSpec()):
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault
         return vim.ResourcePool()

      def destroyChildren():
         return None

      def createVApp(name="", resSpec=vim.ResourceConfigSpec(), configSpec=vim.vApp.VAppConfigSpec(), vmFolder=vim.Folder() or None):
         # throws vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.VirtualApp()

      def createVm(config=vim.vm.ConfigSpec(), host=vim.HostSystem() or None):
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def registerVm(path="", name="" or None, host=vim.HostSystem() or None):
         # throws vim.fault.OutOfBounds, vim.fault.AlreadyExists, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.VmConfigFault, vim.fault.InsufficientResourcesFault, vim.fault.FileFault
         return vim.Task()

      def importVApp(spec=vim.ImportSpec(), folder=vim.Folder() or None, host=vim.HostSystem() or None):
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault
         return vim.HttpNfcLease()

      def queryResourceConfigOption():
         return vim.ResourceConfigOption()

      def refreshRuntime():
         return None

      class ResourceUsage(vmodl.DynamicData):
         reservationUsed = 0
         reservationUsedForVm = 0
         unreservedForPool = 0
         unreservedForVm = 0
         overallUsage = 0
         maxUsage = 0

      class RuntimeInfo(vmodl.DynamicData):
         memory = vim.ResourcePool.ResourceUsage()
         cpu = vim.ResourcePool.ResourceUsage()
         overallStatus = vim.ManagedEntity.Status()
         sharesScalable = ""

      class Summary(vmodl.DynamicData):
         name = ""
         config = vim.ResourceConfigSpec()
         runtime = vim.ResourcePool.RuntimeInfo()
         quickStats = vim.ResourcePool.Summary.QuickStats()
         configuredMemoryMB = 0

         class QuickStats(vmodl.DynamicData):
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

   class SingleIp(vim.IpAddress):
      address = ""

   class SingleMac(vim.MacAddress):
      address = ""

   class Task(vim.ExtensibleManagedObject):
      info = vim.TaskInfo()

      def cancel():
         # throws vim.fault.InvalidState
         return None

      def UpdateProgress(percentDone=0):
         # throws vim.fault.InvalidState, vim.fault.OutOfBounds
         return None

      def setState(state=vim.TaskInfo.State(), result=anyType() or None, fault=vmodl.MethodFault() or None):
         # throws vim.fault.InvalidState
         return None

      def UpdateDescription(description=vmodl.LocalizableMessage()):
         return None

   class TaskFilterSpec(vmodl.DynamicData):
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

      class RecursionOption(Enum):
         self = 0
         children = 1
         all = 2

      class TimeOption(Enum):
         queuedTime = 0
         startedTime = 1
         completedTime = 2

      class ByEntity(vmodl.DynamicData):
         entity = vim.ManagedEntity()
         recursion = vim.TaskFilterSpec.RecursionOption()

      class ByTime(vmodl.DynamicData):
         timeType = vim.TaskFilterSpec.TimeOption()
         beginTime = vmodl.DateTime()
         endTime = vmodl.DateTime()

      class ByUsername(vmodl.DynamicData):
         systemUser = False
         userList = [ "" ]

   class VirtualApp(vim.ResourcePool):
      parentFolder = vim.Folder()
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      vAppConfig = vim.vApp.VAppConfigInfo()
      parentVApp = vim.ManagedEntity()
      childLink = [ vim.VirtualApp.LinkInfo() ]

      def updateVAppConfig(spec=vim.vApp.VAppConfigSpec()):
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.InvalidDatastore
         return None

      def updateLinkedChildren(addChangeSet=[ vim.VirtualApp.LinkInfo() ] or None, removeSet=[ vim.ManagedEntity() ] or None):
         # throws vim.fault.ConcurrentAccess
         return None

      def clone(name="", target=vim.ResourcePool(), spec=vim.vApp.CloneSpec()):
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.MigrationFault, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def exportVApp():
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
         return vim.HttpNfcLease()

      def powerOn():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmConfigFault, vim.fault.VAppConfigFault, vim.fault.FileFault
         return vim.Task()

      def powerOff(force=False):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.VAppConfigFault
         return vim.Task()

      def suspend():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.VAppConfigFault
         return vim.Task()

      def unregister():
         # throws vim.fault.ConcurrentAccess, vim.fault.InvalidState
         return vim.Task()

      class VAppState(Enum):
         started = 0
         stopped = 1
         starting = 2
         stopping = 3

      class Summary(vim.ResourcePool.Summary):
         product = vim.vApp.ProductInfo()
         vAppState = vim.VirtualApp.VAppState()
         suspended = False
         installBootRequired = False
         instanceUuid = ""

      class LinkInfo(vmodl.DynamicData):
         key = vim.ManagedEntity()
         destroyWithParent = False

   class VirtualDiskManager(vmodl.ManagedObject):

      def createVirtualDisk(name="", datacenter=vim.Datacenter() or None, spec=vim.VirtualDiskManager.VirtualDiskSpec()):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def deleteVirtualDisk(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def moveVirtualDisk(sourceName="", sourceDatacenter=vim.Datacenter() or None, destName="", destDatacenter=vim.Datacenter() or None, force=False or None, profile=[ vim.vm.ProfileSpec() ] or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def copyVirtualDisk(sourceName="", sourceDatacenter=vim.Datacenter() or None, destName="", destDatacenter=vim.Datacenter() or None, destSpec=vim.VirtualDiskManager.VirtualDiskSpec() or None, force=False or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDiskFormat, vim.fault.InvalidDatastore
         return vim.Task()

      def extendVirtualDisk(name="", datacenter=vim.Datacenter() or None, newCapacityKb=0, eagerZero=False or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def queryVirtualDiskFragmentation(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return 0

      def defragmentVirtualDisk(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def shrinkVirtualDisk(name="", datacenter=vim.Datacenter() or None, copy=False or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def inflateVirtualDisk(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def eagerZeroVirtualDisk(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def zeroFillVirtualDisk(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.Task()

      def setVirtualDiskUuid(name="", datacenter=vim.Datacenter() or None, uuid=""):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return None

      def queryVirtualDiskUuid(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return ""

      def queryVirtualDiskGeometry(name="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.FileFault, vim.fault.InvalidDatastore
         return vim.host.DiskDimensions.Chs()

      def importUnmanagedSnapshot(vdisk="", datacenter=vim.Datacenter() or None, vvolId=""):
         # throws vim.fault.NotFound, vim.fault.InvalidDatastore
         return None

      def releaseManagedSnapshot(vdisk="", datacenter=vim.Datacenter() or None):
         # throws vim.fault.InvalidDatastore, vim.fault.FileNotFound
         return None

      class VirtualDiskType(Enum):
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

      class VirtualDiskAdapterType(Enum):
         ide = 0
         busLogic = 1
         lsiLogic = 2

      class VirtualDiskSpec(vmodl.DynamicData):
         diskType = ""
         adapterType = ""

      class FileBackedVirtualDiskSpec(vim.VirtualDiskManager.VirtualDiskSpec):
         capacityKb = 0
         profile = [ vim.vm.ProfileSpec() ]
         crypto = vim.encryption.CryptoSpec()

      class SeSparseVirtualDiskSpec(vim.VirtualDiskManager.FileBackedVirtualDiskSpec):
         grainSizeKb = 0

      class DeviceBackedVirtualDiskSpec(vim.VirtualDiskManager.VirtualDiskSpec):
         device = ""

   class VirtualMachine(vim.ManagedEntity):
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

      def refreshStorageInfo():
         return None

      def createSnapshot(name="", description="" or None, memory=False, quiesce=False):
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.InvalidState
         return vim.Task()

      def createSnapshotEx(name="", description="" or None, memory=False, quiesceSpec=vim.vm.GuestQuiesceSpec() or None):
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.InvalidState
         return vim.Task()

      def revertToCurrentSnapshot(host=vim.HostSystem() or None, suppressPowerOn=False or None):
         # throws vim.fault.TaskInProgress, vim.fault.SnapshotFault, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.NotFound
         return vim.Task()

      def removeAllSnapshots(consolidate=False or None):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.SnapshotFault
         return vim.Task()

      def consolidateDisks():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def estimateStorageRequirementForConsolidate():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def reconfigure(spec=vim.vm.ConfigSpec()):
         # throws vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.ConcurrentAccess, vim.fault.FileFault, vim.fault.InvalidName, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.InvalidDatastore
         return vim.Task()

      def upgradeVirtualHardware(version="" or None):
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.AlreadyUpgraded, vim.fault.NoDiskFound
         return vim.Task()

      def extractOvfEnvironment():
         # throws vim.fault.InvalidState
         return ""

      def powerOn(host=vim.HostSystem() or None):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmConfigFault, vim.fault.FileFault
         return vim.Task()

      def powerOff():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def suspend():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def reset():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState
         return vim.Task()

      def shutdownGuest():
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def rebootGuest():
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def standbyGuest():
         # throws vim.fault.ToolsUnavailable, vim.fault.TaskInProgress, vim.fault.InvalidState
         return None

      def answer(questionId="", answerChoice=""):
         # throws vim.fault.ConcurrentAccess
         return None

      def customize(spec=vim.vm.customization.Specification()):
         # throws vim.fault.CustomizationFault
         return vim.Task()

      def checkCustomizationSpec(spec=vim.vm.customization.Specification()):
         # throws vim.fault.CustomizationFault
         return None

      def migrate(pool=vim.ResourcePool() or None, host=vim.HostSystem() or None, priority=vim.VirtualMachine.MovePriority(), state=vim.VirtualMachine.PowerState() or None):
         # throws vim.fault.MigrationFault, vim.fault.FileFault, vim.fault.Timedout, vim.fault.InsufficientResourcesFault, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.Task()

      def relocate(spec=vim.vm.RelocateSpec(), priority=vim.VirtualMachine.MovePriority() or None):
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.MigrationFault, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.Timedout, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def clone(folder=vim.Folder(), name="", spec=vim.vm.CloneSpec()):
         # throws vim.fault.CustomizationFault, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.TaskInProgress, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.MigrationFault, vim.fault.InsufficientResourcesFault
         return vim.Task()

      def instantClone(spec=vim.vm.InstantCloneSpec()):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault, vim.fault.DisallowedMigrationDeviceAttached, vim.fault.FileFault
         return vim.Task()

      def exportVm():
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.FileFault
         return vim.HttpNfcLease()

      def markAsTemplate():
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.FileFault
         return None

      def markAsVirtualMachine(pool=vim.ResourcePool(), host=vim.HostSystem() or None):
         # throws vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.VmConfigFault, vim.fault.FileFault
         return None

      def unregister():
         # throws vim.fault.TaskInProgress, vim.fault.InvalidPowerState
         return None

      def resetGuestInformation():
         # throws vim.fault.InvalidState
         return None

      def mountToolsInstaller():
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.VmToolsUpgradeFault
         return None

      def unmountToolsInstaller():
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return None

      def upgradeTools(installerOptions="" or None):
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress, vim.fault.VmToolsUpgradeFault, vim.fault.ToolsUnavailable, vim.fault.VmConfigFault
         return vim.Task()

      def acquireMksTicket():
         return vim.VirtualMachine.MksTicket()

      def acquireTicket(ticketType=""):
         # throws vim.fault.InvalidState
         return vim.VirtualMachine.Ticket()

      def setScreenResolution(width=0, height=0):
         # throws vim.fault.InvalidState, vim.fault.ToolsUnavailable
         return None

      def defragmentAllDisks():
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault
         return None

      def createSecondary(host=vim.HostSystem() or None):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmFaultToleranceIssue, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def createSecondaryEx(host=vim.HostSystem() or None, spec=vim.vm.FaultToleranceConfigSpec() or None):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.InsufficientResourcesFault, vim.fault.VmFaultToleranceIssue, vim.fault.FileFault, vim.fault.VmConfigFault
         return vim.Task()

      def turnOffFaultTolerance():
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def makePrimary(vm=vim.VirtualMachine()):
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def terminateFaultTolerantVM(vm=vim.VirtualMachine() or None):
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def disableSecondary(vm=vim.VirtualMachine()):
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState
         return vim.Task()

      def enableSecondary(vm=vim.VirtualMachine(), host=vim.HostSystem() or None):
         # throws vim.fault.TaskInProgress, vim.fault.VmFaultToleranceIssue, vim.fault.InvalidState, vim.fault.VmConfigFault
         return vim.Task()

      def setDisplayTopology(displays=[ vim.VirtualMachine.DisplayTopology() ]):
         # throws vim.fault.InvalidState, vim.fault.ToolsUnavailable
         return None

      def startRecording(name="", description="" or None):
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault, vim.fault.VmConfigFault, vim.fault.RecordReplayDisabled, vim.fault.HostIncompatibleForRecordReplay, vim.fault.InvalidName
         return vim.Task()

      def stopRecording():
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault
         return vim.Task()

      def startReplaying(replaySnapshot=vim.vm.Snapshot()):
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault, vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.RecordReplayDisabled, vim.fault.HostIncompatibleForRecordReplay
         return vim.Task()

      def stopReplaying():
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.SnapshotFault
         return vim.Task()

      def promoteDisks(unlink=False, disks=[ vim.vm.device.VirtualDisk() ] or None):
         # throws vim.fault.InvalidState, vim.fault.InvalidPowerState, vim.fault.TaskInProgress
         return vim.Task()

      def createScreenshot():
         # throws vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def putUsbScanCodes(spec=vim.vm.UsbScanCodeSpec()):
         return 0

      def queryChangedDiskAreas(snapshot=vim.vm.Snapshot() or None, deviceKey=0, startOffset=0, changeId=""):
         # throws vim.fault.FileFault, vim.fault.NotFound
         return vim.VirtualMachine.DiskChangeInfo()

      def queryUnownedFiles():
         return [ "" ]

      def reloadFromPath(configurationPath=""):
         # throws vim.fault.InvalidPowerState, vim.fault.TaskInProgress, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.VmConfigFault, vim.fault.AlreadyExists
         return vim.Task()

      def queryFaultToleranceCompatibility():
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return [ vmodl.MethodFault() ]

      def queryFaultToleranceCompatibilityEx(forLegacyFt=False or None):
         # throws vim.fault.InvalidState, vim.fault.VmConfigFault
         return [ vmodl.MethodFault() ]

      def terminate():
         # throws vim.fault.InvalidState, vim.fault.TaskInProgress
         return None

      def sendNMI():
         # throws vim.fault.InvalidState
         return None

      def attachDisk(diskId=vim.vslm.ID(), datastore=vim.Datastore(), controllerKey=0 or None, unitNumber=0 or None):
         # throws vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidState, vim.fault.InvalidDatastore, vim.fault.InvalidController, vim.fault.MissingController, vim.fault.DeviceUnsupportedForVmVersion
         return vim.Task()

      def detachDisk(diskId=vim.vslm.ID()):
         # throws vim.fault.NotFound, vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def applyEvcMode(mask=[ vim.host.FeatureMask() ] or None, completeMasks=False or None):
         # throws vim.fault.InvalidState
         return vim.Task()

      def cryptoUnlock():
         # throws vim.fault.InvalidState, vmodl.fault.NotSupported
         return vim.Task()

      class StorageRequirement(vmodl.DynamicData):
         datastore = vim.Datastore()
         freeSpaceRequiredInKb = 0

      class PowerState(Enum):
         poweredOff = 0
         poweredOn = 1
         suspended = 2

      class AppHeartbeatStatusType(Enum):
         appStatusGray = 0
         appStatusGreen = 1
         appStatusRed = 2

      class ConnectionState(Enum):
         connected = 0
         disconnected = 1
         orphaned = 2
         inaccessible = 3
         invalid = 4

      class CryptoState(Enum):
         unlocked = 0
         locked = 1

      class MovePriority(Enum):
         lowPriority = 0
         highPriority = 1
         defaultPriority = 2

      class Ticket(vmodl.DynamicData):
         ticket = ""
         cfgFile = ""
         host = ""
         port = 0
         sslThumbprint = ""
         url = ""

      class MksTicket(vmodl.DynamicData):
         ticket = ""
         cfgFile = ""
         host = ""
         port = 0
         sslThumbprint = ""

      class FaultToleranceState(Enum):
         notConfigured = 0
         disabled = 1
         enabled = 2
         needSecondary = 3
         starting = 4
         running = 5

      class RecordReplayState(Enum):
         recording = 0
         replaying = 1
         inactive = 2

      class NeedSecondaryReason(Enum):
         initializing = 0
         divergence = 1
         lostConnection = 2
         partialHardwareFailure = 3
         userAction = 4
         checkpointError = 5
         other = 6

      class FaultToleranceType(Enum):
         unset = 0
         recordReplay = 1
         checkpointing = 2

      class TicketType(Enum):
         mks = 0
         device = 1
         guestControl = 2
         dnd = 3
         webmks = 4
         guestIntegrity = 5
         webRemoteDevice = 6

      class DisplayTopology(vmodl.DynamicData):
         x = 0
         y = 0
         width = 0
         height = 0

      class DiskChangeInfo(vmodl.DynamicData):
         startOffset = 0
         length = 0
         changedArea = [ vim.VirtualMachine.DiskChangeInfo.DiskChangeExtent() ]

         class DiskChangeExtent(vmodl.DynamicData):
            start = 0
            length = 0

      class WipeResult(vmodl.DynamicData):
         diskId = 0
         shrinkableDiskSpace = 0

   class ComputeResource(vim.ManagedEntity):
      resourcePool = vim.ResourcePool()
      host = [ vim.HostSystem() ]
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      summary = vim.ComputeResource.Summary()
      environmentBrowser = vim.EnvironmentBrowser()
      configurationEx = vim.ComputeResource.ConfigInfo()
      lifecycleManaged = False

      def reconfigureEx(spec=vim.ComputeResource.ConfigSpec(), modify=False):
         return vim.Task()

      class Summary(vmodl.DynamicData):
         totalCpu = 0
         totalMemory = 0
         numCpuCores = 0
         numCpuThreads = 0
         effectiveCpu = 0
         effectiveMemory = 0
         numHosts = 0
         numEffectiveHosts = 0
         overallStatus = vim.ManagedEntity.Status()

      class ConfigInfo(vmodl.DynamicData):
         vmSwapPlacement = ""
         spbmEnabled = False
         defaultHardwareVersionKey = ""

      class HostSPBMLicenseInfo(vmodl.DynamicData):
         host = vim.HostSystem()
         licenseState = vim.ComputeResource.HostSPBMLicenseInfo.HostSPBMLicenseState()

         class HostSPBMLicenseState(Enum):
            licensed = 0
            unlicensed = 1
            unknown = 2

      class ConfigSpec(vmodl.DynamicData):
         vmSwapPlacement = ""
         spbmEnabled = False
         defaultHardwareVersionKey = ""
         desiredSoftwareSpec = vim.DesiredSoftwareSpec()

   class Datastore(vim.ManagedEntity):
      info = vim.Datastore.Info()
      summary = vim.Datastore.Summary()
      host = [ vim.Datastore.HostMount() ]
      vm = [ vim.VirtualMachine() ]
      browser = vim.host.DatastoreBrowser()
      capability = vim.Datastore.Capability()
      iormConfiguration = vim.StorageResourceManager.IORMConfigInfo()

      def refresh():
         # throws vim.fault.NotFound, vim.fault.HostConfigFault
         return None

      def refreshStorageInfo():
         return None

      def updateVirtualMachineFiles(mountPathDatastoreMapping=[ vim.Datastore.MountPathDatastorePair() ]):
         # throws vim.fault.ResourceInUse, vim.fault.PlatformConfigFault, vim.fault.TaskInProgress, vim.fault.InvalidDatastore
         return vim.Task()

      def renameDatastore(newName=""):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return None

      def destroyDatastore():
         # throws vim.fault.ResourceInUse
         return None

      def enterMaintenanceMode():
         # throws vim.fault.InvalidState
         return vim.storageDrs.StoragePlacementResult()

      def exitMaintenanceMode():
         # throws vim.fault.InvalidState
         return vim.Task()

      def updateVVolVirtualMachineFiles(failoverPair=[ vim.Datastore.VVolContainerFailoverPair() ] or None):
         # throws vmodl.fault.NotSupported, vim.fault.PlatformConfigFault, vim.fault.TaskInProgress, vim.fault.InvalidDatastore
         return vim.Task()

      class Accessible(Enum):
         True = 0
         False = 1

      class Summary(vmodl.DynamicData):
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

         class MaintenanceModeState(Enum):
            normal = 0
            enteringMaintenance = 1
            inMaintenance = 2

      class Info(vmodl.DynamicData):
         name = ""
         url = ""
         freeSpace = 0
         maxFileSize = 0
         maxVirtualDiskCapacity = 0
         maxMemoryFileSize = 0
         timestamp = vmodl.DateTime()
         containerId = ""
         aliasOf = ""

      class Capability(vmodl.DynamicData):
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

      class HostMount(vmodl.DynamicData):
         key = vim.HostSystem()
         mountInfo = vim.host.MountInfo()

      class MountPathDatastorePair(vmodl.DynamicData):
         oldMountPath = ""
         datastore = vim.Datastore()

      class VVolContainerFailoverPair(vmodl.DynamicData):
         srcContainer = ""
         tgtContainer = ""
         vvolMapping = [ vim.KeyValue() ]

   class DistributedVirtualSwitch(vim.ManagedEntity):
      uuid = ""
      capability = vim.DistributedVirtualSwitch.Capability()
      summary = vim.DistributedVirtualSwitch.Summary()
      config = vim.DistributedVirtualSwitch.ConfigInfo()
      networkResourcePool = [ vim.dvs.NetworkResourcePool() ]
      portgroup = [ vim.dvs.DistributedVirtualPortgroup() ]
      runtime = vim.DistributedVirtualSwitch.RuntimeInfo()

      def fetchPortKeys(criteria=vim.dvs.PortCriteria() or None):
         return [ "" ]

      def fetchPorts(criteria=vim.dvs.PortCriteria() or None):
         return [ vim.dvs.DistributedVirtualPort() ]

      def queryUsedVlanId():
         return [ 0 ]

      def reconfigure(spec=vim.DistributedVirtualSwitch.ConfigSpec()):
         # throws vim.fault.DvsFault, vim.fault.ConcurrentAccess, vim.fault.DuplicateName, vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.NotFound, vim.fault.AlreadyExists, vim.fault.LimitExceeded, vim.fault.ResourceInUse, vim.fault.ResourceNotAvailable, vim.fault.DvsNotAuthorized
         return vim.Task()

      def performProductSpecOperation(operation="", productSpec=vim.dvs.ProductSpec() or None):
         # throws vim.fault.TaskInProgress, vim.fault.InvalidState, vim.fault.DvsFault
         return vim.Task()

      def merge(dvs=vim.DistributedVirtualSwitch()):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.InvalidHostState
         return vim.Task()

      def addPortgroups(spec=[ vim.dvs.DistributedVirtualPortgroup.ConfigSpec() ]):
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def movePort(portKey=[ "" ], destinationPortgroupKey="" or None):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ConcurrentAccess
         return vim.Task()

      def updateCapability(capability=vim.DistributedVirtualSwitch.Capability()):
         # throws vim.fault.DvsFault
         return None

      def reconfigurePort(port=[ vim.dvs.DistributedVirtualPort.ConfigSpec() ]):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.ResourceInUse, vim.fault.ConcurrentAccess
         return vim.Task()

      def refreshPortState(portKeys=[ "" ] or None):
         # throws vim.fault.DvsFault, vim.fault.NotFound
         return None

      def rectifyHost(hosts=[ vim.HostSystem() ] or None):
         # throws vim.fault.DvsFault, vim.fault.NotFound
         return vim.Task()

      def updateNetworkResourcePool(configSpec=[ vim.dvs.NetworkResourcePool.ConfigSpec() ]):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ConcurrentAccess
         return None

      def addNetworkResourcePool(configSpec=[ vim.dvs.NetworkResourcePool.ConfigSpec() ]):
         # throws vim.fault.DvsFault, vim.fault.InvalidName
         return None

      def removeNetworkResourcePool(key=[ "" ]):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ResourceInUse
         return None

      def reconfigureVmVnicNetworkResourcePool(configSpec=[ vim.dvs.VmVnicNetworkResourcePool.ConfigSpec() ]):
         # throws vim.fault.DvsFault, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.ConcurrentAccess, vim.fault.ConflictingConfiguration, vim.fault.ResourceInUse
         return vim.Task()

      def enableNetworkResourceManagement(enable=False):
         # throws vim.fault.DvsFault
         return None

      def rollback(entityBackup=vim.dvs.EntityBackup.Config() or None):
         # throws vim.fault.DvsFault, vim.fault.RollbackFailure
         return vim.Task()

      def addPortgroup(spec=vim.dvs.DistributedVirtualPortgroup.ConfigSpec()):
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Task()

      def updateHealthCheckConfig(healthCheckConfig=[ vim.DistributedVirtualSwitch.HealthCheckConfig() ]):
         # throws vim.fault.DvsFault
         return vim.Task()

      def lookupPortgroup(portgroupKey=""):
         # throws vim.fault.NotFound
         return vim.dvs.DistributedVirtualPortgroup()

      class ProductSpecOperationType(Enum):
         preInstall = 0
         upgrade = 1
         notifyAvailableUpgrade = 2
         proceedWithUpgrade = 3
         updateBundleInfo = 4

      class ContactInfo(vmodl.DynamicData):
         name = ""
         contact = ""

      class NicTeamingPolicyMode(Enum):
         loadbalance_ip = 0
         loadbalance_srcmac = 1
         loadbalance_srcid = 2
         failover_explicit = 3
         loadbalance_loadbased = 4

      class NetworkResourceManagementCapability(vmodl.DynamicData):
         networkResourceManagementSupported = False
         networkResourcePoolHighShareValue = 0
         qosSupported = False
         userDefinedNetworkResourcePoolsSupported = False
         networkResourceControlVersion3Supported = False
         userDefinedInfraTrafficPoolSupported = False

      class RollbackCapability(vmodl.DynamicData):
         rollbackSupported = False

      class BackupRestoreCapability(vmodl.DynamicData):
         backupRestoreSupported = False

      class FeatureCapability(vmodl.DynamicData):
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

      class HealthCheckFeatureCapability(vmodl.DynamicData):
         pass

      class Capability(vmodl.DynamicData):
         dvsOperationSupported = False
         dvPortGroupOperationSupported = False
         dvPortOperationSupported = False
         compatibleHostComponentProductInfo = [ vim.dvs.HostProductSpec() ]
         featuresSupported = vim.DistributedVirtualSwitch.FeatureCapability()

      class Summary(vmodl.DynamicData):
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

      class SwitchPolicy(vmodl.DynamicData):
         autoPreInstallAllowed = False
         autoUpgradeAllowed = False
         partialUpgradeAllowed = False

      class UplinkPortPolicy(vmodl.DynamicData):
         pass

      class NameArrayUplinkPortPolicy(vim.DistributedVirtualSwitch.UplinkPortPolicy):
         uplinkPortName = [ "" ]

      class ConfigSpec(vmodl.DynamicData):
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

      class CreateSpec(vmodl.DynamicData):
         configSpec = vim.DistributedVirtualSwitch.ConfigSpec()
         productInfo = vim.dvs.ProductSpec()
         capability = vim.DistributedVirtualSwitch.Capability()

      class ConfigInfo(vmodl.DynamicData):
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

      class NetworkResourceControlVersion(Enum):
         version2 = 0
         version3 = 1

      class HostInfrastructureTrafficClass(Enum):
         management = 0
         faultTolerance = 1
         vmotion = 2
         virtualMachine = 3
         iSCSI = 4
         nfs = 5
         hbr = 6
         vsan = 7
         vdp = 8

      class HostInfrastructureTrafficResource(vmodl.DynamicData):
         key = ""
         description = ""
         allocationInfo = vim.DistributedVirtualSwitch.HostInfrastructureTrafficResource.ResourceAllocation()

         class ResourceAllocation(vmodl.DynamicData):
            limit = 0
            shares = vim.SharesInfo()
            reservation = 0

      class HealthCheckConfig(vmodl.DynamicData):
         enable = False
         interval = 0

      class ResourceRuntimeInfo(vmodl.DynamicData):
         capacity = 0
         usage = 0
         available = 0
         allocatedResource = [ vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource() ]
         vmVnicNetworkResourcePoolRuntime = [ vim.dvs.VmVnicNetworkResourcePool.RuntimeInfo() ]

      class RuntimeInfo(vmodl.DynamicData):
         hostMemberRuntime = [ vim.dvs.HostMember.RuntimeInfo() ]
         resourceRuntimeInfo = vim.DistributedVirtualSwitch.ResourceRuntimeInfo()

   class Folder(vim.ManagedEntity):
      childType = [ vmodl.TypeName() ]
      childEntity = [ vim.ManagedEntity() ]
      namespace = ""

      def createFolder(name=""):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Folder()

      def moveInto(list=[ vim.ManagedEntity() ]):
         # throws vim.fault.DuplicateName, vim.fault.InvalidFolder, vim.fault.InvalidState
         return vim.Task()

      def createVm(config=vim.vm.ConfigSpec(), pool=vim.ResourcePool(), host=vim.HostSystem() or None):
         # throws vim.fault.VmConfigFault, vim.fault.FileFault, vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.InvalidDatastore, vim.fault.InsufficientResourcesFault, vim.fault.AlreadyExists, vim.fault.InvalidState
         return vim.Task()

      def registerVm(path="", name="" or None, asTemplate=False, pool=vim.ResourcePool() or None, host=vim.HostSystem() or None):
         # throws vim.fault.OutOfBounds, vim.fault.DuplicateName, vim.fault.AlreadyExists, vim.fault.InvalidDatastore, vim.fault.NotFound, vim.fault.InvalidName, vim.fault.VmConfigFault, vim.fault.InsufficientResourcesFault, vim.fault.FileFault, vim.fault.InvalidState
         return vim.Task()

      def createCluster(name="", spec=vim.cluster.ConfigSpec()):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.ClusterComputeResource()

      def createClusterEx(name="", spec=vim.cluster.ConfigSpecEx()):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.ClusterComputeResource()

      def addStandaloneHost(spec=vim.host.ConnectSpec(), compResSpec=vim.ComputeResource.ConfigSpec() or None, addConnected=False, license="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault, vim.fault.DuplicateName
         return vim.Task()

      def createDatacenter(name=""):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.Datacenter()

      def unregisterAndDestroy():
         # throws vim.fault.ConcurrentAccess, vim.fault.InvalidState
         return vim.Task()

      def createDistributedVirtualSwitch(spec=vim.DistributedVirtualSwitch.CreateSpec()):
         # throws vim.fault.DvsFault, vim.fault.DuplicateName, vim.fault.InvalidName, vim.fault.NotFound, vim.fault.DvsNotAuthorized
         return vim.Task()

      def createStoragePod(name=""):
         # throws vim.fault.DuplicateName, vim.fault.InvalidName
         return vim.StoragePod()

      def batchAddStandaloneHosts(newHosts=[ vim.Folder.NewHostSpec() ] or None, compResSpec=vim.ComputeResource.ConfigSpec() or None, addConnected=False):
         return vim.Task()

      def batchAddHostsToCluster(cluster=vim.ClusterComputeResource(), newHosts=[ vim.Folder.NewHostSpec() ] or None, existingHosts=[ vim.HostSystem() ] or None, compResSpec=vim.ComputeResource.ConfigSpec() or None, desiredState="" or None):
         return vim.Task()

      class DesiredHostState(Enum):
         maintenance = 0
         non_maintenance = 1

      class NewHostSpec(vmodl.DynamicData):
         hostCnxSpec = vim.host.ConnectSpec()
         esxLicense = ""

      class FailedHostResult(vmodl.DynamicData):
         hostName = ""
         host = vim.HostSystem()
         context = vmodl.LocalizableMessage()
         fault = vmodl.MethodFault()

      class BatchAddStandaloneHostsResult(vmodl.DynamicData):
         addedHosts = [ vim.HostSystem() ]
         hostsFailedInventoryAdd = [ vim.Folder.FailedHostResult() ]

      class BatchAddHostsToClusterResult(vmodl.DynamicData):
         hostsAddedToCluster = [ vim.HostSystem() ]
         hostsFailedInventoryAdd = [ vim.Folder.FailedHostResult() ]
         hostsFailedMoveToCluster = [ vim.Folder.FailedHostResult() ]

   class HealthUpdate(vmodl.DynamicData):
      entity = vim.ManagedEntity()
      healthUpdateInfoId = ""
      id = ""
      status = vim.ManagedEntity.Status()
      remediation = ""

   class HostSystem(vim.ManagedEntity):
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

      def queryTpmAttestationReport():
         return vim.host.TpmAttestationReport()

      def queryConnectionInfo():
         return vim.host.ConnectInfo()

      def updateSystemResources(resourceInfo=vim.host.SystemResourceInfo()):
         return None

      def updateSystemSwapConfiguration(sysSwapConfig=vim.host.SystemSwapConfiguration()):
         return None

      def reconnect(cnxSpec=vim.host.ConnectSpec() or None, reconnectSpec=vim.HostSystem.ReconnectSpec() or None):
         # throws vim.fault.InvalidLogin, vim.fault.InvalidState, vim.fault.InvalidName, vim.fault.HostConnectFault
         return vim.Task()

      def disconnect():
         return vim.Task()

      def enterMaintenanceMode(timeout=0, evacuatePoweredOffVms=False or None, maintenanceSpec=vim.host.MaintenanceSpec() or None):
         # throws vim.fault.InvalidState, vim.fault.Timedout
         return vim.Task()

      def exitMaintenanceMode(timeout=0):
         # throws vim.fault.InvalidState, vim.fault.Timedout
         return vim.Task()

      def reboot(force=False):
         # throws vim.fault.InvalidState
         return vim.Task()

      def shutdown(force=False):
         # throws vim.fault.InvalidState
         return vim.Task()

      def enterStandbyMode(timeoutSec=0, evacuatePoweredOffVms=False or None):
         # throws vim.fault.HostPowerOpFailed, vim.fault.InvalidState, vmodl.fault.NotSupported, vim.fault.Timedout, vmodl.fault.RequestCanceled
         return vim.Task()

      def exitStandbyMode(timeoutSec=0):
         # throws vim.fault.HostPowerOpFailed, vim.fault.InvalidState, vmodl.fault.NotSupported, vim.fault.Timedout
         return vim.Task()

      def queryOverhead(memorySize=0, videoRamSize=0 or None, numVcpus=0):
         return 0

      def queryOverheadEx(vmConfigInfo=vim.vm.ConfigInfo()):
         return 0

      def reconfigureDAS():
         # throws vim.fault.DasConfigFault
         return vim.Task()

      def updateFlags(flagInfo=vim.host.FlagInfo()):
         return None

      def enterLockdownMode():
         # throws vim.fault.HostConfigFault
         return None

      def exitLockdownMode():
         # throws vim.fault.HostConfigFault
         return None

      def acquireCimServicesTicket():
         return vim.HostServiceTicket()

      def updateIpmi(ipmiInfo=vim.host.IpmiInfo()):
         # throws vim.fault.InvalidIpmiLoginInfo, vim.fault.InvalidIpmiMacAddress
         return None

      def retrieveHardwareUptime():
         return 0

      def prepareCrypto():
         # throws vim.fault.InvalidState
         return None

      def enableCrypto(keyPlain=vim.encryption.CryptoKeyPlain()):
         # throws vim.fault.InvalidState
         return None

      def configureCryptoKey(keyId=vim.encryption.CryptoKeyId() or None):
         return None

      def queryProductLockerLocation():
         # throws vim.fault.HostConfigFault
         return ""

      def updateProductLockerLocation(path=""):
         # throws vmodl.fault.InvalidArgument, vim.fault.FileNotFound, vim.fault.TaskInProgress, vim.fault.HostConfigFault
         return vim.Task()

      def retrieveFreeEpcMemory():
         return 0

      class ConnectionState(Enum):
         connected = 0
         notResponding = 1
         disconnected = 2

      class PowerState(Enum):
         poweredOn = 0
         poweredOff = 1
         standBy = 2
         unknown = 3

      class StandbyMode(Enum):
         entering = 0
         exiting = 1
         in = 2
         none = 3

      class CryptoState(Enum):
         incapable = 0
         prepared = 1
         safe = 2
         pendingIncapable = 3

      class RemediationState(vmodl.DynamicData):
         state = ""
         operationTime = vmodl.DateTime()

         class State(Enum):
            remediationReady = 0
            precheckRemediationRunning = 1
            precheckRemediationComplete = 2
            precheckRemediationFailed = 3
            remediationRunning = 4
            remediationFailed = 5

      class ComplianceCheckState(vmodl.DynamicData):
         state = ""
         checkTime = vmodl.DateTime()

      class ReconnectSpec(vmodl.DynamicData):
         syncState = False

   class ServiceInstance(vmodl.ManagedObject):
      serverClock = vmodl.DateTime()
      capability = vim.Capability()
      content = vim.ServiceInstanceContent()

      def currentTime():
         return vmodl.DateTime()

      def retrieveContent():
         return vim.ServiceInstanceContent()

      def validateMigration(vm=[ vim.VirtualMachine() ], state=vim.VirtualMachine.PowerState() or None, testType=[ "" ] or None, pool=vim.ResourcePool() or None, host=vim.HostSystem() or None):
         # throws vim.fault.InvalidState
         return [ vim.event.Event() ]

      def queryVMotionCompatibility(vm=vim.VirtualMachine(), host=[ vim.HostSystem() ], compatibility=[ "" ] or None):
         return [ vim.ServiceInstance.HostVMotionCompatibility() ]

      def retrieveProductComponents():
         return [ vim.ServiceInstance.ProductComponentInfo() ]

      class ValidateMigrationTestType(Enum):
         sourceTests = 0
         compatibilityTests = 1
         diskAccessibilityTests = 2
         resourceTests = 3

      class VMotionCompatibilityType(Enum):
         cpu = 0
         software = 1

      class HostVMotionCompatibility(vmodl.DynamicData):
         host = vim.HostSystem()
         compatibility = [ "" ]

      class ProductComponentInfo(vmodl.DynamicData):
         id = ""
         name = ""
         version = ""
         release = 0

   class StoragePod(vim.Folder):
      summary = vim.StoragePod.Summary()
      podStorageDrsEntry = vim.StorageResourceManager.PodStorageDrsEntry()

      class Summary(vmodl.DynamicData):
         name = ""
         capacity = 0
         freeSpace = 0

   class VasaVvolManager(object):

      class VasaProviderContainerSpec(vmodl.DynamicData):
         vasaProviderInfo = [ vim.VimVasaProviderInfo() ]
         scId = ""
         deleted = False

   class ClusterComputeResource(vim.ComputeResource):
      configuration = vim.cluster.ConfigInfo()
      recommendation = [ vim.cluster.Recommendation() ]
      drsRecommendation = [ vim.cluster.DrsRecommendation() ]
      hciConfig = vim.ClusterComputeResource.HCIConfigInfo()
      migrationHistory = [ vim.cluster.DrsMigration() ]
      actionHistory = [ vim.cluster.ActionHistory() ]
      drsFault = [ vim.cluster.DrsFaults() ]

      def configureHCI(clusterSpec=vim.ClusterComputeResource.HCIConfigSpec(), hostInputs=[ vim.ClusterComputeResource.HostConfigurationInput() ] or None):
         return vim.Task()

      def extendHCI(hostInputs=[ vim.ClusterComputeResource.HostConfigurationInput() ] or None, vSanConfigSpec=vim.SDDCBase() or None):
         return vim.Task()

      def AbandonHciWorkflow():
         # throws vim.fault.InvalidState
         return None

      def validateHCIConfiguration(hciConfigSpec=vim.ClusterComputeResource.HCIConfigSpec() or None, hosts=[ vim.HostSystem() ] or None):
         # throws vim.fault.InvalidState
         return [ vim.ClusterComputeResource.ValidationResultBase() ]

      def reconfigure(spec=vim.cluster.ConfigSpec(), modify=False):
         return vim.Task()

      def applyRecommendation(key=""):
         return None

      def cancelRecommendation(key=""):
         return None

      def recommendHostsForVm(vm=vim.VirtualMachine(), pool=vim.ResourcePool() or None):
         return [ vim.cluster.HostRecommendation() ]

      def addHost(spec=vim.host.ConnectSpec(), asConnected=False, resourcePool=vim.ResourcePool() or None, license="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault, vim.fault.DuplicateName
         return vim.Task()

      def moveInto(host=[ vim.HostSystem() ]):
         # throws vim.fault.DuplicateName, vim.fault.TooManyHosts, vim.fault.InvalidState
         return vim.Task()

      def moveHostInto(host=vim.HostSystem(), resourcePool=vim.ResourcePool() or None):
         # throws vim.fault.TooManyHosts, vim.fault.InvalidState
         return vim.Task()

      def refreshRecommendation():
         return None

      def evcManager():
         return vim.cluster.EVCManager()

      def retrieveDasAdvancedRuntimeInfo():
         return vim.cluster.DasAdvancedRuntimeInfo()

      def enterMaintenanceMode(host=[ vim.HostSystem() ], option=[ vim.option.OptionValue() ] or None):
         return vim.cluster.EnterMaintenanceResult()

      def placeVm(placementSpec=vim.cluster.PlacementSpec()):
         # throws vim.fault.InvalidState
         return vim.cluster.PlacementResult()

      def findRulesForVm(vm=vim.VirtualMachine()):
         return [ vim.cluster.RuleInfo() ]

      def stampAllRulesWithUuid():
         return vim.Task()

      def getResourceUsage():
         return vim.cluster.ResourceUsageSummary()

      def setCryptoMode(cryptoMode=""):
         # throws vmodl.fault.InvalidRequest, vmodl.fault.InvalidArgument
         return None

      class Summary(vim.ComputeResource.Summary):
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

      class DVSSetting(vmodl.DynamicData):
         dvSwitch = vim.DistributedVirtualSwitch()
         pnicDevices = [ "" ]
         dvPortgroupSetting = [ vim.ClusterComputeResource.DVSSetting.DVPortgroupToServiceMapping() ]

         class DVPortgroupToServiceMapping(vmodl.DynamicData):
            dvPortgroup = vim.dvs.DistributedVirtualPortgroup()
            service = ""

      class HCIWorkflowState(Enum):
         in_progress = 0
         done = 1
         invalid = 2

      class HostConfigurationProfile(vmodl.DynamicData):
         dateTimeConfig = vim.host.DateTimeConfig()
         lockdownMode = vim.host.HostAccessManager.LockdownMode()

      class HCIConfigInfo(vmodl.DynamicData):
         workflowState = ""
         dvsSetting = [ vim.ClusterComputeResource.DVSSetting() ]
         configuredHosts = [ vim.HostSystem() ]
         hostConfigProfile = vim.ClusterComputeResource.HostConfigurationProfile()

      class ClusterConfigResult(vmodl.DynamicData):
         failedHosts = [ vim.Folder.FailedHostResult() ]
         configuredHosts = [ vim.HostSystem() ]

      class DvsProfile(vmodl.DynamicData):
         dvsName = ""
         dvSwitch = vim.DistributedVirtualSwitch()
         pnicDevices = [ "" ]
         dvPortgroupMapping = [ vim.ClusterComputeResource.DvsProfile.DVPortgroupSpecToServiceMapping() ]

         class DVPortgroupSpecToServiceMapping(vmodl.DynamicData):
            dvPortgroupSpec = vim.dvs.DistributedVirtualPortgroup.ConfigSpec()
            dvPortgroup = vim.dvs.DistributedVirtualPortgroup()
            service = ""

      class VCProfile(vmodl.DynamicData):
         clusterSpec = vim.cluster.ConfigSpecEx()
         evcModeKey = ""

      class HCIConfigSpec(vmodl.DynamicData):
         dvsProf = [ vim.ClusterComputeResource.DvsProfile() ]
         hostConfigProfile = vim.ClusterComputeResource.HostConfigurationProfile()
         vSanConfigSpec = vim.SDDCBase()
         vcProf = vim.ClusterComputeResource.VCProfile()

      class HostVmkNicInfo(vmodl.DynamicData):
         nicSpec = vim.host.VirtualNic.Specification()
         service = ""

      class HostConfigurationInput(vmodl.DynamicData):
         host = vim.HostSystem()
         hostVmkNics = [ vim.ClusterComputeResource.HostVmkNicInfo() ]
         allowedInNonMaintenanceMode = False

      class ValidationResultBase(vmodl.DynamicData):
         info = [ vmodl.LocalizableMessage() ]

      class HostConfigurationValidation(vim.ClusterComputeResource.ValidationResultBase):
         host = vim.HostSystem()
         isDvsSettingValid = False
         isVmknicSettingValid = False
         isNtpSettingValid = False
         isLockdownModeValid = False

      class DVSConfigurationValidation(vim.ClusterComputeResource.ValidationResultBase):
         isDvsValid = False
         isDvpgValid = False

   class Datacenter(vim.ManagedEntity):
      vmFolder = vim.Folder()
      hostFolder = vim.Folder()
      datastoreFolder = vim.Folder()
      networkFolder = vim.Folder()
      datastore = [ vim.Datastore() ]
      network = [ vim.Network() ]
      configuration = vim.Datacenter.ConfigInfo()

      def batchQueryConnectInfo(hostSpecs=[ vim.host.ConnectSpec() ] or None):
         return [ vim.Datacenter.BasicConnectInfo() ]

      def queryConnectionInfo(hostname="", port=0, username="", password="", sslThumbprint="" or None):
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
         return vim.host.ConnectInfo()

      def queryConnectionInfoViaSpec(spec=vim.host.ConnectSpec()):
         # throws vim.fault.InvalidLogin, vim.fault.HostConnectFault
         return vim.host.ConnectInfo()

      def powerOnVm(vm=[ vim.VirtualMachine() ], option=[ vim.option.OptionValue() ] or None):
         return vim.Task()

      def queryConfigOptionDescriptor():
         return [ vim.vm.ConfigOptionDescriptor() ]

      def reconfigure(spec=vim.Datacenter.ConfigSpec(), modify=False):
         return vim.Task()

      class BasicConnectInfo(vmodl.DynamicData):
         hostname = ""
         error = vmodl.MethodFault()
         serverIp = ""
         numVm = 0
         numPoweredOnVm = 0
         hostProductInfo = vim.AboutInfo()
         hardwareVendor = ""
         hardwareModel = ""

      class ConfigInfo(vmodl.DynamicData):
         defaultHardwareVersionKey = ""

      class ConfigSpec(vmodl.DynamicData):
         defaultHardwareVersionKey = ""
