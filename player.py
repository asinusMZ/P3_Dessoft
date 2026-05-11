from pathlib import Path

print("Current folder:", Path.cwd())
print("Assets folder exists:", Path("assets").exists())

if Path("assets").exists():
    print("Files inside assets:", list(Path("assets").iterdir()))


import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3

        self.direction = "down" # IA
        self.frame_index = 0 # IA
        self.animation_timer = 0 # IA

        self.sprite_width = 16
        self.sprite_height = 21
        self.scale = 3

        self.sheet = pygame.image.load("assets/player_spritesheet.png").convert_alpha() # IA

        # Remove blue background
        self.sheet.set_colorkey((0, 0, 0)) # IA

        self.animations = {
            "down": [
                self.get_sprite(23, 30),
                self.get_sprite(39, 30),
                self.get_sprite(55, 30),
            ],
            "up": [
                self.get_sprite(23, 37),
                self.get_sprite(39, 37),
                self.get_sprite(55, 37),
            ],
            "left": [
                self.get_sprite(23, 64),
                self.get_sprite(39, 64),
                self.get_sprite(55, 64),
            ],
            "right": [
                self.get_sprite(40, 85),
                self.get_sprite(45, 85),
                self.get_sprite(50, 85),
            ],
        }

    def get_sprite(self, x, y): # IA
        sprite = pygame.Surface(
            (self.sprite_width, self.sprite_height),
            pygame.SRCALPHA
        )

        sprite.blit(
            self.sheet,
            (0, 0),
            (x, y, self.sprite_width, self.sprite_height)
        )

        sprite = pygame.transform.scale(
            sprite,
            (self.sprite_width * self.scale, self.sprite_height * self.scale)
        )

        return sprite

    def movimento(self, keys):
        movendo = False

        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "up"
            movendo = True

        elif keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "down"
            movendo = True

        elif keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "left"
            movendo = True

        elif keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "right"
            movendo = True

        if movendo:
            self.animate()
        else:
            self.frame_index = 1

    def animate(self): # IA
        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.frame_index += 1

            if self.frame_index >= len(self.animations[self.direction]):
                self.frame_index = 0

    def draw(self, screen):
        current_sprite = self.animations[self.direction][self.frame_index]
        screen.blit(current_sprite, (self.x, self.y))