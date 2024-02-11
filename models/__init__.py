#!/usr/bin/python3
""" initializing the magic file"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
