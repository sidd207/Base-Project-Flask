class ExceptionBase(Exception):
   error_enum = None

   def __init__(self, error_code, message_params_dict={}, *args):
       self.error_enum = error_code
       self.error_code = error_code.name
       self.error_message = error_code.value.format(**message_params_dict)
       super(ExceptionBase, self).__init__(self.error_message, *args)


class DocumentNotFound(ExceptionBase):
   """If while viewing document is not found"""
   pass


class AWSException(ExceptionBase):
   """All the aws related exception will be under this blanket exception"""
   pass


class AttributeException(ExceptionBase):
   """For any function parameter value missing will be captured by this"""
   pass


class TableNameException(ExceptionBase):
   """exception for table name check"""
   pass


class FailedAPIRequest(ExceptionBase):
   """Failed API access"""
   pass


class CommercialValidatorException(ExceptionBase):
   """Failed validation for commercial"""
   pass

class TrackerIdValidatorException(ExceptionBase):
   """Failed validation for commercial"""
   pass

class ClientValidatorException(ExceptionBase):
   pass

class FcValidatorException(ExceptionBase):
   pass

class MandatoryFieldException(ExceptionBase):
   """Field in not present in object"""