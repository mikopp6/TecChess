import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import game
import settings
import help

def exit_clicked():
	if(messagebox.askyesno("Exit","Are you sure?", parent=root, default="no")):
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

new_game = tk.Button(root, command=game.game, text="New game", font=("Calibri", 30), bg="white")
new_game.grid(row=1, padx=5, pady=5)

settings_button = tk.Button(root, command=settings.settings, text="Settings", font=("Calibri", 30), bg="white")
settings_button.grid(row=2, padx=5, pady=5)

help_button = tk.Button(root, command=help.help, text="Help", font=("Calibri", 30), bg="white")
help_button.grid(row=3, padx=5, pady=5)

exit_button = tk.Button(root, command=exit_clicked, text="Exit Game", font=("Calibri", 30), bg="white")
exit_button.grid(row=4, padx=5, pady=5)

tk.mainloop()