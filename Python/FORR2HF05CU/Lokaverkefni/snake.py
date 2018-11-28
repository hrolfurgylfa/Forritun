'''
Lokaverkefni
Hrólfur Gylfason
28/11/2018
'''
import pygame

pygame.init()# Byrjar pygame

# Stærð glugga
window_size = 640, 480
# Býr til gluggann
window = pygame.display.set_mode(window_size)
# Segir til um hvort leikurinn sé í fullscreen
fullscreen = False
# Setir titil á gluggann
pygame.display.set_caption('Snake')

running = True  # loop control variable(for the game loop)

while running:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Ef ýtt er á Esc
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        # Ef ýtt er á F til þess að skipta a milli fullscreen og ekki fullscreen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
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

# Slekkur á pygame
pygame.quit()