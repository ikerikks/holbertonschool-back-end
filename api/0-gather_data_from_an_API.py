#!/usr/bin/python3
"""Gather data from API"""
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    uncompleted = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    for idx in data2:
        if idx.get("id") == int(argv[1]):
            employee = idx.get("name")

    for idx in data:
        if idx.get("userId") == int(argv[1]):
            if idx.get("completed") is True:
                completed += 1
                tasks.append(idx.get("title"))
            else:
                uncompleted += 1
        total = completed + uncompleted

    print("Employee {} is done with task({}/{}):".format(employee,
                                                         completed, total))

    for idx in tasks:
        print("\t {}".format(idx))
