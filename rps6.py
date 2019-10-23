# Lucas Williams 
# Rock Paper Scissors 
# rps6.py 
# added comment for github

import random
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

# Welcome Message (Done)
# Print a welcome message
print("Welcome to Rock Paper Scissors")
# prompt for name
pName = input("What is your name? ")


# Score Tracker
# Make a function
def printScore():
# Prints Score:
print("Score: ")
# Shows player score
print(pName + ": " + str(pScore))
# Shows computer score
print("Computer Score: " + str(cScore))
# Shows how many ties
print("Ties: " + str(ties))

# Game Loop
# loop until q is entered
while True:
# prompt for player move (r, p, s, q)
pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit")
# print the score
printScore()
# check if q is entered if so end the game
if pMove == 'q':
break
# get a computer move (random)
cMove = random.choice(CMoves)
# compare player move with the computer move
# player picks rock
if pMove == "r":
print(pName + " picked Rock")
if cMove == "rock":
print("Computer picks Rock")
print("Tie")
ties += 1
elif cMove == "paper":
print("Computer picks Paper")
print("Paper covers Rock")
cScore += 1
else:
print("Computer picks Scissors")
print("Rock breaks scissors")
pScore += 1
# player picks paper
elif pMove == "p":
print(pName + " picked Paper")
if cMove == "rock":
print("Computer picks Rock")
print("Paper covers rock")
pScore += 1
elif cMove == "paper":
print("Computer picks Paper")
print("This is a tie")
ties += 1
else:
print("Computer picks Scissors")
print("Scissors cuts paper")
cScore += 1

# player picks scissors
elif pMove == "s":
print(pName + " picked Scissors")
if cMove == "rock":
print("Computer picks Rock")
print("Rock breaks Scissors")
cScore += 1
elif cMove == "paper":
print("Computer picks Paper")
print("Scissors cuts paper")
pScore += 1
else:
print("Computer picks Scissors")
print("This is a tie")
ties += 1
# check if pMove is valid
else:
print("That is not an option")