'''
Uzair Anjum
14/10/2022
purpose: make a guessing game
'''

#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed low, high, or exactly right.
#Keep the game going until the user types "exit"
#Keep track of how many guesses the user has made, and when the game ends, print this out.
#Hint: import random library at the beginning of the code "import random" and use this function to generate a number between 1-9 "random.randint(1,9)"

import numbers
from pickle import TRUE
import random
#Provide instructions to the end user explaining the purpose of the application.
print("this is a game where you have guess the correct number and we will tell you if you are HIGHER or lower")
choice= input("would you like to coninue:(Y/N):").upper
if choice == "N":
    print("good bye")
    exit()
    #store value
random_num= random.randint(1,9)
while TRUE:
    user_guess= (input("guess the random number:"))
    if user_guess== "exit":
        break
    user_guess= int(user_guess)
    if user_guess > random_num:
         print("higer")
    if user_guess<random_num:
        print('lower')
    elif user_guess == random_num:
        print("exactly right")
    
print("thanks for playing")
quit
        
    
                


