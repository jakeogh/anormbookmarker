#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

# make tag
eucalyptus_deglupta = Tag.construct(session=SESSION, tag='Eucalyptus deglupta')
SESSION.commit()

# make a tag to use in a conflicting alias for 'Eucalyptus deglupta'
trees = Tag.construct(session=SESSION, tag='trees')
SESSION.commit()

# make conflicting Alias
try:
    alias = Alias.construct(session=SESSION, tag=trees, alias='Eucalyptus deglupta')
except ConflictingAliasError:
    print("Correctly throws ConflictingAliasError")
SESSION.commit()

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
