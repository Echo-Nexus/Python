class student :
  def __init__(self, phy, chem, bio):
    self.phy = phy
    self.chem = chem
    self.bio = bio  
    
  @property
  def percentage(self):
    return str((self.phy + self.chem + self.bio) / 3) + " %"

stu1 = student(89, 48, 69)
stu1.phy = 99
stu1.chem = 99
print(stu1.percentage)