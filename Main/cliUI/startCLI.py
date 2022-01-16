# Starting Game CLI - Alfinata

import os, pickle
from os import path

from cliUI.loginCLI import *
from cliUI.mainMenuCLI import *

def startCLI():
    exitStatus = 0
    while exitStatus == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===============================================================================================================")
        print("   _       ___   _           ____    ____     ____       ____    ____     ___        _   _____    ____   _____ ")
        print("  | |     |_ _| | |         |  _ \  |  _ \   / ___|     |  _ \  |  _ \   / _ \      | | | ____|  / ___| |_   _|")
        print("  | |      | |  | |         | |_) | | |_) | | |  _      | |_) | | |_) | | | | |  _  | | |  _|   | |       | |  ")
        print("  | |___   | |  | |___   _  |  _ <  |  __/  | |_| |  _  |  __/  |  _ <  | |_| | | |_| | | |___  | |___    | |  ")
        print("  |_____| |___| |_____| (_) |_| \_\ |_|      \____| (_) |_|     |_| \_\  \___/   \___/  |_____|  \____|   |_|  \n")
        print("===============================================================================================================\n")
        print("                                      Created by AveragePixelEnjoyer")
        print("1. New Game.")
        print("2. Load Game.")
        print("3. Exit Game.")
        nextSelect = input("\nPress the keys to continue >> ")
        if nextSelect == "1":
            selectedHero = gameLogin()
            gameMenu(selectedHero, 1, 0)

        # Load Game
        elif nextSelect == "2":
            loadStatus = 0
            while loadStatus == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======================================")
                print("Select game file:")

                # Slot Checking
                for i in range(3):
                    if path.exists(f"saves/data{i+1}.txt"):
                        with open(f"saves/data{i+1}.txt", 'rb') as fileOut:
                            objectToOutput = pickle.load(fileOut)
                        print(f"{i+1}. Data Slot {i+1}: {objectToOutput.getHero().heroRole.checkRole()} {objectToOutput.getHero().getName()}")
                    else: 
                        print(f"{i+1}. Data Slot {i+1}: Empty")
                print("4. Back to Start Game")
                        
                # Slot Selecting
                slotSelection = input("\nPress the keys to continue >> ")
                if (slotSelection == "1" or slotSelection == "2" or slotSelection == "3"):
                    if path.exists(f"saves/data{slotSelection}.txt"):
                        fileOut = open(f"saves/data{slotSelection}.txt", 'rb')
                        objectToOutput = pickle.load(fileOut)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Game Loaded.")
                        input("\nPress the keys to continue >> ")
                        gameMenu(objectToOutput.getHero(), objectToOutput.getStageProgress(), objectToOutput.getStoryProgress)
                        loadStatus = 1
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Save State is empty.")
                        input("\nPress the keys to continue >> ")

                # Back
                elif slotSelection == "4":
                    loadStatus = 1

        elif nextSelect == "3":
            exitStatus = 1