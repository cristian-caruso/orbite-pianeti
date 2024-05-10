from tkinter import *
from tkcalendar import *
import datetime

root = Tk()
root.title("Orbite pianeti")
root.iconbitmap('img/icon.ico')
root.geometry('1300x900')
root.resizable(False, False)

#fonts
import pyglet
pyglet.font.add_file('fonts/title.ttf')
pyglet.font.add_file('fonts/scritte.otf')

#background
bg = PhotoImage(file='img/bg.png').subsample(2)
canvas = Canvas(root, width = 1100, height = 900)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0,0,image = bg, anchor = 'nw')

#title
canvas.create_text(500, 100, anchor = "n",
                   text="Orbite dei pianeti",
                   fill="white",
                   font=("Space Crusaders", 42))


#form
form = Frame(root)
canvas.create_window(420,500,window=form)

#calendari
Label(form, text="Scegliere una data di inizio", font=("Nasalization Rg", 15)).grid(row = 0, column = 0, pady = 10)
calendar_start = Calendar(form, selectmode="day",
                    year=datetime.datetime.now().year,
                    month = datetime.datetime.now().month,
                    day = datetime.datetime.now().day-1,
                    background = "white",
                    borderwidth = 10,
                    locale = "it_IT",
                    bordercolor = "white",
                    headersbackground = "#6bcbff",
                    headersforeground = "black",
                    foreground = "black",
                    selectbackground = "#21b1ff",
                    weekendbackground = "white",
                    weekendforeground = "black",
                    font=("Nasalization Rg", 10)).grid(row = 1, column = 0, padx = 15)
Label(form, text="Scegliere una data di fine", font=("Nasalization Rg", 15)).grid(row = 0, column = 1, pady = 10)
calendar_stop = Calendar(form, selectmode="day",
                    year=datetime.datetime.now().year,
                    month = datetime.datetime.now().month,
                    day = datetime.datetime.now().day,
                    background = "white",
                    borderwidth = 10,
                    locale = "it_IT",
                    bordercolor = "white",
                    headersbackground = "#6bcbff",
                    headersforeground = "black",
                    foreground = "black",
                    selectbackground = "#21b1ff",
                    weekendbackground = "white",
                    weekendforeground = "black",
                    font=("Nasalization Rg", 10)).grid(row = 1, column = 1, padx = 15)

Label(form, text = "Selezionare i corpi celesti", font = ("Nasalization Rg", 15)).grid(row = 2,
                                                                                       column = 0,
                                                                                       columnspan = 2,
                                                                                       pady = 30)
Checkbutton(form, text = "Mercurio", font = ("Nasalization Rg", 13)).grid(row = 3, column = 0, sticky = "w", padx = 20)
Checkbutton(form, text = "Venere").grid(row = 4, column = 0, sticky = "w")
Checkbutton(form, text = "Terra").grid(row = 5, column = 0, sticky = "w")
Checkbutton(form, text = "Marte").grid(row = 6, column = 0, sticky = "w")
Checkbutton(form, text = "Giove").grid(row = 7, column = 0, sticky = "w")

Checkbutton(form, text = "Saturno").grid(row = 3, column = 1, sticky = "w")
Checkbutton(form, text = "Urano").grid(row = 4, column = 1, sticky = "w")
Checkbutton(form, text = "Nettuno").grid(row = 5, column = 1, sticky = "w")
Checkbutton(form, text = "Luna").grid(row = 6, column = 1, sticky = "w")















root.mainloop()
