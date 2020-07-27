#!/usr/bin/python3.8

# chaning the data inside the object is called modifying the internal 
# state of the object.

# mutable obj: an object whose internal state can be changed
# immutable obj: an object whose internal state cannot be changed

# immutables: numbers (all kind of them), tupples, strings, frozen sets
#   user-defined classes can also be immutable if you define your own 
#   class and you don't allow for any way of modiffying the internal state of it
# mutables: lists, sets, dictionaries,
#   you can also define mutable user-define classes


# challenge: mutable inside an immutable (nested)
my_tuple = ([1, 2], [3, 4])
my_tuple[0][0] = 333
print(my_tuple)