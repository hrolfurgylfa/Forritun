'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame
import random
import sys

skraarnafn = "gameFiles/stig.txt"
nafn_fonts = "gameFiles/Ubuntu-R.ttf"

def skrifaIStigaSkra(oll_skra):# Þetta fall skrifar lista í stiga skránna
    skra = open(skraarnafn, "w")
    for lina in oll_skra:
        skra.write(str(lina[0])+";"+str(lina[1])+";\n")
    skra.close()

def haetta():# Þetta slekkur á forritinu
    pygame.quit()
    sys.exit()

def faStigaSkra():# Þetta sækir stigaskránna og skilar henni í lista
    allt = []

    try:
        skra = open(skraarnafn, "r")
        for line in skra:
            lina = line.split(";")
            allt.append(lina[0:2])
        skra.close()
    except FileNotFoundError:
        pass
    
    return allt

def faBestuSpilara():# Þetta fall skilar núverandi notanda með hæstu stigin eða notendum með hæstu stigin ef nokkrir eru jafnir
    stiga_listi = faStigaSkra()# Sækir stiga listann úr fallinu faStigaSkra

    haestu_stig_listi = []
    haestu_stig = -1

    for met in stiga_listi:# Fer yfir öll metin í listanum stiga_listi
        if int(met[1]) > haestu_stig:# Þetta gerist ef forritið finnur nýjan meistara
            haestu_stig_listi = []# Hreinsar listann
            haestu_stig_listi.append(met)# Bætir metinu sem for lúppan er á núna í hreinsaða listann
            haestu_stig = int(met[1])# Breitir tölunni sem segir hvað hæstu stigin eru í hæsta stig metsins sem for lúppan er á núna

        elif int(met[1]) == haestu_stig:# Þetta gerist ef það jafnar eitthver núverandi meistara
            haestu_stig_listi.append(met)# Bætir núverandi meti í listann

    return haestu_stig_listi

valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    # Þetta sýnir notandann með hæstu stigin
    haestu_spilarar = faBestuSpilara()
    
    if len(haestu_spilarar) == 1:# Þetta gerist ef það er einn notandi með metið
        nafn = str(haestu_spilarar[0][0])
        stig = str(haestu_spilarar[0][1])

        print(nafn+" er með metið og er með "+stig+" stig")

    elif len(haestu_spilarar) == 2:# Þetta gerist ef það eru tveir notendur með metið
        nafn = str(haestu_spilarar[0][0])
        nafn2 = str(haestu_spilarar[1][0])
        stig = str(haestu_spilarar[0][1])

        print(nafn+" og "+nafn2+" eru með metið og eru með "+stig+" stig")

    elif len(haestu_spilarar) >= 3:# Þetta gerist ef það eru þrír eða fleiri notendur með metið
        n_listi = []# n stendur fyrir nafna
        stig = str(haestu_spilarar[0][1])

        for i in haestu_spilarar:
            nafn = str(i[0])
            n_listi.append(nafn)
        
        print(n_listi[0],end="")

        for i in range(1, len(n_listi) -1):
            print(", "+n_listi[i],end="")
        
        print(" og "+n_listi[-1]+" eru með metið og eru með "+stig+" stig")

    print()#Þetta er til þess að gera enter
        

    print("Ýttu á 1 til þess að spila")
    print("Ýttu á 2 til þess að skoða hæstu stigin")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":# Snake leikurinn sjálfur
        
        # Setja breytur til þess að geta byrjað glugann
        width = 640
        height = 480
        window_size = width, height# Stærð glugga

        # Byrja glugga
        pygame.init()# Byrjar pygame
        window = pygame.display.set_mode(window_size)# Býr til gluggann
        pygame.display.set_caption('Snake')# Setir titil á gluggann

        # Litir
        bakgrunnslitur = (255, 255, 255)
        litur_snaks = (0, 0, 0)
        litur_mats = (255, 0, 0)
        litur_byrjunartexta = (0, 0, 0)
        litur_stigatexta = (0, 0, 255)

        # Stig
        stig = 0

        # Hversu miklu á eftir að bæta á snákinn
        baeta_a_snakinn = 0

        # Vegalengd snáks farin frá síðustu begju
        vegalengd_fra_begju = 0

        # Lengd snáks
        lengd = 10

        # Stærð snáks
        snakur_w = 15
        snakur_h = 15
        snakur_r = 10

        # Staðsetning
        snakur_x = [x*10 for x in range(lengd)]
        snakur_y = [30 for x in range(lengd)]

        # Velocity
        velocity_x = 1
        velocity_y = 0

        # Hraði leiksins
        hradi = 5

        # Initializa letrið
        pygame.font.init()

        # Að gera texta fyrir stigateljara
        stigateljari_letur = pygame.font.Font(nafn_fonts, 60)# Leturgerð fyrir stigateljarann gerð
        leturstaerd_stiga = (snakur_r/2,snakur_r/2)# Leturstærð stiga reiknað

        # Að gera texta fyrir byrjunartexta
        skilabod = "Ýttu á enter til þess að byrja"# Texti byrjunarskilaboða búinn til til þess að ég geti mælt hann og renderað hann án þess að skrifa hann tvisvar
        byrjunarskilabod_letur = pygame.font.Font(nafn_fonts, 40)# Leturgerð fyrir byrjunartextann gerð
        textsurface_byrjunarskilabod = byrjunarskilabod_letur.render(skilabod, False, litur_byrjunartexta)# Byrjunarskilaboð renderuð
        text_width, text_height = byrjunarskilabod_letur.size(skilabod)# Náð stærð byrjunarskilaboða
        byrjunartexta_stadsetning = ((width/2)-(text_width/2), (height/2)-(text_height/2))# Staðsetning byrjunarskilaboða reiknuð

        # Eftir að commenta
        meiri_lengd = False# Þetta verður true einu sinni til þess að stækka við snákinn

        matur_a_bordi = False# Þetta er True þegar það er matur á borðinu en svo þegar snákurinn borðar mat þá verður þetta False og þá kemur matur inná völlinn á næsta ramma

        clock = pygame.time.Clock()# Þetta kveikir á klukkunni
        clock_ticks = 60# Þetta eru rammarnir sem koma á sekúntu

        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
                if event.type == pygame.QUIT:
                    haetta()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    haetta()

            # Teikna byrjunartextann
            window.blit(textsurface_byrjunarskilabod,byrjunartexta_stadsetning)

            # Updata skjáinn
            pygame.display.update()
            window.fill(bakgrunnslitur)

            clock.tick(10)

        running = True

        while running:# Þar sem leikurinn sjálfur keyrir
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    haetta()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:# Ef ýtt er á Esc
                    running = False

                # Hreyfa snákinn
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w or event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if velocity_x != 0 and vegalengd_fra_begju > 10:
                        velocity_x = 0
                        velocity_y = -1
                        vegalengd_fra_begju = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s or event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if velocity_x != 0 and vegalengd_fra_begju > 10:
                        velocity_x = 0
                        velocity_y = 1
                        vegalengd_fra_begju = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    if velocity_y != 0 and vegalengd_fra_begju > 10:
                        velocity_x = -1
                        velocity_y = 0
                        vegalengd_fra_begju = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d or event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    if velocity_y != 0 and vegalengd_fra_begju > 10:
                        velocity_x = 1
                        velocity_y = 0
                        vegalengd_fra_begju = 0

            # Bæta við mat fyrir snákinn ef hann er búinn að borða síðasta mat
            if matur_a_bordi is False:
                matur_x = random.randint(0 + snakur_w, width - snakur_w)
                matur_y = random.randint(0 + snakur_h, height - snakur_h)
                matur_a_bordi = True

            # Teikna snákinn
            for tel in range(lengd):
                pygame.draw.circle(window, litur_snaks, (snakur_x[tel], snakur_y[tel]), snakur_r)
            
            # Teikna textann
            textsurface = stigateljari_letur.render(str(stig), False, litur_stigatexta)
            window.blit(textsurface,leturstaerd_stiga)

            # Updata skjáinn
            pygame.display.update()
            window.fill(bakgrunnslitur)

            # Teikna matinn
            pygame.draw.circle(window, litur_mats, (matur_x, matur_y), snakur_r)

            # Tékka hvort að snákurinn sé búinn að ná mat
            if snakur_x[-1] < matur_x + snakur_r*2 and snakur_x[-1] > matur_x - snakur_r*2 and snakur_y[-1] < matur_y + snakur_r*2 and snakur_y[-1] > matur_y - snakur_r*2:
                    matur_a_bordi = False
                    meiri_lengd = True
                    stig += 1
            
            # Tékka hvort að snákurinn sé búinn að klessa á vegg
            if snakur_x[-1] < 0 + snakur_w or snakur_x[-1] > width - snakur_w or snakur_y[-1] < 0 + snakur_h or snakur_y[-1] > height - snakur_h:
                running = False
            
            # Tékka hvort að snákurinn sé búinn að bíta í sig
            for i in range(0, lengd - 10):
                if snakur_x[i] < snakur_x[-1] + snakur_r * 2 and snakur_x[i] > snakur_x[-1] - snakur_r * 2:
                    if snakur_y[i] < snakur_y[-1] + snakur_r * 2 and snakur_y[i] > snakur_y[-1] - snakur_r * 2:
                        running = False

            # Þetta færir snákinn áfram
            snakur_x.append(int(snakur_x[-1] + velocity_x * hradi))
            snakur_y.append(int(snakur_y[-1] + velocity_y * hradi))

            # Þetta bætir 10 við breytuna baeta_a_snakinn
            if meiri_lengd is True:
                baeta_a_snakinn += 10
                meiri_lengd = False

            # Þetta bætir rólega við á snákinn (einn hring í einu) og lækkar baeta_a_snakin um einn með
            if baeta_a_snakinn > 0:
                baeta_a_snakinn -= 1
                lengd += 1

            # Þetta tekur aftasta partinn af snáknum svo að hann hreifist
            while len(snakur_x) > lengd:
                snakur_x.pop(0)
            while len(snakur_y) > lengd:
                snakur_y.pop(0)

            # Þetta er til þess að snákurinn geti ekki bitið í sig
            vegalengd_fra_begju += hradi

            clock.tick(clock_ticks)

        # Segir hversu mörgum stigum var náð
        print("Þú fékst",stig,"stig\n")

        # LAUSN FUNDIN VIÐ Segmentation fault (core dumped) Crasi!!!!!!!
        # Að hreinsa letrið, þetta hreinsar letrið sem ég nota og þetta gerir það að verkum að forritið crashar ekki vegna þess að það má ekki snerta við þessu (hvorki reassigna né hreinsa) eftir að það er búið að loka pygame-ið sem þetta var opnað í en það er hægt að hreinsa þetta á meðan það er ekki býið að loka pygame
        stigateljari_letur = None
        byrjunarskilabod_letur = None
        
        # Slekkur á pygame
        pygame.quit()

        # Hérna fer notandinn aftur í texta forritið
        # Hérna slær notandinn inn nafnið sitt
        while True:# Þetta fær nafn síðasta spilara
            nafn = input("Sláðu inn nafn til þess að vista með metinu þínu og er undir 12 stafir eða ekki skrifa neitt til þess að vista þetta ekki\n--->")
            if len(nafn) < 12: break # Þetta heldur áfram ef það sem var slegið inn var undir 12
            else: print("\nNafnið þarf að vera undir 16 stafir")

        if nafn != "":# Þetta er til þess að ef maður ýtir bara á enter þá er ekki sett neitt nafn í skránna
            oll_nofn = []
            oll_skra = []
            try:# Þetta er til þess að þegar skráin er ekki til þá býr forritið til nýja skrá
                skra = open(skraarnafn, "r")
                for line in skra:# Þessi for lúppa setir öll nöfnin í stig.txt í listann oll_nofn og nöfnin og stigin í listann oll_skra
                    lina = line.split(";")
                    oll_nofn.append(lina[0])# lina[0] er nafnið í skránni
                    oll_skra.append(lina[0:2])# lina[0:2] eru nafnið og stigin
                skra.close()
            except FileNotFoundError:# Þetta gerist ef skráin er ekki til núþegar
                pass

            if nafn not in oll_nofn:# Þetta gerist ef þessi notandi hefur ekki spilað núþegar og bætir honum þá við í skránna
                skra = open(skraarnafn, "a")
                skra.write(nafn+";"+str(stig)+";\n")
                skra.close()
            else:# Þetta gerist ef notandinn hefur núþegar spilað og þá tékkar tölvan hvort að stigin sem notandinn var að fá núna séu hærri en þau sem voru þar áður og ef þau eru hærri skiptir hann þeim út, annars gerist ekki neitt
                for lina in oll_skra:
                    if lina[0] == nafn and int(lina[1]) > stig or lina[0] == nafn and int(lina[1]) == stig:
                        break
                    elif lina[0] == nafn and int(lina[1]) < stig:
                        lina[1] = stig
                        skrifaIStigaSkra(oll_skra)


    elif valmynd == "2":# Leaderboards
        stiga_listi = faStigaSkra()# Þetta sækir öll stigin
        print("Nafn\t\tStig")# Þetta prentar fyrirsögnina
        for met in stiga_listi:# Þetta tékkar á hverju meti hversu langt nafnið sé og setir paslega mörg tab met til þess að stigin séu alltaf í sama dálk
            if len(str(met[0])) < 8:
                print(str(met[0])+"\t\t"+str(met[1]))

            elif len(str(met[0])) < 12:
                print(str(met[0])+"\t"+str(met[1]))

            else:
                print(str(met[0])+" "+str(met[1]))

