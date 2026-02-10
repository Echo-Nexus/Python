import os

# Let's assume you run this script.
# __file__ will contain the string: 'd:\Coding\Python\Practice-questions\File I0\test.py'
file_path = os.path.join(os.path.dirname(__file__), "hello.txt")

with open(file_path, "r") as f:
    content = f.read()
    print(content)
import os

file_path = os.path.join(os.path.dirname(__file__), "hello.txt")

with open(file_path, "r") as f:
    content = f.read()
    print(content)