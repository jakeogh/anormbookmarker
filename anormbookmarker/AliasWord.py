#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from .BaseMixin import BASE


class AliasWord(BASE):
    '''
    Tag instances are composed of a list of AliasWord instances.
    Tags with spaces are composed of multiple AliasWord instances.
    Each AliasWord maps a Word to a position and a specific Tag.
    position is always 0 unless the alias is composed of multiple AliasWord instances
    The Slide/Bullett example:
        http://docs.sqlalchemy.org/en/latest/orm/extensions/orderinglist.html
        seems to confirm that AliasWords are necessary because in this instance
        many Slides(Tags) can have the same Bullet(Word), and in the example
        a Bullet can only exist on one Slide.

    The aliasword table has a row count:
    of (4 col) that are parsed by the ORM to reconstruct each Tag's __repr__.
    * row_count = count of every word in every alias including duplicates
    * row_count = aliass + spaces
    Does not appear to be a big deal because it's not exp and most aliass have 0 spaces

    aliasword:
    alias_id, word_id, position, previous_position,
    [(1, 11, 0, None), (1, 12, 1, 0),
     (2, 11, 0, None), (2, 12, 1, 0)]


    '''

    #prevent creation of duplicate AliasWords, note adding alias_id breaks it
    __table_args__ = (UniqueConstraint('word_id', 'position', 'previous_position'),)
    alias_id = Column(Integer,
                    ForeignKey("alias.id"),
                    unique=False,
                    primary_key=True)
    word_id = Column(Integer,
                     ForeignKey("word.id"),
                     unique=False,
                     primary_key=True)
    # These must be a signed int's because -1 has special meaning
    position_constraint = 'position<100' #limit words/alias to 100
    position = Column(Integer,
                      CheckConstraint(position_constraint),
                      unique=False,
                      primary_key=True)
    previous_position_constraint = \
        '(previous_position IS NULL AND position = 0) ' + \
        'OR ((previous_position = position - 1) IS TRUE)'
    previous_position = Column(Integer,
                               CheckConstraint(previous_position_constraint),
                               primary_key=False,
                               nullable=True)
    # collection_class=set?
    word = relationship("Word", backref='alias_words')
    def __repr__(self):
        return 'AliasWord<' + \
            'word: ' + str(self.word) + \
            ', alias_id: ' + str(self.alias_id) + \
            ', word_id: ' + str(self.word_id) + \
            ', alias_id: ' + str(self.alias_id) + \
            ', position: ' + str(self.position) + '>'


