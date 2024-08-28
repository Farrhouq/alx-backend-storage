
#!/usr/bin/env python3
"""This is the python mongo"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Thisi sthe listing files"""
    documents = mongo_collection.find()
    return [doc for doc in documents]
