import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
import threading
import time
from plyer import notification

# Global task list
tasks = []

# Function to notify
def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

# Function to monitor task reminders in background
def reminder_thread():
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if task['time'] == now and not task['notified']:
                notify("⏰ Task Reminder", f"{task['task']}")
                task['notified'] = True
        time.sleep(30)  # Check every 30 seconds

# Add task to list
def add_task():
    task_text = task_entry.get()
    reminder_time = time_entry.get()

    if task_text == "" or reminder_time == "":
        messagebox.showwarning("Input Error", "Please enter both task and time.")
        return

    try:
        datetime.strptime(reminder_time, "%H:%M")  # Validates time
    except ValueError:
        messagebox.showerror("Format Error", "Time must be in HH:MM format (24-hr)")
        return

    tasks.append({'task': task_text, 'time': reminder_time, 'notified': False})
    update_task_list()
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

# Update listbox
def update_task_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        listbox.insert(tk.END, f"{i+1}. {task['task']} at {task['time']}")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Delete Task", "Select a task to delete.")
        return
    index = selected[0]
    del tasks[index]
    update_task_list()

# Set up GUI
root = tk.Tk()
root.title("📝 To-Do + Task Reminder")
root.geometry("400x500")
root.resizable(False, False)

# Title label
tk.Label(root, text="To-Do List + Reminder", font=("Helvetica", 16, "bold")).pack(pady=10)

# Task entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)
task_entry.insert(0, "Enter your task")

# Time entry
time_entry = tk.Entry(root, width=40)
time_entry.pack(pady=5)
time_entry.insert(0, "HH:MM (24-hour)")

# Add button
tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Listbox for tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Delete button
tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white", width=20).pack(pady=5)

# Start background reminder thread
threading.Thread(target=reminder_thread, daemon=True).start()

root.mainloop()
