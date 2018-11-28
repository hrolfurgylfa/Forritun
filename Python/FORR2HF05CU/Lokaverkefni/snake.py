'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame

# Litir
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def byrjaPygame(glugga_stærð):
    pygame.init()# Byrjar pygame

    if glugga_stærð != "f":
        window = pygame.display.set_mode(glugga_stærð)# Býr til gluggann
    else:
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Snake')# Setir titil á gluggann
    window.fill(WHITE)

    return pygame

window_size = 640, 480# Stærð glugga
byrjaPygame(window_size)
fullscreen = False

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
                pygame = byrjaPygame("f")
                fullscreen = True
            elif fullscreen is True:
                pygame.display.quit()
                pygame = byrjaPygame(window_size)
                fullscreen = False

        pygame.display.update()

# Slekkur á pygame
pygame.quit()