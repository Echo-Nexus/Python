class student :
  def __init__(self, name):
    self.__name = name #It is private using underscore before the variable

s1 = student("Komal Chaudhary")
print(s1.name)  #It will throw an error.
print(s1._student__name)  #It will show the actual value.