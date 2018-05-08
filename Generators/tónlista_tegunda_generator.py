'''
Tónlista tegunda generator
Hrólfur Gylfason
4/5/2018
'''
import random

listi = ["Rokk","Jass","Pop","Klasísk","Dubstep","Rap","Raftónlist","Vocaloid","Country","Rokk","Jass","Pop","Klasísk","Rap","Rokk","Jass","Pop","Klasísk","Rap"]

hversu_oft = int(input("Sláðu inn hversu margar tónlistategundir þér vantar "))

for x in range(hversu_oft):
    random_numer_ur_listi = random.randint(0,len(listi)-1)
    listi.append(listi[random_numer_ur_listi])

for item in listi:
    print(item)