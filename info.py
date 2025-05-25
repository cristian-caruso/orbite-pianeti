from tkinter import *

def window():
    info = Tk()
    iwidth = 700
    iheight = 500
    info.geometry(f'{iwidth}x{iheight}')
    info.title("Informazioni sui corpi celesti")
    info.iconbitmap("img/about.ico")
    info.resizable(False, False)

    import pyglet
    pyglet.font.add_file('fonts/RubikSprayPaint-Regular.ttf')
    pyglet.font.add_file('fonts/Roboto-VariableFont_wdth,wght.ttf')

    Label(info, text="Informazioni sui corpi celesti", font=("Rubik Spray Paint", 20)).grid(row=0,
                                                                                          column=1,
                                                                                          sticky = 'ew',
                                                                                          pady = 40)

    Label(info, text="Corpo celeste", font=("Roboto Regular", 13, 'bold')).grid(row=1, column=0, sticky="w", padx = 10)
    Label(info, text="Periodo di rivoluzione", font=("Roboto Regular", 13, 'bold')).grid(row=1, column=1)
    Label(info, text="Velocità", font=("Roboto Regular", 13, 'bold')).grid(row=1, column=2, sticky="e", padx = 30)

    Label(info, text="Mercurio", font=("Roboto Regular", 13)).grid(row=2, column=0, sticky="w", padx = 30)
    Label(info, text="87,97 giorni", font=("Roboto Regular", 13)).grid(row=2, column=1, padx = 30)
    Label(info, text="47,36 km/s", font=("Roboto Regular", 13)).grid(row=2, column=2, sticky="e", padx = 30)

    Label(info, text="Venere", font=("Roboto Regular", 13)).grid(row=3, column=0, sticky="w", padx = 30)
    Label(info, text="224,7 giorni", font=("Roboto Regular", 13)).grid(row=3, column=1, padx = 30)
    Label(info, text="35,02 km/s", font=("Roboto Regular", 13)).grid(row=3, column=2, sticky="e", padx = 30)

    Label(info, text="Terra", font=("Roboto Regular", 13)).grid(row=4, column=0, sticky="w", padx = 30)
    Label(info, text="1 anno", font=("Roboto Regular", 13)).grid(row=4, column=1, padx = 30)
    Label(info, text="29,78 km/s", font=("Roboto Regular", 13)).grid(row=4, column=2, sticky="e", padx = 30)

    Label(info, text="Marte", font=("Roboto Regular", 13)).grid(row=5, column=0, sticky="w", padx = 30)
    Label(info, text="1,88 anni", font=("Roboto Regular", 13)).grid(row=5, column=1, padx = 30)
    Label(info, text="24,08 km/s", font=("Roboto Regular", 13)).grid(row=5, column=2, sticky="e", padx = 30)

    Label(info, text="Giove", font=("Roboto Regular", 13)).grid(row=6, column=0, sticky="w", padx = 30)
    Label(info, text="11,86 anni", font=("Roboto Regular", 13)).grid(row=6, column=1, padx = 30)
    Label(info, text="13,06 km/s", font=("Roboto Regular", 13)).grid(row=6, column=2, sticky="e", padx = 30)

    Label(info, text="Saturno", font=("Roboto Regular", 13)).grid(row=7, column=0, sticky="w", padx = 30)
    Label(info, text="29,45 anni", font=("Roboto Regular", 13)).grid(row=7, column=1, padx = 30)
    Label(info, text="9,64 km/s", font=("Roboto Regular", 13)).grid(row=7, column=2, sticky="e", padx = 30)

    Label(info, text="Urano", font=("Roboto Regular", 13)).grid(row=8, column=0, sticky="w", padx = 30)
    Label(info, text="84,07 anni", font=("Roboto Regular", 13)).grid(row=8, column=1, padx = 30)
    Label(info, text="6,81 km/s", font=("Roboto Regular", 13)).grid(row=8, column=2, sticky="e", padx = 30)

    Label(info, text="Nettuno", font=("Roboto Regular", 13)).grid(row=9, column=0, sticky="w", padx = 30)
    Label(info, text="164,88 anni", font=("Roboto Regular", 13)).grid(row=9, column=1, padx = 30)
    Label(info, text="5,43 km/s", font=("Roboto Regular", 13)).grid(row=9, column=2, sticky="e", padx = 30)

    Label(info, text="Luna", font=("Roboto Regular", 13)).grid(row=10, column=0, sticky="w", padx = 30)
    Label(info, text="27,32 giorni", font=("Roboto Regular", 13)).grid(row=10, column=1, padx = 30)
    Label(info, text="1,02 km/s", font=("Roboto Regular", 13)).grid(row=10, column=2, sticky="e", padx = 30)


    Button(info,
           text = "CHIUDI",
           bg = "#002987",
           fg = "white",
           font = ("Roboto Bold", 18),
           activebackground = "#215dbf",
           command = info.destroy,
           cursor = 'hand2').grid(row = 11,
                             column = 1,
                             sticky="we",
                             padx = 30,
                             pady = 60)
