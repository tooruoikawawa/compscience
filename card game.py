import random
print("Get a random card out of a deck of cards!!")

suits = [" hearts", " clubs", " spades", " diamonds"]
a = random.randint(0, 3)
faces = [" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10", " King", " Queen", " Jack"]
b = random.randint(0, 12)

for i in range(5):
    print("You got: ", faces[b] + suits[a])
    
# problem = it prints 5 of the same card, im not sure how to fix it
      
      
