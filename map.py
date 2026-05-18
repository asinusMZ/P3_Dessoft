import pygame

map = pygame.image.load("assets/rota1.png")

def load_map():
    map = pygame.image.load("assets/rota1.png").convert()
    return map


def draw_map(screen, map):
    screen.blit(map, (0,0))
