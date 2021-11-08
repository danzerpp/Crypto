from textwrap import wrap

def checkCount(self,count,bin): # sprawdamy długość serii i do którego bitu ją przypisać
        if count == 1:
            if bin == '1':
                self.series1_1 = self.series1_1+1
            else:
                self.series1_0 = self.series1_0+1
        elif count ==2:
            if bin == '1':
                self.series2_1 = self.series2_1+1
            else:
                self.series2_0 = self.series2_0+1
        elif count ==3:
            if bin == '1':
                self.series3_1 = self.series3_1+1
            else:
                self.series3_0 = self.series3_0+1
        elif count ==4:
            if bin == '1':
                self.series4_1 = self.series4_1+1
            else:
                self.series4_0 = self.series4_0+1
        elif count ==5:
            if bin == '1':
                self.series5_1 = self.series5_1+1
            else:
                self.series5_0 = self.series5_0+1
        else:
            if bin == '1':
                self.series6_1 = self.series6_1+1
            else:
                self.series6_0 = self.series6_0+1
            if self.maxCount< count : # w tym momencie zapisujemy najdłuższą serię - długość serii
                self.maxCount = count

class StandardTests(object):

    def __init__(self, binaryString="", path = ""): # klasa przyjmuje od użytkownika ciąg bitów
                                                    # lub ściężkę do pliku
        if path != "":                              # gdy ciąg jest za długi pobiera pierwsze 20000 bitów
            with open(path) as f:
                  self.binStr = f.read()
                  f.close()
        else:
            self.binStr = binaryString
        if len(self.binStr) < 20000:
            print("Długość ciągu jest za krótka")
        if len(self.binStr) >20000:
            print("Długość ciągu jest za duża - pobrano początkowe 20000 znaków")
            self.binStr = self.binStr[0:20000]


        self.series1_0 =0
        self.series2_0 =0
        self.series3_0 =0
        self.series4_0 =0
        self.series5_0 =0
        self.series6_0 =0
        self.series1_1 =0
        self.series2_1 =0
        self.series3_1 =0
        self.series4_1 =0
        self.series5_1 =0
        self.series6_1 =0
        self.maxCount =0
        
    def oneBitTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        oneCount = 0
        for bin in self.binStr: ## sumujemy wszystkie jedynki
            if bin == '1':
                oneCount = oneCount + 1

        print("Test pojedynczego bitu:")  
        print("-----")
        if oneCount > 9725 and oneCount < 10275: ## sprawdzamy czy wynik jest wprzedziale i wyświetlamy wynik
            print ("Ilość jedynek = "+ str(oneCount)+ "\n\nPomyślny: TAK")
        else:
            print ("Ilość jedynek = "+ str(oneCount)+ "\n\nPomyślny: NIE")
        print("-----")
        print("")





    def seriesTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        lastValue = ''
        count = 0
        
        for bin in self.binStr: ## iterujemy po ciągu bitów
                if lastValue == '':
                    lastValue = bin
                    count =1
                    continue

                if bin == lastValue: # jeżeli aktualny bit jest równy poprzedniemu, zwiększamy długość serii o 1
                    count = count+1
                else:                #w przeciwnym przypadku w funkcji checkCount przypisujemy bit i jego serie do odpowiedniej grupy
                    checkCount(self,count,bin)
                    count = 1
                    lastValue = bin

        checkCount(self,count,lastValue)

        print("Test serii")
        print("-----")

        passed = True
        if (2315 <= self.series1_0 <= 2685 and 2315 <= self.series1_1 <= 2685        # sprawdzamy, czy wszystkie serie mieszczą się w przedziałach
              and 1114 <= self.series2_0 <= 1386 and 1114 <= self.series2_1 <= 1386  # i wyświetlamy wynik testu 
              and 527 <= self.series3_0 <= 723 and 527 <= self.series3_1 <= 723 
              and 240 <= self.series4_0 <= 384 and 240 <= self.series4_1 <= 384 
              and 103 <= self.series5_0 <= 209 and 103 <= self.series5_1 <= 209 
              and 103 <= self.series6_0 <= 209 and 103 <= self.series6_1 <= 209):
            passed = True
        else:
            passed = False


        print("Seria 1:")
        print("\t0 - " + str(self.series1_0))
        print("\t1 - " + str(self.series1_1))

        print("Seria 2:")
        print("\t0 - " + str(self.series2_0))
        print("\t1 - " + str(self.series2_1))

        print("Seria 3:")
        print("\t0 - " + str(self.series3_0))
        print("\t1 - " + str(self.series3_1))

        print("Seria 4:")
        print("\t0 - " + str(self.series4_0))
        print("\t1 - " + str(self.series4_1))

        print("Seria 5:")
        print("\t0 - " + str(self.series5_0))
        print("\t1 - " + str(self.series5_1))

        print("Seria 6:")
        print("\t0 - " + str(self.series6_0))
        print("\t1 - " + str(self.series6_1))
        if passed:
           print ("\nPomyślny: TAK")
        else:
           print ("\nPomyślny: NIE")
        print("-----\n")



    def longSeriesTest(self):
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return

        lastValue = ''
        count = 0


        if self.maxCount == 0:
             for bin in self.binStr:
                if lastValue == '':
                    lastValue = bin
                    count =1
                    continue

                if bin == lastValue:
                    count = count+1
                else:
                    checkCount(self,count,bin)
                    count = 1
                    lastValue = bin
             checkCount(self,count,lastValue)
        print("Test długiej serii")
        print("-----")
        print("Najdłuższa seria ma długość - " + str(self.maxCount))
         
        if self.maxCount <26:
           print ("\nPomyślny: TAK")
        else:
           print ("\nPomyślny: NIE")
        print("-----\n")


    def pokerTest(self): ##
        if len(self.binStr) != 20000:
            print("Nie podano prawidłowego ciągu!")
            return
        segmentsCount= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # tworzymy listę o długości 16 - 2^4
        segmentsString = ["","","","","","","","","","","","","","","",""] #tworzymy listę o długości 16 - potrzebna tylko do wyświetlania
        for val in wrap(self.binStr,4): # funkcja wrap dzieli ciąg na podciągi, każdy o długości 4 bitów
            segVal = int(val,2) # oblcizamy wartość całkowitoliczbową  i przypisujemy do odpowiedniego miejsca w liście
            segmentsCount[segVal]= segmentsCount[segVal] + 1 # index w liście jest równy wartości bitów
            segmentsString [segVal]= val
        testVal = (16/5000 * sum(x*x for x in segmentsCount)) - 5000  # obliczamy wynik testu

        for i in range(0,16):
            print("Ilość wystąpień '" + segmentsString[i]+"' - " + str(segmentsCount[i]))

        print("X = " + str(testVal))
        
        if 2.16 <= testVal <= 46.17: # sprawdzamy, czy wynik mieści się w przedziale
           print ("\nPomyślny: TAK")
        else:
           print ("\nPomyślny: NIE")
        print("-----\n")
    
        

