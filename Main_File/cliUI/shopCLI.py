import os
from LogicCodes.heroClass import *

# CLI Shop - Dindin
def gameShop(hero, weaponPool, armorPool):
    exitShopStatus = 0
    while exitShopStatus == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print(f"Money: {hero.money} Gold")
        print("======================================")
        print("Welcome to the shop:")
        print("1. Buy Weapon")
        print("2. Buy Armor")
        print("3. Buy Consumable")
        print("4. Back to Main Menu")
        shopSelect = input("\nPress the keys to continue >> ")

        # Buy Weapon
        if shopSelect == "1":
            j = 0
            while j == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======================================")
                print(f"Current Weapon: {hero.weapon.getName()} (Damage: {hero.weapon.ATKBonus})")
                print(f"Money: {hero.money} Gold")
                print("======================================")
                print("Select the weapon you want to buy:")
                for i in range(1, 4):
                    print(f"{i}. {weaponPool[i].getName()} (Damage: {weaponPool[i].ATKBonus}) (Price: {weaponPool[i].getPrice()} Gold)")
                print("4. Back to General Shop")
                weaponSelect = input("\nPress the keys to continue >> ")
                if weaponSelect == "1":
                    if hero.money >= weaponPool[1].getPrice():
                        lateATK = hero.getATK()
                        hero.equipWeapon(weaponPool[1])
                        hero.money = hero.money - weaponPool[1].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.weapon.getName()} successfully purchased.")
                        print(f"Previous Attack Power: {lateATK}")
                        print(f"New Attack Power: {hero.getATK()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Weapon Price: {weaponPool[1].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {weaponPool[1].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif weaponSelect == "2":
                    if hero.money >= weaponPool[2].getPrice():
                        lateATK = hero.getATK()
                        hero.equipWeapon(weaponPool[2])
                        hero.money = hero.money - weaponPool[2].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.weapon.getName()} successfully purchased.")
                        print(f"Previous Attack Power: {lateATK}")
                        print(f"New Attack Power: {hero.getATK()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Weapon Price: {weaponPool[2].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {weaponPool[2].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif weaponSelect == "3":
                    if hero.money >= weaponPool[3].getPrice():
                        lateATK = hero.getATK()
                        hero.equipWeapon(weaponPool[3])
                        hero.money = hero.money - weaponPool[3].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.weapon.getName()} successfully purchased.")
                        print(f"Previous Attack Power: {lateATK}")
                        print(f"New Attack Power: {hero.getATK()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Weapon Price: {weaponPool[3].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {weaponPool[3].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif weaponSelect == "4":
                    j = 1
                else:
                    pass    
        
        # Buy Armor
        elif shopSelect == "2":
            j = 0
            while j == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======================================")
                print(f"Current Armor: {hero.armor.getName()} (Defense Bonus: {hero.armor.DEFBonus}%) (HP Bonus: {hero.armor.HPBonus})" )
                print(f"Money: {hero.money} Gold")
                print("======================================")
                print("Select the Armor you want to buy:")
                for i in range(1, 4):
                    print(f"{i}. {armorPool[i].getName()} (Defense Bonus: {armorPool[i].DEFBonus}%) (HP Bonus: {armorPool[i].HPBonus}) (Price: {armorPool[i].getPrice()} Gold)")
                print("4. Back to General Shop")
                armorSelect = input("Press the keys to continue >> ")
                if armorSelect == "1":
                    if hero.money >= armorPool[1].getPrice():
                        lateDEF = hero.getDEF()
                        lateHP = hero.getHPMax()
                        hero.equipArmor(armorPool[1])
                        hero.money = hero.money - armorPool[1].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.armor.getName()} successfully purchased.")
                        print(f"Previous Defense: {lateDEF}%")
                        print(f"Previous HP: {lateHP}")
                        print("")
                        print(f"New Defense: {hero.getDEF()}%")
                        print(f"New HP: {hero.getHPMax()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Armor Price: {armorPool[1].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {armorPool[1].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif armorSelect == "2":
                    if hero.money >= armorPool[2].getPrice():
                        lateDEF = hero.getDEF()
                        lateHP = hero.getHPMax()
                        hero.equipArmor(armorPool[2])
                        hero.money = hero.money - armorPool[2].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.armor.getName()} successfully purchased.")
                        print(f"Previous Defense: {lateDEF}%")
                        print(f"Previous HP: {lateHP}")
                        print("")
                        print(f"New Defense: {hero.getDEF()}%")
                        print(f"New HP: {hero.getHPMax()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Armor Price: {armorPool[2].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {armorPool[2].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif armorSelect == "3":
                    if hero.money >= armorPool[3].getPrice():
                        lateDEF = hero.getDEF()
                        lateHP = hero.getHPMax()
                        hero.equipArmor(armorPool[3])
                        hero.money = hero.money - armorPool[3].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.armor.getName()} successfully purchased.")
                        print(f"Previous Defense: {lateDEF}%")
                        print(f"Previous HP: {lateHP}")
                        print("")
                        print(f"New Defense: {hero.getDEF()}%")
                        print(f"New HP: {hero.getHPMax()}")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"Armor Price: {armorPool[3].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {armorPool[3].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif armorSelect == "4":
                    j = 1
                else:
                    pass
        
        # Buy Consumable
        elif shopSelect == "3":
            j = 0
            while j == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("======================================")
                print(f"Money: {hero.money} Gold")
                print(f"Owned Mana Potion : {hero.inventory.potions[0].stack}")
                print(f"Owned Health Potion : {hero.inventory.potions[1].stack}")
                print(f"Owned Attack Potion : {hero.inventory.potions[2].stack}")
                print("======================================")
                print("Select the Potion you want to buy:")
                print("1. Mana Potion")
                print("2. HP Potion")
                print("3. Attack Potion")
                print("4. Back to General Shop")
                potionSelect = input("Press the keys to continue >> ")
                if potionSelect == "1":
                    if hero.money >= hero.inventory.potions[0].getPrice():
                        hero.inventory.potions[0].stack = hero.inventory.potions[0].stack + 1
                        hero.money = hero.money - hero.inventory.potions[0].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.inventory.potions[0].getName()} successfully purchased.")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"{hero.inventory.potions[0].getName()} Price: {hero.inventory.potions[0].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {hero.inventory.potions[0].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif potionSelect == "2":
                    if hero.money >= hero.inventory.potions[1].getPrice():
                        hero.inventory.potions[1].stack = hero.inventory.potions[1].stack + 1
                        hero.money = hero.money - hero.inventory.potions[1].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.inventory.potions[1].getName()} successfully purchased.")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"{hero.inventory.potions[1].getName()} Price: {hero.inventory.potions[1].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {hero.inventory.potions[1].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif potionSelect == "3":
                    if hero.money >= hero.inventory.potions[2].getPrice():
                        hero.inventory.potions[2].stack = hero.inventory.potions[2].stack + 1
                        hero.money = hero.money - hero.inventory.potions[2].getPrice()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print(f"{hero.inventory.potions[2].getName()} successfully purchased.")
                        input("\nPress enter to continue >> ")
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("======================================")
                        print("Insufficient amount of money.")
                        print(f"{hero.inventory.potions[2].getName()} Price: {hero.inventory.potions[2].getPrice()} Gold")
                        print(f"Money: {hero.money} Gold")
                        print(f"You need {hero.inventory.potions[2].getPrice() - hero.money} more Gold")
                        input("\nPress enter to continue >> ")
                elif potionSelect == "4":
                    j = 1
                else:
                    pass
        
        # Exit Shop
        elif shopSelect == "4":
            exitShopStatus = 1

        else:
            pass
            