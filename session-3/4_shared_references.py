#!/usr/bin/python3.8

# These two guys acutally point to the same memory location!
# Python's memory manager decides to use the same reference:
# Is this safe? Yes! Since hese objects are immutable if we 
# modify a, we do not actually modify its value, rather, 
# we leave the previous value of a alone and we put another 
# object in the memory to represent a.
a = 10
b = 10

# The same is true for these:
str_1 = 'hello'
str_2 = 'hello'

# Let's test the theory:
print(hex(id(str_1)) == hex(id(str_2))) # This will evaluate to True!


# Does this hold even for mutables? No!
list_1 = [1, 2]
list_2 = [1, 2]
print(hex(id(list_1)) == hex(id(list_2))) # This will evaluate to False!


# The above point is the main reason that == and is operators do not yield
# the same results! `is` operator checks if the two operands share the
# reference (are they pointing to the same place in memory)? Whereas, ==
# only looks at their value. 


# `None` value is always a shared reference. That's why we can always
# use `is` operator for checking if a variable is set to something (
# other than None).
a = None
b = None
print(id(a))
print(id(b))