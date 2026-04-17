import raad_het_getal
import galgje
import jokes
import urllib3

if __name__ == "__main__":
    print("==== NANO Game Centre ====\n",
          "Kies een getal en druk op enter om het spel te spelen:\n",
          "1. Galgje\n",
          "2. Raad het getal\n",
          "3. Grappen generator\n",
          "4. Stoppen\n")
    
    choice = input(">> ")

    if choice == "1":
        galgje.menu()
    elif choice == "2":
        raad_het_getal.app()
    elif choice == "3":
        jokes.app()
    else:
        print("GAME OVER")
        exit()
    