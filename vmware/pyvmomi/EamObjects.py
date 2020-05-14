from enum import Enum

class eam(object): # (unknown name)

   class EamObject(vmodl.ManagedObject): # eam.EamObject

      def resolve(issueKey=[ 0 ]): # eam.EamObject.resolve
         return [ 0 ]

      def resolveAll(): # eam.EamObject.resolveAll
         return None

      def queryIssue(issueKey=[ 0 ] or None): # eam.EamObject.queryIssue
         return [ eam.issue.Issue() ]

      class RuntimeInfo(vmodl.DynamicData): # eam.EamObject.RuntimeInfo
         status = ""
         issue = [ eam.issue.Issue() ]
         goalState = ""
         entity = eam.EamObject()

         class Status(Enum): # eam.EamObject.RuntimeInfo.Status
            green = 0
            yellow = 1
            red = 2

         class GoalState(Enum): # eam.EamObject.RuntimeInfo.GoalState
            enabled = 0
            disabled = 1
            uninstalled = 2

   class Task(vmodl.ManagedObject): # eam.Task
      pass

   class fault(object): # (unknown name)

      class EamFault(vmodl.MethodFault): # eam.fault.EamFault
         pass

      class EamRuntimeFault(vmodl.RuntimeFault): # eam.fault.EamRuntimeFault
         pass

      class EamServiceNotInitialized(eam.fault.EamRuntimeFault): # eam.fault.EamServiceNotInitialized
         pass

      class EamSystemFault(eam.fault.EamRuntimeFault): # eam.fault.EamSystemFault
         pass

      class InvalidAgencyScope(eam.fault.EamFault): # eam.fault.InvalidAgencyScope
         unknownComputeResource = [ vim.ComputeResource() ]

      class InvalidLogin(eam.fault.EamRuntimeFault): # eam.fault.InvalidLogin
         pass

      class InvalidUrl(eam.fault.EamFault): # eam.fault.InvalidUrl
         url = ""
         malformedUrl = False
         unknownHost = False
         connectionRefused = False
         responseCode = 0

      class InvalidVibPackage(eam.fault.EamRuntimeFault): # eam.fault.InvalidVibPackage
         pass

      class NoConnectionToVCenter(eam.fault.EamRuntimeFault): # eam.fault.NoConnectionToVCenter
         pass

      class NotAuthorized(eam.fault.EamRuntimeFault): # eam.fault.NotAuthorized
         pass

      class EamAppFault(eam.fault.EamRuntimeFault): # eam.fault.EamAppFault
         pass

      class EamIOFault(eam.fault.EamRuntimeFault): # eam.fault.EamIOFault
         pass

      class InvalidAgentConfiguration(eam.fault.EamFault): # eam.fault.InvalidAgentConfiguration
         invalidAgentConfiguration = eam.Agent.ConfigInfo()
         invalidField = ""

      class InvalidState(eam.fault.EamAppFault): # eam.fault.InvalidState
         pass

   class issue(object): # (unknown name)

      class Issue(vmodl.DynamicData): # eam.issue.Issue
         key = 0
         description = ""
         time = vmodl.DateTime()

      class AgencyIssue(eam.issue.Issue): # eam.issue.AgencyIssue
         agency = eam.Agency()
         agencyName = ""
         solutionId = ""
         solutionName = ""

      class AgentIssue(eam.issue.AgencyIssue): # eam.issue.AgentIssue
         agent = eam.Agent()
         agentName = ""
         host = vim.HostSystem()
         hostName = ""

      class ExtensibleIssue(eam.issue.Issue): # eam.issue.ExtensibleIssue
         typeId = ""
         argument = [ vmodl.KeyAnyValue() ]
         target = vim.ManagedEntity()
         agent = eam.Agent()
         agency = eam.Agency()

      class HostIssue(eam.issue.Issue): # eam.issue.HostIssue
         host = vim.HostSystem()

      class HostNotReachable(eam.issue.AgentIssue): # eam.issue.HostNotReachable
         pass

      class MissingDvFilterSwitch(eam.issue.AgentIssue): # eam.issue.MissingDvFilterSwitch
         pass

      class OrphanedAgency(eam.issue.AgencyIssue): # eam.issue.OrphanedAgency
         pass

      class OrphanedDvFilterSwitch(eam.issue.HostIssue): # eam.issue.OrphanedDvFilterSwitch
         pass

      class OvfInvalidProperty(eam.issue.AgentIssue): # eam.issue.OvfInvalidProperty
         error = [ vmodl.MethodFault() ]

      class UnknownAgentVm(eam.issue.HostIssue): # eam.issue.UnknownAgentVm
         vm = vim.VirtualMachine()

      class VibIssue(eam.issue.AgentIssue): # eam.issue.VibIssue
         pass

      class VibNotInstalled(eam.issue.VibIssue): # eam.issue.VibNotInstalled
         pass

      class VibRequirementsNotMetByHost(eam.issue.VibNotInstalled): # eam.issue.VibRequirementsNotMetByHost
         pass

      class VibRequiresHostInMaintenanceMode(eam.issue.VibIssue): # eam.issue.VibRequiresHostInMaintenanceMode
         pass

      class VibRequiresHostReboot(eam.issue.VibIssue): # eam.issue.VibRequiresHostReboot
         pass

      class VibRequiresManualInstallation(eam.issue.VibIssue): # eam.issue.VibRequiresManualInstallation
         bulletin = [ "" ]

      class VibRequiresManualUninstallation(eam.issue.VibIssue): # eam.issue.VibRequiresManualUninstallation
         bulletin = [ "" ]

      class VmIssue(eam.issue.AgentIssue): # eam.issue.VmIssue
         vm = vim.VirtualMachine()

      class VmMarkedAsTemplate(eam.issue.VmIssue): # eam.issue.VmMarkedAsTemplate
         pass

      class VmNotDeployed(eam.issue.AgentIssue): # eam.issue.VmNotDeployed
         pass

      class VmOrphaned(eam.issue.VmIssue): # eam.issue.VmOrphaned
         pass

      class VmPoweredOff(eam.issue.VmIssue): # eam.issue.VmPoweredOff
         pass

      class VmPoweredOn(eam.issue.VmIssue): # eam.issue.VmPoweredOn
         pass

      class VmSuspended(eam.issue.VmIssue): # eam.issue.VmSuspended
         pass

      class VmWrongFolder(eam.issue.VmIssue): # eam.issue.VmWrongFolder
         currentFolder = vim.Folder()
         requiredFolder = vim.Folder()

      class VmWrongResourcePool(eam.issue.VmIssue): # eam.issue.VmWrongResourcePool
         currentResourcePool = vim.ResourcePool()
         requiredResourcePool = vim.ResourcePool()

      class cluster(object): # (unknown name)

         class agent(object): # (unknown name)

            class AgentIssue(eam.issue.AgencyIssue): # eam.issue.cluster.agent.AgentIssue
               agent = eam.Agent()
               cluster = vim.ComputeResource()

            class OvfInvalidProperty(eam.issue.cluster.agent.AgentIssue): # eam.issue.cluster.agent.OvfInvalidProperty
               error = [ vmodl.MethodFault() ]

            class VmIssue(eam.issue.cluster.agent.AgentIssue): # eam.issue.cluster.agent.VmIssue
               vm = vim.VirtualMachine()

            class VmNotDeployed(eam.issue.cluster.agent.AgentIssue): # eam.issue.cluster.agent.VmNotDeployed
               pass

            class VmNotRemoved(eam.issue.cluster.agent.VmIssue): # eam.issue.cluster.agent.VmNotRemoved
               pass

            class VmPoweredOff(eam.issue.cluster.agent.VmIssue): # eam.issue.cluster.agent.VmPoweredOff
               pass

            class VmPoweredOn(eam.issue.cluster.agent.VmIssue): # eam.issue.cluster.agent.VmPoweredOn
               pass

            class VmSuspended(eam.issue.cluster.agent.VmIssue): # eam.issue.cluster.agent.VmSuspended
               pass

            class InsufficientClusterResources(eam.issue.cluster.agent.VmPoweredOff): # eam.issue.cluster.agent.InsufficientClusterResources
               pass

            class InsufficientClusterSpace(eam.issue.cluster.agent.VmNotDeployed): # eam.issue.cluster.agent.InsufficientClusterSpace
               pass

            class InvalidConfig(eam.issue.cluster.agent.VmIssue): # eam.issue.cluster.agent.InvalidConfig
               error = {}

            class MissingClusterVmDatastore(eam.issue.cluster.agent.VmNotDeployed): # eam.issue.cluster.agent.MissingClusterVmDatastore
               missingDatastores = [ vim.Datastore() ]

            class MissingClusterVmNetwork(eam.issue.cluster.agent.VmNotDeployed): # eam.issue.cluster.agent.MissingClusterVmNetwork
               missingNetworks = [ vim.Network() ]
               networkNames = [ "" ]

      class integrity(object): # (unknown name)

         class agency(object): # (unknown name)

            class VUMIssue(eam.issue.AgencyIssue): # eam.issue.integrity.agency.VUMIssue
               pass

            class VUMUnavailable(eam.issue.integrity.agency.VUMIssue): # eam.issue.integrity.agency.VUMUnavailable
               pass

            class CannotDeleteSoftware(eam.issue.integrity.agency.VUMIssue): # eam.issue.integrity.agency.CannotDeleteSoftware
               pass

            class CannotStageSoftware(eam.issue.integrity.agency.VUMIssue): # eam.issue.integrity.agency.CannotStageSoftware
               pass

      class personality(object): # (unknown name)

         class agency(object): # (unknown name)

            class PMIssue(eam.issue.AgencyIssue): # eam.issue.personality.agency.PMIssue
               pass

            class PMUnavailable(eam.issue.personality.agency.PMIssue): # eam.issue.personality.agency.PMUnavailable
               pass

            class CannotConfigureSolutions(eam.issue.personality.agency.PMIssue): # eam.issue.personality.agency.CannotConfigureSolutions
               cr = vim.ComputeResource()
               solutionsToModify = [ "" ]
               solutionsToRemove = [ "" ]

            class DepotIssue(eam.issue.personality.agency.PMIssue): # eam.issue.personality.agency.DepotIssue
               remoteDepotUrl = ""

            class InaccessibleDepot(eam.issue.personality.agency.DepotIssue): # eam.issue.personality.agency.InaccessibleDepot
               pass

            class InvalidDepot(eam.issue.personality.agency.DepotIssue): # eam.issue.personality.agency.InvalidDepot
               pass

            class CannotUploadDepot(eam.issue.personality.agency.DepotIssue): # eam.issue.personality.agency.CannotUploadDepot
               localDepotUrl = ""

         class agent(object): # (unknown name)

            class PMIssue(eam.issue.AgentIssue): # eam.issue.personality.agent.PMIssue
               pass

            class AwaitingPMRemediation(eam.issue.personality.agent.PMIssue): # eam.issue.personality.agent.AwaitingPMRemediation
               pass

            class BlockedByAgencyOperation(eam.issue.personality.agent.PMIssue): # eam.issue.personality.agent.BlockedByAgencyOperation
               pass

      class CannotAccessAgentOVF(eam.issue.VmNotDeployed): # eam.issue.CannotAccessAgentOVF
         downloadUrl = ""

      class CannotAccessAgentVib(eam.issue.VibNotInstalled): # eam.issue.CannotAccessAgentVib
         downloadUrl = ""

      class ImmediateHostRebootRequired(eam.issue.VibIssue): # eam.issue.ImmediateHostRebootRequired
         pass

      class IncompatibleHostVersion(eam.issue.VmNotDeployed): # eam.issue.IncompatibleHostVersion
         pass

      class InsufficientIpAddresses(eam.issue.VmPoweredOff): # eam.issue.InsufficientIpAddresses
         network = vim.Network()

      class InsufficientResources(eam.issue.VmNotDeployed): # eam.issue.InsufficientResources
         pass

      class InsufficientSpace(eam.issue.VmNotDeployed): # eam.issue.InsufficientSpace
         pass

      class InvalidConfig(eam.issue.VmIssue): # eam.issue.InvalidConfig
         error = {}

      class MissingAgentIpPool(eam.issue.VmPoweredOff): # eam.issue.MissingAgentIpPool
         network = vim.Network()

      class NoAgentVmDatastore(eam.issue.VmNotDeployed): # eam.issue.NoAgentVmDatastore
         pass

      class NoAgentVmNetwork(eam.issue.VmNotDeployed): # eam.issue.NoAgentVmNetwork
         pass

      class NoCustomAgentVmDatastore(eam.issue.NoAgentVmDatastore): # eam.issue.NoCustomAgentVmDatastore
         customAgentVmDatastore = [ vim.Datastore() ]
         customAgentVmDatastoreName = [ "" ]

      class NoCustomAgentVmNetwork(eam.issue.NoAgentVmNetwork): # eam.issue.NoCustomAgentVmNetwork
         customAgentVmNetwork = [ vim.Network() ]
         customAgentVmNetworkName = [ "" ]

      class OvfInvalidFormat(eam.issue.VmNotDeployed): # eam.issue.OvfInvalidFormat
         error = [ vmodl.MethodFault() ]

      class VibCannotPutHostInMaintenanceMode(eam.issue.VibIssue): # eam.issue.VibCannotPutHostInMaintenanceMode
         pass

      class VibCannotPutHostOutOfMaintenanceMode(eam.issue.VibIssue): # eam.issue.VibCannotPutHostOutOfMaintenanceMode
         pass

      class VibDependenciesNotMetByHost(eam.issue.VibNotInstalled): # eam.issue.VibDependenciesNotMetByHost
         pass

      class VibInvalidFormat(eam.issue.VibNotInstalled): # eam.issue.VibInvalidFormat
         pass

      class VmCorrupted(eam.issue.VmIssue): # eam.issue.VmCorrupted
         missingFile = ""

      class VmDeployed(eam.issue.VmIssue): # eam.issue.VmDeployed
         pass

      class HostInMaintenanceMode(eam.issue.VmDeployed): # eam.issue.HostInMaintenanceMode
         pass

      class HostInStandbyMode(eam.issue.VmDeployed): # eam.issue.HostInStandbyMode
         pass

      class HostPoweredOff(eam.issue.VmDeployed): # eam.issue.HostPoweredOff
         pass

   class vib(object): # (unknown name)

      class VibInfo(vmodl.DynamicData): # eam.vib.VibInfo
         id = ""
         name = ""
         version = ""
         vendor = ""
         summary = ""
         softwareTags = eam.vib.VibInfo.SoftwareTags()
         releaseDate = vmodl.DateTime()

         class SoftwareTags(vmodl.DynamicData): # eam.vib.VibInfo.SoftwareTags
            tags = [ "" ]

   class Agent(eam.EamObject): # eam.Agent
      runtime = eam.Agent.RuntimeInfo()
      config = eam.Agent.ConfigInfo()

      def queryRuntime(): # eam.Agent.queryRuntime
         return eam.Agent.RuntimeInfo()

      def markAsAvailable(): # eam.Agent.markAsAvailable
         return None

      def queryConfig(): # eam.Agent.queryConfig
         return eam.Agent.ConfigInfo()

      class RuntimeInfo(eam.EamObject.RuntimeInfo): # eam.Agent.RuntimeInfo
         vmPowerState = vim.VirtualMachine.PowerState()
         receivingHeartBeat = False
         host = vim.HostSystem()
         vm = vim.VirtualMachine()
         vmIp = ""
         vmName = ""
         esxAgentResourcePool = vim.ResourcePool()
         esxAgentFolder = vim.Folder()
         installedBulletin = [ "" ]
         installedVibs = [ eam.vib.VibInfo() ]
         agency = eam.Agency()
         vmHook = eam.Agent.VmHook()

      class VmHook(vmodl.DynamicData): # eam.Agent.VmHook
         vm = vim.VirtualMachine()
         vmState = ""

         class VmState(Enum): # eam.Agent.VmHook.VmState
            provisioned = 0
            poweredOn = 1
            prePowerOn = 2

      class StoragePolicy(vmodl.DynamicData): # eam.Agent.StoragePolicy
         pass

      class VsanStoragePolicy(eam.Agent.StoragePolicy): # eam.Agent.VsanStoragePolicy
         profileId = ""

      class ConfigInfo(vmodl.DynamicData): # eam.Agent.ConfigInfo
         productLineId = ""
         hostVersion = ""
         ovfPackageUrl = ""
         ovfEnvironment = eam.Agent.OvfEnvironmentInfo()
         vibUrl = ""
         vibMatchingRules = [ eam.Agent.VibMatchingRule() ]
         vibName = ""
         dvFilterEnabled = False
         rebootHostAfterVibUninstall = False
         vmciService = [ "" ]
         ovfDiskProvisioning = ""
         vmStoragePolicies = [ eam.Agent.StoragePolicy() ]

         class OvfDiskProvisioning(Enum): # eam.Agent.ConfigInfo.OvfDiskProvisioning
            none = 0
            thin = 1
            thick = 2

      class OvfEnvironmentInfo(vmodl.DynamicData): # eam.Agent.OvfEnvironmentInfo
         ovfProperty = [ eam.Agent.OvfEnvironmentInfo.OvfProperty() ]

         class OvfProperty(vmodl.DynamicData): # eam.Agent.OvfEnvironmentInfo.OvfProperty
            key = ""
            value = ""

      class VibMatchingRule(vmodl.DynamicData): # eam.Agent.VibMatchingRule
         vibNameRegex = ""
         vibVersionRegex = ""

   class Agency(eam.EamObject): # eam.Agency
      solutionId = ""
      owner = ""
      config = eam.Agency.ConfigInfo()
      runtime = eam.EamObject.RuntimeInfo()
      agent = [ eam.Agent() ]

      def querySolutionId(): # eam.Agency.querySolutionId
         return ""

      def queryConfig(): # eam.Agency.queryConfig
         return eam.Agency.ConfigInfo()

      def update(config=eam.Agency.ConfigInfo()): # eam.Agency.update
         # throws eam.fault.InvalidAgentConfiguration, eam.fault.InvalidAgencyScope, eam.fault.InvalidUrl
         return None

      def queryRuntime(): # eam.Agency.queryRuntime
         return eam.EamObject.RuntimeInfo()

      def queryAgent(): # eam.Agency.queryAgent
         return [ eam.Agent() ]

      def registerAgentVm(agentVm=vim.VirtualMachine()): # eam.Agency.registerAgentVm
         # throws vmodl.fault.ManagedObjectNotFound
         return eam.Agent()

      def unregisterAgentVm(agentVm=vim.VirtualMachine()): # eam.Agency.unregisterAgentVm
         return None

      def enable(): # eam.Agency.enable
         return None

      def disable(): # eam.Agency.disable
         return None

      def uninstall(): # eam.Agency.uninstall
         return None

      def destroyAgency(): # eam.Agency.destroyAgency
         return None

      def addIssue(issue=eam.issue.Issue()): # eam.Agency.addIssue
         # throws vmodl.fault.InvalidArgument
         return eam.issue.Issue()

      class VMResourcePool(vmodl.DynamicData): # eam.Agency.VMResourcePool
         resourcePoolId = vim.ResourcePool()
         computeResourceId = vim.ComputeResource()

      class VMFolder(vmodl.DynamicData): # eam.Agency.VMFolder
         folderId = vim.Folder()
         datacenterId = vim.Datacenter()

      class ConfigInfo(vmodl.DynamicData): # eam.Agency.ConfigInfo
         agentConfig = [ eam.Agent.ConfigInfo() ]
         scope = eam.Agency.Scope()
         manuallyMarkAgentVmAvailableAfterProvisioning = False
         manuallyMarkAgentVmAvailableAfterPowerOn = False
         optimizedDeploymentEnabled = False
         agentName = ""
         agencyName = ""
         manuallyProvisioned = False
         manuallyMonitored = False
         bypassVumEnabled = False
         agentVmNetwork = [ vim.Network() ]
         agentVmDatastore = [ vim.Datastore() ]
         preferHostConfiguration = False
         ipPool = vim.vApp.IpPool()
         resourcePools = [ eam.Agency.VMResourcePool() ]
         folders = [ eam.Agency.VMFolder() ]

      class Scope(vmodl.DynamicData): # eam.Agency.Scope
         pass

      class ComputeResourceScope(eam.Agency.Scope): # eam.Agency.ComputeResourceScope
         computeResource = [ vim.ComputeResource() ]

   class EsxAgentManager(eam.EamObject): # eam.EsxAgentManager
      agency = [ eam.Agency() ]
      issue = [ eam.issue.Issue() ]

      def queryAgency(): # eam.EsxAgentManager.queryAgency
         return [ eam.Agency() ]

      def createAgency(agencyConfigInfo=eam.Agency.ConfigInfo(), initialGoalState=""): # eam.EsxAgentManager.createAgency
         # throws eam.fault.InvalidAgentConfiguration, eam.fault.InvalidAgencyScope, eam.fault.InvalidUrl
         return eam.Agency()

      def scanForUnknownAgentVm(): # eam.EsxAgentManager.scanForUnknownAgentVm
         return None
