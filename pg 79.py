#task 1
'''
nums = [1, 2, 3, -3, 4, -4]
for item in nums:
    if item < 0:
        nums.remove(item)
print(nums)
'''
#task 2
'''
nums = [2, 43, 42, 4, 53, 29, 3, 1, 75, 54, -35, -2, 4, -643, 533, 64, 45, -54, -90, 10]
nums.sort(reverse = True)

file = open("myNumbers.csv", "w")
file.write(str(nums))
file.close()

print("The largest number in the list is: ", nums[0])
print("The lowest number in the list is: ", nums[19])
'''

#task 3
'''
import random
file = open("rand.numbers.csv", "w")
nums = []
counter = 0
while counter <100:
    file.write(str(random.randint(0,100)) + ",")
    counter += 1
file.close()
'''

#task 4
a = open("rand.numbers.csv", "r")
for item in a:
    if item >= 50:
        print(item)
file.close()