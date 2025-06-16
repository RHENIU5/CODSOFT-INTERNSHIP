import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty")
    else:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        del tasks[task_index]
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "No task selected")

def mark_done():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        task = tasks[task_index]
        if "[Done]" not in task:
            tasks[task_index] = task + " [Done]"
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "No task selected")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Widgets
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=12, command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

done_button = tk.Button(root, text="Mark as Done", width=12, command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=12, command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()
