#Zahlenratespiel
import random
spieler = None

# menü
def menue():
    choice = None

    while choice not in ["1","2","3"]:
        print("1 : Spieler Erstellen")
        print("2 : Spielen")
        print("3 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:", choice)

        if choice not in ["1","2","3"]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3  wählen.")

    return choice

#funktion aufrufen
#zahl zufällig generieren
def zahlgenerator():

    zahlen_liste = ["1","2","3","4","5","6","7","8","9","10",
                     "11","12","13","14","15","16","17","18","19","20","21"]

    zufallzahl = random.choice(zahlen_liste)
    return int(zufallzahl)


def abgleich(zufallzahl):
    while True:
        print("Bitte geben Sie eine Zahl von 1-21 ein.")
        spielerzahl = int(input("Zahl eingeben:"))          #int: da nur ganze zahlen
        print("Sie haben sich für", spielerzahl, "entschieden.")

        if spielerzahl == zufallzahl:
            print("richtig score + 1")
            weiter = input("Weiter spielen (y/n):")

            if weiter == "y":
                return

            elif weiter == "n":
                break

        elif spielerzahl < zufallzahl:
            print("Sie sind zu niedrig , die Zahl ist höher")

        elif spielerzahl > zufallzahl:
            print("Sie sind zu hoch die Zahl ist niedriger")

def spieler_erstellen():
    name = input("Wähle eine Namen:")
    print("Du hast den Namen :",name,"gewählt")
    return name

while True:
    wahl = menue()

    if wahl == "1":
        print("Spieler erstellen ")
        spieler = spieler_erstellen()

    elif wahl == "2":
        print("Spielen")

        if spieler == None:
            print("Namen erstellen")

        else:
            print("Spieler:",spieler)
            zufallzahl = zahlgenerator()
            abgleich(zufallzahl)

    elif wahl == "3":
        print("Spiel beendet")
        break

