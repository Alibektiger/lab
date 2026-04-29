#1
a = 800
b = 111
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#2
x=54
y=32
if x>y:
  print("x > y")
else:
  print("x < y")
#3
n=99
if n % 2 == 0:
  print("even")
else:
  print("odd")
#4
username = ""

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")
#5
fullpoint=87
if fullpoint <= 50:
  print ("E")
elif fullpoint <=70:
  print("D")
elif fullpoint <=80:
  print("C")  
elif fullpoint <=90:
  print("B")  
elif fullpoint <=100:
  print("A")  