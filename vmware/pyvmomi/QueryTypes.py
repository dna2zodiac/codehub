from enum import Enum

class vmodl(object):

   class query(object):

      class InvalidCollectorVersion(vmodl.MethodFault):
         pass

      class InvalidProperty(vmodl.MethodFault):
         name = vmodl.PropertyPath()

      class PropertyCollector(vmodl.ManagedObject):
         filter = [ vmodl.query.PropertyCollector.Filter() ]

         def createFilter(spec=vmodl.query.PropertyCollector.FilterSpec(), partialUpdates=False):
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.Filter()

         def retrieveContents(specSet=[ vmodl.query.PropertyCollector.FilterSpec() ]):
            # throws vmodl.query.InvalidProperty
            return [ vmodl.query.PropertyCollector.ObjectContent() ]

         def checkForUpdates(version="" or None):
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def waitForUpdates(version="" or None):
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def cancelWaitForUpdates():
            return None

         def waitForUpdatesEx(version="" or None, options=vmodl.query.PropertyCollector.WaitOptions() or None):
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def retrievePropertiesEx(specSet=[ vmodl.query.PropertyCollector.FilterSpec() ], options=vmodl.query.PropertyCollector.RetrieveOptions()):
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.RetrieveResult()

         def continueRetrievePropertiesEx(token=""):
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.RetrieveResult()

         def cancelRetrievePropertiesEx(token=""):
            # throws vmodl.query.InvalidProperty
            return None

         def createPropertyCollector():
            return vmodl.query.PropertyCollector()

         def destroy():
            return None

         class FilterSpec(vmodl.DynamicData):
            propSet = [ vmodl.query.PropertyCollector.PropertySpec() ]
            objectSet = [ vmodl.query.PropertyCollector.ObjectSpec() ]
            reportMissingObjectsInResults = False

         class PropertySpec(vmodl.DynamicData):
            type = vmodl.TypeName()
            all = False
            pathSet = [ vmodl.PropertyPath() ]

         class ObjectSpec(vmodl.DynamicData):
            obj = vmodl.ManagedObject()
            skip = False
            selectSet = [ vmodl.query.PropertyCollector.SelectionSpec() ]

         class SelectionSpec(vmodl.DynamicData):
            name = ""

         class TraversalSpec(vmodl.query.PropertyCollector.SelectionSpec):
            type = vmodl.TypeName()
            path = vmodl.PropertyPath()
            skip = False
            selectSet = [ vmodl.query.PropertyCollector.SelectionSpec() ]

         class Filter(vmodl.ManagedObject):
            spec = vmodl.query.PropertyCollector.FilterSpec()
            partialUpdates = False

            def destroy():
               return None

         class ObjectContent(vmodl.DynamicData):
            obj = vmodl.ManagedObject()
            propSet = [ vmodl.DynamicProperty() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingProperty() ]

         class UpdateSet(vmodl.DynamicData):
            version = ""
            filterSet = [ vmodl.query.PropertyCollector.FilterUpdate() ]
            truncated = False

         class FilterUpdate(vmodl.DynamicData):
            filter = vmodl.query.PropertyCollector.Filter()
            objectSet = [ vmodl.query.PropertyCollector.ObjectUpdate() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingObject() ]

         class ObjectUpdate(vmodl.DynamicData):
            kind = vmodl.query.PropertyCollector.ObjectUpdate.Kind()
            obj = vmodl.ManagedObject()
            changeSet = [ vmodl.query.PropertyCollector.Change() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingProperty() ]

            class Kind(Enum):
               modify = 0
               enter = 1
               leave = 2

         class Change(vmodl.DynamicData):
            name = vmodl.PropertyPath()
            op = vmodl.query.PropertyCollector.Change.Op()
            val = anyType()

            class Op(Enum):
               add = 0
               remove = 1
               assign = 2
               indirectRemove = 3

         class MissingProperty(vmodl.DynamicData):
            path = vmodl.PropertyPath()
            fault = vmodl.MethodFault()

         class MissingObject(vmodl.DynamicData):
            obj = vmodl.ManagedObject()
            fault = vmodl.MethodFault()

         class WaitOptions(vmodl.DynamicData):
            maxWaitSeconds = 0
            maxObjectUpdates = 0

         class RetrieveOptions(vmodl.DynamicData):
            maxObjects = 0

         class RetrieveResult(vmodl.DynamicData):
            token = ""
            objects = [ vmodl.query.PropertyCollector.ObjectContent() ]
