#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License
'''
    general Timestamp class
'''

import decimal
from sqlalchemy import Column
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy import Numeric
from kcl.sqlalchemy.BaseMixin import BASE
i
class Timestamp(BASE):
    '''
    todo: use Date type:
        http://www.postgresql.org/docs/9.4/static/datatype-datetime.html
    '''
    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                index=True)

    timestamp = Column(Numeric(32, 22),
                       CheckConstraint('timestamp>0'),
                       unique=True,
                       nullable=False,
                       index=True)

    def __init__(self, timestamp):
        self.timestamp = decimal.Decimal(format(decimal.Decimal(str(timestamp)), '0.22f'))

    def __repr__(self):
        return str(self.timestamp)
