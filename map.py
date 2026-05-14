import pygame

map = pygame.image.load("assets/rota1.png")

def load_map():
    map = pygame.image.load("assets/rota1.png").convert()
    map = pygame.transform.scale(map, (160, 160))
    return map


def draw_map(screen, map):
    screen.blit(map, (0,0))
