#!/usr/bin/env python3
"""This used to find top students"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """Thisis the main top students function"""
    pipeline = [
            {
                "$addFields": {
                    "averageScore": {
                        "$avg": "$topics.score"
                        }
                    }
                },
            {"$sort": {"averageScore": -1}}
            ]
    return list(mongo_collection.aggregate(pipeline))
