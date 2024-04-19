#!/usr/bin/python3

"""Python script to retrieve information about an employee's TODO list progress using a REST API"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve employee information and TODO list progress based on the employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None

    Prints:
        Displays the employee's TODO list progress.
    """

    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print("Error: Unable to retrieve employee data.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print("Error: Unable to retrieve TODO list data.")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task['completed'])

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
