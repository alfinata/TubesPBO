import os
from LogicCodes.basicClass import *

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
                print(f"{hero.heroRole.checkRole()} {hero.getName()}")
                print(f"Hero HP: {hero.getHPCurrent()}/{hero.getHPMax()}")
                print(f"Attack Power: {hero.getATK()}")
                print(f"Defense Power: {hero.getDEF()}\n")
                print("======================================\n")
                print(f"Enemy: {enemy.getName()}")
                print(f"Enemy HP: {enemy.getHPCurrent()}/{enemy.getHPMax()}")
                print(f"Attack Power: {enemy.getATK()}")
                print(f"Defense Power: {enemy.getDEF()}\n")
                print("======================================\n")
                print("Actions")
                print("1. Attack")
                toDo = input("Press the keys to continue >> ")
                if toDo == "1":
                    enemyHPThen = enemy.getHPCurrent()
                    hero.attackTarget(enemy)
                    enemyHPNow = enemy.getHPCurrent()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("======================================\n")
                    print(f"{hero.getName()} attacked {enemy.getName()}, dealing {enemyHPThen-enemyHPNow} damage.")
                    print(f"Enemy: {enemy.getName()}")
                    print(f"Enemy HP: {enemy.getHPCurrent()}/{enemy.getHPMax()}")
                    input("<<Press enter to continue>>")
                    exitStatus = 1
                else:
                    pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("======================================\n")
            myHPThen = hero.getHPCurrent()
            enemy.attackTarget(hero)
            myHPNow = hero.getHPCurrent()
            print(f"{enemy.getName()} attacked {hero.getName()}, dealing {myHPThen-myHPNow} damage.\n")
            print(f"{hero.heroRole.checkRole()} {hero.getName()}")
            print(f"Hero HP: {hero.getHPCurrent()}/{hero.getHPMax()}")
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
        print(f"You get 20 gold after looting the enemy.")
    elif whoWin == 2:
        print(f"Oh no! You got beaten by {enemy.getName()}")
    input("<<Press enter to continue>>")
