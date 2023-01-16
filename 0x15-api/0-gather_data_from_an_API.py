#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests


def get_todos(id=None):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()
    complete = [todo['title'] for todo in todos if todo['completed']]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(complete), len(todos)))
    for title in complete:
        print("\t {}".format(title))


if __name__ == "__main__":
    get_todos(sys.argv[1])
