# Using while loop with if condition

num = int(input("Enter a number : "))
i = 1
while i <= num :
  if (i % 2 == 0):
    print("Even number : ", i)
    i += 1