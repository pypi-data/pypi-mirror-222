#!/usr/bin/env python

'''README
Usage:
  # pip install sleepyemoji
  # pip install --upgrade sleepyemoji

  from sleepyemoji import sleepyemoji
  from sys import argv, exit

  sleepyemoji(argv[1:])
  exit(0)

Adding Emojis:
  1. New category? Update toolchain/commands.py
  2. Append lists in toolchain/emojis.py
  3. Update pypi package:
  4. Update repository
'''

# stdlib
import os
from typing import List
from sys import exit
# custom modules
from toolchain.commands import run_logic
# 3rd party
try:
  import typer
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)


#───Globals──────────────────



#───Commands─────────────────
def sleepyemoji(categories:List[str]) -> str:
  app = typer.Typer()
  @app.command()
  def run(categories:List[str]) -> str:
    '''Another example command

    Prints emojis with some metadata, organized by category.
    ───Params
    categories:List[str] :: emoji categories to include (casing ignored)

    ───Categories
      animals, a
      faces, f
      hands, h
      icons, i
      people, p
      combos, combinations
      all

    ───Example
      ./sleepyemoji.py a f h

    ───Return
    str :: prettytable string
    '''
    if not categories:
      os.environ['PAGER'] = 'cat'
      help(sleepyemoji)
      exit(1)
    return run_logic(categories)
  
  if __name__ == "__run__":
    app()


#───Entry────────────────────
