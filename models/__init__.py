#!/usr/bin/python3
"""
init file, makes models a package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
