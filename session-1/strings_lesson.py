# statically typed ::: C/C++
# dynamically typed ::: python

'''
name = 'leyla'
age = 27
if type(age) != type(name):
    print('their type is not equal')
'''


# string concatenation
'''
name = 'mojtaba'
rest_of_sentence = ' is a good man'
print(name + rest_of_sentence)
'''


# upper-casing and lower-casing
'''
my_string = "Today is a sunny day!!!"
my_upper_string = my_string.upper()
my_lower_string = my_string.lower()
print(my_lower_string)
'''


# dir function
'''
my_string = 'mojtaba'
print(dir(my_string))
my_string = my_string.capitalize()
print(my_string)
print(len(my_string))
print(my_string.index('ba'))


try:
    print(my_string.index('u'))
except:
    # write your error phrases specific
    print('the string was probably not found in the my_string variable')

if my_string.find('u') != -1:
    print(my_string.index('u'))
else:
    print('string was not found')
print('Hello world!')
'''




# string slicing
'''
my_string = 'My name is mojtaba eshghie!!!'
print(my_string[0:10:3])
print(my_string[len(my_string)-1])
print(my_string[0:-4])
'''


# string formatting
print('enter your name')
name = input()
print('enter your age')
age = input()
print('Hello ' + name + ', you are ' + age + '.')
print('Hello {0}, you are {1}'.format(name, age)) #curly bracket
print('Hello {the_name}, you are {the_age}'.format(the_name=name, the_age=age))
print('Hello {name}, you are {age}'.format(name=name, age=age))

