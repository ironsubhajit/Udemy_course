import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, {}".format(user_name.get() or 'world'))


root = tk.Tk()
root.title("Hello")

user_name = tk.StringVar()  # contains a string & that is whatever is currently typed in the Entry widget

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

# greet button
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

# quit program
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", fill="x", expand=False)

root.mainloop()
