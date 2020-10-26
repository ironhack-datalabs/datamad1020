import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage
    


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)        
        self.name = name

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"

    def battleCry(self,damage):
        self.health -= damage

    def battleCry(self):
        return "Odin Owns You All!" 


# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):      
        self.vikingArmy =  []
        self.saxonArmy = []

    def addViking(self,a_viking):
        self.vikingArmy.append(a_viking)
    
    def addSaxon(self,a_saxon):
        self.saxonArmy.append(a_saxon)
        
    def vikingAttack(self):
        attacker = random.sample(self.vikingArmy, 1)[0]
        defender = random.sample(self.saxonArmy, 1)[0]
        action = defender.receiveDamage(attacker.attack())
        if defender.health <= 0:
            self.saxonArmy.remove(defender)
        return action
        
    def saxonAttack(self):
        attacker = random.sample(self.saxonArmy, 1)[0]
        defender = random.sample(self.vikingArmy, 1)[0]
        action = defender.receiveDamage(attacker.attack())
        if defender.health <= 0:
            self.vikingArmy.remove(defender)
        return action
            
    def showStatus(self):
        if self.saxonArmy == []:
            return  "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


