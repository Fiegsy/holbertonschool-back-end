#!/usr/bin/python3
"""Script that retrieves information on a given employee's TODO list
progress"""

import json
import requests
import sys

def get_employee_todo_progress(emp_id):
    
    task_titles = []
    number_of_done_tasks = 0
    total_number_of_tasks = 0

    
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todo_response.json()

    
    for task in todos:
        if task.get('userId') == emp_id:
            total_number_of_tasks += 1
            if task.get('completed'):
                number_of_done_tasks += 1
                task_titles.append(task['title'])

    
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
    for title in task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
