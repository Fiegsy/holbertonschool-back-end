#!/usr/bin/python3
"""Script that returns information on a given employee's TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":
    task_titles = []
    num_completed_tasks = 0
    total_tasks = 0

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_user = requests.get(user_url)
    user_data = json.loads(response_user.content)

    employee_name = user_data.get('name')

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response_todo = requests.get(todo_url)
    todo_data = json.loads(response_todo.content)

    for task in todo_data:
        if task.get('userId') == employee_id:
            total_tasks += 1
            if task.get('completed'):
                num_completed_tasks += 1
                task_titles.append(task['title'])

    print(f"Employee {employee_name} is done with "
          f"tasks ({num_completed_tasks}/{total_tasks}):")

    for title in task_titles:
        print(f"\t{title}")
