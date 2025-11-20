import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

# Add new task
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, f"• {task}")  # Add bullet point before each task
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()
        save_tasks()

# ------------------- GUI SETUP -------------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x480")
root.config(bg="#1F4E5F")  # Dark teal background

title = tk.Label(root, text="📝 My To-Do List", font=("Arial", 18, "bold"), bg="#1F4E5F", fg="white")
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12), bg="#CBE4DE", fg="#000", relief="flat", justify="center")
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=12, bg="#3AAFA9", fg="white", font=("Arial", 11, "bold"), command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(
    root,
    width=40,
    height=12,
    font=("Arial", 12),
    selectmode=tk.SINGLE,
    bg="#CBE4DE",
    fg="#000",
    relief="flat",
    highlightthickness=0,
)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", width=12, bg="#F76C6C", fg="white", font=("Arial", 11, "bold"), command=delete_task)
delete_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All", width=12, bg="#17252A", fg="white", font=("Arial", 11, "bold"), command=clear_tasks)
clear_btn.pack(pady=5)

# Load existing tasks (add bullets when displaying)
tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, f"• {task}")

# Footer
footer = tk.Label(root, text="✨ Designed by Aryan Kumar", font=("Poppins", 10), bg="#217B9B", fg="white")
footer.pack(side="bottom", pady=10)

root.mainloop()
