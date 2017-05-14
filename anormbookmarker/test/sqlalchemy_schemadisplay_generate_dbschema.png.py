#!/usr/bin/env python3
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph
import time
from anormbookmarker.Config import CONFIG
import sys

try:
    CONFIG.dbpath = sys.argv[1]
except:
    pass

# create the pydot graph object by autoloading all tables via a bound metadata object
#graph = create_schema_graph(metadata=MetaData('postgres://postgres:@localhost/sa_orm_import_test'),
graph = create_schema_graph(metadata=MetaData(CONFIG.dbpath),
   show_datatypes=False, # The image would get nasty big if we'd show the datatypes
   show_indexes=False, # ditto for indexes
   rankdir='TB', # From left to right (instead of top to bottom) LR TB
   concentrate=False # Don't try to join the relation lines together
)
graph.write_png('dbschema.' + str(time.time()) + '.png') # write out the file
