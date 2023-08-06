#!/usr/bin/env python

'''README
<readme-blurb>

❕ There is a CLIPME docstring at the bottom that serves a quick reference for useful python factoids that aren't particularly memorable, remove after development
❕ Re-populate this README docstring with whatever makes sense
❕ Remove unused imports
❕ Remove example command
❕ Run `poetry init` to generate basic pyproject.toml (consult existing examples)
'''

# stdlib
from os import path
from pathlib import Path
from typing import List, Dict, Union
from sys import argv, exit, getsizeof
from subprocess import call, check_output
# custom modules
from toolchain.commands import datapeek_logic
# 3rd party
try:
  import typer
  from yaml import safe_load, YAMLError
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)


def sleepydatapeek(input_path:str, output_path:str='') -> str:
  app = typer.Typer()
  @app.command()
  def datapeek(input_path:str, output_path:str='') -> str:
    '''TITLE

    DESCRIPTION

    ───Params
    my_param:type :: description

    ───Return
    type :: description
    '''
    return datapeek_logic(input_path, output_path)
  if (__name__ == 'sleepydatapeek') or (__name__ == '__main__'):
    app()


## Local Testing
# sleepydatapeek(argv)
