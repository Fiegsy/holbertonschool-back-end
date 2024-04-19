#!/usr/bin/python3
"""Script that returns information on a given employee's TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

   
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name')

    
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todo_response.json()

    
    tasks_completed = [task['title'] for task in todo_data if task['userId'] == employee_id and task['completed']]
    total_tasks = sum(1 for task in todo_data if task['userId'] == employee_id)

    
    print(f"Employee {employee_name} is done with tasks ({len(tasks_completed)}/{total_tasks}):")
    for task_title in tasks_completed:
        print(f"\t{task_title}")
