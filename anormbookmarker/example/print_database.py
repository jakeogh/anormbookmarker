#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

import pprint
from sqlalchemy import inspect as sqlalchemy_inspect

def print_database(session):
    inspector = sqlalchemy_inspect(session.bind)
    for table_name in sorted(inspector.get_table_names()):
        print('\n' + table_name + ':')
        columns = inspector.get_columns(table_name)
        for column in columns:
            print("%s, " % column['name'], end='')
        print('\n', end='')
        select_statement = "select * from " + table_name + ";"
        pprint.pprint(session.execute(select_statement).fetchall())


