#!/usr/bin/env python3

from anormbookmarker.test.functions import *

f = Filename.construct(session=SESSION, filename=b"/var/log/messages")
SESSION.commit()

ff = Filename.construct(session=SESSION, filename=b"/var/log/messages")
SESSION.commit()

assert id(f) == id(ff)

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 1),
             ('select COUNT(*) from tag;', 0),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 0),
             ('select COUNT(*) from timestamp;', 0),
             ('select COUNT(*) from word;', 0),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
SESSION.close()
