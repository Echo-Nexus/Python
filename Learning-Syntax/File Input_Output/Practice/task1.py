with open("Python/Learning-Syntax/File Input_Output/Practice/task1.txt", "r") as f:
   data = f.read()
   new_data = data.replace("Java", "Python")
   print(new_data)
with open("Python/Learning-Syntax/File Input_Output/Practice/task1.txt", "w") as f:
   f.write(new_data)
   