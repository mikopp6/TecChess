import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import help
from settings import options

def game():

	def exit_game_clicked():
		if(messagebox.askyesno("Exit","Exiting the game results in a forfeit.\nAre you sure you want to exit?", parent=newgame, default="no")):
			newgame.destroy()

	newgame = tk.Toplevel()
	newgame.title("TecChess - New game")
	newgame.configure(bg="white")
	newgame.geometry("1400x900")
	newgame.resizable(width=False, height=False)
	
	light, dark = options.boardcolor.split(" ")
	difficulty = options.difficulty
	timing = options.timing

	exit_btn = tk.Button(newgame, command=exit_game_clicked, text="Exit Game", font=("Calibri", 20), bg ="white")
	exit_btn.grid(row=0, column=0, padx=5, pady=5, sticky="NW")
	help_btn = tk.Button(newgame, command=help.help, text="Help", font=("Calibri", 20), bg ="white")
	help_btn.grid(row=0, column=1, padx=5, pady=5, sticky="NW")

	options_lbl= tk.Label(newgame, text=light + " " + dark).grid(row=0, column=2)
	options_lbl= tk.Label(newgame, text=difficulty).grid(row=0, column=3)
	options_lbl= tk.Label(newgame, text=timing).grid(row=0, column=4)
	
	board_cnv = tk.Canvas(newgame, bg="white", height=640, width=640)
	board_cnv.grid(row=2, column=0, columnspan=1000)

	for row in range(8):
		for column in range(8):
			if column&1 ^ row&1:
				fill = dark
			else:
				fill = light
			coords = (column*80+1, row*80+1, column*80+80, row*80+80)
			board_cnv.create_rectangle(coords, fill=fill, width=0, state='disabled')
