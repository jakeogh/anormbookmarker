#!/usr/bin/env python3

import click
from kcl.dirops import all_files
import os
import pkg_resources


DATA_PATH = pkg_resources.resource_filename('<package name>', 'cli/test/tests/')

@click.command()
def test():
    os.system('sudo /home/cfg/database/postgresql/start')
    for test_file in all_files(DATA_PATH):
        if test_file.endswith('''.py''') and not test_file.endswith('__init__.py'):
            print("\nrunning test:", test_file)
            exit_status = os.WEXITSTATUS(os.system(test_file))
            if exit_status != 0:
                quit(exit_status)

    print("\n\nAll Tests Completed OK")

