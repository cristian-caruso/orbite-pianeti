import subprocess
from matplotlib import pyplot as plt

print("La data deve essere del formato YYYY-MM-DD")
start = input("Inserisci una data da cui iniziare: ")
stop = input("Inserisci una data in cui finire: ")
corpi_celesti = {
    "Mercurio": {"selected": "no",
                 "number_option": 1,
                 "number_horizon": 199,
                 },
    "Venere": {"selected": "no",
                 "number_option": 2,
                 "number_horizon": 299,
                 },
    "Terra": {"selected": "no",
                 "number_option": 3,
                 "number_horizon": 399,
                 },
    "Marte": {"selected": "no",
                 "number_option": 4,
                 "number_horizon": 499,
                 },
    "Giove": {"selected": "no",
                 "number_option": 5,
                 "number_horizon": 599,
                 },
    "Saturno": {"selected": "no",
                 "number_option": 6,
                 "number_horizon": 699,
                 },
    "Urano": {"selected": "no",
                 "number_option": 7,
                 "number_horizon": 799,
                 },
    "Nettuno": {"selected": "no",
                 "number_option": 8,
                 "number_horizon": 899,
                 },
    "Luna": {"selected": "no",
                 "number_option": 9,
                 "number_horizon": 301,
                 }
    }
while True:
    print("Selezionare un corpo celeste:")
    for body in corpi_celesti:
        if corpi_celesti[body]["selected"] == "yes":
            print("[X] - " + body)
        else:
            print("[ ] - " + body)
    print("Premere G per il grafico")
    option = input("Inserire l'opzione: ")
    if option == 'G':
        break
    if corpi_celesti[option]["selected"] == "no":
        corpi_celesti[option]["selected"] = "yes"
    else:
        corpi_celesti[option]["selected"] = "no"

for body in corpi_celesti:
    if corpi_celesti[body]["selected"] == "yes":
        address = 'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27' + str(corpi_celesti[body]["number_horizon"]) + '%27&OBJ_DATA=%27YES%27&EPHEM_TYPE=%27VECTORS%27&CSV_FORMAT=%27YES%27&START_TIME=%27' + start + '%27&STOP_TIME=%27' + stop + '%27&STEP_SIZE=%271%20d%27'
        sp = subprocess.Popen(['wget.exe', '-O', 'data', address])

        if sp.wait()!=0:
            import sys
            sys.exit(2)

        fhand = open('data','r')
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

        plt.plot(data_x, data_y)

plt.show()
