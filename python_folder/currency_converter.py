# Calculator
from tkinter import Tk, Entry, Button, Label, PhotoImage

gui = Tk()
gui.configure(background="crimson")
gui.title("Currency Converter")
gui.geometry(f"270x270+{gui.winfo_screenwidth()-280}+0")

# Country Flags
can_img = PhotoImage(file="can.png")
usa_img = PhotoImage(file="usa.png")
eur_img = PhotoImage(file="eur.png")
jap_img = PhotoImage(file="jap.png")
chi_img = PhotoImage(file="chi.png")
phi_img = PhotoImage(file="phi.png")
ira_img = PhotoImage(file="ira.png")

# Interface Variables
c = 3
r = 8
ft = "Calibri 16 bold"
fg = "black"
bg = "white"


def convert():
	cad = float(can_input.get())
	usd = round(0.78*cad,2)	
	euro = round(0.76*cad,2)
	japanese_yen = round(104.81*cad,2)
	chinese_yuan = round(5.25*cad,2)
	philippine_peso = round(43.23*cad,2)
	iranian_rial = round(32883.74*cad,2)

	clear()
	
	can_input.insert(0,str(cad))
	usa_input.insert(0,str(usd))
	eur_input.insert(0,str(euro))
	jap_input.insert(0,str(japanese_yen))
	chi_input.insert(0,str(chinese_yuan))
	phi_input.insert(0,str(philippine_peso))
	ira_input.insert(0,str(iranian_rial))
	
	# this function should be called when the convert button
	# is clicked. It should take the value in the Canadian
	# Entry, convert it into the other currency values
	# and place those values into their respective Entry boxes

def clear():
	# pass is a holder. Remove pass when writing code in this function
    can_input.delete(0, len(can_input.get()))
    usa_input.delete(0, len(usa_input.get()))
    eur_input.delete(0, len(eur_input.get()))
    jap_input.delete(0, len(jap_input.get()))
    chi_input.delete(0, len(chi_input.get()))
    phi_input.delete(0, len(phi_input.get()))
    ira_input.delete(0, len(ira_input.get()))

	# this function should clear all the Entries in the app
	# of any values


# Graphical User Interface
# 
# Buttons
btn_convert = Button(gui, text="Convert", fg=fg, bg=bg, font=ft,command=lambda:convert())
btn_convert.place(relw=2/c, relh=1/r, relx=0,   rely=1/r)

btn_clear = Button(gui, text="C", fg=fg, bg=bg, font=ft, command=lambda:clear())
btn_clear.place(relw=1/c, relh=1/r, relx=2/c,   rely=1/r)


# Flag Labels and Entries
can_flag = Label(gui, image=can_img)
can_flag.place(relw=1/c, relh=1/r, relx=0, rely=0)
can_input = Entry(gui, fg="black", bg="light green", bd=5, font=ft)
can_input.place(relw=2/c, relh=1/r, relx=1/c, rely=0)


usa_flag = Label(gui, image=usa_img)
usa_flag.place(relw=1/c, relh=1/r, relx=0, rely=2/r)
usa_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
usa_input.place(relw=2/c, relh=1/r, relx=1/c, rely=2/r)

eur_flag = Label(gui, image=eur_img)
eur_flag.place(relw=1/c, relh=1/r, relx=0, rely=3/r)
eur_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
eur_input.place(relw=2/c, relh=1/r, relx=1/c, rely=3/r)

jap_flag = Label(gui, image=jap_img)
jap_flag.place(relw=1/c, relh=1/r, relx=0, rely=4/r)
jap_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
jap_input.place(relw=2/c, relh=1/r, relx=1/c, rely=4/r)

chi_flag = Label(gui, image=chi_img)
chi_flag.place(relw=1/c, relh=1/r, relx=0, rely=5/r)
chi_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
chi_input.place(relw=2/c, relh=1/r, relx=1/c, rely=5/r)

phi_flag = Label(gui, image=phi_img)
phi_flag.place(relw=1/c, relh=1/r, relx=0, rely=6/r)
phi_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
phi_input.place(relw=2/c, relh=1/r, relx=1/c, rely=6/r)

ira_flag = Label(gui, image=ira_img)
ira_flag.place(relw=1/c, relh=1/r, relx=0, rely=7/r)
ira_input = Entry(gui, fg=fg, bg=bg, bd=5, font=ft)
ira_input.place(relw=2/c, relh=1/r, relx=1/c, rely=7/r)


gui.mainloop()
