#1
class M:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Hello,"+ self.name)

p1=M("Alibek")
p1.greet()
#2
class calculator:
    def add(self,a,b):
        return a+b
    def mult(self,a,b):
        return a*b
    
calc=calculator()
print(calc.add(5,3))
print(calc.mult(4,7))
#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())
#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age}"

p1 = Person("Tobias", 36)
print(p1)