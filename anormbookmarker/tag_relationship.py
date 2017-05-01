#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from .BaseMixin import BASE

tag_relationship = Table(
    'tag_relationship', BASE.metadata,
    Column('tag_parent_id', Integer, ForeignKey('tag.id')),
    Column('tag_id', Integer, ForeignKey('tag.id')))


