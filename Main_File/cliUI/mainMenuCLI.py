import os
from cliUI.shopCLI import gameShop
from cliUI.combatCLI import gameCombat
from LogicCodes.equipmentPool import *
from LogicCodes.enemyClass import *
from LogicCodes.heroClass import *

# CLI Main Menu - Rapip
def gameMenu(hero):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================\n")

    i = 0
    while i == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================\n")
        hero.showHeroInfo()
        print("\nMenu selection:")
        print("1. Go to The Dungeon")
        print("2. Go to The Shop")
        print("3. Exit")
        print("")
        menuInput = input("Press the keys to continue >> ")
        if menuInput == "1":
            testing_slime = goblin()
            i = gameCombat(hero, testing_slime)
        elif menuInput == "2":
            if(hero.heroRole.checkRole() == "Mage"):
                gameShop(hero, mageWeaponPool, mageArmorPool)
            elif(hero.heroRole.checkRole() == "Assassin"):
                gameShop(hero, assassinWeaponPool, assassinArmorPool)
            elif(hero.heroRole.checkRole() == "Warrior"):
                gameShop(hero, warriorWeaponPool, warriorArmorPool)
            i = 1
        elif menuInput == "3":
            i = 1
        else:
            pass