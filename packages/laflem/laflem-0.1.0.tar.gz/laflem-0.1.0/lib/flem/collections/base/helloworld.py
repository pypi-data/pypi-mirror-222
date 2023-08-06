'''
Define the helloworld module.
This module is used to print an "Hello World!".
This is a demonstration module.
'''

from flem.log import console

class HelloWorldModule:
  '''
  The helloworld module.
  '''
  name = "helloworld"
  description = "Just an Hello World module."
  version = "0.1.0"

  def run(self, *_args, **_kwargs):
    '''
    Run the module.
    '''
    console.print(r"""\
 _  _     _ _      __      __       _    _ _ 
| || |___| | |___  \ \    / /__ _ _| |__| | |
| __ / -_) | / _ \  \ \/\/ / _ \ '_| / _` |_|
|_||_\___|_|_\___/   \_/\_/\___/_| |_\__,_(_)\
""", style="bold green")

  @classmethod
  def build_parser(cls, parser):
    '''
    Add arguments to the parser or options.
    '''
