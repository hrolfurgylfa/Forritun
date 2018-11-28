'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame

pygame.init()# Byrjar pygame

# Litir
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


window_size = 640, 480# Stærð glugga
window = pygame.display.set_mode(window_size)# Býr til gluggann
fullscreen = False# Segir til um hvort leikurinn sé í fullscreen
pygame.display.set_caption('Snake')# Setir titil á gluggann

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
                pygame.display.init()
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                fullscreen = True

            elif fullscreen is True:
                pygame.display.quit()
                pygame.display.init()
                screen = pygame.display.set_mode(window_size)
                fullscreen = False

        pygame.display.update()
# Slekkur á pygame
pygame.quit()