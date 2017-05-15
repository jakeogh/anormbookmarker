#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

'''
A Bookmark combines a set of Tags and a single Object ('class Filename' in the inclided example).
'''

import datetime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.associationproxy import association_proxy
from .get_one_or_create import get_one_or_create
from .BaseMixin import BASE
from .Timestamp import Timestamp

tagbookmarks_table = \
    Table('tagbookmarks', BASE.metadata,
          Column('bookmark_id',
                 Integer,
                 ForeignKey("bookmark.id"),
                 primary_key=True),
          Column('tag_id',
                 Integer,
                 ForeignKey("tag.id"),
                 primary_key=True),
          UniqueConstraint('bookmark_id', 'tag_id'))

@classmethod
def construct(cls, session, tag, **kwargs):
    #tag = Tag.construct(session=session, tag=tag) # could demand to get a tag obj...
    result = get_one_or_create(session, cls, **kwargs)
    result.tag_rel.add(tag)
    return result

def repr(self):
    return str(getattr(self, self.target_name)) + ' ' + str(self.tags)

class BookmarkClassConstructor():
    def __new__(cls, mapper_to_bookmark):
        future_class_attr = {}
        future_class_attr['id'] = Column(Integer, primary_key=True)
        future_class_attr['tag_rel'] = relationship("Tag",
                                                    secondary=lambda: tagbookmarks_table,
                                                    collection_class=set,
                                                    backref=backref('bookmarks'))
        future_class_attr['tags'] = association_proxy('tag_rel', 'tag')
        target_class_name = mapper_to_bookmark.__name__
        target_name = target_class_name.lower().split('.')[-1] # 'filename' usually

        future_class_attr[target_name+'_id'] = Column(Integer, ForeignKey(target_name+'.id'), unique=False, nullable=False)
        future_class_attr[target_name] = relationship(target_class_name, backref='bookmarks')
        future_class_attr['target_class_name'] = target_class_name
        future_class_attr['target_name'] = target_name

        future_class_attr['timestamp_id'] = \
            Column(Integer, ForeignKey('timestamp.id'), unique=False, nullable=False)
        future_class_attr['timestamp'] = relationship('Timestamp', backref='bookmarks')

        future_class_attr['construct'] = construct
        future_class_attr['__repr__'] = repr
        return type('Bookmark', (BASE,), future_class_attr)


