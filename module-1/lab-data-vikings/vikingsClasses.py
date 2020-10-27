
# Soldier


class Soldier:
	def __init__(self,health, strength):
		self.health = health
		self.strength = strength
	
	def attack(self):
		return self.strength
	
	def receiveDamage(self,damage):
		self.damage = damage
		
		
		self.health -= self.damage

		

    

# Viking


class Viking(Soldier):
	def __init__(self,name,health,strength):
		super().__init__(health,strength)
		self.name = name
	def receiveDamage(self,damage):
		self.damage = damage
		self.health -= self.damage
		if self.health == 0:
			return f"{self.name} has died in act of combat"
			
		else:
			return f"{self.name} has received {self.damage} points of damage"
	def battleCry(self):
		
		return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
	def __init__(self,health,strength):
		super().__init__(health,strength)
	def receiveDamage(self,damage):
		self.damage = damage
		self.health-= self.damage
		
		if self.health == 0:
			return f"A Saxon has died in combat"
		else: 
			return f"A Saxon has received {self.damage} points of damage"


# War


class War:
	def __init__(self):
		self.vikingArmy = []
		self.saxonArmy = []
	def addViking(self,Viking):
		self.Viking = Viking
		self.vikingArmy.append(self.Viking)

	def addSaxon(self,Saxon):
		self.Saxon = Saxon
		self.saxonArmy.append(self.Saxon)
	def vikingAttack(self):
		if (self.Saxon.health - self.Viking.damage) == self.Viking.strength:
			saxonArmy.remove(self.Saxon)

			
			
			 
	def saxonAttack(self):
		self.Saxon.health - self.Viking.strength
			
	def showStatus(self):
		if len(saxonArmy) == 0:
			return "Vikings have won the war of the century!"
		if len(vikingArmy) == 0:
			return "Saxons have fought for their lives and survive another day..."
		if  len(vikingArmy) >= 1 and len(saxonArmy) >=1:
			return "Vikings and Saxons are still in the thick of battle."






		






    	



