class Character:
    name=""
    energy=100
    damage=30
    def fight(self, enemy):
        pass
    def rest(self, hours):
        self.energy+=5*hours
        if self.energy>100:
            self.energy=100
class Freezer:
    name = ""
    energy = 100
    damage = 30
    def freez_on(self):
        print("Freez is on!")

class CharacterFreezer(Character, Freezer):
    pass

# freezer = Freezer()
# print(f"Персонаж с заморозкой {freezer.name}, энергия {freezer.energy}, урон {freezer.damage}")
# freezer.freez_on()

fighter2 = CharacterFreezer()
fighter2.name="Sub Zero"
print(f"Fighter #2: {fighter2.name}, energy: {fighter2.energy}, damage: {fighter2.damage}")
fighter2.freez_on()
print(CharacterFreezer.mro())
print(Character.mro())
print(Freezer.mro())