from LogicCodes.enemyClass import *
from cliUI.combatCLI import *
import random

def dungeon(hero, stageNow):
    if(stageNow == 1):
        chanceSpawn = random.randrange(1, 101)
        roundNow = 1
        endGameCondition = 0
        while roundNow != 4 and endGameCondition == 0:
            if chanceSpawn > 33:
                enemy = slime()
            else:
                enemy = goblin()
            endGameCondition, hero = gameCombat(hero, enemy, roundNow)
            roundNow += 1
    return hero
        
        
        

