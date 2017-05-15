#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

import os
import decimal
#import datetime
from sqlalchemy import Numeric
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import CheckConstraint
from sqlalchemy.types import DateTime
from .BaseMixin import BASE
from sqlalchemy.sql import func


# might want a to add a Date type http://www.postgresql.org/docs/9.4/static/datatype-datetime.html
class Timestamp(BASE):

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), unique=True, nullable=False, index=True, server_default=func.now())


    @classmethod
    def construct(cls, session):
        result = get_one_or_create(session, Timestamp)
        #print("returning result:", result)
        return result

    def __repr__(self):
        return str(self.timestamp)
