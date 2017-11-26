#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)


#from anormbookmarker.test.Filename import Filename
from kcl.sqlalchemy.Filename import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.Alias import Alias
from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Word import Word
from anormbookmarker.Config import CONFIG
from kcl.postgresqlops import get_engine
from kcl.postgresqlops import create_database_and_tables
from kcl.postgresqlops import create_session
from kcl.postgresqlops import delete_database
from anormbookmarker.find_alias import ConflictingAliasError
from kcl.sqlalchemy.BaseMixin import BASE

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)

create_database_and_tables(database=CONFIG.database, schema=BASE)
SESSION = create_session(database=CONFIG.database, multithread=False)

from kcl.sqlalchemy.check_db_result import check_db_result
