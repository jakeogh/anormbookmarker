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
from kcl.printops import ceprint
from .Exceptions import ConflictingAliasError

# todo:
# does it make sense to have Aliases composed of a single AliasWord?
# seems no, because that could just be a WordMisspelling instead

class Alias(BASE):
    '''
    List of AliasWord instances that together point to a Tag

    '''
    id = Column(Integer, primary_key=True)
    aliaswords = relationship("AliasWord", backref='alias') # a list of AliasWord instances
    tag_id = Column(Integer, ForeignKey("tag.id"), unique=False, nullable=False)
    tag = relationship('Tag', backref='aliases')

#    def __new__(self, session, alias, tag): # called when Alias() is first called, not when a @classmethod is called
#        assert isinstance(alias, str)
#        assert not isinstance(tag, str) # rather not import Tag


    def __init__(self, session, alias, tag):
        assert isinstance(alias, str)
        assert not isinstance(tag, str) # rather not import Tag
        assert not find_alias(session=session, alias=alias) # because get_one_or_create should have already found it
        try: # special case only for Alias?
            conflicting_tag = find_tag(session=session, tag=alias)
            assert not conflicting_tag #dont create aliase that conflict with an existing tag
        except AssertionError:
            error_msg = "alias: '%s' conflicts with existing tag: %s" % (alias, conflicting_tag)
            raise ConflictingAliasError(error_msg)

        self.tag = tag
        ceprint("constructing aliaswords for alias:", alias)
        for index, word in enumerate(alias.split(' ')):
            previous_position = index - 1
            if previous_position == -1:
                previous_position = None
            ceprint("AliasWord, alias_id:", self.id, "position:", index, "previous_position:", previous_position)
            aliasword = AliasWord(alias_id=self.id, position=index, previous_position=previous_position)
            aliasword.word = Word.construct(session=session, word=word) #todo should be get_one_or_create?
            self.aliaswords.append(aliasword)
        session.add(self)
        session.flush(objects=[self]) # any db error will happen here, like attempting to add a duplicate alias
        # maybe return the already existing alias if it's a duplicate or conflicting

    @classmethod
    def construct(cls, session, alias, tag):
        '''
        prevents creation of duplicate alias
        prevents creation of a alias that conflicts with an existing tag
        '''
        assert alias
        assert tag
        #existing_tag = find_tag(session=session, tag=alias) #todo?
        existing_alias = find_alias(session=session, alias=alias, tag=tag)
        if existing_alias:
            return existing_alias #todo check if it points to the same tag
        else:
            new_alias = Alias(alias=alias, tag=tag, session=session)
            assert new_alias
            return new_alias

    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)

