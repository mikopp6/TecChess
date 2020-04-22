#
# File settings.py
# 
# Contains settings for the program, runs as toplevel window. 
# Different settings are packed in their own frames. These frames are then organized
# to the window using grid.
#

import tkinter as tk
from tkinter import messagebox

class options():
	# Class containing all changeable settings.

	boardcolor = "#b1e4b9 #70a2a3"
	difficulty = "Easy"
	timing = "No time"

def settings():

	def cancel_clicked():
		# Function for the cancel-messagebox. Used to exit without saving.

		if(messagebox.askyesno("Exit","Exit without saving settings?", parent=settings)):
			settings.destroy()
	def save_clicked():
		# Function for the save and exit-messagebox. Saves all settings to options-class.
		
		messagebox.showinfo("Settings", "Settings saved!")
		options.boardcolor = tempcolor.get()
		options.difficulty = tempdifficulty.get()
		options.timing = temptiming.get()
		settings.destroy()

	settings = tk.Toplevel()
	settings.title("TecChess - Settings")
	settings.geometry("300x400")
	settings.configure(bg ="white")
	settings.resizable(width=False, height=False)

	tempdifficulty = tk.StringVar()
	tempdifficulty.set(options.difficulty)
	difficulties = ["Easy", "Medium", "Hard"]

	difficulty_lbl = tk.Label(settings, text="Difficulty", font=("Calibri", 15), bg ="white")
	difficulty_lbl.grid(row=0, column=0, sticky="W")
	diff_frm = tk.Frame(settings)
	diff_frm.grid(row=1, sticky="W")
	
	easy_btn = tk.Radiobutton(diff_frm, text=difficulties[0], variable=tempdifficulty, value=difficulties[0], bg="white", activebackground="white")
	easy_btn.pack(side="left")
	
	medium_btn = tk.Radiobutton(diff_frm, text=difficulties[1], variable=tempdifficulty, value=difficulties[1], bg="white", activebackground="white", state="disabled")
	medium_btn.pack(side="left")

	hard_btn = tk.Radiobutton(diff_frm, text=difficulties[2], variable=tempdifficulty, value=difficulties[2], bg="white", activebackground="white", state="disabled")
	hard_btn.pack(side="left")

	#medium_tp = tooltips.CreateToolTip(medium_btn, "Medium and Hard difficulties not available in this version.")
	#hard_tp = tooltips.CreateToolTip(hard_btn, "Medium and Hard difficulties not available in this version.")

	tempcolor = tk.StringVar()
	tempcolor.set(options.boardcolor)
	colors = ["#b1e4b9 #70a2a3", "#adbd8f #6f8f72", "#eedab6 #c7a37b", "#ffffff #999999"]

	color_lbl = tk.Label(settings, text="Color scheme", font=("Calibri", 15), bg ="white")
	color_lbl.grid(row=2, column=0, sticky="W")
	color_frm = tk.Frame(settings)
	color_frm.grid(row=3, sticky="W")

	for value in colors:
		img = tk.PhotoImage(file="img/"+value+".png")
		label = tk.Label(image=img)
		label.image = img
		tk.Radiobutton(color_frm, variable=tempcolor, value=value, image=img, anchor="n", bg="white", activebackground="white").pack(side="left")

	temptiming = tk.StringVar()
	temptiming.set(options.timing)
	timings = ["No time", "5min/player", "10min/player", "30min/player",]

	timing_lbl = tk.Label(settings, text="Timing", font=("Calibri", 15), bg ="white")
	timing_lbl.grid(row=4, column=0, sticky="W")
	timing_options = tk.OptionMenu(settings, temptiming, *timings)
	timing_options.grid(row=5, sticky="W", padx=5)

	exitbtn_frm = tk.Frame(settings, bg="white", pady=10)
	exitbtn_frm.grid(row=6)

	cancel_btn = tk.Button(exitbtn_frm, command=cancel_clicked, text="Cancel", font=("Calibri", 12), bg="white")
	cancel_btn.pack(side="left", padx=50, pady=10)
	save_btn = tk.Button(exitbtn_frm, command=save_clicked, text="Save & Exit", font=("Calibri", 12), bg="white")
	save_btn.pack(side="left")