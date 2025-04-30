import tkinter as tk

# Function to update the label with selected color
def update_color():
    selected = color_var.get()
    label_display.config(text=f"Selected Color: {selected}", fg=selected.lower())

# Create main window
root = tk.Tk()
root.title("Color Selector")
root.geometry("300x200")

# Create StringVar to hold selected color
color_var = tk.StringVar()
color_var.set("Red")  # Default selection

# Create Radiobuttons
radio_red = tk.Radiobutton(root, text="Red", variable=color_var, value="Red", command=update_color)
radio_green = tk.Radiobutton(root, text="Green", variable=color_var, value="Green", command=update_color)
radio_blue = tk.Radiobutton(root, text="Blue", variable=color_var, value="Blue", command=update_color)

# Pack Radiobuttons
radio_red.pack(anchor='w', padx=20, pady=5)
radio_green.pack(anchor='w', padx=20, pady=5)
radio_blue.pack(anchor='w', padx=20, pady=5)

# Label to show selected color
label_display = tk.Label(root, text="Selected Color: Red", fg="red", font=("Arial", 12))
label_display.pack(pady=20)

# Run the application
root.mainloop()
