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

width = 1024
height = 576
window_size = width, height# Stærð glugga
pygame_tuple = byrjaPygame(window_size)
pygame = pygame_tuple[0]
window = pygame_tuple[1]
fullscreen = False

fullscreen_w = 0
fullscreen_h = 0

# Hraði
hradi = 5

# Stærð snáks
w_snakur = 15
h_snakur = 15

# Staðsetning
snakur_x = 0
snakur_y = 30

# Velocity
velocity_x = 1
velocity_y = 0

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:# Ef ýtt er á F til þess að skipta a milli fullscreen og ekki fullscreen
            if fullscreen is False:
                pygame.display.quit()
                pygame_tuple = byrjaPygame("f")
                pygame = pygame_tuple[0]
                window = pygame_tuple[1]
                fullscreen = True
                fullscreen_w, fullscreen_h = pygame.display.get_surface().get_size()

            elif fullscreen is True:
                pygame.display.quit()
                pygame_tuple = byrjaPygame(window_size)
                pygame = pygame_tuple[0]
                window = pygame_tuple[1]
                fullscreen = False

        # Hreyfa snákinn
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w or event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if velocity_x != 0:
                velocity_x = 0
                velocity_y = -1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s or event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if velocity_x != 0:
                velocity_x = 0
                velocity_y = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a or event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if velocity_y != 0:
                velocity_x = -1
                velocity_y = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d or event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if velocity_y != 0:
                velocity_x = 1
                velocity_y = 0

        # Debug
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            hradi = .1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            hradi = 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            hradi = 5

    if matur_a_bordi is False:
        if fullscreen is True:
            matur_x = random.randint(0 + w_snakur, fullscreen_w - w_snakur)
            matur_y = random.randint(0 + h_snakur, fullscreen_h - h_snakur)
            matur_a_bordi = True
        else:
            matur_x = random.randint(0 + w_snakur, width - w_snakur)
            matur_y = random.randint(0 + h_snakur, height - h_snakur)
            matur_a_bordi = True

    pygame.draw.circle(window, RED, (matur_x, matur_y), int(w_snakur / 2))
    pygame.draw.rect(window, BLACK, pygame.Rect(snakur_x, snakur_y, w_snakur, h_snakur))
    pygame.display.update()
    window.fill(WHITE)
    

    # Tékka hvort að snákurinn sé búinn að ná mat
    if snakur_x < matur_x + 30 / 2 and snakur_x > matur_x - 30 / 2:
        print("Framhjá X")
    if snakur_y < matur_y + 30 / 2 and snakur_y > matur_y - 30 / 2:
        print("Framhjá Y")

    # Tékka hvort að snákurinn sé búinn að klessa á
    if fullscreen is True:
        if snakur_x < 0 or snakur_x > fullscreen_w - w_snakur or snakur_y < 0 or snakur_y > fullscreen_h - h_snakur:
            running = False
    else:
        if snakur_x < 0 or snakur_x > width - w_snakur or snakur_y < 0 or snakur_y > height - h_snakur:
            running = False

    snakur_x += velocity_x * hradi
    snakur_y += velocity_y * hradi

    clock.tick(clock_ticks)

# Slekkur á pygame
pygame.quit()