# itarable

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
