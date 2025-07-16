import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time
from plyer import notification

# Global task list
tasks = []


# ---------------- Reminder Background Thread ----------------
def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def reminder_thread():
    while True:
        now = datetime.now().strftime("%H:%M")
        for task in tasks:
            if task['time'] == now and not task['notified']:
                notify("🔔 Reminder", f"{task['task']}")
                task['notified'] = True
        time.sleep(30)


# ---------------- Task Handling Functions ----------------
def add_task():
    task_text = task_entry.get()
    reminder_time = time_entry.get()

    if task_text == "" or task_text == "Enter your task" or reminder_time == "" or reminder_time == "HH:MM (24-hour)":
        messagebox.showwarning("Input Error", "Please enter a valid task and time.")
        return

    try:
        datetime.strptime(reminder_time, "%H:%M")
    except ValueError:
        messagebox.showerror("Format Error", "Time must be in HH:MM (24-hr format)")
        return

    tasks.append({'task': task_text, 'time': reminder_time, 'notified': False})
    update_task_list()
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    task_entry.insert(0, "Enter your task")
    time_entry.insert(0, "HH:MM (24-hour)")

def update_task_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        listbox.insert(tk.END, f"{i+1}. {task['task']} @ {task['time']}")

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Delete Task", "Select a task to delete.")
        return
    del tasks[selected[0]]
    update_task_list()

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("📝 Task Reminder & To-Do List")
root.geometry("450x550")
root.configure(bg="#f7f7f7")
root.resizable(False, False)

title_label = tk.Label(root, text="📋 Daily Task Manager", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
title_label.pack(pady=15)

# Frame for input
input_frame = tk.Frame(root, bg="#f7f7f7")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=30, fg="gray")
task_entry.grid(row=0, column=0, padx=5, pady=5)
task_entry.insert(0, "Enter your task")

time_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=30, fg="gray")
time_entry.grid(row=1, column=0, padx=5, pady=5)
time_entry.insert(0, "HH:MM (24-hour)")

def clear_placeholder(e, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def add_placeholder(e, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="gray")

task_entry.bind("<FocusIn>", lambda e: clear_placeholder(e, task_entry, "Enter your task"))
task_entry.bind("<FocusOut>", lambda e: add_placeholder(e, task_entry, "Enter your task"))

time_entry.bind("<FocusIn>", lambda e: clear_placeholder(e, time_entry, "HH:MM (24-hour)"))
time_entry.bind("<FocusOut>", lambda e: add_placeholder(e, time_entry, "HH:MM (24-hour)"))

# Buttons
btn_style = {"font": ("Segoe UI", 11, "bold"), "bg": "#4CAF50", "fg": "white", "width": 18, "bd": 0, "padx": 5, "pady": 5}

add_btn = tk.Button(root, text="➕ Add Task", command=add_task, **btn_style)
add_btn.pack(pady=10)

# Task Listbox
listbox_frame = tk.Frame(root, bg="#e0e0e0", bd=2, relief="groove")
listbox_frame.pack(pady=10, padx=20, fill="both", expand=True)

listbox = tk.Listbox(listbox_frame, font=("Segoe UI", 12), selectbackground="#c0c0c0", bg="#ffffff", bd=0)
listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

# Delete Button
delete_btn = tk.Button(root, text="🗑️ Delete Selected Task", command=delete_task, font=("Segoe UI", 11, "bold"), bg="#f44336", fg="white", width=25, bd=0)
delete_btn.pack(pady=15)

# Start reminder thread
threading.Thread(target=reminder_thread, daemon=True).start()

root.mainloop()
