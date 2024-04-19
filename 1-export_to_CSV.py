#!/usr/bin/python3
"""Script to export data in CSV format"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = json.loads(user_response.content)
    username = user_data.get('username')

    
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = json.loads(todo_response.content)

   
    with open(f"{user_id}.csv", mode='w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['User ID', 'Username', 'Task Completed', 'Task Title'])
        for task in todo_data:
            if task.get('userId') == user_id:
                task_completed_status = task['completed']
                task_title = task['title']
                csv_writer.writerow([user_id, username, task_completed_status, task_title])
