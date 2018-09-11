'''
Hrólfur Gylfason
11/9/2018
Bekkjar samansetjari
'''


valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Veldu 1 til þess að gera bekk með input")
    print("Veldu 2 til þess að gera bekk með skrá")
    print("Veldu 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        hopur = []

        magn_nafna = int(input("Hversu margir eru í hópnum\n--->"))
        print()

        fjoldi_vala = int(input("Hversu marga getur hver persóna valið\n--->"))
        print()

        for tel1 in range(magn_nafna):
            persona = []

            nafn = input("Nafn: ")
            persona.append(nafn)

            for tel2 in range(1, fjoldi_vala + 1):
                val = input("Val "+str(tel2)+": ")
                persona.append(val)
            
            hopur.append(persona)
            
            print()
        
        print(hopur)


    elif valmynd == "2":#Liður 2
        hopur = []

        # nafn_skraar = input("Nafn skráar\n--->")
        nafn_skraar = "Hopur_1.txt"
        print()

        skra = open(nafn_skraar)

        for line in skra:
            lina = line.split(",")
            lina[-1] = lina[-1][0:-1]
            hopur.append(lina)


    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")
