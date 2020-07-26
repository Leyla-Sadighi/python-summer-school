#!/usr/bin/python3.8

# variables are objs in memory: 
name1 = 'mojtaba'
name2 = 'leyla'
name3 = name2
name1_hex_id = hex(id(name1))
name2_hex_id = hex(id(name2))
name3_hex_id = hex(id(name3))
print(name1_hex_id)
print(name2_hex_id)
print(name3_hex_id)



# reference counting in python
# using the sys.getrefcount function increases the ref count
import sys
name1_ref_count = sys.getrefcount(name1)
name2_ref_count = sys.getrefcount(name2)
print(name1_ref_count)
print(name2_ref_count)

# However, using this function does not increase the referenece count:
import ctypes
name1_ref_count_via_ctypes = ctypes.c_long.from_address(id(name1)).value
name2_ref_count_via_ctypes = ctypes.c_long.from_address(id(name2)).value
print(name1_ref_count_via_ctypes)
print(name2_ref_count_via_ctypes)



# let's define a function to use for the abovementioned task:
def count_references(address: int):
    return ctypes.c_long.from_address(address).value
print(count_references(id(name3)))

# being playful teaches us that:
name3 = None
print(count_references(id(name3))) # we don't know what is in name3 when we set it to None








# GC: Garbage Collection
# python reclaims memory when reference count is zero
# but what about circular references? they cause memory leaks (
# by making GC impossible, then they will cause the memory location
# not to be erased!)

# GC identifies circular references!
# GC can be controlled using gc module
# GC can be turned off (GC is turned on by default)
# GC runs periodically (you may want to turn off to increase performance)
# Caviat: it does not always work (version bellow 3.4):
#   in such a situation even if one of the objs (in the circular reference situation) 
#   has a __del__() or destructor (which is called when you call del on obj)
#   then, in such a situation (that destructor exists) the order of destruction
#   might be important (for instance, first close the db connection then smt else)
#   this causes the GC to mark both of these objects as uncollectable objs
#   which may cause memory leaks (since the objs are not going to be collected
#   at least automatically)

# circular reference example:
import gc
an_obj = 123

def obj_by_id(obj_id: int):
    """
    this method looks through every object in gc to see
    """
    for obj in gc.get_objects():
        if id(obj) == obj_id:
            return "Object Exists!"
    return "Object Not Found in GC"

# now we are going to artifically create a circular reference here:
class A:
    def __init__(self):
        self.b = B(self)
        print('A: (which is self): {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, other_class):
        self.a = other_class
        print('B: (which is self): {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

# let's disable gc so that we can see what's going on 
# we need to disable it since it will kill references when objs are deleted
a_obj = A() # this will alone cause the constructor of both classes be called

# counting the references, we find out that there are two references to a_obj,
# this is because both a_obj and a_obj.b.a are pointing to this object (a_obj)
# however, a just has a_obj pointed to it
print(count_references(id(a_obj.b)))
print(count_references(id(a_obj.b.a))) 

a_obj_address = id(a_obj)
b_obj_address = id(a_obj.b)
print(obj_by_id(a_obj_address))
print(obj_by_id(b_obj_address)) # you see? both of them exist in gc

a_obj = None
print(count_references(a_obj_address)) # count should be 1 now
print(count_references(b_obj_address)) # count should be 1 now
print(obj_by_id(a_obj_address)) 
print(obj_by_id(b_obj_address)) 
# as you see a_obj is deleted but because of their circular reference type
# their reference count is non-zero so automatic erazing cannot happen (and we 
# have disabled gc as well so it can not check for circular references and 
# delete them), in fact, the fact that they still exist in gc.objects shows
# that gc was going to take care of them but we turned it off
# Now, let's run gc manually to collect!
gc.collect()
print(obj_by_id(a_obj_address)) 
print(obj_by_id(b_obj_address)) 
print(count_references(a_obj_address)) # we should get zero or meaningless objs
print(count_references(b_obj_address)) # that's because they do not exist anymore in there (smt else is probably there)
