# Class Debuffs - Alfinata
class debuff:
    def __init__(self, name, durationTotal, durationRemaining):
        self.name = name
        self.durationTotal = durationTotal
        self.durationRemaining = durationRemaining

    def triggerEffect(self):
        pass

# Class Mage Burn Debuff - Alfinata
class mageBurn(debuff):
    def __init__(self):
        super().__init__("mageBurn", 3, 3)
    
    def triggerEffect(self, target):
        target.takeDamage(10)
        self.durationRemaining =- 1