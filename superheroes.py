import random

class Ability:

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)



class Armor:

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)



class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health



    def add_ability(self, ability):
        self.abilities.append(ability)



    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()

        return total



    def add_armor(self, armor):
        self.armors.append(armor)



    def defend(self, damage_amt):
        total = 0
        for armor in self.armors:
            total += armor.block()

        return total + damage_amt



    def take_damage(self, damage):
        print(self.defend(damage))
        self.current_health = self.current_health - self.defend(damage)



    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False



    def fight(self, opponent):
        while True:
            if self.is_alive():
                attack_damage = self.attack()
                opponent.take_damage(attack_damage)
            else:
                print("Opponent Wins!")
                break

            if opponent.is_alive():
                attack_damage = opponent.attack()
                self.take_damage(attack_damage)
            else:
                print("Hero Wins!")
                break
        


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
