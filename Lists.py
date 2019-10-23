# Make a list
myCars = ["Devil Sixteen", "Ferrari", "lamborghini"] 
print(myCars) 

# add an item to the list 
# append or insert 
# append will add to the back of the list
myCars.append("Mustang")
print(myCars)
favCar = input("What is your favorite car? ")
myCars.append(favCar) 
print(myCars)
# insert 
myCars.insert(3, "Maserati") 
print(myCars)
# overwrite 
myCars[4] = "Mazda" 
print(myCars)

# remove list items 
# remove, pop 
# remove will remove a specific item 
myCars.remove("Mazda") 
print(myCars)
# myCars.remove("Ford") 
# pop will remove the item at a specific index 
myCars.pop() # erase the last item 
print(myCars)
myCars.pop(1)
print(myCars) 
# len - it returns the length of a list 
print("myCars is " + str(len(myCars))+ " items long" 

print(myCars[len(myCars) -1])