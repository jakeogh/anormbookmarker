#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
#from sqlalchemy import ForeignKey
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
#from BaseMixin import BASE
from Config import CONFIG
from Word import Word
#from Word import WordMisSpelling
#from tag_relationship import tag_relationship
#from TagWord import TagWord
from find_tag import find_tag


class TagAlias(BASE):
    '''
    List of TagWord instances that point to a Tag

    '''
    id = Column(Integer, primary_key=True)

    words = relationship("TagWord", backref='tag') # a list of TagWord instances

    def __init__(self, session, tag):
        print("Tag.__init__() tag:", tag)
        assert isinstance(tag, str)
        assert not find_tag(session=session, tag=tag)

        for index, word in enumerate(tag.split(' ')):
            previous_position = index - 1
            if previous_position == -1:
                previous_position = None
            tagword = TagWord(position=index, previous_position=previous_position)
            tagword.word = Word.construct(session=session, word=word)
            self.words.append(tagword)
            session.add(self)
            session.flush(objects=[self])

    @classmethod
    def construct(cls, session, tag):
        '''
        prevents creation of duplicate tag aliases or conflicting tag aliases and tags
        '''
        #print("Tag.construct() tag:", tag)
        assert tag
        existing_tag = find_tag(session=session, tag=tag)
        if existing_tag:
            #print("Tag.construct() existing_tag:", existing_tag)
            return existing_tag
        else:
            new_tag = Tag(tag=tag, session=session)
            #print("Tag.construct() new_tag:", new_tag)
            return new_tag

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
    def tag(self): # appears to always return the same result as tag_with_checks()
        tag = " ".join([str(word.word) for word in self.words])
        return tag

    def __repr__(self):
        return str(self.tag)


