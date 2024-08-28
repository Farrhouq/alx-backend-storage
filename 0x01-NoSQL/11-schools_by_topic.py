#!/usr/bin/env python3
"""Thisis used to arrange schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """thisis the main fucntiontodo that"""
    return list(mongo_collection.find({"topics": topic}))
