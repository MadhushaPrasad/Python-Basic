# scope
# Scope - what variables do I have access to?
# Python has functional scope

if True:
    x = 10


def my_method():
    total = 10


print(total)  # NameError: name 'total' is not defined

print(x)  # 10 - x is in the global scope and is accessible anywhere in the program

# scope reules
# 1 - start with local
# example:


def my_method():
    total = 10
    # total is in the local scope and is accessible only inside the function
    print(total)


# 2 - parent local?
    # example:
def my_method():
    total = 10
    # total is in the local scope and is accessible only inside the function
    print(total)

    def my_child_method():
        # total is in the local scope and is accessible only inside the function
        print(total)
    # 10 - total is in the parent local scope and is accessible inside the child function
    my_child_method()


# 3 - global
    # example:
total = 100

def my_method():
    total = 10
    # total is in the local scope and is accessible only inside the function
    print(total)

    def my_child_method():
        # total is in the local scope and is accessible only inside the function
        print(total)
    # 10 - total is in the parent local scope and is accessible inside the child function
    my_child_method()


# 100 - total is in the global scope and is accessible anywhere in the program
print(total)

# 4 - built in python functions
# example:
total = 100


def my_method():
    total = 10
    # total is in the local scope and is accessible only inside the function
    print(total)

    def my_child_method():
        # total is in the local scope and is accessible only inside the function
        print(total)
    # 10 - total is in the parent local scope and is accessible inside the child function
    my_child_method()


# 100 - total is in the global scope and is accessible anywhere in the program
print(total)
# 5 - len is a built in python function and is accessible anywhere in the program
print(len('hello'))
