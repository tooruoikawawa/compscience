'''
1. a model is a block of code or logic that takes in an argument or multiple arguments and returns a result or set of results
2. models are used to stimulate what is happening in the system that the model represents
3. computer modelling is any activity that involves using software abstractions to represent a real or virtual problem
4. a model is a block of code or logic that takes in an argument or multiple arguments and returns a result or set of results, scenarios are conditions pr 
   or situations in the enviroment that can change, stimulation refers to running a model to allow different scenarios to be tested.
5. This function can have a number of arguments but only one expression, which is evaluated and returned.
6. It might need another number to compare off of.
7. Covid-19
'''
#task 1
'''
import random as r
def dice():
    return r.randint(1,6)
a = int(input("Choose a random number on a dice: "))
if a == dice():
    print ("wow well done")
else:
    print("ur wrong")
'''
#task 2
