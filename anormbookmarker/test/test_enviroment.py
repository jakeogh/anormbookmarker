#!/usr/bin/env python3

from kcl.sqlalchemy.model.Filename import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.Alias import Alias
from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Word import Word
from anormbookmarker.find_alias import ConflictingAliasError

from sqlalchemy_utils.functions import create_database
from anormbookmarker.Config import CONFIG
CONFIG.database = CONFIG.database_timestamp
create_database(CONFIG.database)

from kcl.sqlalchemy.base_test_enviroment import *
