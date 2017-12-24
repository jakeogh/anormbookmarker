#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    # make Filename object to attach to a Bookmark
    filename = Filename.construct(session=session, filename=b"messages")
    session.commit()

    # make tag
    messages = Tag.construct(session=session, tag='messages')
    session.commit()

    # make bookmark
    bookmark = Bookmark.construct(session=session, filename=filename, tag=messages)
    session.commit()

    # make second tag
    more_messages = Tag.construct(session=session, tag='more messages')

    # make duplicate bookmark
    duplicate_bookmark = Bookmark.construct(session=session, filename=filename, tag=more_messages)
    session.commit()

    assert id(bookmark) == id(duplicate_bookmark)

    assert 'more messages' in bookmark.tags

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 1),
             ('select COUNT(*) from filename;', 1),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 2),
             ('select COUNT(*) from tagword;', 3),
             ('select COUNT(*) from word;', 2),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
