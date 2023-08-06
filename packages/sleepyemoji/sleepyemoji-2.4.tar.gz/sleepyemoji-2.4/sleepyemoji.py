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
  1. Append lists in toolchain/emojis.py
  2. Update pypi package:
    - poetry config http-basic.pypi sleepyboy <password>
    - poetry version <next-version>
    - poetry build
    - poetry publish
    - pip install sleepyemoji --upgrade # pull down update
  3. Update repository
'''

# stdlib
from typing import List, Dict, Union
from sys import argv, exit, getsizeof
from subprocess import call, check_output
# custom modules
from toolchain.commands import sleepyemoji_logic
# 3rd party
try:
  import typer
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)


#───Globals──────────────────
app = typer.Typer()


#───Commands─────────────────
@app.command()
def sleepyemoji(categories:List[str]) -> str:
  '''Another example command

  Prints emojis with some metadata, organized by category.\n
  ───Params\n
  categories:List[str] :: emoji categories to include (casing ignored)

  ───Categories\n
    animals, a\n
    faces, f\n
    hands, h\n
    icons, i\n
    people, p\n
    combos, combinations\n
    all\n

  ───Example\n
    ./sleepyemoji.py a f h

  ───Return\n
  str :: prettytable string
  '''
  return sleepyemoji_logic(categories)


#───Entry────────────────────
if __name__ == "__main__":
  app()
