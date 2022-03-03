#question 2

print("""
Welcome!

Price:
1 photo = 10c
50+ photos = 25% discount

Sizes:
 - normal
 - large (10% extra)
""")

photos = int(input("How many photos would you like to print?:  "))
size = input("What size would you like them?:  ")

if size == "normal":
    if photos >= 50:
        a = photos * 0.1
        b = a/100*25
        c = a - b
        print("Your total cost is: €", round(c,2))
    else:
        a = photos * 0.1
        print("Your total cost is: €", round(a,2))

if size == "large":
    if photos >= 50:
        a = photos * 0.1
        b = a/100*25
        c = a - b
        d = c + c/100*10
        print("Your total cost is: €", round(d,2))
    else:
        a = photos * 0.1
        b = a + a/100*10
        print("Your total cost is: €", round(b,2))



#question 4
'''
cols = int(input("How many columns?: "))
rows = int(input("How many rows?: "))

for i in range(rows):
    for i in range(cols):
        print("*", end = "")
    print()
'''

#question 15
'''
num = input("Enter a number: ")
file = open("myCSVFile.csv", "a")
file.write(num)
file.close()
'''