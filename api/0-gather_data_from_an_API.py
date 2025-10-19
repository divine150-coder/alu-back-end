#!/usr/bin/python3
"""
This script retrieves TODO list progress for a given employee ID
from the JSONPlaceholder REST API and displays it in a formatted way.
"""

import requests
import sys


def get_employee_todos(employee_id):
    """Fetch employee info and TODO list from JSONPlaceholder API."""
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        print("Error: Employee with ID {} not found.".format(employee_id))
        return

    user = user_response.json()
    employee_name = user.get("name")

    # Get TODO list
    todos_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    if todos_response.status_code != 200:
        print("Error: Could not fetch TODO list for {}.".format(employee_name))
        return

    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed") is True]

    # Print progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.")
        sys.exit(1)

    get_employee_todos(emp_id)

