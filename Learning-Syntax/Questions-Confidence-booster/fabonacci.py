#Generate the Fibonacci series up to n terms using a loop.

num = int(input("Enter a number : "))

a = 0
b = 1

for i in range(num):
    print(a, end= " ")
    c = a + b
    a = b
    b = c

# Using loops only : 

a = 0
b = 1
print("\nUsing while loop:")

while num > 0:
    print(a, end = " ")
    c = a  + b 
    a = b
    b = c
    num -= 1
