#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

from anormbookmarker.test.db_utils import get_engine

from anormbookmarker.test.Filename import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.Alias import Alias
from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Word import Word
from anormbookmarker.Timestamp import Timestamp
from anormbookmarker.Config import CONFIG
from anormbookmarker.test.db_utils import create_database_and_tables
from anormbookmarker.test.db_utils import create_session
from anormbookmarker.find_alias import ConflictingAliasError

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)

create_database_and_tables(config=CONFIG)
SESSION = create_session(config=CONFIG)

def check_db_result(config, db_result):
    ENGINE = get_engine(config)
    tables = set(ENGINE.table_names())
    print("tables:", tables)
    assert tables

    for db_test in db_result:
        print(db_test)
        db_test_table = db_test[0].split()[-1].split(';')[0]
        #print("db_test_table:", db_test_table)
        tables.remove(db_test_table)
        with ENGINE.connect() as connection:
            answer = connection.execute(db_test[0])
            for row in answer:
                try:
                    assert row[0] == db_test[1]
                except AssertionError as e:
                    print("\nAssertionError on db test:", db_test[0])
                    print("row[0] != db_test[0]:\n", row[0], "!=", db_test[1])
                    raise e
    if tables:
        print("Missed table test(s):", tables)
    assert not tables

    ENGINE.dispose()
