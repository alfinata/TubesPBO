import os, copy
from LogicCodes.basicClass import *
from LogicCodes.heroRole import *

# CLI Combat - Alfinata
def gameCombat(inHero, enemy, level, round):
    battleCounter = 0
    battleFinished = 0
    whoWin = 0
    ATKPotionUsed = 0
    hero = copy.deepcopy(inHero)

    while battleFinished == 0:
        if battleCounter == 2:
            battleCounter = 0
        if battleCounter % 2 == 0:
            exitStatus = 0
            while exitStatus == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"======== COMBAT LEVEL {level} ==============")
                print(f"======== COMBAT STAGE {round} ==============")
                hero.showInfo()
                print("======================================")
                enemy.showInfo()
                print("======================================")
                print("Actions")
                print("1. Attack")
                print("2. Skill")
                print(f"3. Use Health Potion to restore {hero.inventory.potions[1].value} HP ({hero.inventory.potions[1].stack}) remaining.")
                print(f"4. Use Mana Potion to restore {hero.inventory.potions[0].value} Energy ({hero.inventory.potions[0].stack}) remaining.")
                print(f"5. Use ATK Potion to increase {hero.inventory.potions[2].value} attack power ({hero.inventory.potions[2].stack}) remaining.")
                print("6. Flee")
                toDo = input("\nPress the keys to continue >> ")

                # Attack Enemy
                if toDo == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"======== COMBAT LEVEL {level} ==============")
                    print(f"======== COMBAT STAGE {round} ==============")
                    hero.attackTarget(enemy)
                    print("======================================")
                    enemy.showInfo()
                    input("\nPress enter to continue>>")
                    exitStatus = 1

                # Choose and Use Skills
                elif toDo == "2":
                    skillChosen = 0
                    while skillChosen == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"======== COMBAT LEVEL {level} ==============")
                        print(f"======== COMBAT STAGE {round} ==============")
                        hero.showInfo()
                        print("======================================")
                        enemy.showInfo()
                        print("======================================")
                        print("Your skills:")
                        hero.heroRole.showAbilities()
                        print("3. Cancel")
                        skillInput = input("\nPress the keys to continue >> ")

                        # 1st Skill Chosen
                        if skillInput == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            if hero.heroRole.manaCost1 <= hero.energyCurrent:
                                hero.heroRole.doAbility1(hero, enemy)
                                skillChosen = 1
                                exitStatus = 1
                            else:
                                print("Not enough energy")
                            print("======================================")
                            enemy.showInfo()
                            input("\nPress enter to continue>>")

                        # 2nd Skill Chosen
                        elif skillInput == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            if hero.heroRole.manaCost2 <= hero.energyCurrent:
                                hero.heroRole.doAbility2(hero, enemy)
                                skillChosen = 1
                                exitStatus = 1
                            else:
                                print("Not enough energy")
                            print("======================================")
                            enemy.showInfo()
                            input("\nPress enter to continue>>")

                        # Cancel
                        elif skillInput == "3":
                            skillChosen = 1

                        else:
                            pass

                # Use Health Potion
                elif toDo == "3":
                    if hero.inventory.potions[1].stack > 0:
                        hero.inventory.potions[1].stack -= 1
                        hero.healHP(hero.inventory.potions[1].value)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.getName()} consumed a Health Potion, restored {hero.inventory.potions[1].value} HP.")
                        print("======================================")
                        hero.showInfo()
                        input("\nPress enter to continue>>")
                        exitStatus = 1
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Not enough potions.")
                        input("\nPress enter to continue>>")

                # Use Mana Potion
                elif toDo == "4":
                    if hero.inventory.potions[0].stack > 0:
                        hero.inventory.potions[0].stack -= 1
                        hero.restoreEnergy(hero.inventory.potions[0].value)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.getName()} consumed a Mana Potion, restored {hero.inventory.potions[0].value} Energy.")
                        print("======================================")
                        hero.showInfo()
                        input("\nPress enter to continue>>")
                        exitStatus = 1
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Not enough potions.")
                        input("\nPress enter to continue>>")

                # Use ATK Potion
                elif toDo == "5":
                    if hero.inventory.potions[2].stack > 0:
                        if ATKPotionUsed == 0:
                            hero.inventory.potions[2].stack -= 1
                            hero.setATK(hero.getATK() + hero.inventory.potions[2].value)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            print(f"{hero.getName()} consumed a ATK Potion, increasing ATK by {hero.inventory.potions[2].value}.")
                            print("======================================")
                            hero.showInfo()
                            input("\nPress enter to continue>>")
                            ATKPotionUsed = 1
                            exitStatus = 1
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================")
                            print("Already used in this stage")
                            input("\nPress enter to continue>>")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Not enough potions.")
                        input("\nPress enter to continue>>")

                # Flee
                elif toDo == "6":
                    battleFinished = 1
                    whoWin = 3
                    exitStatus = 1
                else:
                    pass

        # Enemy Turn
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"======== COMBAT LEVEL {level} ==============")
            print(f"======== COMBAT STAGE {round} ==============")
            enemy.doSomething(hero)
            print("======================================")
            hero.showInfo()
            input("<<Press enter to continue>>")
        if hero.getHPCurrent() == 0:
            battleFinished = 1
            whoWin = 2
        elif enemy.getHPCurrent() == 0:
            battleFinished = 1
            whoWin = 1
        battleCounter += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"======== COMBAT LEVEL {level} ==============")
    print(f"======== COMBAT STAGE {round} ==============")
    if whoWin == 1:
        print(f"Congratulations, you beat {enemy.getName()}")
        print(f"You get {enemy.money} gold after looting the enemy.")
        inHero.money += enemy.money
        inHero.setHPCurrent(hero.getHPCurrent())
        inHero.energyCurrent = hero.energyCurrent
        inHero.inventory = hero.inventory
        input("\n<<Press enter to continue>>")
        return 0, inHero
    elif whoWin == 2:
        moneyNow = int(hero.money*0.8)
        inHero.money = moneyNow
        print(f"Oh no! You got beaten by {enemy.getName()}")
        print("======================================")
        print("You got unconscious. You then wake up in the town. It seems you managed to stay alive.")
        print(f"But you lose some gold, you now only have {inHero.money} Gold left.")
        print("======================================")
        inHero.setHPCurrent(hero.getHPMax()*0.2)
        inHero.energyCurrent = hero.energyMax*0.2
        inHero.inventory = hero.inventory
        input("\n<<Press enter to continue>>")
        return 1, inHero
    elif whoWin == 3:
        print(f"You Managed to get Away...")
        inHero.money = hero.money
        inHero.setHPCurrent(hero.getHPCurrent())
        inHero.energyCurrent = hero.energyCurrent
        inHero.inventory = hero.inventory
        input("\n<<Press enter to continue>>")
        return 1, inHero
