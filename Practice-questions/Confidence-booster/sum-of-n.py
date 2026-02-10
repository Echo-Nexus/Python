# WAP to find the sum of first n natural numbers 

num = int(input("Enter a number : "))
sum = 0

# Using for loop
for i in range(num + 1):
  sum += i
print("The sum of first", num, "natural numbers is : ", sum)

# Using while loop
i = 0
while 0 < num:
  sum += i
  num -= 1
print("The sum of first", num, "natural numbers is : ", sum)