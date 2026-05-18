import pygame

rosa = (240, 0, 255)
amarelo = (251, 255, 0)
verde = (0, 255, 0)


def load_map():
    mapa = pygame.image.load("assets/rota1.png").convert()
    return mapa

def load_mask():
    return pygame.image.load("assets/rota1masks.png").convert()


def draw_map(surface, mapa, camera_x, camera_y):
    surface.blit(mapa, (-camera_x, -camera_y))

def get_mask_color(mask, x, y): 
    if x < 0 or y < 0 or x >= mask.get_width() or y >= mask.get_height(): 
        return rosa
    
    color = mask.get_at((int(x), int(y))) 
    return color[:3]

def is_collision(mask, rect): 
    pontos = [
        rect.topleft,
        rect.topright,
        rect.bottomleft,
        rect.bottomright,
        rect.center,
        rect.midbottom,
        rect.midtop,
        rect.midleft,
        rect.midright,
    ]
    for x, y in pontos: 
        if get_mask_color(mask, x, y) == rosa: 
            return True 
        return False
    
def is_grama(mask, rect): 
    center_x = rect.centerx 
    center_y = rect.centery 
    return get_mask_color(mask, center_x, center_y) == verde