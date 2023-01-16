#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests


def get_todos(id):
    url = f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
    todos = requests.get(url).json()
    url_users = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(url_users).json()['name']
    complete = [todo['title'] for todo in todos if todo['completed']]
    print(f"Employee {name} is done with tasks({len(complete)}/{len(todos)}):")
    for title in complete:
        print("\t{}".format(title))


if __name__ == "__main__":
    get_todos(sys.argv[1])
