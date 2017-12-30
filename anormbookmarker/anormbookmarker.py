#!/usr/bin/env python3

import click
import builtins
from anormbookmarker.model.Config import CONFIG
builtins.config = CONFIG

from kcl.sqlalchemy.clickapp.clickapp import clickapp as anormbookmarker
anormbookmarker.help = CONFIG.appname + " interface"
CONFIG.appobject = anormbookmarker

from kcl.sqlalchemy.clickapp.default import *

from .cli.visualization.sa_display import sa_display
#from .cli.list_objects.list_objects import list_objects
#from .cli.create_objects.create_objects import create_objects

anormbookmarker.add_command(sa_display)
#anormbookmarker.add_command(display_database)
