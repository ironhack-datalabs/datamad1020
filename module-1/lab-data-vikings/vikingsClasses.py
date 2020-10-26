
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage


  

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"





# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return "A Saxon has died in combat"





# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        r = saxon.receiveDamage(viking.strength)
        if saxon.health < 1:
            self.saxonArmy.remove(saxon)
        return r

    def saxonAttack(self):
        import random
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        r = viking.receiveDamage(saxon.strength)
        if viking.health < 1:
            self.vikingArmy.remove(viking)
        return r

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
