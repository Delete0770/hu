import os
import random
import dutch_words
import woorden
import score

wordDict = {}
wordDict = woorden.lezen('/Users/david/Documents/github/hu/nano/woorden.txt')
for word in wordDict:
    wordDict[word] = len(word)

wordDict = dict(sorted(wordDict.items(), key=lambda item: item[1]))

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
            print(l, end="")
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
    score = lifes * int(hardness)
    print(f"woord: {word}, Score: {score}")
    

    if done == len(word):
        print("Gefeliciteerd, je hebt het woord geraden!")
    if lifes == 0:
        print("Helaas, je hebt geen levens meer over.")
    print("GAME OVER")


def menu():
    while True:
        #lees_woorden('woorden.txt')
        print("=== Galgje Controller ===\n",
            "Kies een optie: \n",
            "1. Speel galgje\n",
            "2. Wijzig een woord in de woordenlijst\n",
            "3. Voeg woord toe aan de woordenlijst\n",
            "4. Toon aantal woorden in de woordenlijst\n",
            "5. Stoppen\n")

        var = input(">> ")

        if var == "1":
            speel_sessie()
        if var == "2":
            #changeWord()
            pass
        if var == "3":
            var2 = input("Kies een wooord om toe te voegen: ")
            print(f"variabele var2 bevat > {var2} en is het type {type(var2)}\n")
            print(f"de functie woorden.graad(var2) returned > {woorden.graad(var2)} en is het type {type(woorden.graad(var2))}\n")
            wordDict[var2] = float(woorden.graad(var2))
            print(f"woord {var2} toegevoegd met moeilijkheidsgraad {wordDict[var2]}")
            #sla_woorden_op('woorden.txt', var2)
        if var == "4":
            lenWL = len(wordDict)
            print(f"Aantal woorden in woordenbestand: {lenWL}\n")
        if var == "5":
            print("GAME OVER")
            break
    #return var

if __name__ == "__main__": 
    menu()

'''
print(f"WordList: {wordDict}\n")

woorden.opslaan('woorden2.txt', wordDict)
woorden.toevoegen('David', "woord", '1000')
speel_sessie()




dutch_words.bereken_score(aantal_levens_over, moeilijkheid)
dutch_words.voeg_score_toe()

woorden.kiezen(woorden_dict, moeilijkheidsgraad)
woorden.lezen(bestandsnaam)
woorden.lijst()
woorden.opslaan(bestandsnaam, woorden_lijst)

score.bereken(aantal_levens_over, moeilijkheid)
score.toevoegen(naam, woord, score)
score.toon_tussenstand(woord, geraden_letters)
'''
