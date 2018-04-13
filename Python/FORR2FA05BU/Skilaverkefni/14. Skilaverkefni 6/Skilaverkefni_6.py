import random

class Hermenn:
    def __init__(self,lif, afl, vopn):
        self.vopn = vopn
        self.lif = lif
        self.afl = afl
    def generator_A(self):
        herdeild_A = []
        for tel in range(5):
            self.lif = random.randint(1,5)
            self.afl = random.randint(1,5)
            self.vopn = random.randint(1,3)#Sverð = 1, Spjót = 2, Exi = 3
            h1 = Hermenn(self.lif, self.afl, self.vopn)
            herdeild_A.append(h1)
        print(herdeild_A)

h1 = Hermenn(0, 0, 0)
h1.generator_A()