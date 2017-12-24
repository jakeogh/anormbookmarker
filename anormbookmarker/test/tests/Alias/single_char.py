#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *
with self_contained_session(CONFIG.database_timestamp) as session:
    BASE.metadata.create_all(session.bind)

    # make a tag to make an alias to
    e_uppercase_tag = Tag.construct(session=session, tag='E')
    session.commit()

    # make a Alias #todo, this single char case shouldnt be allowed, prob no single AliasWord Alias instances
    e_lowercase_alias = Alias.construct(session=session, tag=e_uppercase_tag, alias='e')
    session.commit()

db_result = [('select COUNT(*) from alias;', 1),
             ('select COUNT(*) from aliasword;', 1),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 1),
             ('select COUNT(*) from word;', 2),
             ('select COUNT(*) from wordmisspelling;', 0)]

check_db_result(config=CONFIG, db_result=db_result)
