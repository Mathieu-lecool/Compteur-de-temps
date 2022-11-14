from time import localtime
from tkinter import *

app = Tk()
app.title("Compteur de temps")
app.resizable(0, 0)

mois_31 = (1,3,5,7,8,10,12)

def Calcul():
    MINUTE = int(minuteEntry.get())
    HEURE = int(heureEntry.get())
    JOUR = int(jourEntry.get())
    MOIS = int(moisEntry.get())
    ANNEE = int(anneeEntry.get())

    aujourdhui = localtime()

    minute = aujourdhui[4] - MINUTE
    if minute < 0: minute = 60 - abs(minute)

    heure = aujourdhui[3] - HEURE
    if heure < 0: heure = 24 - abs(heure)

    jour = aujourdhui[2] - JOUR
    if jour < 0:
        if aujourdhui[1] in mois_31: jourPlus = 1
        else: jourPlus = 0
        jour = (30 + jourPlus) - abs(jour)
        MOIS += 1

    mois = aujourdhui[1] - MOIS
    if mois < 0:
        mois = 12 - abs(mois)
        variable = str(mois) + " mois, "
        ANNEE += 1
    elif mois == 0: variable = ""
    else: variable = str(mois) + " mois, "

    annee = aujourdhui[0] - ANNEE
    if annee == 0: variable_annee = ""
    else: variable_annee = str(annee) + " ans, "

    resultat["text"] = f"Depuis {variable_annee}{variable}{jour} jour, {heure} heures et {minute} minutes"

Label(app, text="Compteur de temps", font=("Arial", 15)).grid(column=1, row=1, columnspan=5, pady=10, padx=5)

frame = Frame(app)

Label(frame, text="Année :").grid(row=2, column=1)
anneeEntry = Entry(frame, width=10, justify="center")
anneeEntry.grid(row=2, column=2, pady=2)

Label(frame, text="Mois :").grid(row=3, column=1)
moisEntry = Entry(frame, width=10, justify="center")
moisEntry.grid(row=3, column=2, pady=2)

Label(frame, text="Jour :").grid(row=4, column=1)
jourEntry = Entry(frame, width=10, justify="center")
jourEntry.grid(row=4, column=2, pady=2)

Label(frame, text="Heure :").grid(row=5, column=1)
heureEntry = Entry(frame, width=10, justify="center")
heureEntry.grid(row=5, column=2, pady=2)

Label(frame, text="Minute :").grid(row=6, column=1)
minuteEntry = Entry(frame, width=10, justify="center")
minuteEntry.grid(row=6, column=2, pady=2)

frame.grid(column=1, columnspan=5)

Button(app, text="Calculer", bg="lime", command=Calcul).grid(column=1, columnspan=5, pady=10)

resultat = Label(app, text="", font=("Arial", 11))
resultat.grid(column=1, columnspan=5, padx=5, pady=5)

app.mainloop()