#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

buffalo = Tag.construct(session=SESSION, tag='Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo')
SESSION.commit()

buffalo_subset = Tag.construct(session=SESSION, tag='Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo')
SESSION.commit()

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 15),
             ('select COUNT(*) from word;', 2),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
