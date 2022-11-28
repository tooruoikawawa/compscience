#Question 16 (b)
#Student name:
import random
ticket = []
counter = 0
while counter <3:
    user_number = int(input ("Please pick a number between 1 and 10: "))
    ticket.append(user_number)
    counter +=1

print ("Your ticket is: ", ticket)
print ("The draw will start now, good luck!")

drum = [1,2,3,4,5,6,7,8,9,10]
result = []
def lotto (ticket,drum):
    for times in range (3):
        draw = drum [random.randint (0,len (drum))-1]
        result.append (draw)
        drum.remove(draw)
    print("The draw was: ", result)
    
    if result == ticket:
        print("You win!")
    else:
        print("You lose!")

lotto (ticket,drum)
