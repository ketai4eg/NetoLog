class Character:
    def __init__(self, name, energy=100, level=1, skills=[]):
        self.name=name
        self.energy=energy
        self.skills=skills
        self.level=level
    def fight(self, enemy):
        if not isinstance(enemy, Character):
            return
        self.energy-=30
        enemy.energy-=30
        if self.energy>0:
            self.level+=1
        if enemy.energy > 0:
            enemy.level += 1

    def rest(self, hours):
        self.energy+=5*hours
        if self.energy>100:
            self.energy=100
fighter1=Character("Lu Kan")
fighter1.fights=0
fighter1.level=5
fighter2=Character("Sub Zero", 100, 6, "freezing")
fighter2.level=6
print("Begining of the competition")
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")
# fighter2.skills.append("Freezing")
# print(f"Fighter 1: {fighter1.name}, skill {fighter1.skills}")
# print(f"Fighter 2: {fighter2.name}, skill {fighter2.skills}")
# print("FIGHT!!!")
fighter1.fight(fighter2)
# fighter2.fight(fighter1.energy)
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")
print("Rest")
fighter1.rest(12)
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")
print("FIGHT!!!")
fighter1.fight(fighter2)
# fighter2.fight(fighter1.energy)
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")
print("FIGHT!!!")
fighter1.fight(fighter2)
# fighter2.fight(fighter1.energy)
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")
print("FIGHT!!!")
fighter1.fight(fighter2)
# fighter2.fight(fighter1.energy)
print(f"Fighter 1: {fighter1.name}, level {fighter1.level}, energy {fighter1.energy}")
print(f"Fighter 2: {fighter2.name}, level {fighter2.level}, energy {fighter2.energy}")