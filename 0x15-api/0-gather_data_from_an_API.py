#!/usr/bin/python3
"""script uses a REST API for a given employee ID and returns information"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress
    For a given employee ID using a REST API.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetch user data."""
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        print("Failed to fetch user data for employee {}".format(employee_id))
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    """ Fetch TODO list data for the employee."""
    todo_response = requests.get("{}/todos?userId={}"
                                 .format(base_url, employee_id))
    if todo_response.status_code != 200:
        print("Failed to fetch TODO list for employee {}".format(employee_id))
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for todo in todo_data if todo['completed'])

    """Display progress information."""
    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))

    """Display titles of completed tasks."""
    for todo in todo_data:
        if todo['completed']:
            print("\t{}".format(todo['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
