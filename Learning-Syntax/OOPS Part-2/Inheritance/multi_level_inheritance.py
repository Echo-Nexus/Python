class car:
  @staticmethod
  def start():
    print("car started...")
  
  @staticmethod
  def stop():
    print("car stopped...")

class Rolls_royce (car):
  def __init__(self, brand):
    self.brand = brand 

class phantom (Rolls_royce):
  def __init__(self, type):
    self.type = type

car1 = phantom("Phantom")
car1.brand = "Rolls Royce"
car1.start()
print(car1.brand)
print(car1.type)