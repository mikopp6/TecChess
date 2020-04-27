#
# File game.py
# 
# Main game window, runs as toplevel window. 
# The window is split into two frames, left and right.
# The left frame contains the exit and help-buttons, the coordinates, and the chessboard itself.
# The right frame contains clocks for both players, a section for lost pieces, and a turn indicator.
# 

import tkinter as tk
from tkinter import messagebox
import time
import os, sys, subprocess

from settings import options


def open_file(filename):
	# Function provides open file -support for Windows, MacOS and Linux..
	# Actual user experience may wary depending on plaform, tested only on Windows 10.

	if sys.platform == "win32":
		os.startfile(filename)
	elif sys.platform == "darwin":
		subprocess.call(["open", filename])
	elif sys.platform == "linux":
		subprocess.call(["xdg-open", filename])

def game():

	def exit_game_clicked():
		# Function for the exit-messagebox. Used to exit the back to the main menu.

		if(messagebox.askyesno("Exit","Exiting the game results in a forfeit.\nAre you sure you want to exit?", parent=newgame)):
			newgame.destroy()

	def drawpieces(canvas, piece, xpos, ypos):
		# Function for initially drawing the pieces on the canvas/chessboard.

		img = tk.PhotoImage(file="img/"+piece+".png")
		label = tk.Label(image=img)
		label.image = img
		canvas.create_image(xpos, ypos, image=img)

	def placepieces(canvas):
		# Function containg all initial piece positions.

		for x in range(8):
			drawpieces(canvas, "BlackPawn", 40+80*x, 120)
			drawpieces(canvas, "WhitePawn", 40+80*x, 520)

		drawpieces(canvas, "BlackRook", 40, 40)
		drawpieces(canvas, "BlackRook", 600, 40)
		drawpieces(canvas, "WhiteRook", 40, 600)
		drawpieces(canvas, "WhiteRook", 600, 600)
		drawpieces(canvas, "BlackKnight", 120, 40)
		drawpieces(canvas, "BlackKnight", 520, 40)
		drawpieces(canvas, "WhiteKnight", 120, 600)
		drawpieces(canvas, "WhiteKnight", 520, 600)
		drawpieces(canvas, "BlackBishop", 200, 40)
		drawpieces(canvas, "BlackBishop", 440, 40)
		drawpieces(canvas, "WhiteBishop", 200, 600)
		drawpieces(canvas, "WhiteBishop", 440, 600)
		drawpieces(canvas, "BlackQueen", 280, 40)
		drawpieces(canvas, "BlackKing", 360, 40)
		drawpieces(canvas, "WhiteQueen", 280, 600)
		drawpieces(canvas, "WhiteKing", 360, 600)

	def drawboard(frame):
		# Function for drawing the coordinates and the chessboard on the given frame.

		coordinate_cnv = tk.Canvas(frame, height=700, width=700, bg="white")
		coordinate_cnv.grid(row=1, column=0, columnspan=5, padx=20, pady=20)
		horisontal = ["A", "B", "C", "D", "E", "F", "G", "H"]
		vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
	
		for hor_coords in range(0,8):
			coordinate_cnv.create_text(70+80*hor_coords, 15, text=horisontal[hor_coords], font=("Times New Roman", 15))
			coordinate_cnv.create_text(70+80*hor_coords, 690, text=horisontal[hor_coords], font=("Times New Roman", 15))
	
		for ver_coords in range(0,8):
			coordinate_cnv.create_text(15, 70+80*ver_coords, text=vertical[ver_coords], font=("Times New Roman", 15))
			coordinate_cnv.create_text(690, 70+80*ver_coords, text=vertical[ver_coords], font=("Times New Roman", 15))
	
		board_cnv = tk.Canvas(frame, bg="white", height=638, width=638)
		board_cnv.grid(row=1, column=0, columnspan=5)
	
		for row in range(8):
			for column in range(8):
				if column&1 ^ row&1:
					fill = dark
				else:
					fill = light
				coords = (column*80, row*80, column*80+80, row*80+80)
				board_cnv.create_rectangle(coords, fill=fill, width=0)
		return board_cnv

	def drawleftframe():
		# Function for drawing the left frame containing the buttons on the window.

		leftframe_frm = tk.Frame(newgame, bg="white")
		leftframe_frm.grid(row=0, column=0, padx=20, pady=20)
		
		exit_btn = tk.Button(leftframe_frm, command=exit_game_clicked, text="Exit Game", font=("Calibri", 20), bg ="white")
		exit_btn.grid(row=0, column=0, sticky="W")
		help_btn = tk.Button(leftframe_frm, command=lambda: open_file("helptext.txt"), text="Help", font=("Calibri", 20), bg ="white")
		help_btn.grid(row=0, column=1, sticky="W")

		return leftframe_frm

	def drawrightframe():
		# Function for drawing right frame containing all game info.

		rightframe_frm = tk.Frame(newgame, bg="white")
		rightframe_frm.grid(row=0, column=1)
	
		blacktimermn_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), text="Time remaining:", bg ="white")
		blacktimermn_lbl.grid(row=0, column=0, sticky="W")
		blackclock_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), bg ="white", text=timing, relief="solid", width=20)
		blackclock_lbl.grid(row=0, column=1)	
		blacklostpieces_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), bg ="white", text="Lost pieces")
		blacklostpieces_lbl.grid(row=1, column=0, columnspan=2)	
		lostblackpieces_cnv = tk.Canvas(rightframe_frm, bg="white", height=175, width=500)
		lostblackpieces_cnv.grid(row=2, column=0, columnspan=2)
	
		turn_btn = tk.Button(rightframe_frm, font=("Calibri", 30), text="XXXXXX's turn", bg ="white")
		turn_btn.grid(row=3, column=0, columnspan=2, pady=25)
	
		whitetimermn_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), text="Time remaining:", bg ="white")
		whitetimermn_lbl.grid(row=4, column=0, sticky="W")	
		whiteclock_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), bg ="white", text=timing, relief="solid", width=20)
		whiteclock_lbl.grid(row=4, column=1)	
		whitelostpieces_lbl = tk.Label(rightframe_frm, font=("Calibri", 20), bg ="white", text="Lost pieces")
		whitelostpieces_lbl.grid(row=5, column=0, columnspan=2)
		lostwhitepieces_cnv = tk.Canvas(rightframe_frm, bg="white", height=175, width=500)
		lostwhitepieces_cnv.grid(row=6, column=0, columnspan=2)

	newgame = tk.Toplevel()
	newgame.title("TecChess - New game")
	newgame.configure(bg="white")
	newgame.geometry("1300x850")
	newgame.resizable(width=False, height=False)

	light, dark = options.boardcolor.split(" ")
	difficulty = options.difficulty
	timing = options.timing
	
	leftframe = drawleftframe()
	rightframe = drawrightframe()
	canvas = drawboard(leftframe)
	placepieces(canvas)
