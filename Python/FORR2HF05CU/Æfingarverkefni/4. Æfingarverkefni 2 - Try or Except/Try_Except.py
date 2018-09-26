# import sys

# randomListi = ["a", 0, 2]

# for stak in randomListi:
#     try:
#         print("Þetta stak er", stak)
#         r = 1/int(stak)
#         break
#     except:
#         print("Oops! Þessi villa kom upp",sys.exc_info()[0])
#         print("Næsta stak.")
#         print()
    
# print("Talan", stak, "deilt með einum er", r)

'''
Æfingarverkefni 2 - Try/Except
Hrólfur Gylfason
19/9/2018
'''
import sys

def takaInnTolur(fjoldi_talna):
    toluListi = []

    while len(toluListi) < fjoldi_talna:
        try:
            tala = int(input("\nSláðu inn tölu\n--->"))
            toluListi.append(tala)
        except ValueError:
            print("\nVinsamlegast sláðu inn heiltölu")
    
    return toluListi


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
        print(takaInnTolur(10))

    elif valmynd == "2":#Liður 2
        val2 = input("Sláðu inn 1 til 6\n--->")

        if val2 == "1":
            try:
                import randoom
            except ImportError:
                print("Það er ekkert til sem heitir randoom heldur heitir það random")
        
        elif val2 == "2":
            try:
                i = 2/0
            except ZeroDivisionError:
                print("Það er ekki hægt að deila með 0")
        
        elif val2 == "3":
            try:
                dict1 = {"Stafur": "a", "tala": 0}
                print(dict1["tolur"])

            except KeyError:
                print("Þessi lykill er ekki til í dictionaryinu")
        
        elif val2 == "4":
            try:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("1")
            except IndentationError:
                print("Það eru aðeins of mörg bil")
        
        elif val2 == "5":
            try:
                pint("1")
            except SyntaxError:
                print("Það vantar r í print")
        
        elif val2 == "6":
            try:
                listi = [0, 1, 2, 3, 4]
                listi[5]
            except IndexError:
                print("Þetta stak er ekki á listanum")
        
        else:
            print("ERROR")
        
    elif valmynd == "3":#Liður 3
        try:
            tala = int(input("Sláðu inn heiltölu sem er stærri eða jafnt og -10, minni eða jaft og 200 og ekki 12\n--->"))
            print()

            if tala > 200:
                raise Exception("Þessi tala er hærri en 200")
            elif tala < -10:
                raise Exception("Þessi tala er lægri en -10")
            elif tala == 12:
                raise Exception("Þessi tala er 12")

        except ValueError:
            print("Þessi tala er ekki heiltala")

        except Exception as error:
            print(error)

    elif valmynd == "4":#Liður 4
        skra = open("skra.txt","r")
        listi = []
        tolu_listi = []

        for line in skra:
            lina = line.split(", ")
            listi.append(lina)
        
        print(listi)

        for hlutur in listi:
            print("LOOP")
            try:
                tolu_listi.append(int(hlutur))
            
            except:
                print("Óþekkt villa kom upp: ")
        
        print(tolu_listi)
            
        print("Summa talna:", sum(tolu_listi))
        print("Meðaltal talna:", sum(tolu_listi)/len(tolu_listi))

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
