'''
Höfundur: Hrólfur Gylfason
Æfingarverkefni 4
'''
#Verð, til þess að breyta þeim auðveldlega
veHrSk=3000#Herra Skyrtur
veDoSk=3500#Dömu Skyrtur
veHrBu=5000#Herra Gallabuxur
veDoBu=4700#Dömu Gallabuxur

#Til þess að það komi ekki error ef maður kaupir 0 af eitthverju
fjoHrSk=0
fjoDoSk=0
fjoHrBu=0
fjoDoBu=0

val=6#Ég setti þetta hérna vegna þess að það var alltaf að koma error sem sagði val not defined svo að ég gerði val defined með eitthverju sem gerir ekki neitt
while val!="5":#Loop þangað til ýtt er á 5
    print("1. Herra skyrtur")
    print("2. Dömu skyrtur")
    print("3. Herra buxur")
    print("4. Dömu buxur")
    print("5. Hætta og fá reikning")
    val=input("-----------------> ")
    #Hérna spyr ég notandan hversu mikið hann vill af því sem hann valdi
    if val=="1":
        fjoHrSk=int(input("Hversu margar herra skyrtur má bjóða þér? "))
    elif val=="2":
        fjoDoSk=int(input("Hversu margar dömu skyrtur má bjóða þér? "))
    elif val=="3":
        fjoHrBu=int(input("Hversu margar herra buxur má bjóða þér? "))
    elif val=="4":
        fjoDoBu=int(input("Hversu margar dömu buxur má bjóða þér? "))
    else:
        print("Error\tSláðu inn 1, 2, 3, 4 eða 5")
#Útreykningar
veHrSk_out=fjoHrSk*veHrSk
veDoSk_out=fjoDoSk*veDoSk
veHrBu_out=fjoHrBu*veHrBu
veDoBu_out=fjoDoBu*veDoBu
summa=veHrSk_out+veDoSk_out+veHrBu_out+veDoBu_out
#Hérna prenta ég út kvittunina
print("Þú hefur keypt:")
print("Herra Skyrtur=",fjoHrSk,"stk",veHrSk_out,"kr")
print("Dömu Skyrtur=",fjoDoSk,"stk",veDoSk_out,"kr")
print("Herra Buxur=",fjoHrBu,"stk",veHrBu_out,"kr")
print("Dömu Buxur=",fjoDoBu,"stk",veDoBu_out,"kr")
print("Samtals=",summa,"kr")
#kaupbæti
if summa%7==0:
    print("og þú færð súkkulaðistykki í kaupbæti")
