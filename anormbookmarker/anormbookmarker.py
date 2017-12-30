#!/usr/bin/env python3

import click
import builtins
from anormbookmarker.model.Config import CONFIG
builtins.config = CONFIG

from kcl.sqlalchemy.clickapp.clickapp import clickapp as anormbookmarker
anormbookmarker.help = CONFIG.appname + " interface"

from kcl.sqlalchemy.clickapp.default import *
anormbookmarker.add_command(ipython)
anormbookmarker.add_command(print_database)
anormbookmarker.add_command(test)
anormbookmarker.add_command(show_config, name="config")

from .cli.visualization.sa_display import sa_display
#from .cli.list_objects.list_objects import list_objects
#from .cli.create_objects.create_objects import create_objects

fsindex.add_command(sa_display)

#anormbookmarker.add_command(display_database)
