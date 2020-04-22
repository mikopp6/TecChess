#
# File main.py
# 
# Root window for the program, executes the mainloop. All other windows run under this as toplevel windows.
# Window contains only the logo, and buttons to access different parts of the program.
#

import tkinter as tk
from tkinter import messagebox
from os import startfile

import game
import settings

def exit_clicked():
	# Function for the exit-messagebox. Used to exit the program.

	if(messagebox.askyesno("Exit","Are you sure?", parent=root)):
		root.destroy()

root = tk.Tk()
root.title("TecChess")
root.configure(bg="white")
root.geometry("600x625")
root.minsize(600,625)
root.columnconfigure(0, weight=1)
for row in range(0, 5):
	root.rowconfigure(row, weight=1)

logo = tk.PhotoImage(file="img/logo.png")
lbl_logo = tk.Label(root, image=logo, bg="white")
lbl_logo.grid(row=0, padx=50, pady=10)

newgame_btn = tk.Button(root, command=game.game, text="New game", font=("Calibri", 30), bg="white")
newgame_btn.grid(row=1, padx=5, pady=5)

settings_btn = tk.Button(root, command=settings.settings, text="Settings", font=("Calibri", 30), bg="white")
settings_btn.grid(row=2, padx=5, pady=5)

help_btn = tk.Button(root, command=lambda: startfile("helptext.txt"), text="Help", font=("Calibri", 30), bg="white")
help_btn.grid(row=3, padx=5, pady=5)

exit_btn = tk.Button(root, command=exit_clicked, text="Exit Game", font=("Calibri", 30), bg="white")
exit_btn.grid(row=4, padx=5, pady=5)

tk.mainloop()