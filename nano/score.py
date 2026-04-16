
def bereken(aantal_levens_over, moeilijkheid):
    # Berekent de score: aantal_levens_over * moeilijkheid.
    score = int(aantal_levens_over) * int(moeilijkheid)
    return score


def toevoegen(naam, woord, score):
    with open('score.txt', 'a') as file:
        file.write(f"{naam} " + f"{woord} " + f"{score}\n")
    # Voegt score van gebruiker toe aan het bestand.