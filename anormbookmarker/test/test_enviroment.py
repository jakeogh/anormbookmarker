#!/usr/bin/env python3

from kcl.sqlalchemy.model.Filename import Filename
from anormbookmarker.model.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.model.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.model.Alias import Alias
from anormbookmarker.model.Word import WordMisSpelling
from anormbookmarker.model.Word import Word
from anormbookmarker.model.exceptions import ConflictingAliasError
from anormbookmarker.model.exceptions import ConflictingWordMisSpellingError

from sqlalchemy_utils.functions import create_database
from anormbookmarker.model.Config import CONFIG
CONFIG.database = CONFIG.database_timestamp
create_database(CONFIG.database)

from kcl.sqlalchemy.base_test_enviroment import *
