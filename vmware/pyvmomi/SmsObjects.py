from enum import Enum

class sms(object): # (unknown name)

   class AboutInfo(vmodl.DynamicData): # sms.AboutInfo
      name = ""
      fullName = ""
      vendor = ""
      apiVersion = ""
      instanceUuid = ""
      vasaApiVersion = ""

   class EntityReference(vmodl.DynamicData): # sms.EntityReference
      id = ""
      type = sms.EntityReference.EntityType()

      class EntityType(Enum): # sms.EntityReference.EntityType
         datacenter = 0
         resourcePool = 1
         storagePod = 2
         cluster = 3
         vm = 4
         datastore = 5
         host = 6
         vmFile = 7
         scsiPath = 8
         scsiTarget = 9
         scsiVolume = 10
         scsiAdapter = 11
         nasMount = 12

   class FaultDomainFilter(vmodl.DynamicData): # sms.FaultDomainFilter
      providerId = ""

   class ReplicationGroupFilter(vmodl.DynamicData): # sms.ReplicationGroupFilter
      groupId = [ vim.vm.replication.ReplicationGroupId() ]

   class ServiceInstance(vmodl.ManagedObject): # sms.ServiceInstance

      def queryStorageManager(): # sms.ServiceInstance.queryStorageManager
         return sms.StorageManager()

      def querySessionManager(): # sms.ServiceInstance.querySessionManager
         return sms.auth.SessionManager()

      def queryAboutInfo(): # sms.ServiceInstance.queryAboutInfo
         return sms.AboutInfo()

   class StorageManager(vmodl.ManagedObject): # sms.StorageManager

      def registerProvider(providerSpec=sms.provider.ProviderSpec()): # sms.StorageManager.registerProvider
         # throws vim.fault.AlreadyExists, sms.fault.ProviderRegistrationFault
         return sms.Task()

      def unregisterProvider(providerId=""): # sms.StorageManager.unregisterProvider
         # throws vim.fault.NotFound, sms.fault.ProviderUnregistrationFault
         return sms.Task()

      def queryProvider(): # sms.StorageManager.queryProvider
         # throws sms.fault.QueryExecutionFault
         return [ sms.provider.Provider() ]

      def queryArray(providerId=[ "" ] or None): # sms.StorageManager.queryArray
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageArray() ]

      def queryProcessorAssociatedWithArray(arrayId=""): # sms.StorageManager.queryProcessorAssociatedWithArray
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageProcessor() ]

      def queryPortAssociatedWithArray(arrayId=""): # sms.StorageManager.queryPortAssociatedWithArray
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StoragePort() ]

      def queryPortAssociatedWithLun(scsi3Id="", arrayId=""): # sms.StorageManager.queryPortAssociatedWithLun
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StoragePort()

      def queryLunAssociatedWithPort(portId="", arrayId=""): # sms.StorageManager.queryLunAssociatedWithPort
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageLun() ]

      def queryArrayAssociatedWithLun(canonicalName=""): # sms.StorageManager.queryArrayAssociatedWithLun
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageArray()

      def queryPortAssociatedWithProcessor(processorId="", arrayId=""): # sms.StorageManager.queryPortAssociatedWithProcessor
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StoragePort() ]

      def queryLunAssociatedWithArray(arrayId=""): # sms.StorageManager.queryLunAssociatedWithArray
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageLun() ]

      def queryFileSystemAssociatedWithArray(arrayId=""): # sms.StorageManager.queryFileSystemAssociatedWithArray
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageFileSystem() ]

      def queryDatastoreCapability(datastore=vim.Datastore()): # sms.StorageManager.queryDatastoreCapability
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageCapability()

      def queryHostAssociatedWithLun(scsi3Id="", arrayId=""): # sms.StorageManager.queryHostAssociatedWithLun
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ vim.HostSystem() ]

      def queryVmfsDatastoreAssociatedWithLun(scsi3Id="", arrayId=""): # sms.StorageManager.queryVmfsDatastoreAssociatedWithLun
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return vim.Datastore()

      def queryNfsDatastoreAssociatedWithFileSystem(fileSystemId="", arrayId=""): # sms.StorageManager.queryNfsDatastoreAssociatedWithFileSystem
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return vim.Datastore()

      def queryDrsMigrationCapabilityForPerformance(srcDatastore=vim.Datastore(), dstDatastore=vim.Datastore()): # sms.StorageManager.queryDrsMigrationCapabilityForPerformance
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return False

      def queryDrsMigrationCapabilityForPerformanceEx(datastore=[ vim.Datastore() ]): # sms.StorageManager.queryDrsMigrationCapabilityForPerformanceEx
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.DrsMigrationCapabilityResult()

      def queryStorageContainer(containerSpec=sms.storage.StorageContainerSpec() or None): # sms.StorageManager.queryStorageContainer
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageContainerResult()

      def queryAssociatedBackingStoragePool(entityId="" or None, entityType="" or None): # sms.StorageManager.queryAssociatedBackingStoragePool
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.BackingStoragePool() ]

      def queryDatastoreBackingPoolMapping(datastore=[ vim.Datastore() ]): # sms.StorageManager.queryDatastoreBackingPoolMapping
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.DatastoreBackingPoolMapping() ]

      def refreshCACertificatesAndCRLs(providerId=[ "" ] or None): # sms.StorageManager.refreshCACertificatesAndCRLs
         # throws vim.fault.NotFound, sms.fault.CertificateRefreshFailed
         return sms.Task()

      def queryFaultDomain(filter=sms.FaultDomainFilter() or None): # sms.StorageManager.queryFaultDomain
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ vim.vm.replication.FaultDomainId() ]

      def queryReplicationGroupInfo(rgFilter=sms.ReplicationGroupFilter()): # sms.StorageManager.queryReplicationGroupInfo
         # throws sms.fault.QueryExecutionFault
         return [ sms.storage.replication.GroupOperationResult() ]

   class Task(vmodl.ManagedObject): # sms.Task

      def queryResult(): # sms.Task.queryResult
         return {}

      def queryInfo(): # sms.Task.queryInfo
         return sms.TaskInfo()

   class TaskInfo(vmodl.DynamicData): # sms.TaskInfo
      key = ""
      task = sms.Task()
      object = vmodl.ManagedObject()
      error = vmodl.MethodFault()
      result = {}
      startTime = vmodl.DateTime()
      completionTime = vmodl.DateTime()
      state = ""
      progress = 0

      class State(Enum): # sms.TaskInfo.State
         queued = 0
         running = 1
         success = 2
         error = 3

   class fault(object): # (unknown name)

      class AuthConnectionFailed(vim.fault.NoPermission): # sms.fault.AuthConnectionFailed
         pass

      class CertificateRefreshFailed(vmodl.MethodFault): # sms.fault.CertificateRefreshFailed
         providerId = [ "" ]

      class CertificateRevocationFailed(vmodl.MethodFault): # sms.fault.CertificateRevocationFailed
         pass

      class DuplicateEntry(vmodl.MethodFault): # sms.fault.DuplicateEntry
         pass

      class InactiveProvider(vmodl.MethodFault): # sms.fault.InactiveProvider
         mapping = [ sms.storage.FaultDomainProviderMapping() ]

      class InvalidLogin(vmodl.MethodFault): # sms.fault.InvalidLogin
         pass

      class InvalidProfile(vmodl.MethodFault): # sms.fault.InvalidProfile
         pass

      class InvalidSession(vim.fault.NoPermission): # sms.fault.InvalidSession
         sessionCookie = ""

      class MultipleSortSpecsNotSupported(vmodl.fault.InvalidArgument): # sms.fault.MultipleSortSpecsNotSupported
         pass

      class NotSupportedByProvider(vmodl.MethodFault): # sms.fault.NotSupportedByProvider
         pass

      class ProviderBusy(vmodl.MethodFault): # sms.fault.ProviderBusy
         pass

      class ProviderConnectionFailed(vmodl.RuntimeFault): # sms.fault.ProviderConnectionFailed
         pass

      class ProviderOutOfProvisioningResource(vmodl.MethodFault): # sms.fault.ProviderOutOfProvisioningResource
         provisioningResourceId = ""
         availableBefore = 0
         availableAfter = 0
         total = 0
         isTransient = False

      class ProviderOutOfResource(vmodl.MethodFault): # sms.fault.ProviderOutOfResource
         pass

      class ProviderRegistrationFault(vmodl.MethodFault): # sms.fault.ProviderRegistrationFault
         pass

      class ProviderSyncFailed(vmodl.MethodFault): # sms.fault.ProviderSyncFailed
         pass

      class ProviderUnavailable(vmodl.MethodFault): # sms.fault.ProviderUnavailable
         pass

      class ProviderUnregistrationFault(vmodl.MethodFault): # sms.fault.ProviderUnregistrationFault
         pass

      class ProxyRegistrationFailed(vmodl.RuntimeFault): # sms.fault.ProxyRegistrationFailed
         pass

      class QueryExecutionFault(vmodl.MethodFault): # sms.fault.QueryExecutionFault
         pass

      class QueryNotSupported(vmodl.fault.InvalidArgument): # sms.fault.QueryNotSupported
         entityType = sms.EntityReference.EntityType()
         relatedEntityType = sms.EntityReference.EntityType()

      class ResourceInUse(vim.fault.ResourceInUse): # sms.fault.ResourceInUse
         deviceIds = [ sms.storage.replication.DeviceId() ]

      class ServiceNotInitialized(vmodl.RuntimeFault): # sms.fault.ServiceNotInitialized
         pass

      class SyncInProgress(sms.fault.ProviderSyncFailed): # sms.fault.SyncInProgress
         pass

      class TooMany(vmodl.MethodFault): # sms.fault.TooMany
         maxBatchSize = 0

      class replication(object): # (unknown name)

         class ReplicationFault(vmodl.MethodFault): # sms.fault.replication.ReplicationFault
            pass

         class SyncOngoing(sms.fault.replication.ReplicationFault): # sms.fault.replication.SyncOngoing
            task = sms.Task()

         class AlreadyDone(sms.fault.replication.ReplicationFault): # sms.fault.replication.AlreadyDone
            pass

         class InvalidFunctionTarget(sms.fault.replication.ReplicationFault): # sms.fault.replication.InvalidFunctionTarget
            pass

         class InvalidReplicationState(sms.fault.replication.ReplicationFault): # sms.fault.replication.InvalidReplicationState
            desiredState = [ "" ]
            currentState = ""

         class NoReplicationTarget(sms.fault.replication.ReplicationFault): # sms.fault.replication.NoReplicationTarget
            pass

         class NoValidReplica(sms.fault.replication.ReplicationFault): # sms.fault.replication.NoValidReplica
            deviceId = sms.storage.replication.DeviceId()

         class PeerNotReachable(sms.fault.replication.ReplicationFault): # sms.fault.replication.PeerNotReachable
            pass

      class CertificateAuthorityFault(sms.fault.ProviderRegistrationFault): # sms.fault.CertificateAuthorityFault
         faultCode = 0

      class CertificateNotImported(sms.fault.ProviderRegistrationFault): # sms.fault.CertificateNotImported
         pass

      class CertificateNotTrusted(sms.fault.ProviderRegistrationFault): # sms.fault.CertificateNotTrusted
         certificate = ""

      class IncorrectUsernamePassword(sms.fault.ProviderRegistrationFault): # sms.fault.IncorrectUsernamePassword
         pass

      class InvalidCertificate(sms.fault.ProviderRegistrationFault): # sms.fault.InvalidCertificate
         certificate = ""

      class InvalidUrl(sms.fault.ProviderRegistrationFault): # sms.fault.InvalidUrl
         url = ""

      class NoCommonProviderForAllBackings(sms.fault.QueryExecutionFault): # sms.fault.NoCommonProviderForAllBackings
         pass

      class ProviderNotFound(sms.fault.QueryExecutionFault): # sms.fault.ProviderNotFound
         pass

   class provider(object): # (unknown name)

      class AlarmFilter(vmodl.DynamicData): # sms.provider.AlarmFilter
         alarmStatus = ""
         alarmType = ""
         entityType = ""
         entityId = [ {} ]
         pageMarker = ""

      class AlarmResult(vmodl.DynamicData): # sms.provider.AlarmResult
         storageAlarm = [ sms.storage.StorageAlarm() ]
         pageMarker = ""

      class Provider(vmodl.ManagedObject): # sms.provider.Provider

         def queryProviderInfo(): # sms.provider.Provider.queryProviderInfo
            return sms.provider.ProviderInfo()

      class ProviderInfo(vmodl.DynamicData): # sms.provider.ProviderInfo
         uid = ""
         name = ""
         description = ""
         version = ""

      class ProviderSpec(vmodl.DynamicData): # sms.provider.ProviderSpec
         name = ""
         description = ""

      class VasaProvider(sms.provider.Provider): # sms.provider.VasaProvider

         def sync(arrayId="" or None): # sms.provider.VasaProvider.sync
            # throws sms.fault.ProviderSyncFailed
            return sms.Task()

         def refreshCertificate(): # sms.provider.VasaProvider.refreshCertificate
            # throws sms.fault.CertificateRefreshFailed
            return sms.Task()

         def revokeCertificate(): # sms.provider.VasaProvider.revokeCertificate
            # throws sms.fault.CertificateRevocationFailed
            return sms.Task()

         def reconnect(): # sms.provider.VasaProvider.reconnect
            # throws sms.fault.InvalidCertificate, sms.fault.ProviderConnectionFailed
            return sms.Task()

         def queryReplicationPeer(faultDomainId=[ vim.vm.replication.FaultDomainId() ] or None): # sms.provider.VasaProvider.queryReplicationPeer
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.QueryReplicationPeerResult() ]

         def queryReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None): # sms.provider.VasaProvider.queryReplicationGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.GroupOperationResult() ]

         def queryPointInTimeReplica(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, queryParam=sms.storage.replication.QueryPointInTimeReplicaParam() or None): # sms.provider.VasaProvider.queryPointInTimeReplica
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.GroupOperationResult() ]

         def testFailoverReplicationGroupStart(testFailoverParam=sms.storage.replication.TestFailoverParam()): # sms.provider.VasaProvider.testFailoverReplicationGroupStart
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def testFailoverReplicationGroupStop(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, force=False): # sms.provider.VasaProvider.testFailoverReplicationGroupStop
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault, sms.fault.NotSupportedByProvider
            return sms.Task()

         def promoteReplicationGroup(promoteParam=sms.storage.replication.PromoteParam()): # sms.provider.VasaProvider.promoteReplicationGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def syncReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, pitName=""): # sms.provider.VasaProvider.syncReplicationGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault, sms.fault.TooMany
            return sms.Task()

         def prepareFailoverReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None): # sms.provider.VasaProvider.prepareFailoverReplicationGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def failoverReplicationGroup(failoverParam=sms.storage.replication.FailoverParam()): # sms.provider.VasaProvider.failoverReplicationGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def reverseReplicateGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None): # sms.provider.VasaProvider.reverseReplicateGroup
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def queryActiveAlarm(alarmFilter=sms.provider.AlarmFilter() or None): # sms.provider.VasaProvider.queryActiveAlarm
            # throws vim.fault.NotFound, sms.fault.ProviderBusy, sms.fault.InactiveProvider, sms.fault.ProviderUnavailable, sms.fault.QueryExecutionFault
            return sms.provider.AlarmResult()

      class VasaProviderInfo(sms.provider.ProviderInfo): # sms.provider.VasaProviderInfo
         url = ""
         certificate = ""
         status = ""
         statusFault = vmodl.MethodFault()
         vasaVersion = ""
         namespace = ""
         lastSyncTime = ""
         supportedVendorModelMapping = [ sms.provider.VasaProviderInfo.SupportedVendorModelMapping() ]
         supportedProfile = [ "" ]
         supportedProviderProfile = [ "" ]
         relatedStorageArray = [ sms.provider.VasaProviderInfo.RelatedStorageArray() ]
         providerId = ""
         certificateExpiryDate = ""
         certificateStatus = ""
         serviceLocation = ""
         needsExplicitActivation = False
         maxBatchSize = 0
         retainVasaProviderCertificate = False
         arrayIndependentProvider = False
         type = ""
         category = ""
         priority = 0
         failoverGroupId = ""

         class CertificateStatus(Enum): # sms.provider.VasaProviderInfo.CertificateStatus
            valid = 0
            expirySoftLimitReached = 1
            expiryHardLimitReached = 2
            expired = 3
            invalid = 4

         class RelatedStorageArray(vmodl.DynamicData): # sms.provider.VasaProviderInfo.RelatedStorageArray
            arrayId = ""
            active = False
            manageable = False
            priority = 0

         class SupportedVendorModelMapping(vmodl.DynamicData): # sms.provider.VasaProviderInfo.SupportedVendorModelMapping
            vendorId = ""
            modelId = ""

         class VasaProviderStatus(Enum): # sms.provider.VasaProviderInfo.VasaProviderStatus
            online = 0
            offline = 1
            syncError = 2
            unknown = 3
            connected = 4
            disconnected = 5

         class VasaProviderProfile(Enum): # sms.provider.VasaProviderInfo.VasaProviderProfile
            blockDevice = 0
            fileSystem = 1
            capability = 2

         class ProviderProfile(Enum): # sms.provider.VasaProviderInfo.ProviderProfile
            ProfileBasedManagement = 0
            Replication = 1

         class Type(Enum): # sms.provider.VasaProviderInfo.Type
            PERSISTENCE = 0
            DATASERVICE = 1
            UNKNOWN = 2

         class Category(Enum): # sms.provider.VasaProviderInfo.Category
            internal = 0
            external = 1

      class VasaProviderSpec(sms.provider.ProviderSpec): # sms.provider.VasaProviderSpec
         username = ""
         password = ""
         url = ""
         certificate = ""

      class VmodlVasaProviderSpec(object): # (unknown name)

         class AuthenticationType(Enum): # sms.provider.VmodlVasaProviderSpec.AuthenticationType
            LoginByToken = 0
            UseSessionId = 1

   class storage(object): # (unknown name)

      class AlarmStatus(Enum): # sms.storage.AlarmStatus
         Red = 0
         Green = 1
         Yellow = 2

      class AlarmType(Enum): # sms.storage.AlarmType
         SpaceCapacityAlarm = 0
         CapabilityAlarm = 1
         StorageObjectAlarm = 2
         ObjectAlarm = 3
         ComplianceAlarm = 4
         ManageabilityAlarm = 5
         ReplicationAlarm = 6

      class BackingConfig(vmodl.DynamicData): # sms.storage.BackingConfig
         thinProvisionBackingIdentifier = ""
         deduplicationBackingIdentifier = ""
         autoTieringEnabled = False
         deduplicationEfficiency = 0
         performanceOptimizationInterval = 0

      class BackingStoragePool(vmodl.DynamicData): # sms.storage.BackingStoragePool
         uuid = ""
         type = ""
         capacityInMB = 0
         usedSpaceInMB = 0

         class BackingStoragePoolType(Enum): # sms.storage.BackingStoragePool.BackingStoragePoolType
            thinProvisioningPool = 0
            deduplicationPool = 1
            thinAndDeduplicationCombinedPool = 2

      class DatastoreBackingPoolMapping(vmodl.DynamicData): # sms.storage.DatastoreBackingPoolMapping
         datastore = [ vim.Datastore() ]
         backingStoragePool = [ sms.storage.BackingStoragePool() ]

      class DatastorePair(vmodl.DynamicData): # sms.storage.DatastorePair
         datastore1 = vim.Datastore()
         datastore2 = vim.Datastore()

      class DrsMigrationCapabilityResult(vmodl.DynamicData): # sms.storage.DrsMigrationCapabilityResult
         recommendedDatastorePair = [ sms.storage.DatastorePair() ]
         nonRecommendedDatastorePair = [ sms.storage.DatastorePair() ]

      class EntityType(Enum): # sms.storage.EntityType
         StorageArrayEntity = 0
         StorageProcessorEntity = 1
         StoragePortEntity = 2
         StorageLunEntity = 3
         StorageFileSystemEntity = 4
         StorageCapabilityEntity = 5
         CapabilitySchemaEntity = 6
         CapabilityProfileEntity = 7
         DefaultProfileEntity = 8
         ResourceAssociationEntity = 9
         StorageContainerEntity = 10
         StorageObjectEntity = 11
         MessageCatalogEntity = 12
         ProtocolEndpointEntity = 13
         VirtualVolumeInfoEntity = 14
         BackingStoragePoolEntity = 15
         FaultDomainEntity = 16
         ReplicationGroupEntity = 17

      class FaultDomainProviderMapping(vmodl.DynamicData): # sms.storage.FaultDomainProviderMapping
         activeProvider = sms.provider.Provider()
         faultDomainId = [ vim.vm.replication.FaultDomainId() ]

      class FileSystemInfo(vmodl.DynamicData): # sms.storage.FileSystemInfo
         fileServerName = ""
         fileSystemPath = ""
         ipAddress = ""

      class LunHbaAssociation(vmodl.DynamicData): # sms.storage.LunHbaAssociation
         canonicalName = ""
         hba = [ vim.host.HostBusAdapter() ]

      class NameValuePair(vmodl.DynamicData): # sms.storage.NameValuePair
         parameterName = ""
         parameterValue = ""

      class StorageAlarm(vmodl.DynamicData): # sms.storage.StorageAlarm
         alarmId = 0
         alarmType = ""
         containerId = ""
         objectId = ""
         objectType = ""
         status = ""
         alarmTimeStamp = vmodl.DateTime()
         messageId = ""
         parameterList = [ sms.storage.NameValuePair() ]
         alarmObject = {}

      class StorageArray(vmodl.DynamicData): # sms.storage.StorageArray
         name = ""
         uuid = ""
         vendorId = ""
         modelId = ""
         firmware = ""
         alternateName = [ "" ]
         supportedBlockInterface = [ "" ]
         supportedFileSystemInterface = [ "" ]
         supportedProfile = [ "" ]
         priority = 0

         class BlockDeviceInterface(Enum): # sms.storage.StorageArray.BlockDeviceInterface
            fc = 0
            iscsi = 1
            fcoe = 2
            otherBlock = 3

         class FileSystemInterface(Enum): # sms.storage.StorageArray.FileSystemInterface
            nfs = 0
            otherFileSystem = 1

         class VasaProfile(Enum): # sms.storage.StorageArray.VasaProfile
            blockDevice = 0
            fileSystem = 1
            capability = 2
            policy = 3
            object = 4
            statistics = 5
            storageDrsBlockDevice = 6
            storageDrsFileSystem = 7

      class StorageCapability(vmodl.DynamicData): # sms.storage.StorageCapability
         uuid = ""
         name = ""
         description = ""

      class StorageContainer(vmodl.DynamicData): # sms.storage.StorageContainer
         uuid = ""
         name = ""
         maxVvolSizeInMB = 0
         providerId = [ "" ]
         arrayId = [ "" ]

      class StorageContainerResult(vmodl.DynamicData): # sms.storage.StorageContainerResult
         storageContainer = [ sms.storage.StorageContainer() ]
         providerInfo = [ sms.provider.ProviderInfo() ]

      class StorageContainerSpec(vmodl.DynamicData): # sms.storage.StorageContainerSpec
         containerId = [ "" ]

      class StorageFileSystem(vmodl.DynamicData): # sms.storage.StorageFileSystem
         uuid = ""
         info = [ sms.storage.FileSystemInfo() ]
         nativeSnapshotSupported = False
         thinProvisioningStatus = ""
         type = ""
         version = ""
         backingConfig = sms.storage.BackingConfig()

         class FileSystemInterfaceVersion(Enum): # sms.storage.StorageFileSystem.FileSystemInterfaceVersion
            NFSV3_0 = 0

      class StorageLun(vmodl.DynamicData): # sms.storage.StorageLun
         uuid = ""
         vSphereLunIdentifier = ""
         vendorDisplayName = ""
         capacityInMB = 0
         usedSpaceInMB = 0
         lunThinProvisioned = False
         alternateIdentifier = [ "" ]
         drsManagementPermitted = False
         thinProvisioningStatus = ""
         backingConfig = sms.storage.BackingConfig()

      class StoragePort(vmodl.DynamicData): # sms.storage.StoragePort
         uuid = ""
         type = ""
         alternateName = [ "" ]

      class StorageProcessor(vmodl.DynamicData): # sms.storage.StorageProcessor
         uuid = ""
         alternateIdentifer = [ "" ]

      class ThinProvisioningStatus(Enum): # sms.storage.ThinProvisioningStatus
         RED = 0
         YELLOW = 1
         GREEN = 2

      class replication(object): # (unknown name)

         class DeviceId(vmodl.DynamicData): # sms.storage.replication.DeviceId
            pass

         class FailoverParam(vmodl.DynamicData): # sms.storage.replication.FailoverParam
            isPlanned = False
            checkOnly = False
            replicationGroupsToFailover = [ sms.storage.replication.FailoverParam.ReplicationGroupData() ]
            policyAssociations = [ sms.storage.replication.FailoverParam.PolicyAssociation() ]

            class ReplicationGroupData(vmodl.DynamicData): # sms.storage.replication.FailoverParam.ReplicationGroupData
               groupId = vim.vm.replication.ReplicationGroupId()
               pitId = sms.storage.replication.PointInTimeReplicaId()

            class PolicyAssociation(vmodl.DynamicData): # sms.storage.replication.FailoverParam.PolicyAssociation
               id = sms.storage.replication.DeviceId()
               policyId = ""
               datastore = vim.Datastore()

         class FaultDomainInfo(vim.vm.replication.FaultDomainId): # sms.storage.replication.FaultDomainInfo
            name = ""
            description = ""
            storageArrayId = ""
            children = [ vim.vm.replication.FaultDomainId() ]
            provider = sms.provider.Provider()

         class GroupInfo(vmodl.DynamicData): # sms.storage.replication.GroupInfo
            groupId = vim.vm.replication.ReplicationGroupId()

         class GroupOperationResult(vmodl.DynamicData): # sms.storage.replication.GroupOperationResult
            groupId = vim.vm.replication.ReplicationGroupId()
            warning = [ vmodl.MethodFault() ]

         class PointInTimeReplicaId(vmodl.DynamicData): # sms.storage.replication.PointInTimeReplicaId
            id = ""

         class PromoteParam(vmodl.DynamicData): # sms.storage.replication.PromoteParam
            isPlanned = False
            replicationGroupsToPromote = [ vim.vm.replication.ReplicationGroupId() ]

         class QueryPointInTimeReplicaParam(vmodl.DynamicData): # sms.storage.replication.QueryPointInTimeReplicaParam
            replicaTimeQueryParam = sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam()
            pitName = ""
            tags = [ "" ]

            class ReplicaQueryIntervalParam(vmodl.DynamicData): # sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam
               fromDate = vmodl.DateTime()
               toDate = vmodl.DateTime()
               number = 0

         class QueryPointInTimeReplicaSuccessResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.QueryPointInTimeReplicaSuccessResult
            replicaInfo = [ sms.storage.replication.QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo() ]

            class PointInTimeReplicaInfo(vmodl.DynamicData): # sms.storage.replication.QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo
               id = sms.storage.replication.PointInTimeReplicaId()
               pitName = ""
               timeStamp = vmodl.DateTime()
               tags = [ "" ]

         class QueryPointInTimeReplicaSummaryResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.QueryPointInTimeReplicaSummaryResult
            intervalResults = [ sms.storage.replication.QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult() ]

            class ReplicaIntervalQueryResult(vmodl.DynamicData): # sms.storage.replication.QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult
               fromDate = vmodl.DateTime()
               toDate = vmodl.DateTime()
               number = 0

         class QueryReplicationGroupSuccessResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.QueryReplicationGroupSuccessResult
            rgInfo = sms.storage.replication.GroupInfo()

         class QueryReplicationPeerResult(vmodl.DynamicData): # sms.storage.replication.QueryReplicationPeerResult
            sourceDomain = vim.vm.replication.FaultDomainId()
            targetDomain = [ vim.vm.replication.FaultDomainId() ]
            error = [ vmodl.MethodFault() ]
            warning = [ vmodl.MethodFault() ]

         class ReplicaId(vmodl.DynamicData): # sms.storage.replication.ReplicaId
            id = ""

         class ReplicationState(Enum): # sms.storage.replication.ReplicationState
            SOURCE = 0
            TARGET = 1
            FAILEDOVER = 2
            INTEST = 3
            REMOTE_FAILEDOVER = 4

         class ReverseReplicationSuccessResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.ReverseReplicationSuccessResult
            newGroupId = vim.vm.replication.DeviceGroupId()

         class SourceGroupInfo(sms.storage.replication.GroupInfo): # sms.storage.replication.SourceGroupInfo
            name = ""
            description = ""
            state = ""
            replica = [ sms.storage.replication.SourceGroupInfo.ReplicationTargetInfo() ]
            memberInfo = [ sms.storage.replication.SourceGroupMemberInfo() ]

            class ReplicationTargetInfo(vmodl.DynamicData): # sms.storage.replication.SourceGroupInfo.ReplicationTargetInfo
               targetGroupId = vim.vm.replication.ReplicationGroupId()
               replicationAgreementDescription = ""

         class SourceGroupMemberInfo(vmodl.DynamicData): # sms.storage.replication.SourceGroupMemberInfo
            deviceId = sms.storage.replication.DeviceId()
            targetId = [ sms.storage.replication.SourceGroupMemberInfo.TargetDeviceId() ]

            class TargetDeviceId(vmodl.DynamicData): # sms.storage.replication.SourceGroupMemberInfo.TargetDeviceId
               domainId = vim.vm.replication.FaultDomainId()
               deviceId = sms.storage.replication.ReplicaId()

         class SyncReplicationGroupSuccessResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.SyncReplicationGroupSuccessResult
            timeStamp = vmodl.DateTime()
            pitId = sms.storage.replication.PointInTimeReplicaId()
            pitName = ""

         class TargetGroupInfo(sms.storage.replication.GroupInfo): # sms.storage.replication.TargetGroupInfo
            sourceInfo = sms.storage.replication.TargetGroupInfo.TargetToSourceInfo()
            state = ""
            devices = [ sms.storage.replication.TargetGroupMemberInfo() ]
            isPromoteCapable = False

            class TargetToSourceInfo(vmodl.DynamicData): # sms.storage.replication.TargetGroupInfo.TargetToSourceInfo
               sourceGroupId = vim.vm.replication.ReplicationGroupId()
               replicationAgreementDescription = ""

         class TargetGroupMemberInfo(vmodl.DynamicData): # sms.storage.replication.TargetGroupMemberInfo
            replicaId = sms.storage.replication.ReplicaId()
            sourceId = sms.storage.replication.DeviceId()
            targetDatastore = vim.Datastore()

         class TestFailoverParam(sms.storage.replication.FailoverParam): # sms.storage.replication.TestFailoverParam
            pass

         class VVolId(sms.storage.replication.DeviceId): # sms.storage.replication.VVolId
            id = ""

         class VirtualDiskId(sms.storage.replication.DeviceId): # sms.storage.replication.VirtualDiskId
            diskId = ""

         class VirtualDiskKey(sms.storage.replication.DeviceId): # sms.storage.replication.VirtualDiskKey
            vmInstanceUUID = ""
            deviceKey = 0

         class VirtualDiskMoId(sms.storage.replication.DeviceId): # sms.storage.replication.VirtualDiskMoId
            vcUuid = ""
            vmMoid = ""
            diskKey = ""

         class VirtualMachineId(sms.storage.replication.DeviceId): # sms.storage.replication.VirtualMachineId
            pass

         class VirtualMachineMoId(sms.storage.replication.VirtualMachineId): # sms.storage.replication.VirtualMachineMoId
            vcUuid = ""
            vmMoid = ""

         class VirtualMachineUUID(sms.storage.replication.VirtualMachineId): # sms.storage.replication.VirtualMachineUUID
            vmInstanceUUID = ""

         class FailoverSuccessResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.FailoverSuccessResult
            newState = ""
            pitId = sms.storage.replication.PointInTimeReplicaId()
            pitIdBeforeFailover = sms.storage.replication.PointInTimeReplicaId()
            recoveredDeviceInfo = [ sms.storage.replication.FailoverSuccessResult.RecoveredDevice() ]
            timeStamp = vmodl.DateTime()

            class RecoveredDiskInfo(vmodl.DynamicData): # sms.storage.replication.FailoverSuccessResult.RecoveredDiskInfo
               deviceKey = 0
               dsUrl = ""
               diskPath = ""

            class RecoveredDevice(vmodl.DynamicData): # sms.storage.replication.FailoverSuccessResult.RecoveredDevice
               targetDeviceId = sms.storage.replication.ReplicaId()
               recoveredDeviceId = sms.storage.replication.DeviceId()
               sourceDeviceId = sms.storage.replication.DeviceId()
               info = [ "" ]
               datastore = vim.Datastore()
               recoveredDiskInfo = [ sms.storage.replication.FailoverSuccessResult.RecoveredDiskInfo() ]
               error = vmodl.MethodFault()
               warnings = [ vmodl.MethodFault() ]

         class GroupErrorResult(sms.storage.replication.GroupOperationResult): # sms.storage.replication.GroupErrorResult
            error = [ vmodl.MethodFault() ]

         class RecoveredTargetGroupMemberInfo(sms.storage.replication.TargetGroupMemberInfo): # sms.storage.replication.RecoveredTargetGroupMemberInfo
            recoveredDeviceId = sms.storage.replication.DeviceId()

         class VirtualMachineFilePath(sms.storage.replication.VirtualMachineId): # sms.storage.replication.VirtualMachineFilePath
            vcUuid = ""
            dsUrl = ""
            vmxPath = ""

      class FcStoragePort(sms.storage.StoragePort): # sms.storage.FcStoragePort
         portWwn = ""
         nodeWwn = ""

      class FcoeStoragePort(sms.storage.StoragePort): # sms.storage.FcoeStoragePort
         portWwn = ""
         nodeWwn = ""

      class IscsiStoragePort(sms.storage.StoragePort): # sms.storage.IscsiStoragePort
         identifier = ""
