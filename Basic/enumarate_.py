# enumarate
# enumarate is a built-in function of Python. It's usefulness can not be summarized in a single line. 
# Yet most of the newcomers and even some advanced programmers are unaware of it. 
# It allows us to loop over something and have an automatic counter. 

# Here is an example:

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

for i, v in enumerate(list(range(100))):
    if v == 50:
        print(f'index of 50 is {i}')
