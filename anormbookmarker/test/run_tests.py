#!/usr/bin/env python3

from kcl.dirops import all_files
import os

os.system('sudo /home/cfg/database/postgresql/start')

if __name__ == '__main__':
    for test_file in all_files('./tests/'):
        if test_file.endswith('''.py''') and not test_file.endswith('__init__.py'):
            print("\nrunning test:", test_file)
            exit_status = os.WEXITSTATUS(os.system(test_file))
            if exit_status != 0:
                quit(exit_status)

    print("\n\nAll Tests Completed OK")
