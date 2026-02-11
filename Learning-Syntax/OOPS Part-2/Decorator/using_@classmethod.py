class hello:
  name = "anonymous"

  @classmethod
  def change_name(cls, name):
    cls.name = name
    

p = hello()
print(hello.name)
p.change_name("Arix Ratgaiya")
print(p.name)
print(hello.name)