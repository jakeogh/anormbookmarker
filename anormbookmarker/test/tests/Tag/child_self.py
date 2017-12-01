#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
from sqlalchemy.exc import IntegrityError

plants = Tag.construct(session=SESSION, tag='plants')
SESSION.commit()

plants.children.append(plants)
try:
    SESSION.commit()
except IntegrityError:
    print("correctly throws IntegrityError")

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 1),
             ('select COUNT(*) from word;', 1),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
