#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + "/{}".format(user_id)).json()
    todos = requests.get(url + "/{}/todos".format(user_id)).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get('username')
            } for t in todos]}, jsonfile)
