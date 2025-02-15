import random

#anzahl der runden
match_count = int(input("Wählen sie eine beliebige anzahl an Spielen aus: "))

#gespielte runden
played_games = 0

#wen die gespielte rundenanzahl kleiner ist als die ausgewählte runden anzahl, spielt man weiter
while played_games < match_count:

    #Der Pc wählt eine spiel möglichkeit aus
    pc_random = random.randint(0,2)

    #Konvertiert die Spielmöglichkeit des Pc´s in ein Wort
    if(pc_random == 0):
        pc_choice = "Schere"
    elif(pc_random == 1):
        pc_choice = "Stein"
    else:
        pc_choice = "Papier"

    #Kontroliert das die wahl richtig geschrieben wird
    nummbers_of_controls = 0
    while(nummbers_of_controls < 1):
        choice = input("Schere, Stein oder Papier? ")
        #if choice not in ["Schere", "Stein", "Papier"]:
        if (choice != "Schere" and choice != "Stein" and choice != "Papier"):
            print("Ihre auswahl ist falsch geschrieben geben sie es bitte erneut ein")
        else:
            nummbers_of_controls += 1

    #Logik des Spiels (wer gewinnt und verliert)
    if(pc_choice == choice):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Unentschieden|")

    elif((pc_choice == "Stein") & (choice == "Schere")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliehrt|")

    elif((pc_choice == "Schere") & (choice == "Papier")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliehrt|")

    elif((pc_choice == "Papier") & (choice == "Stein")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliehrt|")

    else:
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler gewint|")

    #Anzahl gespielter runden + 1
    played_games += 1

    #Wie viel runden noch den spieler übrig stehen
    print("")
    print("Du hast schon [" + str(played_games) + "] von [" + str(match_count) + "] Runden gespielt, dir blieben noch [" + str(match_count - played_games) + "] !")
    print("")