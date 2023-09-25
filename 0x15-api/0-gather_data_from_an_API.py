#!/usr/bin/python3
"""script that returns information about employee"""

import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com/'


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    emp_id = sys.argv[1]

    response = requests.get(BASE_URL + 'users/' + emp_id)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user_list = response.json()

    response = requests.get(BASE_URL + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == user_list.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]

    print('Employee', user_list.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]


if __name__ == '__main__':
    main()
