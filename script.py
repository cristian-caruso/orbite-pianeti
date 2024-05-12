import subprocess
import time
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def plot(start, stop, corpi_celesti, selected):
    loading_window = Tk()
    width = 800
    height = 35
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()
    x = screen_width//2 - width//2
    y = screen_height//2 - height//2
    loading_window.geometry(f'{width}x{height}+{x}+{y}')
    loading_window.wm_attributes('-transparentcolor', 'red')
    loading_window.attributes('-topmost',True)
    loading_window.configure(bg = 'red')
    loading_window.overrideredirect(1)
    loading_window.resizable(False, False)
    s = ttk.Style(loading_window)
    s.theme_use('default')
    s.configure("TProgressbar", background='#6bcbff', thickness=height)
    progressbar = ttk.Progressbar(loading_window,
                                  style = "TProgressbar",
                                  length = width)
    progressbar.pack()
    loading_window.update()
    directory = "datas/data"
    loading_var = 0
    for corpo in corpi_celesti:
        if corpi_celesti[corpo]["selected"]:
            address = 'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27' + str(corpi_celesti[corpo]["number_horizon"]) + '%27&OBJ_DATA=%27YES%27&EPHEM_TYPE=%27VECTORS%27&CENTER=%27@sun%27&CSV_FORMAT=%27YES%27&START_TIME=%27' + start + '%27&STOP_TIME=%27' + stop + '%27&STEP_SIZE=%271%20d%27'
            sp = subprocess.Popen(['wget.exe', '-O', directory, address])

            if sp.wait()!=0:
                import sys
                loading_window.destroy()
                loading_window.update()
                messagebox.showerror("Errore!", "Errore di connessione, assicurarsi di essere connessi a internet o riprovare più tardi!")
                sys.exit()

            fhand = open(directory,'r')
            line = fhand.readline()
            while line !='$$SOE\n':
                line = fhand.readline()
            line = fhand.readline()
            data_x = []
            data_y = []

            while line!='$$EOE\n':
                line_data = line.split(',')
                data_x.append(float(line_data[2]))
                data_y.append(float(line_data[3]))
                line = fhand.readline()
            fhand.close()

            plt.plot(data_x, data_y, label = corpo)
            plt.legend()
            loading_var += 1/selected*100
            progressbar['value']=loading_var
            loading_window.update()
            if round(loading_var) >= 100:
                time.sleep(1)
                loading_window.destroy()

    plt.show()
