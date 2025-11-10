from utils.storage import load_tasks, save_tasks
from utils.Task import Task
import pprint

# Helper Functions

def create_task(id):
    title = input("Enter the title of the task: ")
    description = input("Add some description: ")
    priority = input("High / Medium / Low :")
    deadline = input("Enter random deadline: ")
    new_task = Task(id,title,description,priority,deadline)
    return new_task

def update_completion(id):
    for task in tasks:
        if task.id == id:
            if not task.completed:
                task.mark_completed()
            else:
                print("Task already completed")


while True:
    tasks = load_tasks()
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Completed")
    print("4. Exit")

    choice = input("Select option: ")
    
    if choice == "1":
        new_task = create_task(len(tasks))
        tasks.append(new_task)
        save_tasks(tasks)

    elif choice == "2":
        print("id\tTask\tDescription\tPriority\tDeadline\tIs Completed?")
        for task in tasks:
            print(task.id,"\t",task.title,"\t",task.description,"\t",task.priority,"\t",task.deadline,"\t",task.completed)
    
    elif choice == "3":
        idnum = int(input("Enter the ID of the task: "))
        update_completion(idnum)
        save_tasks(tasks)

    elif choice == "4":
        print("Thankyou for using the Personal task manager")
        break
    else:
        print("Invalid choice")