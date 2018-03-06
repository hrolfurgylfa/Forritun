'''
Hrólfur Gylfason 2017
Æfingarverkefni For lykkjur
'''
val="0"

while val!="i":
    print("Ýttu á A til þess að skoða lið A")
    print("Ýttu á B til þess að skoða lið B")
    print("Ýttu á C til þess að skoða lið C")
    print("Ýttu á D til þess að skoða lið D")
    print("Ýttu á E til þess að skoða lið E")
    print("Ýttu á F til þess að skoða lið F")
    print("Ýttu á G til þess að skoða lið G")
    print("Ýttu á H til þess að skoða lið H")
    print("Ýttu á I til þess að hætta")
    val=input("------------------------------------->").lower()

    if val=="a":
        for tel in range(1000,10000):
            print(tel, end="  ")

    elif val=="b":
        tala_1=int(input("Sláðu inn fyrri heiltöluna "))
        tala_2=int(input("Sláðu inn seinni heiltöluna "))
        if tala_1==tala_2 or tala_1+1==tala_2:
            print("ERROR\tSláðu inn tölur lengra frá hver annari\n")
            print()

        else:
            for tel in range(tala_1+1,tala_2):
                print(tel,end="  ")
                print()

    elif val=="c":
        tala_1=int(input("Sláðu inn fyrri heiltöluna "))
        tala_2=int(input("Sláðu inn seinni heiltöluna "))
        if tala_1>tala_2:
            for tel in range(tala_1, tala_2-1,-1):
                print(tel,end="  ")
                print()
        else:
            for tel in range(tala_1, tala_2+1):
                print(tel,end="  ")
                print()

    elif val=="d":
        tala_1=int(input("Sláðu inn fyrri heiltöluna "))
        tala_2=int(input("Sláðu inn seinni heiltöluna "))
        if tala_1>tala_2:
            if tala_2%2==0:
                tala_2=tala_2+1
            for tel in range(tala_1, tala_2-1,-2):
                print(tel,end="  ")
                print()
        else:
            if tala_1%2==0:
                tala_1=tala_1+1
            for tel in range(tala_1, tala_2+1,2):
                print(tel,end="  ")
                print()

    elif val=="e":
        tala_1=int(input("Sláðu inn fyrri heiltöluna "))
        tala_2=int(input("Sláðu inn seinni heiltöluna "))
        if tala_1>tala_2:
            for tel in range(tala_1, tala_2-1,-1):
                print(tel,"og",tel*tel,end="\t\t")
                print()
        else:
            for tel in range(tala_1, tala_2+1):
                print(tel,"og",tel*tel,end="\t\t")
                print()
                
    elif val=="f":
        tala_lægri=int(input("Sláðu inn lægri töluna "))
        tala_hærri=int(input("Sláðu inn hærri töluna "))
        summa=0
        for tel in range(tala_lægri, tala_hærri+1):
            summa=summa+tel
            if tel==tala_hærri:
                print(tel,end="=")
                
            else:
                print(tel, end="+")
        print(summa)
        
    elif val=="g":
        m_tafla=int(input("Sláðu inn hvaða margföldunartöflu þig langar að sjá "))
        for tel in range(m_tafla, m_tafla*10+1, m_tafla):
            print(tel, end=" ")
        print("\n")
    elif val=="h":
        haed=0
        haed=float(input("Sláðu inn hæð þína í metrum "))
        print("BMI fyrir þessa hæð er:")
        print("Þyngd\tBMI")
        for þyngd in range(60, 126, 5):
            haed2=haed*haed
            bmi=þyngd/haed2
            print(þyngd, end="\t")
            print(round(bmi, 2))
        print()

    elif val=="i":
        for tel in range(50):
            print("\n")
    
    else:
        print("ERROR\tÝttu á A, B, C, D, E, F, G, H eða I")
        print()
    
