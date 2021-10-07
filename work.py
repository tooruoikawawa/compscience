import random

n1 = random.randint(0, 12) 
n2 = random.randint(0, 12) 
ans = n1*n2
print("%d * %d" %(n1,n2)) # find out the question to make life easier
# above same as - print(str(n1), "*",str(n2))
keepGoing = True

while  keepGoing:  
    guess = int(input("Guess the product of two numbers from 0 to 12 "))
    
    if guess == ans:
        print("You are correct!")
        playAgain = input("Would you like to play again? Y or N")
        if playAgain.upper() == "N":
            keepGoing = False
        elif playAgain.upper() == "Y":
            n1 = random.randint(0, 12)
            n2 = random.randint(0, 12)
            ans = n1*n2
            print("%d * %d" %(n1,n2))
            
    elif guess < ans:
        print("That's too low")
        
    else:
        print("That's too high")
    
    
print(" \nThe correct answer was %d" %(n1*n2))
print("Thanks for playing!")
print("Goodbye :)")
