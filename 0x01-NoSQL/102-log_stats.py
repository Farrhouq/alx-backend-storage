#!/usr/bin/env python3
"""This is the advanced status log"""

from pymongo import MongoClient

cli = MongoClient('mongodb://localhost:27017')

db = cli['logs']
nginx_col = db['nginx']

tot = nginx_col.count_documents({})
print(f'{tot} logs')

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = nginx_col.count_documents({"method": method})
    print(f'\tmethod {method}: {count}')

status_check = nginx_col.count_documents({"path": "/status"})
print(f'{status_check} status check')
