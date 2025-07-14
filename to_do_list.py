"""
To‑Do List 📝
-------------
A simple command-line to-do list app with:
- Add, view, and remove tasks
- Input validation to prevent errors
- Task numbering for easy removal
- Fun feedback sound using winsound module
"""

import winsound
import time

def todo_list():
    """
    Runs an interactive command-line To-Do List app:
    - Lets user add, view, and remove tasks
    - Shows tasks with numbering for easy removal
    - Handles invalid inputs gracefully
    - Plays beep sound on add/remove (Windows only)
    """
    tasks = []

#Loop for chooosing the option
    while True:
        print("\nTo‑Do List 📝")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

#if-else ladder for add,view,delete, exit task
        if choice == "1":
            while True:
                add_task = input("\nEnter the task you want to add 📒: ").strip()
                if add_task:
                    tasks.append(add_task)
                    time.sleep(1)
                    print("Task added successfully..")
                    winsound.Beep(400, 700)
                    break
                else:
                    print("Task cannot be empty! Please enter something.")
        elif choice == "2":
            time.sleep(1)
            print("\n" + "-" * 40 , end="")
            print("\n         Your To-do-list 📒")
            print("-" * 40)
            if not tasks:
                print("No task added yet.")
            else:
                number = 1
                for task in tasks:
                    print(f"{number}. {task}")
                    number += 1
        elif choice == "3":
            try:
                remove_task = int(input("\nEnter the task you want to remove : "))
                if 1 <= remove_task <= len(tasks):
                    tasks.pop(remove_task - 1)
                    time.sleep(1)
                    print("Task Removed successfully... ")
                    winsound.Beep(300, 500)
                else:
                    print("Invalid number ❌. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    todo_list()
