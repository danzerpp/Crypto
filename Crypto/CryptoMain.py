import Zad1.BBS as gen
import Zad1.StandardTests as tests
import Zad1.StreamCipher as stCi
import Zad2.BlockCipher as bc
import Zad3.RSA as RSA
from Zad3.RSA import RSA, decryptMessage
from colorama import Fore, init, AnsiToWin32
import os
import sys



#bbs = gen.BlumBlumShub()
#mln = bbs.bits(n=1000000)
#f = open("mlnFile.txt", "w")
#f.write(mln)
#f.close()
#print(len(mln))
#a ="Stop"

#ZAD 3

#1

#plainMessage ="Podstawy kryptografii - Implementacja RSA  11.2021"
#rsa = RSA()
#rsa.encryptMessage(plainMessage,rsa.e,rsa.n)
##rsa.printEncryptedMessage()
#decryptMessage(rsa.c,rsa.d,rsa.n)

#END 1

#2

#zad2Text = "Dwadziescia znakow!!"

#rsa = RSA() #pierwsza para
#rsaSecond = RSA() # druga para

#rsa.encryptMessage(zad2Text,rsa.d,rsa.n)
#rsa.printEncryptedMessage()
#decryptMessage(rsa.c,rsa.e,rsa.n)

#rsaSecond.encryptMessage(zad2Text,rsaSecond.d,rsaSecond.n)
#rsaSecond.printEncryptedMessage()
#decryptMessage(rsaSecond.c,rsaSecond.e,rsaSecond.n)


#END 2

#END ZAD 3

#ZAD2

blockA = bc.blockCipher(text ="A00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000Z", key = "xyzW3abdefsykl12")
blockA.ecbEncrypt()
blockA.cipherArray[2].remove(blockA.cipherArray[0][0])
blockA.ecbDecrypt()

blockB = bc.blockCipher(text ="A00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000Z", key = "xyzW3abdefsykl12")
blockB.cbcEncrypt()
blockB.cipherArray[2].remove(blockC.cipherArray[2][15])
blockB.cbcDecrypt()

blockC = bc.blockCipher(text ="A00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000ZA00000000000000Z", key = "xyzW3abdefsykl12")
blockC.cfbEncrypt()
blockC.cipherArray[2].remove(blockC.cipherArray[2][15])
blockC.cfbDecrypt()
#END ZAD2


#ZAD1
##st = stCi.streamCipher(path = "someText.txt")
##st.setSi()
##st.setCi()
##print(st.ci)

##test = tests.StandardTests(binaryString=st.ci)

##test.oneBitTest()
##test.seriesTest()
##test.longSeriesTest()
##test.pokerTest()
##st.decrypt()
###print(len(st.mi))
###asasa = ""
#bbs = gen.BlumBlumShub()

#f = open("10mlnFile", "r")
#van = f.read()
#print(len(van))

#f2 = open("10mlnFile.txt","w")
#f2.write()
#f.close()
##print(binary)

#END ZAD1
