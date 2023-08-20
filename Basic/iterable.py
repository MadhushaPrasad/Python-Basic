# itarable
# iterables are objects that can return one of their elements at a time, such as a list. 
# Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)


for item in user.keys():
    key, value = item
    print(key, value)
