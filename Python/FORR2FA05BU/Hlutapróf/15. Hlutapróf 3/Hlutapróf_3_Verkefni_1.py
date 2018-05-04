import random

def bua_til_lista(random_min, random_max, fjoldi=200):
    listi = []
    for x in range(fjoldi):
        listi.append(random.randint(random_min,random_max))
    return listi

def syna_lista(tolulisti):
    tel = 0
    for tala in tolulisti:
        if tel != len(tolulisti)-1:
            print(tala,end=":")
            tel += 1
        else:
            print(tala)
            break

def summa_og_medaltal(tolulisti):
    print("Heildarsumma:",sum(tolulisti))
    return round(sum(tolulisti)/len(tolulisti),3)

def deilanlegt_med_5_og_8(tolulisti):
    for tala in tolulisti:
        if tala % 5 == 0 or tala % 8 == 0:
            print(tala,end="\t")
    print()

def skila_bili(tolulisti, fra, til):
    listi = []
    for tala in tolulisti:
        if tala >= fra and tala <= til:
            listi.append(tala)
    return listi

listi1 = bua_til_lista(100,200)
syna_lista(listi1)
print("Meðaltal:",summa_og_medaltal(listi1))

print()

listi2 = bua_til_lista(1,50,50)
deilanlegt_med_5_og_8(listi2)
print(skila_bili(listi2,21,30))

print()#SKIPTING ÚR 1 Í 2
print()#SKIPTING ÚR 1 Í 2
print()#SKIPTING ÚR 1 Í 2

class FyrstiKlasi:
    def utreikningur(tala_1,tala_2,tala_3,tala_4):
        return round((tala_1*tala_2*tala_3*tala_4)/3,2)

class AnnarKlasi:
    def __init__(self,nafn_lids,fjoldi_stiga):
        self.nafn_lids = nafn_lids
        self.fjoldi_stiga = fjoldi_stiga
    
    def setning(self):
        print("Ég er í",self.nafn_lids,"og skoraði",self.fjoldi_stiga,"stig")

h1 = FyrstiKlasi
h2 = AnnarKlasi("Breiðablik",5)

print(h1.utreikningur(4,7,5,2))
h2.setning()