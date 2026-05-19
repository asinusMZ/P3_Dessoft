import pygame
from spritesheet import SpriteSheet

class NPC:
    def __init__(self, x, y, image_path=None):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16

        self.load_sprite()

    def load_sprite(self):
        sheet = SpriteSheet("assets/pokecharacters.png", (255, 127, 39))

        self.image = sheet.get_sprite(26, 306, 15, 15)

    def draw(self, surface, camera_x, camera_y):
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
