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
'''

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from kcl.sqlalchemy.BaseMixin import BASE
from .Word import Word
from .TagWord import TagWord
from .find_tag import find_tag
from .find_alias import find_alias
from .tag_relationship import tag_relationship

class TagClassConstructor():
    def __new__(cls, mapper_to_bookmark):
        class_attr = {}
        class_attr['id'] = Column(Integer, primary_key=True)
        class_attr['tagwords'] = relationship("TagWord", backref='tag') # list of TagWord instances
        class_attr['parents'] = relationship('Tag',
                                             secondary=tag_relationship,
                                             primaryjoin=tag_relationship.c.tag_id == class_attr['id'],
                                             secondaryjoin=tag_relationship.c.tag_parent_id == class_attr['id'],
                                             backref="children")
        target_class_name = mapper_to_bookmark.__name__
        target_name = target_class_name.lower().split('.')[-1] # 'filename' usually

        class_attr['target_class_name'] = target_class_name
        class_attr['target_name'] = target_name

        class_attr['__init__'] = init
        class_attr['__repr__'] = display
        class_attr['construct'] = construct         # @classmethod
        class_attr['tag'] = build_tag               # @property
        class_attr[target_name+'s'] = tag_targets   # @hybrid_property
        class_attr['words'] = words                 # @hybrid_property
        return type('Tag', (BASE,), class_attr)


def init(self, session, tag):
    assert isinstance(tag, str)
    assert not find_tag(session=session, tag=tag) # because get_one_or_create should have already found it
    #assert not find_alias(session=session, alias=tag) #todo
    for index, word in enumerate(tag.split(' ')):
        previous_position = index - 1
        if previous_position == -1:
            previous_position = None
        tagword = TagWord(position=index, previous_position=previous_position)
        tagword.word = Word.construct(session=session, word=word)
        self.tagwords.append(tagword)
    session.add(self)
    session.flush(objects=[self])

def display(self):
    return str(self.tag)

@classmethod
def construct(cls, session, tag, **kwargs):
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
    new_tag = cls(tag=tag, session=session)
    return new_tag

@property
def build_tag(self): # appears to always return the same result as tag_with_checks()
    tag = " ".join([str(word) for word in self.words])
    return tag

@hybrid_property
def tag_targets(self):
    target_list = []
    for bookmark in self.bookmarks:
        target = getattr(bookmark, self.target_name)
        target_list.append(target)
    return set(target_list)

@hybrid_property
def words(self):
    word_list = []
    for tagword in self.tagwords:
        #tag_word = getattr(word, self.tagword)
        word_list.append(tagword.word)
    return word_list # cant be a set because "a a" -> "a"

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
