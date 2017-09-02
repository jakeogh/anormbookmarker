#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

# make a tag to make an alias to
eucalyptus_deglupta = Tag.construct(session=SESSION, tag='Eucalyptus deglupta')
SESSION.commit()

# make a tag to use in a conflicting alias for rainbow eucalyptus
trees = Tag.construct(session=SESSION, tag='trees')
SESSION.commit()

# make a Alias
alias = Alias.construct(session=SESSION, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
SESSION.commit()

try:
    # make a duplicate (conflicting) Alias to a different tag (correctly throws ConflictingAliasError)
    alias = Alias.construct(session=SESSION, tag=trees, alias='rainbow eucalyptus')
except ConflictingAliasError:
    print("Correctly throws ConflictingAliasError")

SESSION.commit()

db_result = [('select COUNT(*) from alias;', 1),
             ('select COUNT(*) from aliasword;', 2),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 3),
             ('select COUNT(*) from word;', 5),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result, session=SESSION)
