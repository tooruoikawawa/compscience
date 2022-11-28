# Question 16(a)
# Student name: 

import random
def dice_game():
    print ("Welcome to my dice game!!")
    your_name = input("Please enter your name: ")
    lucky_number = int(input("Please select a lucky number between 1 and 6: "))
    #initialize computer number
    computer_die_roll = random.randint(1,6)
    print(your_name + "'s lucky number was: " + str(lucky_number))
    print("The computer rolled: ", computer_die_roll)
    #lucky number checker
    if lucky_number == computer_die_roll:
        print("You guessed correct, well done!")
    elif lucky_number > computer_die_roll:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

dice_game()


