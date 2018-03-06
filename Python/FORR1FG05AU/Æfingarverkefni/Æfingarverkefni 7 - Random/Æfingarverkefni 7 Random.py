'''
Hrólfur Gylfason 2017
Æfingarverkefni 7 - Random
'''
import random

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
        random_tala=random.randint(1,6)
        print(random_tala)

    elif val=="2":
        for tel in range(5):
            random_tala=random.randint(1,6)
            print(random_tala, end=" ")
        print()

    elif val=="3":
        summa=0
        o_summa=0
        for tel in range(25):
            random_tala=random.randint(1,999)
            summa+=random_tala
            if random_tala%2==1:
                print(random_tala,"Hei ég fann oddatölu")
                o_summa+=random_tala
            else:
                print(random_tala)
        print()
        print("Summa talnana er",summa,"og summa oddatalnana er",o_summa)

    elif val=="4":
        tala99=0
        strengur=""
        for tel in range(250):
            random_tala=random.randint(25, 115)
            if random_tala==73:
                print(random_tala, end=" ")
                break
            elif random_tala==99:
                strengur+="99 "
            else:
                print(random_tala, end=" ")
        print(strengur)

    elif val=="5":
        pass
    
    else:
        print("ERROR\trangur innsláttur")

