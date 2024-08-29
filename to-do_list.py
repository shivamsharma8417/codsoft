import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})

    def update_task(self, task_number):
        """Mark a task as completed."""
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
        else:
            raise IndexError("Invalid task number.")

    def delete_task(self, task_number):
        """Delete a task from the list."""
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
        else:
            raise IndexError("Invalid task number.")

    def get_tasks(self):
        """Return all tasks with their statuses."""
        return [f"{i}. {task['task']} - {'Completed' if task['completed'] else 'Not Completed'}" for i, task in enumerate(self.tasks)]

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.todo_list = ToDoList()

        # Create UI elements
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Mark Task as Completed", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View All Tasks", command=self.view_tasks)
        self.view_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.todo_list.update_task(selected_task_index)
            self.view_tasks()
        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.todo_list.delete_task(selected_task_index)
            self.view_tasks()
        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def view_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
