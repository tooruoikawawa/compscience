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
'''
bag = 2.23
bags = int(input("How many bags?: "))
cust = input("Are you a Gold Customer? (y/n): ")
a = bag * bags

if cust == "y":
    if a >= 25:
        disc = a / 100 * 8.5
        total = a - disc
        print(round(total,2))
    if a >= 100:
        disc = a / 100 * 13.5
        total = a - disc
        print(round(total,2))
if cust == "n":
        if a >= 25:
        disc = a / 100 * 5    
        total = a - disc
        print(round(total,2))
    if a >= 100:
        disc = a / 100 * 10
        total = a - disc
        print(round(total,2))
'''
#q3
'''
from datetime import date
date = date.today()
month = int(date.strftime("%m"))

bd = int(input("What month is your birthday?(in numbers) : "))
m1 = bd-month
if m1 >= 0:
    print(f"Your birthday is in {m1} months (This Year)")
elif m1 <= -1:
    print(f"Your birthday is in {12-m1} months (Next Years)")
else:
    exit()
'''
#q4
m = input("What type of moped would you like?\n 50cc or 250cc? : ")
d = input("Is it a weekday or weekend? : ")
h = input("How many hours do you want the moped for? : ")

if m == "50cc":
    
    