print("Welcome to the to do list!")
todoList = []
while True: 
	print("Enter a to add an item")
	print("Enter r to remove an item") 
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q": 
		break 
	elif choice == "a": 

		todoList.append(input("What do you want to add?: ")) 
		# add an item to the list 
		
	elif choice == "r": 
		todoList.remove(input("What do you want to remove?: "))
		# remove an item from the list 
		
	elif choice == "p":
		print(todoList)
		# print the list 
		
	else: 
		print("This is not a choice ")
		pass 