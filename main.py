# Zahlenratespiel
import random

spieler = None
score = 0
speichern = []


# score und spieler speichern und laden
def load_speichern():
    with open("speichern.txt", "r") as file:
        for save in file:
            speichern.append(save)

    return speichern

def save_speichern():
    with open("speichern.txt", "w") as file:
        for save in speichern:
            file.write(save)


# menü
def menue():
    choice = None

    while choice not in ["0","1", "2", "3","4"]:
        print("0 : Benutzer wählen")
        print("1 : Spieler Erstellen")
        print("2 : Spielen")
        print("3 : score anzeigen")
        print("4 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:", choice)

        if choice not in ["0","1", "2", "3","4"]:
            print("Ungültige Option, bitte erneut zwischen 0,1,2,3,4  wählen.")

    return choice


# funktion aufrufen
# zahl zufällig generieren
def zahlgenerator():
    zahlen_liste = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

    zufallzahl = random.choice(zahlen_liste)
    return int(zufallzahl)


def abgleich(zufallzahl):
    global score

    while True:

        try :
            spielerzahl = int(input("Zahl eingeben:"))

        except:
            print("Bitte nur Zahlen!")
            continue

        if spielerzahl < 1 or spielerzahl > 21 :
            print("Bitte geben Sie eine Zahl von 1-21 ein.")
            continue

        print("Sie haben sich für", spielerzahl, "entschieden.")

        if spielerzahl == zufallzahl:
            score += 1
            lines = load_speichern()
            score_liste = umwandeln_txt(lines)
            score_liste[spieler] = score
            speichern.clear()

            for user,score in score_liste.items():
                speichern.append(user + "=" + str(score) + "\n")

            print("richtig score :", score)
            weiter = input("Weiter spielen (y/n):")

            if weiter == "y":
                continue

            elif weiter == "n":
                break

        elif spielerzahl < zufallzahl:
            print("Sie sind zu niedrig , die Zahl ist höher")

        elif spielerzahl > zufallzahl:
            print("Sie sind zu hoch die Zahl ist niedriger")


def spieler_erstellen():
    global score
    name = input("Wähle eine Namen:")
    print("Du hast den Namen :", name, "gewählt")
    score = 0
    return name

def score_anzeigen():

    if len(speichern) == 0:
        print("Kein Score vorhanden")

    else:
        for scores in speichern:
            print(scores)

def benutzer_auswaehlen():

    print("Wähle einen Benutzer")
    lines = load_speichern()
    score_liste = umwandeln_txt(lines)

    for user in score_liste:
        print(user)
    benutzer = input("Welchen Benutzer ?")
    print("Du hast den Spieler:",benutzer, "gewählt")

    return benutzer

def umwandeln_txt(lines):
    speichern = {}
    for line in lines:
        line = line.strip()

        try:
            if line =="":
                continue

            spieler, score = line.split("=")
            speichern[spieler] = int(score)

        except ValueError:
            continue

    return speichern

load_speichern()

while True:
    wahl = menue()

    if wahl == "0":
        print("Benutzer auswählen")
        spieler = benutzer_auswaehlen()

    elif wahl == "1":
        print("Spieler erstellen ")
        spieler = spieler_erstellen()

    elif wahl == "2":
        print("Spielen")

        if spieler == None:
            print("Namen erstellen")

        else:
            print("Spieler:", spieler)
            zufallzahl = zahlgenerator()
            abgleich(zufallzahl)

    elif wahl == "3":
        score_anzeigen()

    elif wahl == "4":
        print("Spiel beendet")
        save_speichern()
        break
