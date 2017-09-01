#!/usr/bin/env python3

from anormbookmarker.test.functions import *

# make a tag to make an alias to
eucalyptus_deglupta = Tag.construct(session=SESSION, tag='Eucalyptus deglupta')
SESSION.commit()

# make a Alias
alias = Alias.construct(session=SESSION, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
SESSION.commit()

# make a duplicate Alias
duplicate_alias = Alias.construct(session=SESSION, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
SESSION.commit()

assert id(alias) == id(duplicate_alias)

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
