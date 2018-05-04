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