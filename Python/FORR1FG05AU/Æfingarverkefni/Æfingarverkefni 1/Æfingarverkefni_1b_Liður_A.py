'''
Höfundur Hrólfur
Æfingarverkefni 1b Liður A
'''
#Hérna fæ ég upplýsingarnar frá notandanum
karl=input("Hvað Heitir Karlinn?")
kona=input("Hvað Heitir Konan?")
kronur=int(input("Hvað kostuðu Skórnir?"))
#Þetta er til þess að ég geti hafn nöfn karlsins og konunar í eitthverju sem notandinn á að svara
strengur="Hvaða skónúmer voru skórnir sem "+str(karl)+" keypti fyrir "+str(kona)+"?"
skonumer=int(input(strengur))
#útreykningar
skonumer_retta=skonumer+2
#Hérna sýni ég notandanum söguna
print("karl keypti skónúmer",skonumer,"fyrir",kona,"sem kostuðu",kronur,"krónur")
print("En þá mundi hann að hún notar skónúmer",skonumer_retta)
