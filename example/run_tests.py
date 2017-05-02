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
        print('    bookmark.id:', bookmark.id)
        print('    bookmark.filename:', bookmark.filename)
        print('    tags:')
        for tag in bookmark.tags:
            print('    '*2, tag)

    print("\nAll Tag's:")
    tag_generator = session.query(Tag)
    for tag in tag_generator:
        print('    tag:', tag)
        print('        tag.id:', tag.id)
        print('        aliases:', tag.aliases)
        print('        parents:', tag.parents)
        print('        children:', tag.children)
        print('        filenames:', tag.filenames)
        print("        bookmarks:")
        for bookmark in tag.bookmarks:
            print('            ', bookmark)

    print("\nAll Aliases's:")
    alias_generator = session.query(Alias)
    for alias in alias_generator:
        print('    alias:', alias)
        print('        alias.id:', alias.id)
        print('        tag:', alias.tag)

    print("\nAll Word's:")
    word_generator = session.query(Word)
    for word in word_generator:
        print('    word:', word)
        print('    word.id:', word.id)
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

    # make a tag
    a = Tag.construct(session=session, tag='a')
    session.commit()

    # make duplicate tag (returns pre-existing tag)
    a = Tag.construct(session=session, tag='a')
    session.commit()

    # make another tag
    a = Tag.construct(session=session, tag='a a')
    session.commit()

    # make another tag
    a = Tag.construct(session=session, tag='a aa')
    session.commit()

    # make another tag
    a = Tag.construct(session=session, tag='a b')
    session.commit()

    # make another tag
    a = Tag.construct(session=session, tag='b a')
    session.commit()

    # make another duplicate tag
    a = Tag.construct(session=session, tag='b a')
    session.commit()

    # make another tag
    a = Tag.construct(session=session, tag='b a')
    session.commit()

    # make a tag to make an alias to
    eucalyptus_deglupta = Tag.construct(session=session, tag='Eucalyptus deglupta')
    session.commit()

    # make a Alias
    #alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus', casesensitive=False)
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()

    # make a duplicate Alias (correctly returns the existing alias)
    alias = Alias.construct(session=session, tag=eucalyptus_deglupta, alias='rainbow eucalyptus')
    session.commit()

    # make a tag to use in a conflicting alias for rainbow eucalyptus
    trees = Tag.construct(session=session, tag='trees')
    session.commit()

    # make a duplicate (conflicting) Alias to a different tag (correctly throws ConflictingAliasError)
    #alias = Alias.construct(session=session, tag=trees, alias='rainbow eucalyptus')
    #session.commit()

    # create a tag that conflicts with an existing alias
    # correctly returns alias target
    rainbow_eucalyptus = Tag.construct(session=session, tag='rainbow eucalyptus')
    session.commit()
    print("rainbow_eucalyptus:", rainbow_eucalyptus)
    print("eucalyptus_deglupta:", eucalyptus_deglupta)
    assert rainbow_eucalyptus == eucalyptus_deglupta

    #make a Filename object to attach to a Bookmark
    filename = Filename.construct(session=session, filename=b"/var/log/messages")
    session.commit()

    #make a duplicate Filename object (correctly returns the existing filename)
    filename = Filename.construct(session=session, filename=b"/var/log/messages")
    session.commit()

    # make a tag
    messages = Tag.construct(session=session, tag='messages')
    session.commit()

    # make a Bookmark
    bookmark = Bookmark.construct(session=session, filename=filename, tag=messages)
    session.commit()

    # make a tag
    more_messages = Tag.construct(session=session, tag='more messages')
    session.commit()

    # make aother Bookmark (correctly adds "more messages" tag to existing bookmark)
    bookmark = Bookmark.construct(session=session, filename=filename, tag=more_messages)
    session.commit()

    #make another Filename object to attach to a Bookmark
    filename = Filename.construct(session=session, filename=b"/var/log/mail.log")
    session.commit()

    # make tag
    mail = Tag.construct(session=session, tag='mail')
    session.commit()

    # make Bookmark
    bookmark = Bookmark.construct(session=session, filename=filename, tag=mail)
    session.commit()

    # make tag
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make another tag out of the same Word objects but swap order
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo Buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make another tag out of the same Word objects that is a subset of above
    next_tag = "Buffalo buffalo Buffalo buffalo buffalo buffalo buffalo"
    tag = Tag.construct(session=session, tag=next_tag)
    session.commit()

    # make a tag to misspell
    tag = Tag.construct(session=session, tag='plants')
    session.commit()

    # todo require manual creation of Word to pass?
    # make a WordMispelling of the plants tag
    WordMisSpelling.construct(session=session, wordmisspelling="plantss", word="plants")
    session.commit()

    # test the WordMispelling (correctly does not create a plantss tag)
    plants = Tag.construct(session=session, tag='plantss')
    session.commit()

    # test wordmisspelling on a multiple word tag
    plants_plants = Tag.construct(session=session, tag='plantss plants')
    session.commit()
    assert str(plants_plants) == 'plants plants'

    # make a child tag for plants (it's a duplicate tag and is correctly returned)
    trees = Tag.construct(session=session, tag='trees')
    session.commit()

    # test parent/child Tag relationship
    # works. plants gets a tree child and tree gets a plants parent
    plants.children.append(trees)
    session.commit()

    # make a parent tag for plants
    life = Tag.construct(session=session, tag='life')
    session.commit()

    # test parent Tag relationship
    # correctly gives plants a parent of life and life a child of plants
    plants.parents.append(life)
    session.commit()


    # make an Alias that conflicts with existing tag (correctly throws exception)
    # ConflictingAliasError
    #alias = Alias(session=session, tag=trees, alias='Eucalyptus deglupta')
    #session.commit()

    # attempt to make a tag it's own parent and child
    # also attempts to give a tag the same parent and child
    # hm, works. trees gets a trees parent and child
    # todo fix. cant thing of a reason to have circular ref
    trees.parents.append(trees)
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

