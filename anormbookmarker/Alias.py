#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from .Config import CONFIG
from .Word import Word
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
        assert not find_tag(session=session, tag=alias) #dont create aliase that conflict with an existing tag

        self.tag = tag

        for index, word in enumerate(alias.split(' ')):
            previous_position = index - 1
            if previous_position == -1:
                previous_position = None
            aliasword = AliasWord(position=index, previous_position=previous_position)
            aliasword.word = Word.construct(session=session, word=word)
            self.words.append(aliasword)

        session.add(self)
        session.flush(objects=[self]) # any db error will happen here, like attempting to add a duplicate alias
        # maybe return the already existing alias if it's a duplicate or conflicting


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



    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)


