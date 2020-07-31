#!/usr/bin/python3.8



'''
    Immutalbe objs are generally safe from un-intended side-effects
'''
def my_process(s):
    s = s + ' world'
    return s

my_var = 'hello' 
variable = my_process(my_var) #my_var's reference is passed to my_process
print(variable)
print(my_var)
# thus, s inside the my_process points to the same place where my_var is
# pointing to. But when is changing inside my_process it is no longer pointing
# to the same thing that my_var is pointing to. Therefore, immutability here
# makes scoping possible for strings. What about lists?
# Unfortunately, the same thing does not hold for mutables: take a look:

def a_list_processor(a_list: list):
    a_list.append('new item')
    return a_list

a_list = [1, 2, 3]
print(a_list_processor(a_list=a_list))
print(a_list) # the value of a_list is changed!

# The above example leads us to the point that: 
# Mutable objects are not safe from un-intended side-effects





# What about immutalbe collection objs that contain mutables?

def process(t: tuple):
    t[0].append(3) # adding an element to a list inside a tupple

my_tuple = ([1, 2], 'e')
process(my_tuple)
print(my_tuple)