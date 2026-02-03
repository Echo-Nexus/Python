# Reverse a number using a loop.
# Example: 123 → 321

num = int(input("Enter a number : "))
rev = 0
rem = None

#Using for loop
for i in str(num):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print("Reversed number using for loop : ", rev)

#Using while loop
while (num != 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print("Reversed number using while loop : ", rev)