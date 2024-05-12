from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from matplotlib import pyplot as plt
import datetime
import script

root = Tk()
root.title("Orbite dei corpi celesti")
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
canvas.create_text(414, 100, anchor = "n",
                   text="Orbite dei corpi celesti",
                   fill="white",
                   font=("Space Crusaders", 42))

#variables
corpi_celesti = {
    "Mercurio": {"selected": 0,
                 "number_horizon": 199,
                 },
    "Venere": {"selected": 0,
                 "number_horizon": 299,
                 },
    "Terra": {"selected": 0,
                 "number_horizon": 399,
                 },
    "Marte": {"selected": 0,
                 "number_horizon": 499,
                 },
    "Giove": {"selected": 0,
                 "number_horizon": 599,
                 },
    "Saturno": {"selected": 0,
                 "number_horizon": 699,
                 },
    "Urano": {"selected": 0,
                 "number_horizon": 799,
                 },
    "Nettuno": {"selected": 0,
                 "number_horizon": 899,
                 },
    "Luna": {"selected": 0,
                 "number_horizon": 301,
                 }
    }

mercurio = IntVar()
venere = IntVar()
terra = IntVar()
marte = IntVar()
giove = IntVar()
saturno = IntVar()
urano = IntVar()
nettuno = IntVar()
luna = IntVar()


#form
form = Frame(root)
canvas.create_window(420,500,window=form)

#calendari
Label(form, text="Scegliere una data di inizio", font=("Nasalization Rg", 15)).grid(row = 0, column = 0, pady = 10)
calendar_start = Calendar(form,
                    selectmode = "day",
                    year=datetime.datetime.now().year,
                    month = datetime.datetime.now().month,
                    day = datetime.datetime.now().day-1,
                    background = "white",
                    borderwidth = 10,
                    locale = "it_IT",
                    date_pattern = "yyyy-mm-dd",
                    bordercolor = "white",
                    headersbackground = "#6bcbff",
                    headersforeground = "black",
                    foreground = "black",
                    selectbackground = "#21b1ff",
                    weekendbackground = "white",
                    weekendforeground = "black",
                    font=("Nasalization Rg", 10))
calendar_start.grid(row = 1, column = 0, padx = 15)
Label(form, text="Scegliere una data di fine", font=("Nasalization Rg", 15)).grid(row = 0, column = 1, pady = 10)
calendar_stop = Calendar(form, selectmode="day",
                    year=datetime.datetime.now().year,
                    month = datetime.datetime.now().month,
                    day = datetime.datetime.now().day,
                    date_pattern = "yyyy-mm-dd",
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
                    font=("Nasalization Rg", 10))
calendar_stop.grid(row = 1, column = 1, padx = 15)

Label(form, text = "Selezionare i corpi celesti", font = ("Nasalization Rg", 15)).grid(row = 2,
                                                                                       column = 0,
                                                                                       columnspan = 2,
                                                                                       pady = 30)
Checkbutton(form, variable = mercurio, text = "Mercurio", font = ("Nasalization Rg", 13)).grid(row = 3, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = venere, text = "Venere", font = ("Nasalization Rg", 13)).grid(row = 4, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = terra, text = "Terra", font = ("Nasalization Rg", 13)).grid(row = 5, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = marte, text = "Marte", font = ("Nasalization Rg", 13)).grid(row = 6, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = giove, text = "Giove", font = ("Nasalization Rg", 13)).grid(row = 7, column = 0, sticky = "w", padx = 40)

Checkbutton(form, variable = saturno, text = "Saturno", font = ("Nasalization Rg", 13)).grid(row = 3, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = urano, text = "Urano", font = ("Nasalization Rg", 13)).grid(row = 4, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = nettuno, text = "Nettuno", font = ("Nasalization Rg", 13)).grid(row = 5, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = luna, text = "Luna", font = ("Nasalization Rg", 13)).grid(row = 6, column = 1, sticky = "w", padx = 80)



def exe():
    start_date = calendar_start.get_date()
    stop_date = calendar_stop.get_date()
    if start_date >= stop_date:
        messagebox.showerror("Errore!", "Assicurati che la data di inizio preceda la data di fine")
    elif stop_date > str(datetime.datetime.now().strftime("%Y-%m-%d")):
        messagebox.showerror("Errore!", "Assicurati che la data di fine sia passata")
    else:
        corpi_celesti["Mercurio"]["selected"] = mercurio.get()
        corpi_celesti["Venere"]["selected"] = venere.get()
        corpi_celesti["Terra"]["selected"] = terra.get()
        corpi_celesti["Marte"]["selected"] = marte.get()
        corpi_celesti["Giove"]["selected"] = giove.get()
        corpi_celesti["Saturno"]["selected"] = saturno.get()
        corpi_celesti["Urano"]["selected"] = urano.get()
        corpi_celesti["Nettuno"]["selected"] = nettuno.get()
        corpi_celesti["Luna"]["selected"] = luna.get()
        selected = mercurio.get() + venere.get()+terra.get()+marte.get()+giove.get()+saturno.get()+urano.get()+nettuno.get()+luna.get()
        if selected == 0:
            messagebox.showerror("Errore!", "Selezionare almeno un corpo celeste")
        else:
            loading_var = 0
            for corpo in corpi_celesti:
                if corpi_celesti[corpo]["selected"]:
                    values =script.plot(start_date, stop_date, corpo, corpi_celesti, selected)
                    data_x = values[0]
                    data_y = values[1]
                    loading_var += 1/selected*100
                    progressbar['value']=loading_var
                    root.update()
                    print(loading_var)
                    plt.plot(data_x, data_y)
            plt.show()
                    

    


Button(form,
       text = "MOSTRA ORBITE",
       bg = "#002987",
       fg = "white",
       font = ("Nasalization Rg", 18),
       activebackground = "#215dbf",
       command = exe).grid(row = 8,
                         column = 0,
                         columnspan = 2,
                         sticky="we",
                         padx = 30,
                         pady = 15)

s = ttk.Style()
s.theme_use('default')
s.configure("TProgressbar", background='#6bcbff', thickness=35)
progressbar = ttk.Progressbar(form, style = "TProgressbar")
progressbar.grid(row = 9,
                column = 0,
                columnspan = 2,
                sticky="we",
                padx = 30,
                pady = 20)















root.mainloop()
