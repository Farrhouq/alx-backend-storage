#!/usr/bin/env python3
"""thisisi use to log status"""

from pymongo import MongoClient


if __name__ == "__main__":
    cli = MongoClient('mongodb://127.0.0.1:27017')
    logs = cli['logs']['nginx']
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{logs.count_documents({})} logs')

    print('Methods:')
    for meth in methods:
        num = logs.count_documents({"method": meth})
        print(f'\tmethod {meth}: {num}')

    num = logs.count_documents({"method": "GET", "path": "/status"})
    print(f'{num} status check')
