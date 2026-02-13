#1
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
    
