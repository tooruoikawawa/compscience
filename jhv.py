print("Please enter 6 numbers")
num = int(input("Enter a number:"))
total = num
while num != 0:
    num = int(input("Enter another number:"))
    total += num
print("The total is", total)