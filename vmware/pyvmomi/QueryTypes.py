from enum import Enum

class vmodl(object): # (unknown name)

   class query(object): # (unknown name)

      class InvalidCollectorVersion(vmodl.MethodFault): # vmodl.query.InvalidCollectorVersion
         pass

      class InvalidProperty(vmodl.MethodFault): # vmodl.query.InvalidProperty
         name = vmodl.PropertyPath()

      class PropertyCollector(vmodl.ManagedObject): # vmodl.query.PropertyCollector
         filter = [ vmodl.query.PropertyCollector.Filter() ]

         def createFilter(spec=vmodl.query.PropertyCollector.FilterSpec(), partialUpdates=False): # vmodl.query.PropertyCollector.createFilter
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.Filter()

         def retrieveContents(specSet=[ vmodl.query.PropertyCollector.FilterSpec() ]): # vmodl.query.PropertyCollector.retrieveContents
            # throws vmodl.query.InvalidProperty
            return [ vmodl.query.PropertyCollector.ObjectContent() ]

         def checkForUpdates(version="" or None): # vmodl.query.PropertyCollector.checkForUpdates
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def waitForUpdates(version="" or None): # vmodl.query.PropertyCollector.waitForUpdates
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def cancelWaitForUpdates(): # vmodl.query.PropertyCollector.cancelWaitForUpdates
            return None

         def waitForUpdatesEx(version="" or None, options=vmodl.query.PropertyCollector.WaitOptions() or None): # vmodl.query.PropertyCollector.waitForUpdatesEx
            # throws vmodl.query.InvalidCollectorVersion
            return vmodl.query.PropertyCollector.UpdateSet()

         def retrievePropertiesEx(specSet=[ vmodl.query.PropertyCollector.FilterSpec() ], options=vmodl.query.PropertyCollector.RetrieveOptions()): # vmodl.query.PropertyCollector.retrievePropertiesEx
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.RetrieveResult()

         def continueRetrievePropertiesEx(token=""): # vmodl.query.PropertyCollector.continueRetrievePropertiesEx
            # throws vmodl.query.InvalidProperty
            return vmodl.query.PropertyCollector.RetrieveResult()

         def cancelRetrievePropertiesEx(token=""): # vmodl.query.PropertyCollector.cancelRetrievePropertiesEx
            # throws vmodl.query.InvalidProperty
            return None

         def createPropertyCollector(): # vmodl.query.PropertyCollector.createPropertyCollector
            return vmodl.query.PropertyCollector()

         def destroy(): # vmodl.query.PropertyCollector.destroy
            return None

         class FilterSpec(vmodl.DynamicData): # vmodl.query.PropertyCollector.FilterSpec
            propSet = [ vmodl.query.PropertyCollector.PropertySpec() ]
            objectSet = [ vmodl.query.PropertyCollector.ObjectSpec() ]
            reportMissingObjectsInResults = False

         class PropertySpec(vmodl.DynamicData): # vmodl.query.PropertyCollector.PropertySpec
            type = vmodl.TypeName()
            all = False
            pathSet = [ vmodl.PropertyPath() ]

         class ObjectSpec(vmodl.DynamicData): # vmodl.query.PropertyCollector.ObjectSpec
            obj = vmodl.ManagedObject()
            skip = False
            selectSet = [ vmodl.query.PropertyCollector.SelectionSpec() ]

         class SelectionSpec(vmodl.DynamicData): # vmodl.query.PropertyCollector.SelectionSpec
            name = ""

         class TraversalSpec(vmodl.query.PropertyCollector.SelectionSpec): # vmodl.query.PropertyCollector.TraversalSpec
            type = vmodl.TypeName()
            path = vmodl.PropertyPath()
            skip = False
            selectSet = [ vmodl.query.PropertyCollector.SelectionSpec() ]

         class Filter(vmodl.ManagedObject): # vmodl.query.PropertyCollector.Filter
            spec = vmodl.query.PropertyCollector.FilterSpec()
            partialUpdates = False

            def destroy(): # vmodl.query.PropertyCollector.Filter.destroy
               return None

         class ObjectContent(vmodl.DynamicData): # vmodl.query.PropertyCollector.ObjectContent
            obj = vmodl.ManagedObject()
            propSet = [ vmodl.DynamicProperty() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingProperty() ]

         class UpdateSet(vmodl.DynamicData): # vmodl.query.PropertyCollector.UpdateSet
            version = ""
            filterSet = [ vmodl.query.PropertyCollector.FilterUpdate() ]
            truncated = False

         class FilterUpdate(vmodl.DynamicData): # vmodl.query.PropertyCollector.FilterUpdate
            filter = vmodl.query.PropertyCollector.Filter()
            objectSet = [ vmodl.query.PropertyCollector.ObjectUpdate() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingObject() ]

         class ObjectUpdate(vmodl.DynamicData): # vmodl.query.PropertyCollector.ObjectUpdate
            kind = vmodl.query.PropertyCollector.ObjectUpdate.Kind()
            obj = vmodl.ManagedObject()
            changeSet = [ vmodl.query.PropertyCollector.Change() ]
            missingSet = [ vmodl.query.PropertyCollector.MissingProperty() ]

            class Kind(Enum): # vmodl.query.PropertyCollector.ObjectUpdate.Kind
               modify = 0
               enter = 1
               leave = 2

         class Change(vmodl.DynamicData): # vmodl.query.PropertyCollector.Change
            name = vmodl.PropertyPath()
            op = vmodl.query.PropertyCollector.Change.Op()
            val = {}

            class Op(Enum): # vmodl.query.PropertyCollector.Change.Op
               add = 0
               remove = 1
               assign = 2
               indirectRemove = 3

         class MissingProperty(vmodl.DynamicData): # vmodl.query.PropertyCollector.MissingProperty
            path = vmodl.PropertyPath()
            fault = vmodl.MethodFault()

         class MissingObject(vmodl.DynamicData): # vmodl.query.PropertyCollector.MissingObject
            obj = vmodl.ManagedObject()
            fault = vmodl.MethodFault()

         class WaitOptions(vmodl.DynamicData): # vmodl.query.PropertyCollector.WaitOptions
            maxWaitSeconds = 0
            maxObjectUpdates = 0

         class RetrieveOptions(vmodl.DynamicData): # vmodl.query.PropertyCollector.RetrieveOptions
            maxObjects = 0

         class RetrieveResult(vmodl.DynamicData): # vmodl.query.PropertyCollector.RetrieveResult
            token = ""
            objects = [ vmodl.query.PropertyCollector.ObjectContent() ]
