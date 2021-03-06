#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

'''
 A Bookmark attaches a set of Tags and a single Object ('class Filename' in the
 included example).
'''

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.associationproxy import association_proxy
from kcl.sqlalchemy.get_one_or_create import get_one_or_create
from kcl.sqlalchemy.BaseMixin import BASE

# Timestamps on bookmarks results in 'duplicate' bookmarks
# so dont put timestamps on bookmarks

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
    result = get_one_or_create(session, cls, **kwargs)
    result.tag_rel.add(tag)
    return result

def bookmark_repr(self):
    target_name = str(getattr(self, self.target_name))
    target_name_placeholder = getattr(self, self.target_name_placeholder)
    if target_name_placeholder:
        return target_name + '#' + str(target_name_placeholder) + ' ' + str(self.tags)
    return target_name + ' ' + str(self.tags)

class BookmarkClassConstructor(): #should be a func
    def __new__(cls, mapper_to_bookmark, mapper_to_bookmark_placeholder=False):
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

        if mapper_to_bookmark_placeholder:
            target_class_name_placeholder = mapper_to_bookmark_placeholder.__name__
            target_name_placeholder = target_class_name_placeholder.lower().split('.')[-1] # byteoffset in the filename case
            future_class_attr[target_name_placeholder+'_id'] = Column(Integer, ForeignKey(target_name_placeholder+'.id'), unique=False, nullable=True)
            future_class_attr[target_name_placeholder] = relationship(target_class_name_placeholder, backref='bookmarks')
            future_class_attr['target_class_name_placeholder'] = target_class_name_placeholder
            future_class_attr['target_name_placeholder'] = target_name_placeholder

        future_class_attr['construct'] = construct
        future_class_attr['__repr__'] = bookmark_repr
        return type('Bookmark', (BASE,), future_class_attr)





