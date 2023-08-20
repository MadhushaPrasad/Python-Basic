is_friend = False
is_User = True

# Short Circuiting
# Short Circuiting is a technique used to improve the performance of the program
# It is used to skip the evaluation of the second argument if the first argument is enough to determine the value of the expression
# In the below example, the second argument is not evaluated because the first argument is false
# This is called Short Circuiting


if is_friend and is_User:
    print("Best Friend Forever.!")
