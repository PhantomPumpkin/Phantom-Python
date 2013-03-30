# just for fun!
# imports!
import simplegui
import math
import random

# global variables
starting_hp = ""
hp = ""
starting_damage = ""
damage = ""
starting_exp = ""
exp = ""
enemy_type = ""
gained_exp = ""

# handler functions
def init():
    """Initialize and start the game"""
    global starting_hp, hp, starting_damage, damage, starting_exp, exp
    starting_hp = random.randrange(1,13)
    starting_damage = int(random.randrange(1,5))
    starting_exp = 0
    exp = starting_exp
    damage = starting_damage
    print "Welcome to the start of your adventure!"
    print "Your HP is", starting_hp
    print "Your Dmg is", starting_damage
    print "Your Exp is", starting_exp
    
def get_action(action):
    """inputs from user"""
    global starting_hp, hp, starting_damage, damage, starting_exp, exp
    
def random_enemy():
    """generates a random enemy"""
    global enemy_type
    enemy_type = random.randrange(1,4)
    if enemy_type == 1:
        print "The enemy is an Orc!"
    elif enemy_type == 2:
        print "The enemy is a Human!"
    else:
        print "The enemy is a Dragon!"
def en_num_to_name():
    global enemy_type
    if enemy_type == 1:
        enemy_type = "Org"
    elif enemy_type == 2:
        enemy_type = "Human"
    else:
        enemy_type = "Dragon"
        
def attack():
    """attacks the enemy"""
    global starting_hp, hp, starting_damage, damage, starting_exp, exp, gained_exp
    enemy_hp = random.randrange(1,4)
    en_num_to_name()
    if starting_damage >= enemy_hp:
        print "You deal", starting_damage, "to ", enemy_type, "and slay it!"
        gained_exp = random.randrange(1,4)
        print "You have gained", gained_exp, "exp"
        exp = exp + gained_exp
        if exp >= 2:
            #need to figure out how to set level increments(loop?), else level up each time
            print "Congratulations!  You've leveled up!"
        gained_exp = ""
    
def look_for_enemy():
    """handler for button to generate a random enemy"""
    random_enemy()
    
    
def search():
    """searches the ground"""
    global starting_hp, hp, starting_damage, damage, starting_exp, exp
    find_item = random.randrange(1,101)
    if find_item == 100:
        print "Congratulations, you've found the Sword of 1000 Truths!"
        damage = int(damage) + 10
        print "Your damage increases to", int(damage)
    else:
        print "Sorry, you found nothing!"
    
    
# frame
frame = simplegui.create_frame("Fun Quest", 300,300)

# frame handlers
imp = frame.add_input("What do you do?", get_action, 100)
frame.add_button("Attack", attack, 100)
frame.add_button("Search", search, 100)
frame.add_button("Look for Enemy", look_for_enemy, 100)

# frame start
frame.start()
init()    

