import os, time
from cliUI.shopCLI import gameShop
from cliUI.combatCLI import gameCombat
from LogicCodes.equipmentPool import *
from LogicCodes.enemyClass import *
from LogicCodes.heroClass import *
from cliUI.dungeonCLI import *

# CLI Main Menu - Rapip
def gameMenu(hero):
    loseCondition = 0
    stageNow = 1 #
    while loseCondition == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============= MAIN MENU ==============")
        hero.showHeroInfo()
        print("======================================")
        print("Menu selection:")
        print("1. Go to The Dungeon")
        print("2. Go to The Shop")
        print("3. Check Inventory")
        print("4. Rest")
        print("5. Exit Game")
        menuInput = input("\nPress the keys to continue >> ")
        
        # Enter Dungeon
        if menuInput == "1":
            hero = dungeon(hero, stageNow) #
        
        # Enter Shop
        elif menuInput == "2":
            if(hero.heroRole.checkRole() == "Mage"):
                gameShop(hero, mageWeaponPool, mageArmorPool)
            elif(hero.heroRole.checkRole() == "Assassin"):
                gameShop(hero, assassinWeaponPool, assassinArmorPool)
            elif(hero.heroRole.checkRole() == "Warrior"):
                gameShop(hero, warriorWeaponPool, warriorArmorPool)
        
        # Show Inventory
        elif menuInput == "3":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============= INVENTORY ==============")
                print(f"Money : {hero.money} Gold")
                print(f"Weapon : {hero.weapon.getName()} (Attack Power : {hero.getATK()})")
                print(f"Armor : {hero.armor.getName()} (Defense Power : {hero.getDEF()}%) (HP Bonus : {hero.armor.HPBonus})")
                print("======================================")
                print("Potions : ")
                print(f"Health Potion : {hero.inventory.potions[1].stack}")
                print(f"Mana Potion : {hero.inventory.potions[0].stack}")
                print(f"Attack Potion : {hero.inventory.potions[2].stack}")
                print("\nSelect the potion you want to use")
                print(f"1. Health Potion")
                print(f"2. Mana Potion")
                print(f"3. Exit")   
                potionInput = input("\nPress the keys to continue >> ")
                if potionInput == "1":
                    if hero.inventory.potions[1].stack > 0:
                        hero.inventory.potions[1].stack -= 1
                        hero.healHP(hero.inventory.potions[0].value)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.getName()} consumed a Health Potion, restored {hero.inventory.potions[1].value} HP.")
                        print("======================================")
                        hero.showInfo()
                        input("\nPress enter to continue>>")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Not enough potions.")
                        input("\nPress enter to continue>>")
                elif potionInput == "2":
                    if hero.inventory.potions[0].stack > 0:
                        hero.inventory.potions[0].stack -= 1
                        hero.restoreEnergy(hero.inventory.potions[1].value)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.getName()} consumed a Mana Potion, restored {hero.inventory.potions[0].value} Energy.")
                        print("======================================")
                        hero.showInfo()
                        input("\nPress enter to continue>>")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Not enough potions.")
                        input("\nPress enter to continue>>")
                elif potionInput == "3":
                    i = 1
                    

        # Take a Rest
        elif menuInput == "4":
            i = 0
            innPrice = 25
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=========== TAKE A REST ==============")
                print(f"Current Money : {hero.money} Gold")
                print(f"The Inn Price will be {innPrice} Gold:")
                print("1. Pay")
                print("2. Leave")
                optionInput = input("\nPress the keys to continue >> ")
                if optionInput == "1":
                    if hero.money >= innPrice:
                        hero.money -= innPrice
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print(f"You have successfully paid for your room, you only have {hero.money} Gold left.")
                        input("\nPress enter to take a rest >> ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print("Currently sleeping.")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print("Currently sleeping..")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print("Currently sleeping...")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print("Finished sleeping.")
                        hero.healHP(999)
                        hero.restoreEnergy(120)
                        input("\nPress enter to leave the inn>> ")
                        i = 1
                    else:
                        print("You are currently don't have enough gold.")
                        i = 1
                elif optionInput == "2":
                    i = 1
                else: pass

        # Exit Game
        elif menuInput == "5":
            loseCondition = 1

        else:
            pass

        # Check Lose Condition
        if hero.getHPCurrent == 0:
            loseCondition = 1