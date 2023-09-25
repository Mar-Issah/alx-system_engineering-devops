#!/usr/bin/python3
"""script that, uses a REST API, for a given employee ID,

returns information about his/her TODO list progress"""
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    emp_id = int(sys.argv[1])

    res = requests.get(f"{BASE_URL}/users/{emp_id}")
    todos = requests.get(f"{BASE_URL}/todos?userId={emp_id}")

    if res.status_code == 404 or todos.status_code == 404:
        print(f"Employee with ID {emp_id} not found.")
        sys.exit(1)

    employee_name = res.json()["name"]
    completed_tasks = sum(todo["completed"] for todo in todos.json())
    total_tasks = len(todos.json())

    print(
        f"Employee {employee_name} is done"
        f"withtasks({completed_tasks}/{total_tasks}):")
    for todo in todos.json():
        if todo["completed"]:
            print(f"    {todo['title']}")


if __name__ == '__main__':
    main()
