#!/usr/bin/env python3

from anormbookmarker.example.db_utils import get_engine

def check_db_result(config, db_result):
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
    #session.close()
    ENGINE.dispose()





