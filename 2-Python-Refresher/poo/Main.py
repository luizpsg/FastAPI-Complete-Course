from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
import random


def battle(e: Enemy, e2: Enemy):
    print(e.talk())
    print(e2.talk())

    while e.hp > 0 and e2.hp > 0:
        print("------------")
        print(e.special_attack())
        print(e2.special_attack())
        print(
            f"{e.type_of_enemy}: {e.hp} HP Left | {e2.type_of_enemy}: {e2.hp} HP Left"
        )
        print(e.attack())
        e2.hp -= e.attack_damage
        if random.random() < 0.5:
            print(e2.attack())
            e.hp -= e2.attack_damage
    print("------------")
    if e.hp <= 0:
        print(f"{e2.type_of_enemy} has won!")
    else:
        print(f"{e.type_of_enemy} has won!")


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

# battle(zombie, ogre)


hero = Hero(10, 1)
weapon = Weapon("Sword", 5)
hero.weapon = weapon
hero.equip_weapon()


def hero_battle(hero: Hero, enemy: Enemy):
    print(hero.equip_weapon())
    print(enemy.talk())

    while hero.hp > 0 and enemy.hp > 0:
        print("------------")

        print(enemy.special_attack())

        print(f"Hero: {hero.hp} HP Left | {enemy.type_of_enemy}: {enemy.hp} HP Left")

        print(hero.attack())
        enemy.hp -= hero.attack_damage

        print(enemy.attack())
        hero.hp -= enemy.attack_damage

    print("------------")
    if hero.hp <= 0:
        print(f"{enemy.type_of_enemy} has won!")
    else:
        print(f"Hero wins!")


hero_battle(hero, zombie)
