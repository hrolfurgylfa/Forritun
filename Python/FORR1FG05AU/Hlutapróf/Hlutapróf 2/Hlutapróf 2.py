'''
Hrólfur Gylfason 2017
Skilaverkefni 4
'''
#Liður 1
aftur="j"
while aftur=="j": 
    cm_in=int(input("Sláðu inn lengd í sentimetrum "))#input
    #útreykningar
    m_out=cm_in//100#metrar
    cm_out=cm_in%1000//100#sentimetrar
    dm_out=cm_in%100//10#desimetrar
    #úttak
    print(m_out,"metrar")
    print(dm_out,"desimetrar")
    print(cm_out,"sentimetrar")
    aftur=(input("Viltu keyra forrit aftur? Sláðu inn j ef já "))

#Liður 2
summa=1
aftur="j"
while aftur=="j": 
    #input
    tala=int(input("Sláðu inn tölu "))
    veldi=int(input("Sláðu inn veldisvísi "))
    #útreykningar
    for tel in range(veldi):#for lúppa til þess að gera þetta jafn oft og veldið segir
        summa=summa*tala
    print(tala,"í",veldi,"veldi er",summa)#úttak
    aftur=(input("Viltu keyra forrit aftur? Sláðu inn j ef já "))
    
#Liður 3
svar=int(input("Sláðu inn tölu á bilinu 1-9 "))
strengur="*"
if svar==1 or svar==2 or svar==3 or svar==4 or svar==5 or svar==6 or svar==7 or svar==8 or svar==9:
    for tel in range(1, svar+1):
        print(strengur, end="")
        strengur+="*"
        print("$")

#Liður 4
import random
random_tala=random.randint(1,50)
gisk=51
while gisk!=random_tala:
    gisk=int(input("Giskaðu á tölu á bilinu 1-50 "))
    if gisk==random_tala:
        print("Þú giskaðir rétt")
    elif gisk<random_tala:
        print("Of lágt")
    elif gisk>random_tala:
        print("Of hátt")
    else:
        print("ERROR")
