# Find the largest element in a list using a loop
# (do NOT use max()).
import random
import math

num1 = int(input("Enter the upper limit for random numbers : "))
num = num1
list = []
for i in range( math.trunc(100 * random.random()) + 1000):
    list.append( math.trunc(random.random() * num1))

largest = list[0]
for val in list:
    if val > largest:
        largest = val
print("The largest number in the list is:", largest)

print(math.trunc(random.random() * 10))