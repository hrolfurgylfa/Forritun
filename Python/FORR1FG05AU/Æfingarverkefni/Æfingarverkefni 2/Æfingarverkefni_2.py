'''
Höfundur Hrólfur
ifSetningar
'''
while True:#endalaus lúppa(ekki nota þetta sem aðal aðferð)
    #valmynd
    print("\n-----Valmynd-----")
    print("1.Liður 1")
    print("2.Liður 2")
    print("3.Liður 3")
    print("4.Liður 4")
    print("5.Liður 5")
    liður_val=input("Sláðu inn 1, 2, 3, 4 eða 5 ==> ")
    if liður_val=="1":
        print("\n\nÞetta er liður 1\n")
        tala1=input("Skrifaðu inn heiltölu ")
        tala2=input("Skrifaðu inn aðra heiltölu ")
        if tala1<tala2:
            print("Fyrri talan er minni en seinni talan")
        elif tala1>tala2:
            print("Seinni talan er minni en fyrri talan")
        elif tala1==tala2:
            print("Tölurnar eru jafn stórar")
        else:
            print("\nERROR")
    elif liður_val=="2":
        print("\n\nÞetta er liður 2\n")
        manudur=input("Hvað heitir mánuðurinn sem er núna? ")
        if manudur=="Janúar":
            print("janúar er mánuður númer 1")
        elif manudur=="febrúar":
            print("febrúar er mánuður númer 2")
        elif manudur=="mars":
            print("mars er mánuður númer 3")
        elif manudur=="apríl":
            print("apríl er mánuður númer 4")
        elif manudur=="maí":
            print("maí er mánuður númer 5")
        elif manudur=="júní":
            print("júní er mánuður númer 6")
        elif manudur=="júlí":
            print("júlí er mánuður númer 7")
        elif manudur=="ágúst":
            print("ágúst er mánuður númer 8")
        elif manudur=="september":
            print("september er mánuður númer 9")
        elif manudur=="október":
            print("október er mánuður númer 10")
        elif manudur=="nóvember":
            print("nóvember er mánuður númer 11")
        elif manudur=="desember":
            print("desember er mánuður númer 12")
        else:
            print("Ég þekki ekki þennan mánuð")
    elif liður_val=="3":
        print("\n\nÞetta er liður 3\n")
    elif liður_val=="4":
        print("\n\nÞetta er liður 4\n")
    elif liður_val=="5":
        print("\n\nÞetta er liður 5\n")
    else:
        print("\n\n\nERROR Þú verður að slá inn 1, 2, 3, 4 eða 5")
