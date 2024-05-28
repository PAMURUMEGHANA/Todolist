import os
import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def complete_task(tasks):
    print_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Function to display tasks
def print_tasks(tasks):
    if tasks:
        for index, task in enumerate(tasks):
            print(f"{index}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
    else:
        print("No tasks.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. View Tasks\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()