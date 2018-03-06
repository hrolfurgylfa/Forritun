'''
Æfingarverkefni_föll_1
Hrólfur Gylfason
29/1/2018
'''

def brandari():
    brandari = "Einu sinni voru tveir menn að tala saman.  Annar maðurinn sagði: Ég festist í lyftu í tvo klukkutíma í gær þá sagði hinn maðurinn það er nú ekkjert ég festist í rúllustiga í fjóra klukkutíma"
    return brandari

def brandari1():
    brandari = "Það var maður sem fór til læknis og sagðist eiga við vandamál að stríða, nú sagði læknirinn, hvað er vandamálið. Jú sjáðu til ég þarf alltaf að kúka kl 9 á morgnana. Er það eitthvað vandamál, sagði læknirinn. Já sagði maðurinn ég vakna aldrei fyrr en 10."
    return brandari

def brandari2():
    brandari = "Einu sinni var maður sem átti pafagauk og var að reyna að kenna honum að tala og sagði ég heiti palli og fuglinn sagði ég heiti palli ,maðurinn sagði ég get flogið og páfagaukurinn sagði það væri gaman að sjá það."
    return brandari

def brandari3():
    brandari = 'Einu sinni voru björn og kanína að labba um í skóginum, en þeir voru að rífast. allt í einu kom andi og gaf þeim 3.óskir hvor um sig. Björnin óskaði þess að hann væri svo fallegur að allar kvenbirnir óskuðu þess að vera með honum. Og það var hann. Kanínan óskaði þess að eignast mótorhjól. Og svo var það. Björninn vildi núna vera eini karlbjörninn í landinu, svo var það. Kanínan vildi svo eignast hjálm fyrir mótorjhólið, og það varð. Svo vildi björninn vera eini karlbjörninn í veröldinni, og það varð. Þá kveikti kanínan á hjólinu, og sagði:,,Ég vildi óska að björninn væri hommi!!!" Og þaut af stað'
    return brandari

def kyn_def(kyn = "hk"):
    if kyn == "kk":
        return "Þú ert karlmaður"
    elif kyn == "kvk":
        return "Þú ert kvennmaður"

    elif kyn == "hk":
        return "Ég þekki ekki þetta kyn"


valmynd = ""

while valmynd != "4":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print(brandari())

    elif valmynd == "2":#Liður 2
        val = input("Sláðu inn 1, 2, eða 3 til þess að velja brandara ")

        print()

        if val == "1":
            print(brandari1())

        elif val == "2":
            print(brandari2())

        elif val == "3":
            print(brandari3())
        
    elif valmynd == "3":#Liður 3
        print(kyn_def("kk"))
        print(kyn_def())

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
