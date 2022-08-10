# Calculator
# # Info on Tkinter
# https://realpython.com/python-gui-tkinter/

# Import only Tk (interface), Widgets - Entry (text input) and Buttons
from ast import Expression
from tkinter import Tk, Entry, Button

gui = Tk()
gui.configure(background="light green")
gui.title("Calculator - Jinsoo")
gui.geometry("400x400-0+0")




# Interface Variables
rows = 7
cols = 3
fg = "black"
bg = "white smoke"
ft = "Calibri 14"


# Build Graphical User Interface
# Text Input
calc_input = Entry(gui, fg="light green", bg="black", font=ft, justify="right")
calc_input.place(relw=1, relh=1/rows)

# Buttons
Button(gui, text="1", fg=fg, bg=bg, font=ft, command=lambda:btn_click("1")).place(relw=1/cols,relh=1/rows, relx=0,rely=1/rows)
Button(gui, text="2", fg=fg, bg=bg, font=ft, command=lambda:btn_click("2")).place(relw=1/cols,relh=1/rows, relx=1/cols,rely=1/rows)
Button(gui, text="3", fg=fg, bg=bg, font=ft, command=lambda:btn_click("3")).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=1/rows)

Button(gui, text="4", fg=fg, bg=bg, font=ft, command=lambda:btn_click("4")).place(relw=1/cols,relh=1/rows, relx=0,rely=2/rows)
Button(gui, text="5", fg=fg, bg=bg, font=ft, command=lambda:btn_click("5")).place(relw=1/cols,relh=1/rows, relx=1/cols,rely=2/rows)
Button(gui, text="6", fg=fg, bg=bg, font=ft, command=lambda:btn_click("6")).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=2/rows)

Button(gui, text="7", fg=fg, bg=bg, font=ft, command=lambda:btn_click("7")).place(relw=1/cols,relh=1/rows, relx=0,rely=3/rows)
Button(gui, text="8", fg=fg, bg=bg, font=ft, command=lambda:btn_click("8")).place(relw=1/cols,relh=1/rows, relx=1/cols,rely=3/rows)
Button(gui, text="9", fg=fg, bg=bg, font=ft, command=lambda:btn_click("9")).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=3/rows)

Button(gui, text="+", fg=fg, bg=bg, font=ft, command=lambda:btn_click("+")).place(relw=1/cols,relh=1/rows, relx=0,rely=4/rows)
Button(gui, text="0", fg=fg, bg=bg, font=ft, command=lambda:btn_click("0")).place(relw=1/cols,relh=1/rows, relx=1/cols,rely=4/rows)
Button(gui, text="-", fg=fg, bg=bg, font=ft, command=lambda:btn_click("-")).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=4/rows)

Button(gui, text="x", fg=fg, bg=bg, font=ft, command=lambda:btn_click("x")).place(relw=1/cols,relh=1/rows, relx=0,rely=5/rows)
Button(gui, text="/", fg=fg, bg=bg, font=ft, command=lambda:btn_click("/")).place(relw=1/cols,relh=1/rows, relx=1/cols,rely=5/rows)
Button(gui, text=".", fg=fg, bg=bg, font=ft, command=lambda:btn_click(".")).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=5/rows)

Button(gui, text="=", fg="white", bg="blue", font=ft, command=lambda: calculate()).place(relw=2/cols,relh=1/rows, relx=0,rely=6/rows)
Button(gui, text="C", fg="white", bg="red", font=ft, command=lambda:clear()).place(relw=1/cols,relh=1/rows, relx=2/cols,rely=6/rows)


# Numbers



# Interface functions
def btn_click(char):
    text = calc_input.get()
    calc_input.insert(len(text), char)

def clear():
    text = calc_input.get()
    calc_input.delete(0, len(text))

def calculate():
    expression = calc_input.get().replace("x","*")
    result = str(eval(expression))
    clear()
    calc_input.insert(0,result)

def fix_error(text):
    text
# Set everything up


gui.mainloop()