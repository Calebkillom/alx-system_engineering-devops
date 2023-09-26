#!/usr/bin/python3
""" script that exports data in the JSON format."""
import json
import requests
import sys


def export_employee_todo_data_to_json(employee_id):
    """function that exports data in the JSON format."""
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """Make a GET request to retrieve the employee's TODO list."""
    todos_response = requests.get('{}/todos?userId={}'
                                  .format(BASE_URL, employee_id))

    if todos_response.status_code != 200:
        print('Failed to fetch TODO list for employee {}'.format(employee_id))
        return

    todos = todos_response.json()

    """Get employee name from API."""
    user_response = requests.get('{}/users/{}'.format(BASE_URL, employee_id))
    if user_response.status_code != 200:
        print('Failed to fetch user data for employee {}'.format(employee_id))
        return

    employee = user_response.json()
    employee_name = employee['username']

    """Create a list of tasks"""
    task_list = []
    for todo in todos:
        task = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': employee_name
        }
        task_list.append(task)

    """Create a dictionary with user ID and task information."""
    user_data = {str(employee_id): task_list}

    """Export data to JSON file."""
    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=4)

    print('Data for Employee {} exported to {}'.format(employee_id, filename))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        employee_id = int(sys.argv[1])
        export_employee_todo_data_to_json(employee_id)
