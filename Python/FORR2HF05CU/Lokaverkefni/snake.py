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

width = 1024
height = 576
window_size = width, height# Stærð glugga
pygame_tuple = byrjaPygame(window_size)
pygame = pygame_tuple[0]
window = pygame_tuple[1]
fullscreen = False

# Stærð snáks
x_snakur = 15 / 1024 * 576
y_snakur = 15 / 1024 * 576

# Staðsetning
snakur_x = 0 / 1024 * 576
snakur_y = 30 / 1024 * 576

# Velocity
velocity_x = 1 / 1024 * 576
velocity_y = 0 / 1024 * 576

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

    if matur_a_bordi is False:
        pass

    pygame.draw.rect(window, BLACK, pygame.Rect(snakur_x, snakur_y, x_snakur, y_snakur))
    pygame.display.update()
    window.fill(WHITE)

    # Tékka hvort að snákurinn sé búinn að klessa á
    if fullscreen is True:
        pass
    else:
        if snakur_x < 0 or snakur_x > width - x_snakur or snakur_y < 0 or snakur_y > height - y_snakur:
            running = False

    snakur_x += velocity_x * 5
    snakur_y += velocity_y * 5

    clock.tick(clock_ticks)

# Slekkur á pygame
pygame.quit()