#!/usr/bin/python3.8

# Everything in Python is an instance of some class which makes 
# everything an object!
# Classes themselves are themselves objects of class "type"
# Functions are objects of class "function"!
class MyClass:
    pass

def my_function():
    pass

print(type(MyClass))
print(type(my_function))


# What now?
# Well, objects have memory addresses!!!
print(hex(id(my_function))) 


# That means we have these consequences:
#   1. Any obj can be assign to a variable, so, everything can be 
#   assigned here including functions.
#   2. Any obj can be passed to a function. Functions, classes, ... 
#   can all be passed to functions.
#   3. Any obj can be returned from a function including functions!
#   4. We can use operators on objects (for example to compare if two
#   functions are the same)