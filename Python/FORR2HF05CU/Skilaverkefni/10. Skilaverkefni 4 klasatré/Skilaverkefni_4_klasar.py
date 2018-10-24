class Nemi():
    __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang
        
    __str__(self):
        pass

class Grunnskolanemi(Nemi):
    __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, forradamadur, nafnSkola):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.forradamadur = forradamadur
        self.nafnSkola = nafnSkola

    __str__(self):
        pass

class Framhaldsskolanemi(Nemi):
    __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, brautarheiti, busetustyrkur = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.brautarheiti = brautarheiti
        self.busetustyrkur = busetustyrkur

    __str__(self):
        pass

class Haskolanemi(Nemi):
    __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, stigNams, namslan = False):
        Nemi.__init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.stigNams = stigNams
        self.namslan = namslan

    __str__(self):
        pass

