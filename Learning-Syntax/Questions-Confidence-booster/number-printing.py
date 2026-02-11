#Print numbers from 1 to n using: for loop & while loop

num = int(input("Enter a number : "))

#Using for loop
for i in range( 1, num + 1):
  print("Using for loop : ", i)

print("\n\n")
#Using while loop
i = 1
while i <= num:
  print("Using while loop : ",i)
  i += 1
