import os

from LogicCodes.heroClass import *
from LogicCodes.heroRole import *

# UI Login - Alfinata
def gameLogin():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================\n")
    heroName = input("Insert your hero name here: ")

    i = 0
    while i == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================\n")
        print("Hero class selection:")
        print("1. Warrior - Relies on pure strength")
        print("2. Mage - Master of powerful spells")
        print("3. Assassin - Agile and deadly")
        print("")
        roleInput = input("Press the keys to continue >> ")
        if roleInput == "1":
            heroRole = warriorRole()
            playerHero = basicHero(heroName, 120, 100, heroRole, 0)
            i = 1
        elif roleInput == "2":
            heroRole = mageRole()
            playerHero = basicHero(heroName, 100, 120, heroRole, 0)
            i = 1
        elif roleInput == "3":
            heroRole = assassinRole()
            playerHero = basicHero(heroName, 100, 100, heroRole, 10)
            i = 1
        else:
            pass

    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================\n")
    print(f"OK {playerHero.heroRole.checkRole()} {playerHero.getName()}, Welcome to this little RPG game.")
    print("In this game, your objective is to defeat the final boss.")
    print("Each fight will drop gold, which you'll use to buy equipments to make yourself stronger\n")
    input("<<Press enter to continue>>")

    os.system('cls' if os.name == 'nt' else 'clear')
    return playerHero