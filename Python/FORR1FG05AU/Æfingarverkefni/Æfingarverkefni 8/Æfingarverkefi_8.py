'''
Hrólfur Gylfason 2017
Æfingarverkefni 8
'''
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="5":
    print("--------------------------------------------------\n")
    print("Ýttu á 1 til þess að skoða lið eitt")
    print("Ýttu á 2 til þess að skoða lið tvö")
    print("Ýttu á 3 til þess að skoða lið þrjú")
    print("Ýttu á 4 til þess að skoða lið fjögur")
    print("Ýttu á 5 til þess að hætta")
    val=input("-------------------------------------> ")

    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":
        nafn1=input("Sláðu inn nafn 1 ")
        nafn2=input("Sláðu inn nafn 2 ")
        if len(nafn1)>len(nafn2):
            print("fyrsti stafur í lengra nafninu er",nafn1[0],"og síðasti stafurinn í lengra nafninu er",nafn1[-1])
        elif len(nafn1)<len(nafn2):
            print("fyrsti stafur í lengra nafninu er",nafn2[0],"og síðasti stafurinn í lengra nafninu er",nafn2[-1])
        else:
            print("ERROR\tNöfnin eru jafn löng")

    elif val=="2":
        nafn=input("Sláðu inn nafnið þitt ")
        print("Þetta nafn í hástöfum er",nafn.upper())
        print("Þetta nafn í lágstöfum er",nafn.lower())
        skipta_hver=input("Hvaða staf á að skipta út? ")
        skipta_ihvad=input("Hvað á að skipta stafnum í? ")
        print("Ef",skipta_hver,"er skipt í",skipta_ihvad,"verður nafnið",nafn.replace(skipta_hver,skipta_ihvad))

    elif val=="3":
        tel_b=0
        strengur=input("Sláðu inn setningu ")
        for tel in strengur:
            if tel==" ":
                tel_b+=1
        print("Fjöldi orða í þessari setningu eru",tel_b)

    elif val=="4":
        nafn=input("Sláðu inn nafn ")
        print("Nafnið afturábak er",nafn[::-1])

    elif val=="5":
        pass

    else:
        print("ERROR\trangur innsláttur")


