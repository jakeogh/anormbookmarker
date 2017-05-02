#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
from sqlalchemy import ForeignKey
#from sqlalchemy import UniqueConstraint
#from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
#from sqlalchemy import Unicode
from sqlalchemy.orm import relationship
#from sqlalchemy.orm import backref
#from sqlalchemy.orm.exc import NoResultFound
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.ext.declarative import declared_attr
#from sqlalchemy.ext.associationproxy import association_proxy
#from sqlalchemy.ext.hybrid import hybrid_property
#from get_one_or_create import get_one_or_create
from .Config import CONFIG
from .Word import Word
#from Word import WordMisSpelling
#from tag_relationship import tag_relationship
from .AliasWord import AliasWord
from .find_tag import find_tag
from .BaseMixin import BASE

class Alias(BASE):
    '''
    List of AliasWord instances that point to a Tag

    '''
    id = Column(Integer, primary_key=True)

    words = relationship("AliasWord", backref='alias') # a list of AliasWord instances

    tag_id = Column(Integer, ForeignKey("tag.id"), unique=False, nullable=False)
    tag = relationship('Tag', backref='aliases')

    def __init__(self, session, alias, tag):
        print("Alias.__init__() alias:", alias)
        assert isinstance(alias, str)
        assert not find_tag(session=session, tag=alias)

        for index, word in enumerate(alias.split(' ')):
            previous_position = index - 1
            if previous_position == -1:
                previous_position = None
            aliasword = AliasWord(position=index, previous_position=previous_position)
            aliasword.word = Word.construct(session=session, word=word)
            self.words.append(aliasword)
            self.tag = tag
            session.add(self)
            print("Alias.__init__ calling session.flush()")
            session.flush(objects=[self])
            print("Alias.__init__ done calling session.flush()")

    @classmethod
    def construct(cls, session, alias, tag):
        '''
        prevents creation of duplicate aliases or conflicting aliases and tags
        '''
        print("Alias.construct() alias:", alias)
        assert alias
        existing_tag = find_tag(session=session, tag=alias)
        if existing_tag: # this would be an existing tag that matches this alias
            print("Alias.construct() existing_tag:", existing_tag)
            quit(1)
            return False #todo
        else:
            new_alias = Alias(alias=alias, tag=tag, session=session)
            print("Alias.construct() new_alias:", new_alias)
            return new_alias

#    # not sure if sorting is necessary
#    @property
#    def tag_with_checks(self):
#        tagwords_objects = sorted([word for word in self.words], key=lambda x: x.position)
#        sorted_tag = " ".join([str(word.word) for word in tagwords_objects])
#
#        unsorted_tag = " ".join([word.word for word in self.words])
#        if sorted_tag != unsorted_tag:
#            print("TAGS DO NOT MATCH")
#            print("sorted_tag:", sorted_tag)
#            print("unsorted_tag:", unsorted_tag)
#            quit(1)
#        return unsorted_tag

    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)


