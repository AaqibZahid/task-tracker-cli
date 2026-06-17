# Task Tracker CLI
https://roadmap.sh/projects/task-tracker
## Overview

A simple command-line tool to track your daily tasks. It lets you add, update, delete, and filter tasks by status (to-do, in-progress, and done) right from your terminal.

## Code Style

This project uses a hybrid approach: procedural functions handle the command logic and file operations, while OOP concepts keep the task data structures clean and organized.

## Features

- Add, update, and delete tasks
- Mark tasks as to-do, in-progress, or done
- List all tasks or filter them by their status
- Tracks when tasks are created and updated using timestamps
- Asks for confirmation before deleting a task to prevent accidents

## Concepts Learned

- Using Python's native `argparse` to create subparsers and handle CLI commands.
- Reading, writing, and safely updating data in a local `json` file.
- Managing file system edge cases (like checking if the file is empty or missing before loading).
- Working with the `datetime` module for time-tracking.

## How to Run

1. Clone this repo and navigate into the folder:

```bash
git clone <your-repo-link>
cd task-tracker-cli
```

2. Run the script using python main.py or py main.py followed by your command:

```bash
# Add a task
python main.py add "Buy groceries"

# List all tasks
python main.py list

# List filtered tasks
python main.py list in-progress

# Update a task description
python main.py update 1 "Buy groceries and cook dinner"

# Change a task's status
python main.py mark-in-progress 1
python main.py mark-done 1

# Delete a task
python main.py delete 1
```
