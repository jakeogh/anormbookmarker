anormbookmarker provides a Bookmark class that links Tags (unicode sentences) with another mapper class that the user would like to Tag.

The included example shows a simple 'class Filename' getting bookmarked.

A Tag is a unicode string with leading and trailing spaces stripped.

Consecutive spaces are collapsed.

The only invalid Tag is a sequence of 1 or more spaces.

A space is only 0x20. Any other unicode (including whitespace) is treated as valid tag chars.

A Tag is composed of Words seperated by spaces.

Words are unicode strings excluding the standard 0x20 space.

Said another way, the only char that can not be in a Word is 0x20.

Words can have mispellings that alias back to the correct Word.

Tags (Word sequences) can themselves have aliases.

Mispellings also apply to the words that Tag aliases are composed of.

Tags can have any number of parents and/or children.

A Tag can not be it's own parent or child.


![image of db schema from pydot](https://github.com/jakeogh/anormbookmarker/raw/master/dbschema.png "dbschema.png")


Output:

```

$ anormbookmarker
Usage: anormbookmarker [OPTIONS] COMMAND [ARGS]...

  anormbookmarker interface

Options:
  --verbose
  --database TEXT
  --temp-database
  --delete-database
  --debug
  --help             Show this message and exit.

Commands:
  debug
  print_database
  sa_display
  show_config
  test





$ ./run_tests.py
create_database() CONFIG.dbname: anormbookmarker_test_1493721990_0023692
create_database() CONFIG.dbpath: postgres://postgres@localhost/anormbookmarker_test_1493721990_0023692

All Bookmark's:
    bookmark: b'/var/log/messages' {'more messages', 'messages'}
    bookmark.id: 1
    bookmark.filename: b'/var/log/messages'
    tags:
         more messages
         messages
    bookmark: b'/var/log/mail.log' {'mail'}
    bookmark.id: 2
    bookmark.filename: b'/var/log/mail.log'
    tags:
         mail

All Tag's:
    tag: a
        tag.id: 1
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: a a
        tag.id: 2
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: a aa
        tag.id: 3
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: a b
        tag.id: 4
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: b a
        tag.id: 5
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: Eucalyptus deglupta
        tag.id: 6
        aliases: [rainbow eucalyptus]
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: trees
        tag.id: 7
        aliases: []
        parents: [plants, trees]
        children: [trees]
        filenames: set()
        bookmarks:
    tag: messages
        tag.id: 8
        aliases: []
        parents: []
        children: []
        filenames: {b'/var/log/messages'}
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    tag: more messages
        tag.id: 9
        aliases: []
        parents: []
        children: []
        filenames: {b'/var/log/messages'}
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    tag: mail
        tag.id: 10
        aliases: []
        parents: []
        children: []
        filenames: {b'/var/log/mail.log'}
        bookmarks:
             b'/var/log/mail.log' {'mail'}
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo
        tag.id: 11
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo Buffalo
        tag.id: 12
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo
        tag.id: 13
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: plants
        tag.id: 14
        aliases: []
        parents: [life]
        children: [trees]
        filenames: set()
        bookmarks:
    tag: plants plants
        tag.id: 15
        aliases: []
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: life
        tag.id: 16
        aliases: []
        parents: []
        children: [plants]
        filenames: set()
        bookmarks:

All Aliases's:
    alias: rainbow eucalyptus
        alias.id: 1
        tag: Eucalyptus deglupta

All Word's:
    word: a
    word.id: 1
        misspellings: []
        bookmarks:
    word: aa
    word.id: 2
        misspellings: []
        bookmarks:
    word: b
    word.id: 3
        misspellings: []
        bookmarks:
    word: Eucalyptus
    word.id: 4
        misspellings: []
        bookmarks:
    word: deglupta
    word.id: 5
        misspellings: []
        bookmarks:
    word: rainbow
    word.id: 6
        misspellings: []
        bookmarks:
    word: eucalyptus
    word.id: 7
        misspellings: []
        bookmarks:
    word: trees
    word.id: 8
        misspellings: []
        bookmarks:
    word: messages
    word.id: 9
        misspellings: []
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    word: more
    word.id: 10
        misspellings: []
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    word: mail
    word.id: 11
        misspellings: []
        bookmarks:
             b'/var/log/mail.log' {'mail'}
    word: Buffalo
    word.id: 12
        misspellings: []
        bookmarks:
    word: buffalo
    word.id: 13
        misspellings: []
        bookmarks:
    word: plants
    word.id: 14
        misspellings: [plantss]
        bookmarks:
    word: life
    word.id: 15
        misspellings: []
        bookmarks:

All Wordmisspellings:
plantss -> plants

alias:
id, tag_id, 
[(1, 6)]

aliasword:
alias_id, word_id, position, previous_position, 
[(1, 6, 0, None), (1, 7, 1, 0)]

bookmark:
id, filename_id, 
[(1, 1), (2, 2)]

filename:
id, filename, 
[(1, <memory at 0x6c2c300f8a70>), (2, <memory at 0x6c2c300f8f20>)]

tag:
id, 
[(1,),
 (2,),
 (3,),
 (4,),
 (5,),
 (6,),
 (7,),
 (8,),
 (9,),
 (10,),
 (11,),
 (12,),
 (13,),
 (14,),
 (15,),
 (16,)]

tag_relationship:
tag_parent_id, tag_id, 
[(14, 7), (16, 14), (7, 7)]

tagbookmarks:
bookmark_id, tag_id, 
[(1, 8), (1, 9), (2, 10)]

tagword:
tag_id, word_id, position, previous_position, 
[(1, 1, 0, None),
 (2, 1, 0, None),
 (2, 1, 1, 0),
 (3, 1, 0, None),
 (3, 2, 1, 0),
 (4, 1, 0, None),
 (4, 3, 1, 0),
 (5, 3, 0, None),
 (5, 1, 1, 0),
 (6, 4, 0, None),
 (6, 5, 1, 0),
 (7, 8, 0, None),
 (8, 9, 0, None),
 (9, 10, 0, None),
 (9, 9, 1, 0),
 (10, 11, 0, None),
 (11, 12, 0, None),
 (11, 13, 1, 0),
 (11, 12, 2, 1),
 (11, 13, 3, 2),
 (11, 13, 4, 3),
 (11, 13, 5, 4),
 (11, 12, 6, 5),
 (11, 13, 7, 6),
 (12, 12, 0, None),
 (12, 13, 1, 0),
 (12, 12, 2, 1),
 (12, 13, 3, 2),
 (12, 13, 4, 3),
 (12, 13, 5, 4),
 (12, 13, 6, 5),
 (12, 12, 7, 6),
 (13, 12, 0, None),
 (13, 13, 1, 0),
 (13, 12, 2, 1),
 (13, 13, 3, 2),
 (13, 13, 4, 3),
 (13, 13, 5, 4),
 (13, 13, 6, 5),
 (14, 14, 0, None),
 (15, 14, 0, None),
 (15, 14, 1, 0),
 (16, 15, 0, None)]

word:
id, word, 
[(1, 'a'),
 (2, 'aa'),
 (3, 'b'),
 (4, 'Eucalyptus'),
 (5, 'deglupta'),
 (6, 'rainbow'),
 (7, 'eucalyptus'),
 (8, 'trees'),
 (9, 'messages'),
 (10, 'more'),
 (11, 'mail'),
 (12, 'Buffalo'),
 (13, 'buffalo'),
 (14, 'plants'),
 (15, 'life')]

wordmisspelling:
id, wordmisspelling, word_id, 
[(1, 'plantss', 14)]


```

