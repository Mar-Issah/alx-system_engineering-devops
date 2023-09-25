#!/usr/bin/python3
"""Script that returns information about an employee in JSON format."""

import json
import requests


def main():
    """Dump data into a Dict file."""
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    users = requests.get(f"{BASE_URL}/users").json()
    todos = requests.get(f"{BASE_URL}/todos").json()

    data = {}
    for user in users:
        user_todos = [todo for todo in todos
                      if todo['userId'] == user['id']]
        user_todos = [{'username': user['username'],
                       'task': todo['title'],
                       'completed': todo['completed']}
                      for todo in user_todos]
        data[str(user['id'])] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    main()
