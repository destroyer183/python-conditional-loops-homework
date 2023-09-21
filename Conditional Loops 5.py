import tkinter as tk
from tkinter import *
import tkinter.messagebox

subjectcount = 0
subjectmarktotal = 0

root = tk.Tk()

root.title("Conditional Loops 3")

root.geometry('250x100')

subject = tk.Label(root, text = "Subject:")
subject.place(x = 0, y = 0)

subjectbox = tk.Text(root, height = 1, width = 10, bg='white')
subjectbox.place(x = 50, y = 0)

subjectmark = tk.Label(root, text = "Mark:")
subjectmark.place(x = 0, y = 25)

subjectmarkbox = tk.Text(root, height = 1, width = 10, bg='white')
subjectmarkbox.place(x = 50, y = 25)

submit = tk.Button(root, text="Submit", command=lambda:average())
submit.place(x = 50, y = 50)

def average():
    global subjectcount, subjectmarktotal

    if subjectbox.get(1.0, tk.END) != "\n":
        subjectcount += 1
        subjectmarktotal += int(subjectmarkbox.get(1.0, tk.END))
        subjectbox.delete(1.0, tk.END)
        subjectmarkbox.delete(1.0, tk.END)

    elif subjectbox.get(1.0, tk.END) == "\n":
        subjectmarktotal /= subjectcount
        tkinter.messagebox.showinfo("Conditional Loops 5", "Mark Average: " + str(subjectmarktotal) + "%" + "\n Total Subjects: " + str(subjectcount))

root.mainloop()