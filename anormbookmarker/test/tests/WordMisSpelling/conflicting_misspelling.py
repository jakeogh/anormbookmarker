#!/usr/bin/env python3

from anormbookmarker.test.test_enviroment import *

# make tag to misspell later
plants = Tag.construct(session=SESSION, tag='plants')
SESSION.commit()

# make tag to misspell later
Plantss = Tag.construct(session=SESSION, tag='Plants')
SESSION.commit()

# make WordMisSpelling
plants_wms = WordMisSpelling.construct(session=SESSION, wordmisspelling="plantss", word="plants")
SESSION.commit()

# make conflicting WordMisSpelling
plants_wms = WordMisSpelling.construct(session=SESSION, wordmisspelling="plantss", word="Plants")
SESSION.commit()

assert str(plants) == 'plants'
#assert id(plants_plants) == id(plantss)

db_result = [('select COUNT(*) from alias;', 0),
             ('select COUNT(*) from aliasword;', 0),
             ('select COUNT(*) from bookmark;', 0),
             ('select COUNT(*) from filename;', 0),
             ('select COUNT(*) from tag;', 2),
             ('select COUNT(*) from tag_relationship;', 0),
             ('select COUNT(*) from tagbookmarks;', 0),
             ('select COUNT(*) from tagword;', 2),
             ('select COUNT(*) from word;', 2),
             ('select COUNT(*) from wordmisspelling;', 1)]

check_db_result(config=CONFIG, db_result=db_result, session=SESSION)
