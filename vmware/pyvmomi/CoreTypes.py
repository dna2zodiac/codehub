from enum import Enum

class vmodl(object): # (unknown name)

   class URI(object): # vmodl.URI
      pass

   class Binary(object): # vmodl.Binary
      pass

   class DateTime(object): # vmodl.DateTime
      pass

   class TypeName(object): # vmodl.TypeName
      pass

   class MethodName(object): # vmodl.MethodName
      pass

   class DataObject(object): # vmodl.DataObject
      pass

   class ManagedObject(object): # vmodl.ManagedObject
      pass

   class PropertyPath(object): # vmodl.PropertyPath
      pass

   class MethodFault(vmodl.DynamicData): # vmodl.MethodFault
      msg = ""
      faultCause = vmodl.MethodFault()
      faultMessage = [ vmodl.LocalizableMessage() ]

   class RuntimeFault(vmodl.MethodFault): # vmodl.RuntimeFault
      pass

   class LocalizedMethodFault(vmodl.MethodFault): # vmodl.LocalizedMethodFault
      fault = vmodl.MethodFault()
      localizedMessage = ""

   class DynamicArray(vmodl.DataObject): # vmodl.DynamicArray
      dynamicType = ""
      val = [ {} ]

   class DynamicData(vmodl.DataObject): # vmodl.DynamicData
      dynamicType = ""
      dynamicProperty = [ vmodl.DynamicProperty() ]

   class DynamicProperty(vmodl.DataObject): # vmodl.DynamicProperty
      name = vmodl.PropertyPath()
      val = {}

   class KeyAnyValue(vmodl.DynamicData): # vmodl.KeyAnyValue
      key = ""
      value = {}

   class LocalizableMessage(vmodl.DynamicData): # vmodl.LocalizableMessage
      key = ""
      arg = [ vmodl.KeyAnyValue() ]
      message = ""

   class fault(object): # (unknown name)

      class HostCommunication(vmodl.RuntimeFault): # vmodl.fault.HostCommunication
         pass

      class HostNotConnected(vmodl.fault.HostCommunication): # vmodl.fault.HostNotConnected
         pass

      class HostNotReachable(vmodl.fault.HostCommunication): # vmodl.fault.HostNotReachable
         pass

      class InvalidArgument(vmodl.RuntimeFault): # vmodl.fault.InvalidArgument
         invalidProperty = vmodl.PropertyPath()

      class InvalidRequest(vmodl.RuntimeFault): # vmodl.fault.InvalidRequest
         pass

      class InvalidType(vmodl.fault.InvalidRequest): # vmodl.fault.InvalidType
         argument = vmodl.PropertyPath()

      class ManagedObjectNotFound(vmodl.RuntimeFault): # vmodl.fault.ManagedObjectNotFound
         obj = vmodl.ManagedObject()

      class MethodNotFound(vmodl.fault.InvalidRequest): # vmodl.fault.MethodNotFound
         receiver = vmodl.ManagedObject()
         method = ""

      class NotEnoughLicenses(vmodl.RuntimeFault): # vmodl.fault.NotEnoughLicenses
         pass

      class NotImplemented(vmodl.RuntimeFault): # vmodl.fault.NotImplemented
         pass

      class NotSupported(vmodl.RuntimeFault): # vmodl.fault.NotSupported
         pass

      class RequestCanceled(vmodl.RuntimeFault): # vmodl.fault.RequestCanceled
         pass

      class SecurityError(vmodl.RuntimeFault): # vmodl.fault.SecurityError
         pass

      class SystemError(vmodl.RuntimeFault): # vmodl.fault.SystemError
         reason = ""

      class UnexpectedFault(vmodl.RuntimeFault): # vmodl.fault.UnexpectedFault
         faultName = vmodl.TypeName()
         fault = vmodl.MethodFault()
