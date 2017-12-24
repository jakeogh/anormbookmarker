#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    # make tag
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()

    # make a tag to use in a conflicting alias for 'Eucalyptus deglupta'
    trees = Tag.construct(session=session, tag='trees')
    session.commit()

    # make conflicting Alias
    try:
        alias = Alias.construct(session=session, tag=trees, alias='Eucalyptus deglupta')
    except ConflictingAliasError:
        print("Correctly throws ConflictingAliasError")
    session.commit()

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 3),
             ('select COUNT(*) from word;', 3),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
