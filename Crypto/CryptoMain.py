import Zad1.BBS as gen
import Zad1.StandardTests as tests
import Zad1.StreamCipher as stCi
import Zad2.BlockCipher as bc
import colorama
from colorama import Fore, init, AnsiToWin32
import os
import sys

#my_str_as_bytes = str.encode(my_str)
#my_decoded_str = my_str_as_bytes.decode()
blockA = bc.blockCipher(text ="Jestem nioma!@#$%", key = "xyzW3abdefsykl12")
blockA.ecbEncrypt()
blockA.ecbDecrypt()

blockB = bc.blockCipher(text ="Jestem nioma!@#$%", key = "xyzW3abdefsykl12")
blockB.cbcEncrypt()
blockB.cbcDecrypt()

blockC = bc.blockCipher(text ="Jestem nioma!@#$%", key = "xyzW3abdefsykl12")
blockC.cfbEncrypt()
blockC.cfbDecrypt()
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