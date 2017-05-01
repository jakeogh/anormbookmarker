#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License
'''
Example Filename class that is being Bookmarked
The goal is to be able to apply the Bookmark class to any ORM table, not just
the Filename example.
'''

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy import LargeBinary # bytea on postgresql
from get_one_or_create import get_one_or_create
from BaseMixin import BASE


class Filename(BASE):
    '''
    UNIX filenames can be anything but NULL and / therefore a binary type is required.
    max file name length is 255 on all UNIX-like filesystems
    this stores paths to the name as well, so / is allowed
    a Bookmark can only have 1 Filename
    a Filename can have many Bookmarks
    '''
    id = Column(Integer, primary_key=True)

    #filename_constraint = "position('\\x00' in filename) = 0 and position('\\x2f' in filename) = 0"
    #filename_constraint = "position('\\x00' in filename) = 0"
    filename = Column(LargeBinary(255), unique=True, nullable=False, index=True)

    @classmethod
    def construct(cls, session, filename):
        #print("Filename.construct()")
        result = get_one_or_create(session, Filename, filename=filename)
        return result

    def __repr__(self):
        return str(self.filename)    #todo: going to fail if it's outside Unicode
