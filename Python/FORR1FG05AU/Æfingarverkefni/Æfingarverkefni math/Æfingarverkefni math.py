import math
val="1"
while val !="5":
    print("--------------------------------------------------\n")
    print("1: Þriðja veldi")
    print("2: Langhlið þríhyrnings")
    print("3: Mismunur, algildi (e. absolute value)")
    print("4: Ummál og flatarmál hrings og rúmmál kúlu")
    print("5: Hætta")
    val=input("-------------------------------------> ")

    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":
        tala=int(input("Sláðu inn heiltölu "))
        print("Þessi tala í þriðja veldi er",math.pow(tala,3))

    elif val=="2":
        a=int(input("Sláðu inn lengd hliðar a "))
        b=int(input("Sláðu inn lengd hliðar b "))
        c=math.sqrt(math.pow(a,2)+math.pow(b,2))
        print("Lengd langhliðarinnar er",c)
        
    elif val=="3":
        tala_1=int(input("Sláðu inn tölu eitt "))
        tala_2=int(input("Sláðu inn tölu tvö "))
        mismunur=math.fabs(tala_1-tala_2)
        print("Mismunur þessara talna er",mismunur)

    elif val=="4":
        radius=int(input("Sláðu inn radíus kúlunnar "))
        ummal=2*radius*math.pi
        flatarmal=math.pow(radius,2)*math.pi
        rummal=(4*math.pow(radius,3)*math.pi)/3
        print("Ummálið er",round(ummal,2))
        print("Flatarmálið er",round(flatarmal,2))
        print("Rúmmálið er",round(rummal,2))

    elif val=="5":
        pass
    
    else:
        print("ERROR\trangur innsláttur")
