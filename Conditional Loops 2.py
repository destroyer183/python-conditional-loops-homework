import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("Conditional Loops 2")

root.geometry('250x100')

namelabel = tk.Label(root, text = "What is Your Name?")
namelabel.place(x = 0, y = 0)

namebox = tk.Text(root, height = 1, width = 10, bg='white')
namebox.place(x = 125, y = 0)

submit = tk.Button(root, text="Submit", command=lambda:spam())
submit.place(x = 50, y = 50)

def spam():
    while True:
        tkinter.messagebox.showinfo(namebox.get(1.0, tk.END), namebox.get(1.0, tk.END))

root.mainloop()