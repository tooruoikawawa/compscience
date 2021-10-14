# page 36 questions
'''
1. Unlike while loops, for loops loop for a specific amount of times
2. range()
3. 1, 2 ,3 ,4 ,5
4. The first argument indicates the start, last argument the end
5. 0 to 7 not including 7
6. The step argument
7. range(x, x, -1)
8. - for
   - a colon
   - the word in
9. A variable that contains more than one item e.g a string
10. It can loop through a string
'''

#task 1
'''
for y in range(1,11):
    print(y)
'''
'''
a = 0
while a != 11:
    a += 1
    print (a)
'''

#task 2
'''
a = int(input("Enter a value"))

for b in range(1,a+1):
    print(b)
'''

#task 3
'''
sentence = input("Write a sentence > ")
counter = 0
z = 0
while counter < len(sentence):
    if sentence[counter] == "a":
        z += 1
    if sentence[counter] == "e":
        z += 1
    if sentence[counter] == "i":
        z += 1
    if sentence[counter] == "o":
        z += 1
    if sentence[counter] == "u":
        z += 1
    counter += 1
print(z)
'''

#task 4
'''
str = input("Write a sentence:")
print(str[::-1])
'''

#task 5
'''
sentence = input("Write a sentence: ")
letter = input("Write a random letter")
counter = 0
z = 0
while counter < len(sentence):
    if sentence[counter] == letter:
        z += 1
        
    counter += 1
print(z)
'''