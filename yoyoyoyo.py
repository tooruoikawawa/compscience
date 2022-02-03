#task 1
'''
name = input("What's your name?")
file = open("myTextFile.txt", "w")
file.write(name)
file.close()
'''
#task 2
'''
file = open("password.txt", "w")
file.write("password123")
file.close()
'''
#task 3
'''
file = open("password.txt", "r")
a = file.read()
password = input("Enter your password:  ")
if password == a:
    print("Correct")
else:
    print("Wrong")
file.close()
'''
#task 4
'''
file = open("numbers.csv", "a")
counter = 0
while counter < 10:
    a = input("Enter a number: ")
    file.write(a + ",")
    counter+=1
file.close()
'''
#task 5
'''
myList = []
file = open("numbers.csv", "a")
counter = 0
while counter < 10:
    nums = input("Enter a number: ")
    file.write(nums + ",")
    myList.append(nums)
    counter+=1
file.close()
myList = [float(item) for item in myList]
print(myList)
'''
#task 6

salesppl = []
totalsales = []
counter = 0

file1 = open("names.csv", "a")
file2 = open("sales.csv", "w")

a = int(input("How many salespeople are there?"))

while counter < a:
    name = input("Input salesperson name:  ")
    sales = input("Input amount of sales for the day:  ")
    salesppl.append(name)
    totalsales.append(int(sales))
    file1.write(name + ",")
    file2.write(sales + ",")
    counter+=1    

sale = sum(totalsales)
print("The total sales for today were: ")
print(sale)

file1.close()
file2.close()
