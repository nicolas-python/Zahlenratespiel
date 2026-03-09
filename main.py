#Zahlenratespiel
import random


#zahl zufällig generieren
def zahlgenerator():

    zahlen_liste = ["1","2","3","4","5","6","7","8","9","10",
                     "11","12","13","14","15","16","17","18","19","20","21"]

    zufallzahl = random.choice(zahlen_liste)
    return int(zufallzahl)


#funktion aufrufen
zufallzahl = zahlgenerator()

def abgleich():
    while True:
        print("Bitte geben Sie eine Zahl von 1-21 ein.")
        spielerzahl = int(input("Zahl eingeben:"))          #int: da nur ganze zahlen
        print("Sie haben sich für", spielerzahl, "entschieden.")

        if spielerzahl == zufallzahl:
            print("richtig score + 1")
            break

        elif spielerzahl < zufallzahl:
            print("Sie sind zu niedrig , die Zahl ist höher")

        elif spielerzahl > zufallzahl:
            print("Sie sind zu hoch die Zahl ist niedriger")

abgleich()


