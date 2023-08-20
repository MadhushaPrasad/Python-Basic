# range
# range() is a built-in function of Python. It's usefulness can not be summarized in a single line.
# Yet most of the newcomers and even some advanced programmers are unaware of it.
# It allows us to loop over something and have an automatic counter.
# range syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)
# range(stop)

# display number from 0 to 99

print(range(100))

for number in range(0, 100):
    print(number)

# range(start, stop, step)
# display revirse number
for number in range(100, 0, -1):
    print(number)

# list
print(list(range(0, 100)))
