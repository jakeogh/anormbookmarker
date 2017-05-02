anormbookmarker provides a Bookmark class that links Tags (unicode sentences) with another mapper class that the user would like to Tag.

The included example shows a simple 'class Filename' getting bookmarked.

Tags are a ordered sequence of unicode strings (class Word).

Words can have mispellings that alias back to the correct Word.

Tags can have any number of parents and/or children.


![image of db schema from pydot](https://github.com/jakeogh/anormbookmarker/raw/master/dbschema.1493601122.7285874.png "dbschema.png")

Current Output:
```
 $ ./run_tests.py 
create_database() CONFIG.dbname: anormbookmarker_test_1493702428_8747272
create_database() CONFIG.dbpath: postgres://postgres@localhost/anormbookmarker_test_1493702428_8747272
2017-05-01 22:20:29,205 INFO sqlalchemy.engine.base.Engine select version()
2017-05-01 22:20:29,205 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,206 INFO sqlalchemy.engine.base.Engine select current_schema()
2017-05-01 22:20:29,206 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,208 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2017-05-01 22:20:29,208 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,208 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2017-05-01 22:20:29,208 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,209 INFO sqlalchemy.engine.base.Engine show standard_conforming_strings
2017-05-01 22:20:29,209 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,210 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,210 INFO sqlalchemy.engine.base.Engine {'name': 'tag'}
2017-05-01 22:20:29,211 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,211 INFO sqlalchemy.engine.base.Engine {'name': 'alias'}
2017-05-01 22:20:29,212 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,212 INFO sqlalchemy.engine.base.Engine {'name': 'tagbookmarks'}
2017-05-01 22:20:29,213 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,213 INFO sqlalchemy.engine.base.Engine {'name': 'tag_relationship'}
2017-05-01 22:20:29,214 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,214 INFO sqlalchemy.engine.base.Engine {'name': 'tagword'}
2017-05-01 22:20:29,215 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,215 INFO sqlalchemy.engine.base.Engine {'name': 'filename'}
2017-05-01 22:20:29,215 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,216 INFO sqlalchemy.engine.base.Engine {'name': 'bookmark'}
2017-05-01 22:20:29,216 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,216 INFO sqlalchemy.engine.base.Engine {'name': 'word'}
2017-05-01 22:20:29,217 INFO sqlalchemy.engine.base.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%(name)s
2017-05-01 22:20:29,217 INFO sqlalchemy.engine.base.Engine {'name': 'wordmisspelling'}
2017-05-01 22:20:29,218 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE tag (
        id SERIAL NOT NULL, 
        PRIMARY KEY (id)
)


2017-05-01 22:20:29,219 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,224 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,226 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE alias (
        id SERIAL NOT NULL, 
        PRIMARY KEY (id)
)


2017-05-01 22:20:29,227 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,231 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,233 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE filename (
        id SERIAL NOT NULL, 
        filename BYTEA NOT NULL, 
        PRIMARY KEY (id)
)


2017-05-01 22:20:29,233 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,239 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,241 INFO sqlalchemy.engine.base.Engine CREATE UNIQUE INDEX ix_filename_filename ON filename (filename)
2017-05-01 22:20:29,241 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,244 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,246 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE word (
        id SERIAL NOT NULL, 
        word VARCHAR(255) NOT NULL CHECK (position('\x20' in word) = 0), 
        PRIMARY KEY (id)
)


2017-05-01 22:20:29,246 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,250 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,252 INFO sqlalchemy.engine.base.Engine CREATE UNIQUE INDEX ix_word_word ON word (word)
2017-05-01 22:20:29,252 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,258 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,260 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE tag_relationship (
        tag_parent_id INTEGER, 
        tag_id INTEGER, 
        FOREIGN KEY(tag_parent_id) REFERENCES tag (id), 
        FOREIGN KEY(tag_id) REFERENCES tag (id)
)


2017-05-01 22:20:29,260 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,262 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,264 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE tagword (
        tag_id INTEGER, 
        alias_id INTEGER, 
        word_id INTEGER NOT NULL, 
        position INTEGER NOT NULL CHECK (position<100), 
        previous_position INTEGER CHECK ((previous_position IS NULL AND position = 0) OR ((previous_position = position - 1) IS TRUE)), 
        PRIMARY KEY (tag_id, alias_id, word_id, position), 
        UNIQUE (word_id, tag_id, alias_id, position), 
        FOREIGN KEY(tag_id) REFERENCES tag (id), 
        FOREIGN KEY(alias_id) REFERENCES alias (id), 
        FOREIGN KEY(word_id) REFERENCES word (id)
)


2017-05-01 22:20:29,264 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,272 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,274 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE bookmark (
        id SERIAL NOT NULL, 
        filename_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(filename_id) REFERENCES filename (id)
)


2017-05-01 22:20:29,274 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,278 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,283 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE wordmisspelling (
        id SERIAL NOT NULL, 
        wordmisspelling VARCHAR(255) NOT NULL, 
        word_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(word_id) REFERENCES word (id)
)


2017-05-01 22:20:29,283 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,287 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,289 INFO sqlalchemy.engine.base.Engine CREATE INDEX ix_wordmisspelling_id ON wordmisspelling (id)
2017-05-01 22:20:29,289 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,292 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,293 INFO sqlalchemy.engine.base.Engine CREATE UNIQUE INDEX ix_wordmisspelling_wordmisspelling ON wordmisspelling (wordmisspelling)
2017-05-01 22:20:29,293 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,296 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,297 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE tagbookmarks (
        bookmark_id INTEGER NOT NULL, 
        tag_id INTEGER NOT NULL, 
        PRIMARY KEY (bookmark_id, tag_id), 
        UNIQUE (bookmark_id, tag_id), 
        FOREIGN KEY(bookmark_id) REFERENCES bookmark (id), 
        FOREIGN KEY(tag_id) REFERENCES tag (id)
)


2017-05-01 22:20:29,297 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,301 INFO sqlalchemy.engine.base.Engine COMMIT

making Filename: /var/log/messages
2017-05-01 22:20:29,331 INFO sqlalchemy.engine.base.Engine select version()
2017-05-01 22:20:29,331 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,332 INFO sqlalchemy.engine.base.Engine select current_schema()
2017-05-01 22:20:29,332 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,333 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2017-05-01 22:20:29,333 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,333 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2017-05-01 22:20:29,333 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,334 INFO sqlalchemy.engine.base.Engine show standard_conforming_strings
2017-05-01 22:20:29,334 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,334 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2017-05-01 22:20:29,335 INFO sqlalchemy.engine.base.Engine SELECT filename.id AS filename_id, filename.filename AS filename_filename 
FROM filename 
WHERE filename.filename = %(filename_1)s
2017-05-01 22:20:29,335 INFO sqlalchemy.engine.base.Engine {'filename_1': <psycopg2.extensions.Binary object at 0x6e58eea77058>}
2017-05-01 22:20:29,337 INFO sqlalchemy.engine.base.Engine INSERT INTO filename (filename) VALUES (%(filename)s) RETURNING filename.id
2017-05-01 22:20:29,337 INFO sqlalchemy.engine.base.Engine {'filename': <psycopg2.extensions.Binary object at 0x6e58eea77080>}
2017-05-01 22:20:29,338 INFO sqlalchemy.engine.base.Engine COMMIT
2017-05-01 22:20:29,343 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2017-05-01 22:20:29,344 INFO sqlalchemy.engine.base.Engine SELECT wordmisspelling.id AS wordmisspelling_id, wordmisspelling.wordmisspelling AS wordmisspelling_wordmisspelling, wordmisspelling.word_id AS wordmisspelling_word_id 
FROM wordmisspelling 
WHERE wordmisspelling.wordmisspelling = %(wordmisspelling_1)s
2017-05-01 22:20:29,344 INFO sqlalchemy.engine.base.Engine {'wordmisspelling_1': 'messages'}
2017-05-01 22:20:29,347 INFO sqlalchemy.engine.base.Engine SELECT word.id AS word_id, word.word AS word_word 
FROM word 
WHERE word.word = %(word_1)s
2017-05-01 22:20:29,347 INFO sqlalchemy.engine.base.Engine {'word_1': 'messages'}
2017-05-01 22:20:29,348 INFO sqlalchemy.engine.base.Engine SELECT wordmisspelling.id AS wordmisspelling_id, wordmisspelling.wordmisspelling AS wordmisspelling_wordmisspelling, wordmisspelling.word_id AS wordmisspelling_word_id 
FROM wordmisspelling 
WHERE wordmisspelling.wordmisspelling = %(wordmisspelling_1)s
2017-05-01 22:20:29,348 INFO sqlalchemy.engine.base.Engine {'wordmisspelling_1': 'messages'}
2017-05-01 22:20:29,349 INFO sqlalchemy.engine.base.Engine SELECT word.id AS word_id, word.word AS word_word 
FROM word 
WHERE word.word = %(word_1)s
2017-05-01 22:20:29,349 INFO sqlalchemy.engine.base.Engine {'word_1': 'messages'}
2017-05-01 22:20:29,351 INFO sqlalchemy.engine.base.Engine SELECT wordmisspelling.id AS wordmisspelling_id, wordmisspelling.wordmisspelling AS wordmisspelling_wordmisspelling, wordmisspelling.word_id AS wordmisspelling_word_id 
FROM wordmisspelling 
WHERE wordmisspelling.wordmisspelling = %(wordmisspelling_1)s
2017-05-01 22:20:29,351 INFO sqlalchemy.engine.base.Engine {'wordmisspelling_1': 'messages'}
2017-05-01 22:20:29,352 INFO sqlalchemy.engine.base.Engine SELECT word.id AS word_id, word.word AS word_word 
FROM word 
WHERE word.word = %(word_1)s
2017-05-01 22:20:29,352 INFO sqlalchemy.engine.base.Engine {'word_1': 'messages'}
2017-05-01 22:20:29,354 INFO sqlalchemy.engine.base.Engine INSERT INTO word (word) VALUES (%(word)s) RETURNING word.id
2017-05-01 22:20:29,354 INFO sqlalchemy.engine.base.Engine {'word': 'messages'}
2017-05-01 22:20:29,356 INFO sqlalchemy.engine.base.Engine INSERT INTO tag DEFAULT VALUES RETURNING tag.id
2017-05-01 22:20:29,356 INFO sqlalchemy.engine.base.Engine {}
2017-05-01 22:20:29,358 INFO sqlalchemy.engine.base.Engine INSERT INTO tagword (tag_id, word_id, position, previous_position) VALUES (%(tag_id)s, %(word_id)s, %(position)s, %(previous_position)s)
2017-05-01 22:20:29,358 INFO sqlalchemy.engine.base.Engine {'tag_id': 1, 'position': 0, 'previous_position': None, 'word_id': 1}
2017-05-01 22:20:29,359 INFO sqlalchemy.engine.base.Engine ROLLBACK
Traceback (most recent call last):
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 1182, in _execute_context
    context)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/default.py", line 470, in do_execute
    cursor.execute(statement, parameters)
psycopg2.IntegrityError: null value in column "alias_id" violates not-null constraint
DETAIL:  Failing row contains (1, null, 1, 0, null).


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "./run_tests.py", line 175, in <module>
    run_tests(SESSION)
  File "./run_tests.py", line 72, in run_tests
    messages = Tag.construct(session=session, tag=next_tag)
  File "/usr/lib64/python3.4/site-packages/anormbookmarker/TagClassConstructor.py", line 99, in tag_construct
    new_tag = cls(tag=tag, session=session)
  File "<string>", line 4, in __init__
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/state.py", line 414, in _initialize_instance
    manager.dispatch.init_failure(self, args, kwargs)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/langhelpers.py", line 60, in __exit__
    compat.reraise(exc_type, exc_value, exc_tb)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/compat.py", line 187, in reraise
    raise value
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/state.py", line 411, in _initialize_instance
    return manager.original_init(*mixed[1:], **kwargs)
  File "/usr/lib64/python3.4/site-packages/anormbookmarker/TagClassConstructor.py", line 88, in tag_init
    session.flush(objects=[self])
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/scoping.py", line 157, in do
    return getattr(self.registry(), name)(*args, **kwargs)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/session.py", line 2139, in flush
    self._flush(objects)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/session.py", line 2259, in _flush
    transaction.rollback(_capture_exception=True)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/langhelpers.py", line 60, in __exit__
    compat.reraise(exc_type, exc_value, exc_tb)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/compat.py", line 187, in reraise
    raise value
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/session.py", line 2223, in _flush
    flush_context.execute()
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/unitofwork.py", line 389, in execute
    rec.execute(self)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/unitofwork.py", line 548, in execute
    uow
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/persistence.py", line 181, in save_obj
    mapper, table, insert)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/orm/persistence.py", line 835, in _emit_insert_statements
    execute(statement, params)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 945, in execute
    return meth(self, multiparams, params)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/sql/elements.py", line 263, in _execute_on_connection
    return connection._execute_clauseelement(self, multiparams, params)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 1053, in _execute_clauseelement
    compiled_sql, distilled_params
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 1189, in _execute_context
    context)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 1393, in _handle_dbapi_exception
    exc_info
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/compat.py", line 203, in raise_from_cause
    reraise(type(exception), exception, tb=exc_tb, cause=cause)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/util/compat.py", line 186, in reraise
    raise value.with_traceback(tb)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/base.py", line 1182, in _execute_context
    context)
  File "/usr/lib64/python3.4/site-packages/sqlalchemy/engine/default.py", line 470, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.IntegrityError: (psycopg2.IntegrityError) null value in column "alias_id" violates not-null constraint
DETAIL:  Failing row contains (1, null, 1, 0, null).
 [SQL: 'INSERT INTO tagword (tag_id, word_id, position, previous_position) VALUES (%(tag_id)s, %(word_id)s, %(position)s, %(previous_position)s)'] [parameters: {'tag_id': 1, 'position': 0, 'previous_position': None, 'word_id': 1}]

```




Expected Output:

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

