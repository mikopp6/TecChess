import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class options():
	boardcolor = "#b1e4b9 #70a2a3"
	difficulty = "Easy"
	timing = "No time"

def settings():

	def cancel_clicked():
		if(messagebox.askyesno("Exit","Exit without saving settings?", parent=settings, default="no")):
			settings.destroy()
	def save_clicked():
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

	difficulty_label = tk.Label(settings, text="Difficulty", font=("Calibri", 15), bg ="white")
	difficulty_label.grid(row=0, column=0, sticky="W")
	diff_frm = tk.Frame(settings)
	for value in difficulties:
		if value=="Easy":
			tk.Radiobutton(diff_frm, text=value, variable=tempdifficulty, value=value, bg="white", activebackground="white").pack(side="left")
		else:
			tk.Radiobutton(diff_frm, text=value, variable=tempdifficulty, value=value, bg="white", activebackground="white", state="disabled").pack(side="left")	
	diff_frm.grid(row=1, sticky="W")

	tempcolor = tk.StringVar()
	tempcolor.set(options.boardcolor)
	colors = ["#b1e4b9 #70a2a3", "#adbd8f #6f8f72", "#eedab6 #c7a37b", "#ffffff #999999"]

	color_label = tk.Label(settings, text="Color scheme", font=("Calibri", 15), bg ="white")
	color_label.grid(row=2, column=0, sticky="W")
	color_frm = tk.Frame(settings)
	
	for value in colors:
		img = tk.PhotoImage(file="img/"+value+".png")
		label = tk.Label(image=img)
		label.image = img
		tk.Radiobutton(color_frm, variable=tempcolor, value=value, image=img, anchor="n", bg="white", activebackground="white").pack(side="left")
		
	color_frm.grid(row=3, sticky="W")

	temptiming = tk.StringVar()
	temptiming.set(options.timing)
	timings = ["No time", "5min/player", "10min/player", "30min/player",]

	timing_label = tk.Label(settings, text="Timing", font=("Calibri", 15), bg ="white")
	timing_label.grid(row=4, column=0, sticky="W")
	timing_options = tk.OptionMenu(settings, temptiming, *timings)
	timing_options.grid(row=5, sticky="W", padx=5)


	exitbtn_frame = tk.Frame(settings, bg="white", pady=10)
	cancel_btn = tk.Button(exitbtn_frame, command=cancel_clicked, text="Cancel", font=("Calibri", 12), bg="white")
	cancel_btn.pack(side="left", padx=20)
	save_btn = tk.Button(exitbtn_frame, command=save_clicked, text="Save & Exit", font=("Calibri", 12), bg="white")
	save_btn.pack(side="left")
	exitbtn_frame.grid(row=6, sticky="S")