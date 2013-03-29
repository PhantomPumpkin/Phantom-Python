Phantom-Python
==============

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code
secnum = ""
guessnum = ""
maxguess = ""
gamewon = ""
num_range = 100
# define event handlers for control panel
def init():
    global secnum, maxguess, gamewon, prevguess
    if num_range == 100:
        maxguess = 7
    else:
        maxguess = 10
    if num_range == 100:
        secnum = random.randrange(0,100)
    else:
        secnum = random.randrange(0,1000)
    gamewon = ""
    print "A secret number exists!"
    print "The range is", num_range
    print "Enter a guess."
    print "You have", maxguess, "guesses remaining"
    print ""

def get_input(guess):
    global guessnum, secnum, maxguess, gamewon, prevguess
    guessnum = int(guess)
    if guessnum == secnum:
        maxguess = 0
        gamewon = 1
        print "You guessed", guessnum
        print "Congrats, you guessed the number!  The world is now safe from certain DOOM!"
        print "A new game will automatically be started.  Aperture Laboratories would like to thank you for playing."
        print ""
    elif guessnum > secnum:
        maxguess = maxguess - 1
        print "You guessed", guessnum
        print "The Secret Number is Lower!"
    else:
        maxguess = maxguess - 1
        print "You guessed", guessnum
        print "The Secret Number is Higher!"
    if gamewon == 1:
        init()
    else:
        if maxguess == 0:
            print "The secret number was ", secnum
            print "Game over, no more guesses remaining!"
            print "The world will now 'asplode in 5...4...3...2...1..."
            print "Game is automatically restarting..."
            print ""
            init()
        else:
            print "You have", maxguess,"guesses remaining!"
            print "Guess again!"
            print ""
       
            
        
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    print "Game restarting, range 0-100"
    print ""
    init()
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    print "Game restarting, range 0-1000"
    print ""
    init()
def restart_game():
    init()

    
# create frame
frame = simplegui.create_frame("Guess the Number", 300,300)

# register event handlers for control elements
inp = frame.add_input("Enter your guess", get_input, 100)
frame.add_button("Restart the game", restart_game, 100)
frame.add_button("Set range to 100", range100, 100)
frame.add_button("Set range to 1000", range1000, 100)


# start frame
frame.start()

init()
