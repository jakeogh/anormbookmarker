#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from kcl.sqlalchemy.BaseMixin import BASE
from kcl.printops import ceprint

class AliasWord(BASE):
    '''
    AliasWords are to Aliases as TagWords are to Tags
    Aliases are like Tags, but instead an Alias points to a Tag

    Alias instances are composed of one or more AliasWord instances.
    Aliases with spaces are composed of a list of AliasWord instances.
    Each AliasWord maps a Word to a position and a specific Alias.
    position is always 0 unless the Alias is composed of multiple AliasWord instances
    The Slide/Bullett example:
        http://docs.sqlalchemy.org/en/latest/orm/extensions/orderinglist.html
        seems to confirm that AliasWords are necessary because in this instance
        many Slides(Tags) can have the same Bullet(Word), and in the example
        a Bullet can only exist on one Slide.

    The aliasword table has a row count:
    of (4 col) that are parsed by the ORM to reconstruct each Alias  __repr__.
    * row_count = count of every word in every alias including duplicates
    * row_count = aliass + spaces
    Does not appear to be a big deal because it's not exp and most aliass have 0 spaces

    '''
    __table_args__ = (UniqueConstraint('alias_id', 'word_id', 'position', 'previous_position'),)
    alias_id = Column(Integer,
                    ForeignKey("alias.id"),
                    unique=False,
                    primary_key=True)
    word_id = Column(Integer,
                     ForeignKey("word.id"),
                     unique=False,
                     primary_key=True)
    # Must be signed int because -1 has special meaning
    position_constraint = 'position<100' #limit words/alias to 100 # bug: why 100?
    position = Column(Integer,
                      CheckConstraint(position_constraint),
                      unique=False,
                      primary_key=True)
    previous_position_constraint = \
        '(previous_position IS NULL AND position = 0) ' + \
        'OR ((previous_position = position - 1) IS TRUE)'

    # primary_key=False because it can be Null
    previous_position = Column(Integer,
                               CheckConstraint(previous_position_constraint),
                               primary_key=False,
                               nullable=True)
    # collection_class=set?
    word = relationship("Word", backref='aliaswords')
    def __repr__(self):
        return 'AliasWord<' + \
            'word: ' + str(self.word) + \
            ', alias_id: ' + str(self.alias_id) + \
            ', word_id: ' + str(self.word_id) + \
            ', position: ' + str(self.position) + '>'

