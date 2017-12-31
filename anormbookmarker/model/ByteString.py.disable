#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Generic 'group of bytes' type to collect all strings (bytes, unicode whatever) into a easy to search index
'''
from anormbookmarker.model.Config import CONFIG
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence
from kcl.hashops import bytes_dict_bytes
from kcl.sqlalchemy.get_one_or_create import get_one_or_create
from kcl.sqlalchemy.BaseMixin import BASE
from kcl.sqlalchemy.model.BytesHash import BytesHash

# some iri's (and uri's) are too long to have a unique constraint so using unique=True on hash instead
class ByteString(BASE):
    # store all iri's, uri's together - 99% of iri's will match the uri
    id = Column(Integer, Sequence('id_seq', start=0, minvalue=0), autoincrement=True, primary_key=True, index=True)
    # IRI_MAX_LENGTH is too long to unique or index
    byte_string = Column(Unicode(CONFIG.iri_max_length), unique=False, nullable=False, index=False)
    hash_id = Column(Integer, ForeignKey('hash.id'), unique=True, nullable=False, index=True)
    hash = relationship('BytesHash', backref='byte_string')

    @classmethod
    def construct(cls, session, byte_string):
        assert isinstance(byte_string, str) #BUG
        # byte strings come in unicode, UTF8 is the chosen byte encoding #bug
        # bug: tags should allow all bytes, not just valid UTF8.
        # todo: add test for bytes tag
        # todo: feed the tag system with angryfiles
        hash_dict = bytes_dict_bytes(byte_string)
        hash = get_one_or_create(session, BytesHash, **hash_dict)
        result = get_one_or_create(session, ByteString, byte_string=byte_string, hash=hash)
        assert isinstance(result, ByteString)
        return result

    def __repr__(self):
        return str(self.byte_string)


