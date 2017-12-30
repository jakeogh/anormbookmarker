#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

from sqlalchemy.orm.exc import NoResultFound
from .Word import Word
from .Word import WordMisSpelling
from .AliasWord import AliasWord
from .Exceptions import ConflictingAliasError

def find_alias(session, alias, tag=False):
    '''
    iterates over the aliaswords table to check for a existing alias
    checks each word for a misspelling and replaces the mispelling if it's found
    returns the alias if found, else returns False
    it's reasonable to return the tag if it's found beacuse unlike an alias, a tag cant point to
    the wrong thing. returning a "duplicate" alias only makes sense if it's pointing to the same tag.
    '''
    corrected_alias = alias
    possible_alias_set = set([])
    assert isinstance(alias, str)

    alias_split = alias.split(' ')

    corrected_alias = alias
    for index, word in enumerate(alias_split):
        try:
            wordmisspelling = session.query(WordMisSpelling).filter_by(wordmisspelling=word).one()
            target_word = wordmisspelling.word
            word = str(target_word)
            corrected_alias = alias.replace(wordmisspelling.wordmisspelling, word)
        except NoResultFound:
            pass

    corrected_alias_split = corrected_alias.split(' ')
    try:
        for index, word in enumerate(corrected_alias_split):
            current_word = session.query(Word).filter_by(word=word).one()
            current_aliasword_list = session.query(AliasWord).filter_by(word=current_word, position=index).all()
            if current_aliasword_list:
                current_aliasword_list_alias_set = set([aliasword.alias for aliasword in current_aliasword_list])
                if not possible_alias_set:
                    possible_alias_set = current_aliasword_list_alias_set
                else:
                    possible_alias_set = possible_alias_set & current_aliasword_list_alias_set
                for aliasword in current_aliasword_list:
                    if index == 0: # only add aliass that start with the correct word
                        possible_alias_set.add(aliasword.alias)
                    else:
                        if aliasword.alias not in possible_alias_set:
                            return False
                if not possible_alias_set:
                    return False
                if len(possible_alias_set) == 1:
                    last_alias = list(possible_alias_set)[0]
                    last_alias_text = str(last_alias)
                    if last_alias_text == corrected_alias:
                        if tag:
                            if last_alias.tag == tag:
                                return last_alias
                            else:
                                error_msg = "alias: '%s' exists, but points to different tag: '%s'" % (alias, last_alias.tag)
                                raise ConflictingAliasError(error_msg)
                        else:
                            return last_alias
                    else:
                        return False
    except NoResultFound: # any failed query
        return False
