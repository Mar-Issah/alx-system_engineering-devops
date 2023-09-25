#!/usr/bin/python3
"""script that returns information about employee"""

import csv
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

    employee_name = res.json()["username"]
    completed_tasks = sum(todo["completed"] for todo in todos.json())
    total_tasks = len(todos.json())

    print(
        f"Employee {employee_name} is done"
        f"withtasks({completed_tasks}/{total_tasks}):")
    for todo in todos.json():
        if todo["completed"]:
            print(f"    {todo['title']}")

    filename = f"{emp_id}.csv"

    with open(filename, "w") as file:
        writer = csv.writer(
            file, lineterminator='\n', quoting=csv.QUOTE_ALL)
        for todo in todos.json():
            task_completed = "True" if todo["completed"] else "False"
            task_title = todo["title"]
            writer.writerow(
                [emp_id, employee_name, task_completed, task_title])


if __name__ == '__main__':
    main()
