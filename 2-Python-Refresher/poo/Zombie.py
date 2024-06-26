from Enemy import *
import random


class Zombie(Enemy):

    def __init__(self, hp: int, attack_damage: int):
        super().__init__(type_of_enemy="Zombie", hp=hp, attack_damage=attack_damage)

    def talk(self):
        return "*Grumbling..*"

    def spread_infection(self):
        return "Zombie bites you and you are infected!"

    def special_attack(self):
        did_special_attack_work = random.random() < 0.55
        if did_special_attack_work:
            self.hp += 4
            return "Zombie has regenerated 4 HP!"
