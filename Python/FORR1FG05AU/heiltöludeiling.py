'''
Höfundur: Hrólfur Gylfason
Heiltöludeiling
'''
fj_i_lidi=7
hopur=int(input("Hvað eru margir strákar mættir á æfingu?? "))
# finna út hvað það eru mörg lið
fj_lida=hopur//fj_i_lidi
#úttak
varamenn=hopur % fj_i_lidi#Hér er ég að athuga hver afgangur deilingarinnar er
if varamenn==1:
    print("Fjöldi liða er",fj_lida,"og það er",varamenn,"varamaður")
elif varamenn==0:
    print("Fjöldi liða er",fj_lida,"og það eru engir varamenn")
else:
    print("Fjöldi liða er",fj_lida,"og það eru",varamenn,"varamenn")
tala=int(input("Sláðu inn tölu "))
if tala % 2==0:
    print("Talan er slétt tala")
if tala % 2==1:
    print("Talan er odda tala")
