from textwrap import wrap

import Zad1.BBS as gen
def getBinaryText(self,text):
    binStr =""
    for char in text:
        binStr = binStr +  str(bin(ord(char))[2:]).zfill(7) #przerabianie string na binary string
    return binStr

def getSi(self,length):
    bbs = gen.BlumBlumShub()
    return bbs.bits(length)

class streamCipher(object):
    """description of class"""
    def __init__(self,text = "", path =""): # szyfrator strumieniowy przyjumje gotowy tekst lub ścieżkę do pliku
        if path == "":
            self.plainText =text
        else:
            with open(path) as f:
                  self.plainText = f.read()
                  f.close()
        self.mi =  getBinaryText(self,self.plainText) # jawny binarny # tekst zostaje przetworzony na ciąg bitów - każdy znak 7 bitów
        self.si = "" # bbs
        self.ci = "" # szyfrogram


    def setSi(self): #ustaw klucz - bbs
        self.si = getSi(self,len(self.mi))  # pobieramy długość ciągu bitów tekstu i generatorem BBS tworzymy ciąg bitów o tej samej długości
                                                                                                                                      
    def setCi(self): #ustaw szyfrogram
        cryptogram =""
        for i in range(0,len(self.mi)): # dla każdego bita w wiadomości jawnej wykonujemy operację XOR z bitem o tym samym indeksie z klucza
            cryptogram += str(int(self.si[i]) ^ int(self.mi[i]))
        self.ci = cryptogram # zapisujemy szyfrogram

    def decrypt(self):
        plainBin=""
        for i in range(0,len(self.ci)): #deszyfrowanie polega operacji XOR wykonywanej na szyfrogamie(ci) i kluczu (si)
            plainBin += str(int(self.ci[i]) ^ int(self.si[i]))
        plainTxt = ""
        for asci in wrap(plainBin,7):
            plainTxt+= chr(int(asci,2))
        print(plainTxt)
        return plainTxt # zwróć text jawny


        

