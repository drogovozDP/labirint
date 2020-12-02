import pygame
import labirint

BLACK = (0, 0, 0)

pygame.init() # main settings for pygame

WIDTH, HEIGHT, FPS = 900, 700, 120
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('labirint')
clock = pygame.time.Clock()

map = labirint.Labirint(screen)
# map.dfs()

run = True # main cycle
while run:
    # clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT))
    map.step()
    # map.dfs()
    map.draw()
    pygame.display.update()
