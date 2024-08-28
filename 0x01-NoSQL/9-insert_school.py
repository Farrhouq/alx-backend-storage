#!/usr/bin/env python3
"""This is is used to insert a school"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """This is the insertion function"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
