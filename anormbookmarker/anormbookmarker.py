#!/usr/bin/env python3


import click
import builtins
from anormbookmarker.model.Config import CONFIG
builtins.config = CONFIG

from kcl.sqlalchemy.clickapp.clickapp import clickapp as anormbookmarker
from kcl.sqlalchemy.clickapp.print_database import print_database
from kcl.sqlalchemy.clickapp.test import test
from kcl.sqlalchemy.clickapp.show_config import show_config
from kcl.sqlalchemy.ipython import ipython
from .cli.visualization.sa_display import sa_display
#from .cli.list_objects.list_objects import list_objects
#from .cli.create_objects.create_objects import create_objects

anormbookmarker.help = CONFIG.appname + " interface"

anormbookmarker.add_command(ipython)
anormbookmarker.add_command(print_database)

anormbookmarker.add_command(show_config, name='config')
#anormbookmarker.add_command(display_database)
anormbookmarker.add_command(test)
