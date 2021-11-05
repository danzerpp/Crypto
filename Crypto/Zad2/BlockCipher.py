from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from termcolor import colored
from textwrap import wrap
import random
from math import ceil
def pad(m):
    return m+chr(16-len(m)%16)*(16-len(m)%16)

def unpad(ct):
    return ct[:-ord(ct[-1])]

def getBits(bytes):
    outPut =""
    for b in bytes:
        outPut+= str(bin(b)[2:]).zfill(8)
    return outPut

def getBytes(bits):
    blocks = wrap(bits,8)
    bytes = []
    for block in blocks:
        bytes.append(int(block,2))
    return bytes

def prepareText(self,text):
    paddedText = pad(text)
    return str.encode(paddedText)

def xorOperation(self,firstBits,secondBits):
    outPutBits = ""
    for i in range(0,len(firstBits)):
        outPutBits += str(int(firstBits[i]) ^ int(secondBits[i]))
    return outPutBits

def doXorOperation(self,input,inputBin=""):
    if inputBin =="":
        for i in str.encode(input):
            inputBin += str(bin(i)[2:]).zfill(8)
    
        
    if len(inputBin) != len(self.currentIV):
        print("Błąd w funkcji doXorOperation")
        return

    outPutBits = ""
    for i in range(0,len(inputBin)):
        outPutBits += str(int(inputBin[i]) ^ int(self.currentIV[i]))

    bitsWrap = wrap(outPutBits,8)
    outPutBytes =[]
    for bits in bitsWrap:
        outPutBytes.append(int(bits,2))
    return bytes(outPutBytes)


def generateIV(self):
    tempIV = []
    for x in range(0,16):
        tempIV.append(random.randint(0,255))
    self.cfbIV =[]
    self.currentCfbIV=[]
    self.IV = ""
    self.currentIV = ""
    for i in tempIV:
        self.cfbIV.append(i)
        self.currentCfbIV.append(i)
        self.IV += str(bin(i)[2:]).zfill(8)
        self.currentIV += str(bin(i)[2:]).zfill(8)

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))



class blockCipher(object):
    def __init__(self,text="", key = ""):
        self.cipherKey = b'xyzW3abdefsykl12'
        if key != "":
             tempKey = str.encode(key)
             if len(tempKey) != 16:
                 print("Klucz nie składa się z 16 bajtów !! Użyto domyślnego")
             else:
                 self.cipherKey = tempKey
        if len(text) ==0:
            print("Nie podano wiadomości do szyfrowania!!")
        else :
            self.textToEncrypt = prepareText(self,text)

        self.complement =self.textToEncrypt[len(self.textToEncrypt)-1]
        
        self.cipherText =""
        self.IV = ""

        
    def getPlainBits(self):
        for i in self.textToEncrypt:
            print(str(bin(i )[2:]).zfill(8) +" ",end="")  
        print()

    def getPlainHEX(self):
        for i in self.textToEncrypt:
            print(str(hex(i )).lstrip("0x").zfill(2) +" ",end="")  
        print()

    def ecbEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)

        self.cipherArray =[]
        byteBlocks = list(split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16)))
        for block in byteBlocks:
            tempArray=[]
            for i in cipher.encrypt(block):
                tempArray.append(i)
            self.cipherArray.append(tempArray)

    def ecbDecrypt(self):
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        decryptedArray=[]
        for block in  self.cipherArray:
            diffrence = 16 - len(block) 
            while len(block)!= 16:
                block.append(diffrence)
            for i in decipher.decrypt(bytes(block)):
                decryptedArray.append(i)
        string =""
        for x in decryptedArray:
            string += chr(x)
        print(unpad(string))


    def cbcEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        generateIV(self)
        
        byteBlocks = list(split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16)))
        
        count =0
        self.cipherArray=[]
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
       
        for byteBlock in byteBlocks:
            toEncrypt = xorOperation(self,getBits(byteBlock),self.currentIV)
            tempIV =""
            tempArray=[]
            for enc in cipher.encrypt(bytes(getBytes(toEncrypt))):
                tempArray.append(enc)
                tempIV+=  str(bin(enc)[2:]).zfill(8)
            self.cipherArray.append(tempArray)
            self.currentIV = tempIV
    
    def cbcDecrypt(self):
        self.currentIV = self.IV
        decryptedArray =[]
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)

        for block in self.cipherArray:
            diffrence = 16 - len(block) 
            while len(block)!= 16:
                block.append(diffrence)
            tempOut =""
            for enc in decipher.decrypt(bytes(block)):
                tempOut+= str(bin(enc)[2:]).zfill(8)

            for i in getBytes(xorOperation(self,tempOut,self.currentIV)):
                decryptedArray.append(i)

            self.currentIV =""
            for i in block:
                self.currentIV += str(bin(i)[2:]).zfill(8)
        string =""
        for x in decryptedArray:
            string += chr(x)
        print(unpad(string))

    def cfbEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        generateIV(self)

        self.cipherArray=[]
        a = len(self.textToEncrypt)
        blocks = wrap(self.textToEncrypt.decode(),16)
        
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        
        for block in blocks:
            cipherBits =""
            plainBits =""

            for i in cipher.encrypt(bytes(self.currentCfbIV)):
                cipherBits+= str(bin(i)[2:]).zfill(8)

            for i in str.encode(block):
                plainBits+= str(bin(i)[2:]).zfill(8)

            outBits= xorOperation(self,plainBits,cipherBits)
            self.currentCfbIV =[]
            tempArray =[]
            for x in wrap(outBits,8):
                tempArray.append(int(x,2))
                self.currentCfbIV.append(int(x,2))
            self.cipherArray.append(tempArray)

    def cfbDecrypt(self):
        self.currentCfbIV = self.cfbIV
        
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        decryptedArray =[]
     
        for block in self.cipherArray:
            diffrence = 16 - len(block) 
            while len(block)!= 16:
                block.append(diffrence)
            cipherBits =""
            blockBits=""

            for i in cipher.encrypt(bytes(self.currentCfbIV)):
                cipherBits+= str(bin(i)[2:]).zfill(8)

            for i in block:
                blockBits+= str(bin(i)[2:]).zfill(8)
            outBits= xorOperation(self,blockBits,cipherBits)
            
            for x in wrap(outBits,8):
                decryptedArray.append(int(x,2))
            self.currentCfbIV = block
        string =""
        for x in decryptedArray:
            string += chr(x)
        print(unpad(string))







                
            



        
        



        