#!/usr/bin/python38
# shebang line


'''
my_list = []
my_list2 = list()

# is checks if the variables are actally same thing in memory (Ram)
# == checks the values inside the lists (or other things)
print(my_list is my_list2)
print(my_list == my_list2)


# note: GC
my_list = [1, 2, 3]
my_list2 = ['1', '2', '3']
print(my_list == my_list2)

'''



# put 0, 999 inside a list for me (just even number)
'''
my_list = list()

for i in range(0, 1000):
    if i % 2 == 0:
        my_list.append(i)

my_list2 = list(range(0, 1000, 2))
print(my_list)
print(my_list2)
'''


# nested lists
'''
my_list = [[1, 2, 3], [4, 5, 6], 7]
print(my_list.__len__())
print(len(my_list))
print(my_list[1][0])


# extending and appending a list with another list
my_list.extend([88888888, 0, 'mojtaba'])
print(my_list)
my_list.append([88888888, 0, 'mojtaba'])
print(my_list)
'''



'''
my_list = list(range(1, 10, 2))
my_list.sort(reverse=True)

for i in my_list:
    print('The odd number is {number}'.format(number=i))

# slicing lists:
print(my_list[0:-1:2])
'''


'''
try:
    print(my_list.index('mojtaba'))
except:
    print('mojtaba was not invited')
'''


# mutability: lists are mutable (unlike tupples and strings)
my_list = ['a', 'b', 'c', 'd']
element = my_list.pop(2) #pop means to get the element that you give to it, and delete it from list
#del my_list[2]
print(element)



# adding to specific location in list:
my_list = ['a', 'b', 'c', 'd']
#my_list[-2] = 'u'
#print(my_list)
my_list.insert(1, 'r')
print(my_list)