import pygame

class SpriteSheet:
    def __init__(self, image_path, background_color=None):
        self.image = pygame.image.load(image_path).convert()

        if background_color != None:
            self.image.set_colorkey(background_color)

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.image, (0, 0), (x, y, width, height))
        return sprite