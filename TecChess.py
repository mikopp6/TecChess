from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main_menu = Tk()
main_menu.title("TecChess")
main_menu.geometry("600x600")
main_menu.configure(bg="white")

logo = PhotoImage(file="logo.png")
label = Label(image=logo)
label.place(relx=0.5, rely=0.16, anchor=CENTER)

def newgame_clicked():
	newgame = Tk()
	newgame.title("TecChess - New game")
	newgame.geometry("700x500")
	chessboard = PhotoImage(file="chessboard.png")
	label = Label(image=chessboard)
	label.place(relx=0.5, rely=0.16, anchor=CENTER)
	newgame.mainloop()

def settings_clicked():
	settings = Tk()
	settings.title("TecChess - Settings")
	settings.geometry("700x500")
	settings.mainloop()

def help_clicked():
	help_menu = Tk()
	help_menu.title("TecChess - Help")
	
	treeview = ttk.Treeview(help_menu)
	treeview.pack()

	with open("helptext.txt", "r", encoding="utf-8") as f:
		for line in f:
			if line[0].isdigit():
				if line[2].isdigit():
					treeview.insert(line[0], line)
				else:
					treeview.insert(line[0], line)
			else:
				treeview.insert(line[0], line)
			

def exit_clicked():
	if(messagebox.askyesno("Exit","Are you sure?", parent=main_menu, default="no")):
		main_menu.destroy()

new_game = Button(main_menu, command=newgame_clicked, text="New game", font=("Emilbus Mono", 25), bg ="white")
new_game.place(relx=0.5, rely=0.4, anchor=CENTER)

settings_button = Button(main_menu, command=settings_clicked, text="Settings", font=("Emilbus Mono", 25), bg ="white")
settings_button.place(relx=0.5, rely=0.55, anchor=CENTER)

help_button = Button(main_menu, command=help_clicked, text="Help", font=("Emilbus Mono", 25), bg ="white")
help_button.place(relx=0.5, rely=0.7, anchor=CENTER)

exit_button = Button(main_menu, command=exit_clicked, text="Exit game", font=("Emilbus Mono", 25), bg ="white")
exit_button.place(relx=0.5, rely=0.85, anchor=CENTER)

main_menu.mainloop()