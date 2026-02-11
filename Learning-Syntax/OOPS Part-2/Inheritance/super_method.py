class car:
  def __init__(self, type):
    self.type = type

  @staticmethod
  def start():
    print("car started...")

  @staticmethod
  def stop():
    print("car stopped...")

class rolls_royce(car):
  def __init__(self, name, type):
    super().__init__(type)
    self.name = name
    super().start()


car1 = rolls_royce("Phantom", "Rolls Royce")
car1.start()
print(car1.name)
print(car1.type)