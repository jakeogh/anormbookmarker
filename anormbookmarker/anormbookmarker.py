#!/usr/bin/env python3

import click
import shutil
from kcl.logops import set_verbose
from kcl.sqlalchemy.test import test as kcltest
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

@anormbookmarker.command()
@click.option('--keep-databases', is_flag=True)
@click.option('--count', is_flag=False, type=int, required=False)
@click.option('--test-class', is_flag=False, type=str, required=False)
@click.option('--test-match', is_flag=False, type=str, required=False)
def test(keep_databases, count, test_class):
    kcltest('anormbookmarker', keep_databases=keep_databases, count=count, test_class=test_class)

anormbookmarker.add_command(print_database)
