#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)


from anormbookmarker.test.Filename import Filename
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
from kcl.postgresqlops import drop_database
from anormbookmarker.find_alias import ConflictingAliasError
from anormbookmarker.BaseMixin import BASE

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)

create_database_and_tables(dbname=CONFIG.dbname, schema=BASE)
SESSION = create_session(dbname=CONFIG.dbname, multithread=False)

def check_db_result(config, db_result):
    ENGINE = get_engine(dbpath=config.dbpath)
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
    #drop_database(dbname=config.dbname)

