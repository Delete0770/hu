import random

# Maak aantal_pogingen global
global moeilijkheidsgraad

# Functies:
def genereer_getal(moeilijkheid):
    getal = 0
    if moeilijkheid == 1:
        getal = 10
        getal = random.randint(1, getal)
    elif moeilijkheid == 2:
        getal = 50
        getal = random.randint(1, getal)
    elif moeilijkheid == 3:
        getal = 100
        getal = random.randint(1, getal)
    return getal


def max_pogingen(moeilijkheid):
    pogingen = 0
    if moeilijkheid == 1:
        maxPogingen = 5
    elif moeilijkheid == 2:
        maxPogingen = 7
    elif moeilijkheid == 3:
        maxPogingen = 10
    return maxPogingen


def inputLoop(poging):
    global app
    try:
        m = int(input(f"dit is poging {poging + 1}. Raad een getal van 1 t/m 10: "))
    except ValueError:
        app = False
            #print("Probeer het nog eens...")
    return m


def score(moeilijkheidsgraad, aantal_pogingen):
    eindScore = aantal_pogingen * moeilijkheidsgraad
    # score = (max_pogingen - gebruikte_pogingen) * moeilijkheidsgraad
    return eindScore


def advies_moeilijkheidsgraad(score):
    if score < 5:
        print("Probeer een lagere moeilijkheidsgraad.")
    elif score <= 12 and score >= 5:
        print("Houd deze moeilijkheidsgraad aan.")
    else:
        print("Je kunt een hogere moeilijkheidsgraad aan!")


def spelerInput():
    # global app
    spelerNaam = input("Speler: ")
    if spelerNaam == "":
        print("GAME OVER")
        exit()
    #if not spelerNaam:
    #    app = False


def menu():
    # global app
    global moeilijkheidsgraad
    moeilijkheidsgraad = input(
        "1 (makkelijk): getal raden 1-10\n"
        "2 (normaal): getal raden 1-50\n"
        "3 (moeilijk): getal raden 1-100\n\n"
        "Voer een keus in: ")
    try:
        moeilijkheidsgraad = int(moeilijkheidsgraad)
    except ValueError:
        print("GAME OVER")
        exit()


def raad_het_nummer():
    global moeilijkheidsgraad
    if moeilijkheidsgraad == 1:
        max_pogingen = 5
        aantal_pogingen = 0
        n = random.randint(1, 11)
        print("Je hebt 5 pogingen.")
    elif moeilijkheidsgraad == 2:
        max_pogingen = 7
        aantal_pogingen = 0
        n = random.randint(1, 51)
        print("Je hebt 7 pogingen.")

    elif moeilijkheidsgraad == 3:
        max_pogingen = 10
        aantal_pogingen = 0
        n = random.randint(1, 101)
        print("Je hebt 10 pogingen.")

    for poging in range(max_pogingen):
        m = inputLoop(poging)
        if m is None:
            return
        elif m == n:
            print("Goed!!!")
            aantal_pogingen += 1
            break
        else:
            if m + 1 == n or m - 1 == n:
                print("Bijna!")
            elif m < n:
                print("Hoger.")
            elif m > n:
                print("Lager.")
            else:
                print("Geen getal?")
            aantal_pogingen += 1
    new_score = (max_pogingen * moeilijkheidsgraad) - score(moeilijkheidsgraad, aantal_pogingen)
    # score = (max_pogingen - gebruikte_pogingen) * moeilijkheidsgraad
    print(f"Je score is {new_score}")
    return new_score

#main loop
def appLoop():
    while True:
        spelerInput()
        moeilijkheidsgraad = menu()
        score = raad_het_nummer()
        genereer_getal(moeilijkheidsgraad)
        advies_moeilijkheidsgraad(score)
        print("GAME OVER")
        exit()

# run
appLoop()