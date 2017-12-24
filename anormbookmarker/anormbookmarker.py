#!/usr/bin/env python3

import shutil
import click
from sqlalchemy_utils.functions import database_exists
from sqlalchemy_utils.functions import create_database
from kcl.sqlalchemy.test import test as kcltest
from kcl.sqlalchemy.print_database import print_database
from .Config import CONFIG
#from kcl.sqlalchemy.model.Config import CONFIG
from kcl.sqlalchemy.self_contained_session import self_contained_session
from kcl.sqlalchemy.BaseMixin import BASE

__version__ = 0.01

# https://github.com/mitsuhiko/click/issues/441
CONTEXT_SETTINGS = \
    dict(help_option_names=['--help'],
         terminal_width=shutil.get_terminal_size((80, 20)).columns)

# pylint: disable=C0326
# http://pylint-messages.wikidot.com/messages:c0326
@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', is_flag=True)
@click.option('--database', is_flag=False, type=str, required=False)
@click.option('--temp-database', is_flag=True, required=False, default=True)
@click.pass_context
def anormbookmarker(ctx, verbose, database, temp_database):
    '''anormbookmarker'''
    if database:
        if temp_database:
            eprint("Error: --database and --temp-database are mutually exclusive.")
            quit(1)
        CONFIG.database = database
    elif temp_database:
        CONFIG.database = CONFIG.database_timestamp
    else:
        CONFIG.database = CONFIG.database_real('anormbookmarker')
    if not database_exists(CONFIG.database):
        create_database(CONFIG.database)
        with self_contained_session(CONFIG.database) as session:
            BASE.metadata.create_all(session.bind)
    if verbose:
        eprint(CONFIG.database)
    ctx.obj = CONFIG
    pass


@anormbookmarker.command()
@click.option('--package', is_flag=False, type=str, required=False, default='anormbookmarker')
@click.option('--keep-databases', is_flag=True)
@click.option('--count', is_flag=False, type=int, required=False)
@click.option('--test-class', is_flag=False, type=str, required=False)
@click.option('--test-match', is_flag=False, type=str, required=False)
def test(package, keep_databases, count, test_class, test_match):
    kcltest(package=package, keep_databases=keep_databases, count=count, test_class=test_class, test_match=test_match)

anormbookmarker.add_command(print_database)
