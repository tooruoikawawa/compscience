#tasks pg 189
#q1
'''
age = int(input("How old are you?: "))
testSc = int(input("What is your test score?: "))

if age <= 16 and testSc >= 80:
    print("Excellent")

if age > 16 and testSc >= 80:
    print("Good")

if age >= 0 and testSc < 80:
    print("Please try harder next time:")
'''
#q2
bag = 2.23
bags = int(input("How many bags?: "))
cust = input("Are you a Gold Customer? (y/n): ")
a = bag * bags

if cust == "y":
    if a