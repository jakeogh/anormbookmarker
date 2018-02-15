#!/usr/bin/env python3

from kcl.sqlalchemy.model.Filename import Filename
from anormbookmarker.model.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)
