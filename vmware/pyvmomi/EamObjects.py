from enum import Enum

class eam(object):

   class EamObject(vmodl.ManagedObject):

      def resolve(issueKey=[ 0 ]):
         return [ 0 ]

      def resolveAll():
         return None

      def queryIssue(issueKey=[ 0 ] or None):
         return [ eam.issue.Issue() ]

      class RuntimeInfo(vmodl.DynamicData):
         status = ""
         issue = [ eam.issue.Issue() ]
         goalState = ""
         entity = eam.EamObject()

         class Status(Enum):
            green = 0
            yellow = 1
            red = 2

         class GoalState(Enum):
            enabled = 0
            disabled = 1
            uninstalled = 2

   class Task(vmodl.ManagedObject):
      pass

   class fault(object):

      class EamFault(vmodl.MethodFault):
         pass

      class EamRuntimeFault(vmodl.RuntimeFault):
         pass

      class EamServiceNotInitialized(eam.fault.EamRuntimeFault):
         pass

      class EamSystemFault(eam.fault.EamRuntimeFault):
         pass

      class InvalidAgencyScope(eam.fault.EamFault):
         unknownComputeResource = [ vim.ComputeResource() ]

      class InvalidLogin(eam.fault.EamRuntimeFault):
         pass

      class InvalidUrl(eam.fault.EamFault):
         url = ""
         malformedUrl = False
         unknownHost = False
         connectionRefused = False
         responseCode = 0

      class InvalidVibPackage(eam.fault.EamRuntimeFault):
         pass

      class NoConnectionToVCenter(eam.fault.EamRuntimeFault):
         pass

      class NotAuthorized(eam.fault.EamRuntimeFault):
         pass

      class EamAppFault(eam.fault.EamRuntimeFault):
         pass

      class EamIOFault(eam.fault.EamRuntimeFault):
         pass

      class InvalidAgentConfiguration(eam.fault.EamFault):
         invalidAgentConfiguration = eam.Agent.ConfigInfo()
         invalidField = ""

      class InvalidState(eam.fault.EamAppFault):
         pass

   class issue(object):

      class Issue(vmodl.DynamicData):
         key = 0
         description = ""
         time = vmodl.DateTime()

      class AgencyIssue(eam.issue.Issue):
         agency = eam.Agency()
         agencyName = ""
         solutionId = ""
         solutionName = ""

      class AgentIssue(eam.issue.AgencyIssue):
         agent = eam.Agent()
         agentName = ""
         host = vim.HostSystem()
         hostName = ""

      class ExtensibleIssue(eam.issue.Issue):
         typeId = ""
         argument = [ vmodl.KeyAnyValue() ]
         target = vim.ManagedEntity()
         agent = eam.Agent()
         agency = eam.Agency()

      class HostIssue(eam.issue.Issue):
         host = vim.HostSystem()

      class HostNotReachable(eam.issue.AgentIssue):
         pass

      class MissingDvFilterSwitch(eam.issue.AgentIssue):
         pass

      class OrphanedAgency(eam.issue.AgencyIssue):
         pass

      class OrphanedDvFilterSwitch(eam.issue.HostIssue):
         pass

      class OvfInvalidProperty(eam.issue.AgentIssue):
         error = [ vmodl.MethodFault() ]

      class UnknownAgentVm(eam.issue.HostIssue):
         vm = vim.VirtualMachine()

      class VibIssue(eam.issue.AgentIssue):
         pass

      class VibNotInstalled(eam.issue.VibIssue):
         pass

      class VibRequirementsNotMetByHost(eam.issue.VibNotInstalled):
         pass

      class VibRequiresHostInMaintenanceMode(eam.issue.VibIssue):
         pass

      class VibRequiresHostReboot(eam.issue.VibIssue):
         pass

      class VibRequiresManualInstallation(eam.issue.VibIssue):
         bulletin = [ "" ]

      class VibRequiresManualUninstallation(eam.issue.VibIssue):
         bulletin = [ "" ]

      class VmIssue(eam.issue.AgentIssue):
         vm = vim.VirtualMachine()

      class VmMarkedAsTemplate(eam.issue.VmIssue):
         pass

      class VmNotDeployed(eam.issue.AgentIssue):
         pass

      class VmOrphaned(eam.issue.VmIssue):
         pass

      class VmPoweredOff(eam.issue.VmIssue):
         pass

      class VmPoweredOn(eam.issue.VmIssue):
         pass

      class VmSuspended(eam.issue.VmIssue):
         pass

      class VmWrongFolder(eam.issue.VmIssue):
         currentFolder = vim.Folder()
         requiredFolder = vim.Folder()

      class VmWrongResourcePool(eam.issue.VmIssue):
         currentResourcePool = vim.ResourcePool()
         requiredResourcePool = vim.ResourcePool()

      class cluster(object):

         class agent(object):

            class AgentIssue(eam.issue.AgencyIssue):
               agent = eam.Agent()
               cluster = vim.ComputeResource()

            class OvfInvalidProperty(eam.issue.cluster.agent.AgentIssue):
               error = [ vmodl.MethodFault() ]

            class VmIssue(eam.issue.cluster.agent.AgentIssue):
               vm = vim.VirtualMachine()

            class VmNotDeployed(eam.issue.cluster.agent.AgentIssue):
               pass

            class VmNotRemoved(eam.issue.cluster.agent.VmIssue):
               pass

            class VmPoweredOff(eam.issue.cluster.agent.VmIssue):
               pass

            class VmPoweredOn(eam.issue.cluster.agent.VmIssue):
               pass

            class VmSuspended(eam.issue.cluster.agent.VmIssue):
               pass

            class InsufficientClusterResources(eam.issue.cluster.agent.VmPoweredOff):
               pass

            class InsufficientClusterSpace(eam.issue.cluster.agent.VmNotDeployed):
               pass

            class InvalidConfig(eam.issue.cluster.agent.VmIssue):
               error = anyType()

            class MissingClusterVmDatastore(eam.issue.cluster.agent.VmNotDeployed):
               missingDatastores = [ vim.Datastore() ]

            class MissingClusterVmNetwork(eam.issue.cluster.agent.VmNotDeployed):
               missingNetworks = [ vim.Network() ]
               networkNames = [ "" ]

      class integrity(object):

         class agency(object):

            class VUMIssue(eam.issue.AgencyIssue):
               pass

            class VUMUnavailable(eam.issue.integrity.agency.VUMIssue):
               pass

            class CannotDeleteSoftware(eam.issue.integrity.agency.VUMIssue):
               pass

            class CannotStageSoftware(eam.issue.integrity.agency.VUMIssue):
               pass

      class personality(object):

         class agency(object):

            class PMIssue(eam.issue.AgencyIssue):
               pass

            class PMUnavailable(eam.issue.personality.agency.PMIssue):
               pass

            class CannotConfigureSolutions(eam.issue.personality.agency.PMIssue):
               cr = vim.ComputeResource()
               solutionsToModify = [ "" ]
               solutionsToRemove = [ "" ]

            class DepotIssue(eam.issue.personality.agency.PMIssue):
               remoteDepotUrl = ""

            class InaccessibleDepot(eam.issue.personality.agency.DepotIssue):
               pass

            class InvalidDepot(eam.issue.personality.agency.DepotIssue):
               pass

            class CannotUploadDepot(eam.issue.personality.agency.DepotIssue):
               localDepotUrl = ""

         class agent(object):

            class PMIssue(eam.issue.AgentIssue):
               pass

            class AwaitingPMRemediation(eam.issue.personality.agent.PMIssue):
               pass

            class BlockedByAgencyOperation(eam.issue.personality.agent.PMIssue):
               pass

      class CannotAccessAgentOVF(eam.issue.VmNotDeployed):
         downloadUrl = ""

      class CannotAccessAgentVib(eam.issue.VibNotInstalled):
         downloadUrl = ""

      class ImmediateHostRebootRequired(eam.issue.VibIssue):
         pass

      class IncompatibleHostVersion(eam.issue.VmNotDeployed):
         pass

      class InsufficientIpAddresses(eam.issue.VmPoweredOff):
         network = vim.Network()

      class InsufficientResources(eam.issue.VmNotDeployed):
         pass

      class InsufficientSpace(eam.issue.VmNotDeployed):
         pass

      class InvalidConfig(eam.issue.VmIssue):
         error = anyType()

      class MissingAgentIpPool(eam.issue.VmPoweredOff):
         network = vim.Network()

      class NoAgentVmDatastore(eam.issue.VmNotDeployed):
         pass

      class NoAgentVmNetwork(eam.issue.VmNotDeployed):
         pass

      class NoCustomAgentVmDatastore(eam.issue.NoAgentVmDatastore):
         customAgentVmDatastore = [ vim.Datastore() ]
         customAgentVmDatastoreName = [ "" ]

      class NoCustomAgentVmNetwork(eam.issue.NoAgentVmNetwork):
         customAgentVmNetwork = [ vim.Network() ]
         customAgentVmNetworkName = [ "" ]

      class OvfInvalidFormat(eam.issue.VmNotDeployed):
         error = [ vmodl.MethodFault() ]

      class VibCannotPutHostInMaintenanceMode(eam.issue.VibIssue):
         pass

      class VibCannotPutHostOutOfMaintenanceMode(eam.issue.VibIssue):
         pass

      class VibDependenciesNotMetByHost(eam.issue.VibNotInstalled):
         pass

      class VibInvalidFormat(eam.issue.VibNotInstalled):
         pass

      class VmCorrupted(eam.issue.VmIssue):
         missingFile = ""

      class VmDeployed(eam.issue.VmIssue):
         pass

      class HostInMaintenanceMode(eam.issue.VmDeployed):
         pass

      class HostInStandbyMode(eam.issue.VmDeployed):
         pass

      class HostPoweredOff(eam.issue.VmDeployed):
         pass

   class vib(object):

      class VibInfo(vmodl.DynamicData):
         id = ""
         name = ""
         version = ""
         vendor = ""
         summary = ""
         softwareTags = eam.vib.VibInfo.SoftwareTags()
         releaseDate = vmodl.DateTime()

         class SoftwareTags(vmodl.DynamicData):
            tags = [ "" ]

   class Agent(eam.EamObject):
      runtime = eam.Agent.RuntimeInfo()
      config = eam.Agent.ConfigInfo()

      def queryRuntime():
         return eam.Agent.RuntimeInfo()

      def markAsAvailable():
         return None

      def queryConfig():
         return eam.Agent.ConfigInfo()

      class RuntimeInfo(eam.EamObject.RuntimeInfo):
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

      class VmHook(vmodl.DynamicData):
         vm = vim.VirtualMachine()
         vmState = ""

         class VmState(Enum):
            provisioned = 0
            poweredOn = 1
            prePowerOn = 2

      class StoragePolicy(vmodl.DynamicData):
         pass

      class VsanStoragePolicy(eam.Agent.StoragePolicy):
         profileId = ""

      class ConfigInfo(vmodl.DynamicData):
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

         class OvfDiskProvisioning(Enum):
            none = 0
            thin = 1
            thick = 2

      class OvfEnvironmentInfo(vmodl.DynamicData):
         ovfProperty = [ eam.Agent.OvfEnvironmentInfo.OvfProperty() ]

         class OvfProperty(vmodl.DynamicData):
            key = ""
            value = ""

      class VibMatchingRule(vmodl.DynamicData):
         vibNameRegex = ""
         vibVersionRegex = ""

   class Agency(eam.EamObject):
      solutionId = ""
      owner = ""
      config = eam.Agency.ConfigInfo()
      runtime = eam.EamObject.RuntimeInfo()
      agent = [ eam.Agent() ]

      def querySolutionId():
         return ""

      def queryConfig():
         return eam.Agency.ConfigInfo()

      def update(config=eam.Agency.ConfigInfo()):
         # throws eam.fault.InvalidAgentConfiguration, eam.fault.InvalidAgencyScope, eam.fault.InvalidUrl
         return None

      def queryRuntime():
         return eam.EamObject.RuntimeInfo()

      def queryAgent():
         return [ eam.Agent() ]

      def registerAgentVm(agentVm=vim.VirtualMachine()):
         # throws vmodl.fault.ManagedObjectNotFound
         return eam.Agent()

      def unregisterAgentVm(agentVm=vim.VirtualMachine()):
         return None

      def enable():
         return None

      def disable():
         return None

      def uninstall():
         return None

      def destroyAgency():
         return None

      def addIssue(issue=eam.issue.Issue()):
         # throws vmodl.fault.InvalidArgument
         return eam.issue.Issue()

      class VMResourcePool(vmodl.DynamicData):
         resourcePoolId = vim.ResourcePool()
         computeResourceId = vim.ComputeResource()

      class VMFolder(vmodl.DynamicData):
         folderId = vim.Folder()
         datacenterId = vim.Datacenter()

      class ConfigInfo(vmodl.DynamicData):
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

      class Scope(vmodl.DynamicData):
         pass

      class ComputeResourceScope(eam.Agency.Scope):
         computeResource = [ vim.ComputeResource() ]

   class EsxAgentManager(eam.EamObject):
      agency = [ eam.Agency() ]
      issue = [ eam.issue.Issue() ]

      def queryAgency():
         return [ eam.Agency() ]

      def createAgency(agencyConfigInfo=eam.Agency.ConfigInfo(), initialGoalState=""):
         # throws eam.fault.InvalidAgentConfiguration, eam.fault.InvalidAgencyScope, eam.fault.InvalidUrl
         return eam.Agency()

      def scanForUnknownAgentVm():
         return None
