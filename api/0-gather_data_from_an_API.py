#!/usr/bin/python3
"""Script that provides information on an employee's task completion"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_tasks = []
    completed_tasks = 0
    total_tasks = 0

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = json.loads(user_response.content)

    employee_name = user_data.get('name')

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = json.loads(todo_response.content)

    for task in todo_data:
        if task.get('userId') == employee_id:
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1
                employee_tasks.append(task['title'])

    print(f"Employee {employee_name} has completed "
          f"{completed_tasks} out of {total_tasks} tasks:")

    for title in employee_tasks:
        print(f"\t- {title}")
