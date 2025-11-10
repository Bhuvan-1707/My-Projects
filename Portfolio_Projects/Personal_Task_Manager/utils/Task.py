class Task:

    def __init__(self,id,title,description,priority,deadline):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
    
    def to_dict(self):
        dictio = dict(id = self.id,
            title = self.title,
            description = self.description,
            priority = self.priority,
            deadline = self.deadline,
            completed = self.completed)
        return dictio
    
    @staticmethod
    def from_dict(Task_dict):
        Task_Instance = Task(Task_dict["id"],Task_dict["title"],Task_dict["description"],Task_dict["priority"],Task_dict["deadline"])
        if Task_dict["completed"]:
            Task_Instance.mark_completed()
        return Task_Instance
    
    def print_task(self):
        print(f"""id: {self.id},
    title: {self.title},
    description: {self.description},
    priority: {self.priority},
    deadline: {self.deadline},
    completed: {self.completed}"""
        )