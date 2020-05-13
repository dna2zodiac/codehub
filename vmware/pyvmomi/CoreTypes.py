from enum import Enum

class vmodl(object):

   class URI(object):
      pass

   class Binary(object):
      pass

   class DateTime(object):
      pass

   class TypeName(object):
      pass

   class MethodName(object):
      pass

   class DataObject(object):
      pass

   class ManagedObject(object):
      pass

   class PropertyPath(object):
      pass

   class MethodFault(vmodl.DynamicData):
      msg = ""
      faultCause = vmodl.MethodFault()
      faultMessage = [ vmodl.LocalizableMessage() ]

   class RuntimeFault(vmodl.MethodFault):
      pass

   class LocalizedMethodFault(vmodl.MethodFault):
      fault = vmodl.MethodFault()
      localizedMessage = ""

   class DynamicArray(vmodl.DataObject):
      dynamicType = ""
      val = [ anyType() ]

   class DynamicData(vmodl.DataObject):
      dynamicType = ""
      dynamicProperty = [ vmodl.DynamicProperty() ]

   class DynamicProperty(vmodl.DataObject):
      name = vmodl.PropertyPath()
      val = anyType()

   class KeyAnyValue(vmodl.DynamicData):
      key = ""
      value = anyType()

   class LocalizableMessage(vmodl.DynamicData):
      key = ""
      arg = [ vmodl.KeyAnyValue() ]
      message = ""

   class fault(object):

      class HostCommunication(vmodl.RuntimeFault):
         pass

      class HostNotConnected(vmodl.fault.HostCommunication):
         pass

      class HostNotReachable(vmodl.fault.HostCommunication):
         pass

      class InvalidArgument(vmodl.RuntimeFault):
         invalidProperty = vmodl.PropertyPath()

      class InvalidRequest(vmodl.RuntimeFault):
         pass

      class InvalidType(vmodl.fault.InvalidRequest):
         argument = vmodl.PropertyPath()

      class ManagedObjectNotFound(vmodl.RuntimeFault):
         obj = vmodl.ManagedObject()

      class MethodNotFound(vmodl.fault.InvalidRequest):
         receiver = vmodl.ManagedObject()
         method = ""

      class NotEnoughLicenses(vmodl.RuntimeFault):
         pass

      class NotImplemented(vmodl.RuntimeFault):
         pass

      class NotSupported(vmodl.RuntimeFault):
         pass

      class RequestCanceled(vmodl.RuntimeFault):
         pass

      class SecurityError(vmodl.RuntimeFault):
         pass

      class SystemError(vmodl.RuntimeFault):
         reason = ""

      class UnexpectedFault(vmodl.RuntimeFault):
         faultName = vmodl.TypeName()
         fault = vmodl.MethodFault()
