from dnd import *
import time
from char_info import char_info

RAT_AC = 12
RAT_HP = 7
SPEED = 30

strength = 7
str_mod = -2

dexterity = 15
dex_mod = 2

constitution = 11
con_mod = 0

intelligence = 2
int_mod = -2

wisdom = 10
wis_mod = 0

charisma = 4
char_mod = -3

character_traits = {"strength": [strength, str_mod],
                    "dexterity": [dexterity, dex_mod],
                    "constitution": [constitution, con_mod],
                    "intelligence": [intelligence, int_mod],
                    "wisdom": [wisdom, wis_mod],
                    "charisma": [charisma , char_mod]
                   }
# Advantage on wisdom/perception
# Advantage if another rat within 5 feet

# ATTACKS
HIT = roll(20) + 4
BITE = roll(4)+2

HUMAN_AC = char_info[1]["AC"]
print(HUMAN_AC)
HUMAN_HP = char_info[1]["HP"]
print("...")
time.sleep(2)

while RAT_HP and HUMAN_HP > 0:


    if HIT <= HUMAN_AC:
        DAMAGE = 0
    else:
        DAMAGE = BITE

    print("The GIANT RAT is trying to attack!")
    print("...")
    time.sleep(2)

    HUMAN_HP -= DAMAGE
    if DAMAGE == 0:
        print("Miss!")
    else:
        print(f"Hit for {DAMAGE} HP! Health is now at {HUMAN_HP}")

    print("...")
    time.sleep(2)
    
    print("What would you like to do?")

    print("[0] shortsword")

    answer = input("Type a number: ")

    if answer == "0":
        HIT = roll_traits(20)
        if HIT <= RAT_AC:
            DAMAGE = 0
        else:
            DAMAGE = roll(6)

    RAT_HP -= DAMAGE


    print("...")
    time.sleep(2)

    if DAMAGE == 0:
        print("Miss!")
    else:
        print(f"Hit rat for {DAMAGE} HP!")

    print("...")
    time.sleep(2)

if HUMAN_HP <= 0:
    print("You Died! Start Over in Character Creation.")
else:
    print("You slayed the GIANT RAT! Gain 10XP")

## NEED TO CHANGE HP IN CHAR_INFO DOCUMENT
