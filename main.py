from classess.game import Person, bcolors
from classess.magic import Spell
from classess.inventory import Item

# Creates Black Magic
FireStream = Spell("Fire", 10, 100, "black")
ThunderClap = Spell("ThunderClap", 11, 120, "black")
Blizzard = Spell("Blizzard", 10, 100, "black")
MeteorDrop = Spell("MeteorDrop", 20, 200, "black")
Quake = Spell("Quake", 14, 140, "black")

# Creates White Magic
Cure = Spell("Cure", 12, 120, "white")
Cura = Spell("Cura", 18, 200, "white")

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully Restore HP/MP of single part Member", 999)
hi_elixer = Item("Hi-Elixer", "hi_elixer", "Fully Restore Party HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_magic = [FireStream, ThunderClap, Blizzard, MeteorDrop, Quake, Cure, Cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hi_potion, "quantity": 2},
                {"item": super_potion, "quantity": 4},
                {"item": elixer, "quantity": 8},
                {"item": hi_elixer, "quantity": 10},
                {"item": grenade, "quantity": 8}]
# Instantiate People
player = Person(450, 65, 60, 35, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("====================")
    player.choose_action()
    choice = int(input("Choose action: ")) - 1

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("====================")
        print(bcolors.FAIL + bcolors.BOLD + "\nATTACK" + bcolors.ENDC)
        print(bcolors.OKBLUE + f'Player Attack: {dmg}' + bcolors.ENDC)

    elif choice == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "Insufficient MP" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + f"\n{spell.name} Heals: {magic_dmg}" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + f"\n{spell.name} Deals: {magic_dmg}" + bcolors.ENDC)

    elif choice == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + f"\nNone Left..." + bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + f"\n{item.name} Heals: {item.prop}" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + f"\n{item.name} Fully Heals HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + f"\n{item.name} Deals: {item.prop}")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    print(bcolors.FAIL + f"Enemy Attack: {enemy_dmg}" + bcolors.ENDC)

    print("====================")
    print(bcolors.OKGREEN + bcolors.BOLD + "\nSTATUS" + bcolors.ENDC)
    print("Enemy HP: ", bcolors.FAIL + f"{enemy.get_hp()}/{enemy.get_maxhp()}" + bcolors.ENDC)

    print("Player HP: ", bcolors.OKGREEN + f"{player.get_hp()}/{player.get_maxhp()}" + bcolors.ENDC)
    print("Player MP: ", bcolors.OKBLUE + f"{player.get_mp()}/{player.get_maxmp()}" + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "Enemy defeated you" + bcolors.ENDC)
        running = False
