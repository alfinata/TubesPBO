import os
from LogicCodes.basicClass import *
from LogicCodes.heroRole import *

# CLI Combat - Alfinata
def gameCombat(hero, enemy):
    battleCounter = 0
    battleFinished = 0
    whoWin = 0

    while battleFinished == 0:
        if battleCounter % 2 == 0:
            exitStatus = 0
            while exitStatus == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======================================\n")
                hero.showInfo()
                print("\n======================================\n")
                enemy.showInfo()
                print("\n======================================\n")
                print("Actions")
                print("1. Attack")
                print("2. Skill")
                toDo = input("\nPress the keys to continue >> ")
                if toDo == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======================================\n")
                    hero.attackTarget(enemy)
                    print("\n======================================\n")
                    enemy.showInfo()
                    input("<<Press enter to continue>>")
                    exitStatus = 1
                elif toDo == "2":
                    skillChosen = 0
                    while skillChosen == 0:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================\n")
                        hero.showInfo()
                        print("\n======================================\n")
                        enemy.showInfo()
                        print("\n======================================\n")
                        print("Your skills:")
                        hero.heroRole.showAbilities()
                        print("3. Cancel")
                        skillInput = input("\nPress the keys to continue >> ")
                        if skillInput == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================\n")
                            if hero.heroRole.manaCost1 <= hero.energyCurrent:
                                hero.heroRole.doAbility1(hero, enemy)
                                skillChosen = 1
                                exitStatus = 1
                            else:
                                print("Not enough energy")
                            print("\n======================================\n")
                            enemy.showInfo()
                            input("<<Press enter to continue>>")
                        elif skillInput == "2":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("======================================\n")
                            if hero.heroRole.manaCost2 <= hero.energyCurrent:
                                hero.heroRole.doAbility2(hero, enemy)
                                skillChosen = 1
                                exitStatus = 1
                            else:
                                print("Not enough energy")
                            print("\n======================================\n")
                            enemy.showInfo()
                            input("<<Press enter to continue>>")
                        elif skillInput == "3":
                            skillChosen = 1
                        else:
                            pass
                else:
                    pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("======================================\n")
            enemy.attackTarget(hero)
            print("======================================\n")
            hero.showInfo()
            input("<<Press enter to continue>>")
        if hero.getHPCurrent() == 0:
            battleFinished = 1
            whoWin = 2
        if enemy.getHPCurrent() == 0:
            battleFinished = 1
            whoWin = 1
        battleCounter += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================\n")
    if whoWin == 1:
        print(f"Congratulations, you beat {enemy.getName()}")
        print(f"You get {enemy.money} gold after looting the enemy.")
        hero.money += enemy.money
        input("<<Press enter to continue>>")
        return 0
    elif whoWin == 2:
        print(f"Oh no! You got beaten by {enemy.getName()}")
        print("\n======================================\n")
        print("GAME OVER")
        print("\n======================================\n")
        return 1
