import random
print("Get a random card out of a deck of cards!!")

suits = [" hearts", " clubs", " spades", " diamonds"]
faces = [" A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10", " King", " Queen", " Jack"]


for i in range(5):
    print("You got: ", str(suits[random.randint(0, 3)]}, {faces[random.randint(0, 12)]})