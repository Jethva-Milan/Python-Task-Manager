import json
import os

FILE_NAME="task.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r")as file:
            return json.load(file)
    return []

def save_tasks():
    with open(FILE_NAME,"w") as file:
        json.dump(tasks,file,indent=4)
    
tasks =load_tasks()

def add_task():
    name = input("enter your Task = ").strip()

    if name=="":
        print("task name cannot be empty!")
        return
    tasks.append({"name":name,"completed":False})
    save_tasks()
    print("Task is added successfully")

def view_tasks():
    if not tasks:
        print("task is not available")
        return
    for i , task in enumerate(tasks, start=1):
        status= "completed" if task["completed"] else "pending"
        print(f"{i}.{task['name']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter tesk number to complete :"))

        if 1<=number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("please enter a number.")
        
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("enter task number to delete:"))

        if 1<=number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print("Deleted:",removed["name"])
        else:
            print("Invalid task number.")
    except ValueError:
            print("please enter a numer.")
while True:
    print("\n===== TAKS MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("choose an option : ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using Task Manager!")
        break
    else:
        print("Invalid choice. Try agaain")
        
