from enum import Enum

class pbm(object): # (unknown name)

   class AboutInfo(vmodl.DynamicData): # pbm.AboutInfo
      name = ""
      version = ""
      instanceUuid = ""

   class ExtendedElementDescription(vmodl.DynamicData): # pbm.ExtendedElementDescription
      label = ""
      summary = ""
      key = ""
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ServerObjectRef(vmodl.DynamicData): # pbm.ServerObjectRef
      objectType = ""
      key = ""
      serverUuid = ""

      class VvolType(Enum): # pbm.ServerObjectRef.VvolType
         Config = 0
         Data = 1
         Swap = 2

      class ObjectType(Enum): # pbm.ServerObjectRef.ObjectType
         virtualMachine = 0
         virtualMachineAndDisks = 1
         virtualDiskId = 2
         virtualDiskUUID = 3
         datastore = 4
         vsanObjectId = 5
         fileShareId = 6
         host = 7
         cluster = 8
         unknown = 9

   class ServiceInstance(vmodl.ManagedObject): # pbm.ServiceInstance
      content = pbm.ServiceInstanceContent()

      def retrieveContent(): # pbm.ServiceInstance.retrieveContent
         return pbm.ServiceInstanceContent()

   class ServiceInstanceContent(vmodl.DynamicData): # pbm.ServiceInstanceContent
      aboutInfo = pbm.AboutInfo()
      sessionManager = pbm.auth.SessionManager()
      capabilityMetadataManager = pbm.capability.CapabilityMetadataManager()
      profileManager = pbm.profile.ProfileManager()
      complianceManager = pbm.compliance.ComplianceManager()
      placementSolver = pbm.placement.PlacementSolver()
      replicationManager = pbm.replication.ReplicationManager()

   class auth(object): # (unknown name)

      class SessionManager(vmodl.ManagedObject): # pbm.auth.SessionManager
         pass

   class capability(object): # (unknown name)

      class CapabilityMetadata(vmodl.DynamicData): # pbm.capability.CapabilityMetadata
         id = pbm.capability.CapabilityMetadata.UniqueId()
         summary = pbm.ExtendedElementDescription()
         mandatory = False
         hint = False
         keyId = ""
         allowMultipleConstraints = False
         propertyMetadata = [ pbm.capability.PropertyMetadata() ]

         class UniqueId(vmodl.DynamicData): # pbm.capability.CapabilityMetadata.UniqueId
            namespace = ""
            id = ""

      class CapabilityMetadataManager(vmodl.ManagedObject): # pbm.capability.CapabilityMetadataManager
         pass

      class ConstraintInstance(vmodl.DynamicData): # pbm.capability.ConstraintInstance
         propertyInstance = [ pbm.capability.PropertyInstance() ]

      class Operator(Enum): # pbm.capability.Operator
         NOT = 0

      class PropertyInstance(vmodl.DynamicData): # pbm.capability.PropertyInstance
         id = ""
         operator = ""
         value = {}

      class PropertyMetadata(vmodl.DynamicData): # pbm.capability.PropertyMetadata
         id = ""
         summary = pbm.ExtendedElementDescription()
         mandatory = False
         type = pbm.capability.TypeInfo()
         defaultValue = {}
         allowedValue = {}
         requirementsTypeHint = ""

      class TypeInfo(vmodl.DynamicData): # pbm.capability.TypeInfo
         typeName = ""

      class provider(object): # (unknown name)

         class CapabilityObjectMetadataPerCategory(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectMetadataPerCategory
            subCategory = ""
            capabilityMetadata = [ pbm.capability.CapabilityMetadata() ]

         class CapabilityObjectSchema(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectSchema
            vendorInfo = pbm.capability.provider.CapabilityObjectSchema.VendorInfo()
            namespaceInfo = pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo()
            lineOfService = pbm.capability.provider.LineOfServiceInfo()
            capabilityMetadataPerCategory = [ pbm.capability.provider.CapabilityObjectMetadataPerCategory() ]

            class VendorInfo(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectSchema.VendorInfo
               vendorUuid = ""
               info = pbm.ExtendedElementDescription()

            class NamespaceInfo(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo
               version = ""
               namespace = ""
               info = pbm.ExtendedElementDescription()

            class VendorResourceTypeInfo(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo
               resourceType = ""
               vendorNamespaceInfo = [ pbm.capability.provider.CapabilityObjectSchema.VendorNamespaceInfo() ]

            class VendorNamespaceInfo(vmodl.DynamicData): # pbm.capability.provider.CapabilityObjectSchema.VendorNamespaceInfo
               vendorInfo = pbm.capability.provider.CapabilityObjectSchema.VendorInfo()
               namespaceInfo = pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo()

         class LineOfServiceInfo(vmodl.DynamicData): # pbm.capability.provider.LineOfServiceInfo
            lineOfService = ""
            name = pbm.ExtendedElementDescription()
            description = pbm.ExtendedElementDescription()

            class LineOfServiceEnum(Enum): # pbm.capability.provider.LineOfServiceInfo.LineOfServiceEnum
               INSPECTION = 0
               COMPRESSION = 1
               ENCRYPTION = 2
               REPLICATION = 3
               CACHING = 4
               PERSISTENCE = 5
               DATA_PROVIDER = 6
               DATASTORE_IO_CONTROL = 7

         class PersistenceBasedDataServiceInfo(pbm.capability.provider.LineOfServiceInfo): # pbm.capability.provider.PersistenceBasedDataServiceInfo
            compatiblePersistenceSchemaNamespace = [ "" ]

         class VaioDataServiceInfo(pbm.capability.provider.LineOfServiceInfo): # pbm.capability.provider.VaioDataServiceInfo
            pass

      class types(object): # (unknown name)

         class BuiltinGenericTypesEnum(Enum): # pbm.capability.types.BuiltinGenericTypesEnum
            VMW_RANGE = 0
            VMW_SET = 1

         class BuiltinTypesEnum(Enum): # pbm.capability.types.BuiltinTypesEnum
            XSD_LONG = 0
            XSD_SHORT = 1
            XSD_INTEGER = 2
            XSD_INT = 3
            XSD_STRING = 4
            XSD_BOOLEAN = 5
            XSD_DOUBLE = 6
            XSD_DATETIME = 7
            VMW_TIMESPAN = 8
            VMW_POLICY = 9

         class DescriptiveValue(vmodl.DynamicData): # pbm.capability.types.DescriptiveValue
            description = pbm.ExtendedElementDescription()
            value = {}

         class DiscreteSet(vmodl.DynamicData): # pbm.capability.types.DiscreteSet
            values = [ {} ]

         class Range(vmodl.DynamicData): # pbm.capability.types.Range
            min = {}
            max = {}

         class TimeSpan(vmodl.DynamicData): # pbm.capability.types.TimeSpan
            value = 0
            unit = ""

         class TimeUnitEnum(Enum): # pbm.capability.types.TimeUnitEnum
            SECONDS = 0
            MINUTES = 1
            HOURS = 2
            DAYS = 3
            WEEKS = 4
            MONTHS = 5
            YEARS = 6

      class CapabilityInstance(vmodl.DynamicData): # pbm.capability.CapabilityInstance
         id = pbm.capability.CapabilityMetadata.UniqueId()
         constraint = [ pbm.capability.ConstraintInstance() ]

      class GenericTypeInfo(pbm.capability.TypeInfo): # pbm.capability.GenericTypeInfo
         genericTypeName = ""

   class compliance(object): # (unknown name)

      class ComplianceManager(vmodl.ManagedObject): # pbm.compliance.ComplianceManager

         def checkCompliance(entities=[ pbm.ServerObjectRef() ], profile=pbm.profile.ProfileId() or None): # pbm.compliance.ComplianceManager.checkCompliance
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.ComplianceResult() ]

         def fetchComplianceResult(entities=[ pbm.ServerObjectRef() ], profile=pbm.profile.ProfileId() or None): # pbm.compliance.ComplianceManager.fetchComplianceResult
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.ComplianceResult() ]

         def checkRollupCompliance(entity=[ pbm.ServerObjectRef() ]): # pbm.compliance.ComplianceManager.checkRollupCompliance
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.RollupComplianceResult() ]

         def fetchRollupComplianceResult(entity=[ pbm.ServerObjectRef() ]): # pbm.compliance.ComplianceManager.fetchRollupComplianceResult
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.RollupComplianceResult() ]

         def queryByRollupComplianceStatus(status=""): # pbm.compliance.ComplianceManager.queryByRollupComplianceStatus
            # throws vmodl.fault.InvalidArgument, pbm.fault.PBMFault
            return [ pbm.ServerObjectRef() ]

      class ComplianceResult(vmodl.DynamicData): # pbm.compliance.ComplianceResult
         checkTime = vmodl.DateTime()
         entity = pbm.ServerObjectRef()
         profile = pbm.profile.ProfileId()
         complianceTaskStatus = ""
         complianceStatus = ""
         mismatch = False
         violatedPolicies = [ pbm.compliance.PolicyStatus() ]
         errorCause = [ vmodl.MethodFault() ]
         operationalStatus = pbm.compliance.OperationalStatus()
         info = pbm.ExtendedElementDescription()

         class ComplianceStatus(Enum): # pbm.compliance.ComplianceResult.ComplianceStatus
            compliant = 0
            nonCompliant = 1
            unknown = 2
            notApplicable = 3
            outOfDate = 4

         class ComplianceTaskStatus(Enum): # pbm.compliance.ComplianceResult.ComplianceTaskStatus
            inProgress = 0
            success = 1
            failed = 2

      class EntityHealthStatus(object): # (unknown name)

         class HealthStatus(Enum): # pbm.compliance.EntityHealthStatus.HealthStatus
            red = 0
            yellow = 1
            green = 2
            unknown = 3

      class OperationalStatus(vmodl.DynamicData): # pbm.compliance.OperationalStatus
         healthy = False
         operationETA = vmodl.DateTime()
         operationProgress = 0
         transitional = False

      class PolicyStatus(vmodl.DynamicData): # pbm.compliance.PolicyStatus
         expectedValue = pbm.capability.CapabilityInstance()
         currentValue = pbm.capability.CapabilityInstance()

      class RollupComplianceResult(vmodl.DynamicData): # pbm.compliance.RollupComplianceResult
         oldestCheckTime = vmodl.DateTime()
         entity = pbm.ServerObjectRef()
         overallComplianceStatus = ""
         overallComplianceTaskStatus = ""
         result = [ pbm.compliance.ComplianceResult() ]
         errorCause = [ vmodl.MethodFault() ]
         profileMismatch = False

   class fault(object): # (unknown name)

      class PBMFault(vmodl.MethodFault): # pbm.fault.PBMFault
         pass

      class ProfileStorageFault(pbm.fault.PBMFault): # pbm.fault.ProfileStorageFault
         pass

      class ResourceInUse(pbm.fault.PBMFault): # pbm.fault.ResourceInUse
         type = vmodl.TypeName()
         name = ""

      class AlreadyExists(pbm.fault.PBMFault): # pbm.fault.AlreadyExists
         name = ""

      class CompatibilityCheckFault(pbm.fault.PBMFault): # pbm.fault.CompatibilityCheckFault
         hub = pbm.placement.PlacementHub()

      class DefaultProfileAppliesFault(pbm.fault.CompatibilityCheckFault): # pbm.fault.DefaultProfileAppliesFault
         pass

      class DuplicateName(pbm.fault.PBMFault): # pbm.fault.DuplicateName
         name = ""

      class InvalidLogin(pbm.fault.PBMFault): # pbm.fault.InvalidLogin
         pass

      class LegacyHubsNotSupported(pbm.fault.PBMFault): # pbm.fault.LegacyHubsNotSupported
         hubs = [ pbm.placement.PlacementHub() ]

      class NonExistentHubs(pbm.fault.PBMFault): # pbm.fault.NonExistentHubs
         hubs = [ pbm.placement.PlacementHub() ]

      class NotFound(pbm.fault.PBMFault): # pbm.fault.NotFound
         pass

      class PropertyMismatchFault(pbm.fault.CompatibilityCheckFault): # pbm.fault.PropertyMismatchFault
         capabilityInstanceId = pbm.capability.CapabilityMetadata.UniqueId()
         requirementPropertyInstance = pbm.capability.PropertyInstance()

      class CapabilityProfilePropertyMismatchFault(pbm.fault.PropertyMismatchFault): # pbm.fault.CapabilityProfilePropertyMismatchFault
         resourcePropertyInstance = pbm.capability.PropertyInstance()

      class IncompatibleVendorSpecificRuleSet(pbm.fault.CapabilityProfilePropertyMismatchFault): # pbm.fault.IncompatibleVendorSpecificRuleSet
         pass

   class placement(object): # (unknown name)

      class CompatibilityResult(vmodl.DynamicData): # pbm.placement.CompatibilityResult
         hub = pbm.placement.PlacementHub()
         matchingResources = [ pbm.placement.MatchingResources() ]
         howMany = 0
         utilization = [ pbm.placement.ResourceUtilization() ]
         warning = [ vmodl.MethodFault() ]
         error = [ vmodl.MethodFault() ]

      class MatchingResources(vmodl.DynamicData): # pbm.placement.MatchingResources
         pass

      class PlacementHub(vmodl.DynamicData): # pbm.placement.PlacementHub
         hubType = ""
         hubId = ""

      class PlacementSolver(vmodl.ManagedObject): # pbm.placement.PlacementSolver

         def queryMatchingHub(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profile=pbm.profile.ProfileId()): # pbm.placement.PlacementSolver.queryMatchingHub
            # throws pbm.fault.PBMFault
            return [ pbm.placement.PlacementHub() ]

         def queryMatchingHubWithSpec(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, createSpec=pbm.profile.CapabilityBasedProfileCreateSpec()): # pbm.placement.PlacementSolver.queryMatchingHubWithSpec
            # throws pbm.fault.PBMFault
            return [ pbm.placement.PlacementHub() ]

         def checkCompatibility(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profile=pbm.profile.ProfileId()): # pbm.placement.PlacementSolver.checkCompatibility
            return [ pbm.placement.CompatibilityResult() ]

         def checkCompatibilityWithSpec(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profileSpec=pbm.profile.CapabilityBasedProfileCreateSpec()): # pbm.placement.PlacementSolver.checkCompatibilityWithSpec
            return [ pbm.placement.CompatibilityResult() ]

         def checkRequirements(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, placementSubjectRef=pbm.ServerObjectRef() or None, placementSubjectRequirement=[ pbm.placement.Requirement() ] or None): # pbm.placement.PlacementSolver.checkRequirements
            # throws pbm.fault.PBMFault
            return [ pbm.placement.CompatibilityResult() ]

      class Requirement(vmodl.DynamicData): # pbm.placement.Requirement
         pass

      class ResourceUtilization(vmodl.DynamicData): # pbm.placement.ResourceUtilization
         name = pbm.ExtendedElementDescription()
         description = pbm.ExtendedElementDescription()
         availableBefore = 0
         availableAfter = 0
         total = 0

      class CapabilityConstraintsRequirement(pbm.placement.Requirement): # pbm.placement.CapabilityConstraintsRequirement
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityProfileRequirement(pbm.placement.Requirement): # pbm.placement.CapabilityProfileRequirement
         profileId = pbm.profile.ProfileId()

      class MatchingReplicationResources(pbm.placement.MatchingResources): # pbm.placement.MatchingReplicationResources
         replicationGroup = [ vim.vm.replication.ReplicationGroupId() ]

   class profile(object): # (unknown name)

      class CapabilityBasedProfileCreateSpec(vmodl.DynamicData): # pbm.profile.CapabilityBasedProfileCreateSpec
         name = ""
         description = ""
         category = ""
         resourceType = pbm.profile.ResourceType()
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityBasedProfileUpdateSpec(vmodl.DynamicData): # pbm.profile.CapabilityBasedProfileUpdateSpec
         name = ""
         description = ""
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityConstraints(vmodl.DynamicData): # pbm.profile.CapabilityConstraints
         pass

      class DataServiceToPoliciesMap(vmodl.DynamicData): # pbm.profile.DataServiceToPoliciesMap
         dataServicePolicy = pbm.profile.ProfileId()
         parentStoragePolicies = [ pbm.profile.ProfileId() ]
         fault = vmodl.MethodFault()

      class DefaultProfileInfo(vmodl.DynamicData): # pbm.profile.DefaultProfileInfo
         datastores = [ pbm.placement.PlacementHub() ]
         defaultProfile = pbm.profile.Profile()

      class EntityAssociations(object): # (unknown name)

         class Operation(Enum): # pbm.profile.EntityAssociations.Operation
            CREATE = 0
            REGISTER = 1
            RECONFIGURE = 2
            MIGRATE = 3
            CLONE = 4

      class IofilterInfo(object): # (unknown name)

         class FilterType(Enum): # pbm.profile.IofilterInfo.FilterType
            INSPECTION = 0
            COMPRESSION = 1
            ENCRYPTION = 2
            REPLICATION = 3
            CACHE = 4
            DATAPROVIDER = 5
            DATASTOREIOCONTROL = 6

      class Profile(vmodl.DynamicData): # pbm.profile.Profile
         profileId = pbm.profile.ProfileId()
         name = ""
         description = ""
         creationTime = vmodl.DateTime()
         createdBy = ""
         lastUpdatedTime = vmodl.DateTime()
         lastUpdatedBy = ""

      class ProfileId(vmodl.DynamicData): # pbm.profile.ProfileId
         uniqueId = ""

      class ProfileManager(vmodl.ManagedObject): # pbm.profile.ProfileManager

         def fetchResourceType(): # pbm.profile.ProfileManager.fetchResourceType
            return [ pbm.profile.ResourceType() ]

         def fetchVendorInfo(resourceType=pbm.profile.ResourceType() or None): # pbm.profile.ProfileManager.fetchVendorInfo
            return [ pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo() ]

         def fetchCapabilityMetadata(resourceType=pbm.profile.ResourceType() or None, vendorUuid="" or None): # pbm.profile.ProfileManager.fetchCapabilityMetadata
            return [ pbm.capability.provider.CapabilityObjectMetadataPerCategory() ]

         def fetchCapabilitySchema(vendorUuid="" or None, lineOfService=[ "" ] or None): # pbm.profile.ProfileManager.fetchCapabilitySchema
            # throws pbm.fault.PBMFault
            return [ pbm.capability.provider.CapabilityObjectSchema() ]

         def create(createSpec=pbm.profile.CapabilityBasedProfileCreateSpec()): # pbm.profile.ProfileManager.create
            # throws vmodl.fault.InvalidArgument, pbm.fault.ProfileStorageFault, pbm.fault.DuplicateName
            return pbm.profile.ProfileId()

         def update(profileId=pbm.profile.ProfileId(), updateSpec=pbm.profile.CapabilityBasedProfileUpdateSpec()): # pbm.profile.ProfileManager.update
            # throws vmodl.fault.InvalidArgument, pbm.fault.ProfileStorageFault
            return None

         def delete(profileId=[ pbm.profile.ProfileId() ]): # pbm.profile.ProfileManager.delete
            return [ pbm.profile.ProfileOperationOutcome() ]

         def queryProfile(resourceType=pbm.profile.ResourceType(), profileCategory="" or None): # pbm.profile.ProfileManager.queryProfile
            # throws vmodl.fault.InvalidArgument
            return [ pbm.profile.ProfileId() ]

         def retrieveContent(profileIds=[ pbm.profile.ProfileId() ]): # pbm.profile.ProfileManager.retrieveContent
            # throws vmodl.fault.InvalidArgument
            return [ pbm.profile.Profile() ]

         def queryAssociatedProfiles(entities=[ pbm.ServerObjectRef() ]): # pbm.profile.ProfileManager.queryAssociatedProfiles
            # throws pbm.fault.PBMFault
            return [ pbm.profile.QueryProfileResult() ]

         def queryAssociatedProfile(entity=pbm.ServerObjectRef()): # pbm.profile.ProfileManager.queryAssociatedProfile
            # throws pbm.fault.PBMFault
            return [ pbm.profile.ProfileId() ]

         def queryAssociatedEntity(profile=pbm.profile.ProfileId(), entityType="" or None): # pbm.profile.ProfileManager.queryAssociatedEntity
            # throws pbm.fault.PBMFault
            return [ pbm.ServerObjectRef() ]

         def queryDefaultRequirementProfile(hub=pbm.placement.PlacementHub()): # pbm.profile.ProfileManager.queryDefaultRequirementProfile
            # throws vmodl.fault.InvalidArgument, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return pbm.profile.ProfileId()

         def resetDefaultRequirementProfile(profile=pbm.profile.ProfileId() or None): # pbm.profile.ProfileManager.resetDefaultRequirementProfile
            return None

         def assignDefaultRequirementProfile(profile=pbm.profile.ProfileId(), datastores=[ pbm.placement.PlacementHub() ]): # pbm.profile.ProfileManager.assignDefaultRequirementProfile
            # throws vmodl.fault.InvalidArgument, pbm.fault.LegacyHubsNotSupported, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return None

         def findApplicableDefaultProfile(datastores=[ pbm.placement.PlacementHub() ]): # pbm.profile.ProfileManager.findApplicableDefaultProfile
            # throws pbm.fault.LegacyHubsNotSupported, pbm.fault.NonExistentHubs, pbm.fault.PBMFault, vmodl.fault.InvalidArgument
            return [ pbm.profile.Profile() ]

         def queryDefaultRequirementProfiles(datastores=[ pbm.placement.PlacementHub() ]): # pbm.profile.ProfileManager.queryDefaultRequirementProfiles
            # throws vmodl.fault.InvalidArgument, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return [ pbm.profile.DefaultProfileInfo() ]

         def resetVSanDefaultProfile(): # pbm.profile.ProfileManager.resetVSanDefaultProfile
            return None

         def querySpaceStatsForStorageContainer(datastore=pbm.ServerObjectRef(), capabilityProfileId=[ pbm.profile.ProfileId() ] or None): # pbm.profile.ProfileManager.querySpaceStatsForStorageContainer
            # throws vmodl.fault.InvalidArgument, pbm.fault.PBMFault
            return [ pbm.profile.provider.DatastoreSpaceStatistics() ]

         def queryAssociatedEntities(profiles=[ pbm.profile.ProfileId() ] or None): # pbm.profile.ProfileManager.queryAssociatedEntities
            # throws pbm.fault.PBMFault
            return [ pbm.profile.QueryProfileResult() ]

      class ProfileOperationOutcome(vmodl.DynamicData): # pbm.profile.ProfileOperationOutcome
         profileId = pbm.profile.ProfileId()
         fault = vmodl.MethodFault()

      class ProfileType(vmodl.DynamicData): # pbm.profile.ProfileType
         uniqueId = ""

      class QueryProfileResult(vmodl.DynamicData): # pbm.profile.QueryProfileResult
         object = pbm.ServerObjectRef()
         profileId = [ pbm.profile.ProfileId() ]
         fault = vmodl.MethodFault()

      class ResourceType(vmodl.DynamicData): # pbm.profile.ResourceType
         resourceType = ""

      class ResourceTypeEnum(Enum): # pbm.profile.ResourceTypeEnum
         STORAGE = 0

      class SubProfileCapabilityConstraints(pbm.profile.CapabilityConstraints): # pbm.profile.SubProfileCapabilityConstraints
         subProfiles = [ pbm.profile.SubProfileCapabilityConstraints.SubProfile() ]

         class SubProfile(vmodl.DynamicData): # pbm.profile.SubProfileCapabilityConstraints.SubProfile
            name = ""
            capability = [ pbm.capability.CapabilityInstance() ]
            forceProvision = False

      class VmAssociations(object): # (unknown name)

         class Operation(Enum): # pbm.profile.VmAssociations.Operation
            CREATE = 0
            RECONFIGURE = 1
            MIGRATE = 2
            CLONE = 3

      class provider(object): # (unknown name)

         class DatastoreSpaceStatistics(vmodl.DynamicData): # pbm.profile.provider.DatastoreSpaceStatistics
            profileId = ""
            physicalTotalInMB = 0
            physicalFreeInMB = 0
            physicalUsedInMB = 0
            logicalLimitInMB = 0
            logicalFreeInMB = 0
            logicalUsedInMB = 0

      class CapabilityBasedProfile(pbm.profile.Profile): # pbm.profile.CapabilityBasedProfile
         profileCategory = ""
         resourceType = pbm.profile.ResourceType()
         constraints = pbm.profile.CapabilityConstraints()
         generationId = 0
         isDefault = False
         systemCreatedProfileType = ""
         lineOfService = ""

         class ProfileCategoryEnum(Enum): # pbm.profile.CapabilityBasedProfile.ProfileCategoryEnum
            REQUIREMENT = 0
            RESOURCE = 1
            DATA_SERVICE_POLICY = 2

         class SystemCreatedProfileType(Enum): # pbm.profile.CapabilityBasedProfile.SystemCreatedProfileType
            VsanDefaultProfile = 0
            VVolDefaultProfile = 1
            PmemDefaultProfile = 2
            VmcManagementProfile = 3

      class DefaultCapabilityBasedProfile(pbm.profile.CapabilityBasedProfile): # pbm.profile.DefaultCapabilityBasedProfile
         vvolType = [ "" ]
         containerId = ""

   class provider(object): # (unknown name)

      class Provider(vmodl.ManagedObject): # pbm.provider.Provider
         pass

   class replication(object): # (unknown name)

      class QueryReplicationGroupResult(vmodl.DynamicData): # pbm.replication.QueryReplicationGroupResult
         object = pbm.ServerObjectRef()
         replicationGroupId = vim.vm.replication.ReplicationGroupId()
         fault = vmodl.MethodFault()

      class ReplicationManager(vmodl.ManagedObject): # pbm.replication.ReplicationManager

         def queryReplicationGroups(entities=[ pbm.ServerObjectRef() ] or None): # pbm.replication.ReplicationManager.queryReplicationGroups
            # throws pbm.fault.PBMFault
            return [ pbm.replication.QueryReplicationGroupResult() ]
