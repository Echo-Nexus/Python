class A():
  varA = "I am varA"

class B():
  varB = "I am varB"

class C(A, B):
  varC = "I am varC"

obj1 = C()
print(obj1.varA)
print(obj1.varB)
print(obj1.varC)