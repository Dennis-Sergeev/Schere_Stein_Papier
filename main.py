import random

#Anzahl der Runden
match_count = int(input("Wählen sie eine beliebige Anzahl an Spielen aus: "))

#Gespielte Runden
played_games = 0

#Wenn die gespielte Rundenanzahl kleiner ist als die ausgewählte Rundenanzahl, spielt man weiter
while played_games < match_count:

    #Der PC wählt eine Spielmöglichkeit aus
    pc_random = random.randint(0,2)

    #Konvertiert die Spielmöglichkeit des PCs in ein Wort
    if(pc_random == 0):
        pc_choice = "Schere"
    elif(pc_random == 1):
        pc_choice = "Stein"
    else:
        pc_choice = "Papier"

    #Kontroliert, dass die Wahl richtig geschrieben wird
    nummbers_of_controls = 0
    while(nummbers_of_controls < 1):
        choice = input("Schere, Stein oder Papier? ")
        #if choice not in ["Schere", "Stein", "Papier"]:
        if (choice != "Schere" and choice != "Stein" and choice != "Papier"):
            print("")
            print("Ihre Auswahl ist falsch geschrieben, geben sie es bitte erneut ein!")
            print("")
        else:
            nummbers_of_controls += 1

    #Logik des Spiels (wer gewinnt und verliert)
    if(pc_choice == choice):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Unentschieden|")

    elif((pc_choice == "Stein") & (choice == "Schere")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliert|")

    elif((pc_choice == "Schere") & (choice == "Papier")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliert|")

    elif((pc_choice == "Papier") & (choice == "Stein")):
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler verliert|")

    else:
        print("Pc nimmt [" + pc_choice + "] und Spieler [" + choice + "] = |Spieler gewinnt|")

    #Anzahl gespielter runden + 1
    played_games += 1

    #Zeigt dem Spieler an, wie viele Runden noch dem Spieler zur Verfügung stehen
    print("")
    print("Du hast schon [" + str(played_games) + "] von [" + str(match_count) + "] Runden gespielt, dir blieben noch [" + str(match_count - played_games) + "] Runden!")
    print("")