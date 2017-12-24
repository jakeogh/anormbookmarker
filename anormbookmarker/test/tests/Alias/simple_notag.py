#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    # make a tag to make an alias to
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()

    # make a Alias
    #alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus', casesensitive=False)
    #import pdb; pdb.set_trace()
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    #alias = Alias.construct(session=session, alias='rainbow eucalyptus')

    session.commit()

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
