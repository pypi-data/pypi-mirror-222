'''
Define the ask module.
This module is used to ask the user about him.
This is a demonstration module.
'''

from flem.log import console
from flem.tools.prompt import prompt

class AskModule:
  '''
  The ask module.
  '''
  name = "ask"
  description = "Ask the user about him."
  version = "0.1.0"

  def run(self, *_args, **_kwargs):
    '''
    Run the module.
    '''
    name = None
    while not name:
      name = prompt("What is your [bold red]name[/] ? :smiley: ")
      if not name:
        console.print("Please enter your name.", style="blue")

    console.print(f"Hello, {name} !", style="green")

  @classmethod
  def build_parser(cls, parser):
    '''
    Add arguments to the parser or options.
    '''
