'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 1 Liður 6
'''
#Hérna fæ ég aldur þriggja einstaklingana
aldur_einstaklingur_1=int(input("Hvað er einstaklingur 1 gamall? "))
aldur_einstaklingur_2=int(input("Hvað er einstaklingur 2 gamall? "))
aldur_einstaklingur_3=int(input("Hvað er einstaklingur 3 gamall? "))
#Hérna reikna ég út meðalaldurinn
medalaldur=(aldur_einstaklingur_1+aldur_einstaklingur_2+aldur_einstaklingur_3)/3
#Hérna segi ég notandanum meðalaldurinn
print("Meðalaldur þessara einstaklinga er",round(medalaldur,2),"ára")
