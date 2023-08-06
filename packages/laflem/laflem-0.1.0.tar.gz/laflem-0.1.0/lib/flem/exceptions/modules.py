'''
Define module exceptions.
'''

from .base import FlemException

class ModuleNotFound(FlemException):
  '''
  Raised when a module is not found.
  '''
