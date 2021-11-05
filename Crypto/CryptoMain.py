import Zad1.BBS as gen
import Zad1.StandardTests as tests
import Zad1.StreamCipher as stCi
import Zad2.BlockCipher as bc
import Zad3.RSA as RSA
from Zad3.RSA import RSA, decryptMessage
from colorama import Fore, init, AnsiToWin32
import os
import sys

#ZAD 3

#1

#plainMessage ="Podstawy kryptografii - Implementacja RSA  11.2021"
#rsa = RSA()
#rsa.encryptMessage(plainMessage,rsa.e,rsa.n)
##rsa.printEncryptedMessage()
#rsa.decryptMessage(rsa.c,rsa.d,rsa.n)

#END 1

#2

zad2Text = "Dwadziescia znakow!!"

rsa = RSA() #pierwsza para
rsaSecond = RSA() # druga para

rsa.encryptMessage(zad2Text,rsa.d,rsa.n)
decryptMessage(rsa.c,rsa.e,rsa.n)

rsaSecond.encryptMessage(zad2Text,rsaSecond.d,rsaSecond.n)
decryptMessage(rsaSecond.c,rsaSecond.e,rsaSecond.n)


#END 2

#END ZAD 3

#ZAD2

#blockA = bc.blockCipher(text ="asdghe3#$%aasd6rgdFWW$#$yerye6434^#$#4teqRhjSRTnfzetye6s4z5t", key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#blockA.cipherArray[0].remove(blockA.cipherArray[0][0])
#blockA.ecbDecrypt()

#print(bytes(0).decode())
#blockB = bc.blockCipher(text ="Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%", key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#blockB.cipherArray[3].remove(blockB.cipherArray[3][4])
#blockB.cbcDecrypt()

#blockC = bc.blockCipher(text ="A00000000000000ZA00000000000000ZA00000000000000ZA00000000000000Z", key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#blockC.cipherArray[2].remove(blockC.cipherArray[2][15])
#blockC.cfbDecrypt()

#END ZAD2


#ZAD1
#st = stCi.streamCipher(path = "someText.txt")

#st.setSi()
#st.setCi()
#st.decrypt()
#print(len(st.mi))
#asasa = ""
##binary = bbs.bits(1000000)
##print(binary)
#test = tests.StandardTests(st.ci)

#test.oneBitTest()
#test.seriesTest()
#test.longSeriesTest()
#test.pokerTest()
#END ZAD1
