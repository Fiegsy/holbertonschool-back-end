#!/usr/bin/python3
"""
Script to display the progress of a given employee's TODO list.
"""

import json
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    
    task_titles = []
    num_completed_tasks = 0
    total_tasks = 0

    
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todo_response.json()

    
    for task in todos:
        if task.get('userId') == employee_id:
            total_tasks += 1
            if task.get('completed'):
                num_completed_tasks += 1
                task_titles.append(task['title'])

    
    print(f"Employee {employee_name} has completed {num_completed_tasks}/{total_tasks} tasks:")
    for title in task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
