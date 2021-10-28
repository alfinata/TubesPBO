import os

def navigate(h1):
    while 0 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================================")
        print("")
        h1.showInfo()
        print("Navigation:")
        print("1. Fight an enemy")
        print("2. Change weapon")
        print("3. Change armor")
        print("4. Check items")
        print("5. Visit shop")
        print("")
        x = input("Press the keys to continue >>")
        if x == "1":
            pass
        elif x == "2":
            pass
        elif x == "3":
            pass
        elif x == "4":
            pass
        elif x == "5":
            pass
        else:
            pass

