import ast
import dutch_words


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

    with open('/Users/david/Documents/github/hu/nano/woorden.txt', 'w') as file:
        file.write(str(hangman_words))
        #print(f"{word} has the highest letter frequency: {highest}")


def opslaan(bestandsnaam, woorden_lijst):
    # Schrijft de volledigde woordenlijst terug naar het bestand en returnt niets.
    try:
        with open(bestandsnaam, 'w') as file:
            # dict naar bestand
            for words in woorden_lijst:
                file.write(words + '\n')
    
    except TypeError:
        print('no wordlist to save')

    except FileNotFoundError:
        print('file not found')