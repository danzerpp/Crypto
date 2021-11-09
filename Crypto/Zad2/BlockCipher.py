from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from termcolor import colored
from textwrap import wrap
import random
from math import ceil


def pad(m): # dopełnienie tekstu do 128 bitowych bloków
    return m+chr(16-len(m)%16)*(16-len(m)%16)

def unpad(ct): # powrót do wiadomości pierwotnej
    return ct[:-ord(ct[-1])]

def prepareText(self,text):
    paddedText = pad(text)
    return str.encode(paddedText) # zwrócenie tekstu w blokach 16 bajtowych

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


def generateIV(self): # generowanie bloku o długości 16 z losowymi bajtami
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
        self.cipherKey = b'xyzW3abdefsykl12' # przypisanie klucza domyślnego
        if key != "":                        # jeżeli użytkownik żadnego nie podał
             tempKey = str.encode(key)
             if len(tempKey) != 16:
                 print("Klucz nie składa się z 16 bajtów !! Użyto domyślnego")
             else:
                 self.cipherKey = tempKey
        if len(text) ==0:
            print("Nie podano wiadomości do szyfrowania!!")
        else :
            self.textToEncrypt = prepareText(self,text) # przygotowanie tekstu do szyfrowania - dopełnienie i zmiana na bajty
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

    def ecbEncrypt(self):   # szyfrowanie ECB
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)

        self.cipherArray =[]
        a= len(self.textToEncrypt)
        byteBlocks = list(split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16))) # dzielę wszystkie bajty na bloki o długości 16
        for block in byteBlocks:
            tempArray=[]
            for i in cipher.encrypt(block): #każdy blok szyfruje gotową biblioteką dla ECB
                tempArray.append(i)
            self.cipherArray.append(tempArray) # tworzę szyfrogram - lista podlist o długości bloku

    def ecbDecrypt(self):     #deszfrowanie ECB   
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        decryptedArray=[]
        for block in  self.cipherArray: # dla każdego bloku wykonuje deszyfrowanie
            diffrence = 16 - len(block) 
            while len(block)!= 16:
                block.append(diffrence)
            for i in decipher.decrypt(bytes(block)):
                decryptedArray.append(i) # zapisuje bajty po deszyfrowaniu
        string =""
        for x in decryptedArray: # ponownie generuje tekst jawny z bajtów
            string += chr(x)
        if len(unpad(string)) < 16:
            print(string)
        else:
            print(unpad(string)) # zwracam oryginalny tekst


    def cbcEncrypt(self, IV =""):
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        if IV =="" or len(IV) != 128: # blok 128 bitów
            generateIV(self)
        else:
            self.currentIV = IV # losowe generowanie IV
        byteBlocks = list(split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16))) # jak w ECB dzielę na podlisty(bloki)
        
        count =0
        self.cipherArray=[]
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
       
        for byteBlock in byteBlocks:
            toEncrypt = xorOperation(self,getBits(byteBlock),self.currentIV) # wykonuję operację XOR na bloku waidomiści jawnej i IV
            tempIV =""
            tempArray=[]
            for enc in cipher.encrypt(bytes(getBytes(toEncrypt))): # szyfruje blok za pomocą gotowej implementacji ECB
                tempArray.append(enc)
                tempIV+=  str(bin(enc)[2:]).zfill(8) # tworzę zaszyfrowany blok i generuje bity, które będą użyte do następnej operacji XOR z blokiem tesktu
            self.cipherArray.append(tempArray)
            self.currentIV = tempIV
    
    def cbcDecrypt(self):
        self.currentIV = self.IV
        decryptedArray =[]
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)

        for block in self.cipherArray: # dla bloków 16 bajtowych z szyfrogramu
            diffrence = 16 - len(block)  # jeżeli blok jest za mały, dokonuję dopełnienia
            while len(block)!= 16:
                block.append(diffrence)
            tempOut =""
            for enc in decipher.decrypt(bytes(block)): # deszyfruje blok szyfrogramu
                tempOut+= str(bin(enc)[2:]).zfill(8)

            for i in getBytes(xorOperation(self,tempOut,self.currentIV)): # wykonuję operację XOR z wygenerowanym IV
                decryptedArray.append(i)

            self.currentIV =""
            for i in block:
                self.currentIV += str(bin(i)[2:]).zfill(8) # w kolejnej operacji do funkcji XOR wykorzystuje się poprzedni blok szyfrogramu
        string =""
        for x in decryptedArray: # przywracam oryginalny tekst
            string += chr(x)
        if len(unpad(string)) < 16:
            print(string)
        else:
            print(unpad(string))

    def cfbEncrypt(self,IV =""): # szyfrownaie CFB
        if len(self.textToEncrypt) ==0:
            return "Nie podano wiadomości do szyfrowania!"
        if IV =="" or len(IV) != 16: # blok 16 bajtów
            generateIV(self)
        else:
            self.currentIV = IV # losowe generowanie IV

        self.cipherArray=[]
        a = len(self.textToEncrypt)
        bytesBlocks = list(split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16))) # dzielimy na bloki 16 bajtowe
        aa = len(self.textToEncrypt)
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        
        for block in bytesBlocks:
            cipherBits =""
            plainBits =""

            for i in cipher.encrypt(bytes(self.currentCfbIV)): # szyfrujemy IV trybem ECB
                cipherBits+= str(bin(i)[2:]).zfill(8) # tworzymy z wyniku ciąg bitów

            for i in block: # blok bajtowy przetwarzamy na ciąg binarny
                plainBits+= str(bin(i)[2:]).zfill(8)

            outBits= xorOperation(self,plainBits,cipherBits) # operacja XOR na ciągach binarnych
            self.currentCfbIV =[]
            tempArray =[]
            for x in wrap(outBits,8):
                tempArray.append(int(x,2))
                self.currentCfbIV.append(int(x,2)) # wynik operacji xor będzie szyfrowany w kolejnym bloku
            self.cipherArray.append(tempArray) # dodanie bloku zaszyfrowanego do szyfrogramu

    def cfbDecrypt(self): # deszyfrowanie CFB
        self.currentCfbIV = self.cfbIV
        
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        decryptedArray =[]
     
        for block in self.cipherArray: # dla zaszyfrowanych bloków 16 bajtowych
            diffrence = 16 - len(block) 
            while len(block)!= 16: # dopełneinie, gdy mniejszy od 16 bajtów
                block.append(diffrence)
            cipherBits =""
            blockBits=""

            for i in cipher.encrypt(bytes(self.currentCfbIV)): # szyfrujemy IV korzystając z ECB
                cipherBits+= str(bin(i)[2:]).zfill(8)

            for i in block: # zamieniamy blok na ciąg bitów
                blockBits+= str(bin(i)[2:]).zfill(8)
            outBits= xorOperation(self,blockBits,cipherBits) # wykonujemy operację XOR
            
            for x in wrap(outBits,8):
                decryptedArray.append(int(x,2))
            self.currentCfbIV = block # w kolejnym bloku szyfrowany jest blok poprzednika(czyli aktualny w tej iteracji)
        string =""
        for x in decryptedArray: # przywracamy oryginalny tekst
            string += chr(x)
        if len(unpad(string)) < 16:
            print(string)
        else:
            print(unpad(string))







                
            



        
        



        