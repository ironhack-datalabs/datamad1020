import random
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
    def __init__(self, name,health, strength):
        super().__init__(health,strength)
        self.name = name
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
    def battleCry(self) :
        return "Odin Owns You All!"   


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        if self.health <= 0:
            return f"A Saxon has died in combat"
            
#War
class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        #viking += 1
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        #Saxon += 1
        self.saxonArmy.append(Saxon)
        
        
    def vikingAttack(self):
        #debe igualar un saxon receiveDamage con la fuerza de un vikingo
        #debe retirar saxons muertos
        #debe devolver la llamada de receiveDamage de saxon con la fuerza de un vikingo
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        resultado = saxon.receiveDamage(viking.attack())
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return resultado
       
    
    def saxonAttack(self):
        #lo de arriba pero al revés'
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        resultado = viking.receiveDamage(saxon.attack())
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return resultado
    
    def showStatus(self):
        #si el array de saxon está vacío = "Vikings have won the war of the century!
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        #si el array de vikings está vacío = "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        #si hay al menos 1 viking y 1 saxon = "Vikings and Saxons are still in the thick of battle."
        if len(self.vikingArmy) >=1 or len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."