import random
from math import gcd as bltin_gcd
from textwrap import wrap

def decryptMessage(message,d,n):
        mD = []
        for cs in message:
            val = cs ** d % n
            values = wrap(str(val),3)
            for value in values:
                val = int(value)
                if val >=300:
                    val = val -300
                mD.append(val)
                print(chr(val),end="")
        print()

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def isCoprime(a, b):
    return bltin_gcd(a, b) == 1

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

class RSA(object):
    def __init__(self,p=1009  ,q=1381 , e =0, d =0):
        self.p = p
        self.q = q
        self.c =[]

        self.n = self.p * self.q

        self.phi_n = (self.p-1) * (self.q-1)

        if e ==0:
            temp_e = random.randint(3,self.phi_n-1)
            while not isPrime(temp_e) and not isCoprime(temp_e,self.phi_n):
                  temp_e = random.randint(3,self.phi_n-1)
            self.e = temp_e
        else:
            self.e = e
        if d ==0:
            temp_d = 3
            while (self.e* temp_d) % self.phi_n !=1 and temp_d < self.phi_n:
                  temp_d = temp_d +1
            if temp_d>=self.phi_n:
                print("Błędne dane")
            self.d = temp_d
        else:
            self.d = d

        
    def encryptMessage(self,message,e,n):
        naturalMess = ""
        for byte in str.encode(message):
            i = int(byte)
            if i<100:
                i = i+300
            naturalMess += str(i)
        toEncrypt = wrap(naturalMess,6)
        
        self.c =[]
        for m in toEncrypt:
            self.c.append(int(m)**e % n)

    def printEncryptedMessage(self):
        toPrint =""
        for x in self.c:
            toPrint+= str(x) +" "
        print(toPrint)
       
    
