import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not name or not email or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

root = tk.Tk()
root.title("User Login Form")
root.geometry("300x250")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

name_label = tk.Label(frame, text="Name")
name_label.pack(fill="x", pady=5)

name_entry = tk.Entry(frame)
name_entry.pack(fill="x", pady=5)

email_label = tk.Label(frame, text="Email")
email_label.pack(fill="x", pady=5)

email_entry = tk.Entry(frame)
email_entry.pack(fill="x", pady=5)

password_label = tk.Label(frame, text="Password")
password_label.pack(fill="x", pady=5)

password_entry = tk.Entry(frame, show="*")
password_entry.pack(fill="x", pady=5)

submit_button = tk.Button(frame, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
