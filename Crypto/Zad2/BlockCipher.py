from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from termcolor import colored
from textwrap import wrap
import random

def pad(m):
    return m+chr(16-len(m)%16)*(16-len(m)%16)

def unpad(ct):
    return ct[:-ord(ct[-1])]

def prepareText(self,text):
    return str.encode(pad(text))

def xorCfb(self,firstBits,secondBits):
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
        
        self.cipherText =""
        self.IV = ""

        
        
        

    def ecbEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        self.cipherText  =cipher.encrypt(self.textToEncrypt)

        self.plainHex =""
        self.plainBin =""

        self.cipherHex =""
        self.cipherBin =""
        count =0

        for x in self.cipherText:
            self.cipherBin += str(bin(x)[2:]).zfill(8)
            self.cipherHex += str(format(x,"x").zfill(2))
        for x in self.textToEncrypt:
            self.plainBin += str(bin(x)[2:]).zfill(8)
            self.plainHex += str(format(x,"x").zfill(2))

        self.plainBin = wrap(self.plainBin,128)
        self.plainHex = wrap(self.plainHex,32)

        self.cipherBin = wrap(self.cipherBin,128)
        self.cipherHex = wrap(self.cipherHex,32)


    def ecbDecrypt(self):
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        dec_msg = decipher.decrypt(bytes(self.cipherText))
        print(unpad(dec_msg.decode()))


    def cbcEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        generateIV(self)
        blocks = wrap(self.textToEncrypt.decode(),16)
        count =0
        self.cipherArray=[]
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in blocks:
            toEncrypt = doXorOperation(self,block)
            tempIV =""
            for enc in cipher.encrypt(toEncrypt):
                self.cipherArray.append(enc)
                tempIV+= str(bin(enc)[2:]).zfill(8)
            self.currentIV = tempIV
    
    def cbcDecrypt(self):
        self.currentIV = self.IV
        decryptedArray =[]
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in list(split(self.cipherArray,int(len(self.cipherArray)/16))):
            if len(block) != 16:
                print("Błąd w cbcDecrypt")

            tempOut =""
            for enc in decipher.decrypt(bytes(block)):
                tempOut+= str(bin(enc)[2:]).zfill(8)

            for i in doXorOperation(self,"",tempOut):
                decryptedArray.append(i)

            self.currentIV =""
            for i in block:
                self.currentIV += str(bin(i)[2:]).zfill(8)

        print(unpad(bytes(decryptedArray).decode()))

        #dec_msg = decipher.decrypt(bytes(self.cipherText))
        #print(unpad(dec_msg.decode()))

    def cfbEncrypt(self):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        generateIV(self)

        self.cipherArray=[]
        blocks = wrap(self.textToEncrypt.decode(),16)
        
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        
        for block in blocks:
            cipherBits =""
            plainBits =""

            for i in cipher.encrypt(bytes(self.currentCfbIV)):
                cipherBits+= str(bin(i)[2:]).zfill(8)

            for i in str.encode(block):
                plainBits+= str(bin(i)[2:]).zfill(8)

            outBits= xorCfb(self,plainBits,cipherBits)
            self.currentCfbIV =[]
            for x in wrap(outBits,8):
                self.cipherArray.append(int(x,2))
                self.currentCfbIV.append(int(x,2))
        abc = "Stoop"

    def cfbDecrypt(self):
        self.currentCfbIV = self.cfbIV
        
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        decryptedArray =[]
        for block in list(split(self.cipherArray,int(len(self.cipherArray)/16))):
            cipherBits =""
            blockBits=""

            for i in cipher.encrypt(bytes(self.currentCfbIV)):
                cipherBits+= str(bin(i)[2:]).zfill(8)

            for i in block:
                blockBits+= str(bin(i)[2:]).zfill(8)
            outBits= xorCfb(self,blockBits,cipherBits)
            
            for x in wrap(outBits,8):
                decryptedArray.append(int(x,2))
            self.currentCfbIV = block
        print(unpad(bytes(decryptedArray).decode()))







                
            



        
        



        