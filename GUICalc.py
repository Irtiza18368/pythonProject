import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')

frame = tk.Frame(window, bg="blue", padx=10)
frame.pack()

entry_value = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry_value.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(num):
    entry_value.insert(tk.END, num)

def equal():
    try:
        result = str(eval(entry_value.get()))
        entry_value.delete(0, tk.END)
        entry_value.insert(0, result)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry_value.delete(0, tk.END)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0)
]

for txt, r, c in buttons:
    tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)
tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()