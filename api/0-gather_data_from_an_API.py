#!/usr/bin/python3
"""Script that returns information on a given employee's TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":
    TASK_TITLES = []
    NUM_DONE_TASKS = 0
    TOTAL_TASKS = 0

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = json.loads(user_response.content)

    employee_name = user_data.get('name')

    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = json.loads(todo_response.content)

    for task in todo_data:
        if task.get('userId') == employee_id:
            if task.get('completed'):
                TASK_TITLES.append(task['title'])
                NUM_DONE_TASKS += 1
            TOTAL_TASKS += 1

    print(f"Employee {employee_name} has completed "
          f"{NUM_DONE_TASKS} out of {TOTAL_TASKS} tasks:")

    for title in TASK_TITLES:
        print(f"\t{title}")
