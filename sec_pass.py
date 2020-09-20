import numpy as np
import string
import random as random

class PasswordGen():
    def __init__(self):
        self.index = 0
        self.currentpass = str()
        self.dummychars = [',', '!', '_', '#', '$', '@', '(', ')', '[', ']',
                           '-', '.', '&', '-', '=']

    def GenerateNumbers(self):
        self.index = np.random.randint(low=0,high=9)
        self.currentpass += (str(self.index))

    def GenerateSymbols(self):
        self.index = np.random.randint(low=0, high=len(self.dummychars))
        self.currentpass += (self.dummychars[self.index])

    def GenerateLower(self):
        self.index = np.random.randint(low=0,high=25)                 #index in ascii_lower chars
        self.currentpass += string.ascii_lowercase[self.index]

    def GenerateUpper(self):
        self.index = np.random.randint(low=0, high=25)                # index in ascii_upper chars
        self.currentpass += string.ascii_uppercase[self.index]

    def ShufflePassword(self):
        aftershuf = list(self.currentpass)
        random.shuffle(aftershuf)
        self.currentpass = ''.join(aftershuf)

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

        self.ShufflePassword()

    def GetPass(self):
        return self.currentpass


x = PasswordGen()
x.CallOthers()
print(x.GetPass())
