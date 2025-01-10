import datetime
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TodoApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("Todo App")

        # Task List
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task_gui)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.check_button = tk.Button(root, text="Mark Completed", command=self.check_task_gui)
        self.check_button.pack(side=tk.LEFT, padx=10)

        self.list_button = tk.Button(root, text="Refresh Tasks", command=self.refresh_task_list)
        self.list_button.pack(side=tk.LEFT, padx=10)

        # Start Reminder Thread
        self.reminder_thread = threading.Thread(target=self.remind, daemon=True)
        self.reminder_thread.start()

    def add_task(self, task, due_date=None):
        self.tasks.append({
            "task": task,
            "due_date": due_date,
            "completed": False
        })
        self.refresh_task_list()

    def check_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                messagebox.showinfo("Task Completed", f"Task '{task}' marked as completed.")
                break
        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for t in self.tasks:
            status = "X" if t["completed"] else "O"
            due_date = f" (Due: {t['due_date']})" if t["due_date"] else ""
            self.task_listbox.insert(tk.END, f"[{status}] {t['task']}{due_date}")

    def remind(self):
        while True:
            current_time = datetime.datetime.now()
            for t in self.tasks:
                if t["due_date"] and not t["completed"]:
                    if current_time >= t["due_date"]:
                        messagebox.showwarning("Task Due", f"Reminder: Task '{t['task']}' is due!")
                        t["completed"] = True
            self.refresh_task_list()
            threading.Event().wait(60)  # Sleep for 60 seconds

    def add_task_gui(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            due_date_input = simpledialog.askstring("Add Task", "Enter due date (YYYY-MM-DD HH:MM) or leave blank:")
            due_date = None
            if due_date_input:
                try:
                    due_date = datetime.datetime.strptime(due_date_input, "%Y-%m-%d %H:%M")
                except ValueError:
                    messagebox.showerror("Invalid Date", "The date format is incorrect. Task not added.")
                    return
            self.add_task(task_name, due_date)

    def check_task_gui(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            task_name = selected_task.split("] ")[1].split(" (Due")[0]  # Extract task name
            self.check_task(task_name)

# Main Application
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
