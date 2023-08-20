# enumarate

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

for i, v in enumerate(list(range(100))):
    if v == 50:
        print(f'index of 50 is {i}')
