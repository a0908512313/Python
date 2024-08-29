class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id          # 任務編號
        self.description = description  # 任務描述
        self.completed = False         # 任務狀態，默認為未完成

    def mark_as_complete(self):
        self.completed = True  # 將任務標記為完成


class TaskManager:
    def __init__(self):
        self.tasks = []  # 任務列表

    def check_task(self, id, decription):
        for task in self.tasks:
            if task.task_id == id or task.description == decription:
                return True
        return False

    def add_task(self, description):
        if self.check_task(None, description):
            for task in self.tasks:
                if task.decription == description:
                    task.completed = False
                    return
        else:
            task = Task((len(self.tasks) + 1), description)
            self.tasks.append(task)

    def remove_task(self, task_id):
        if self.check_task(task_id, None):
            for i, task in enumerate(self.tasks):
                if task.id == task_id:
                    del self.tasks[i]
        else:
            print('task do not exist.')

    def mark_task_complete(self, task_id):
        if self.check_task(task_id, None):
            for task in self.tasks:
                if task.task_id == task_id:
                    task.completed = True
        else:
            print('task do not exist.')

    def display_all_tasks(self):
        if not self.tasks:
            print('no any task exist.')
        else:
            for task in self.tasks:
                print(f'task id : {task.task_id}')
                print(f'task description : {task.description}')
                print(f'task status : {task.completed}')


# 使用範例
task_manager = TaskManager()
task_manager.add_task("Complete Python homework")
task_manager.add_task("Read book")
task_manager.mark_task_complete(1)
task_manager.display_all_tasks()
