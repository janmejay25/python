import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas with Shapes")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack(padx=10, pady=10)

# Draw a rectangle: (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")

# Draw a circle (using create_oval for a perfect circle): (x1, y1, x2, y2)
canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")

# Draw a line: (x1, y1, x2, y2)
canvas.create_line(50, 200, 300, 300, fill="green", width=3)

# Run the Tkinter event loop
root.mainloop()
