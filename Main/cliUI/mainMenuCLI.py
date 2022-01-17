import os, time, pickle
from os import path
from cliUI.shopCLI import gameShop
from cliUI.dungeonCLI import *
from LogicCodes.equipmentPool import *
from LogicCodes.enemyClass import *
from LogicCodes.heroClass import *
from LogicCodes.saveStateClass import *

# CLI Main Menu - Rapip
def gameMenu(hero, stageProgress, storyProgress):
    exitGameStatus = 0
    while exitGameStatus == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("============= MAIN MENU ==============")
        hero.showHeroInfo()
        print("======================================")
        print("Menu selection:")
        print("1. Go to The Dungeon")
        print("2. Go to The Shop")
        print("3. Check Inventory")
        print("4. Rest")
        print("5. Save Game")
        print("6. Exit Game")
        menuInput = input("\nPress the keys to continue >> ")
        
        # Enter Dungeon
        if menuInput == "1":
            if storyProgress == 0:
                storyStart()
                storyProgress = 1
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("============= DUNGEON ================")
                print("Dungeon stage selection:")
                for stage in range(stageProgress):
                    if stage <= 6:
                        print(f"{stage+1}. Stage {stage+1}")
                print("8. Exit Dungeon")
                stageInput = input("\nPress the keys to continue >> ")
                if stageInput == "8":
                    i = 1
                elif (stageInput == "1" or 
                    stageInput == "2" or
                    stageInput == "3" or 
                    stageInput == "4" or 
                    stageInput == "5" or 
                    stageInput == "6" or 
                    stageInput == "7"):
                    if int(stageInput) <= stageProgress:
                        hero, storyProgress, stageProgress = dungeon(hero, int(stageInput), storyProgress, stageProgress)
                        i = 1
                else: pass
        
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
                print("\nActions: ")
                print(f"1. Use Health Potion to heal {hero.inventory.potions[1].value} HP")
                print(f"2. Use Mana Potion to restore {hero.inventory.potions[0].value} Energy")
                print(f"3. Exit")   
                potionInput = input("\nPress the keys to continue >> ")
                if potionInput == "1":
                    if hero.inventory.potions[1].stack > 0:
                        hero.inventory.potions[1].stack -= 1
                        hero.healHP(hero.inventory.potions[1].value)
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
                        hero.restoreEnergy(hero.inventory.potions[0].value)
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
            innPrice = 20
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
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=========== TAKE A REST ==============")
                        print("You are currently don't have enough gold.")
                        input("\nPress enter to leave the inn>> ")
                        i = 1
                elif optionInput == "2":
                    i = 1
                else: pass

        # Save Game
        elif menuInput == "5":
            selectedFile = 0
            while selectedFile == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======== SAVE FILE SELECTION =========")

                # Slot Checking
                print("Select the slots to save your file:")
                for i in range(3):
                    if path.exists(f"saves/data{i+1}.txt"):
                        fileOut = open(f"saves/data{i+1}.txt", 'rb')
                        objectToOutput = pickle.load(fileOut)
                        print(f"{i+1}. Data Slot {i+1}: {objectToOutput.getHero().heroRole.checkRole()} {objectToOutput.getHero().getName()}")
                    else: 
                        print(f"{i+1}. Data Slot {i+1}: Empty")
                print("4. Back to Start Game")
                            
                # Slot Selecting
                slotSelection = input("\nPress the keys to continue >> ")
                if (slotSelection == "1" or slotSelection == "2" or slotSelection == "3"):
                    if path.exists(f"saves/data{slotSelection}.txt"):
                        overwriteStatus = 0
                        while overwriteStatus == 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            print("This slot already used, do you want to overwrite?")
                            print("1. Yes")
                            print("2. No")
                            overwriteSelection = input("\nPress the keys to continue >> ")
                            if overwriteSelection == "1":
                                fileIn = open(f"saves/data{slotSelection}.txt", 'wb')
                                objectToSave = saveStateClass(hero, stageProgress, storyProgress)
                                pickle.dump(objectToSave, fileIn)
                                fileIn.close()
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("======================================")
                                print("Game Saved.")
                                input("\nPress the keys to continue >> ")
                                overwriteStatus = 1
                                selectedFile = 1
                            elif overwriteSelection == "2":
                                overwriteStatus = 1
                    else:
                        writeStatus = 0
                        while writeStatus == 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            print("This slot is empty, do you want to save here?")
                            print("1. Yes")
                            print("2. No")
                            writeSelection = input("\nPress the keys to continue >> ")
                            
                            if writeSelection == "1":
                                fileIn = open(f"saves/data{slotSelection}.txt", 'wb')
                                objectToSave = saveStateClass(hero, stageProgress, storyProgress)
                                pickle.dump(objectToSave, fileIn)
                                fileIn.close()
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("======================================")
                                print("Game Saved.")
                                input("\nPress the keys to continue >> ")
                                selectedFile = 1
                                writeStatus = 1
                                
                            elif writeSelection == "2":
                                writeStatus = 1
                elif slotSelection == "4":
                    selectedFile = 1

        # Exit Game
        elif menuInput == "6":
            exitGameStatus = 1