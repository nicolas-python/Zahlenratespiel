#Zahlenratespiel
import random


#zahl zufällig generieren
def zahlgenerator():

    zahlen_liste = ["1","2","3","4","5","6","7","8","9","10",
                     "11","12","13","14","15","16","17","18","19","20","21"]

    zufallzahl = random.choice(zahlen_liste)
    print(zufallzahl)


#funktion aufrufen
zahlgenerator()
