class Nemi():
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang
        
    def __str__(self):
        return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)

class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, forradamadur, nafnSkola):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.forradamadur = forradamadur
        self.nafnSkola = nafnSkola

    def __str__(self):
        return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nForráðamaður: "+str(self.forradamadur)+"\nnafnSkóla: "+str(self.nafnSkola)

class Framhaldsskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, brautarheiti, busetustyrkur = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.brautarheiti = brautarheiti
        self.busetustyrkur = busetustyrkur

    def __str__(self):
        if busetustyrkur is not False:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nbrautarheiti: "+str(self.brautarheiti)+"\nbusetustyrkur: "+str(self.busetustyrkur)+"kr."
        else:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nbrautarheiti: "+str(self.brautarheiti)+"\nbusetustyrkur: Nei"

class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, stigNams, namslan = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.stigNams = stigNams
        self.namslan = namslan

    def __str__(self):
        if namslan is not False:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nstig náms: "+str(self.stigNams)+"\nnámslán: "+str(self.namslan)+"kr."
        else:
            return "Kennitala: "+str(self.kt)+"\nNafn: "+str(self.nafn)+"\nKyn: "+str(self.kyn)+"\nHeimilisfang: "+str(self.heimilisfang)+"\nSímanúmer: "+str(self.simanumer)+"\nNetfang: "+str(self.netfang)+"\nstig náms: "+str(self.stigNams)+"\nnámslán: Nei"

