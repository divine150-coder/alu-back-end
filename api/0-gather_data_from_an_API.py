#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]
base_url = "https://jsonplaceholder.typicode.com"

# Fetch employee info
user_url = f"{base_url}/users/{employee_id}"
response = requests.get(user_url)
employee = response.json()
employee_name = employee.get("name")

# Fetch todos
todos_url = f"{base_url}/todos?userId={employee_id}"
response = requests.get(todos_url)
todos = response.json()

# Filter completed tasks
done_tasks = [task for task in todos if task.get("completed")]
total_tasks = len(todos)
number_done = len(done_tasks)

# Print output
print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
for task in done_tasks:
    print(f"\t {task.get('title')}")

