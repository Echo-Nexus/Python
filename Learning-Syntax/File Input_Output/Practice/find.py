def check() :
   word = "learning"
   with open("Python/Learning-Syntax/File Input_Output/Practice/task1.txt", "r") as f:
      data = f.read()
      if(data.find(word) != -1):
         print("Found")
      else:
         print("not found")

check()