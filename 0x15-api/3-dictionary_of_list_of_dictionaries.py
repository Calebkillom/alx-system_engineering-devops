#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests


def export_todo_data():
    """function that exports data in the JSON format."""
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """Fetch user data."""
    response_users = requests.get('{}/users'.format(BASE_URL))
    users = response_users.json()

    """Fetch TODO list data."""
    response_todos = requests.get('{}/todos'.format(BASE_URL))
    todos = response_todos.json()

    """Create a dictionary to hold the unique JSON format data."""
    todo_data = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        """ Initialize the list for this user's tasks"""
        user_tasks = []

        for todo in todos:
            if todo['userId'] == user_id:
                task_data = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(task_data)

        """ Add the user's tasks to the dictionary"""
        todo_data[user_id] = user_tasks

    """ Export the data to a unique JSON file """
    unique_filename = 'todo_all_employees.json'
    with open(unique_filename, 'w') as json_file:
        json.dump(todo_data, json_file, indent=4)


if __name__ == '__main__':
    export_todo_data()
