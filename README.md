anormbookmarker provides a Bookmark class that links Tags (unicode sentences) with another mapper class that the user would like to Tag.

The included example shows a simple 'class Filename' getting bookmarked.


![image of db schema from pydot](https://github.com/jakeogh/anormbookmarker/raw/master/dbschema.1493601122.7285874.png "dbschema.png")


Output:

```
$ ./run_tests.py 
create_database() CONFIG.dbname: bookmark_test_1493594511_58077
create_database() CONFIG.dbpath: postgres://postgres@localhost/bookmark_test_1493594511_58077

making Filename: /var/log/messages

making Bookmark:
        file: /var/log/messages
        tag: messages

making Bookmark:
        file: /var/log/messages
        tag: more messages

making Bookmark:
        file: /var/log/mail.log
        tag: mail

All Bookmark's:
    bookmark: b'/var/log/messages' {'more messages', 'messages'}
    bookmark.filename: b'/var/log/messages'
    tags:
         more messages
         messages
    bookmark: b'/var/log/mail.log' {'mail'}
    bookmark.filename: b'/var/log/mail.log'
    tags:
         mail

All Tag's:
    tag: messages
        tag.id: 1
        parents: []
        children: []
        filenames: {b'/var/log/messages'}
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    tag: more messages
        tag.id: 2
        parents: []
        children: []
        filenames: {b'/var/log/messages'}
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    tag: mail
        tag.id: 3
        parents: []
        children: []
        filenames: {b'/var/log/mail.log'}
        bookmarks:
             b'/var/log/mail.log' {'mail'}
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo
        tag.id: 4
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo Buffalo
        tag.id: 5
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo
        tag.id: 6
        parents: []
        children: []
        filenames: set()
        bookmarks:
    tag: plants
        tag.id: 7
        parents: [life]
        children: [trees]
        filenames: set()
        bookmarks:
    tag: trees
        tag.id: 8
        parents: [plants]
        children: []
        filenames: set()
        bookmarks:
    tag: life
        tag.id: 9
        parents: []
        children: [plants]
        filenames: set()
        bookmarks:

All Word's:
    word: messages
        misspellings: []
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    word: more
        misspellings: []
        bookmarks:
             b'/var/log/messages' {'more messages', 'messages'}
    word: mail
        misspellings: []
        bookmarks:
             b'/var/log/mail.log' {'mail'}
    word: Buffalo
        misspellings: []
        bookmarks:
    word: buffalo
        misspellings: []
        bookmarks:
    word: plants
        misspellings: [plantss]
        bookmarks:
    word: trees
        misspellings: []
        bookmarks:
    word: life
        misspellings: []
        bookmarks:

All Wordmisspellings:
plantss -> plants

tag_relationship:
tag_parent_id, tag_id, 
[(7, 8), (9, 7)]

tagword:
tag_id, word_id, position, previous_position, 
[(1, 1, 0, None),
 (2, 2, 0, None),
 (2, 1, 1, 0),
 (3, 3, 0, None),
 (4, 4, 0, None),
 (4, 5, 1, 0),
 (4, 4, 2, 1),
 (4, 5, 3, 2),
 (4, 5, 4, 3),
 (4, 5, 5, 4),
 (4, 4, 6, 5),
 (4, 5, 7, 6),
 (5, 4, 0, None),
 (5, 5, 1, 0),
 (5, 4, 2, 1),
 (5, 5, 3, 2),
 (5, 5, 4, 3),
 (5, 5, 5, 4),
 (5, 5, 6, 5),
 (5, 4, 7, 6),
 (6, 4, 0, None),
 (6, 5, 1, 0),
 (6, 4, 2, 1),
 (6, 5, 3, 2),
 (6, 5, 4, 3),
 (6, 5, 5, 4),
 (6, 5, 6, 5),
 (7, 6, 0, None),
 (8, 7, 0, None),
 (9, 8, 0, None)]

filename:
id, filename, 
[(1, <memory at 0x60ad89be9048>), (2, <memory at 0x60ad89be9110>)]

tagbookmarks:
bookmark_id, tag_id, 
[(1, 1), (1, 2), (2, 3)]

wordmisspelling:
id, wordmisspelling, word_id, 
[(1, 'plantss', 6)]

bookmark:
id, filename_id, 
[(1, 1), (2, 2)]

word:
id, word, 
[(1, 'messages'),
 (2, 'more'),
 (3, 'mail'),
 (4, 'Buffalo'),
 (5, 'buffalo'),
 (6, 'plants'),
 (7, 'trees'),
 (8, 'life')]

tag:
id, 
[(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]

```

