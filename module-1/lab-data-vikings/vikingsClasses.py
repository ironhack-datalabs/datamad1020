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






guerra = War()


viky1 = Viking("The Warrior of the Barrio",60,40)
viky2 = Viking("Goteulfo el potras",60,40)
viky3 = Viking("Sigmundo el imprudente",60,40)
viky4 = Viking("Vikingo indistinto nº42",60,40)

saja1 = Saxon(60,40)
saja2 = Saxon(60,40)
saja3 = Saxon(60,40)
saja4 = Saxon(60,40)


guerra.addViking(viky1)
guerra.addViking(viky2)
guerra.addViking(viky3)
guerra.addViking(viky4)

guerra.addSaxon(saja1)
guerra.addSaxon(saja2)
guerra.addSaxon(saja3)
guerra.addSaxon(saja4)

print(guerra.vikingAttack())

print(guerra.saxonAttack())


print(guerra.vikingAttack())

print(guerra.saxonAttack())

print(guerra.vikingAttack())

print(guerra.saxonAttack())
print(guerra.showStatus())







"""

#Purria para probar

viky = Viking("The Warrior of the Barrio",60,15)
print(viky.receiveDamage(30))
print(viky.battleCry())
print(viky.receiveDamage(40))

print("\n\n")

pringadete = Saxon(60,15)
print(pringadete.receiveDamage(40))
print(pringadete.receiveDamage(40))
"""