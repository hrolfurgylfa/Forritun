'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame

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

window_size = 640, 480# Stærð glugga
pygame_tuple = byrjaPygame(window_size)
pygame = pygame_tuple[0]
window = pygame_tuple[1]
fullscreen = False

# Staðsetning
snakur_x = 0
snakur_y = 30

# Velocity
velocity_x = 1
velocity_y = 0

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

    pygame.draw.rect(window, RED, pygame.Rect(snakur_x, snakur_y, 15, 15))
    pygame.display.update()
    window.fill(WHITE)

    snakur_x += velocity_x * 5
    snakur_y += velocity_y * 5

    clock.tick(clock_ticks)

# Slekkur á pygame
pygame.quit()