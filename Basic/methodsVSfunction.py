# methods vs function
# methods are functions that are associated with a particular object
# functions are not associated with particular object
# methods are called using dot notation
# functions are called using parenthesis
# methods are used with objects
# functions are used with variables
# methods are used with objects for the purpose of abstraction
# functions are used with variables for the purpose of code reuse
# methods are bound to the object
# functions are not bound to the object

# method example
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def print_student_details(self):
        print(self.name)
        print(self.roll_no)


student = Student('john', 2)
student.print_student_details()

# function example
def print_student_details(name, roll_no):
    print(name)
    print(roll_no)


print_student_details('john', 2)
