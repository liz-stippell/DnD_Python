from char_info import *

#print(char_info)

import time
for i in range(3):
    print("\n ==================================================")
    time.sleep(0.5)
    
print(f"\n Welcome Adventurer! Is this you? \n {char_info[2]} \n \n These are your stats: \n {char_info[0]} \n {char_info[1]}")

confirm = input("\n Continue? [y/n] ")

if confirm == "y":
    print("\n Let's start our adventure!")

import sys
    
if confirm != "y":
    print("\n Please go to the character_creation.py to create your character and start an adventure!")
    for i in range(2):
        time.sleep(0.5)
    print("\n \n Now exiting the journey...")
    sys.exit()
    

print("\n ==================================================")

for i in range(1):
    print("You start your journey in a small town just before the entrance of a large cave system. \n")
    time.sleep(1.5)

for i in range(1):
    print("The towns folk have told you that there are hidden treasures that lie deep within the caves, but also hidden threats as well. \n")
    time.sleep(1.5)
    
for i in range(1):
    print("You approach a small marketplace, eager to get supplies to start your journey. \n")
    time.sleep(1.5)
    
for i in range(1):
    print("What appears to be a shopkeeper approaches you. She looks you up and down, smirks, and says, \"You're not from around here, are you?\"")
    time.sleep(5)
          
shopkeeper_choice = float(input("Do you: \n [1] Tell her you're here for the caves \n [2] Not say anything \n [1]/[2]: \n"))
               
if shopkeeper_choice == 1.0:
    for i in range(1):
        print("\n The shopkeeper responds: \"Ah, of course. The caves. We have exactly what you need to be going down there. I can give you an adventuring kit for 10 gold pieces.\"")
        time.sleep(5)
               
if shopkeeper_choice == 2.0:
    for i in range(1):
        print("\n The shopkeeper responds: \"A quiet one, I see... Well, I'm selling adventuring kits today for 5 gold pieces. It'll have everything you need for this small town.\"")
        time.sleep(5)
    
print("\n You begrudgingly hand over your money to the shopkeeper, and obtain an ADVENTURING KIT.")


f = open("char_info.py", "a")
f.write(f"\n adventuring_kit = [bedroll, rations, rations, rations, rations, rations, rope (50 feet), tinderbox, torch, water pouch]")
f.close()
