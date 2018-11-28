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

snakur_x = 0
snakur_y = 0

clock = pygame.time.Clock()
clock_ticks = 20

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

    pygame.draw.rect(window, RED, pygame.Rect(snakur_x, 30, 20, 10))
    pygame.display.update()
    window.fill(WHITE)

    snakur_x += 1

    clock.tick(clock_ticks)

# Slekkur á pygame
pygame.quit()