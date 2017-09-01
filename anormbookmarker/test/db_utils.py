#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


def get_engine(config):
    assert isinstance(config.dbpath, str)
    engine = create_engine(config.dbpath, echo=False)
    return engine



