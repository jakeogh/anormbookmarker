#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

# make Filename object to attach to a Bookmark
filename = Filename.construct(session=SESSION, filename=b"/var/log/messages")
SESSION.commit()

# make tag
messages = Tag.construct(session=SESSION, tag='messages')
SESSION.commit()

# make bookmark
bookmark = Bookmark.construct(session=SESSION, filename=filename, tag=messages)
SESSION.commit()

# make duplicate bookmark
duplicate_bookmark = Bookmark.construct(session=SESSION, filename=filename, tag=messages)
SESSION.commit()

assert id(bookmark) == id(duplicate_bookmark)

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 1),
             ('select COUNT(*) from filename;', 1),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 1),
             ('select COUNT(*) from tagword;', 1),
             ('select COUNT(*) from word;', 1),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
