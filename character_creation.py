from dnd import *

print("Hello, welcome to the character creator. You are playing as a HUMAN. You have a SPEED of 30. Please pick a subclass from the following options: \n")

subclass_options = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]

print(" [0] barbarian \n [1] bard \n [2] cleric \n [3] druid \n [4] fighter \n [5] monk \n [6] paladin \n [7] ranger \n [8] rogue \n [9] sorcerer \n [10] warlock \n [11] wizard \n")

subclass = float(input("What is your subclass? [select a number] "))

subclass_info = {"barbarian": "Not only do they have the highest hit point pool of any class, but their Rage ability also grants them resistance to the most common forms of damage. They're basically designed to pummel the bad guys until they drop.",
                 "bard": "Bards tend to fill something of a support role in combat, particularly with their Bardic Inspiration ability. They're also full casters, with access to cantrips and a variety of spells. Unlike Clerics and Druids, they only know a certain amount of chosen spells at any given time. Plus, Bards possess not-so-insignificant physical combat skills and thus have a lot to offer a player.",
                 "cleric": "Both Clerics and Druids use Wisdom as their spellcasting stat and have access to all their class spells (of an appropriate level) at once, with a chosen few being prepared each day for use. As such, Clerics and Druids fill pretty similar roles in a party, as support. In combat, they use their many abilities to heal, buff allies, or debuff enemies.",
                 "druid": "Both Clerics and Druids use Wisdom as their spellcasting stat and have access to all their class spells (of an appropriate level) at once, with a chosen few being prepared each day for use. As such, Clerics and Druids fill pretty similar roles in a party, as support. In combat, they use their many abilities to heal, buff allies, or debuff enemies. \n Druids also have the ability to wildshape.",
                 "fighter": "As they gain levels, Fighters become more resilient, more versatile, and most importantly they gain the ability to hit people more often. If a player is ever unsure what class would be best, it's hard to go wrong with a good old stock-standard Fighter.",
                 "monk": "Being high Dexterity characters, their abilities emphasize mobility when both attacking and defending. They can channel the ki energy in their bodies to trigger a quick flurry of unarmed blows, catching projectiles, and running up walls.",
                 "paladin": "Paladins and rangers are pretty similar when it comes to the kinds of features they get. Both are half-casters, meaning they're primarily martial fighters, but do eventually get access to a limited amount of magic. Paladins have some of the highest armor across all classes which makes them great tanks. They also have access to healing magic for good measure.",
                 "ranger": "Paladins and rangers are pretty similar when it comes to the kinds of features they get. Both are half-casters, meaning they're primarily martial fighters, but do eventually get access to a limited amount of magic. The class also allows for multiple weapon types, so players can choose between ranged or melee combat options. Rangers have the option of picking up spells, or players can choose to max into cantrips and other abilities instead.",
                 "rogue": "They're the best D&D class for beginners who want to play a martial class without swinging around a huge ax or getting in super close for a flurry of attacks.",
                 "sorcerer": "Sorcerers function as a pretty straightforward spellcasting class. Unlike Wizards, who get their powers from book learning, Sorcerers have magic in their blood. They learn more towards elemental combat with a large variety of combat cantrips and heavy-hitting spells.",
                 "warlock": "They have access to many fewer spells and have fewer spell slots than the other magical classes. However, those spells hit harder and regenerate faster. Warlocks regain their spell slots on a short rest as opposed to a long one, so they don't have to ration their magic as strictly as a Wizard usually does.",
                 "wizard": "Being high Dexterity characters, their abilities emphasize mobility when both attacking and defending. They can channel the ki energy in their bodies to trigger a quick flurry of unarmed blows, catching projectiles, and running up walls."
                }


subclass_choice = str(subclass_options[int(subclass)])

print("You have chosen the following subclass: " + str(subclass_options[int(subclass)]) + f"\n \n {subclass_info[str(subclass_choice)]}")

confirm = input("\n Continue? [y/n] ")

if confirm == "y":
    print("Now on to stats!")
    
while confirm != "y":
    print("Select again: \n")
    subclass = float(input("What is your subclass? [select a number] "))
    print("You have chosen the following subclass: " + str(subclass_options[int(subclass)]) + f"\n \n {subclass_info[str(subclass_choice)]}")
    confirm = input("\n Continue? [y/n] ")

print("Your stats will be automatically rolled for you. \n \
      If you do not like your stats, you may roll again however many times you'd like \n")

strength = roll_traits(20)
dexterity = roll_traits(20)
constitution = roll_traits(20)
intelligence = roll_traits(20)
wisdom = roll_traits(20)
charisma = roll_traits(20)

character_traits = {"strength": [strength, find_modifier(strength)],
                    "dexterity": [dexterity, find_modifier(dexterity)],
                    "constitution": [constitution, find_modifier(constitution)],
                    "intelligence": [intelligence, find_modifier(intelligence)],
                    "wisdom": [wisdom, find_modifier(wisdom)],
                    "charisma": [charisma , find_modifier(charisma)]
                   }

print(character_traits)
print("\n These are your stats. The first number is the stat, and the second is its modifier.")

roll_again = input("Roll again? [y/n] ")
    
while roll_again =="y":
    strength = roll_traits(20)
    dexterity = roll_traits(20)
    constitution = roll_traits(20)
    intelligence = roll_traits(20)
    wisdom = roll_traits(20)
    charisma = roll_traits(20)

    character_traits = {"strength": [strength, find_modifier(strength)],
                        "dexterity": [dexterity, find_modifier(dexterity)],
                        "constitution": [constitution, find_modifier(constitution)],
                        "intelligence": [intelligence, find_modifier(intelligence)],
                        "wisdom": [wisdom, find_modifier(wisdom)],
                        "charisma": [charisma , find_modifier(charisma)]
                       }
    print(character_traits)
    roll_again = input("Roll again? [y/n] ")

player_name = input("Lastly, what is your player's NAME? ")

player_complete = [subclass_options[int(subclass)], character_traits, player_name]
player_complete2 = f" SUBCLASS: {subclass_options[int(subclass)]} \n CHARACTER TRAITS: {character_traits} \n PLAYER NAME: {player_name}"

print("\n Is this all correct? \n" + player_complete2)
confirm = input("\n Continue? [y/n] ")

print(f"\n WELCOME {player_name}! Onward on our adventure! \n")

import time
for i in range(3):
    print("...")
    time.sleep(0.5)
    
# main.py

f = open("char_info.py", "w")
f.write(f"char_info = {player_complete}")
f.close()

with open("start_of_journey.py") as f:
    exec(f.read())