import random


class Ability:
# Ability Constructor
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

# Calculates how much (Ability) damage is given to Opponent
    def attack(self):
        return random.randint(0, self.max_damage)


class Weapon(Ability):
# Calculates how much (Weapon) damage is given to Opponent
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


class Armor:
# Armor Constructor
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

# Calculates how much damage is taken from Opponent's Attack
    def block(self):
        return random.randint(0, self.max_block)


class Arena:
    #Arena Constructor
    def __init__(self):
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        name = input("Enter Ability Name:")
        max_damage = int(input("Enter (Ability)Max Damage:"))
        new_ability = Ability(name, max_damage)
        return new_ability

    def create_weapon(self):
        name = input("Enter Weapon Name:")
        max_damage = int(input("Enter (Weapon)Max Damage:"))
        Weapon = Ability(name, max_damage)
        return Weapon

    def create_armor(self):
        name = input("Enter Armor Name:")
        max_block = int(input("Enter (Armor)Max Block:"))
        return Armor(name, max_block)

    def create_hero(self):
        name = input("Enter Hero Name:")
        starting_health = int(input("Enter Starting Health:"))
        numAbilities = int(input("How many Abilities?:"))
        numWeapons = int(input("How many Weapons?:"))
        numArmor = int(input("How many Armor?:"))
        new_hero = Hero(name, starting_health)


        for ability in range(numAbilities):
            new_hero.abilities.append(self.create_ability())

        for weapon in range(numWeapons):
            new_hero.abilities.append(self.create_weapon())

        for armor in range(numArmor):
            new_hero.armors.append(self.create_armor())

        return new_hero

    def build_team_one(self):
        name = input("Enter Team Name:")
        self.team_one = Team(name)
        numHeroes = int(input("Enter (Team One)Number of Heroes:"))
        for x in range(numHeroes):
            hero = self.create_hero()
            self.team_one.heroes.append(hero)
        pass

    def build_team_two(self):
        name = input("Enter Team Name:")
        self.team_two = Team(name)
        numHeroes = int(input("Enter (Team Two)Number of Heroes:"))
        for x in range(numHeroes):
            hero = self.create_hero()
            self.team_two.heroes.append(hero)


    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        if len(self.team_one.get_living_heroes()) > 0:
            print("Your Team(team_one) Won!!!")
        else:
            print("Your Team(team_two) Won!!!")

        self.team_one.stats()
        self.team_two.stats()

        print (self.team_one.get_living_heroes())
        print (self.team_two.get_living_heroes())




class Team:
# Team Constructor
    def __init__(self, name):
        self.name = name
        self.heroes = []

# Updates Hero's List (+)
    def add_hero(self, hero):
        self.heroes.append(hero)
        return

# Updates Hero's List (-)
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        else:
            return 0

# Prints Hero List
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def get_living_heroes(self):
        living_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)
        return living_heroes

# Battle each team against each other
    def attack(self, other_team):
        # living_heroes = self.get_living_heroes()
        # opponent_living_heroes = other_team.get_living_heroes()

        while len(self.get_living_heroes()) > 0 and len(other_team.get_living_heroes()) > 0:

        # living_heroes = self.get_living_heroes()
        # opponent_living_heroes = other_team.get_living_heroes()

            selected_hero = random.choice(self.get_living_heroes())

            selected_opponent = random.choice(other_team.get_living_heroes())

            selected_hero.fight(selected_opponent)
            #randomly pick a hero
            #check if hero is alive
            #if alive set aliveHero to True

# Resets all heroes to starting_health
    def revive_heroes(self, starting_health=100):
        for hero in self.heroes:
            hero.current_health = starting_health

# Print team statistics (K:D Ratio)
    def stats(self):
        for hero in self.heroes:
            print(f"Kills: {hero.kills} and Deaths: {hero.deaths}")


class Hero:
# Hero Constructor
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.kills = 0
        self.deaths = 0

# Updates Hero's Abilities
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

# Determines Value of Hero's Attack
    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()

        return total

# Updates Hero's Armor
    def add_armor(self, armor):
        self.armors.append(armor)

# Updates N.(Deaths) from Fight
    def add_deaths(self, deaths):
        self.deaths += deaths

# Updates N.(Kills) from Fight
    def add_kills(self, kills):
        self.kills += kills

# Determines Value. of Hero's Defense
    def defend(self, damage_amt=0):
        total = 0
        for a in self.armors:
            total += a.block()

        return total + damage_amt

# Determines Health after Hero Takes Damage
    def take_damage(self, damage):
        print(self.defend(damage))
        self.current_health = self.current_health - self.defend(damage)

# (T/F) determines if I'm Alive or Not
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

# Simulates Hero vs. Opponent
    def fight(self, opponent):
        while True:
            if self.is_alive():
                attack_damage = self.attack()
                opponent.take_damage(attack_damage)
            else:
                self.add_deaths(1)
                opponent.add_kills(1)
                print("Opponent Wins!")
                break

            if opponent.is_alive():
                attack_damage = opponent.attack()
                self.take_damage(attack_damage)
            else:
                self.add_kills(1)
                opponent.add_deaths(1)
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

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
