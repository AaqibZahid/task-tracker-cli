import argparse
import json
import random
import os
import time
from datetime import datetime

file_path = "tasks.json"

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

parser = argparse.ArgumentParser(
    description="task tracker CLI tool"
)

# --- Setting up sub parsers ---
subparsers = parser.add_subparsers(dest="action", required=True)

# Add, Update, and Delete tasks
add_command_parser = subparsers.add_parser("add", help="command for adding a task")
update_command_parser = subparsers.add_parser("update", help="command for updating a task")
delete_command_parser = subparsers.add_parser("delete", help="command for deleting a task")

# Mark a task as in progress or done
mark_in_progress_command_parser = subparsers.add_parser("mark-in-progress", help="command for marking a task as 'In Progress'")
mark_done_command_parser = subparsers.add_parser("mark-done", help="command for marking a task as 'Done'")

# List all tasks
list_command_parser = subparsers.add_parser("list", help="command for listing all of the tasks")

# --- Adding arguments for sub parsers ---
add_command_parser.add_argument("description", type=str, metavar="<DESCRIPTON>")

update_command_parser.add_argument("id", type=int, action="store", metavar="<TASK_ID>")
update_command_parser.add_argument("New_description", type=str, action="store", metavar="<NEW DESCRIPTON>")

delete_command_parser.add_argument("id", type=int, action="store", metavar="<TASK_ID>")

mark_in_progress_command_parser.add_argument("id", type=int, action="store", metavar="<TASK_TO_MARK>")

mark_done_command_parser.add_argument("id", type=int, action="store", metavar="<TASK_TO_MARK>")

list_command_parser.add_argument("status", type=str, nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status, which can be either to-do, in progress, or done" )

args = parser.parse_args()

# --- Functions ---

def get_current_timestamp():
    # Capture the exact date and time right now
    now = datetime.now()
    # Format: Year-Month-Day Hour:Minute:Second
    return now.strftime("%Y-%m-%d %H:%M:%S")

def getLatestId():
    with open(file_path, "r") as file:
        # read the whole json and get the largest dictionary's id to up-to-date id count
        pass
    return

def addTask(id, desc):

    task = {
        "id": id,
        "description": desc,
        "status": "to-do",
        "createdAt": get_current_timestamp(), # timestamp
        "updatedAt": None # or timestamp when it does get updated 
    }

    with open(file_path, "a") as file:
        # json.dump(task, file)
        pass
    print(f"task {id} has been added!")

def updateTask(id, new_desc):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            pass
            # open json and update the task, add its updatedAt attribute, then write back to the file
    else:
        print(f"task of such id doesnt exist")

def deleteTask(id):
    choice = input("Are you sure? (Y/N): ")
    if choice.lower() == 'y':
        # read the whole json
        # pop that item/task to delete
        # write back the new json to file
        pass

def markTask(id, status):
    # read the whole json
    # update the task's status to update (if it even exists)
    # write back to the file
    print(f"task {id} has been marked '{status}'")

def listTasks(status):
    if status:
        print(f"listing all tasks of status: {status}!")
    else:
        print("listing tasks of all categories!")
    # read the whole json and print the tasks who are of status 'status'
    pass

# --- Logic for running each command ---

id_count = getLatestId()

if args.action == "add":
    addTask(id_count, args.description)
    # id_count = id_count + 1

elif args.action == "update":
    updateTask(args.id, args.New_description)

elif args.action == "delete":
    deleteTask(args.id)

elif args.action in ("mark-to-do" , "mark-in-progress", "mark-done"):
    markTask(args.id, args.status)

elif args.action == "list":
    listTasks(args.status)
