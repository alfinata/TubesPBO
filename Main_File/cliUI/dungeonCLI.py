from LogicCodes.enemyClass import *
from cliUI.combatCLI import *
from cliUI.storyCLI import *
import random


def dungeon(hero, stageNow, storyProgress, stageProgress):
    if(stageNow == 1):
        if storyProgress == 1:
            storyStage1()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 4 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 4)
            if chanceSpawn >= 2:
                enemy = slime()
            else:
                enemy = goblin()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1

    if(stageNow == 2):
        if storyProgress == 2:
            storyStage2()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 4 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 4)
            if chanceSpawn == 1:
                enemy = slime()
            elif chanceSpawn == 2:
                enemy = goblin()
            else:
                enemy = skeleton()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1

    if(stageNow == 3):
        if storyProgress == 3:
            storyStage3()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 5 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 3)
            if chanceSpawn == 1:
                enemy = goblin()
            else:
                enemy = skeleton()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1
    
    if(stageNow == 4):
        if storyProgress == 4:
            storyStage4()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 5 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 11)
            if chanceSpawn >= 4:
                enemy = skeleton()
            else:
                enemy = vampire()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1

    if(stageNow == 5):
        if storyProgress == 5:
            storyStage5()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 6 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 11)
            if chanceSpawn >= 5:
                enemy = skeleton()
            elif chanceSpawn >= 2:
                enemy = vampire()
            else:
                enemy = demon()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1

    if(stageNow == 6):
        if storyProgress == 6:
            storyStage6()
            storyProgress += 1
        roundNow = 1
        endGameCondition = 0
        while roundNow != 6 and endGameCondition == 0:
            chanceSpawn = random.randrange(1, 6)
            if chanceSpawn >= 3:
                enemy = vampire()
            else:
                enemy = demon()
            endGameCondition, hero = gameCombat(hero, enemy, stageNow, roundNow)
            roundNow += 1
    
    if(stageNow == 7):
        finishedTheGame = 0
        endGameCondition = 0
        while endGameCondition == 0:
            enemy = demonking()
            endGameCondition, hero = gameCombat(hero, enemy, roundNow)
            roundNow += 1
    
    if endGameCondition == 0 and stageProgress == stageNow:
        stageProgress += 1
    return hero, storyProgress, stageProgress
