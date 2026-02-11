class student :
  def __init__(self, phy, chem, bio):
    self.phy = phy
    self.chem = chem
    self.bio = bio  
    self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"
  def calPercentage(self):
    self.percentage = str((self.phy + self.chem + self.bio) / 3) + "%"

stu1 = student(89, 48, 69)
stu1.calPercentage()
print(stu1.percentage)
stu1.phy = 99
stu1.calPercentage()
print(stu1.percentage)