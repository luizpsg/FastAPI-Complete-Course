class Enemy:
  
  def __init__(self, type_of_enemy: str, hp: int, attack_damage: int):
    self.__type_of_enemy = type_of_enemy
    self.hp = hp
    self.attack_damage = attack_damage

  @property
  def type_of_enemy(self):
    return self.__type_of_enemy
  @type_of_enemy.setter
  def type_of_enemy(self, type_of_enemy):
    self.__type_of_enemy = type_of_enemy
  
  def talk(self):
    return (f"I am a {self.type_of_enemy} and I will destroy you!")

  def walk_forward(self):
    print(f"{self.type_of_enemy} is walking forward")

  def attack(self):
    print(f"{self.type_of_enemy} attacks you for {self.attack_damage} damage!")