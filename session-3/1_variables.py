#!/usr/bin/python3.8

'''
In Java, C, and C++ variables have a static type, but in python 
the variables do not really have a type. Variables are "just" a 
reference to a an object in memory, and that means there is no 
type attached to variables. 

'''
a = 1
print(type(a))
a = 'hello'
print(type(a)) # type is changed 




'''
variable reassignment:
'''
a = 1
a = 2 # a new obj is created at a new memory address and the reference of
# a is going to be changed to this new memory location (any we know what
# will happen to the previous mem location if there is no other reference to it)



# note: you can create ints of different bases using int():
a = int() # a will be zero
a = int('1', base=2) # first argument should be string ::: not an integer? surprising hah?