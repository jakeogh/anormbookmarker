#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MIT License

class ConflictingAliasError(ValueError):
    '''
    An Alias cant be created because it conflicts with a existing Alias to a different Word.
    '''
    pass

class ConflictingWordMisSpellingError(ValueError):
    '''
    A WordMisSpelling cant be created because it conflicts with a existing WordMisSpelling to a different Word.
    '''
    pass

class ConflictingWordError(ValueError):
    '''
    An Alias or WordMisSpelling cant be created because it conflicts with a existing Word.
    '''
    pass

class MissingWordError(ValueError):
    '''
    An Alias or WordMisSpelling cant be created because it references a non-existing Word.
    '''
    pass
