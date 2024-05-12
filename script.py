import subprocess
import time
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox


def plot(start, stop, corpo, corpi_celesti, selected):  
    directory = "datas/data"
    loading_var = 0
    address = 'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27' + str(corpi_celesti[corpo]["number_horizon"]) + '%27&OBJ_DATA=%27YES%27&EPHEM_TYPE=%27VECTORS%27&CENTER=%27@sun%27&CSV_FORMAT=%27YES%27&START_TIME=%27' + start + '%27&STOP_TIME=%27' + stop + '%27&STEP_SIZE=%271%20d%27'
    sp = subprocess.Popen(['wget.exe', '-O', directory, address])

    if sp.wait()!=0:
        import sys
        sys.exit(2)

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

    return (data_x, data_y)
