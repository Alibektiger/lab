#1
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#2
def my_function(country = "Kazakhstan"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#3
def plus(x,y):
   return x+y
result=plus(5,13)
print(result)
