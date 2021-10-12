# page 30 questions
'''
1. George Boole was an English mathematician and worked at the Queen's College in Cork
2. Boolean Logic.
3. They are used for comparing one item to another and recording the result.
4. == - is equal to
   != - is not equal to
   < - less than
5. True or False
6. False
7. Comparisons that give a True or False aswer ar Boolena expressions.
8. An expression consists of values and operators and always evaluates to a single value.
9. and, or, not
10. To show every result that can occur when a Boolean operator is used.
11.
12. - True
    - True
    - False
    - False
13. A conditional is used for for testing if a Boolean expression is True or False.
14. Branches in code are executed when the variable is True
15. if
16.
17.
18. When the conditional is false.
19.
20. after if and before else
'''
# tasks page 30-31

#task 1
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a%b > 0:
    print("This number does not divide perfectly")
else:
    print("This number divides perfectly")    
'''

#task 2
'''
print("Welcome! \nLet's see if you are eligible for a driver's license.")
age = int(input("Enter your age:"))
if age >= 17:
    print("You are eligible for a driver's license!")
    
else:
    print("Your still too young!")
    ageLeft = 17 - age
    print("You only have ", ageLeft, " years left.")
'''

#task 3
'''
print("Welcome to Rogerson's Robotics Factory! \nFind out what purchasing policy applies to you based on the cost of your item.")
cost = int(input("Input the cost of the item: "))
if cost >= 10000:
    print("You must go to a tender")
elif cost >= 500:
    print("You should get 3 more quotes from other suppliers first")
else:
    print("You can buy it right now!")
'''

#task 4
'''
ans = input("Welcome! \nTo win free weekend Luas tickets to a location in Dublin,\nplease enter A, B or C.")
if ans == str("A"):
    print("You have won tickets to Dundrum Shopping Centre!")
elif ans == str("B"):
    print("You have won tickets to Tallaght!")
elif ans == str("C"):
    print("You have won tickets to Broombridge!")
else:
    print("Invalid entry.")
'''

#task 5
'''
per = int(input("What percentage did you get on your LC Computer Science Exam?"))
print("You entered", per,"%")

if per <= 29:
    print("Your grade is H8")
elif per <= 39:
    print("Your grade is H7")
elif per <= 49:
    print("Your grade is H6")
elif per <= 59:
    print("Your grade is H5")
elif per <= 69:
    print("Your grade is H4")
elif per <= 79:
    print("Your grade is H3")
elif per <= 89:
    print("Your grade is H2")
elif per <= 100:
    print("Your grade is H1 \nCongrats!!")
else:
    print("Invalid entry")
'''

# page 33 questions
'''
1. Iteration occurs when the computer is instructed to carry out a task over and over again
   by repeating a section of code.
2. A loop is a section of code that is repeated over and over again
3. A while loop keeps repeating while a certain condition is true
4. A boolean value
5. True
6. :
7. The while clause is indenting a block of code after using while
8. - a loop control variable
   - the word while
   - a boolean expression
   - a colon
   - an indented block of code on the next line
   - a way of changing the loop control variable
9. To get an infinite loop the condition should always stay True
10. - to check if the data a user inputs is correct
    -
11. OBOE is an off-by-one error and occurs when a loop is repeated to many or too little times
12. Initialise the loop counter to 0 and use the test condition counter < N
13. A sentinel controlled loop is used for validation of data
'''

# tasks page 33

#task 1
'''
counter = 1000
while counter <= 1500:
    print(counter)
    counter+=1
print("done")
'''

#task 2
print("Please enter 6 numbers")
num = int(input("Enter a number:"))
total = num
while num != 0:
    num = int(input("Enter another number:"))
    total += num
print("The total is", total)
