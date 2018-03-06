'''
Höfundur: Hrólfur Gylfason
Æfingarverkefni 3
'''
'''
#Liður 1

#Hérna fæ ég gráðutölnua frá notandanum
gradur_i_hring=360
gradur_input=int(input("Sláðu inn gráðutölu "))
#Útreikningar
fjoldi_hringja=gradur_input//gradur_i_hring
auka_gradur=gradur_input % gradur_i_hring #Hér er ég að athuga hver afgangur deilingarinnar er
#Hérna segi ég notandanum hversu oft talans hans gengur upp í 360
if gradur_input % 360==0 and fjoldi_hringja==1:
    print("Þetta er",fjoldi_hringja,"hringur")
elif gradur_input % 360==0:
    print("Þetta eru",fjoldi_hringja,"hringir")
elif fjoldi_hringja==1:
    print("Þetta er",fjoldi_hringja,"hringur og",auka_gradur,"auka gráður")
else:
    print("Þetta eru",fjoldi_hringja,"hringir og",auka_gradur,"auka gráður")
'''
'''
#Liður 2

#Hérna fæ ég frá notanda hvað það eru margir margir mættir og hvað það eiga að vera margir í liði
hopur=int(input("Hvað eru margir strákar mættir á æfingu? "))
fj_i_lidi=int(input("hvað eiga að vera margir í liði? "))
#Útreykningar
fj_lida=hopur//fj_i_lidi
varamenn=hopur % fj_i_lidi#Hér er ég að athuga hver afgangur deilingarinnar er
#Hérna gef ég notandanum upplýsingarnar
if varamenn==1:
    print("Fjöldi liða er",fj_lida,"og það er",varamenn,"varamaður")
elif varamenn==0:
    print("Fjöldi liða er",fj_lida,"og það eru engir varamenn")
else:
    print("Fjöldi liða er",fj_lida,"og það eru",varamenn,"varamenn")
'''
'''
#Liður 3

#Hérna fæ ég sekúnturnar frá notandanum
sek_input=int(input("Sláðu inn fjölda sekúnda "))
#Útreykningar
kls=sek_input//3600#3600 sek í kls
restin=sek_input % 3600#hvað eru margar sekúndur eftir
minutur=restin//60#hvað eru margar minutur eftir
rest2=restin % 60
#Hér segi ég notandanum hversu margar kls, min og sek sekúndurnar eru
print("þetta er/u",kls,"klukkustund/ir,",minutur,"minutur og",rest2,"sekúndur")
'''
'''
#Liður 4

#Hérna fæ ég milælimetrana frá notandanum
mm_in=int(input("Sláðu inn fjölda millimetra "))
#Útreykningar
m_out=mm_in//1000
mm_eftir_m=mm_in % 1000
cm_out=mm_eftir_m//10
mm_out=mm_eftir_m % 10
#Hérna segi ég notandanum hversu margir mm cm og m þetta voru
print("Þetta eru",m_out,"metrar,",cm_out,"sentímetrar og",mm_out,"millímetrar")
'''
'''
#Liður 5

#Hérna fæ ég krónurnar frá notandanum
kr=int(input("Hvað ertu með margar krónur = "))
#Útreykningar
kr_1000_out=kr//1000
kr_eftir_1000=kr % 1000
kr_500_out=kr_eftir_1000//500
kr_eftir_500=kr_eftir_1000 % 500
kr_100_out=kr_eftir_500//100
kr_1_out=kr_eftir_500 % 100
#Úttak
print("Þetta gerir",kr_1000_out,"stk 1000 kr seðla,",kr_500_out,"stk 500kr seðla,",kr_100_out,"stk 100kr peninga og",kr_1_out,"krónur")
'''
'''
#Liður 6

#Hérna fæ ég töluna frá notandanum
tala=int(input("Sláðu inn tölu = "))
#Útreykningar og Úttak
if tala % 2==0:
    print("Þetta er slétttala")
elif tala % 2==1:
    print("Þetta er oddatala")
else:
    print("ERROR")
'''
