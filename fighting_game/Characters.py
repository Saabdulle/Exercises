class Characters: 
    def __init__(self, name, attack, defense, special, health, energy):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.special = special
        self.health = health
        self.energy = energy

    def attack(self, other):
        print(f"{self.name} attacks {other.name}")
        damage = self.attack - other.defense 
        if damage < 0:
            damage = 0
        other.health -= damage
        self.energy -= 1
        print(f"{self.name} used 1 energy point")
        print(f"{other.name} loses {damage} health points")


    def defense(self):
        print(f"{self.name} defends")
        self.energy += 1
        print(f"{self.name} gains 1 energy point")

    def special(self, other):
            print(f"{self.name} does a special attack on {other.name}")
            damage = self.special - other.defense
            if damage < 0:
                damage = 0
            other.health -= damage
            self.energy -= 2
            print(f"{self.name} loses 2 energy points")
            print(f"{other.name} loses {damage} health points")
