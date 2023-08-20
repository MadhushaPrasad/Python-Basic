# is_old = True
# is_licenced = True

#if statement
# if statement is used to check a condition and execute the code inside the if block only if the condition is true

is_old = bool("hello")
is_licenced = bool(5)

# Truthy and Falsy values

if is_old:
    print("You are old enough to drive.!")
elif is_licenced:
    print("You can drive now.!")
else:
    print("You are not of age.!")

print("Done")
