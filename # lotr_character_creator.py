# lotr_character_creator.py 

def character_creator():
    print("Welcome to the LOTR-Inspired MMO Character Creator!")
    print("Available Races: Orc, Elf, Man, Dwarf, Hobbit, Goblin, Uruk")
    print("Available Classes: Warrior, Paladin, Warlock, Lorebook, Assassin, Rogue\n")

    race = input("Choose your race: ").strip().title()
    char_class = input("Choose your class: ").strip().title()

    good_races = ["Man", "Elf", "Dwarf", "Hobbit"]

    if race == "Orc" and char_class == "Paladin":
        print("Orcs can't be Paladins. Try Warlock or Warrior.")
    elif race in good_races and char_class == "Warlock":
        print(f"{race}s can’t be Warlocks. Try Lorebook or Paladin.")
    elif race == "Dwarf" and char_class == "Assassin":
        print("Dwarves can’t be Assassins. Try Warrior or Paladin.")
    elif race == "Hobbit" and char_class == "Warrior":
        print("Hobbits can’t be Warriors. Try Lorebook or Rogue.")
    elif race == "Goblin" and char_class == "Warrior":
        print("Goblins can’t be Warriors. Try Assassin or Warlock.")
    elif race == "Uruk" and char_class == "Assassin":
        print("Uruks can’t be Assassins. Try Warrior or Warlock.")
    elif race == "Orc" and char_class != "Paladin":
        print(f"Character created: {race} {char_class}")
    elif race in ["Man", "Elf"]:
        print(f"Character created: {race} {char_class}")
    else:
        print(f"Character created: {race} {char_class}")

if __name__ == "__main__":
    character_creator()

