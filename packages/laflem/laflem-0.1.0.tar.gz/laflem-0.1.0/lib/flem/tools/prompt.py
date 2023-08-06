'''
Define prompt related tools used in flem.
'''
from flem.log import console

def prompt(message):
  '''
  Prompt the user for an input.
  Return the inputed value.
  '''
  return console.input(message)
