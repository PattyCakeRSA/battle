import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp -= dmg
        if self.hp < self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "\nACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print(f"{i}: {item}")
            i += 1

    def choose_magic(self):
        i = 1

        print("====================")
        print(bcolors.OKBLUE + bcolors.BOLD + "\nMAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print(f"{i}: {spell.name} (cost: {spell.cost})")
            i += 1

    def choose_item(self):
        i = 1

        print(bcolors.OKGREEN + bcolors.BOLD + "\nITEMS: " + bcolors.ENDC)
        for item in self.items:
            print(f"{i}: {item['item'].name}, {item['item'].description}, x{item['quantity']}")
            i += 1