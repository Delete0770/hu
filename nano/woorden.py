import ast
import dutch_words
import os

cwd = os.getcwd()
print(cwd)

def kiezen(woorden_dict, moeilijkheidsgraad):
    '''
    De volgende code heb ik gebruikt om woorden te kiezen en een moeilijkheidsgraad toe te kennen aan de woorden. De moeilijkheidsgraad is gebaseerd op de hoogste letter frequentie in het woord en de lengte van het woord. Hoe hoger de frequentie en hoe langer het woord, hoe makkelijker het woord is. De moeilijkheidsgraad is een getal tussen 0 en 1, waarbij 0 betekent dat alle letters even vaak voorkomen en 1 betekent dat één letter in het woord voorkomt.
    '''
    # Returnt het random gekozen woord met meegegeven moeilijkheidsgraad
    pass


def lezen(bestandsnaam):
    # Leest alle woorden uit het woordenbestand en returnt een dictionary waarin het woord en diens moeilijkheid staat
    wordDict = {}
    try:
        with open(bestandsnaam, 'r') as file:
            inhoud = file.read()
            return ast.literal_eval(inhoud)
    except FileNotFoundError:
        print('file not found')
        return {}


def graad(word):
    highest = 0
    for letter in word:
        count = word.count(letter)
        if count > highest:
            highest = count
    return float(round(highest/len(word), 2))


def lijst():
    words = dutch_words.get_ranked()
    hangman_words = {}
    for word in words:
        highest = 0
        for letter in word:
            count = word.count(letter)
            if count > highest:
                highest = count
        hangman_words[word] = round(highest/len(word), 2) #*100

    print(hangman_words)

    with open(cwd + '/woordenCopy.txt', 'w') as file:
        file.write(str(hangman_words))
        #print(f"{word} has the highest letter frequency: {highest}")


def opslaan(bestandsnaam, woorden_lijst):
    # Schrijft de volledigde woordenlijst terug naar het bestand en returnt niets.
    try:
        with open(cwd + '/' + bestandsnaam, 'w') as file:
            # dict naar bestand
            for words in woorden_lijst:
                file.write(words + '\n')
    
    except TypeError:
        print('no wordlist to save')

    except FileNotFoundError:
        print('file not found')


def verwijderen(bestandsnaam, woord):
    woorden_dict = {}
    print(bestandsnaam)

    try:
        with open(cwd + '/' + bestandsnaam, 'r') as file:
            inhoud = file.read()
            woorden_dict = ast.literal_eval(inhoud)
            print(f"{woorden_dict}\n")
    except FileNotFoundError:
        print('file not found')

    # Schrijft de volledigde woordenlijst terug naar het bestand en returnt niets.
    if woord in woorden_dict:
        del woorden_dict[woord]
    else:
        print(f"woord '{woord}' niet gevonden in woordenlijst")

    try:
        with open(cwd + '/' + bestandsnaam, 'w') as file:
            # dict naar bestand
            #for words in woorden_lijst:
            #    file.write(words + '\n')
            file.write(str(woorden_dict))
    except TypeError:
        print('no wordlist to save')

    except FileNotFoundError:
        print('file not found')


def toevoegen(bestandsnaam, woord):
    woorden_dict = {}
    print(bestandsnaam)

    try:
        with open(cwd + '/' + bestandsnaam, 'r') as file:
            inhoud = file.read()
            woorden_dict = ast.literal_eval(inhoud)
            #print(f"{woorden_dict}\n")
    except FileNotFoundError:
        print('file not found')

    # Schrijft de volledigde woordenlijst terug naar het bestand en returnt niets.
    if woord in woorden_dict:
        print(f"woord '{woord}' zit al in woordenlijst")
    else:
        len_word = len(woord)
        woorden_dict[woord] = len_word
        print(f"woord '{woord}' toegevoegd aan woordenlijst")

    try:
        with open(cwd + '/' + bestandsnaam, 'w') as file:
            # dict naar bestand
            #for words in woorden_lijst:
            #    file.write(words + '\n')
            file.write(str(woorden_dict))
    except TypeError:
        print('no wordlist to save')
    except FileNotFoundError:
        print('file not found')