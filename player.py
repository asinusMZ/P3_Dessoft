import pygame
from spritesheet import SpriteSheet


class Player:
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.width = 16
        self.height = 16
        self.speed = 2

        self.direction = "down"
        self.frame_index = 0
        self.animation_timer = 0

        self.load_frames()

    def load_frames(self):
        sheet = SpriteSheet("assets/pokecharacters.png", (255, 127, 39))
        self.animations = {
            "down": [
                sheet.get_sprite(26, 34, 15, 15),
                sheet.get_sprite(43, 34, 15, 15),
                sheet.get_sprite(9, 34, 15, 15),
            ],

            "up": [
                sheet.get_sprite(77, 34, 15, 15),
                sheet.get_sprite(94, 34, 15, 15),
                sheet.get_sprite(60, 34, 15, 15),
            ],

            "left": [
                sheet.get_sprite(111, 34, 15, 15),
                sheet.get_sprite(128, 34, 15, 15),
            ],

            "right": [
                sheet.get_sprite(145, 34, 15, 15),
                sheet.get_sprite(162, 34, 15, 15),
            ],
        }

        # Resize all sprites to 32x32
        for direction in self.animations:
            for i in range(len(self.animations[direction])):
                self.animations[direction][i] = pygame.transform.scale(
                    self.animations[direction][i],
                    (self.width, self.height)
                )

    def move(self, keys):
        moving = False

        old_direction = self.direction

        new_x = self.x
        new_y = self.y

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            new_y -= self.speed
            self.direction = "up"
            moving = True

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            new_y += self.speed
            self.direction = "down"
            moving = True

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            new_x -= self.speed
            self.direction = "left"
            moving = True

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            new_x += self.speed
            self.direction = "right"
            moving = True

        if self.direction != old_direction:
            self.frame_index = 0

        self.x = new_x
        self.y = new_y

        if moving:
            self.animate()
        else:
            self.frame_index = 0

    def animate(self):
        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_timer = 0

            self.frame_index += 1

            if self.frame_index >= len(self.animations[self.direction]):
                self.frame_index = 0

    def draw(self, screen, camera_x=0, camera_y=0):
        current_sprite = self.animations[self.direction][self.frame_index]
        screen.blit(current_sprite, (self.x - camera_x, self.y - camera_y))
    
    def get_rect(self):
        return pygame.Rect(
            self.x + 6,
            self.y + 16,
            self.width - 12,
            self.height - 16)
    
    def gethits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits


    def checkCollisionsx(self, tiles):
        collisions = self.gethits(tiles)
        if self.velocity.x > 0:
            self.position.x = tile.rect.left - self.rect.w
            self 