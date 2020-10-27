
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength      
        
    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        if self.health <= 0:
            return "A Saxon has died in combat"


# War
import random
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    
    def addViking(self, v_soldier):
        for x in range(6):
            x = v_soldier
        self.vikingArmy.append(v_soldier)
    
    def addSaxon(self, s_soldier):
        for x in range(6):
            x = s_soldier
        self.saxonArmy.append(s_soldier)
        

    def vikingAttack(self):
        randSaxon = random.choice(self.saxonArmy)
        randViking = random.choice(self.vikingArmy)
        randSaxon.receiveDamage(randViking.attack())
        if randSaxon.health <= 0:
            self.saxonArmy.remove(randSaxon)
        s_health = randSaxon.health()
        return s_health 

    
    def saxonAttack(self):
        randViking = random.choice(self.vikingArmy)
        randSaxon = random.choice(self.saxonArmy)
        randViking.receiveDamage(randSaxon.attack())
        if randViking.health <= 0:
            self.vikingArmy.remove(randViking)
        v_health = randViking.health()
        return v_health

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >=1:
            return "Vikings and Saxons are still in the thick of battle."


