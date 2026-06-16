import argparse
import json
import os
from datetime import datetime

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

list_command_parser.add_argument("status", type=str, nargs="?", choices=["to-do", "in-progress", "done"], help="Filter tasks by status, which can be either to-do, in progress, or done" )

args = parser.parse_args()

# --- setting up json file ---
file_path = "tasks.json"
content = {
    "last_id": 0,
    "tasks": []
}

# check if the file is missing OR if it's completely empty (0 bytes)
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    with open(file_path, "w", newline="") as file:
        json.dump(content, file, indent=4)
else:
    with open(file_path, "r") as file:
        content = json.load(file)

# --- Functions ---
def write():
    with open(file_path, "w", newline="") as file:
        json.dump(content, file, indent=4)

def get_current_timestamp():
    now = datetime.now()
    # Format: Day-Month-Year Hour:Minute:Second
    return now.strftime("%d-%m-%Y %H:%M:%S")

def addTask(id, desc):
    new_id = id+1
    task = {
        "id": new_id,
        "description": desc,
        "status": "to-do",
        "createdAt": get_current_timestamp(),
        "updatedAt": None # or timestamp when it does get updated 
    }
    content["tasks"].append(task)
    content["last_id"] = new_id
    write()

    print(f"task {new_id} has been added!")

def TaskFound(id):
    for task in content["tasks"]:
        if task["id"] == id:
            return task 
    return None

def updateTask(id, new_desc):
    task = TaskFound(id)
    if task:
        idx = content["tasks"].index(task)
        content["tasks"][idx]["description"] = new_desc
        content["tasks"][idx]["updatedAt"] = get_current_timestamp()
        write()
        print(f"task {id} has been updated!")
    else:
        print(f"task of id {id} doesn't exist")

def deleteTask(id):
    task = TaskFound(id)
    if task:
        choice = input("Are you sure? (Y/N): ")
        if choice.lower() == 'y':
            content["tasks"].remove(task)
            write()
            print(f"task {id} has been deleted.")
        elif choice.lower() == 'n':
            return
    else:
        print(f"task of id {id} doesn't exist")

def markTask(id, status):
    task = TaskFound(id)
    if task:
        idx = content["tasks"].index(task)
        content["tasks"][idx]["status"] = status
        write()
        print(f"task {id} has been marked '{status}'")
    else:
        print(f"task of id {id} doesn't exist")

def listTasks(status):
    if status:
        print(f"listing all tasks of status: {status}!")
        for task in content["tasks"]:
            if task["status"] == status:
                print(task)
    else:
        print("listing tasks of all categories.")
        for task in content["tasks"]:
            print(task)

# --- Logic for running each command ---

if args.action == "add":
    addTask(content["last_id"], args.description)

elif args.action == "update":
    updateTask(args.id, args.New_description)

elif args.action == "delete":
    deleteTask(args.id)

elif args.action == "mark-to-do":
    markTask(args.id, "to-do") 

elif args.action == "mark-in-progress":
    markTask(args.id, "in-progress")

elif args.action == "mark-done":
    markTask(args.id, "done")

elif args.action == "list":
    listTasks(args.status)