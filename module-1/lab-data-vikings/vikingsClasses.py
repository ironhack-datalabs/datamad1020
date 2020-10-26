
# Soldier

class Soldier:
    health=None
    strength=None

    def __init__(self,health,strength): 
        self.health=health
        self.strength=strength 
    

    def attack(self):
        return self.strength 
        
    def receiveDamage(self, damage):
        self.health -= damage
        return None

### Viking

class Viking(Soldier):
    name = ""
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"

        return f"{self.name} has received {damage} points of damage"
        
    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):

    class Saxon(Soldier):
    
    def receiveDamage(self, damage):
        #self.health = max(0, self.health-damage)
        self.health -= damage
        if self.health <= 0:
            return f"A Saxon has died in combat"

        return f"A Saxon has received {damage} points of damage"

class War:
    vikingArmy = None
    saxonArmy = None
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []


    def addViking(self, viking):
        self.vikingArmy.append(viking)
        return None

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        return None

    def vikingAttack(self):
        rand_saxon = random.choice(self.saxonArmy)
        rand_vik = random.choice(self.vikingArmy)

        result = rand_saxon.receiveDamage(rand_vik.attack())

        if "died" in result:
            self.saxonArmy.remove(rand_saxon)

        return result

    def saxonAttack(self):
        rand_saxon = random.choice(self.saxonArmy)
        rand_vik = random.choice(self.vikingArmy)

        result = rand_vik.receiveDamage(rand_saxon.attack())

        if "died" in result:
            self.vikingArmy.remove(rand_vik)

        return result

    def showStatus(self):
        if not len(self.saxonArmy):
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."

        return "Vikings and Saxons are still in the thick of battle."
    

