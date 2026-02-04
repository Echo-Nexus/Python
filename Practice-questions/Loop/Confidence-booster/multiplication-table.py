# Print the multiplication table of a number up to 10
# (use nested loops if you want extra practice).

num = int(input("Enter a number to print its multiplication table : "))

# Using for loop
print("Using for loop : ")
for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")

print("\n\n")

# Using while loop
print("Using while loop : ")
i = 1
while i <= 10 :
  print(f"{num} x {i} = {num * i}")
  i += 1

