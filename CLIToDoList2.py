import json
import os
from datetime import datetime

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)

            upgraded_tasks = []
            for task in data:
                if isinstance(task, str):
                    upgraded_tasks.append({
                        "title": task,
                        "deadline": "No deadline",
                        "completed": False
                    })
                else:
                    upgraded_tasks.append(task)
            return upgraded_tasks
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Task title:")
    deadline = input("Deadline (YYYY-MM-DD): ")

    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return
    
    task = {
        "title": title,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    
    print("\n Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['title']} (Due: {task['deadline']})")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Task number to mark complete: "))
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid selection.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f" Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number")


def search_tasks(tasks):
    keyword = input("Search keyword: ").lower()
    results = [task for task in tasks if keyword in task["title"].lower()]

    if not results:
        print("No matching tasks.")
    else:
        for task in results:
            status = "✔" if task["completed"] else "❌"
            print(f"[{status}] {task['title']} (Due: {task['deadline']})")

def sort_by_deadline(tasks):
    tasks.sort(key=lambda x: x["deadline"])
    save_tasks(tasks)
    print("Tasks sorted by deadline")

def main():
    tasks = load_tasks()

    while True:
        print("\n-- To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Sort by Deadline")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            sort_by_deadline(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice")

main()