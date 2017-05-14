
from anormbookmarker.example import Filename
from anormbookmarker.TagClassConstructor import TagClassConstructor
Tag = TagClassConstructor(mapper_to_bookmark=Filename)
from anormbookmarker.Alias import Alias

debug =  False
echo = False

# make a tag to make an alias to
eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
session.commit()

# make a Alias
#alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus', casesensitive=False)
alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
session.commit()

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
