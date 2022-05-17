#qs page 213
'''
1. a key
2. a linear search algorithm works by iterating through each item in a list
3. binary search differs from linear search as it requires that the list is already sorted
4. a half-interval search
5. binary search works by taking a sorted list. it first selects the item in the middle of the list, then if the key is lower than
   the middle interval it will search through the items in the lower half (first index) of the list and ignore the upper half (last
   index) and vice versa
6. the first and last index
7. the middle item in a list
'''

#task 1
'''
a = [19,87,1,-1,11,0,4,33,19]
key = -1
for index in range(len(a)):
    if a[index] == key:
        location = index
print("Key found at: ", location)
'''

#task 2
'''
a = [19,87,1,-1,11,0,4,33,19]
a.sort()
print(a)
def searchloop(listIn, key):
    first = 0
    last = len(listIn) - 1
    while(last - first) >= 0:
        middle = first + ((last - first)//2)
        if listIn[middle] == key:
            return middle
        elif key < listIn[middle]:
            last = middle - 1
        else:
            first = middle + 1
print(searchloop(a,19))
'''

#task 3
# linear search algorithms search through every item in the list while in binary search algorithms, it only searches through numbers
# < or > the middle interval, also the list must be sorted