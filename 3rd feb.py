
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
file = open("password.txt", "w")
a = file.read()
file.close()
passw = input("Enter your password:  ")
if passw == a:
    print("Correct")
else:
    print("Wrong")
'''
#task 4
file = open("numbers.csv", "a")
counter = 0
while counter < 10:
    a = input("Enter a number")
    file.write(a + ",")
    counter+=1
data = file.read()
list = data.split(",")
file.close()
print(list)

