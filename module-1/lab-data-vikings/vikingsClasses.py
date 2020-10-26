
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def resceiveDamage(self,damage):
        self.health -= damage 

    pass


#Viking
""""AQUI SIEMPRE RECIBO ESTE ERROR:

---------------------
Traceback (most recent call last):
  File "4-testsWar.py", line 36, in setUp
    cls.viking = generateViking()
  File "4-testsWar.py", line 29, in generateViking
    return Viking(cls.name, cls.health, cls.strength)
TypeError: __init__() takes 2 positional arguments but 4 were given
---------------------
""""

class Viking(Soldier):
    def __init__(self,name):
        self.name = name
       
    def resceiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return print(f"{self.name} has received {damage} points of damage")
        else:
            return print(f"{self.name} has died in act of combat")


    def battleCry():
        return "Odin Owns You All!"

    pass

# Saxon


class Saxon(Soldier):
    def __init__(self):
        super().__init__(health,strength)

    def resceiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return print(f"{self.name} has received {damage} points of damage")
        else:
            return print(f"{self.name} has died in act of combat")
 
    pass

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxon=choice(self.saxonArmy)
        viking=choice(self.vikingArmy)

        viking.resceiveDamage(damage=strength)

        return saxon.resceiveDamage(strength)

    def saxonAttack(self):
        viking=choice(self.vikingArmy)
        saxon=choice(self.saxonArmy)
        
        Saxon.resceiveDamage(damage=strength)
        
        return viking.resceiveDamage(strength)

    def showStatus(self):
        if saxonArmy==[]:
            print("Vikings have won the war of the century!") 
        elif vikingArmy==[]:
            print("Saxons have fought for their lives and survive another day...")
        else:
            print("Vikings and Saxons are still in the thick of battle.")

    pass
