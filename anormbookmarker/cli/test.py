#!/usr/bin/env python3

import click
from kcl.dirops import all_files
from kcl.printops import eprint
import os
import pkg_resources


TEST_PATH = pkg_resources.resource_filename('anormbookmarker', 'test/tests')

@click.command()
def test():
    eprint("TEST_PATH:", TEST_PATH)
    os.system('sudo /home/cfg/database/postgresql/start')
    for test_file in all_files(TEST_PATH):
        if test_file.endswith('''.py''') and not test_file.endswith('__init__.py'):
            print("\nrunning test:", test_file)
            exit_status = os.WEXITSTATUS(os.system(test_file))
            if exit_status != 0:
                quit(exit_status)

    print("\n\nAll Tests Completed OK")

