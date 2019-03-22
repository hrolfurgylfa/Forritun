import math

pi = float(input())

aukastafir = 0
punktur_kominn = False
for stafur in str(pi):
    if punktur_kominn == True:
        aukastafir += 1
    elif stafur == ".":
        punktur_kominn = True

if pi == round(math.pi,aukastafir):
    print("Ja, absolut!")
else:
    print("Nein, ich glaube das ist nicht PI.")