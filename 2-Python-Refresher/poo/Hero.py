from Weapon import *


class Hero:
    def __init__(self, hp: int, attack_damage: int):
        self.hp = hp
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Weapon = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            return f"Hero has equipped {self.weapon.weapon_type}!"

    def attack(self):
        return f"Hero attacks with his sword for {self.attack_damage} damage!"
