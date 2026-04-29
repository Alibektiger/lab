#1 *args
def myfunct(*kids):
    print("The youngest child is" , kids[1])

myfunct("Anna","Jeck","Hola")
#2
def funct(*args):
    print(type(args))
    print("first args",args[0])
    print("second args",args[1])
    print("all arguments", args)

funct(580,54,56,0,45)
#3
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#4  *kwargs
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
#5
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

    
