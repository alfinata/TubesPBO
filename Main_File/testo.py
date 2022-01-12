baseDEF = 5

def increaseDEF(input):
    base = input
    inverse = 100 - base
    added = inverse * 25/100
    return base + added

defNow = baseDEF
print(f"Starting DEF = {baseDEF}")

while True:
    input("\nPress enter to apply increase DEF")
    defNow = increaseDEF(defNow)
    print(f"Def now = {defNow}")