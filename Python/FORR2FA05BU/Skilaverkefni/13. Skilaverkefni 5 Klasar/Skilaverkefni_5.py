'''
-----Verkefni-----
Hrólfur Gylfason
-----Dagsetning-----
'''
import math

class Hringur():
    def ummal(radius):
        return radius * 2 * math.pi
    def flatarmal(radius):
        return radius * radius * math.pi
    def rummal(radius):
        return (4 * math.pi * (radius * radius * radius)) / 3

class Jofnur():
    def jafna1(x):
        y = 3*x + 4 + 2*(x*x*x)
        return y
    def jafna2(x,z):
        y = ((z*z)+(x*x))*4
        return y

class Hnit():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def hnitaPrentari(self):
        print("x hnitið er",self.x,"og y hnitið er",self.y)
    def hlutaPrentari(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 or self.y == 0:
            print("Annað hnitið er 0 svo að hnitið er ekki í neinum kassa")

valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print("Ummál með radíusinn 5:",round(Hringur.ummal(5),3))
        print("Flatarmál með radíusinn 5:",round(Hringur.flatarmal(5),3))
        print("Rúmmál með radíusinn 5:",round(Hringur.rummal(5),3))

        print()

        print("Fyrri jafnan X = 7, Y =",Jofnur.jafna1(7))
        print("Seinni jafnan X = 3, Z = 9, Y =",Jofnur.jafna2(3,9))

    elif valmynd == "2":#Liður 2
        Hnit.hnitaPrentari

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")
