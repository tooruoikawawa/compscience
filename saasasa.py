import lib as m
myList = []

for i in range (0,9):
    a = int(input("Enter a number: "))
    myList.append(a)

file = open("numbers.csv", "w")

for i