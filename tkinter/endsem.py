import tkinter as tk

def show_selected():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        label_result.config(text=f"Selected: {selected_item}")

# Create main window
root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

# Create a listbox
listbox = tk.Listbox(root, height=6, selectmode=tk.SINGLE)
colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
for color in colors:
    listbox.insert(tk.END, color)

listbox.pack(pady=10)

# Button to get selected item
btn_show = tk.Button(root, text="Show Selected", command=show_selected)
btn_show.pack()

# Label to display selected item
label_result = tk.Label(root, text="Selected: None")
label_result.pack(pady=10)

root.mainloop()
