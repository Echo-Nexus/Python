class student :
  def __init__(self, name, marks) :
    self.name = name
    self.marks = marks
  
  def avg_marks(self):
    sum = 0
    for i in self.marks:
      sum += i
    print(f"Hi, {self.name} your average marks is {sum/len(self.marks)}")


s1 = student("Komal Chaudhary", [35,64,54])

s1.avg_marks()

s2 = student("Bikram Bohara", [35,64,75])
s2.avg_marks()