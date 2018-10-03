'''
Æfingarverkefni 3 - Klasar
Hrólfur Gylfason
3/10/2018
'''
import random
import time

class trapisaTest:
    def __init__(self, haed = 0, a = 0, b = 0, c = 0, d = 0):
        self.minustolur = False
        for breyta in [haed, a, b, c, d]:
            if breyta < 0:
                print("Þessar breytur meiga ekki vera mínustölur")
                self.minustolur = True
                break

        self.haed = haed
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def ummal_trapisu(self):
        if self.minustolur:
            print("Þessar breytur meiga ekki vera mínustölur")
            return "Villa"

        ummal = self.a + self.b + self.c + self.d
        return ummal

    def flatarmal_trapisu_1(self):
        if self.minustolur:
            print("Þessar breytur meiga ekki vera mínustölur")
            return "Villa"

        s = (self.a + self.b + self.c + self.d)/2
        return s
    
    def flatarmal_trapisu_2(self):
        if self.minustolur:
            print("Þessar breytur meiga ekki vera mínustölur")
            return "Villa"
            
        flatarmal = self.haed * ((self.a + self.c) / 2)
        return flatarmal

    def trapisa_jafnarma(self):
        if self.minustolur:
            print("Þessar breytur meiga ekki vera mínustölur")
            return "Villa"
            
        if self.b == self.d:
            return True
        else:
            return False

    def Lestu_mig(self):
        print("Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða.")

class bill:
    def __init__(self, tegund, argerd):
        self.tegund = tegund
        self.argerd = argerd
        self.dottinn_ut = False
        self.hradi = random.randint(30, 60)
        self.bensin = random.randint(20, 120)
        if self.bensin > 100:
            self.eydsla = random.randint(8, 15)
        elif self.hradi < 35:
            self.eydsla = random.randint(1, 3)
        else:
            self.eydsla = random.randint(1, 10)

    def keppa(t1, t2, t3):
        for keppni in range(10):
            for keppandi in [t1, t2, t3]:
                if keppandi.dottinn_ut is not True:
                    keppandi.bensin -= keppandi.eydsla
                    if keppandi.bensin <= 0:
                        keppandi.dottinn_ut = True
                        print(keppandi.tegund,"er orðinn bensínlaus og er þess vegna dotinn út úr kepninni")
                    else:
                        print(keppandi.tegund,"er enþá í kepninni")
            
            time.sleep(.5)
            print("-------------------------")
        
        keppendur_eftir = []
        keppendur_dottnir_ut = []

        for keppandi in [t1, t2, t3]:
            if keppandi.dottinn_ut is not True:
                keppendur_eftir.append(keppandi)
                
            else:
                keppendur_dottnir_ut.append(keppandi)
        


valmynd = ""

while valmynd != "5":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        trapisa = trapisaTest(3, 2, 3, 4, 3)

        print("Ummál:",trapisa.ummal_trapisu())
        print("Flatarmál 1:",trapisa.flatarmal_trapisu_1())
        print("Flatarmál 2:",trapisa.flatarmal_trapisu_2())
        jafnarma = trapisa.trapisa_jafnarma()

        if jafnarma is True:
            print("Þessi trapisa er jafnarma")
        elif jafnarma is False:
            print("Þessi trapisa er ekki jafnarma")
        else:
            print("Villa, það er ekki hægt að hafa trapisu með neikvæðar mælieiningar")

        trapisa.Lestu_mig()

    elif valmynd == "2":#Liður 2
        pass
        
    elif valmynd == "3":#Liður 3
        bill1 = bill("Lexus", "2002")
        bill2 = bill("VolfsWagen", "2018")
        bill3 = bill("Porche", "2001")

        bill.keppa(bill1, bill2, bill3)

    elif valmynd == "4":#Liður 4
        pass

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
