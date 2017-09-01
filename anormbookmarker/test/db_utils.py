#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

import time
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from anormbookmarker.BaseMixin import BASE

#def create_database(config):
#    '''Create new database.'''
#    print("create_database() config.dbname:", config.dbname)
#    print("create_database() config.dbpath:", config.dbpath)
#    with create_engine(config.pg_dbpath, isolation_level='AUTOCOMMIT', echo=False).connect() as connection:
#        connection.execute('CREATE DATABASE ' + config.dbname)

def get_engine(config):
    assert isinstance(config.dbpath, str)
    engine = create_engine(config.dbpath, echo=False)
    return engine

#def create_tables(config, schema=BASE):
#    '''Create tables.'''
#    engine = get_engine(config=config)
#    schema.metadata.create_all(engine)
#
#def create_database_and_tables(config):
#    '''Create new database and tables.'''
#    create_database(config=config)
#    create_tables(config, schema=BASE)

def create_session(config):
    '''Create a session.'''
    engine = create_engine(config.dbpath, echo=False, poolclass=NullPool)
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=engine))
    return session


