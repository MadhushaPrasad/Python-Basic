# while loop
# while loop is used to execute a block of code multiple times
# while loop is used when we don't know the number of iterations

# Syntax:
# while condition:
#     code

while True:
    print("Hello World")
    break

while 1 == 1:
    print("Hello World")
    break

while 0 > 10:
    print("Hello World")
    break
else:
    print("false")


while 0 < 10:
    userName = input("Enter your name: ")
    break
print(f"Hello {userName}")
