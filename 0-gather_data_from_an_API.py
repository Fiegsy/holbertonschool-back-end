#!/usr/bin/python3
"""Create a python script's that returns information on a given employee's TODO list
progress"""

import json
import requests
import sys


if __name__ == "__main__":

    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    Emp_id = int(sys.argv[1])

    url_requestUser = f"https://jsonplaceholder.typicode.com/users/{Emp_id}"
    responseUser = requests.get(url_requestUser)
    fieldsUser = json.loads(responseUser.content)

    EMPLOYEE_NAME = fieldsUser.get('name')

    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    fieldsTodo = json.loads(responseTodo.content)

    for task in fieldsTodo:
        if task.get('userId') == Emp_id:
            if task.get('completed') is True:
                TASK_TITLE.append(task['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with "
          f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in TASK_TITLE:
        print(f"\t {task}")