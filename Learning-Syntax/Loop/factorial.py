num = int(input("Enter a number to compute its factorial : "))
factorial = 1

if num < 0 :
  print("Sorry, factorial does not exist for negative numbers")
elif num == 0 or num == 1 :
  print("The factorial of 0 is 1")
else :
  for i in range (2, num + 1) :
    factorial = factorial * i
print("The factorial of", num, "is", factorial)