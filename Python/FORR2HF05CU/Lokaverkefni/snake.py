'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame
import random

def byrjaPygame(glugga_stærð):
    pygame.init()# Byrjar pygame

    if glugga_stærð != "f":
        window = pygame.display.set_mode(glugga_stærð)# Býr til gluggann
    else:
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Snake')# Setir titil á gluggann

    return (pygame, window)

def skrifaISkra(oll_skra):
    skra = open("stig.txt", "w")
    for lina in oll_skra:
        skra.write(str(lina[0])+";"+str(lina[1])+";\n")
    skra.close()


valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að spila")
    print("Ýttu á 2 til þess að skoða hæstu stigin")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":# Snake leikurinn sjálfur

        # Byrja glugga
        width = 640
        height = 480
        window_size = width, height# Stærð glugga
        pygame_tuple = byrjaPygame(window_size)
        pygame = pygame_tuple[0]
        window = pygame_tuple[1]
        fullscreen = False

        # Litir
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

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

        # Að gera texta
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 80)
        leturstaerd_stiga = (snakur_r/2,snakur_r/2)

        meiri_lengd = False

        matur_a_bordi = False

        clock = pygame.time.Clock()
        clock_ticks = 60

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                pygame.draw.circle(window, BLACK, (snakur_x[tel], snakur_y[tel]), snakur_r)
            
            # Teikna textann
            textsurface = myfont.render(str(stig), False, (255, 0, 0))
            window.blit(textsurface,leturstaerd_stiga)

            # Updata skjáinn
            pygame.display.update()
            window.fill(WHITE)

            # Teikna matinn
            pygame.draw.circle(window, RED, (matur_x, matur_y), snakur_r)

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

            if meiri_lengd is True:
                baeta_a_snakinn += 10
                meiri_lengd = False

            if baeta_a_snakinn > 0:
                baeta_a_snakinn -= 1
                lengd += 1

            # Þetta tekur aftasta partinn af snáknum svo að hann hreifist
            while len(snakur_x) > lengd:
                snakur_x.pop(0)
            while len(snakur_y) > lengd:
                snakur_y.pop(0)

            vegalengd_fra_begju += hradi

            clock.tick(clock_ticks)

        # Segir hversu mörgum stigum var náð
        print("Þú fékst",stig,"stig\n")

        # Slekkur á pygame
        pygame.quit()

        # Hérna fer notandinn aftur í texta forritið
        # Hérna slær notandinn inn nafnið sitt
        while True:
            nafn = input("Sláðu inn nafn til þess að vista með metinu þínu og er undir 16 stafir eða ekki skrifa neitt til þess að vista þetta ekki\n--->")
            if len(nafn) <= 15: break
            else: print("\nNafnið þarf að vera undir 16 stafir")

        if nafn != "":
            skra = open("stig.txt", "r")
            oll_nofn = []
            oll_skra = []
            for line in skra:# Þessi for lúppa setir öll nöfnin í stig.txt í listann oll_nofn og nöfnin og stigin í listann oll_skra
                lina = line.split(";")
                oll_nofn.append(lina[0])# lina[0] er nafnið í skránni
                oll_skra.append(lina[0:2])# lina[0:2] eru nafnið og stigin
            skra.close()

            if nafn not in oll_nofn:
                skra = open("stig.txt", "a")
                skra.write(nafn+";"+str(stig)+";\n")
                skra.close()
            else:
                for lina in oll_skra:
                    if lina[0] == nafn and int(lina[1]) > stig or lina[0] == nafn and int(lina[1]) == stig:
                        break
                    elif lina[0] == nafn and int(lina[1]) < stig:
                        lina[1] = stig
                        skrifaISkra(oll_skra)


    elif valmynd == "2":# Leaderboards
        try:
            skra = open("stig.txt", "r")
        except FileNotFoundError:
            skra = []
        for line in skra:
            lina = line.split(";")
            lina = lina[0:2]
            print(lina)


