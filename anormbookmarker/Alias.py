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


    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)


