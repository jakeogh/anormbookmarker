#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

from anormbookmarker.TagClassConstructor import TagClassConstructor
from Filename import Filename
Tag = TagClassConstructor(mapper_to_bookmark=Filename)
from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)
from anormbookmarker.Alias import Alias
from anormbookmarker.Word import Word
from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Config import Config
from db_utils import create_database_and_tables
from db_utils import create_session
from db_utils import get_engine
from print_database import print_database

from kcl.printops import cprint
from kcl.dirops import all_files
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)



def check_db_result(db_result)
    ENGINE = get_engine(config)
    for db_test in db_result:
        print("db_test:", db_test)
        with ENGINE.connect() as connection:
            answer = connection.execute(db_test[0])
            for row in answer:
                try:
                    assert row[0] == db_test[1]
                except AssertionError as e:
                    print("\nAssertionError on db test:", db_test[0])
                    print("row[0] != db_test[0]:\n", row[0], "!=", db_test[1])
                    raise e
    session.close()
    ENGINE.dispose()





