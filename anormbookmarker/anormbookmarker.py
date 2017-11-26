#!/usr/bin/env python3

import click
import shutil
from kcl.logops import set_verbose
from .cli.test import test
from kcl.sqlalchemy.print_database import print_database

__version__ = 0.01

# https://github.com/mitsuhiko/click/issues/441
CONTEXT_SETTINGS = \
    dict(help_option_names=['--help'],
         terminal_width=shutil.get_terminal_size((80, 20)).columns)

# pylint: disable=C0326
# http://pylint-messages.wikidot.com/messages:c0326
@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', is_flag=True, callback=set_verbose, expose_value=False)
@click.pass_context
def anormbookmarker(ctx):
    '''anormbookmarker'''
    pass

anormbookmarker.add_command(test)
anormbookmarker.add_command(print_database)
