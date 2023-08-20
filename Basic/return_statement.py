# return
# return <expression>
# return is used to exit a function and go back to the place from where it was called.

def add(a, b):
    return a + b


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum(10, 20)
print(total)
