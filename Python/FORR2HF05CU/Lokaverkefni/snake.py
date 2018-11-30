'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame
import random

# Litir
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def byrjaPygame(glugga_stærð):
    pygame.init()# Byrjar pygame

    if glugga_stærð != "f":
        window = pygame.display.set_mode(glugga_stærð)# Býr til gluggann
    else:
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Snake')# Setir titil á gluggann

    return (pygame, window)

width = 640
height = 480
window_size = width, height# Stærð glugga
pygame_tuple = byrjaPygame(window_size)
pygame = pygame_tuple[0]
window = pygame_tuple[1]
fullscreen = False

# Vegalengd snáks farin frá síðustu begju
vegalengd_fra_begju = 0

# Lengd snáks
lengd = 3

# Stærð snáks
snakur_w = 15
snakur_h = 15
snakur_r = 10

# Staðsetning
snakur_x = [0, 10, 20]
snakur_y = [30, 30, 30]

# Velocity
velocity_x = 1
velocity_y = 0

# Hraði leiksins
hradi = 5

tel = -1
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
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_f:# Ef ýtt er á F til þess að skipta a milli fullscreen og ekki fullscreen
            if fullscreen is False:
                pygame.display.quit()
                pygame_tuple = byrjaPygame("f")
                pygame = pygame_tuple[0]
                window = pygame_tuple[1]
                fullscreen = True
            elif fullscreen is True:
                pygame.display.quit()
                pygame_tuple = byrjaPygame(window_size)
                pygame = pygame_tuple[0]
                window = pygame_tuple[1]
                fullscreen = False

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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            meiri_lengd = True

    # if matur_a_bordi is False:
    #     matur_x = random.randint(int(0 + snakur_w / 2), int(width - snakur_w / 2))
    #     matur_y = random.randint(int(0 + snakur_h / 2), int(height - snakur_h / 2))
    #     matur_a_bordi = True

    # pygame.draw.circle(window, RED, (matur_x, matur_y), snakur_w / 2)
    
    for tel in range(lengd):
        pygame.draw.circle(window, RED, (snakur_x[tel], snakur_y[tel]), snakur_r)
        # pygame.draw.rect(window, BLACK, pygame.Rect(snakur_x, snakur_y, snakur_w, snakur_h))
        # pygame.draw.rect(window, RED, pygame.Rect(snakur_x, snakur_y, 5, 5))
    pygame.display.update()
    window.fill(WHITE)

    # Tékka hvort að snákurinn sé búinn að klessa á vegg
    if snakur_x[-1] < 0 or snakur_x[-1] > width - snakur_w or snakur_y[-1] < 0 or snakur_y[-1] > height - snakur_h:
            running = False

    snakur_x.append(int(snakur_x[-1] + velocity_x * hradi))
    snakur_y.append(int(snakur_y[-1] + velocity_y * hradi))

    if meiri_lengd is True:
        lengd += 1
        meiri_lengd = False

    while len(snakur_x) > lengd:
        snakur_x.pop(0)
    while len(snakur_y) > lengd:
        snakur_y.pop(0)

    vegalengd_fra_begju += hradi

    clock.tick(clock_ticks)

# Slekkur á pygame
pygame.quit()