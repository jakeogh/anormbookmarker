#!/usr/bin/env python3
from kcl.sqlalchemy.model.Filename import Filename
from anormbookmarker.model.BookmarkClassConstructor import BookmarkClassConstructor
Bookmark = BookmarkClassConstructor(mapper_to_bookmark=Filename)
