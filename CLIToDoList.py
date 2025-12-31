import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f" Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number")


def main():
    tasks = load_tasks()

    while True:
        print("\n-- To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

main()