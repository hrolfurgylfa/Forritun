'''
Hrólfur Gylfason 2017
Æfingarverkefni For lúppur
'''
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="5":
    print("Ýttu á 1 til þess að skoða lið eitt")
    print("Ýttu á 2 til þess að skoða lið tvö")
    print("Ýttu á 3 til þess að skoða lið þrjú")
    print("Ýttu á 4 til þess að skoða lið fjögur")
    print("Ýttu á 5 til þess að hætta")
    val=input("-------------------------------------> ")

    if val=="1":
        pass

    elif val=="2":
        lengd=int(input("Sláðu inn lengd ferhyrningsins "))
        breydd=int(input("Sláðu inn breydd ferhyrningsins "))
        for x in range(lengd):
            for y in range(breydd):
                print("#", end="")
            print()
            
    elif val=="3":
        for x in range(7):
            for z in range(7-x):
                print("#", end="")
            print()
        for x in range(7):
            for z in range(x+1):
                print("#", end="")
            print()

    elif val=="4":
        b_gildi=int(input("Sláðu inn byrjunargildi "))
        e_gildi=int(input("Sláðu inn endagildi "))
        step=int(input("Sláðu inn step "))
        print("Liður 1\n")
        for tel in range(b_gildi, e_gildi+1, step):
            print(tel, end=" ")
        print()
        print("Liður 2\n")
        for tel in range(e_gildi, b_gildi-1, step-step*2):
            print(tel, end=" ")
        print()
        print("Liður 3\n")
        for tel in range(b_gildi, e_gildi+1, step):
            if tel % 2==0:
                print(tel, end=" ")
            else:
                pass
        print()
        print("Liður 4\n")
        for tel in range(b_gildi, e_gildi+1, step):
            print(tel*tel*tel, end=" ")
        print()
        print("Liður 5\n")
        teljari=1
        for tel in range(b_gildi, e_gildi+1, step):
            print(tel, end=" ")
            if teljari%3==0:
                 print()
            teljari=teljari+1
        print()
        
    elif val=="5":
        pass
    
    else:
        print("ERROR\trangur innsláttur")

