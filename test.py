#question 16 (a)
# (i)

pin = "1579"

userTry = input("Enter PIN: ")
# the input command is assigning the PIN inputted by the user into the variable userTry
if userTry == pin:
    print("Welcome")
    
# (ii)

pin = "1579"

userTry = input("Enter PIN: ")

if userTry == pin:
    print("Welcome")
else:
    print("Incorrect PIN")
    
# (iii)

pin = "1579"
loggedIn = False

userTry = input("Enter PIN: ")

if userTry == pin:
    print("Welcome")
else:
    print("Incorrect PIN")
    
    
# (iv)

pin = "1579"
loggedIn = False
userTry = input("Enter PIN: ")
if userTry == pin:
    print("Welcome")
    loggedIn = True
else:
    print("Incorrect PIN")
    
# (v)

pin = "1579"
loggedIn = False

while loggedIn = False:
    userTry = input("Enter PIN: ")
    if userTry = pin:
        loggedIn = True
        print("Welcome")
    else:
        print("Incorrect PIN")
        
# (vi)

pin = "1579"
loggedIn = False
failedAttempts = 0

while loggedIn == False:
    userTry = input("Enter PIN: ")
    if userTry == pin:
        loggedIn = True
        print("Welcome")
    else:
        print("Incorrect PIN")
        failedAttempts += 1
        print("You've had", failedAttempts, " failed attempts")
        
# (vii)
pin = "1579"
loggedIn = False
failedAttempts = 0

while failedAttempts != 3:
    userTry = input("Enter PIN: ")
    if userTry == pin:
        loggedIn = True
        print("Welcome")
        break
    else:
        print("Incorrect PIN")
        failedAttempts += 1
if failedAttempts == 3:
    print("You have entered the PIN incorrectly 3 times.")
    
