import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 64
        self.width = 64
        self.speed = 8

    def movimento(self, keys):
        if keys[pygame.K_w]:
            self.y += self.speed
        if keys[pygame.K_s]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x += self.speed
        if keys[pygame.K_d]:
            self.x -= self.speed

        