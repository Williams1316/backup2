import time 
import os

frameList = [ 
''' 
   +---+ 
   o   |
  /|\  | 
  / \  |
      ===''',''' 
   +---+ 
  \o/  | 
   |   | 
   \\\\  |
      ==='''
] 

while True: 
	for frame in frameList:
		os.system("cls")
		print(frame) 
		time.sleep(.2) 

