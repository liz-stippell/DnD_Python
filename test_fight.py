from dnd import *
import time
from char_info import char_info

RAT_AC = 10
RAT_HP = 2
SPEED = 20

strength = 2
str_mod = -4

dexterity = 11
dex_mod = 0

constitution = 9
con_mod = -1

intelligence = 2
int_mod = -4

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
HIT = roll(20)
BITE = 1

HUMAN_AC = char_info[1]["AC"]
HUMAN_HP = char_info[1]["HP"]
print("...")
time.sleep(2)

while RAT_HP > 0 and HUMAN_HP > 0:


    if HIT <= HUMAN_AC:
        DAMAGE = 0
    else:
        DAMAGE = BITE

    print("The RAT is trying to attack!")
    print("...")
    time.sleep(2)

    HUMAN_HP -= DAMAGE
    if DAMAGE == 0:
        print("Miss!")
    else:
        print(f"Hit for {DAMAGE} HP! Health is now at {HUMAN_HP}")
    if HUMAN_HP <= 0:
        break
    print("...")
    time.sleep(2)
    
    print("What would you like to do?")

    print("[0] shortsword")
    print("[1] exit combat \n WARNING: Data will not be saved")

    answer = input("Type a number: ")

    if answer == "0":
        HIT = roll_traits(20)
        if HIT <= RAT_AC:
            DAMAGE = 0
        else:
            DAMAGE = roll(6)
    else:
        print("Exiting combat. Data will not be saved.")
        exit()

    RAT_HP -= DAMAGE
    print(RAT_HP)

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


char_info[1]["HP"] = HUMAN_HP

def replace_line(filename, line_number, text):
    with open(filename) as file:
        lines = file.readlines()
    lines[line_number] = text + "\n"
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)

filename = "char_info.py"
line_number = 0
text = str(char_info)
replace_line(filename, line_number, text)

