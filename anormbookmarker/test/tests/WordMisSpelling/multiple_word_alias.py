#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    # make a tag to make an alias to
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()

    # make a tag to use in a conflicting alias for rainbow eucalyptus
    #trees = Tag.construct(session=session, tag='trees')
    #session.commit()

    # make a Alias
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()

    # make a wordmisspelling for rainbow
    rainbow_wms = WordMisSpelling.construct(session=session, wordmisspelling="rrainbow", word="rainbow")

    # make a Alias with misspelled rrainbow
    alias_rrainbow = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rrainbow eucalyptus')
    session.commit()

    assert id(alias) == id(alias_rrainbow)
    assert str(alias_rrainbow.tag) == 'Eucalyptus deglupta'

    #try:
    #    # make a duplicate (conflicting) Alias to a different tag (correctly throws ConflictingAliasError)
    #    alias = Alias.construct(session=session, tag=trees, alias='rainbow eucalyptus')
    #except ConflictingAliasError:
    #    print("Correctly throws ConflictingAliasError")
    #session.commit()


db_result = [('select COUNT(*) from alias;', 1),
             ('select COUNT(*) from aliasword;', 2),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 2),
             ('select COUNT(*) from word;', 4),
             ('select COUNT(*) from wordmisspelling;', 1)]

check_db_result(config=CONFIG, db_result=db_result)
