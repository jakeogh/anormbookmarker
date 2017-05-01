#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License


from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import relation
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from .get_one_or_create import get_one_or_create
from .BaseMixin import BASE
from .Config import CONFIG
from .Word import Word
from .Word import WordMisSpelling
from .TagWord import TagWord


def find_tag(session, tag):
    '''
    iterates over the tagwords table to check for a existing tag
    returns if found, else returns False
    '''
    corrected_tag = tag
    possible_tag_set = set([])
    assert isinstance(tag, str)
    try:
        for index, word in enumerate(tag.split(' ')):
            try:
                wordmisspelling = session.query(WordMisSpelling).filter_by(wordmisspelling=tag).one()
                target_word = wordmisspelling.word
                word = str(target_word)
                corrected_tag = tag.replace(wordmisspelling.wordmisspelling, word)
            except NoResultFound:
                pass
            current_word = session.query(Word).filter_by(word=word).one()
            current_tagword_list = session.query(TagWord).filter_by(word=current_word, position=index).all()
            if current_tagword_list:
                current_tagword_list_tag_set = set([tagword.tag for tagword in current_tagword_list])
                possible_tag_set = possible_tag_set & current_tagword_list_tag_set
                for tagword in current_tagword_list:
                    if index == 0: # only add tags that start with the correct word
                        possible_tag_set.add(tagword.tag)
                    else:
                        if tagword.tag not in possible_tag_set:
                            return False
                if not possible_tag_set:
                    return False
                if len(possible_tag_set) == 1:
                    last_tag = list(possible_tag_set)[0]
                    last_tag_text = str(last_tag)
                    if last_tag_text == corrected_tag:
                        return last_tag
                    else:
                        return False
    except NoResultFound: # any failed query
        return False


