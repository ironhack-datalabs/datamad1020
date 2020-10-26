
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


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass





#Purria para probar
warrior_of_the_barrio = Soldier(60,15)
print(warrior_of_the_barrio.attack())

print(warrior_of_the_barrio.receiveDamage(20))
print(warrior_of_the_barrio.health)