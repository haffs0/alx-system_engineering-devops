#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    complete = [todo.get('title') for todo in todos if todo.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(complete), len(todos)))
    for title in complete:
        print("\t {}".format(title))
