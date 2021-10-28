import Zad1.BBS as gen
import Zad1.StandardTests as tests
import Zad1.StreamCipher as stCi

st = stCi.streamCipher(path = "someText.txt")

st.setSi()
st.setCi()
st.decrypt()
print(len(st.mi))
asasa = ""
#binary = bbs.bits(1000000)
#print(binary)
test = tests.StandardTests(st.ci)

test.oneBitTest()
test.seriesTest()
test.longSeriesTest()
test.pokerTest()