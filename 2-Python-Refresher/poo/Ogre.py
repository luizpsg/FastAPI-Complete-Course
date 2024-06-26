from Enemy import *
import random


class Ogre(Enemy):

    def __init__(self, hp: int, attack_damage: int):
        super().__init__(type_of_enemy="Ogre", hp=hp, attack_damage=attack_damage)

    def talk(self):
        return "Ogre is slamming hands all around!*"

    def smash(self):
        return "Ogre smashes you with his club!"

    def special_attack(self):
        did_special_attack_work = random.random() < 0.25
        if did_special_attack_work:
            self.attack_damage += 1
            return "Ogre has increased his attack damage by 1!"
