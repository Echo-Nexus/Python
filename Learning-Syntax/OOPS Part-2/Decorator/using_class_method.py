class hello:
  name = "anonymus"
  def __init__(self, name):
    self.__class__.name = name

p = hello("komal Chaudhary")
print(p.name)
print(hello.name)