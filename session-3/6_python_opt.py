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

############### python compile time optimization #################
# Python does not have to recompile every time your code runs: optimization
# It will keep the compiled version as long as it is possible to use.
# Some things are kept:
#   1. Constant expression: 24 * 60 * 60 (number of seconds in a day)
#       After the first time python runs our code, it will save the result of
#       of the mentioned expression so that it can use it again.
#   2. Short sequences (length of < 20)
#       (1, 2) * 5 ===> this has 10 items, it will be stored
#       "hello world" ===> less than 20 chars, it will be stored
#       "hello" * 100 ===> probably not this one
#   3. Membership tests:
#       this snippet for instance: i is in [1, 2, 3]: this happens because
#       our list has constant things in it (items will not change), for this
#       reason, in python the lists of constants are converted into tuples
#       so that they are more efficiently evaluated for membership operator
#       Besides, sets get converted (behind the scenes) to frozensets.
#       Note: set membership is much faster than tuple membership (sets are 
#       much like dictionaries although they do not look like dicts), therefore,
#       instead of writing `if e in [1, 2, 3]` or `if e in (1, 2, 3)`
#       you should write `if e in {1, 2, 3}`.

def a_function():
    a = 24 * 60 * 60
    b = (1, 2, 3) * 4
    c = "abc" * 3
    d = 'abc' * 30
    f = ['a', 1] * 3


def b_function(e):
    if e in [1, 2, 3]:
        pass


def c_function(e):
    if e in {1, 2, 3}:
        pass

print(a_function.__code__.co_consts) # get the constants of the function code
# the above print shows us the constants that will be store and retrieved again
# without computing again.
# if you look closer ['a', 1] * 3 is not caculated and stored since lists
# are not constants (they are mutables)

print(b_function.__code__.co_consts)
# list became the tuple

print(c_function.__code__.co_consts)


import string

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(n, container):
    #repeat this test n times
    for _ in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print("run time for list: {}".format(end - start))

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print("run time for tuple: {}".format(end - start))

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print("run time for set: {}".format(end - start))

# the runing time for the sets must be lower