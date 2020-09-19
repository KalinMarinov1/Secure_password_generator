import numpy as np
import string

class PasswordGen():
    def __init__(self):
        self.currentpass = str()
        self.dummychars = [',', '!', '_', '#', '$', '@', '(', ')', '[', ']',
                           '-', '.', '&', '-', '=']

    def GenerateNumbers(self):
        raw_x = np.random.randint(low=0,high=9)
        self.currentpass.__add__(str(raw_x))

    def GenerateSymbols(self):
        index = np.random.randint(low=0, high=len(self.dummychars))
        self.currentpass.__add__( self.dummychars[index])

    def GenerateLower(self):
        self.currentpass.__add__(np.random.choice(string.ascii_lowercase))

    def GenerateUpper(self):
        self.currentpass.__add__(np.random.choice(string.ascii_uppercase))

    def CallOthers(self):
        raw_x = input("How many chars of each ? :")
        x = int(raw_x)
        if x < 2 or x > 10:
            x = 5
        while x > 0:
            self.GenerateNumbers()
            self.GenerateSymbols()
            self.GenerateLower()
            self.GenerateUpper()
            x -= 1

x = PasswordGen()
x.CallOthers()