#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

from kcl.sqlalchemy.Filename import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.Alias import Alias
from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Word import Word
from anormbookmarker.Config import CONFIG
from sqlalchemy_utils.functions import create_database
from kcl.sqlalchemy.create_session import create_session
from kcl.sqlalchemy.delete_database import delete_database
from kcl.sqlalchemy.check_db_result import check_db_result
from anormbookmarker.find_alias import ConflictingAliasError
from kcl.sqlalchemy.BaseMixin import BASE
from kcl.sqlalchemy.self_contained_session import self_contained_session
from kcl.printops import eprint

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)

create_database(CONFIG.timestamp_database)
