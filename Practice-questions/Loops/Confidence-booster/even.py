# Print all even numbers between 1 and 100

num = int(input("Enter a number to compute even numbers up to n : "))

#Using for loop only 
for i in range( 2, num + 1, 2):
  print("Even number : ", i)

# Using for loop with if condition 
for i in range( num + 1):
  if (i % 2 == 0 and i != 0):
    print("Even number : ", i)

# Using while loop only
i = 2
while i <= num:
  print("Even number : ", i)
  i += 2

# Using while loop with if condition
i = 1
while (i <= num) :
  if (i % 2 == 0):
    print("Even number : ", i)
  i += 1

