from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import datetime
import info

root = Tk()
root.title("Oscillazioni Celesti: Un Viaggio nelle Orbite")
root.iconbitmap('img/icon.ico')
width = 1300
height = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width)//2
y = (screen_height - height)//2
root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(False, False)

#fonts
import pyglet
pyglet.font.add_file('fonts/RubikSprayPaint-Regular.ttf')
pyglet.font.add_file('fonts/Roboto-VariableFont_wdth,wght.ttf')

#background
bg = PhotoImage(file='img/bg.png').subsample(2)
canvas = Canvas(root, width = 1100, height = 900)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0,0,image = bg, anchor = 'nw')

#title
canvas.create_text(414, 80, anchor = "n",
                   text="Orbite dei corpi celesti",
                   fill="white",
                   font=("Rubik Spray Paint", 42))

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
Label(form, text="Scegliere una data di inizio", font=("Roboto Regular", 15)).grid(row = 0, column = 0, pady = 10)
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
                    font=("Roboto Regular", 10))
calendar_start.grid(row = 1, column = 0, padx = 15)
Label(form, text="Scegliere una data di fine", font=("Roboto Regular", 15)).grid(row = 0, column = 1, pady = 10)
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
                    font=("Roboto Regular", 10))
calendar_stop.grid(row = 1, column = 1, padx = 15)

Label(form, text = "Selezionare i corpi celesti", font = ("Roboto Regular", 15)).grid(row = 2,
                                                                                       column = 0,
                                                                                       columnspan = 2,
                                                                                       pady = 30)
Checkbutton(form, variable = mercurio, text = "Mercurio", font = ("Roboto Regular", 13)).grid(row = 3, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = venere, text = "Venere", font = ("Roboto Regular", 13)).grid(row = 4, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = terra, text = "Terra", font = ("Roboto Regular", 13)).grid(row = 5, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = marte, text = "Marte", font = ("Roboto Regular", 13)).grid(row = 6, column = 0, sticky = "w", padx = 40)
Checkbutton(form, variable = giove, text = "Giove", font = ("Roboto Regular", 13)).grid(row = 7, column = 0, sticky = "w", padx = 40)

Checkbutton(form, variable = saturno, text = "Saturno", font = ("Roboto Regular", 13)).grid(row = 3, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = urano, text = "Urano", font = ("Roboto Regular", 13)).grid(row = 4, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = nettuno, text = "Nettuno", font = ("Roboto Regular", 13)).grid(row = 5, column = 1, sticky = "w", padx = 80)
Checkbutton(form, variable = luna, text = "Luna", font = ("Roboto Regular", 13)).grid(row = 6, column = 1, sticky = "w", padx = 80)



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
        selected = mercurio.get()+venere.get()+terra.get()+marte.get()+giove.get()+saturno.get()+urano.get()+nettuno.get()+luna.get()
        if selected == 0:
            messagebox.showerror("Errore!", "Selezionare almeno un corpo celeste")
        else:
            import script
            script.plot(start_date, stop_date, corpi_celesti, selected)

    


Button(form,
       text = "MOSTRA ORBITE",
       bg = "#002987",
       fg = "white",
       font = ("Roboto Bold", 18),
       activebackground = "#215dbf",
       command = exe,
       cursor = 'hand2').grid(row = 8,
                         column = 0,
                         columnspan = 2,
                         sticky="we",
                         padx = 30,
                         pady = 60)

button = PhotoImage(file='img/about.png')

about = Button(root,
               image = button,
               anchor = "se",
               bg = 'black',
               borderwidth=0,
               activebackground = 'black',
               cursor = 'hand2',
               command = info.window)
canvas.create_window(1248, 848, window = about)















root.mainloop()
