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


class TagWord(BASE):
    '''
    Tag instances are composed of a list of TagWord instances.
    Tags with spaces are composed of multiple TagWord instances.
    Each TagWord maps a Word to a position and a specific Tag.
    position is always 0 unless the tag is composed of multiple TagWord instances
    The Slide/Bullett example:
        http://docs.sqlalchemy.org/en/latest/orm/extensions/orderinglist.html
        seems to confirm that TagWords are necessary because in this instance
        many Slides(Tags) can have the same Bullet(Word), and in the example
        a Bullet can only exist on one Slide.

    The tagword table has a row count:
    of (4 col) that are parsed by the ORM to reconstruct each Tag's __repr__.
    * row_count = count of every word in every tag including duplicates
    * row_count = tags + spaces
    Does not appear to be a big deal because it's not exp and most tags have 0 spaces

    '''
    __table_args__ = (UniqueConstraint('word_id', 'tag_id', 'alias_id', 'position'),)
    tag_id = Column(Integer,
                    ForeignKey("tag.id"),
                    unique=False,
                    primary_key=True,
                    nullable=False)
    alias_id = Column(Integer,
                      ForeignKey("tag.id"),
                      unique=False,
                      primary_key=True,
                      nullable=False)
    word_id = Column(Integer,
                     ForeignKey("word.id"),
                     unique=False,
                     primary_key=True,
                     nullable=False)
    # These must be a signed int's because -1 has special meaning
    position_constraint = 'position<100' #limit words/tag to 100
    position = Column(Integer,
                      CheckConstraint(position_constraint),
                      unique=False,
                      primary_key=True,
                      nullable=False)
    previous_position_constraint = \
        '(previous_position IS NULL AND position = 0) ' + \
        'OR ((previous_position = position - 1) IS TRUE)'
    previous_position = Column(Integer,
                               CheckConstraint(previous_position_constraint),
                               primary_key=False,
                               nullable=True)
    # collection_class=set?
    word = relationship("Word", backref='tag_words')
    def __repr__(self):
        return 'TagWord<' + \
            'word: ' + str(self.word) + \
            ', tag_id: ' + str(self.tag_id) + \
            ', word_id: ' + str(self.word_id) + \
            ', position: ' + str(self.position) + '>'


