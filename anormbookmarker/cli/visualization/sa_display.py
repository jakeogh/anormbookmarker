#!/usr/bin/env python3

import click
from anormbookmarker.model import *
from anormbookmarker.model.BookmarkClassConstructor import tagbookmarks_table
from anormbookmarker.test.test_enviroment import Tag
from anormbookmarker.test.test_enviroment import Bookmark
from kcl.sqlalchemy.model.Filename import Filename

#from kcl.sqlalchemy.model.FileRecord import Filename
#from kcl.sqlalchemy.model.FileRecord import Path
from kcl.sqlalchemy.visualization.sa_display import sa_display as kcl_sa_display

@click.command()
def sa_display():
    #import IPython; IPython.embed()
    kcl_sa_display(globals())
