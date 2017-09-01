#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

'''Base class to automatically name tables.'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

class BaseMixin(object):
    '''Base Mixin class to automate table naming.'''
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower().split('.')[-1]
    @classmethod
    def query(cls, session):
        return session.query_property()

BASE = declarative_base(cls=BaseMixin)
