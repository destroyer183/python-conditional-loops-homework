import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()

root.title("Conditional Loops 3")

root.geometry('250x100')

rectheight = tk.Label(root, text = "Rectangle Height:")
rectheight.place(x = 0, y = 0)

rectheightbox = tk.Text(root, height = 1, width = 10, bg='white')
rectheightbox.place(x = 100, y = 0)

rectwidth = tk.Label(root, text = "Rectangle Width:")
rectwidth.place(x = 0, y = 25)

rectwidthbox = tk.Text(root, height = 1, width = 10, bg='white')
rectwidthbox.place(x = 100, y = 25)

submit = tk.Button(root, text="Submit", command=lambda:area())
submit.place(x = 50, y = 50)

def area():
    if int(rectheightbox.get(1.0, tk.END)) and int(rectwidthbox.get(1.0, tk.END)) > 0:
        area = int(rectheightbox.get(1.0, tk.END)) * int(rectwidthbox.get(1.0, tk.END))
        tkinter.messagebox.showinfo("Conditional Loops 4", area)
    elif rectheightbox.get(1.0, tk.END) or rectwidthbox.get(1.0, tk.END) <= 0:
        quit()

root.mainloop()