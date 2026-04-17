import os
import random
import dutch_words
import woorden
import score

cwd = os.getcwd()
file_var = 'woordenCopy.txt'
path = cwd + '/' + file_var

wordDict = {}
wordDict = woorden.lezen(path)

for word in wordDict:
    wordDict[word] = len(word)

wordDict = dict(sorted(wordDict.items(), key=lambda item: item[1]))

def save_score(name, word, score):
        # slaat naam, woord en score op in een bestand scores.txt
    try:
        with open(cwd + '/scores.txt', 'a') as file:
            file.write(f"{name} | {word} | {score}\n")
    except FileNotFoundError:
        print('file not found\n')
        print('create new file\n')

        '''with open(cwd + '/scores.txt', 'x') as file:
            file.write(f"name | word | score\n{name} | {word} | {score}\n")'''


def toon_tussenstand(woord, geraden_letters):
    """
    Toont de gerade letters als volgt V _ _ R _ E E L D van het woord "voorbeeld"
    Returnt de string met gerade letters als bovenstaand voorbeeld
    :param woord:
    :param geraden_letters:
    :return:
    """
    for l in woord:
        if l in geraden_letters:
            print(l.upper(), end="")
        else:
            print("_", end="")


def speel_sessie():
    """
    Vraagt om de moeilijkheidsgraad
    Kiest een random woord met de juiste moeilijkheidsgraad
    Laat gebruiker raden via console
    Houdt pogingen bij
    Logt resultaat van gebruiker in het scorebestand
    :return:
    """

    tries = 0
    level = input('Moeilijkheidsgraad: ')
    word, hardness = random.choice(list(wordDict.items()))
    lifes = 0
    hidden = []
    previous = []
    done = 0
    fout = []
    
    if level == "1":
        while hardness > 6: 
            word, hardness = random.choice(list(wordDict.items()))
        lifes = 10
    elif level == "2":
        while hardness < 7 and hardness > 11:
            word, hardness = random.choice(list(wordDict.items()))
        lifes = 8
    elif level == "3":
        while hardness < 11:
            word, hardness = random.choice(list(wordDict.items()))
        lifes = 6
    
    print(word, hardness)
    word = word.lower()

    for letter in word:
        hidden.append("_")
    
    while done < len(word) and lifes > 0:
        print("".join(hidden))
        guess = input('Raad een letter: ').lower()
        
        if guess == "":
            print("GAME OVER")
            break
        elif guess in previous:
            print("Al geraden, maar je verliest geen levens.")
        else:
            if guess in word:
                print("Goed!")
                for letter in range(len(word)):
                    if word[letter] == guess:
                        hidden[letter] = guess
                done += 1
            else:
                lifes -= 1
                print(f"Fout. Je hebt nog {lifes} over.")
                fout.append(guess)
                print()
            previous.append(guess)
        print(f"Foute letters: {fout}")
        tries += 1
    score = lifes * int(hardness)
    print(f"woord: {word}, Score: {score}")
    name = input("Save score. Voer je naam in: ")
    save_score(name, word, score)
    

    if done == len(word):
        print("Gefeliciteerd, je hebt het woord geraden!")
    if lifes == 0:
        print("Helaas, je hebt geen levens meer over.")
    
    print("GAME OVER")


def menu():
    while True:
        print("=== Galgje Controller ===\n",
            "Kies een optie: \n",
            "1. Speel galgje\n",
            "2. Verwijder een woord uit de woordenlijst\n",
            "3. Voeg woord toe aan de woordenlijst\n",
            "4. Toon aantal woorden in de woordenlijst\n",
            "5. Stoppen\n")

        var = input(">> ")

        if var == "1":
            speel_sessie()
        if var == "2":
            word_del = input("Kies een woord om te verwijderen: ")
            woorden.verwijderen(file_var, word_del)
        if var == "3":
            word_add = input("Kies een wooord om toe te voegen: ")
            woorden.toevoegen(file_var, word_add)
        if var == "4":
            lenWL = len(wordDict)
            print(f"Aantal woorden in woordenbestand: {lenWL}\n")
        if var == "5":
            print("GAME OVER")
            break
    #return var

if __name__ == "__main__": 
    menu()
