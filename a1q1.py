#Guessing Game
#Get user to input a maximum number 
#Generate a random number between 1 and the maximum number
#Get user's guess
#Calculate the difference between max guess and the user's guess (absolute value)
#If the difference is over 50% of the max value:
#Output “WAY TOO HIGH!”
#OR 
#Output “WAY TOO LOW!”
#If the difference is under 10% of the max value:
#Output “Slightly high!”
#OR
#Output “Slightly low!”
#ELSE
#Output “Too high”
#OR
#Output “Too low”
#Try five times before telling the number

import math 
import random 

print ("Hey welcome to your guessing game")
print ("Do you think it have what it takes to guess a randomly generated number in 5 trials?")
print ("Your aim is to guess the random number generated GOODLUCK!")
max_num = int ( input("Input a maximum number (i.e. If you input 100 the code generates a random number between 1 - 100): ") ) 
random_num = random.randint (1, max_num)

for i in range (5):
    usersGuess = int( input("Input your Guess: ") )
    difference = abs (random_num - usersGuess)
    
    if usersGuess == random_num:
        break 

    if usersGuess > random_num:
        if difference > (0.35 * max_num):
            print("WAY TOO HIGH!")
        elif difference < (0.1 * max_num):
            print("Slightly high!")
        else: 
            print("Too High")

    if usersGuess < random_num:   
        if difference > (0.35 * max_num):
            print("WAY TOO LOW!")
        elif difference < (0.1 * max_num):
            print("Slightly low!")
        else:
            print("Too low")
    
if usersGuess == random_num:
    print ("Congratulations you guessed right!")

if usersGuess != random_num:
    print ("You guessed five times the random number was", random_num)
