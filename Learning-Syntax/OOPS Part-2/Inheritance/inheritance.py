class car:
  color = "black"
  @staticmethod
  def start():
    print("car started...")
  
  @staticmethod
  def stop():
    print("car stopped...")

class Rolls_royce (car):
  def __init__(self, name):
    self.name = name 

car1 = Rolls_royce("Phantom")
car1.start()
car1.stop()
print(car1.name)
print(car1.color)