
# Soldier


class Soldier:
    #The soldiers constructor function receives two arguments
    def __init__(self,health,strength):
        self.health= health
        self.strength= strength
    #Adding the first method
    def attack(self): #receives zero arguments
        return self.strength
    #adding the second method
    def receiveDamage(self,damage):
        self.health -= damage
        #no return 
    pass

# Viking


class Viking (Soldier): #Inherits from Soldier
    #Receives three arguments
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength= strength
    #reimplement because it has different return values
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:#if the viking is still alive
            return (f'{self.name} has received {damage} points of damage')
        else: #if the viking dies
            return (f'{self.name} has died in act of combat')
    def battleCry(self):
        return ('Odin Owns You All!')

    pass

# Saxon


class Saxon (Soldier):#Inherits from soldier
    #Receives two arguments
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    #reimplement because it has different return values
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:#if the saxon is still alive
            return (f'A Saxon has received {damage} points of damage')
        else: #if the saxon dies
            return ('A Saxon has died in combat')
    
    
    pass

# War

import random
class War:
    #Constructor function
    def __init__(self):
        #Create empty arrays to later add soldiers
        vikingArmy = []
        saxonArmy = []

    #Add 5 methods
    def addViking(self, Viking):
        for x in (range(6)):
            Viking + f"{x}" = Viking()
            vikingArmy.append(soldier+f"{x}") 
              
    def addSaxon(self,Saxon):
        for x in (range(6)):
            Saxon + f"{x}" = Saxon()
            saxonArmy.append(soldier + f"{x}")
        
    def vikingAttack(self):
        saxonrandom= random.choice(self.saxonArmy)
        vikingrandom= random.choice(self.vikingArmy)
                
        a = saxon.receiveDamage(viking.strength)
        
        if self.health<0:
            saxonArmy.remove(soldier + f"{x}")
        
        return (a)

    def saxonAttack(self):
        saxonrandom= random.choice(saxonArmy)
        vikingrandom= random.choice(vikingArmy)

        b = viking.receiveDamage(saxon.strength)

        if self.health<0:
            vikingArmy.remove(soldier + f"{x}")

        return (b)

    def showStatus(self):
        if saxonArmy ==0:
            return ('Vikings have won the war of the century!')
        elif vikingArmy ==0:
            return ('Saxons have fought for their lives and survive another day...')
        else:
            return ('Vikings and Saxons are still in the thick of battle')

    pass
