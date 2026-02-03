# 👉 Using loops only:
# Print this pattern:
# *
# **
# ***
# ****
# *****

num = int(input("Enter a number : "))

for i in range(1, num + 1):
    for j in range(i):
        print("*", end="")
    print()


# 1
# 11
# 111
# 1111

for i in range(1, num + 1):
    for j in range(i):
        print("1", end="")
    print()


# 1
# 23
# 456
# 78910

count = 1
for i in range(1, num + 1):
    for j in range(i):
        print(count, end="")
        count += 1
    print()