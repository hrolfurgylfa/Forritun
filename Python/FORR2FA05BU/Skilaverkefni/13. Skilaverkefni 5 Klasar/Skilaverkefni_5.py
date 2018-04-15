'''
Skilaverkefni 5
Hrólfur Gylfason
'''
import math

class Hringur():#Þessi klasi reiknar ummál, flatarmál eða rúmmál hrings eftir því hvað er kallað á
    def ummal(radius):#Þetta fall tekur inn radius, reiknar ummál hringsins og skilar svo ummálinu
        return radius * 2 * math.pi
    def flatarmal(radius):#Þetta fall tekur inn radius, reiknar flatarmál hringsins og skilar svo flatarmálinu
        return radius * radius * math.pi
    def rummal(radius):#Þetta fall tekur inn radius, reiknar rúmmál kúlunar og skilar svo rúmmálinu
        return (4 * math.pi * (radius * radius * radius)) / 3

class Jofnur():#Þessi klasi reiknar tvær mismunandi jöfnur eftir því hvað er kallað á
    def jafna1(x):#Þetta fall tekur inn gildið x og skilar svo svarinu hvað y er
        y = 3*x + 4 + 2*(x*x*x)
        return y
    def jafna2(x,z):#Þetta fall tekur inn gildið x og z og skilar svo svarinu hvað y er
        y = ((z*z)+(x*x))*4
        return y

class Hnit():#Þessi klasi reiknar hnit
    def __init__(self,x,y):#Þetta fall er til þess að búa til gildin self.x og self.y sem eru svo notuð seinna í klasanum
        self.x = x
        self.y = y

    def hnitaPrentari(self):#Þetta fall prentar bara gildi x og y
        print("x hnitið er",self.x,"og y hnitið er",self.y)
    def hlutaPrentari(self):#Þetta fall skilar á hvaða helmingi hnitið er, 1, 2, 3, 4 eða 0 ef hnitið er með 0 í annaðhvort x eða y svo að það sé ekki á neinum hluta
        if x > 0 and y > 0:
            return 2
        elif x < 0 and y > 0:
            return 1
        elif x < 0 and y < 0:
            return 3
        elif x > 0 and y < 0:
            return 4
        elif x == 0 or y == 0:
            return 0

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

        x = 10
        y = 10
        h1 = Hnit(x,y)
        h1.hnitaPrentari()
        print("Þetta hnit er á reiti",h1.hlutaPrentari())

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")
