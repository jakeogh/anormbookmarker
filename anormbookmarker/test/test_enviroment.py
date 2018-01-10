#!/usr/bin/env python3

from anormbookmarker.model.Alias import Alias
from anormbookmarker.model.Word import WordMisSpelling
from anormbookmarker.model.Word import Word
from anormbookmarker.model.Tag import Tag
from anormbookmarker.model.Bookmark import Bookmark
from anormbookmarker.model.exceptions import ConflictingAliasError
from anormbookmarker.model.exceptions import ConflictingWordMisSpellingError
from kcl.sqlalchemy.model.Filename import Filename

from sqlalchemy_utils.functions import create_database
from anormbookmarker.model.Config import CONFIG
CONFIG.database = CONFIG.database_timestamp
create_database(CONFIG.database)

from kcl.sqlalchemy.test_enviroment_base import *
