import tkinter as tk

root = tk.Tk()
root.title("Packing")
tk.Label(root, text="Label 1", bg="green").pack(side="left", fill="y ", padx=(0, 0), pady=(0, 0))
tk.Label(root, text="Label 2", bg="blue").pack(side="top", fill="x", pady=(0, 0), padx=(0, 0))


root.mainloop()