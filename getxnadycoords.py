import pyautogui
from tkinter import *

def on_click(event):
    x, y = pyautogui.position()
    print(f"Clicked at (x: {x}, y: {y})")

# Create a simple tkinter window
root = Tk()
root.title("Click Coordinates Tracker")

# Set the window size
root.geometry("400x200")

# Create a canvas to cover the whole window
canvas = Canvas(root, width=400, height=200)
canvas.pack()

# Bind the left mouse button click event to the on_click function
canvas.bind("<Button-1>", on_click)

# Start the tkinter event loop
root.mainloop()
