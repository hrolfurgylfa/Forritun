'''
Æfingarverkefni 6 Generator föll og comprehension
Hrólfur Gylfason
31/10/2018
'''
def faHeiltolu(texti):
    try:
        heiltala = int(input(texti))
    except ValueError:
        print("Sláðu inn heiltölu")
    return heiltala

def teljarinn():
    for tel in range(1,6):
        texti = "Nú hefur verið náð í mig í "+str(tel)+". sinn."
        print(texti)
        yield texti

def listaPrentun(listi):
    for i in listi:
        print(i)
        yield i


valmynd = ""

while valmynd != "4":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        a = teljarinn()
        hversu_oft = faHeiltolu("Hversu oft viltu keyra fallið teljarinn(max 5)\n--->")
        for tel in range(hversu_oft):
            next(a)

    elif valmynd == "2":#Liður 2
        listi = ["Banani","Epli","Appelsína","Mandarína","Kiwi"]
        a = listaPrentun(listi)
        for tel in range(4):
            next(a)
        
    elif valmynd == "3":#Liður 3
        listi = [x for x in range(1,1001) if x % 2 == 1 and x % 5 == 0]
        print(listi)

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
