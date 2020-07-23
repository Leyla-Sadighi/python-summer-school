#!/usr/bin/python38


#dictionaries are key:value pairs
'''
mojtaba_information = {
    'name': 'mojtaba',
    'age': '27',
    'male': True
}

persons_information = {
    'leyla' : {
        'age' : 30,
        'male': False
    },
    'mojtaba' : {
        'age': 27,
        'male': True
    }
}

dict2 = {
    1.7: 'a value',
    'a value': 1.7
}

print(dict2)
print(dict2[1.7])
print(dict2['a value'])


# keys must be hashable: int, str, and floats are hashable

dict3 = {
    [1, 2, 3]: 'a value',
    8: 'number'
}
print(dict3)


# tupple is hashable:

dict3 = {
    (1, 2, 3): 'a value',
    8: 'number'
}
print(dict3)
'''


new_dictionary = {
    'ali': 28,
    'reza': 50,
    'marjan':30
}
for key, value in new_dictionary.items():
    print('the key:value pair is {key}:{value}'.format(key=key, value=value))



# checking inclusion of strings, lists, tupples and dictionaries using in keyword
my_string = 'name'
print('i' in my_string)
if 'i' in my_string:
    print(my_string.index('i'))

print('reza' in new_dictionary)


# uniqueness of keys??? (there is no need, overwriting happens)
new_dict_2 = {
    'name': 'mojtaba',
    'name': 'leyla'
}
print(new_dict_2)



# problem: change keys to values inside the new_dictionary
changed_dictionary = dict()
for old_key, old_value in new_dictionary.items():
    changed_dictionary.update({
        old_value:old_key
    })

print(changed_dictionary)



# do you just want the keys?
print(list(changed_dictionary.keys()))



# what if order is important for us, but we still want a dictionary?
my_dictionary_list = [
    {'item1': 'value1'},
    {'item2': 'value2'}
]
print(my_dictionary_list[0])