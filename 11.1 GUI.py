import tkinter as tk
from tkinter import * 

def counter(*args):
    text = var.get()
    count_label.config(text = f"Your text has {len(text)} characters.")
    

#tk
root = tk.Tk()
root.title("Charakter Counter")
root.geometry("500x320")
var = StringVar()


label1 = tk.Label(root, text = "Your text: ", font = ("Arial", 18))
label1.pack(side = "top", fill = "x", padx = 5, pady = 10)

label_entry = tk.Entry(root, textvar = var, font = ("Arial", 18))
label_entry.pack(side = "top", fill = "x", padx = 5, pady = 10)

count_label = tk.Label(root, text = "", font = ("Arial", 18))
count_label.pack(side = "top", fill = "x", padx = 5, pady = 10)

var.trace("w", counter)

root.mainloop()