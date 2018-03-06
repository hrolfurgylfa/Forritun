'''
Hrólfur Gylfason 2018
AEfingarverkefni 1 upprifjun
'''
valmynd=""

while valmynd!="7":
    for tel in range(50):
        print("-",end="")
    print("\n")
    print("Ýttu á 1 til þess að fá Dæmi 1")
    print("Ýttu á 2 til þess að fá Dæmi 2")
    print("Ýttu á 3 til þess að fá Dæmi 3")
    print("Ýttu á 4 til þess að fá Dæmi 4")
    print("Ýttu á 5 til þess að fá Dæmi 5")
    print("Ýttu á 6 til þess að fá Dæmi 6")
    print("Ýttu á 7 til þess að hætta")
    valmynd=input("-------------------->>> ")

    print()
    for tel in range(50):
        print("-",end="")
    print()

    if valmynd=="1":
        listi_D1=[]
        tala1=int(input("Sláðu inn heiltölu "))
        tala2=int(input("Sláðu inn heiltölu "))
        print("Tölurnar lagðar saman eru",tala1+tala2,"og tölurnar margfaldaðar saman eru",tala1*tala2)
        
    elif valmynd=="2":
        fornafn_D2=input("Sláðu inn fornafnið þitt ")
        eftirnafn_D2=input("Sláðu inn eftirnafnið þitt ")
        print()
        print("Halló",fornafn_D2,eftirnafn_D2)
        
    elif valmynd=="3":
        km_D3=float(input("Sláðu inn lengd í kílómetrum "))
        print()
        print(km_D3,"kílómetrar eru",km_D3*1000,"metrar")

    elif valmynd=="4":
        laun_a_kl=int(input("Hversu mikið færð þú borgað á klukkustund? "))
        vinnutimi=int(input("Hversu margar klukkustundir vinnur þú á viku? "))
        print()
        print("Heildarlaun þín á viku eru þá",laun_a_kl*vinnutimi,"kr")
        
    elif valmynd=="5":
        laun_a_kl=int(input("Hversu mikið færð þú borgað á klukkustund? "))
        vinnutimi=int(input("Hversu margar klukkustundir vinnur þú á viku? "))
        laun_a_viku=laun_a_kl*vinnutimi
        print()
        print("Heildarlaun þín á viku eru þá",laun_a_viku,"kr")
        if laun_a_viku>=30000:
            print("Og skatturinn er",round((laun_a_viku-30000)/5,0),"kr")
        else:
            print("Og þú þarft ekki að borga skatt af þeim")

    elif valmynd=="6":
        gradur=int(input("Sláðu inn fjölda gráða: "))
        print()
        print(gradur,"gráður eru",gradur//360,"hringir og",gradur%360,"gráður")

    elif valmynd=="7":
        pass
    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 7")
