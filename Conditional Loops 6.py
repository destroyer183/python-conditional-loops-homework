import tkinter as tk
from tkinter import *
import random

randomnum = random.randint(1, 100)
print(random)

guess = 0
while guess != randomnum:
    guess = input("Guess a number:")
    if int(guess) == randomnum:
        print("you got it!")
        break
    elif int(guess) > randomnum:
        print("too high")
    elif int(guess) < randomnum:
        print("too low")