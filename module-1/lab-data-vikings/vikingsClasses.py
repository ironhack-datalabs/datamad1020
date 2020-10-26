
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health-=damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
        
    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        if self.health<=0:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        if self.health<=0:
            return "A Saxon has died in combat"

# War



class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        for x in (range(5)):
            soldier + f"{x}" = Viking()
            vikingArmy.append(soldier+f"{x}")

    def addSaxon(self, saxon):
        for x in (range(5)):
            soldier+f"{x}" = Saxon()
            saxonArmy.append(soldier+f"{x}")

    def vikingAttack(self):
        saxon_random=random.choice(saxonArmy)
        viking_random=random.choice(vikingArmy)
        damagesaxon=saxon.receiveDamage(viking.strength)
        
        if saxon.health<=0:
            saxonArmy.remove(soldier+f"{x}")
        return damagesaxon

    def saxonAttack(self):
        saxon_random=random.choice(saxonArmy)
        viking_random=random.choice(vikingArmy)
        damageviking=viking.receiveDamage(saxon.strength)
        
        if viking.health<=0:
            vikingArmy.remove(soldier+f"{x}")
        return damageviking
        
        
    def showStatus(self):
        if self.saxonArmy==[]:
            return "Vikings have won the war of the century!"
        if self.vikingArmy==[]:
            return "Saxons have fought for their lives and survive another day..."
        if self.saxonArmy!=[] and self.vikingArmy!=[]:
            return "Vikings and Saxons are still in the thick of battle"

