# Count vowels and consonants in a string using a loop.

string = input("Enter a string : ")
vc = 0
cc = 0

for char in string:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vc += 1
        else :
            cc += 1
print("Vowels :", vc)
print("Consonants :", cc)