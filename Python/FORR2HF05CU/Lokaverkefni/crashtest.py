'''
PyGame Crash test
Hrólfur Gylfason
7/12/2018
'''
import pygame
from time import sleep

for x in range(100):
    pygame.init()
    window_size = 640, 480
    window = pygame.display.set_mode(window_size)
    print("Opnað")
    pygame.quit()
    print("Lokað")