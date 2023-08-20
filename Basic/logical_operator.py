is_friend = True
is_User = False

# logical operator : and, or, not
# Logical operators are used to combine conditional statements
# and: returns true if both statements are true
# or: returns true if one of the statements is true
# not: reverse the result, returns false if the result is true

if is_friend and is_User:
    print("Best Friend Forever.!")
elif is_friend and not is_User:
    print("You are not my friend.!")
    