#!/usr/bin/python3
"""Instantiates a storage object."""

from os import getenv

storage_hbnb = getenv("HBNB_TYPE_STORAGE")

if storage_hbnb == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
