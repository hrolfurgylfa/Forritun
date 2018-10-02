'''
Tímaverkefni 1 Try/Except
Hrólfur Gylfason
28/9/2018
'''
import random
from time import sleep
import datetime

def gisk_tala():
    tala = random.randint(1,1000)

    return tala

def skoda_gisk(rett_tala, gisk_tala):
    if rett_tala == gisk_tala:
        return "R"#R stendur fyrir rétt
    elif gisk_tala == 0:
        return "F"#F stendur fyrir fara
    elif rett_tala < gisk_tala:
        return "<"#Þetta er ör niður
    elif rett_tala > gisk_tala:
        return ">"#Þetta er ör upp

def kasta_pening():
    hlid = bool(random.getrandbits(1))

    return hlid

def prentaVikudag():
    vikudagur = datetime.datetime.today().weekday()
    if vikudagur == 0: return "Mánudagur"
    elif vikudagur == 1: return "Þriðjudagur"
    elif vikudagur == 2: return "Miðvikudagur"
    elif vikudagur == 3: return "Fimmtudagur"
    elif vikudagur == 4: return "Föstudagur"
    elif vikudagur == 5: return "Laugardagur"
    elif vikudagur == 6: return "Sunnudagur"

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
        print("Sláðu inn 0 til þess að hætta")
        halda_afram = True
        while halda_afram is True:
            rett_tala = gisk_tala()

            while True:
                try:
                    tala = int(input("Giskaðu á tölu\n--->"))

                    nidurstada = skoda_gisk(rett_tala, tala)

                    print()
                    if nidurstada == "R":
                        print("Vel gert. Þú fannst réttu tölunna")
                        spila_aftur = input("Viltu spila aftur(J/N)?\n--->").lower()
                        if spila_aftur == "j":
                            halda_afram = True
                            break
                        elif spila_aftur == "n":
                            halda_afram = False
                            break
                        else:
                            print("\nÞú svaraðir með hvorugu svo að þú ert ekki að spila aftur")
                            halda_afram = False
                            break
                    
                    elif nidurstada == "F":
                        halda_afram = False
                        break
                    elif nidurstada == "<": print("Talan er of há. reyndu aftur.\n")
                    elif nidurstada == ">": print("Talan er of lág. reyndu aftur.\n")
                    
                except ValueError:
                    print("\nVinsamlegast sláðu inn heiltölu")

    elif valmynd == "2":#Liður 2
        val2 = ""
        lodna = 0
        skjaldamerki = 0

        while val2 != "2":
            print("-------------------------")
            print("Ýttu á 1 til þess kasta peningi")
            print("Ýttu á 2 til þess hætta")
            val2 = input("----->")
            print("-------------------------")

            if val2 == "1":
                hlid = kasta_pening()
                if hlid is True:
                    skjaldamerki += 1
                    print("Skjaldamerki")

                    print("\nSkjaldamerki hefur komið upp",skjaldamerki,"sinnum")
                    print("Loðna hefur komið upp",lodna,"sinnum")
                
                elif hlid is False:
                    lodna += 1
                    print("Loðna")

                    print("\nSkjaldamerki hefur komið upp",skjaldamerki,"sinnum")
                    print("Loðna hefur komið upp",lodna,"sinnum")

            elif val2 == "2":
                print("Bless")
            else:
                print("Sláðu inn 1 eða 2")
        
    elif valmynd == "3":#Liður 3
        sekundur = 1.0
        while sekundur > 0:
            print("Takk.")
            sleep(sekundur)
            sekundur -= .1
        
        print("\nEigðu góðan dag.")
        print(prentaVikudag(),end=" ")

        now = datetime.datetime.now()
        print(str(now.day)+"/"+str(now.month)+"/"+str(now.year))

    elif valmynd == "4":##Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
