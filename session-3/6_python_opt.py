#!/usr/bin/python3.8

######## ints between -5, 256 are supposed to be cached ########
a = 1
b = 1
print(a is b) # checks if the memory addreses are the same

a = -2222222
b = -2222222
print(a is b)


a = 10
b = 10
c = int('10')
d = int('1010', 2)
print(id(a), id(b), id(c), id(d)) # all of the id's are the same 



############### opts for strings ################
a = 'Hi! today is a very beautiful day and I am hhhhunnnngry! lets eat!'
b = 'Hi! today is a very beautiful day and I am hhhhunnnngry! lets eat!'
print(a is b) 
# in fact, when you want to compare strings, first compare them using the
# 'is' operator, and then if you realize that they do not belong tot he
# same memory location (their identity is different), you can try to compare
# them by their characters.

# We cannot rely on strings getting interned (cached the way I told),
# therefore, if needed we do it manually using the sys.intern
import sys
a = sys.intern('5_3_4_2_1'*12) # just making some string interned
b = sys.intern('5_3_4_2_1'*12)
print(a is b)

# In general, do not do it, except you have to do it. For example,
# tokenizing a large corpus of text (like what we do in NLP) may
# need interning. 

# let's show how much different these can be actually:

def compare_using_equals_operator(n):
    a = 'just some long string inside a variable that is not interned' * 200
    b = 'just some long string inside a variable that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_is_operator(n):
    a = 'just some long string inside a variable that is not interned' * 200
    b = 'just some long string inside a variable that is not interned' * 200
    for i in range(n):
        if a is b:
            pass


import time
start = time.perf_counter()
compare_using_equals_operator(10000000)
end = time.perf_counter()
delta1 = end - start

start = time.perf_counter()
compare_using_is_operator(10000000)
end = time.perf_counter()
delta2 = end - start

print(delta1)
print(delta2)