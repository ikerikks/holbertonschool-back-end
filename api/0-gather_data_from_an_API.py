#!/usr/bin/python3
""" Gather data from API """
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    second_data = response2.json()

    for i in second_data:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          completed, total))

    for i in tasks:
        print("\t {}".format(i))