#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent=4)

#from anormbookmarker.TagClassConstructor import TagClassConstructor
#from Filename import Filename
#Tag = TagClassConstructor(mapper_to_bookmark=Filename)
#from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
#Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)
#from anormbookmarker.Alias import Alias
#from anormbookmarker.Word import Word
#from anormbookmarker.Word import WordMisSpelling
from anormbookmarker.Config import CONFIG
from db_utils import create_database_and_tables
from db_utils import create_session
#from db_utils import get_engine
#from print_database import print_database
#
#from kcl.printops import cprint
#from kcl.dirops import all_files
#from kcl.dirops import path_is_dir
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)





if __name__ == '__main__':
    import sys

    test_file = sys.argv[1]
    test_file_module_name = '.'.join(test_file.split('.py')[0].split('/')[-3:])
    import_statement = 'from ' + test_file_module_name + ' import *'
    print("CONFIG.dbpath:", CONFIG.dbpath)
    create_database_and_tables(config=CONFIG)
    SESSION = create_session(config=CONFIG)
    print("import_sstatment:", import_statement)
    #from tests.alias.simple_alias import *
    exec(import_statement)
    pp.pprint(db_result)
    from IPython import embed; embed()

