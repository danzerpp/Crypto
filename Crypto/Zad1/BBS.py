import random
from math import gcd as bltin_gcd


def isCoprime(a, b):
    return bltin_gcd(a, b) == 1
 
 
def makeModulus(p,q):
    if p ==0 or q ==0:
        return 100343 * 104659
    return p*q
    
 
def getBit(n):
    return 
 
def setNewSeed(self):
    newSeed = random.randint(2, self.modulus - 1)
    while not isCoprime(newSeed, self.modulus) :
        newSeed = random.randint(2, self.modulus - 1)
    return newSeed

class BlumBlumShub(object):
    def __init__(self, a=None, p = 0, q = 0):
        self.modulus = makeModulus(p,q)
        self.state = a if a is not None else setNewSeed(self)
        self.state = (self.state**2) % self.modulus

    def a(self, a):
        self.state = a
 
    def bitstream(self):
        while True:
            yield self.state % 2
            self.state = pow(self.state, 2, self.modulus)
 
    def bits(self, n=20):
        outputBits = ''
        for bit in self.bitstream():
            outputBits += str(bit)
            if len(outputBits) == n:
                break
 
        return outputBits