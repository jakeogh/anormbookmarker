#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

import time
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from anormbookmarker.BaseMixin import BASE
from anormbookmarker.Config import CONFIG


def create_database():
    '''Create new database.'''
    print("create_database() CONFIG.dbname:", CONFIG.dbname)
    print("create_database() CONFIG.dbpath:", CONFIG.dbpath)
    with create_engine(CONFIG.pg_dbpath, isolation_level='AUTOCOMMIT', echo=False).connect() as connection:
        connection.execute('CREATE DATABASE ' + CONFIG.dbname)

def create_tables(schema=BASE):
    '''Create tables.'''
    engine = create_engine(CONFIG.dbpath, echo=False)
    schema.metadata.create_all(engine)

def create_database_and_tables():
    '''Create new database and tables.'''
    create_database()
    create_tables(BASE)

def create_session():
    '''Create a session.'''
    engine = create_engine(CONFIG.dbpath, echo=False, poolclass=NullPool)
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=engine))
    return session


