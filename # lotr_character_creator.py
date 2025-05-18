# lotr_character_creator.py

def character_creator():
    good_races = ["Man", "Elf", "Dwarf", "Hobbit"]
    evil_races = ["Orc", "Uruk", "Goblin"]
    all_races = good_races + evil_races

    available_classes = ["Warrior", "Paladin", "Warlock", "Lorebook", "Assassin", "Ranger", "Bard"]

    def print_options():
        print("Good Races:", ", ".join(good_races))
        print("Evil Races:", ", ".join(evil_races))
        print("Available Classes:", ", ".join(available_classes))
        print()

    print("Welcome to the LOTR-Inspired MMO Character Creator!")
    print_options()

    while True:
        race = input("Choose your race: ").strip().title()
        char_class = input("Choose your class: ").strip().title()

        # Validation Rules
        if race in evil_races and char_class == "Paladin":
            print(f"{race}s can’t be Paladins. Try Warrior or Warlock.\n")
            print_options()
        elif race in good_races and char_class == "Warlock":
            print(f"{race}s can’t be Warlocks. Try Lorebook or Paladin.\n")
            print_options()
        elif race == "Dwarf" and char_class == "Assassin":
            print("Dwarves can’t be Assassins. Try Warrior or Paladin.\n")
            print_options()
        elif race == "Hobbit" and char_class == "Warrior":
            print("Hobbits can’t be Warriors. Try Lorebook or Assassin.\n")
            print_options()
        elif race == "Goblin" and char_class == "Warrior":
            print("Goblins can’t be Warriors. Try Assassin or Warlock.\n")
            print_options()
        elif race == "Uruk" and char_class == "Assassin":
            print("Uruks can’t be Assassins. Try Warrior or Warlock.\n")
            print_options()
        elif race not in all_races:
            print("That race does not exist. Please choose from the list below.\n")
            print_options()
        elif char_class not in available_classes:
            print("That class does not exist. Please choose from the list below.\n")
            print_options()
        else:
            print(f"Character created: {race} {char_class}")
            break

if __name__ == "__main__":
    character_creator()
