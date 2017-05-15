#!/usr/bin/env python3

from anormbookmarker.test.functions import *

# make a Filename object to attach to a Bookmark
filename = Filename.construct(session=SESSION, filename=b"/var/log/messages")
SESSION.commit()

# make a tag
messages = Tag.construct(session=SESSION, tag='messages')
SESSION.commit()

# make a Timestamp
timestamp = Timestamp()
SESSION.commit()

print("timestamp:", timestamp)

# make a Bookmark
bookmark = Bookmark.construct(session=SESSION, filename=filename, tag=messages, timestamp=timestamp)
SESSION.commit()

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
SESSION.close()
