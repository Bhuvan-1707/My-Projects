from utils.Task import Task
import json

def load_tasks():
    Task_List = []
    with open("tasks.json") as file:
        tasks = json.load(file)
        for task in tasks:
            Task_List.append(Task.from_dict(task))
        return Task_List

def save_tasks(Task_List):
    tasks = []
    for Task in Task_List:
        tasks.append(Task.to_dict())
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)