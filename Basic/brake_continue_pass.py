# brake,continue,pass

# brake: break the loop
# continue: skip the current iteration
# pass: do nothing

for i in range(10):
    if i == 3:
        print("i == 3, break")
        break
    print(i)

for i in range(10):
    if i == 3:
        print("i == 3, continue")
        continue
    print(i)

for i in range(10):
    if i == 3:
        print("i == 3, pass")
        pass
