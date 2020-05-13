from enum import Enum

class sms(object):

   class AboutInfo(vmodl.DynamicData):
      name = ""
      fullName = ""
      vendor = ""
      apiVersion = ""
      instanceUuid = ""
      vasaApiVersion = ""

   class EntityReference(vmodl.DynamicData):
      id = ""
      type = sms.EntityReference.EntityType()

      class EntityType(Enum):
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

   class FaultDomainFilter(vmodl.DynamicData):
      providerId = ""

   class ReplicationGroupFilter(vmodl.DynamicData):
      groupId = [ vim.vm.replication.ReplicationGroupId() ]

   class ServiceInstance(vmodl.ManagedObject):

      def queryStorageManager():
         return sms.StorageManager()

      def querySessionManager():
         return sms.auth.SessionManager()

      def queryAboutInfo():
         return sms.AboutInfo()

   class StorageManager(vmodl.ManagedObject):

      def registerProvider(providerSpec=sms.provider.ProviderSpec()):
         # throws vim.fault.AlreadyExists, sms.fault.ProviderRegistrationFault
         return sms.Task()

      def unregisterProvider(providerId=""):
         # throws vim.fault.NotFound, sms.fault.ProviderUnregistrationFault
         return sms.Task()

      def queryProvider():
         # throws sms.fault.QueryExecutionFault
         return [ sms.provider.Provider() ]

      def queryArray(providerId=[ "" ] or None):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageArray() ]

      def queryProcessorAssociatedWithArray(arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageProcessor() ]

      def queryPortAssociatedWithArray(arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StoragePort() ]

      def queryPortAssociatedWithLun(scsi3Id="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StoragePort()

      def queryLunAssociatedWithPort(portId="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageLun() ]

      def queryArrayAssociatedWithLun(canonicalName=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageArray()

      def queryPortAssociatedWithProcessor(processorId="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StoragePort() ]

      def queryLunAssociatedWithArray(arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageLun() ]

      def queryFileSystemAssociatedWithArray(arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.StorageFileSystem() ]

      def queryDatastoreCapability(datastore=vim.Datastore()):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageCapability()

      def queryHostAssociatedWithLun(scsi3Id="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ vim.HostSystem() ]

      def queryVmfsDatastoreAssociatedWithLun(scsi3Id="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return vim.Datastore()

      def queryNfsDatastoreAssociatedWithFileSystem(fileSystemId="", arrayId=""):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return vim.Datastore()

      def queryDrsMigrationCapabilityForPerformance(srcDatastore=vim.Datastore(), dstDatastore=vim.Datastore()):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return False

      def queryDrsMigrationCapabilityForPerformanceEx(datastore=[ vim.Datastore() ]):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.DrsMigrationCapabilityResult()

      def queryStorageContainer(containerSpec=sms.storage.StorageContainerSpec() or None):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return sms.storage.StorageContainerResult()

      def queryAssociatedBackingStoragePool(entityId="" or None, entityType="" or None):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.BackingStoragePool() ]

      def queryDatastoreBackingPoolMapping(datastore=[ vim.Datastore() ]):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ sms.storage.DatastoreBackingPoolMapping() ]

      def refreshCACertificatesAndCRLs(providerId=[ "" ] or None):
         # throws vim.fault.NotFound, sms.fault.CertificateRefreshFailed
         return sms.Task()

      def queryFaultDomain(filter=sms.FaultDomainFilter() or None):
         # throws vim.fault.NotFound, sms.fault.QueryExecutionFault
         return [ vim.vm.replication.FaultDomainId() ]

      def queryReplicationGroupInfo(rgFilter=sms.ReplicationGroupFilter()):
         # throws sms.fault.QueryExecutionFault
         return [ sms.storage.replication.GroupOperationResult() ]

   class Task(vmodl.ManagedObject):

      def queryResult():
         return anyType()

      def queryInfo():
         return sms.TaskInfo()

   class TaskInfo(vmodl.DynamicData):
      key = ""
      task = sms.Task()
      object = vmodl.ManagedObject()
      error = vmodl.MethodFault()
      result = anyType()
      startTime = vmodl.DateTime()
      completionTime = vmodl.DateTime()
      state = ""
      progress = 0

      class State(Enum):
         queued = 0
         running = 1
         success = 2
         error = 3

   class fault(object):

      class AuthConnectionFailed(vim.fault.NoPermission):
         pass

      class CertificateRefreshFailed(vmodl.MethodFault):
         providerId = [ "" ]

      class CertificateRevocationFailed(vmodl.MethodFault):
         pass

      class DuplicateEntry(vmodl.MethodFault):
         pass

      class InactiveProvider(vmodl.MethodFault):
         mapping = [ sms.storage.FaultDomainProviderMapping() ]

      class InvalidLogin(vmodl.MethodFault):
         pass

      class InvalidProfile(vmodl.MethodFault):
         pass

      class InvalidSession(vim.fault.NoPermission):
         sessionCookie = ""

      class MultipleSortSpecsNotSupported(vmodl.fault.InvalidArgument):
         pass

      class NotSupportedByProvider(vmodl.MethodFault):
         pass

      class ProviderBusy(vmodl.MethodFault):
         pass

      class ProviderConnectionFailed(vmodl.RuntimeFault):
         pass

      class ProviderOutOfProvisioningResource(vmodl.MethodFault):
         provisioningResourceId = ""
         availableBefore = 0
         availableAfter = 0
         total = 0
         isTransient = False

      class ProviderOutOfResource(vmodl.MethodFault):
         pass

      class ProviderRegistrationFault(vmodl.MethodFault):
         pass

      class ProviderSyncFailed(vmodl.MethodFault):
         pass

      class ProviderUnavailable(vmodl.MethodFault):
         pass

      class ProviderUnregistrationFault(vmodl.MethodFault):
         pass

      class ProxyRegistrationFailed(vmodl.RuntimeFault):
         pass

      class QueryExecutionFault(vmodl.MethodFault):
         pass

      class QueryNotSupported(vmodl.fault.InvalidArgument):
         entityType = sms.EntityReference.EntityType()
         relatedEntityType = sms.EntityReference.EntityType()

      class ResourceInUse(vim.fault.ResourceInUse):
         deviceIds = [ sms.storage.replication.DeviceId() ]

      class ServiceNotInitialized(vmodl.RuntimeFault):
         pass

      class SyncInProgress(sms.fault.ProviderSyncFailed):
         pass

      class TooMany(vmodl.MethodFault):
         maxBatchSize = 0

      class replication(object):

         class ReplicationFault(vmodl.MethodFault):
            pass

         class SyncOngoing(sms.fault.replication.ReplicationFault):
            task = sms.Task()

         class AlreadyDone(sms.fault.replication.ReplicationFault):
            pass

         class InvalidFunctionTarget(sms.fault.replication.ReplicationFault):
            pass

         class InvalidReplicationState(sms.fault.replication.ReplicationFault):
            desiredState = [ "" ]
            currentState = ""

         class NoReplicationTarget(sms.fault.replication.ReplicationFault):
            pass

         class NoValidReplica(sms.fault.replication.ReplicationFault):
            deviceId = sms.storage.replication.DeviceId()

         class PeerNotReachable(sms.fault.replication.ReplicationFault):
            pass

      class CertificateAuthorityFault(sms.fault.ProviderRegistrationFault):
         faultCode = 0

      class CertificateNotImported(sms.fault.ProviderRegistrationFault):
         pass

      class CertificateNotTrusted(sms.fault.ProviderRegistrationFault):
         certificate = ""

      class IncorrectUsernamePassword(sms.fault.ProviderRegistrationFault):
         pass

      class InvalidCertificate(sms.fault.ProviderRegistrationFault):
         certificate = ""

      class InvalidUrl(sms.fault.ProviderRegistrationFault):
         url = ""

      class NoCommonProviderForAllBackings(sms.fault.QueryExecutionFault):
         pass

      class ProviderNotFound(sms.fault.QueryExecutionFault):
         pass

   class provider(object):

      class AlarmFilter(vmodl.DynamicData):
         alarmStatus = ""
         alarmType = ""
         entityType = ""
         entityId = [ anyType() ]
         pageMarker = ""

      class AlarmResult(vmodl.DynamicData):
         storageAlarm = [ sms.storage.StorageAlarm() ]
         pageMarker = ""

      class Provider(vmodl.ManagedObject):

         def queryProviderInfo():
            return sms.provider.ProviderInfo()

      class ProviderInfo(vmodl.DynamicData):
         uid = ""
         name = ""
         description = ""
         version = ""

      class ProviderSpec(vmodl.DynamicData):
         name = ""
         description = ""

      class VasaProvider(sms.provider.Provider):

         def sync(arrayId="" or None):
            # throws sms.fault.ProviderSyncFailed
            return sms.Task()

         def refreshCertificate():
            # throws sms.fault.CertificateRefreshFailed
            return sms.Task()

         def revokeCertificate():
            # throws sms.fault.CertificateRevocationFailed
            return sms.Task()

         def reconnect():
            # throws sms.fault.InvalidCertificate, sms.fault.ProviderConnectionFailed
            return sms.Task()

         def queryReplicationPeer(faultDomainId=[ vim.vm.replication.FaultDomainId() ] or None):
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.QueryReplicationPeerResult() ]

         def queryReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None):
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.GroupOperationResult() ]

         def queryPointInTimeReplica(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, queryParam=sms.storage.replication.QueryPointInTimeReplicaParam() or None):
            # throws sms.fault.ProviderUnavailable, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.QueryExecutionFault
            return [ sms.storage.replication.GroupOperationResult() ]

         def testFailoverReplicationGroupStart(testFailoverParam=sms.storage.replication.TestFailoverParam()):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def testFailoverReplicationGroupStop(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, force=False):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault, sms.fault.NotSupportedByProvider
            return sms.Task()

         def promoteReplicationGroup(promoteParam=sms.storage.replication.PromoteParam()):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def syncReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None, pitName=""):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault, sms.fault.TooMany
            return sms.Task()

         def prepareFailoverReplicationGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def failoverReplicationGroup(failoverParam=sms.storage.replication.FailoverParam()):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def reverseReplicateGroup(groupId=[ vim.vm.replication.ReplicationGroupId() ] or None):
            # throws sms.fault.ProviderUnavailable, sms.fault.ProviderOutOfResource, sms.fault.InactiveProvider, sms.fault.TooMany, sms.fault.ProviderBusy, sms.fault.replication.ReplicationFault
            return sms.Task()

         def queryActiveAlarm(alarmFilter=sms.provider.AlarmFilter() or None):
            # throws vim.fault.NotFound, sms.fault.ProviderBusy, sms.fault.InactiveProvider, sms.fault.ProviderUnavailable, sms.fault.QueryExecutionFault
            return sms.provider.AlarmResult()

      class VasaProviderInfo(sms.provider.ProviderInfo):
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

         class CertificateStatus(Enum):
            valid = 0
            expirySoftLimitReached = 1
            expiryHardLimitReached = 2
            expired = 3
            invalid = 4

         class RelatedStorageArray(vmodl.DynamicData):
            arrayId = ""
            active = False
            manageable = False
            priority = 0

         class SupportedVendorModelMapping(vmodl.DynamicData):
            vendorId = ""
            modelId = ""

         class VasaProviderStatus(Enum):
            online = 0
            offline = 1
            syncError = 2
            unknown = 3
            connected = 4
            disconnected = 5

         class VasaProviderProfile(Enum):
            blockDevice = 0
            fileSystem = 1
            capability = 2

         class ProviderProfile(Enum):
            ProfileBasedManagement = 0
            Replication = 1

         class Type(Enum):
            PERSISTENCE = 0
            DATASERVICE = 1
            UNKNOWN = 2

         class Category(Enum):
            internal = 0
            external = 1

      class VasaProviderSpec(sms.provider.ProviderSpec):
         username = ""
         password = ""
         url = ""
         certificate = ""

      class VmodlVasaProviderSpec(object):

         class AuthenticationType(Enum):
            LoginByToken = 0
            UseSessionId = 1

   class storage(object):

      class AlarmStatus(Enum):
         Red = 0
         Green = 1
         Yellow = 2

      class AlarmType(Enum):
         SpaceCapacityAlarm = 0
         CapabilityAlarm = 1
         StorageObjectAlarm = 2
         ObjectAlarm = 3
         ComplianceAlarm = 4
         ManageabilityAlarm = 5
         ReplicationAlarm = 6

      class BackingConfig(vmodl.DynamicData):
         thinProvisionBackingIdentifier = ""
         deduplicationBackingIdentifier = ""
         autoTieringEnabled = False
         deduplicationEfficiency = 0
         performanceOptimizationInterval = 0

      class BackingStoragePool(vmodl.DynamicData):
         uuid = ""
         type = ""
         capacityInMB = 0
         usedSpaceInMB = 0

         class BackingStoragePoolType(Enum):
            thinProvisioningPool = 0
            deduplicationPool = 1
            thinAndDeduplicationCombinedPool = 2

      class DatastoreBackingPoolMapping(vmodl.DynamicData):
         datastore = [ vim.Datastore() ]
         backingStoragePool = [ sms.storage.BackingStoragePool() ]

      class DatastorePair(vmodl.DynamicData):
         datastore1 = vim.Datastore()
         datastore2 = vim.Datastore()

      class DrsMigrationCapabilityResult(vmodl.DynamicData):
         recommendedDatastorePair = [ sms.storage.DatastorePair() ]
         nonRecommendedDatastorePair = [ sms.storage.DatastorePair() ]

      class EntityType(Enum):
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

      class FaultDomainProviderMapping(vmodl.DynamicData):
         activeProvider = sms.provider.Provider()
         faultDomainId = [ vim.vm.replication.FaultDomainId() ]

      class FileSystemInfo(vmodl.DynamicData):
         fileServerName = ""
         fileSystemPath = ""
         ipAddress = ""

      class LunHbaAssociation(vmodl.DynamicData):
         canonicalName = ""
         hba = [ vim.host.HostBusAdapter() ]

      class NameValuePair(vmodl.DynamicData):
         parameterName = ""
         parameterValue = ""

      class StorageAlarm(vmodl.DynamicData):
         alarmId = 0
         alarmType = ""
         containerId = ""
         objectId = ""
         objectType = ""
         status = ""
         alarmTimeStamp = vmodl.DateTime()
         messageId = ""
         parameterList = [ sms.storage.NameValuePair() ]
         alarmObject = anyType()

      class StorageArray(vmodl.DynamicData):
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

         class BlockDeviceInterface(Enum):
            fc = 0
            iscsi = 1
            fcoe = 2
            otherBlock = 3

         class FileSystemInterface(Enum):
            nfs = 0
            otherFileSystem = 1

         class VasaProfile(Enum):
            blockDevice = 0
            fileSystem = 1
            capability = 2
            policy = 3
            object = 4
            statistics = 5
            storageDrsBlockDevice = 6
            storageDrsFileSystem = 7

      class StorageCapability(vmodl.DynamicData):
         uuid = ""
         name = ""
         description = ""

      class StorageContainer(vmodl.DynamicData):
         uuid = ""
         name = ""
         maxVvolSizeInMB = 0
         providerId = [ "" ]
         arrayId = [ "" ]

      class StorageContainerResult(vmodl.DynamicData):
         storageContainer = [ sms.storage.StorageContainer() ]
         providerInfo = [ sms.provider.ProviderInfo() ]

      class StorageContainerSpec(vmodl.DynamicData):
         containerId = [ "" ]

      class StorageFileSystem(vmodl.DynamicData):
         uuid = ""
         info = [ sms.storage.FileSystemInfo() ]
         nativeSnapshotSupported = False
         thinProvisioningStatus = ""
         type = ""
         version = ""
         backingConfig = sms.storage.BackingConfig()

         class FileSystemInterfaceVersion(Enum):
            NFSV3_0 = 0

      class StorageLun(vmodl.DynamicData):
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

      class StoragePort(vmodl.DynamicData):
         uuid = ""
         type = ""
         alternateName = [ "" ]

      class StorageProcessor(vmodl.DynamicData):
         uuid = ""
         alternateIdentifer = [ "" ]

      class ThinProvisioningStatus(Enum):
         RED = 0
         YELLOW = 1
         GREEN = 2

      class replication(object):

         class DeviceId(vmodl.DynamicData):
            pass

         class FailoverParam(vmodl.DynamicData):
            isPlanned = False
            checkOnly = False
            replicationGroupsToFailover = [ sms.storage.replication.FailoverParam.ReplicationGroupData() ]
            policyAssociations = [ sms.storage.replication.FailoverParam.PolicyAssociation() ]

            class ReplicationGroupData(vmodl.DynamicData):
               groupId = vim.vm.replication.ReplicationGroupId()
               pitId = sms.storage.replication.PointInTimeReplicaId()

            class PolicyAssociation(vmodl.DynamicData):
               id = sms.storage.replication.DeviceId()
               policyId = ""
               datastore = vim.Datastore()

         class FaultDomainInfo(vim.vm.replication.FaultDomainId):
            name = ""
            description = ""
            storageArrayId = ""
            children = [ vim.vm.replication.FaultDomainId() ]
            provider = sms.provider.Provider()

         class GroupInfo(vmodl.DynamicData):
            groupId = vim.vm.replication.ReplicationGroupId()

         class GroupOperationResult(vmodl.DynamicData):
            groupId = vim.vm.replication.ReplicationGroupId()
            warning = [ vmodl.MethodFault() ]

         class PointInTimeReplicaId(vmodl.DynamicData):
            id = ""

         class PromoteParam(vmodl.DynamicData):
            isPlanned = False
            replicationGroupsToPromote = [ vim.vm.replication.ReplicationGroupId() ]

         class QueryPointInTimeReplicaParam(vmodl.DynamicData):
            replicaTimeQueryParam = sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam()
            pitName = ""
            tags = [ "" ]

            class ReplicaQueryIntervalParam(vmodl.DynamicData):
               fromDate = vmodl.DateTime()
               toDate = vmodl.DateTime()
               number = 0

         class QueryPointInTimeReplicaSuccessResult(sms.storage.replication.GroupOperationResult):
            replicaInfo = [ sms.storage.replication.QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo() ]

            class PointInTimeReplicaInfo(vmodl.DynamicData):
               id = sms.storage.replication.PointInTimeReplicaId()
               pitName = ""
               timeStamp = vmodl.DateTime()
               tags = [ "" ]

         class QueryPointInTimeReplicaSummaryResult(sms.storage.replication.GroupOperationResult):
            intervalResults = [ sms.storage.replication.QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult() ]

            class ReplicaIntervalQueryResult(vmodl.DynamicData):
               fromDate = vmodl.DateTime()
               toDate = vmodl.DateTime()
               number = 0

         class QueryReplicationGroupSuccessResult(sms.storage.replication.GroupOperationResult):
            rgInfo = sms.storage.replication.GroupInfo()

         class QueryReplicationPeerResult(vmodl.DynamicData):
            sourceDomain = vim.vm.replication.FaultDomainId()
            targetDomain = [ vim.vm.replication.FaultDomainId() ]
            error = [ vmodl.MethodFault() ]
            warning = [ vmodl.MethodFault() ]

         class ReplicaId(vmodl.DynamicData):
            id = ""

         class ReplicationState(Enum):
            SOURCE = 0
            TARGET = 1
            FAILEDOVER = 2
            INTEST = 3
            REMOTE_FAILEDOVER = 4

         class ReverseReplicationSuccessResult(sms.storage.replication.GroupOperationResult):
            newGroupId = vim.vm.replication.DeviceGroupId()

         class SourceGroupInfo(sms.storage.replication.GroupInfo):
            name = ""
            description = ""
            state = ""
            replica = [ sms.storage.replication.SourceGroupInfo.ReplicationTargetInfo() ]
            memberInfo = [ sms.storage.replication.SourceGroupMemberInfo() ]

            class ReplicationTargetInfo(vmodl.DynamicData):
               targetGroupId = vim.vm.replication.ReplicationGroupId()
               replicationAgreementDescription = ""

         class SourceGroupMemberInfo(vmodl.DynamicData):
            deviceId = sms.storage.replication.DeviceId()
            targetId = [ sms.storage.replication.SourceGroupMemberInfo.TargetDeviceId() ]

            class TargetDeviceId(vmodl.DynamicData):
               domainId = vim.vm.replication.FaultDomainId()
               deviceId = sms.storage.replication.ReplicaId()

         class SyncReplicationGroupSuccessResult(sms.storage.replication.GroupOperationResult):
            timeStamp = vmodl.DateTime()
            pitId = sms.storage.replication.PointInTimeReplicaId()
            pitName = ""

         class TargetGroupInfo(sms.storage.replication.GroupInfo):
            sourceInfo = sms.storage.replication.TargetGroupInfo.TargetToSourceInfo()
            state = ""
            devices = [ sms.storage.replication.TargetGroupMemberInfo() ]
            isPromoteCapable = False

            class TargetToSourceInfo(vmodl.DynamicData):
               sourceGroupId = vim.vm.replication.ReplicationGroupId()
               replicationAgreementDescription = ""

         class TargetGroupMemberInfo(vmodl.DynamicData):
            replicaId = sms.storage.replication.ReplicaId()
            sourceId = sms.storage.replication.DeviceId()
            targetDatastore = vim.Datastore()

         class TestFailoverParam(sms.storage.replication.FailoverParam):
            pass

         class VVolId(sms.storage.replication.DeviceId):
            id = ""

         class VirtualDiskId(sms.storage.replication.DeviceId):
            diskId = ""

         class VirtualDiskKey(sms.storage.replication.DeviceId):
            vmInstanceUUID = ""
            deviceKey = 0

         class VirtualDiskMoId(sms.storage.replication.DeviceId):
            vcUuid = ""
            vmMoid = ""
            diskKey = ""

         class VirtualMachineId(sms.storage.replication.DeviceId):
            pass

         class VirtualMachineMoId(sms.storage.replication.VirtualMachineId):
            vcUuid = ""
            vmMoid = ""

         class VirtualMachineUUID(sms.storage.replication.VirtualMachineId):
            vmInstanceUUID = ""

         class FailoverSuccessResult(sms.storage.replication.GroupOperationResult):
            newState = ""
            pitId = sms.storage.replication.PointInTimeReplicaId()
            pitIdBeforeFailover = sms.storage.replication.PointInTimeReplicaId()
            recoveredDeviceInfo = [ sms.storage.replication.FailoverSuccessResult.RecoveredDevice() ]
            timeStamp = vmodl.DateTime()

            class RecoveredDiskInfo(vmodl.DynamicData):
               deviceKey = 0
               dsUrl = ""
               diskPath = ""

            class RecoveredDevice(vmodl.DynamicData):
               targetDeviceId = sms.storage.replication.ReplicaId()
               recoveredDeviceId = sms.storage.replication.DeviceId()
               sourceDeviceId = sms.storage.replication.DeviceId()
               info = [ "" ]
               datastore = vim.Datastore()
               recoveredDiskInfo = [ sms.storage.replication.FailoverSuccessResult.RecoveredDiskInfo() ]
               error = vmodl.MethodFault()
               warnings = [ vmodl.MethodFault() ]

         class GroupErrorResult(sms.storage.replication.GroupOperationResult):
            error = [ vmodl.MethodFault() ]

         class RecoveredTargetGroupMemberInfo(sms.storage.replication.TargetGroupMemberInfo):
            recoveredDeviceId = sms.storage.replication.DeviceId()

         class VirtualMachineFilePath(sms.storage.replication.VirtualMachineId):
            vcUuid = ""
            dsUrl = ""
            vmxPath = ""

      class FcStoragePort(sms.storage.StoragePort):
         portWwn = ""
         nodeWwn = ""

      class FcoeStoragePort(sms.storage.StoragePort):
         portWwn = ""
         nodeWwn = ""

      class IscsiStoragePort(sms.storage.StoragePort):
         identifier = ""
