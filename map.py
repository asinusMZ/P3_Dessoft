import pygame


def load_map():
    mapa = pygame.image.load("assets/rota1.png").convert()
    return mapa


def draw_map(surface, mapa, camera_x, camera_y):
    surface.blit(mapa, (-camera_x, -camera_y))