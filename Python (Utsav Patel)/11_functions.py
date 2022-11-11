# # Simple Function
#
# def something():
#     print("Hello World!")
#
# something()

##################################################################################

# # Argument Function
#
# def some(name, age):
#     print("Name is ", name)
#     print("Age is ", age)
#
# some("Utsav", 28)

##################################################################################

# # key word Function
#
# def some(name, age, course):
#     print("Name is ", name)
#     print("Age is ", age)
#     print("Course is ", course)
#
# some(age=28, course="Python", name="Utsav")

##################################################################################

# # Return Value function
#
# def some(a, b):
#     return a+b*a-b+a%b
#
# x = 30
# y = 10
# print(some(x,y))

##################################################################################

# # default value function
#
# def some(name="Guest", age=18, course="Python"):
#     print("Name is", name)
#     print("Age is", age)
#     print("Course is", course)

# some("Utsav")
# some("Utsav", 28)

##################################################################################

# args function
def some(*args):
    print(args)
    for x in args:
        print(x)

some(12,43,6)
some(12,43,6,654,876,9,76)
some(12)

a = (12)
print(type(a))

##################################################################################

# # kwargs functions
#
# def some(a,b,*args,**kwargs):
#     print(kwargs)
#     print(args)
#
# some(2,4,Name="Utsav", Age=28, Course="Python")
# some(21,54,Name="Utsav", Age=28, Course="Python", id=9)
# some(23,54,32,Name="Utsav")
# some(323,3,12)

##...........................................................................

# Python program to illustrate
# *kwargs for variable number of keyword arguments

# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print ("%s == %s" %(key, value))

# # Driver code
# myFun(first ='Geeks', mid ='for', last='Geeks')

"""
output :
last == Geeks
mid == for
first == Geeks
"""

##...........................................................................

# def myFun(arg1, arg2, arg3):
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)
	
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)

# kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
# myFun(**kwargs)

"""
output :
arg1: Geeks
arg2: for
arg3: Geeks
arg1: Geeks
arg2: for
arg3: Geeks
"""

##...........................................................................

# def myFun(*args,**kwargs):
# 	print("args: ", args)
# 	print("kwargs: ", kwargs)


# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

"""
output :
args: ('geeks', 'for', 'geeks')
kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
"""

