import tkinter as tk

def button_click(row, col):
    print(f"Button at row {row}, column {col} clicked")

# Create the main window
root = tk.Tk()
root.title("3x3 Game Board")

# Create a 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        btn = tk.Button(root, text=f"{row}, {col}", width=10, height=3, command=lambda r=row, c=col: button_click(r, c))
        btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
