class Nemi():
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang
        
    def __str__(self):#__str__ föll prentast út þegar maður reynir að prenta tilvik af klasanum
        return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)

    def netfang_get(self):#skilar self.netfang ef það er @ í netfanginu
        netfang = self.netfang

        rett_netfang = False
        for stafur in netfang:
            if stafur == "@":
                rett_netfang = True
        
        if rett_netfang is not True:
            return "Rangt netfang"

        return netfang

    def netfang_set(self, netfang):#breytir self.netfang í netfang færibreytuna ef það er @ í færibreytunni netfang
        rett_netfang = False
        for stafur in netfang:
            if stafur == "@":
                rett_netfang = True
        
        if rett_netfang is not True:
            return False

        self.netfang = netfang

class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, forradamadur, nafnSkola):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)#Þetta initialize-ar allt úr klasanum Nemi
        self.forradamadur = forradamadur
        self.nafnSkola = nafnSkola

    def forradamadur_get(self):#skilar self.forradamadur
        return self.forradamadur
    
    def forradamadur_set(self, forradamadur):#breytir self.forradamadur í breytuna forradamadur sem kemur inn sem færibreyta
        self.forradamadur = forradamadur

    def __str__(self):#Svipað og sama fall í Nemi nema með fleiri hlutum í
        return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nForráðamaður: "+str(self.forradamadur)+"\nnafnSkóla: "+str(self.nafnSkola)

class Framhaldsskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, brautarheiti, busetustyrkur = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)#Þetta initialize-ar allt úr klasanum Nemi
        self.brautarheiti = brautarheiti
        self.busetustyrkur = busetustyrkur

    def brautarheiti_get(self):#skilar self.brautarheiti
        return self.brautarheiti

    def brautarheiti_set(self, brautarheiti):#breytir self.brautarheiti í færibreytuna brautarheiti
        self.brautarheiti = brautarheiti

    def __str__(self):#Þetta fall virkar eins og í klasanum nema þetta prentar út nei ef busetustyrkur er false en annars busetustyrkur og bætir við kr. fyrir aftan töluna
        if self.busetustyrkur is not False:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nbrautarheiti: "+str(self.brautarheiti)+"\nbusetustyrkur: "+str(self.busetustyrkur)+"kr."
        else:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nbrautarheiti: "+str(self.brautarheiti)+"\nbusetustyrkur: Nei"

class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, stigNams, namslan = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)#Þetta initialize-ar allt úr klasanum Nemi
        self.stigNams = stigNams
        self.namslan = namslan

    def namslan_get(self):#skilar "Nei ef self.namslan er false en annars skilar þetta namslan sem heiltölu"
        if self.namslan is False:
            return "Nei"
        else:
            return int(namslan)

    def namslan_set(self, namslan):#gerir self.namslan að false ef færibreytan er "Nei" en annars verður self.namslan að færibreytunni namslan
        if namslan == "Nei":
            self.namslan = False
        else:
            self.namslan = namslan

    def __str__(self):#Þetta fall virkar eins og í klasanum nema þetta prentar út nei ef namslan er false en annars namslan og bætir við kr. fyrir aftan töluna
        if self.namslan is not False:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nstig náms: "+str(self.stigNams)+"\nnámslán: "+str(self.namslan)+"kr."
        else:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nstig náms: "+str(self.stigNams)+"\nnámslán: Nei"
