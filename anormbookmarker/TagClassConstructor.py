#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

'''
Implements Tags (unicode sentences) which are used by class Bookmark.

Tags are a sequence of Words separated by 0 or more (0x20) spaces.
Tags can have any number of parent and/or child Tags.
Tag examples:
    "plants"
    "trees"
    "Eucalyptus deglupta"
    "867-5309"
    "☃ Snowman!"

Tags are composed of 1 or more ordered Words.
All Words for the Tag list above:
    "plants"
    "trees"
    "Eucalyptus"
    "deglupta"
    "867-5309"
    "☃"
    "Snowman!"

Words are unique.
Words do not have parents or children.
Words do have misspellings (class WordMisSpelling) that alias to the correctly spelled word.

Tags are composed of Words in a specific order, that order is defined by class TagWord
Each TagWord instance maps a Word to a position.
So, actually, Tag.words is a list of TagWord instances, not Word instances.

TODO: Add aliases for Tag's (so "rainbow eucalyptus" is an alias for "Eucalyptus deglupta").
'''

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.hybrid import hybrid_property
from .BaseMixin import BASE
from .Word import Word
from .TagWord import TagWord
from .find_tag import find_tag
from .find_alias import find_alias
from .tag_relationship import tag_relationship

class TagClassConstructor():
    def __new__(cls, mapper_to_bookmark):
        future_class_attr = {}
        future_class_attr['id'] = Column(Integer, primary_key=True)
        future_class_attr['words'] = relationship("TagWord", backref='tag') # list of TagWord instances

        future_class_attr['parents'] = relationship('Tag',
                                                secondary=tag_relationship,
                                                primaryjoin=tag_relationship.c.tag_id == future_class_attr['id'],
                                                secondaryjoin=tag_relationship.c.tag_parent_id == future_class_attr['id'],
                                                backref="children")
        target_class_name = mapper_to_bookmark.__name__
        target_name =  target_class_name.lower() # 'filename' usually

        future_class_attr['target_class_name'] = target_class_name
        future_class_attr['target_name'] = target_name

        future_class_attr['construct'] = tag_construct
        future_class_attr['__repr__'] = tag_repr
        future_class_attr['__init__'] = tag_init
        future_class_attr['tag'] = tag_property
        future_class_attr[target_name+'s'] = tag_targets
        return type('Tag', (BASE,), future_class_attr)


def tag_init(self, session, tag):
    assert isinstance(tag, str)
    assert not find_tag(session=session, tag=tag)
    #assert not find_alias(session=session, alias=tag) #todo

    for index, word in enumerate(tag.split(' ')):
        previous_position = index - 1
        if previous_position == -1:
            previous_position = None
        tagword = TagWord(position=index,
                          previous_position=previous_position)
        tagword.word = Word.construct(session=session, word=word)
        self.words.append(tagword)

    session.add(self)
    session.flush(objects=[self])


@classmethod
def tag_construct(cls, session, tag, **kwargs):
    '''
    prevents creation of duplicate tags
    prevents creation of a tag that conflicts with an existing alias
    '''
    assert tag
    existing_alias = find_alias(session=session, alias=tag)
    if existing_alias:
        return existing_alias.tag

    existing_tag = find_tag(session=session, tag=tag)
    if existing_tag:
        return existing_tag
    else:
        new_tag = cls(tag=tag, session=session)
        return new_tag


def tag_repr(self):
    return str(self.tag)


@property
def tag_property(self): # appears to always return the same result as tag_with_checks()
    tag = " ".join([str(word.word) for word in self.words])
    return tag


@hybrid_property
def tag_targets(self):
    target_list = []
    for bookmark in self.bookmarks:
        target = getattr(bookmark, self.target_name)
        target_list.append(target)
    return set(target_list)


## not sure if sorting is necessary
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
