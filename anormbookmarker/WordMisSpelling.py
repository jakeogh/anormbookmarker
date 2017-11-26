#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

'''
Tags are composed of 1 or more ordered Words.

Words are unique.
Words do not contain 0x20.
Words do not have parents or children.
Words do have misspellings (class WordMisSpelling) that alias to the correctly spelled word.

Tags are composed of Words in a specific order, that order is defined by class TagWord
Each TagWord instance maps a Word to a position.
So, actually, Tag.words is a list of TagWord instances, not Word instances.
'''

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.hybrid import hybrid_property
from kcl.sqlalchemy.get_one_or_create import get_one_or_create
from kcl.sqlalchemy.BaseMixin import BASE
from .Config import CONFIG

class Word(BASE):
    '''
    Words are grouped in a specific order by a list TagWord instances
    1 or more TagWord instances make up a Tag
    before a Word is created we must make sure it's not already a WordMisSpelling
    the only restrictions on words is they can not contain SPACE
    '''
    id = Column(Integer, primary_key=True)

    word_constraint = "position('\\x20' in word) = 0" # words can not contain SPACE #todo: add test
    word = Column(Unicode(CONFIG.word_max_length),
                  CheckConstraint(word_constraint),
                  unique=True,
                  nullable=False,
                  index=True)

    @classmethod
    def construct(cls, session, word):
        #print("Word.construct() word:", word)
        try:
            wordmisspelling = \
                session.query(WordMisSpelling).filter_by(wordmisspelling=word).one()
            result = get_one_or_create(session, Word, word=wordmisspelling.word)
        except NoResultFound:
            result = get_one_or_create(session, Word, word=word)
        #print("returning result:", result)
        return result

    @hybrid_property
    def tags(self):
        tags = []
        for tag in self.tagwords:
            tags.append(tag)
        return set(tags)

    @hybrid_property
    def bookmarks(self):
        bookmarks = []
        for tagword in self.tagwords:
            for bookmark in tagword.tag.bookmarks:
                bookmarks.append(bookmark)
        return set(bookmarks)

    def __repr__(self):
        return str(self.word)

    def __len__(self):
        return len(str(self.word))


class WordMisSpelling(BASE):
    '''
    alias of a word, intended to be used for misspellings
    '''
    id = Column(Integer, primary_key=True)
    wordmisspelling = Column(Unicode(CONFIG.word_max_length),
                             unique=True,
                             nullable=False,
                             index=True)
    # many WordMisSpelling can have the same word
    word_id = Column(Integer,
                     ForeignKey('word.id'),
                     unique=False,
                     nullable=False)
    word = relationship('Word', backref='wordmisspellings')

    @classmethod
    def construct(cls, session, wordmisspelling, word):
        #print("constructing WordMisSpelling")
        try:
            word = session.query(Word).filter_by(word=word).one()
        except NoResultFound:
            print("cant add WordMisSpelling:", wordmisspelling,
                   "the target word:", word, "does not exist.")
            return False # should be raising exception
        try:
            existing_word = session.query(Word).filter_by(word=wordmisspelling).one()
            print("cant add WordMisSpelling:", wordmisspelling,
                   "identical Word exists:", existing_word)
            return False # should be raising exception
        except NoResultFound:
            pass
        result = get_one_or_create(session,
                                   WordMisSpelling,
                                   wordmisspelling=wordmisspelling,
                                   word=word)
        return result

    def __repr__(self):
        return str(self.wordmisspelling)
