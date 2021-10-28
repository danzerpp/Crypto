from textwrap import wrap

import Zad1.BBS as gen
def getBinaryText(self,text):
    binStr =""
    for char in text:
        binStr = binStr +  str(bin(ord(char))[2:]).zfill(7)
    return binStr

def getSi(self,length):
    bbs = gen.BlumBlumShub()
    return bbs.bits(length)

class streamCipher(object):
    """description of class"""
    def __init__(self,text = "", path =""):
        if path == "":
            self.plainText =text
        else:
            with open(path) as f:
                  self.plainText = f.read()
                  f.close()
        self.mi =  getBinaryText(self,self.plainText) # jawny binarny
        self.si = "" # bbs
        self.ci = "" # szyfrogram


    def setSi(self): #ustaw klucz - bbs
        self.si = getSi(self,len(self.mi)) 

    def setCi(self): #ustaw szyfrogram
        cryptogram =""
        for i in range(0,len(self.mi)):
            cryptogram += str(int(self.si[i]) ^ int(self.mi[i]))
        self.ci = cryptogram

    def decrypt(self):
        plainBin=""
        for i in range(0,len(self.ci)):
            plainBin += str(int(self.ci[i]) ^ int(self.si[i]))
        plainTxt = ""
        for asci in wrap(plainBin,7):
            plainTxt+= chr(int(asci,2))
        print(plainTxt)


        

