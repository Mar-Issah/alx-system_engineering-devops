#!/usr/bin/python3
"""Script that returns information about an employee in JSON format."""

import json
import requests
import sys


def main():
    """Dump data into a JSON file."""
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    emp_id = int(sys.argv[1])

    res = requests.get(f"{BASE_URL}/users/{emp_id}")
    todos = requests.get(f"{BASE_URL}/todos?userId={emp_id}")

    if res.status_code == 404 or todos.status_code == 404:
        print(f"Employee with ID {emp_id} not found.")
        sys.exit(1)

    employee_name = res.json()["username"]
    tasks = []

    for todo in todos.json():
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name
        }
        tasks.append(task)

    data = {str(emp_id): tasks}
    filename = f"{emp_id}.json"

    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == '__main__':
    main()
