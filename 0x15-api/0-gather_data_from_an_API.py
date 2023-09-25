#!/usr/bin/python3
"""script that returns information about employee"""

import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com/'


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    emp_id = sys.argv[1]

    response = requests.get(BASE_URL + 'users/' + emp_id)
    if response.status_code == 404:
        print('User id not found')
        sys.exit(1)
    elif response.status_code != 200:
        print('Error: status_code:', response.status_code)
        sys.exit(1)
    user_list = response.json()

    response = requests.get(BASE_URL + 'todos/')
    if response.status_code != 200:
        print('Error: status_code:', response.status_code)
        sys.exit(1)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == int(emp_id)]
    completed = [todo for todo in user_todos if todo.get('completed')]

    print(
        'Employee', user_list.get('name'),
        'is done with tasks({}/{}):'.format(len(completed),
                                            len(user_todos)))

    for todo in completed:
        print('\t', todo.get('title'))


if __name__ == '__main__':
    main()
