from tkinter import *

from tkinter import messagebox

main_menu = Tk()
main_menu.title("TecChess")
main_menu.geometry("600x600")
main_menu.configure(bg="white")

image = PhotoImage(file="logo.png")
label = Label(image=image)
label.place(relx=0.5, rely=0.16, anchor=CENTER)

def newgame_clicked():
	newgame = Tk()
	newgame.title("TecChess - New game")
	newgame.geometry("700x500")
	newgame.mainloop()

def settings_clicked():
	settings = Tk()
	settings.title("TecChess - Settings")
	settings.geometry("700x500")
	settings.mainloop()

def help_clicked():
	help_menu = Tk()
	help_menu.title("TecChess - Help")
	help_menu.geometry("350x800")
	help_menu.mainloop()

def exit_clicked():
	if(messagebox.askyesno("Exit","Are you sure?")):
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