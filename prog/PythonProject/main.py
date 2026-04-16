
import random

def load():
    try:
        with open('resultaten.txt', 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print('file not found')


def rekensessie(bewerking, aantal, min, max):

    for n in range(int(aantal)):
        a = random.randint(min, max)
        b = random.randint(min, max)
        if bewerking == "+":
            c = a + b
            answer = input(f"{a} - {b} = ")
            if int(answer) == c:
                e = "Goed!"
            else:
                e = "Fout!"
        elif bewerking == "-":
            c = a - b
            answer = input(f"{a} - {b} = ")
            if int(answer) == c:
                e = "Goed!"
            else:
                e = "Fout!"
        elif bewerking == "*":
            c = a * b
            answer = input(f"{a} x {b} = ")
            if int(answer) == c:
                e = "Goed!"
            else:
                e = "Fout!"
        else:
            print('ERROR')
        #answer = input(f"{a} {choice_2} {b} = ")

        text.append(f"{a};{bewerking};{b};{c};{answer};{e}")
        string = f"{a};{bewerking};{b};{c};{answer};{e}"
        print(f"{a};{bewerking};{b};{c};{answer};{e}")

        # elif bewerking == "/":


def menu():
    # Use a breakpoint in the code line below to debug your script.
    print(f'1: Nieuwe rekensessie\n2: Foutrapport\n3: Reset')
    choice = input(">> ")# Press ⌘F8 to toggle the breakpoint.
    if choice == '1':
        print("Welk type rekensom?\n1: Plus\n2: Min")
        choice_2 = input(">> ")
        if choice_2 == '1':
            choice_2 == '+'
        elif choice_2 == '2':
            choice_2 == '-'
        elif choice_2 == '3':
            choice_2 == '*'
        print("Welk type rekensom?\n1: Makkelijk\n2: Moeillijk\n")
        choice_3 = input(">> ")
        if choice_3 == '1':
            min = 0
            max = 10
        else:
            min = -10
            max = 100
        choice_4 = input("Hoe vaak wil je oefenen?\n>> ")
        rekensessie(choice_2, choice_3, min, max)
    else:
        # Doe iets met 2
        pass


def close():
    try:
        with open('resultaten.txt', 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print('file not found')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load()
    menu()
    close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
