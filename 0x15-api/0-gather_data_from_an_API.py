#!/usr/bin/python3
"""script that returns information about employee"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])

    res = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id))
    employee_data = res.json()
    emp_name = employee_data['name']

    # Get todo list data
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id))
    todo_list = response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_list if task['completed']]

    # Display progress
    print(
        "Employee {} is done with tasks({}/{}):".format(
            emp_name, len(completed_tasks), len(todo_list)))
    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == '__main__':
    main()
