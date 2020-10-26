
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
    def __init__(self, name, health, strength):
        self.health = []
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        if damage in self.health:
            self.health.remove(damage)

    def battleCry(self, damage):
        self.damage = damage
        if damage in self.health:
            self.health.remove(damage)


# Saxon


class Saxon:
    pass

# War


class War:
    pass
