#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License
'''
    Config class
'''
import time

class Config():
    '''Simple configuration class.'''
    def __init__(self):
        self.word_max_length = 255
        self.tag_max_length = 255
        self.dbname = 'bookmark_test_' + str(time.time()).replace('.', '_')
        self.dbpath = 'postgres://postgres@localhost/' + self.dbname
        self.pg_dbpath = 'postgresql://postgres@localhost/postgres'

CONFIG = Config()

