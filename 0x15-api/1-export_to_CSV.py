#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves information about an employee's
    TODO list progress from a remote API.
    """
    """Make a GET request to retrieve user data"""
    users_url = "http://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    response = requests.get(users_url)
    response.raise_for_status()
    user_data = response.json()

    """Extract the username"""
    username = user_data.get("username")

    """Make a GET request to retrieve TODO list data"""
    todos_url = "http://jsonplaceholder.typicode.com/todos"
    todos_params = {"userId": employee_id}
    response = requests.get(todos_url, params=todos_params)
    response.raise_for_status()
    todo_data = response.json()

    """Prepare the TODO list progress"""
    todo_progress = []
    for todo in todo_data:
        task_completed_status = "True" if todo["completed"] else "False"
        task_title = todo["title"]
        todo_progress.append([
            employee_id, username, task_completed_status, task_title
        ])

    """Export data to CSV"""
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(todo_progress)

    print('Data for \
          Employee ID {} exported to {}'.format(employee_id, csv_filename))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
