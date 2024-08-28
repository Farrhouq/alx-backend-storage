#!/usr/bin/env python3
"""Thisis used to update the topics"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """this is the updater fucntion"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
