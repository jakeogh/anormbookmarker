#!/usr/bin/env python3

from sqlalchemy.exc import IntegrityError
from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.timestamp_database) as session:
    BASE.metadata.create_all(session.bind)

    # this should not get lost and is reflected in db_result below
    e = Word.construct(session=session, word='Eucalyptus')
    session.commit()

    try:
        ed = Word.construct(session=session, word='Eucalyptus deglupta')
    except IntegrityError:
        print("Correctly raises IntegrityError")
    session.commit()

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 0),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 0),
             ('select COUNT(*) from word;', 1),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
