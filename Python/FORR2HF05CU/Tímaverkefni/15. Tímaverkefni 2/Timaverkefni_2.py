'''
Tímaverkefni 2
Hrólfur Gylfason
2/11/2018
'''
import random

class Tolur():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def gera_lista(self, byrja, enda, haekkun):
        return [x for x in range(byrja, enda, haekkun)]
        
    def gera_dict(self, listi):
        dict1 = {}
        tel = 0

        for hlutur in [self.a, self.b, self.c]:
            dict1[hlutur] = listi[tel]
            tel += 1

        return dict1
    
    def summa(self, *args):
        return sum(args)
    
    def lamban(self, listi):
        return list(filter(lambda x: x>50 and x<90 and x%2==0, listi))

class Geimvera():
    def __init__(self):
        self.frumnafn = "Geimvera"
    
    def HverErEg(self):
        return "Ég er geimvera"
class Venus(Geimvera):
    def __init__(self, litur, tala):
        self.nafn = "Venus"
        self.litur = litur
        self.tala = tala
    
    def HverErEg(self):
        return "Ég er geimvera frá "+str(self.nafn)+", talan er "+str(self.tala)+" og liturinn er "+str(self.litur)
class Mars(Geimvera):
    def __init__(self, litur, tala):
        self.nafn = "Mars"
        self.litur = litur
        self.tala = tala
    
    def HverErEg(self):
        return "Ég er geimvera frá "+str(self.nafn)+", talan er "+str(self.tala)+" og liturinn er "+str(self.litur)

def tolur(*args):
    return list(filter(lambda x: x % 5 == 0, args))

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
        print(tolur(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20))

    elif valmynd == "2":#Liður 2
        listi1 = ["Konni", "Sigga", "Snorri"]
        listi2 = ["fótbolta", "handbolta", "blaki"]

        listi3 = [nafn+" er í "+random.choice(listi2) for nafn in listi1]
        print(listi3)
        
    elif valmynd == "3":#Liður 3
        tilvik1 = Tolur("Banani", "Epli", "Appelsína")

        print(tilvik1.gera_lista(2, 18, 3))
        print(tilvik1.gera_dict([1,5,9]))
        print(tilvik1.summa(1,4,6,8,12,15,18,24,29,32,46,48))
        print(tilvik1.lamban([18,24,29,32,46,48, 53, 58, 62, 77, 82, 96, 104, 109, 128]))
    
    elif valmynd == "4":#Liður 4
        hlutur1 = Geimvera()
        hlutur2 = Venus("gulur", "22")
        hlutur3 = Mars("rauður", "136")

        print(hlutur1.frumnafn)
        print(hlutur1.HverErEg())
        print(hlutur2.nafn)
        print(hlutur2.HverErEg())
        print(hlutur3.nafn)
        print(hlutur3.HverErEg())

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
