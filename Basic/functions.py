# def : define
# def function_name():
#     code

# without calling the function, it will not run

def print_hello():
    print("Hello World!")


def print_hello_and_age(name, age):
    print(name, age)


print_hello()


# parameters
def print_name(name):
    print(name)


# arguments
print_name("John Smith")

# default parameters
def print_name(name="Default"):
    print(name)


# positional arguments
# positional arguments must be in the same order as the parameters so this has to be changed to print_hello_and_age("John Smith", 30).this call as positional matters
print_hello_and_age(30, "John Smith")


# keyword arguments
print_hello_and_age(age=30, name="John Smith")
