import random 

mysteryNumber = random.ranint(1, 100) 
score = 0 

while True: 
	guess = int(input("Guess a number between 1 and 100: ")) 
	score += 1 # the same as score = score + 1
	if guess == mysteryNumber 
		print("You guessed correctly, nice job!")
		break
	elif guess > mysteryNumber: 
		print("Too high, try again") 
	else: 
		print("Too low, try again") 

print("You took " + str(score) + " guesses")
