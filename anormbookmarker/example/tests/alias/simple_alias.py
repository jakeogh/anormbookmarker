#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)


from anormbookmarker.example import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)
from anormbookmarker.Alias import Alias

from anormbookmarker.Config import CONFIG
from anormbookmarker.example.db_utils import create_database_and_tables
from anormbookmarker.example.db_utils import create_session
from anormbookmarker.example.testing_functions import check_db_result

import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)

create_database_and_tables(config=CONFIG)

SESSION = create_session(config=CONFIG)

# make a tag to make an alias to
eucalyptus_deglupta = Tag.construct(session=SESSION, tag='Eucalyptus deglupta')
SESSION.commit()

# make a Alias
#alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus', casesensitive=False)
alias = Alias.construct(session=SESSION, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
SESSION.commit()


str_attrs = {'tag': 'a'}

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

pp.pprint(db_result)

check_db_result(db_result)

#from IPython import embed; embed()
