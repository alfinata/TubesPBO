import os, pickle
from os import path
from LogicCodes.heroClass import *
from LogicCodes.heroRole import *
from LogicCodes.equipmentPool import *
from LogicCodes.saveStateClass import *

# CLI Login - Alfinata
def gameLogin():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Input Nama
    print("============ WHO ARE YOU? ============")
    heroName = input("\nInsert your hero name here: ")

    # Seleksi Hero Class
    i = 0
    while i == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========== CLASS SELECTION ===========")
        print("Hero class selection:")
        print("1. Warrior - Relies on pure might and strength")
        print("2. Mage - Master of powerful and disruptive spells")
        print("3. Assassin - Swift, agile, and extremely deadly")
        roleInput = input("\nPress the keys to continue >> ")

        # Inisialisasi Hero Warrior
        if roleInput == "1":
            playerHero = basicHero(heroName, 120, 100, warriorRole(), 0)
            playerHero.equipWeapon(lowWarriorWeapon)
            playerHero.equipArmor(lowWarriorArmor)
            i = 1
        
        # Inisialisasi Hero Mage
        elif roleInput == "2":
            playerHero = basicHero(heroName, 100, 120, mageRole(), 0)
            playerHero.equipWeapon(lowMageWeapon)
            playerHero.equipArmor(lowMageArmor)
            i = 1
        
        # Inisialisasi Hero Assassin
        elif roleInput == "3":
            playerHero = basicHero(heroName, 100, 100, assassinRole(), 20)
            playerHero.equipWeapon(lowAssassinWeapon)
            playerHero.equipArmor(lowAssassinArmor)
            i = 1

    # Opening
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========= WELCOME TO LIL RPG =========")
    print(f"OK {playerHero.heroRole.checkRole()} {playerHero.getName()}, Welcome to this little RPG game.")
    print("In this game, your objective is to defeat the final boss.")
    print("In each fight you will loot gold, which you'll use to buy equipments to make yourself stronger")
    input("\nPress enter to continue>>")
    return playerHero