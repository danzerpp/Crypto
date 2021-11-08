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
    newSeed = random.randint(2, self.modulus - 1)     #Generujemy losową wartość w przedziale do liczby Bluma -1
    while not isCoprime(newSeed, self.modulus) :      #sprawdzamy czy NWD seed'a i liczby bluma jest równy 1
        newSeed = random.randint(2, self.modulus - 1) # losujemy tak długo, aż warunki będą spełnione
    return newSeed

class BlumBlumShub(object):
    def __init__(self, a=None, p = 0, q = 0):  # p i q podaje użytkownik, gdy nie poda to p = 100343 q = 104659
        self.modulus = makeModulus(p,q)  # obliczamy liczbę Bluma
        self.state = a if a is not None else setNewSeed(self) # jeżeli użytkwnik nie podał, generujemy losowy
        self.state = (self.state**2) % self.modulus #obliczamy x0

    def a(self, a):
        self.state = a
 
    def bitstream(self):
        while True:
            yield self.state % 2  # interesuje nas najmłodszy bit - modulo 2 zwróci nam jego wartość
            self.state = pow(self.state, 2, self.modulus) # podnosimy poprzedniego x do kwadratu i robimy modulo
                                                          # z liczbą bluma     
    def bits(self, n=20): # funkcja zwraca nam ciąg binarny o długości n
        outputBits = ''
        for bit in self.bitstream():
            outputBits += str(bit)
            if len(outputBits) == n: 
                break
 
        return outputBits # zwracamy wygenerowany ciąg o długości n