#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License
'''
    Config class
'''
from kcl.sqlalchemy.model.BaseConfig import BaseConfig

class Config(BaseConfig):
    '''Simple configuration class.'''
    def __init__(self):
        BaseConfig.__init__(self)
        self.word_max_length = 255
        self.tag_max_length = 255

CONFIG = Config()
