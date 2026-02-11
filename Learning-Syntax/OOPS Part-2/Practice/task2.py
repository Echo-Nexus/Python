class employee:
  def __init__(self, role, department, salary):
    self.role = role
    self.department = department
    self.salary = salary

  def showDetails(self):
    print(f"Role : {self.role}")
    print(f"Department : {self.department}")
    print(f"Salary : {self.salary}")

class engineer (employee):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    super().__init__("Engineer", "IT", 50000)

engg1 = engineer("Komal Chaudhary", 18)
engg1.showDetails()