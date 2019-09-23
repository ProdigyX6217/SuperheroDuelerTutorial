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

        pass



class Hero:

    def __init__(self, name, starting_health):
        self.name = name
        self.starting_health = starting_health

    def add_ability(self, ability):

        pass

    def attack(self):

        pass

    def defend(self, incoming_damage):

        pass

    def take_damage(self, damage):

        pass

    def is_alive(self):

        pass

    def fight(self, opponent):

        pass

    if __name__ == "__main__":
    # Run File, Execute Code
        ability = Ability("Debugging Ability", 20)
        print(ability.name)
        print(ability.attack())
