#page 202 + 203
'''
1. using a return value in a function may be more suitable than just displaying the result because you might
   want to use it for some other purpose in the program
2. return
3. it is useful to return boolean values from a function because it allows us to control the flow of
   a program
4. - the function name
   - the argument
   - what does the function test
   - the boolean value
'''
#task 1
'''
def valueOfPi():
    return 22/7
print(valueOfPi())
'''
#task 2
'''
def numbers(a,b):
    return a/b
print(numbers(6,3))
'''
#task 3
'''
def sentence(a):
    return a.count(" ")
print(sentence("hello my name is carla"))
'''
#task 4
'''
def boolean(a,b):
    if a%b == 0:
        return True
    else:
        return False
print(boolean(6,3))
'''
#task 5
'''
a= [1,2,3,4,5]
def program(listt,valuee):
    value = 0
    for item in listt:
        if item == valuee:
            value += 1
    return value
print(program(a,3))
'''
#task 6
'''
def program(RRP,discount):
    saleprice = RRP - discount * RRP/100
    return saleprice
for i in range(6):
    price = int(input("enter a price: "))
    disc = int(input("enter a discount: "))
    print("The new saleprice is" + str(program(price,disc)))
'''
#task 7
def temp(value,scale):
    ftc = (value - 32) * 0.5666
    ctf = (value * 1.8) + 32
    return temp
a = input("Would you like to convert to celsius or fahrenheit?: ")
if a 
    