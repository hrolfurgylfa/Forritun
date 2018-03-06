'''
Höfundur: Hrólfur Gylfason
Hlutapróf 1
'''

#Dæmi 1
#Hérna spyr ég notandann um hvað hann heitir uppáhalds lit hans og hvaða strætó hann tekur oftast
nafn_D1=input("Hvað heitir þú? ")
ULitur_D1=input("Hvað er uppáhalds liturinn þinn? ")
Straeto_D1=input("Hvað er númer strætósins sem þú tekur oftast? ")
#Hérna svara ég notandanum með nafninu hans, uppáhalds lit og númerinu á strætónum sem notandinn notar oftast
print("Góðan dag",nafn_D1,", uppáhalds liturinn þinn er",ULitur_D1,"og þú tekur oftast strætó númer",Straeto_D1)


#Dæmi 2
#Hérna spyr ég um hæð notanda
haed=int(input("Hvað ertu stór í sentímetrum? "))
#Hérna segi ég eitthvað við notandann
if haed<147:
    print("Smávaxin eða barn")
else:
    print("Alltaf að vaxa")
if haed>251:
    print("Nei nú lýgur þú!")


#Dæmi 3
#Hérna bið ég um 3 tölur
tala1=int(input("Sláðu inn tölu eitt "))
tala2=int(input("Sláðu inn tölu tvö "))
tala3=int(input("Sláðu inn tölu þrjú "))
#Útreykningar
summa=(tala1+tala2)-tala3
#Hérna segi ég notandanum hvað svarið er
print("(",tala1,"+",tala2,")-",tala3,"=",summa)


#Dæmi 4
#Hérna spyr ég notandann hvort hann vilji reykna flatarmál ferhyrnings, þríhyrnings eða hryngs
print("Ef þú villt reykna flatarmál ferhyrnings ýttu á 1")
print("Ef þú villt reykna flatarmál þríhyrnings ýttu á 2")
print("Ef þú villt reykna flatarmál hrings ýttu á 3")
valmynd=input("-------------------------------------------> ")
#Hérna fer notandinn ef hann velur að reykna flatarmál ferhyrnings
if valmynd=="1":
    print("Þú valdir að reykna flatarmál ferhyrnings")
    #Hérna spyr ég notandann um lengd og breidd ferhyrningsins
    lengd=float(input("Hver er lengd ferhyrningsins? "))
    breidd=float(input("Hver er breidd ferhyrningsins? "))
    #Útreykningar
    flatarmálFerhyrningsins=lengd*breidd
    #Hérna segi ég notandanum hvað flatarmál ferhyrningsins er
    print("Flatarmál ferhyrningsins er",round(flatarmálFerhyrningsins,2))
elif valmynd=="2":
    #Hérna fer notandinn ef hann velur að reykna flatarmál þríhyrnings
    print("Þú valdir að reykna flatarmál þríhyrnings")
    #Hérna spyr ég notandann um grunnlínu og hæð þríhyrningsins
    gLina=float(input("Hversu stór er grunnlína þríhyrningsins? "))
    haed_þri=float(input("Hver er hæð þríhyrningsins? "))
    #Útreykningar
    flatarmálÞríhyrningsins=gLina*haed_þri/2
    #Hérna segi ég notandanum hvað flatarmál þríhyrningsins er
    print("Flatarmál þríhyrningsins er",round(flatarmálÞríhyrningsins,2))
elif valmynd=="3":
    #Hérna fer notandinn ef hann velur að reykna flatarmál hrings
    print("Þú valdir að reykna flatarmál hrings")
    #Hérna spyr ég notandann um radíus hringsins
    radius=float(input("Hversu stór er radíusinn? "))
    #Útreykningar
    flatarmálHrings=(radius*radius)*3.14
    #Hérna segi ég notandanum hvað flatarmál hringsins er
    print("Flatarmál hringsins er",round(flatarmálHrings,2))
#Hérna seegi ég error og notandanum að slá inn 1, 2 eða 3 ef hann slær inn ranga tölu
else:
    print("Error\tSláðu inn 1, 2 eða 3")
