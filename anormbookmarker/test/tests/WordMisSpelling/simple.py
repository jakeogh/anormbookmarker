#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

# make tag to misspell
plants = Tag.construct(session=SESSION, tag='plants')
SESSION.commit()

# make WordMisSpelling
plants_wms = WordMisSpelling.construct(session=SESSION, wordmisspelling="plantss", word="plants")
SESSION.commit()

# test the WordMispelling (correctly does not create a plantss tag)
plantss = Tag.construct(session=SESSION, tag='plantss')
SESSION.commit()

assert id(plants) == id(plantss)

assert str(plantss) == 'plants'

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 1),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 1),
             ('select COUNT(*) from word;', 1),
             ('select COUNT(*) from wordmisspelling;', 1)]

check_db_result(config=CONFIG, db_result=db_result)
#from IPython import embed; embed()
