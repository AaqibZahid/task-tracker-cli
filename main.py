import argparse
import json
import random
import os
import time

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

list_command_parser.add_argument("status", type=str, nargs="?", choices=["todo", "in-progress", "done"], help="Filter tasks by status" )

args = parser.parse_args()
id_count = 1
tasks = {}

if args.action == "add":
    print(f"task added of ID {id_count}!\n\tTask description: {args.description}")
    tasks.update({id_count:args.description})
    id_count = id_count+1

elif args.action == "update":
    if tasks.get(args.id):
        print(f"task {args.id} updated!\n\tNew task description: {args.New_description}")
        tasks[args.id] = args.New_description
    else:
        print(f"task of such id doesnt exist")

elif args.action == "delete":
    if tasks.get(args.id):
        print(f"task {args.id} deleted!")
        tasks.pop(args.id)
    else:
        print(f"task of such id doesnt exist")

elif args.action == "mark-in-progress":
    print(f"task {args.id} marked to be in progress!")

elif args.action == "mark-done":
    print(f"task {args.id} marked done!")

elif args.action == "list":
    if args.status:
            print(f"listing all tasks with status: {args.status}!")
    else:
        print("listing all of the tasks!")
    
    for key, value in tasks.items():
        print(f"\t- Task {key}: {value}")
