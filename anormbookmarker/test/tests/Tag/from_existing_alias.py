#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.timestamp_database) as session:
    BASE.metadata.create_all(session.bind)

    # make a tag to make an alias to
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()
    eprint(eucalyptus_deglupta)

    # make a Alias
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()
    eprint(alias)

    # create a tag that conflicts with an existing alias
    # returns existing alias target

    rainbow_eucalyptus = Tag.construct(session=session, tag='rainbow eucalyptus')
    session.commit()
    eprint(rainbow_eucalyptus)

    assert rainbow_eucalyptus == eucalyptus_deglupta

db_result = [('select COUNT(*) from alias;', 1),
             ('select COUNT(*) from aliasword;', 2),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 2),
             ('select COUNT(*) from word;', 4),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
