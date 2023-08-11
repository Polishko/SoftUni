from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = set()

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.add(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for item in self.tasks:
            if item.name == task_name:
                item.completed = True

                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed = 0
        tasks_copy = self.tasks.copy()

        for item in tasks_copy:
            if item.completed:
                self.tasks.remove(item)
                removed += 1

        return f"Cleared {removed} tasks."

    def view_section(self) -> str:
        info = []
        info.append(f"Section {self.name}:")
        [info.append(item.details()) for item in self.tasks]

        return "\n".join(info)
