import random

class Characters: 
    def __init__(self, name, attack, defence, special_attack, health, energy):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.special_attack = special_attack
        self.health = health
        self.energy = energy

    def attack(self):
        return self.attack

    def defend(self):
        return self.defence

    def special_attack(self):
        if self.energy >= special_attack:
            self.energy -= self.special_attack
            return self.attack * 2
        else:
            return 0

    def taken_damage(self, damage):
        self.health -= damage
    
    def is_alive(self):
        return self.health > 0