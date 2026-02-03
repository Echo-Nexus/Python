# Count digits in a given number.
# Example: 12345 → 5

num = int(input("Enter a number : "))
count = 0
rem = None

#Using for loop
for i in str(num):
    rem = num % 10
    num = num // 10
    count += 1
print("Number of digits using for loop : ", count)

#Using while loop
while (num != 0):
    rem = num % 10
    num = num // 10
    count += 1
print("Number of digits using while loop : ", count)
