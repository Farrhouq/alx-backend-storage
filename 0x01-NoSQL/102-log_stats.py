#!/usr/bin/env python3
"""This is an advanced status log"""

from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB
    cli = MongoClient('mongodb://127.0.0.1:27017')
    logs = cli['logs']['nginx']

    # Print the total number of logs
    print(f'{logs.count_documents({})} logs')

    # List of HTTP methods to count
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('Methods:')
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count the status checks (GET requests to /status)
    status_checks = logs.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_checks} status check')

    # Aggregate the top 10 IPs by count, sorted in descending order
    print("IPs:")
    top_ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')
