import Zad1.BBS as gen
from Crypto.Cipher import AES
import Zad1.StandardTests as tests
import Zad1.StreamCipher as stCi
import Zad2.BlockCipher as bc
import Zad3.RSA as RSA
from Zad3.RSA import RSA, decryptMessage
from colorama import Fore, init, AnsiToWin32
import os
import sys
import time
import random
from Crypto.Random import get_random_bytes

#strToSave=""
#for x in range(0,50000):
#    strToSave+=chr(random.randint(33,126))

#f = open("50k","w")
#f.write(strToSave)
#f.close()

#strToSave=""
#for x in range(0,150000):
#    strToSave+=chr(random.randint(33,126))

#f = open("150k","w")
#f.write(strToSave)
#f.close()



#strToSave=""
#for x in range(0,25000000):
#    strToSave+=chr(random.randint(33,126))

#f = open("25kk.txt","w")
#f.write(strToSave)
#f.close()

#strToSave=""
#for x in range(0,1000000):
#    strToSave+=chr(random.randint(33,126))

#f = open("50kk.txt","r")
#text = f.read()
#f.close()
#print("Długość ciągu - "+str(len(text)))
#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_ECB)
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )
#decrypted = cipher.decrypt(encrypted)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla ECB " + str(time_elapsed) + " sekund")
      

#tempIV = []
#for x in range(0,16):
#    tempIV.append(random.randint(0,255))
#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CBC, bytes(tempIV))
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CBC, bytes(tempIV))
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()

#time_elapsed = end_time - start_time
#print("Czas dla CBC " + str(time_elapsed) + " sekund")

#tempIV = []
#for x in range(0,16):
#    tempIV.append(random.randint(0,255))
#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CFB, bytes(tempIV))
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CFB, bytes(tempIV))
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()

#time_elapsed = end_time - start_time
#print("Czas dla CFB " + str(time_elapsed) + " sekund")

#tempIV = []
#for x in range(0,16):
#    tempIV.append(random.randint(0,255))
#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_OFB, bytes(tempIV))
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_OFB, bytes(tempIV))
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla OFB " + str(time_elapsed) + " sekund")

#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CTR)
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CTR, nonce=cipher.nonce)
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla CTR " + str(time_elapsed) + " sekund")

#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CCM)
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_CCM,nonce = cipher.nonce)
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla CCM " + str(time_elapsed) + " sekund")


#header = b"header"
#cipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_EAX)
#cipher.update(header)
#start_time = time.time()
#encrypted = cipher.encrypt(str.encode(bc.pad(text)) )

#decipher = AES.new(b'xyzW3abdefsykl12', AES.MODE_EAX,nonce = cipher.nonce)
#decipher.update(header)
#decrypted = decipher.decrypt(encrypted)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla EAX " + str(time_elapsed) + " sekund")

#key = get_random_bytes(16 * 2)
#nonce = get_random_bytes(16)
#header = b"header"
#cipher = AES.new(key, AES.MODE_SIV,nonce = nonce)
#cipher.update(header)
#start_time = time.time()
#encrypted, tag = cipher.encrypt_and_digest(str.encode(bc.pad(text)) )

#decipher = AES.new(key, AES.MODE_SIV,nonce = nonce)
#decipher.update(header)
#decrypted = decipher.decrypt_and_verify(encrypted, tag)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla SIV " + str(time_elapsed) + " sekund")


#key = get_random_bytes(16 * 2)
#header = b"header"
#cipher = AES.new(key, AES.MODE_OCB)
#cipher.update(header)
#start_time = time.time()
#encrypted, tag = cipher.encrypt_and_digest(str.encode(bc.pad(text)) )

#decipher = AES.new(key, AES.MODE_OCB,nonce = cipher.nonce)
#decipher.update(header)
#decrypted = decipher.decrypt_and_verify(encrypted, tag)
#end_time = time.time()
#time_elapsed = end_time - start_time
#print("Czas dla OCB " + str(time_elapsed) + " sekund")

#bbs = gen.BlumBlumShub()
#mln = bbs.bits(n=1000000)
#f = open("mlnFile.txt", "w")
#f.write(mln)
#f.close()
#print(len(mln))
#a ="Stop"

#ZAD 3

#1

#rsa = RSA(p = 1009, q =1103)

#print("Klucz publiczny - "+ str(rsa.e) + ", " + str(rsa.n))
#print("Klucz prywatny - " +str(rsa.d) + ", " + str(rsa.n))

#plainMessage ="Podstawy kryptografii - Implementacja RSA  11.2021"

#rsa.encryptMessage(plainMessage,rsa.e,rsa.n)

#print("Wiadomość zaszyfrowana")
#rsa.printEncryptedMessage()


#print("Wiadomość odszyfrowana")

#print("Poniżej odszyfrowana")
#decryptMessage(rsa.c,rsa.d,rsa.n)
#print(plainMessage)
#print("Powyżej wiadomość jawna, przed szyfrowaniem")

#END 1

#2

zad2Text = "Dwadziescia znakow!!"

rsaA = RSA(p = 1009, q =1103)
rsaB = RSA(p = 1093, q =1229) # druga para

print("Para kluczy A:")
print("Klucz publiczny - "+ str(rsaA.e) + ", " + str(rsaA.n))
print("Klucz prywatny  - " +str(rsaA.d) + ", " + str(rsaA.n))
print()

print("Para kluczy B")
print("Klucz publiczny - "+ str(rsaB.e) + ", " + str(rsaB.n))
print("Klucz prywatny  - " +str(rsaB.d) + ", " + str(rsaB.n))
print()

print("Szyfrowanie kluczem A")
rsaA.encryptMessage(zad2Text,rsaA.d,rsaA.n)
print("Wiadomość zaszyfrowana:")
rsaA.printEncryptedMessage()
print("Wiadomość odszyfrowana")
decryptMessage(rsaA.c,rsaA.e,rsaA.n)
print(zad2Text + "  -- wiadomość przed szyfrowaniem")
print()

print("Szyfrowanie kluczem B")
rsaB.encryptMessage(zad2Text,rsaB.d,rsaB.n)
print("Wiadomość zaszyfrowana:")
rsaB.printEncryptedMessage()
print("Wiadomość odszyfrowana")
decryptMessage(rsaB.c,rsaB.e,rsaB.n)
print(zad2Text + "  -- wiadomość przed szyfrowaniem")
print()



#END 2

#END ZAD 3
           
#ZAD2                                                               
#message = "lubu dubu, lubu dubu, niech zyje nam prezes naszego klubu! Niech zyje nam! To spiewalem ja - Jarzabek."


#print("Wiadomość do szyfrowania:")
#print(message)
#print()

#print("Usunąć cały blok")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#blockA.cipherArray.remove(blockA.cipherArray[1])
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#blockB.cipherArray.remove(blockB.cipherArray[1])

#blockB.cbcDecrypt()
#print()


#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#blockC.cipherArray.remove(blockC.cipherArray[1])

#blockC.cfbDecrypt()
#print()







#print("Wiadomość do szyfrowania:")
#print(message)
#print()

#print("Powielić wybrany blok")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#blockA.cipherArray.insert(2,blockA.cipherArray[1])
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#blockB.cipherArray.insert(2,blockB.cipherArray[1])

#blockB.cbcDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#blockC.cipherArray.insert(2,blockC.cipherArray[1])

#blockC.cfbDecrypt()
#print()

#print("Wiadomość do szyfrowania:")
#print(message)
#print()





#print("Zamienić bloki miejscami ")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#temp1 = blockA.cipherArray[2]
#temp2 = blockA.cipherArray[3]
#blockA.cipherArray[2] = temp2
#blockA.cipherArray[3] = temp1
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#temp1 = blockB.cipherArray[2]
#temp2 = blockB.cipherArray[3]
#blockB.cipherArray[2] = temp2
#blockB.cipherArray[3] = temp1

#blockB.cbcDecrypt()
#print()


#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#temp1 = blockC.cipherArray[2]
#temp2 = blockC.cipherArray[3]
#blockC.cipherArray[2] = temp2
#blockC.cipherArray[3] = temp1
#blockC.cfbDecrypt()
#print()



#print("Wiadomość do szyfrowania:")
#print(message)
#print()




#print("Zmiana wartości bajtu")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#blockA.cipherArray[2][5] = blockA.cipherArray[2][5] +1
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#blockB.cipherArray[2][5] = blockA.cipherArray[2][5] +1

#blockB.cbcDecrypt()
#print()


#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#blockC.cipherArray[2][5] = blockA.cipherArray[2][5] +1

#blockC.cfbDecrypt()
#print()






#print("Wiadomość do szyfrowania:")
#print(message)
#print()

#print("Zamienić wewnątrz bloku bajty miejscami ")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#temp1 = blockA.cipherArray[2][9]
#temp2 = blockA.cipherArray[2][10]
#blockA.cipherArray[2][9] = temp2
#blockA.cipherArray[2][10] = temp1
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#temp1 = blockB.cipherArray[2][9]
#temp2 = blockB.cipherArray[2][10]
#blockB.cipherArray[2][9] = temp2
#blockB.cipherArray[2][10] = temp1

#blockB.cbcDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#temp1 = blockC.cipherArray[2][9]
#temp2 = blockC.cipherArray[2][10]
#blockC.cipherArray[2][9] = temp2
#blockC.cipherArray[2][10] = temp1
#blockC.cfbDecrypt()
#print()





#print("Wiadomość do szyfrowania:")
#print(message)
#print()

#print("Usunąć fragment bloku")
#print("Wynik szyfrowania i deszyfrowania trybem ECB:")
#blockA = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockA.ecbEncrypt()
#blockA.cipherArray[2].remove(blockA.cipherArray[2][12])
#blockA.ecbDecrypt()
#print()

#print("Wynik szyfrowania i deszyfrowania trybem CBC:")
#blockB = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockB.cbcEncrypt()
#blockB.cipherArray[2].remove(blockB.cipherArray[2][12])
#blockB.cbcDecrypt()
#print()


#print("Wynik szyfrowania i deszyfrowania trybem CFB:")
#blockC = bc.blockCipher(text =message, key = "xyzW3abdefsykl12")
#blockC.cfbEncrypt()
#blockC.cipherArray[2].remove(blockC.cipherArray[2][12])

#blockC.cfbDecrypt()
#print()

#END ZAD2


#ZAD1


#st = stCi.streamCipher(path = "someText.txt")
#print("Wiadomość jawna:")
#print(st.plainText)
#st.setSi()
#st.setCi()

#print()
#print("Szyfrogram:")
#print(st.ci)

#print()
#print("Wiadomość odszyfrowana:")
#st.decrypt()


#print()
#print("Testy szyfrogramu:")
#test = tests.StandardTests(binaryString=st.ci)

#test.oneBitTest()
#test.seriesTest()
#test.longSeriesTest()
#test.pokerTest()

###st.decrypt()
####print(len(st.mi))
####asasa = ""



#files = ["string1.txt","string2.txt","string3.txt"]

#for file in files:
#    print("Plik - "+file)
#    test = tests.StandardTests(path = file)
#    test.oneBitTest()
#    test.seriesTest()
#    test.longSeriesTest()
#    test.pokerTest()
#    print()
#    print()
    
    
    
#bbs = gen.BlumBlumShub()
#bbs2 = gen.BlumBlumShub()
#bbs3 = gen.BlumBlumShub()

#f2 = open("string1.txt","w")
#f2.write(bbs.bits(20000))
#f2.close()

#f2 = open("string2.txt","w")
#f2.write(bbs2.bits(20000))
#f2.close()

#f2 = open("string3.txt","w")
#f2.write(bbs3.bits(20000))
#f2.close()

#f = open("10mlnFile", "r")
#van = f.read()
#print(len(van))



#END ZAD1
