#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from kcl.sqlalchemy.BaseMixin import BASE
from kcl.printops import ceprint
from kcl.sqlalchemy.get_one_or_create import get_one_or_create
from .Word import Word
from .AliasWord import AliasWord
from .find_tag import find_tag
from .find_alias import find_alias
from .exceptions import ConflictingAliasError

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

    @classmethod
    def construct(cls, session, alias, tag):
        '''
        prevents creation of duplicate alias
        prevents creation of a alias that conflicts with an existing tag
        '''
        assert session
        assert alias
        assert isinstance(alias, str)
        assert tag
        assert not isinstance(tag, str) # rather not import Tag
        try: # special case only for Alias? or shpould tags also check for existing aliases?
            conflicting_tag = find_tag(session=session, tag=alias)
            assert not conflicting_tag #dont create aliase that conflict with an existing tag
        except AssertionError:
            error_msg = "alias: '%s' conflicts with existing tag: %s" % (alias, conflicting_tag)
            raise ConflictingAliasError(error_msg)
        existing_alias = find_alias(session=session, alias=alias)
        if existing_alias:
            return existing_alias #todo check if it points to the same tag
        else:
            new_alias = get_one_or_create(session, Alias, tag=tag)

        ceprint("constructing aliaswords for alias:", alias)
        for index, word in enumerate(alias.split(' ')):
            previous_position = index - 1
            if previous_position == -1:
                previous_position = None
            ceprint("AliasWord: word:", word, "position:", index, "previous_position:", previous_position)
            aliasword = AliasWord(position=index, previous_position=previous_position) #no construct()?
            aliasword.word = Word.construct(session=session, word=word)
            new_alias.aliaswords.append(aliasword)
        #session.add(self)
        #session.flush(objects=[self]) # any db error will happen here, like attempting to add a duplicate alias

        #existing_tag = find_tag(session=session, tag=alias) #todo?
        #existing_alias = find_alias(session=session, alias=alias, tag=tag)

        return new_alias

    @hybrid_property
    def words(self):
        word_list = []
        for aliasword in self.aliaswords:
            word_list.append(aliasword.word)
        return word_list # cant be a set because "a a" -> "a"

    @property
    def alias(self): # appears to always return the same result as tag_with_checks()
        alias = " ".join([str(word.word) for word in self.words])
        return alias

    def __repr__(self):
        return str(self.alias)
