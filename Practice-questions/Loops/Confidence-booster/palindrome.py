# Check whether a number is a palindrome using loops.
# Example: 121 → Palindrome

num = int(input("Enter a number : "))

ori_num = num
rev_num = 0
rem = None

#Using for loop
for i in str(num):
    rem = num % 10
    rev_num = (rev_num * 10) + rem
    num = num // 10
if ori_num == rev_num:
    print(f"{ori_num} is a palindrome using for loop")
else :
    print(f"{ori_num} is not a palindrome using for loop")


#using while loop

while num != 0 :
    rem = num % 10
    rev = ( rev * 10) + rem
    num = num // 10
if ori_num == rev_num:
    print(f"{ori_num} is a palindrome using while loop")
else :
    print(f"{ori_num} is not a palindrome using while loop")