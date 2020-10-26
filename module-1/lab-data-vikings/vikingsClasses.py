import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        #Initializing the soldier class with their health and strength
        self.health = health
        self.strength = strength
        
    def attack(self):
        #Simply returns the strength, that is going to be the damage inflicted
        return self.strength
    
    def receiveDamage(self,damage):
        #Reducing the soldier's health by the quantity damage 
        self.health -= damage
    


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        #Initializing the soldier class with their own name 
        #and their health and strength (inerhited from the Soldier class)
        super().__init__(health, strength)        
        self.name = name

    def receiveDamage(self,damage):
        #Reducing the viking's health by the quantity damage 
        self.health -= damage
        #If the health points higher than 0, the viking's health points are
        #reduceb by the damage, and returns an string with this info.
        #
        #If the health points are lower or equal than 0, the viking is dead
        #and an string saying so is returned
        if self.health > 0:
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"


    def battleCry(self):
        #The viking shouts its reigious stuff for no reason
        return "Odin Owns You All!" 


# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
        #Reducing the saxon's health by the quantity damage 
        self.health -= damage
        #If the health points higher than 0, the saxon's health points are
        #reduceb by the damage, and returns an string with this info.
        #
        #If the health points are lower or equal than 0, the saxon is dead
        #and an string saying so is returned
        if self.health > 0:
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):  
        #Initializing the war class with an empty list for each army
        self.vikingArmy =  []
        self.saxonArmy = []

    def addViking(self,a_viking):
        #We add a viking to its army
        self.vikingArmy.append(a_viking)
    
    def addSaxon(self,a_saxon):
        #We add a saxon to its army
        self.saxonArmy.append(a_saxon)
        
    def vikingAttack(self):
        #The random sample selection chooses a viking to attack
        attacker = random.sample(self.vikingArmy, 1)[0]
        #A victim from the saxon side is randomly chosen
        defender = random.sample(self.saxonArmy, 1)[0]
        #The defender's health is reduced by the attaker strength
        #and we store the result from this action
        action = defender.receiveDamage(attacker.attack())
        #Dead saxon don't fight, so we remove it from his army if it is murdered
        if defender.health <= 0:
            self.saxonArmy.remove(defender)
        #We return the result of the clash
        return action
        
    def saxonAttack(self):
        #The random sample selection chooses a saxon to attack
        attacker = random.sample(self.saxonArmy, 1)[0]
        #A random viking victim is randomly chosen
        defender = random.sample(self.vikingArmy, 1)[0]
        #The defender's health is reduced by the attaker strength
        #and we store the result from this action        
        action = defender.receiveDamage(attacker.attack())
        #If the viking dies, is sent to Valhalla and removed from its army 
        if defender.health <= 0:
            self.vikingArmy.remove(defender)
        return action
            
    def showStatus(self):
        if self.saxonArmy == []:
            #If all saxons are erradicated, the vikings wins the battle
            return  "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            #If all vikings are sent to Valhalla, we display that the saxons won the battle
            return "Saxons have fought for their lives and survive another day..."
        else:
            #In the other cases, the battle is still undecided, and shows this message
            return "Vikings and Saxons are still in the thick of battle."


