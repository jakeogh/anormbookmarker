#!/usr/bin/env python3

from anormbookmarker.test.functions import *

plants = Tag.construct(session=SESSION, tag='plants')
SESSION.commit()

trees = Tag.construct(session=SESSION, tag='trees')
SESSION.commit()

plants.children.append(trees)
SESSION.commit()

assert trees in plants.children
assert plants in trees.parents

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 1),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 2),
             ('select COUNT(*) from timestamp;', 0),
             ('select COUNT(*) from word;', 2),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
SESSION.close()
