import tkinter as tk
from tkinter import *
import tkinter.messagebox
import math

root = tk.Tk()

root.title("Conditional Loops 3")

root.geometry('250x100')

numberlabel = tk.Label(root, text = "Number:")
numberlabel.place(x = 0, y = 0)

numberbox = tk.Text(root, height = 1, width = 10, bg='white')
numberbox.place(x = 55, y = 0)

submit = tk.Button(root, text="Submit", command=lambda:sqrt())
submit.place(x = 50, y = 50)

def sqrt():
    if int(numberbox.get(1.0, tk.END)) >= 0:
        sqrtnumber = math.sqrt(int(numberbox.get(1.0, tk.END)))
        tkinter.messagebox.showinfo("Conditional Loops 3", sqrtnumber)

root.mainloop()