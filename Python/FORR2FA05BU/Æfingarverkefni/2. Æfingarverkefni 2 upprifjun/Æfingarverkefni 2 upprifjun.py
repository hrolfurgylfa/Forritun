'''
Æfingarverkefni 2 upprifjun
Hrólfur Gylfason
15/1/2018
'''
valmynd = ""

while valmynd != "6":

    for tel in range(50):
        print("-",end="")
    print("\n")

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að hætta")
    valmynd = input("-------------------->>> ")

    print()
    for tel in range(50):
        print("-",end="")
    print()

    if valmynd == "1":
        nafn_p1 = input("Sláðu inn fyrsta nafn fyrri persónunar ")
        haed_p1 = input("Sláðu inn hæð fyrri persónunar ")
        nafn_p2 = input("Sláðu inn fyrsta nafn seinni persónunar ")
        haed_p2 = input("Sláðu inn hæð seinni persónunar ")

        print()

        if haed_p1 > haed_p2:
            print(nafn_p1,"er hærri en",nafn_p2)

        elif haed_p1 < haed_p2:
            print(nafn_p2,"er hærri en",nafn_p1)

        else:
            print(nafn_p1,"og",nafn_p2,"eru jafn há/ar/ir")

    elif valmynd == "2":
        lengd = int(input("Sláðu inn lengd svæðis í metrum "))
        breidd = int(input("Sláðu inn breidd svæðis í metrum "))

        print()

        print("Þessi reitur er",round((lengd*breidd)/4046,3),"ekrur")
        
    elif valmynd == "3":
        breidd = int(input("Sláðu inn breidd ferhyrnds reits "))

        print("-------------------------")

        print("Stærð\tLengd í ekrum")
        print()
        for lengd in range(10,201,10):
            print(lengd,"\t",round((lengd*breidd)/4046,6))

    elif valmynd == "4":
        afangi = input("Sláðu inn skammstöfun áfanga ")
        
        print()

        if len(afangi) == 7:
            if afangi[0:3].isalpha() and afangi[0:3].isupper():
                if afangi[3:7].isdigit():
                    print("Þetta er rétt skammstöfun á áfanga")
                else:
                    print("Þetta er ekki rétt skammstöfun á áfanga")
            else:
                print("Þetta er ekki rétt skammstöfun á áfanga")
        else:
            print("Þetta er ekki rétt skammstöfun á áfanga")

    elif valmynd == "5":
        heild = int(input("Sláðu inn heildina "))
        prosenta = int(input("Sláðu inn prósentuna af heildinni "))

        print()
        
        print(prosenta,"%","af",heild,"er",round(heild/100*prosenta,2))

    elif valmynd == "6":
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 6")
