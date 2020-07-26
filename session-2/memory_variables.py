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


