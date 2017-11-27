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
from .find_alias import find_alias
from kcl.sqlalchemy.BaseMixin import BASE
from .Exceptions import ConflictingAliasError

class Alias(BASE):
    '''
    List of AliasWord instances that point to a Tag

    '''
    id = Column(Integer, primary_key=True)

    words = relationship("AliasWord", backref='alias') # a list of AliasWord instances

    tag_id = Column(Integer, ForeignKey("tag.id"), unique=False, nullable=False)
    tag = relationship('Tag', backref='aliases')

    def __init__(self, session, alias, tag):
        assert isinstance(alias, str)
        try:
            conflicting_tag = find_tag(session=session, tag=alias)
            assert not conflicting_tag #dont create aliase that conflict with an existing tag
        except AssertionError:
            error_msg = "alias: '%s' conflicts with existing tag: %s" % (alias, conflicting_tag)
            raise ConflictingAliasError(error_msg)

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
        assert alias
        #existing_tag = find_tag(session=session, tag=alias)
        existing_alias = find_alias(session=session, alias=alias, tag=tag)
        if existing_alias:
            return existing_alias #todo check if it points to the same tag
        else:
            new_alias = Alias(alias=alias, tag=tag, session=session)
            return new_alias


    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)


