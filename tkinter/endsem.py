import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pack Method Example")
root.geometry("300x200")

# Create three buttons
button1 = tk.Button(root, text="Top" ,bg="red")
button2 = tk.Button(root, text="Left")
button3 = tk.Button(root, text="Right")

# Pack the buttons using different options
button1.place(x=50 ,y=50)

# Start the Tkinter event loop
root.mainloop()
