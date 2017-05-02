#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License


from anormbookmarker.TagClassConstructor import TagClassConstructor
from Filename import Filename
Tag = TagClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)

from anormbookmarker.Alias import Alias
from anormbookmarker.Word import Word
from anormbookmarker.Word import WordMisSpelling
from db_utils import create_database_and_tables
from db_utils import create_session
from print_database import print_database

def list_tables(session):
    print("\nAll Bookmark's:")
    bookmark_generator = session.query(Bookmark)
    for bookmark in bookmark_generator:
        print('    bookmark:', bookmark)
        print('    bookmark.filename:', bookmark.filename)
        print('    tags:')
        for tag in bookmark.tags:
            print('    '*2, tag)

    print("\nAll Tag's:")
    tag_generator = session.query(Tag)
    for tag in tag_generator:
        print('    tag:', tag)
        print('        tag.id:', tag.id)
        print('        parents:', tag.parents)
        print('        children:', tag.children)
        print('        filenames:', tag.filenames)
        print("        bookmarks:")
        for bookmark in tag.bookmarks:
            print('            ', bookmark)

    print("\nAll Word's:")
    word_generator = session.query(Word)
    for word in word_generator:
        print('    word:', word)
        print('        misspellings:', word.wordmisspellings)
        print("        bookmarks:")
        for bookmark in word.bookmarks:
            print('            ', bookmark)

    print("\nAll Wordmisspellings:")
    wordmisspelling_generator = session.query(WordMisSpelling)
    for word_misspelled in wordmisspelling_generator:
        print(word_misspelled, '->', word_misspelled.word)

    #print("\nAll Timestamps:")
    #timestamp_generator = session.query(Timestamp)
    #for timestamp in timestamp_generator:
    #    print('    timestamp:', timestamp)



def run_tests(session):

    #make a Filename object to attach to a Bookmark
    print("\nmaking Filename: /var/log/messages")
    filename = Filename.construct(session=session, filename=b"/var/log/messages")
    session.commit()

    # make a tag
    next_tag = "messages"
    messages = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make a Bookmark
    print("\nmaking Bookmark:\n \tfile: /var/log/messages\n \ttag: messages")
    bookmark = Bookmark.construct(session=session, filename=filename, tag=messages)
    session.commit()

    # make a tag
    next_tag = "more messages"
    more_messages = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make aother Bookmark
    print("\nmaking Bookmark:\n \tfile: /var/log/messages\n \ttag: more messages")
    bookmark = Bookmark.construct(session=session, filename=filename, tag=more_messages)
    session.commit()

    #make another Filename object to attach to a Bookmark
    filename = Filename.construct(session=session, filename=b"/var/log/mail.log")
    session.commit()

    # make a tag
    next_tag = "mail"
    mail = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make third Bookmark
    print("\nmaking Bookmark:\n \tfile: /var/log/mail.log\n \ttag: mail")
    bookmark = Bookmark.construct(session=session, filename=filename, tag=mail)
    session.commit()

    # make a tag
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make another tag out of the same Word objects
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo Buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make another tag out of the same Word objects that is a subset of above
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make a tag to misspell
    next_tag = "plants"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make a WordMispelling of the plants tag
    #print("\n\nmaking WordMisSpelling: plantss")
    WordMisSpelling.construct(session=session, wordmisspelling="plantss", word="plants")
    session.commit()

    # test the WordMispelling
    next_tag = "plantss"
    #print("\n(should find the existing Tag plants)")
    plants = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make a child tag for plants
    next_tag = "trees"
    trees = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # test parent/child Tag relationship
    plants.children.append(trees)
    session.commit()

    # make a parent tag for plants
    next_tag = "life"
    life = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # test parent Tag relationship
    plants.parents.append(life)
    session.commit()

    # make a tag to make an alias to
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()

    # make a Alias
    #alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus', casesensitive=False)
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()

    # make a duplicate Alias
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()

    # make an Alias that conflicts with existing alias
    alias = Alias.construct(session=session, tag=trees, alias='rainbow eucalyptus')
    session.commit()


    list_tables(session)
    print_database(session)


if __name__ == '__main__':
    '''
    Usage example:
     $ ./run_tests.py
    '''
    create_database_and_tables()
    SESSION = create_session()
    run_tests(SESSION)

