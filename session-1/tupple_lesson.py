#!/usr/bin/python38

my_tupple = tuple(range(0, 10))
print(my_tupple[0:3:2])

# this is impossible: my_tupple[0] = 100

def my_function():
    return (1, 2, 3)

my_other_tupple = my_function()
(a, b, c) = my_function() # this is called unpacking
print(a)
print(b)
print(c)
print(type(my_other_tupple))


# Tupple are faster than lists!
## When code is going to be called and executed for many times (milions...)
## When the size of dataset is big: 1TB of Data