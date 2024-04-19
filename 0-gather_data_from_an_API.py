#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Unable to retrieve employee data.")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if todo_response.status_code != 200:
        print("Error: Unable to retrieve TODO list data.")
        sys.exit(1)
    todo_data = todo_response.json()

    
    completed_tasks = [task['title'] for task in todo_data if task['userId'] == employee_id and task['completed']]
    total_tasks = len(completed_tasks) + sum(1 for task in todo_data if task['userId'] == employee_id)

    
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task_title in completed_tasks:
        print(f"\t{task_title}")
