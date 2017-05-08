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


def run_job(session, config, job, test_file):
    print('\n\n\ntest_file:', test_file)
    #print("run_job() job:", job['note'])
    assert isinstance(job, dict)
    assert isinstance(job['debug'], bool)
    assert isinstance(job['echo'], bool)
    if job['echo']:
        pp.pprint(job)

    jobs = job['inputs']
    assert isinstance(jobs, list)
    for test in jobs:
        print("test:", test)
        orm_object = test['orm_object']
        assert ' ' not in orm_object
        print("orm_object:", orm_object)
        orm_object_attr = orm_object.lower()
        orm_object = eval(orm_object)
        print("orm_object:", orm_object)
        orm_object_instance = orm_object.construct(session, tag=test[orm_object_attr], debug=job['debug'])
        print("orm_object_instance:", orm_object_instance)
        print("dir(orm_object_instance):", dir(orm_object_instance))
        attrs_to_check_dict = test['orm_result']
        #print('attrs_to_check_dict:', attrs_to_check_dict)
        for attr in attrs_to_check_dict.keys():
            print("\nattr:", attr)
            result = getattr(orm_object_instance, attr)
            print("result:", result)
            print("type(result):", type(result))
            expected_result = attrs_to_check_dict[attr]
            print("expected_result:", expected_result)
            print("type(expected_result):", type(expected_result))
            if expected_result: # it's not empty
                try:
                    assert result == expected_result
                except AssertionError as e:
                    print("\nAssertionError on attribute:", attr)
                    print("result != expected_result:\n", result, "!=", expected_result)
                    #from IPython import embed; embed()
                    raise e
            else: #it's empty, so compare the empty sets?
                try:
                    assert len(result) == 0
                except AssertionError as e:
                    print("\nAssertionError on attribute:", attr)
                    print("len(result) != 0:\n", len(result), "!= 0")
                    #from IPython import embed; embed()
                    raise e
                try:
                    assert set(result) == set(expected_result)
                except AssertionError as e:
                    print("\nAssertionError on attribute:", attr)
                    print("set(result) != set(expected_result):\n", set(result), "!=", set(expected_result))
                    #from IPython import embed; embed()
                    raise e

    session.commit()

    ENGINE = get_engine(config)
    for db_test in job['db_result']:
        #print("db_test:", db_test)
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



if __name__ == '__main__':

    for test_file in all_files('tests/'):
        with open(test_file, 'r') as fh:
            contents = fh.read()
            job = eval(contents)
            config = Config()
            print("config.dbpath:", config.dbpath)
            create_database_and_tables(config=config)
            SESSION = create_session(config=config)
            run_job(SESSION, config, job, test_file)


