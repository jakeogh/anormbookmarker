#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    ed = Word.construct(session=session, word='Eucalyptus')
    session.commit()

    ed_duplicate = Word.construct(session=session, word='Eucalyptus')
    session.commit()

    assert id(ed) == id(ed_duplicate)

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
