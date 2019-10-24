myWord = "christmas" 

choice = input("Type a word: ") 

if choice =
else: 
	print("Not a match") 

# how to check if a letter is in a word 's a match")                                                             
letter = input("Type a letter") 
if letter in myWord: 
	print("Letter is in the word")
else: 
	print("Letter is not in the word") 

count = 0 
for s in myWord: 
	if s == letter: 
		print(count)
	count += 1 

# how to keep track of misses
secret = "christmas"
misses = 0 
secret = list(secret)

hangList = []

while misses < 7: 
	guess = input("Guess a letter: ")
	if guess in secret: 
		# loop through secret and find all the matching letters 
		print("That letter is in the secret word")
	else:
		misses = misses + 1 