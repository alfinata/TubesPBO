import os

# CLI Shop - Dindin
def gameShop(hero, weaponPool, armorPool):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================================\n")


    i = 0
    while i == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the shop:")
        print("1. Buy Weapon")
        print("2. Sell Weapon")
        print("3. Buy Armor")
        print("4. Sell Armor")
        print("5. Buy Consumable")

        shopSelect = input("Press the keys to continue >> ")

        # weapon WARRIOR
        if shopSelect == "1":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to buy:")
                print("1. Wooden Axe")
                print("2. Stone Sword")
                print("3. Steel Spear")
                print("4. Emerald Claymore")
            i = 1
        elif shopSelect == "2":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to sell:")
                print("1. Wooden Staff")
                print("2. Stone Wand")
                print("3. Hardwood Grimoire")
                print("4. Ruby Magic Book")
            i = 1


        #weapon MAGE
        if shopSelect == "1":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to buy:")
                print("1. Wooden Staff")
                print("2. Stone Wand")
                print("3. Hardwood Grimoire")
                print("4. Ruby Magic Book")
            i = 1
        elif shopSelect == "2":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to sell:")
                print("1. Wooden Staff")
                print("2. Stone Wand")
                print("3. Hardwood Grimoire")
                print("4. Ruby Magic Book"))
            i = 1

        #weapon ASSASIN
        if shopSelect == "1":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to buy:")
                print("1. Rusty Knife")
                print("2. Sharp Shortsword")
                print("3. Iron Machete")
                print("4. Mithril Sabre")
            i = 1
        elif shopSelect == "2":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the weapon you want to buy:")
                print("1. Rusty Knife")
                print("2. Sharp Shortsword")
                print("3. Iron Machete")
                print("4. Mithril Sabre")
            i = 1

        # armor WARRIOR
        if shopSelect == "3":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to buy:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1
        elif shopSelect == "4":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to sell:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1

        # armor MAGE
        if shopSelect == "3":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to buy:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1
        elif shopSelect == "4":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to sell:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1

        # armor ASSASIN
        if shopSelect == "3":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to buy:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1
        elif shopSelect == "4":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the armor you want to sell:")
                print("1. armor 1")
                print("2. armor 2")
                print("3. armor 3")
                print("4. armor 4")
            i = 1


        elif shopSelect == "5":
            i = 0
            while i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Select the comsumable you want to buy:")
                print("1. Mana Potion")
                print("2. HP Potion")
                print("3. Attack Potion")
            i = 1
        else:
            pass