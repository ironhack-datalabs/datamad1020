
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
    pass





#Purria para probar

viky = Viking("The Warrior of the Barrio",60,15)
print(viky.receiveDamage(30))
print(viky.battleCry())
print(viky.receiveDamage(40))

print("\n\n")

pringadete = Saxon(60,15)
print(pringadete.receiveDamage(40))
print(pringadete.receiveDamage(40))
