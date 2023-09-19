import random

def roll(num):
    if num == 20:
        return random.randrange(1, 20, 1)
    if num == 4:
        return random.randrange(1, 4, 1)
    if num == 6:
        return random.randrange(1, 6, 1)
    if num == 8:
        return random.randrange(1, 8, 1)
    
def roll_traits(num):
    return random.randrange(10, 20, 1)

def find_modifier(trait):
    return int((trait-10)/2)

def find_ac(dex_modifier):
    return 10+dex_modifier
### NEED TO INCLUDE ARMOR CLASS: 10 + DEXTERITY MODIFIER
