# *args vs **kwargs
# *args and **kwargs are used to pass a variable number of arguments to a function.
# *args is used to send a non-keyworded variable length argument list to the function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.
# *args and **kwargs are mostly used in function definitions.


def super_func(*args, **kwargs):# get multiple arguments and keyword arguments
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

super_func(1, 2, 3, 4, 5, num1=5, num2=10)


# Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, i='hi', **kwargs):
    print(name)
    print(args)
    print(i)
    print(kwargs)
    
super_func('andy', 1, 2, 3, 4, 5, num1=5, num2=10)