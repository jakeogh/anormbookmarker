#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

import os
import decimal
from sqlalchemy import Numeric
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import CheckConstraint
from sqlalchemy.types import DateTime
from .BaseMixin import BASE

# might want a to add a Date type http://www.postgresql.org/docs/9.4/static/datatype-datetime.html
class Timestamp(BASE):
    # 1431237850.2934275 (os.stat().st_mtime)
    # query returns a padded result
    # 1396732434.7183542000000000000000
    # timestamps should be unique

    id = Column(Integer, primary_key=True)
    #timestamp = Column(Numeric(32,22), CheckConstraint('timestamp>0'), unique=True, nullable=False, index=True)
    timestamp = Column(DateTime(timezone=True), unique=True, nullable=False, index=True, default=datetime.datetime.utcnow)

    #def __init__(self, timestamp=None):  # todo disable passing of timestamp after oldschool import is done
    #    if timestamp:
    #        self.timestamp = decimal.Decimal(format(decimal.Decimal(str(timestamp)), '0.22f'))

    def __repr__(self):
        return str(self.timestamp)

