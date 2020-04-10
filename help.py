import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def help():
	help = tk.Toplevel()
	help.title("TecChess - Help")
	help.resizable(width=False, height=False)

	helptext = tk.Text(help, wrap=tk.WORD)	
	with open("helptext.txt", 'r') as f:
		helptext.insert(tk.INSERT, f.read())
	helptext.pack()