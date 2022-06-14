# class
class PlayerCharacter:
    def __init__(self, name):  # constructor
        self.name = name

    def run(self):  # function
        print('run')


player01 = PlayerCharacter('Madhusha')  # create a object from the PlayerCharacter class
print(player01.name)  # call name variable
print(player01.run())  # call run class
