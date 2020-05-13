from enum import Enum

class pbm(object):

   class AboutInfo(vmodl.DynamicData):
      name = ""
      version = ""
      instanceUuid = ""

   class ExtendedElementDescription(vmodl.DynamicData):
      label = ""
      summary = ""
      key = ""
      messageCatalogKeyPrefix = ""
      messageArg = [ vmodl.KeyAnyValue() ]

   class ServerObjectRef(vmodl.DynamicData):
      objectType = ""
      key = ""
      serverUuid = ""

      class VvolType(Enum):
         Config = 0
         Data = 1
         Swap = 2

      class ObjectType(Enum):
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

   class ServiceInstance(vmodl.ManagedObject):
      content = pbm.ServiceInstanceContent()

      def retrieveContent():
         return pbm.ServiceInstanceContent()

   class ServiceInstanceContent(vmodl.DynamicData):
      aboutInfo = pbm.AboutInfo()
      sessionManager = pbm.auth.SessionManager()
      capabilityMetadataManager = pbm.capability.CapabilityMetadataManager()
      profileManager = pbm.profile.ProfileManager()
      complianceManager = pbm.compliance.ComplianceManager()
      placementSolver = pbm.placement.PlacementSolver()
      replicationManager = pbm.replication.ReplicationManager()

   class auth(object):

      class SessionManager(vmodl.ManagedObject):
         pass

   class capability(object):

      class CapabilityMetadata(vmodl.DynamicData):
         id = pbm.capability.CapabilityMetadata.UniqueId()
         summary = pbm.ExtendedElementDescription()
         mandatory = False
         hint = False
         keyId = ""
         allowMultipleConstraints = False
         propertyMetadata = [ pbm.capability.PropertyMetadata() ]

         class UniqueId(vmodl.DynamicData):
            namespace = ""
            id = ""

      class CapabilityMetadataManager(vmodl.ManagedObject):
         pass

      class ConstraintInstance(vmodl.DynamicData):
         propertyInstance = [ pbm.capability.PropertyInstance() ]

      class Operator(Enum):
         NOT = 0

      class PropertyInstance(vmodl.DynamicData):
         id = ""
         operator = ""
         value = anyType()

      class PropertyMetadata(vmodl.DynamicData):
         id = ""
         summary = pbm.ExtendedElementDescription()
         mandatory = False
         type = pbm.capability.TypeInfo()
         defaultValue = anyType()
         allowedValue = anyType()
         requirementsTypeHint = ""

      class TypeInfo(vmodl.DynamicData):
         typeName = ""

      class provider(object):

         class CapabilityObjectMetadataPerCategory(vmodl.DynamicData):
            subCategory = ""
            capabilityMetadata = [ pbm.capability.CapabilityMetadata() ]

         class CapabilityObjectSchema(vmodl.DynamicData):
            vendorInfo = pbm.capability.provider.CapabilityObjectSchema.VendorInfo()
            namespaceInfo = pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo()
            lineOfService = pbm.capability.provider.LineOfServiceInfo()
            capabilityMetadataPerCategory = [ pbm.capability.provider.CapabilityObjectMetadataPerCategory() ]

            class VendorInfo(vmodl.DynamicData):
               vendorUuid = ""
               info = pbm.ExtendedElementDescription()

            class NamespaceInfo(vmodl.DynamicData):
               version = ""
               namespace = ""
               info = pbm.ExtendedElementDescription()

            class VendorResourceTypeInfo(vmodl.DynamicData):
               resourceType = ""
               vendorNamespaceInfo = [ pbm.capability.provider.CapabilityObjectSchema.VendorNamespaceInfo() ]

            class VendorNamespaceInfo(vmodl.DynamicData):
               vendorInfo = pbm.capability.provider.CapabilityObjectSchema.VendorInfo()
               namespaceInfo = pbm.capability.provider.CapabilityObjectSchema.NamespaceInfo()

         class LineOfServiceInfo(vmodl.DynamicData):
            lineOfService = ""
            name = pbm.ExtendedElementDescription()
            description = pbm.ExtendedElementDescription()

            class LineOfServiceEnum(Enum):
               INSPECTION = 0
               COMPRESSION = 1
               ENCRYPTION = 2
               REPLICATION = 3
               CACHING = 4
               PERSISTENCE = 5
               DATA_PROVIDER = 6
               DATASTORE_IO_CONTROL = 7

         class PersistenceBasedDataServiceInfo(pbm.capability.provider.LineOfServiceInfo):
            compatiblePersistenceSchemaNamespace = [ "" ]

         class VaioDataServiceInfo(pbm.capability.provider.LineOfServiceInfo):
            pass

      class types(object):

         class BuiltinGenericTypesEnum(Enum):
            VMW_RANGE = 0
            VMW_SET = 1

         class BuiltinTypesEnum(Enum):
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

         class DescriptiveValue(vmodl.DynamicData):
            description = pbm.ExtendedElementDescription()
            value = anyType()

         class DiscreteSet(vmodl.DynamicData):
            values = [ anyType() ]

         class Range(vmodl.DynamicData):
            min = anyType()
            max = anyType()

         class TimeSpan(vmodl.DynamicData):
            value = 0
            unit = ""

         class TimeUnitEnum(Enum):
            SECONDS = 0
            MINUTES = 1
            HOURS = 2
            DAYS = 3
            WEEKS = 4
            MONTHS = 5
            YEARS = 6

      class CapabilityInstance(vmodl.DynamicData):
         id = pbm.capability.CapabilityMetadata.UniqueId()
         constraint = [ pbm.capability.ConstraintInstance() ]

      class GenericTypeInfo(pbm.capability.TypeInfo):
         genericTypeName = ""

   class compliance(object):

      class ComplianceManager(vmodl.ManagedObject):

         def checkCompliance(entities=[ pbm.ServerObjectRef() ], profile=pbm.profile.ProfileId() or None):
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.ComplianceResult() ]

         def fetchComplianceResult(entities=[ pbm.ServerObjectRef() ], profile=pbm.profile.ProfileId() or None):
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.ComplianceResult() ]

         def checkRollupCompliance(entity=[ pbm.ServerObjectRef() ]):
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.RollupComplianceResult() ]

         def fetchRollupComplianceResult(entity=[ pbm.ServerObjectRef() ]):
            # throws pbm.fault.PBMFault
            return [ pbm.compliance.RollupComplianceResult() ]

         def queryByRollupComplianceStatus(status=""):
            # throws vmodl.fault.InvalidArgument, pbm.fault.PBMFault
            return [ pbm.ServerObjectRef() ]

      class ComplianceResult(vmodl.DynamicData):
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

         class ComplianceStatus(Enum):
            compliant = 0
            nonCompliant = 1
            unknown = 2
            notApplicable = 3
            outOfDate = 4

         class ComplianceTaskStatus(Enum):
            inProgress = 0
            success = 1
            failed = 2

      class EntityHealthStatus(object):

         class HealthStatus(Enum):
            red = 0
            yellow = 1
            green = 2
            unknown = 3

      class OperationalStatus(vmodl.DynamicData):
         healthy = False
         operationETA = vmodl.DateTime()
         operationProgress = 0
         transitional = False

      class PolicyStatus(vmodl.DynamicData):
         expectedValue = pbm.capability.CapabilityInstance()
         currentValue = pbm.capability.CapabilityInstance()

      class RollupComplianceResult(vmodl.DynamicData):
         oldestCheckTime = vmodl.DateTime()
         entity = pbm.ServerObjectRef()
         overallComplianceStatus = ""
         overallComplianceTaskStatus = ""
         result = [ pbm.compliance.ComplianceResult() ]
         errorCause = [ vmodl.MethodFault() ]
         profileMismatch = False

   class fault(object):

      class PBMFault(vmodl.MethodFault):
         pass

      class ProfileStorageFault(pbm.fault.PBMFault):
         pass

      class ResourceInUse(pbm.fault.PBMFault):
         type = vmodl.TypeName()
         name = ""

      class AlreadyExists(pbm.fault.PBMFault):
         name = ""

      class CompatibilityCheckFault(pbm.fault.PBMFault):
         hub = pbm.placement.PlacementHub()

      class DefaultProfileAppliesFault(pbm.fault.CompatibilityCheckFault):
         pass

      class DuplicateName(pbm.fault.PBMFault):
         name = ""

      class InvalidLogin(pbm.fault.PBMFault):
         pass

      class LegacyHubsNotSupported(pbm.fault.PBMFault):
         hubs = [ pbm.placement.PlacementHub() ]

      class NonExistentHubs(pbm.fault.PBMFault):
         hubs = [ pbm.placement.PlacementHub() ]

      class NotFound(pbm.fault.PBMFault):
         pass

      class PropertyMismatchFault(pbm.fault.CompatibilityCheckFault):
         capabilityInstanceId = pbm.capability.CapabilityMetadata.UniqueId()
         requirementPropertyInstance = pbm.capability.PropertyInstance()

      class CapabilityProfilePropertyMismatchFault(pbm.fault.PropertyMismatchFault):
         resourcePropertyInstance = pbm.capability.PropertyInstance()

      class IncompatibleVendorSpecificRuleSet(pbm.fault.CapabilityProfilePropertyMismatchFault):
         pass

   class placement(object):

      class CompatibilityResult(vmodl.DynamicData):
         hub = pbm.placement.PlacementHub()
         matchingResources = [ pbm.placement.MatchingResources() ]
         howMany = 0
         utilization = [ pbm.placement.ResourceUtilization() ]
         warning = [ vmodl.MethodFault() ]
         error = [ vmodl.MethodFault() ]

      class MatchingResources(vmodl.DynamicData):
         pass

      class PlacementHub(vmodl.DynamicData):
         hubType = ""
         hubId = ""

      class PlacementSolver(vmodl.ManagedObject):

         def queryMatchingHub(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profile=pbm.profile.ProfileId()):
            # throws pbm.fault.PBMFault
            return [ pbm.placement.PlacementHub() ]

         def queryMatchingHubWithSpec(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, createSpec=pbm.profile.CapabilityBasedProfileCreateSpec()):
            # throws pbm.fault.PBMFault
            return [ pbm.placement.PlacementHub() ]

         def checkCompatibility(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profile=pbm.profile.ProfileId()):
            return [ pbm.placement.CompatibilityResult() ]

         def checkCompatibilityWithSpec(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, profileSpec=pbm.profile.CapabilityBasedProfileCreateSpec()):
            return [ pbm.placement.CompatibilityResult() ]

         def checkRequirements(hubsToSearch=[ pbm.placement.PlacementHub() ] or None, placementSubjectRef=pbm.ServerObjectRef() or None, placementSubjectRequirement=[ pbm.placement.Requirement() ] or None):
            # throws pbm.fault.PBMFault
            return [ pbm.placement.CompatibilityResult() ]

      class Requirement(vmodl.DynamicData):
         pass

      class ResourceUtilization(vmodl.DynamicData):
         name = pbm.ExtendedElementDescription()
         description = pbm.ExtendedElementDescription()
         availableBefore = 0
         availableAfter = 0
         total = 0

      class CapabilityConstraintsRequirement(pbm.placement.Requirement):
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityProfileRequirement(pbm.placement.Requirement):
         profileId = pbm.profile.ProfileId()

      class MatchingReplicationResources(pbm.placement.MatchingResources):
         replicationGroup = [ vim.vm.replication.ReplicationGroupId() ]

   class profile(object):

      class CapabilityBasedProfileCreateSpec(vmodl.DynamicData):
         name = ""
         description = ""
         category = ""
         resourceType = pbm.profile.ResourceType()
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityBasedProfileUpdateSpec(vmodl.DynamicData):
         name = ""
         description = ""
         constraints = pbm.profile.CapabilityConstraints()

      class CapabilityConstraints(vmodl.DynamicData):
         pass

      class DataServiceToPoliciesMap(vmodl.DynamicData):
         dataServicePolicy = pbm.profile.ProfileId()
         parentStoragePolicies = [ pbm.profile.ProfileId() ]
         fault = vmodl.MethodFault()

      class DefaultProfileInfo(vmodl.DynamicData):
         datastores = [ pbm.placement.PlacementHub() ]
         defaultProfile = pbm.profile.Profile()

      class EntityAssociations(object):

         class Operation(Enum):
            CREATE = 0
            REGISTER = 1
            RECONFIGURE = 2
            MIGRATE = 3
            CLONE = 4

      class IofilterInfo(object):

         class FilterType(Enum):
            INSPECTION = 0
            COMPRESSION = 1
            ENCRYPTION = 2
            REPLICATION = 3
            CACHE = 4
            DATAPROVIDER = 5
            DATASTOREIOCONTROL = 6

      class Profile(vmodl.DynamicData):
         profileId = pbm.profile.ProfileId()
         name = ""
         description = ""
         creationTime = vmodl.DateTime()
         createdBy = ""
         lastUpdatedTime = vmodl.DateTime()
         lastUpdatedBy = ""

      class ProfileId(vmodl.DynamicData):
         uniqueId = ""

      class ProfileManager(vmodl.ManagedObject):

         def fetchResourceType():
            return [ pbm.profile.ResourceType() ]

         def fetchVendorInfo(resourceType=pbm.profile.ResourceType() or None):
            return [ pbm.capability.provider.CapabilityObjectSchema.VendorResourceTypeInfo() ]

         def fetchCapabilityMetadata(resourceType=pbm.profile.ResourceType() or None, vendorUuid="" or None):
            return [ pbm.capability.provider.CapabilityObjectMetadataPerCategory() ]

         def fetchCapabilitySchema(vendorUuid="" or None, lineOfService=[ "" ] or None):
            # throws pbm.fault.PBMFault
            return [ pbm.capability.provider.CapabilityObjectSchema() ]

         def create(createSpec=pbm.profile.CapabilityBasedProfileCreateSpec()):
            # throws vmodl.fault.InvalidArgument, pbm.fault.ProfileStorageFault, pbm.fault.DuplicateName
            return pbm.profile.ProfileId()

         def update(profileId=pbm.profile.ProfileId(), updateSpec=pbm.profile.CapabilityBasedProfileUpdateSpec()):
            # throws vmodl.fault.InvalidArgument, pbm.fault.ProfileStorageFault
            return None

         def delete(profileId=[ pbm.profile.ProfileId() ]):
            return [ pbm.profile.ProfileOperationOutcome() ]

         def queryProfile(resourceType=pbm.profile.ResourceType(), profileCategory="" or None):
            # throws vmodl.fault.InvalidArgument
            return [ pbm.profile.ProfileId() ]

         def retrieveContent(profileIds=[ pbm.profile.ProfileId() ]):
            # throws vmodl.fault.InvalidArgument
            return [ pbm.profile.Profile() ]

         def queryAssociatedProfiles(entities=[ pbm.ServerObjectRef() ]):
            # throws pbm.fault.PBMFault
            return [ pbm.profile.QueryProfileResult() ]

         def queryAssociatedProfile(entity=pbm.ServerObjectRef()):
            # throws pbm.fault.PBMFault
            return [ pbm.profile.ProfileId() ]

         def queryAssociatedEntity(profile=pbm.profile.ProfileId(), entityType="" or None):
            # throws pbm.fault.PBMFault
            return [ pbm.ServerObjectRef() ]

         def queryDefaultRequirementProfile(hub=pbm.placement.PlacementHub()):
            # throws vmodl.fault.InvalidArgument, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return pbm.profile.ProfileId()

         def resetDefaultRequirementProfile(profile=pbm.profile.ProfileId() or None):
            return None

         def assignDefaultRequirementProfile(profile=pbm.profile.ProfileId(), datastores=[ pbm.placement.PlacementHub() ]):
            # throws vmodl.fault.InvalidArgument, pbm.fault.LegacyHubsNotSupported, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return None

         def findApplicableDefaultProfile(datastores=[ pbm.placement.PlacementHub() ]):
            # throws pbm.fault.LegacyHubsNotSupported, pbm.fault.NonExistentHubs, pbm.fault.PBMFault, vmodl.fault.InvalidArgument
            return [ pbm.profile.Profile() ]

         def queryDefaultRequirementProfiles(datastores=[ pbm.placement.PlacementHub() ]):
            # throws vmodl.fault.InvalidArgument, pbm.fault.NonExistentHubs, pbm.fault.PBMFault
            return [ pbm.profile.DefaultProfileInfo() ]

         def resetVSanDefaultProfile():
            return None

         def querySpaceStatsForStorageContainer(datastore=pbm.ServerObjectRef(), capabilityProfileId=[ pbm.profile.ProfileId() ] or None):
            # throws vmodl.fault.InvalidArgument, pbm.fault.PBMFault
            return [ pbm.profile.provider.DatastoreSpaceStatistics() ]

         def queryAssociatedEntities(profiles=[ pbm.profile.ProfileId() ] or None):
            # throws pbm.fault.PBMFault
            return [ pbm.profile.QueryProfileResult() ]

      class ProfileOperationOutcome(vmodl.DynamicData):
         profileId = pbm.profile.ProfileId()
         fault = vmodl.MethodFault()

      class ProfileType(vmodl.DynamicData):
         uniqueId = ""

      class QueryProfileResult(vmodl.DynamicData):
         object = pbm.ServerObjectRef()
         profileId = [ pbm.profile.ProfileId() ]
         fault = vmodl.MethodFault()

      class ResourceType(vmodl.DynamicData):
         resourceType = ""

      class ResourceTypeEnum(Enum):
         STORAGE = 0

      class SubProfileCapabilityConstraints(pbm.profile.CapabilityConstraints):
         subProfiles = [ pbm.profile.SubProfileCapabilityConstraints.SubProfile() ]

         class SubProfile(vmodl.DynamicData):
            name = ""
            capability = [ pbm.capability.CapabilityInstance() ]
            forceProvision = False

      class VmAssociations(object):

         class Operation(Enum):
            CREATE = 0
            RECONFIGURE = 1
            MIGRATE = 2
            CLONE = 3

      class provider(object):

         class DatastoreSpaceStatistics(vmodl.DynamicData):
            profileId = ""
            physicalTotalInMB = 0
            physicalFreeInMB = 0
            physicalUsedInMB = 0
            logicalLimitInMB = 0
            logicalFreeInMB = 0
            logicalUsedInMB = 0

      class CapabilityBasedProfile(pbm.profile.Profile):
         profileCategory = ""
         resourceType = pbm.profile.ResourceType()
         constraints = pbm.profile.CapabilityConstraints()
         generationId = 0
         isDefault = False
         systemCreatedProfileType = ""
         lineOfService = ""

         class ProfileCategoryEnum(Enum):
            REQUIREMENT = 0
            RESOURCE = 1
            DATA_SERVICE_POLICY = 2

         class SystemCreatedProfileType(Enum):
            VsanDefaultProfile = 0
            VVolDefaultProfile = 1
            PmemDefaultProfile = 2
            VmcManagementProfile = 3

      class DefaultCapabilityBasedProfile(pbm.profile.CapabilityBasedProfile):
         vvolType = [ "" ]
         containerId = ""

   class provider(object):

      class Provider(vmodl.ManagedObject):
         pass

   class replication(object):

      class QueryReplicationGroupResult(vmodl.DynamicData):
         object = pbm.ServerObjectRef()
         replicationGroupId = vim.vm.replication.ReplicationGroupId()
         fault = vmodl.MethodFault()

      class ReplicationManager(vmodl.ManagedObject):

         def queryReplicationGroups(entities=[ pbm.ServerObjectRef() ] or None):
            # throws pbm.fault.PBMFault
            return [ pbm.replication.QueryReplicationGroupResult() ]
