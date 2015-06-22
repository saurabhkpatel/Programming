# program "Guess the number" mini-project (Reverse)
# Saurabh Patel
# skpatel@syr.edu

# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random 
import math

secret_number = 0
number_of_guesses = 0;

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "\n" 
    global secret_number,number_of_guesses
    secret_number = random.randrange(0, 100)
    number_of_guesses = int(math.ceil(math.log(100+1,2)))
    print "New game Range is [0,100)"
    print "Number of remaining guesses is "+ str (number_of_guesses)
    
    
def range1000():
   # button that changes the range to [0,100) and starts a new game 
    print "\n" 
    global secret_number,number_of_guesses
    secret_number = random.randrange(0, 1000)
    number_of_guesses = int(math.ceil(math.log(1000+1,2)))
    print "New game Range is [0,1000)"
    print "Number of remaining guesses is "+ str (number_of_guesses)
    
    
def input_guess(guess):
    # main game logic goes here
    print "\n"
    global number_of_guesses
    guess_number = int(guess)
    print "Guess was " + str(guess_number)
    number_of_guesses= number_of_guesses-1
    print "Number of remaining guesses is "+ str (number_of_guesses)
    if(guess_number==secret_number):
        print "Correct!"
        new_game()
    elif (guess_number>secret_number):
        print "Higher!"
    else :
        print "Lower!"
    if(number_of_guesses == 0) :
        print "Game Over"
        new_game()
        
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess ", input_guess, 200)
frame.start()

# call new_game 
new_game()

